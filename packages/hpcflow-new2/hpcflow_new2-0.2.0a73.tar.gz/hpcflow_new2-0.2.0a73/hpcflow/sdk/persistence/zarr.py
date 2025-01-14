from __future__ import annotations
from contextlib import contextmanager

import copy
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple, Union
import warnings

from fsspec.implementations.zip import ZipFileSystem
import numpy as np
from rich.console import Console

from hpcflow.sdk.core.errors import (
    MissingParameterData,
    MissingStoreEARError,
    MissingStoreElementError,
    MissingStoreElementIterationError,
    MissingStoreTaskError,
)
from hpcflow.sdk.core.utils import ensure_in, get_relative_path, set_in_container
from hpcflow.sdk.persistence.base import (
    PersistentStoreFeatures,
    PersistentStore,
    StoreEAR,
    StoreElement,
    StoreElementIter,
    StoreParameter,
    StoreTask,
)
from hpcflow.sdk.persistence.store_resource import ZarrAttrsStoreResource
from hpcflow.sdk.persistence.utils import ask_pw_on_auth_exc
from hpcflow.sdk.persistence.pending import CommitResourceMap

from numcodecs import MsgPack, VLenArray

import zarr


def _encode_numpy_array(obj, type_lookup, path, root_group, arr_path):
    # Might need to generate new group:
    param_arr_group = root_group.require_group(arr_path)
    names = [int(i.split("arr_")[1]) for i in param_arr_group.keys()]
    if not names:
        new_idx = 0
    else:
        new_idx = max(names) + 1
    param_arr_group.create_dataset(name=f"arr_{new_idx}", data=obj)
    type_lookup["arrays"].append([path, new_idx])

    return len(type_lookup["arrays"]) - 1


def _decode_numpy_arrays(obj, type_lookup, path, arr_group, dataset_copy):
    for arr_path, arr_idx in type_lookup["arrays"]:
        try:
            rel_path = get_relative_path(arr_path, path)
        except ValueError:
            continue

        dataset = arr_group.get(f"arr_{arr_idx}")
        if dataset_copy:
            dataset = dataset[:]

        if rel_path:
            set_in_container(obj, rel_path, dataset)
        else:
            obj = dataset

    return obj


def _encode_masked_array(obj, type_lookup, path, root_group, arr_path):
    data_idx = _encode_numpy_array(obj.data, type_lookup, path, root_group, arr_path)
    mask_idx = _encode_numpy_array(obj.mask, type_lookup, path, root_group, arr_path)
    type_lookup["masked_arrays"].append([path, [data_idx, mask_idx]])


def _decode_masked_arrays(obj, type_lookup, path, arr_group, dataset_copy):
    for arr_path, (data_idx, mask_idx) in type_lookup["masked_arrays"]:
        try:
            rel_path = get_relative_path(arr_path, path)
        except ValueError:
            continue

        data = arr_group.get(f"arr_{data_idx}")
        mask = arr_group.get(f"arr_{mask_idx}")
        dataset = np.ma.core.MaskedArray(data=data, mask=mask)

        if rel_path:
            set_in_container(obj, rel_path, dataset)
        else:
            obj = dataset

    return obj


def append_items_to_ragged_array(arr, items):
    """Append an array to a Zarr ragged array.

    I think `arr.append([item])` should work, but does not for some reason, so we do it
    here by resizing and assignment."""
    num = len(items)
    arr.resize((len(arr) + num))
    for idx, i in enumerate(items):
        arr[-(num - idx)] = i


@dataclass
class ZarrStoreTask(StoreTask):
    def encode(self) -> Tuple[int, np.ndarray, Dict]:
        """Prepare store task data for the persistent store."""
        wk_task = {"id_": self.id_, "element_IDs": np.array(self.element_IDs)}
        task = {"id_": self.id_, **self.task_template}
        return self.index, wk_task, task

    @classmethod
    def decode(cls, task_dat: Dict) -> ZarrStoreTask:
        """Initialise a `StoreTask` from persistent task data"""
        task_dat["element_IDs"] = task_dat["element_IDs"].tolist()
        return super().decode(task_dat)


@dataclass
class ZarrStoreElement(StoreElement):
    def encode(self, attrs: Dict) -> List:
        """Prepare store elements data for the persistent store.

        This method mutates `attrs`.
        """
        elem_enc = [
            self.id_,
            self.index,
            self.es_idx,
            [[ensure_in(k, attrs["seq_idx"]), v] for k, v in self.seq_idx.items()],
            [[ensure_in(k, attrs["src_idx"]), v] for k, v in self.src_idx.items()],
            self.task_ID,
            self.iteration_IDs,
        ]
        return elem_enc

    @classmethod
    def decode(cls, elem_dat: List, attrs: Dict) -> ZarrStoreElement:
        """Initialise a `StoreElement` from persistent element data"""
        obj_dat = {
            "id_": elem_dat[0],
            "index": elem_dat[1],
            "es_idx": elem_dat[2],
            "seq_idx": {attrs["seq_idx"][k]: v for (k, v) in elem_dat[3]},
            "src_idx": {attrs["src_idx"][k]: v for (k, v) in elem_dat[4]},
            "task_ID": elem_dat[5],
            "iteration_IDs": elem_dat[6],
        }
        return cls(is_pending=False, **obj_dat)


@dataclass
class ZarrStoreElementIter(StoreElementIter):
    def encode(self, attrs: Dict) -> List:
        """Prepare store element iteration data for the persistent store.

        This method mutates `attrs`.
        """
        iter_enc = [
            self.id_,
            self.element_ID,
            [[k, v] for k, v in self.EAR_IDs.items()] if self.EAR_IDs else None,
            [
                [ensure_in(dk, attrs["parameter_paths"]), dv]
                for dk, dv in self.data_idx.items()
            ],
            [ensure_in(i, attrs["schema_parameters"]) for i in self.schema_parameters],
            [[ensure_in(dk, attrs["loops"]), dv] for dk, dv in self.loop_idx.items()],
        ]
        return iter_enc

    @classmethod
    def decode(cls, iter_dat: List, attrs: Dict) -> StoreElementIter:
        """Initialise a `StoreElementIter` from persistent element iteration data"""
        obj_dat = {
            "id_": iter_dat[0],
            "element_ID": iter_dat[1],
            "EAR_IDs": {i[0]: i[1] for i in iter_dat[2]} if iter_dat[2] else None,
            "data_idx": {attrs["parameter_paths"][i[0]]: i[1] for i in iter_dat[3]},
            "schema_parameters": [attrs["schema_parameters"][i] for i in iter_dat[4]],
            "loop_idx": {i[0]: i[1] for i in iter_dat[5]},
        }
        return cls(is_pending=False, **obj_dat)


@dataclass
class ZarrStoreEAR(StoreEAR):
    def encode(self, attrs: Dict, ts_fmt: str) -> Tuple[List, Tuple[np.datetime64]]:
        """Prepare store EAR data for the persistent store.

        This method mutates `attrs`.
        """
        EAR_enc = [
            self.id_,
            self.elem_iter_ID,
            self.action_idx,
            [
                [ensure_in(dk, attrs["parameter_paths"]), dv]
                for dk, dv in self.data_idx.items()
            ],
            self.submission_idx,
            self.skip,
            self.success,
            self._encode_datetime(self.start_time, ts_fmt),
            self._encode_datetime(self.end_time, ts_fmt),
            self.snapshot_start,
            self.snapshot_end,
            self.exit_code,
            self.metadata,
        ]
        return EAR_enc

    @classmethod
    def decode(cls, EAR_dat: List, attrs: Dict, ts_fmt: str) -> ZarrStoreEAR:
        """Initialise a `ZarrStoreEAR` from persistent EAR data"""
        obj_dat = {
            "id_": EAR_dat[0],
            "elem_iter_ID": EAR_dat[1],
            "action_idx": EAR_dat[2],
            "data_idx": {attrs["parameter_paths"][i[0]]: i[1] for i in EAR_dat[3]},
            "submission_idx": EAR_dat[4],
            "skip": EAR_dat[5],
            "success": EAR_dat[6],
            "start_time": cls._decode_datetime(EAR_dat[7], ts_fmt),
            "end_time": cls._decode_datetime(EAR_dat[8], ts_fmt),
            "snapshot_start": EAR_dat[9],
            "snapshot_end": EAR_dat[10],
            "exit_code": EAR_dat[11],
            "metadata": EAR_dat[12],
        }
        return cls(is_pending=False, **obj_dat)


@dataclass
class ZarrStoreParameter(StoreParameter):
    _encoders = {  # keys are types
        np.ndarray: _encode_numpy_array,
        np.ma.core.MaskedArray: _encode_masked_array,
    }
    _decoders = {  # keys are keys in type_lookup
        "arrays": _decode_numpy_arrays,
        "masked_arrays": _decode_masked_arrays,
    }

    def encode(self, root_group: zarr.Group, arr_path: str) -> Dict[str, Any]:
        return super().encode(root_group=root_group, arr_path=arr_path)

    @classmethod
    def decode(
        cls,
        id_: int,
        data: Union[None, Dict],
        source: Dict,
        arr_group: zarr.Group,
        path: Optional[List[str]] = None,
        dataset_copy: bool = False,
    ) -> Any:
        return super().decode(
            id_=id_,
            data=data,
            source=source,
            path=path,
            arr_group=arr_group,
            dataset_copy=dataset_copy,
        )


class ZarrPersistentStore(PersistentStore):
    _name = "zarr"
    _features = PersistentStoreFeatures(
        create=True,
        edit=True,
        jobscript_parallelism=True,
        EAR_parallelism=True,
        schedulers=True,
        submission=True,
    )

    _store_task_cls = ZarrStoreTask
    _store_elem_cls = ZarrStoreElement
    _store_iter_cls = ZarrStoreElementIter
    _store_EAR_cls = ZarrStoreEAR
    _store_param_cls = ZarrStoreParameter

    _param_grp_name = "parameters"
    _param_base_arr_name = "base"
    _param_sources_arr_name = "sources"
    _param_user_arr_grp_name = "arrays"
    _param_data_arr_grp_name = lambda _, param_idx: f"param_{param_idx}"
    _task_arr_name = "tasks"
    _elem_arr_name = "elements"
    _iter_arr_name = "iters"
    _EAR_arr_name = "runs"
    _time_res = "us"  # microseconds; must not be smaller than micro!

    _res_map = CommitResourceMap(commit_template_components=("attrs",))

    def __init__(self, app, workflow, path, fs) -> None:
        self._zarr_store = None  # assigned on first access to `zarr_store`
        self._resources = {
            "attrs": ZarrAttrsStoreResource(
                app, name="attrs", open_call=self._get_root_group
            ),
        }
        super().__init__(app, workflow, path, fs)

    @contextmanager
    def cached_load(self) -> Iterator[Dict]:
        """Context manager to cache the root attributes."""
        with self.using_resource("attrs", "read") as attrs:
            yield attrs

    def remove_replaced_dir(self) -> None:
        with self.using_resource("attrs", "update") as md:
            if "replaced_workflow" in md:
                self.logger.debug("removing temporarily renamed pre-existing workflow.")
                self.remove_path(md["replaced_workflow"], self.fs)
                md["replaced_workflow"] = None

    def reinstate_replaced_dir(self) -> None:
        with self.using_resource("attrs", "read") as md:
            if "replaced_workflow" in md:
                self.logger.debug(
                    "reinstating temporarily renamed pre-existing workflow."
                )
                self.rename_path(md["replaced_workflow"], self.path, self.fs)

    @staticmethod
    def _get_zarr_store(path: str, fs) -> zarr.storage.Store:
        return zarr.storage.FSStore(url=path, fs=fs)

    @classmethod
    def write_empty_workflow(
        cls,
        app,
        template_js: Dict,
        template_components_js: Dict,
        wk_path: str,
        fs,
        fs_path: str,
        replaced_wk: str,
        ts_fmt: str,
        ts_name_fmt: str,
        creation_info: Dict,
    ) -> None:
        attrs = {
            "fs_path": fs_path,
            "ts_fmt": ts_fmt,
            "ts_name_fmt": ts_name_fmt,
            "creation_info": creation_info,
            "template": template_js,
            "template_components": template_components_js,
            "num_added_tasks": 0,
            "tasks": [],
            "loops": [],
            "submissions": [],
        }
        if replaced_wk:
            attrs["replaced_workflow"] = replaced_wk

        store = cls._get_zarr_store(wk_path, fs)
        root = zarr.group(store=store, overwrite=False)
        root.attrs.update(attrs)

        md = root.create_group("metadata")

        tasks_arr = md.create_dataset(
            name=cls._task_arr_name,
            shape=0,
            dtype=object,
            object_codec=VLenArray(int),
        )

        elems_arr = md.create_dataset(
            name=cls._elem_arr_name,
            shape=0,
            dtype=object,
            object_codec=MsgPack(),
            chunks=1000,
        )
        elems_arr.attrs.update({"seq_idx": [], "src_idx": []})

        elem_iters_arr = md.create_dataset(
            name=cls._iter_arr_name,
            shape=0,
            dtype=object,
            object_codec=MsgPack(),
            chunks=1000,
        )
        elem_iters_arr.attrs.update(
            {
                "loops": [],
                "schema_parameters": [],
                "parameter_paths": [],
            }
        )

        EARs_arr = md.create_dataset(
            name=cls._EAR_arr_name,
            shape=0,
            dtype=object,
            object_codec=MsgPack(),
            chunks=1,  # single-chunk rows for multiprocess writing
        )
        EARs_arr.attrs.update({"parameter_paths": []})

        parameter_data = root.create_group(name=cls._param_grp_name)
        parameter_data.create_dataset(
            name=cls._param_base_arr_name,
            shape=0,
            dtype=object,
            object_codec=MsgPack(),
            chunks=1,
        )
        parameter_data.create_dataset(
            name=cls._param_sources_arr_name,
            shape=0,
            dtype=object,
            object_codec=MsgPack(),
            chunks=1000,  # TODO: check this is a sensible size with many parameters
        )
        parameter_data.create_group(name=cls._param_user_arr_grp_name)

    def _append_tasks(self, tasks: List[ZarrStoreTask]):
        elem_IDs_arr = self._get_tasks_arr(mode="r+")
        elem_IDs = []
        with self.using_resource("attrs", "update") as attrs:
            for i_idx, i in enumerate(tasks):
                idx, wk_task_i, task_i = i.encode()
                elem_IDs.append(wk_task_i.pop("element_IDs"))
                wk_task_i["element_IDs_idx"] = len(elem_IDs_arr) + i_idx

                attrs["tasks"].insert(idx, wk_task_i)
                attrs["template"]["tasks"].insert(idx, task_i)
                attrs["num_added_tasks"] += 1

        # tasks array rows correspond to task IDs, and we assume `tasks` have sequentially
        # increasing IDs.
        append_items_to_ragged_array(arr=elem_IDs_arr, items=elem_IDs)

    def _append_loops(self, loops: Dict[int, Dict]):
        with self.using_resource("attrs", action="update") as attrs:
            for loop_idx, loop in loops.items():
                attrs["loops"].append(
                    {
                        "num_added_iterations": loop["num_added_iterations"],
                        "iterable_parameters": loop["iterable_parameters"],
                    }
                )
                attrs["template"]["loops"].append(loop["loop_template"])

    def _append_submissions(self, subs: Dict[int, Dict]):
        with self.using_resource("attrs", action="update") as attrs:
            for sub_idx, sub_i in subs.items():
                attrs["submissions"].append(sub_i)

    def _append_task_element_IDs(self, task_ID: int, elem_IDs: List[int]):
        # I don't think there's a way to "append" to an existing array in a zarr ragged
        # array? So we have to build a new array from existing + new.
        arr = self._get_tasks_arr(mode="r+")
        elem_IDs_cur = arr[task_ID]
        elem_IDs_new = np.concatenate((elem_IDs_cur, elem_IDs))
        arr[task_ID] = elem_IDs_new

    def _append_elements(self, elems: List[ZarrStoreElement]):
        arr = self._get_elements_arr(mode="r+")
        attrs_orig = arr.attrs.asdict()
        attrs = copy.deepcopy(attrs_orig)
        arr_add = np.empty((len(elems)), dtype=object)
        arr_add[:] = [i.encode(attrs) for i in elems]
        arr.append(arr_add)
        if attrs != attrs_orig:
            arr.attrs.put(attrs)

    def _append_element_sets(self, task_id: int, es_js: List[Dict]):
        task_idx = task_idx = self._get_task_id_to_idx_map()[task_id]
        with self.using_resource("attrs", "update") as attrs:
            attrs["template"]["tasks"][task_idx]["element_sets"].extend(es_js)

    def _append_elem_iter_IDs(self, elem_ID: int, iter_IDs: List[int]):
        arr = self._get_elements_arr(mode="r+")
        attrs = arr.attrs.asdict()
        elem_dat = arr[elem_ID]
        store_elem = ZarrStoreElement.decode(elem_dat, attrs)
        store_elem = store_elem.append_iteration_IDs(iter_IDs)
        arr[elem_ID] = store_elem.encode(
            attrs
        )  # attrs shouldn't be mutated (TODO: test!)

    def _append_elem_iters(self, iters: List[ZarrStoreElementIter]):
        arr = self._get_iters_arr(mode="r+")
        attrs_orig = arr.attrs.asdict()
        attrs = copy.deepcopy(attrs_orig)
        arr_add = np.empty((len(iters)), dtype=object)
        arr_add[:] = [i.encode(attrs) for i in iters]
        arr.append(arr_add)
        if attrs != attrs_orig:
            arr.attrs.put(attrs)

    def _append_elem_iter_EAR_IDs(self, iter_ID: int, act_idx: int, EAR_IDs: List[int]):
        arr = self._get_iters_arr(mode="r+")
        attrs = arr.attrs.asdict()
        iter_dat = arr[iter_ID]
        store_iter = ZarrStoreElementIter.decode(iter_dat, attrs)
        store_iter = store_iter.append_EAR_IDs(pend_IDs={act_idx: EAR_IDs})
        arr[iter_ID] = store_iter.encode(
            attrs
        )  # attrs shouldn't be mutated (TODO: test!)

    def _append_submission_parts(self, sub_parts: Dict[int, Dict[str, List[int]]]):
        with self.using_resource("attrs", action="update") as attrs:
            for sub_idx, sub_i_parts in sub_parts.items():
                for dt_str, parts_j in sub_i_parts.items():
                    attrs["submissions"][sub_idx]["submission_parts"][dt_str] = parts_j

    def _update_loop_index(self, iter_ID: int, loop_idx: Dict):
        arr = self._get_iters_arr(mode="r+")
        attrs = arr.attrs.asdict()
        iter_dat = arr[iter_ID]
        store_iter = ZarrStoreElementIter.decode(iter_dat, attrs)
        store_iter = store_iter.update_loop_idx(loop_idx)
        arr[iter_ID] = store_iter.encode(attrs)

    def _update_loop_num_iters(self, index: int, num_iters: int):
        with self.using_resource("attrs", action="update") as attrs:
            attrs["loops"][index]["num_added_iterations"] = num_iters

    def _append_EARs(self, EARs: List[ZarrStoreEAR]):
        arr = self._get_EARs_arr(mode="r+")
        attrs_orig = arr.attrs.asdict()
        attrs = copy.deepcopy(attrs_orig)
        arr_add = np.empty((len(EARs)), dtype=object)
        arr_add[:] = [i.encode(attrs, self.ts_fmt) for i in EARs]
        arr.append(arr_add)

        if attrs != attrs_orig:
            arr.attrs.put(attrs)

    def _update_EAR_submission_index(self, EAR_id: int, sub_idx: int):
        arr = self._get_EARs_arr(mode="r+")
        attrs_orig = arr.attrs.asdict()
        attrs = copy.deepcopy(attrs_orig)

        EAR_i = self._get_persistent_EARs([EAR_id])[EAR_id]
        EAR_i = EAR_i.update(submission_idx=sub_idx)
        arr[EAR_id] = EAR_i.encode(attrs, self.ts_fmt)

        if attrs != attrs_orig:
            arr.attrs.put(attrs)

    def _update_EAR_start(self, EAR_id: int, s_time: datetime, s_snap: Dict):
        arr = self._get_EARs_arr(mode="r+")
        attrs_orig = arr.attrs.asdict()
        attrs = copy.deepcopy(attrs_orig)

        EAR_i = self._get_persistent_EARs([EAR_id])[EAR_id]
        EAR_i = EAR_i.update(
            start_time=s_time,
            snapshot_start=s_snap,
        )
        arr[EAR_id] = EAR_i.encode(attrs, self.ts_fmt)

        if attrs != attrs_orig:
            arr.attrs.put(attrs)

    def _update_EAR_end(
        self, EAR_id: int, e_time: datetime, e_snap: Dict, ext_code: int, success: bool
    ):
        arr = self._get_EARs_arr(mode="r+")
        attrs_orig = arr.attrs.asdict()
        attrs = copy.deepcopy(attrs_orig)

        EAR_i = self._get_persistent_EARs([EAR_id])[EAR_id]
        EAR_i = EAR_i.update(
            end_time=e_time,
            snapshot_end=e_snap,
            exit_code=ext_code,
            success=success,
        )
        arr[EAR_id] = EAR_i.encode(attrs, self.ts_fmt)

        if attrs != attrs_orig:
            arr.attrs.put(attrs)

    def _update_EAR_skip(self, EAR_id: int):
        arr = self._get_EARs_arr(mode="r+")
        attrs_orig = arr.attrs.asdict()
        attrs = copy.deepcopy(attrs_orig)

        EAR_i = self._get_persistent_EARs([EAR_id])[EAR_id]
        EAR_i = EAR_i.update(skip=True)
        arr[EAR_id] = EAR_i.encode(attrs, self.ts_fmt)

        if attrs != attrs_orig:
            arr.attrs.put(attrs)

    def _update_js_metadata(self, js_meta: Dict):
        with self.using_resource("attrs", action="update") as attrs:
            for sub_idx, all_js_md in js_meta.items():
                for js_idx, js_meta_i in all_js_md.items():
                    attrs["submissions"][sub_idx]["jobscripts"][js_idx].update(
                        **js_meta_i
                    )

    def _append_parameters(self, params: List[ZarrStoreParameter]):
        """Add new persistent parameters."""
        base_arr = self._get_parameter_base_array(mode="r+")
        src_arr = self._get_parameter_sources_array(mode="r+")
        for param_i in params:
            dat_i = param_i.encode(
                root_group=self._get_parameter_user_array_group(mode="r+"),
                arr_path=self._param_data_arr_grp_name(param_i.id_),
            )
            base_arr.append([dat_i])
            src_arr.append([dict(sorted(param_i.source.items()))])

    def _set_parameter_value(self, param_id: int, value: Any, is_file: bool):
        """Set an unset persistent parameter."""

        # the `decode` call in `_get_persistent_parameters` should be quick:
        param_i = self._get_persistent_parameters([param_id])[param_id]
        if is_file:
            param_i = param_i.set_file(value)
        else:
            param_i = param_i.set_data(value)
        dat_i = param_i.encode(
            root_group=self._get_parameter_user_array_group(mode="r+"),
            arr_path=self._param_data_arr_grp_name(param_i.id_),
        )

        # no need to update sources array:
        base_arr = self._get_parameter_base_array(mode="r+")
        base_arr[param_id] = dat_i

    def _update_parameter_source(self, param_id: int, src: Dict):
        """Update the source of a persistent parameter."""

        param_i = self._get_persistent_parameters([param_id])[param_id]
        param_i = param_i.update_source(src)

        # no need to update base array:
        src_arr = self._get_parameter_sources_array(mode="r+")
        src_arr[param_id] = param_i.source

    def _update_template_components(self, tc: Dict):
        with self.using_resource("attrs", "update") as md:
            md["template_components"] = tc

    def _get_num_persistent_tasks(self) -> int:
        """Get the number of persistent elements."""
        return len(self._get_tasks_arr())

    def _get_num_persistent_loops(self) -> int:
        """Get the number of persistent loops."""
        with self.using_resource("attrs", "read") as attrs:
            return len(attrs["loops"])

    def _get_num_persistent_submissions(self) -> int:
        """Get the number of persistent submissions."""
        with self.using_resource("attrs", "read") as attrs:
            return len(attrs["submissions"])

    def _get_num_persistent_elements(self) -> int:
        """Get the number of persistent elements."""
        return len(self._get_elements_arr())

    def _get_num_persistent_elem_iters(self) -> int:
        """Get the number of persistent element iterations."""
        return len(self._get_iters_arr())

    def _get_num_persistent_EARs(self) -> int:
        """Get the number of persistent EARs."""
        return len(self._get_EARs_arr())

    def _get_num_persistent_parameters(self):
        return len(self._get_parameter_base_array())

    def _get_num_persistent_added_tasks(self):
        with self.using_resource("attrs", "read") as attrs:
            return attrs["num_added_tasks"]

    @property
    def zarr_store(self) -> zarr.storage.Store:
        if self._zarr_store is None:
            self._zarr_store = self._get_zarr_store(self.path, self.fs)
        return self._zarr_store

    def _get_root_group(self, mode: str = "r") -> zarr.Group:
        return zarr.open(self.zarr_store, mode=mode)

    def _get_parameter_group(self, mode: str = "r") -> zarr.Group:
        return self._get_root_group(mode=mode).get(self._param_grp_name)

    def _get_parameter_base_array(self, mode: str = "r") -> zarr.Array:
        return self._get_parameter_group(mode=mode).get(self._param_base_arr_name)

    def _get_parameter_sources_array(self, mode: str = "r") -> zarr.Array:
        return self._get_parameter_group(mode=mode).get(self._param_sources_arr_name)

    def _get_parameter_user_array_group(self, mode: str = "r") -> zarr.Group:
        return self._get_parameter_group(mode=mode).get(self._param_user_arr_grp_name)

    def _get_parameter_data_array_group(
        self,
        parameter_idx: int,
        mode: str = "r",
    ) -> zarr.Group:
        return self._get_parameter_user_array_group(mode=mode).get(
            self._param_data_arr_grp_name(parameter_idx)
        )

    def _get_array_group_and_dataset(self, mode: str, param_id: int, data_path):
        base_dat = self._get_parameter_base_array(mode="r")[param_id]
        arr_idx = None
        for arr_dat_path, arr_idx in base_dat["type_lookup"]["arrays"]:
            if arr_dat_path == data_path:
                break
        if arr_idx is None:
            raise ValueError(
                f"Could not find array path {data_path} in the base data for parameter "
                f"ID {param_id}."
            )
        group = self._get_parameter_user_array_group(mode=mode).get(
            f"{self._param_data_arr_grp_name(param_id)}"
        )
        return group, f"arr_{arr_idx}"

    def _get_metadata_group(self, mode: str = "r") -> zarr.Group:
        return self._get_root_group(mode=mode).get("metadata")

    def _get_tasks_arr(self, mode: str = "r") -> zarr.Array:
        return self._get_metadata_group(mode=mode).get(self._task_arr_name)

    def _get_elements_arr(self, mode: str = "r") -> zarr.Array:
        return self._get_metadata_group(mode=mode).get(self._elem_arr_name)

    def _get_iters_arr(self, mode: str = "r") -> zarr.Array:
        return self._get_metadata_group(mode=mode).get(self._iter_arr_name)

    def _get_EARs_arr(self, mode: str = "r") -> zarr.Array:
        return self._get_metadata_group(mode=mode).get(self._EAR_arr_name)

    @classmethod
    def make_test_store_from_spec(
        cls,
        spec,
        dir=None,
        path="test_store",
        overwrite=False,
    ):
        """Generate an store for testing purposes."""

        path = Path(dir or "", path)
        store = zarr.DirectoryStore(path)
        root = zarr.group(store=store, overwrite=overwrite)
        md = root.create_group("metadata")

        tasks_arr = md.create_dataset(
            name=cls._task_arr_name,
            shape=0,
            dtype=object,
            object_codec=VLenArray(int),
        )

        elems_arr = md.create_dataset(
            name=cls._elem_arr_name,
            shape=0,
            dtype=object,
            object_codec=MsgPack(),
            chunks=1000,
        )
        elems_arr.attrs.update({"seq_idx": [], "src_idx": []})

        elem_iters_arr = md.create_dataset(
            name=cls._iter_arr_name,
            shape=0,
            dtype=object,
            object_codec=MsgPack(),
            chunks=1000,
        )
        elem_iters_arr.attrs.update(
            {
                "loops": [],
                "schema_parameters": [],
                "parameter_paths": [],
            }
        )

        EARs_arr = md.create_dataset(
            name=cls._EAR_arr_name,
            shape=0,
            dtype=object,
            object_codec=MsgPack(),
            chunks=1000,
        )
        EARs_arr.attrs.update({"parameter_paths": []})

        tasks, elems, elem_iters, EARs = super().prepare_test_store_from_spec(spec)

        path = Path(path).resolve()
        tasks = [ZarrStoreTask(**i).encode() for i in tasks]
        elements = [ZarrStoreElement(**i).encode(elems_arr.attrs.asdict()) for i in elems]
        elem_iters = [
            ZarrStoreElementIter(**i).encode(elem_iters_arr.attrs.asdict())
            for i in elem_iters
        ]
        EARs = [ZarrStoreEAR(**i).encode(EARs_arr.attrs.asdict()) for i in EARs]

        append_items_to_ragged_array(tasks_arr, tasks)

        elem_arr_add = np.empty((len(elements)), dtype=object)
        elem_arr_add[:] = elements
        elems_arr.append(elem_arr_add)

        iter_arr_add = np.empty((len(elem_iters)), dtype=object)
        iter_arr_add[:] = elem_iters
        elem_iters_arr.append(iter_arr_add)

        EAR_arr_add = np.empty((len(EARs)), dtype=object)
        EAR_arr_add[:] = EARs
        EARs_arr.append(EAR_arr_add)

        return cls(path)

    def _get_persistent_template_components(self):
        with self.using_resource("attrs", "read") as attrs:
            return attrs["template_components"]

    def _get_persistent_template(self):
        with self.using_resource("attrs", "read") as attrs:
            return attrs["template"]

    def _get_persistent_tasks(
        self, id_lst: Optional[Iterable[int]] = None
    ) -> Dict[int, ZarrStoreTask]:
        with self.using_resource("attrs", action="read") as attrs:
            task_dat = {}
            elem_IDs = []
            for idx, i in enumerate(attrs["tasks"]):
                i = copy.deepcopy(i)
                elem_IDs.append(i.pop("element_IDs_idx"))
                if id_lst is None or i["id_"] in id_lst:
                    task_dat[i["id_"]] = {**i, "index": idx}
        if task_dat:
            try:
                elem_IDs_arr_dat = self._get_tasks_arr().get_coordinate_selection(
                    elem_IDs
                )
            except zarr.errors.BoundsCheckError:
                raise MissingStoreTaskError(elem_IDs) from None  # TODO: not an ID list

            return {
                id_: ZarrStoreTask.decode({**i, "element_IDs": elem_IDs_arr_dat[id_]})
                for idx, (id_, i) in enumerate(task_dat.items())
            }
        else:
            return {}

    def _get_persistent_loops(self, id_lst: Optional[Iterable[int]] = None):
        with self.using_resource("attrs", "read") as attrs:
            loop_dat = {
                idx: i
                for idx, i in enumerate(attrs["loops"])
                if id_lst is None or idx in id_lst
            }
        return loop_dat

    def _get_persistent_submissions(self, id_lst: Optional[Iterable[int]] = None):
        with self.using_resource("attrs", "read") as attrs:
            subs_dat = copy.deepcopy(
                {
                    idx: i
                    for idx, i in enumerate(attrs["submissions"])
                    if id_lst is None or idx in id_lst
                }
            )
            # cast jobscript submit-times and jobscript `task_elements` keys:
            for sub_idx, sub in subs_dat.items():
                for js_idx, js in enumerate(sub["jobscripts"]):
                    for key in list(js["task_elements"].keys()):
                        subs_dat[sub_idx]["jobscripts"][js_idx]["task_elements"][
                            int(key)
                        ] = subs_dat[sub_idx]["jobscripts"][js_idx]["task_elements"].pop(
                            key
                        )

        return subs_dat

    def _get_persistent_elements(
        self, id_lst: Iterable[int]
    ) -> Dict[int, ZarrStoreElement]:
        arr = self._get_elements_arr()
        attrs = arr.attrs.asdict()
        try:
            elem_arr_dat = arr.get_coordinate_selection(list(id_lst))
        except zarr.errors.BoundsCheckError:
            raise MissingStoreElementError(id_lst) from None
        elem_dat = dict(zip(id_lst, elem_arr_dat))
        return {k: ZarrStoreElement.decode(v, attrs) for k, v in elem_dat.items()}

    def _get_persistent_element_iters(
        self, id_lst: Iterable[int]
    ) -> Dict[int, StoreElementIter]:
        arr = self._get_iters_arr()
        attrs = arr.attrs.asdict()
        try:
            iter_arr_dat = arr.get_coordinate_selection(list(id_lst))
        except zarr.errors.BoundsCheckError:
            raise MissingStoreElementIterationError(id_lst) from None
        iter_dat = dict(zip(id_lst, iter_arr_dat))
        return {k: ZarrStoreElementIter.decode(v, attrs) for k, v in iter_dat.items()}

    def _get_persistent_EARs(self, id_lst: Iterable[int]) -> Dict[int, ZarrStoreEAR]:
        arr = self._get_EARs_arr()
        attrs = arr.attrs.asdict()

        try:
            EAR_arr_dat = arr.get_coordinate_selection(list(id_lst))
        except zarr.errors.BoundsCheckError:
            raise MissingStoreEARError(id_lst) from None

        EAR_dat = dict(zip(id_lst, EAR_arr_dat))

        iters = {
            k: ZarrStoreEAR.decode(EAR_dat=v, attrs=attrs, ts_fmt=self.ts_fmt)
            for k, v in EAR_dat.items()
        }
        return iters

    def _get_persistent_parameters(
        self,
        id_lst: Iterable[int],
        dataset_copy: Optional[bool] = False,
    ) -> Dict[int, ZarrStoreParameter]:
        base_arr = self._get_parameter_base_array(mode="r")
        src_arr = self._get_parameter_sources_array(mode="r")

        try:
            param_arr_dat = base_arr.get_coordinate_selection(list(id_lst))
            src_arr_dat = src_arr.get_coordinate_selection(list(id_lst))
        except zarr.errors.BoundsCheckError:
            raise MissingParameterData(id_lst) from None

        param_dat = dict(zip(id_lst, param_arr_dat))
        src_dat = dict(zip(id_lst, src_arr_dat))

        params = {
            k: ZarrStoreParameter.decode(
                id_=k,
                data=v,
                source=src_dat[k],
                arr_group=self._get_parameter_data_array_group(k),
                dataset_copy=dataset_copy,
            )
            for k, v in param_dat.items()
        }

        return params

    def _get_persistent_param_sources(self, id_lst: Iterable[int]) -> Dict[int, Dict]:
        src_arr = self._get_parameter_sources_array(mode="r")
        try:
            src_arr_dat = src_arr.get_coordinate_selection(list(id_lst))
        except zarr.errors.BoundsCheckError:
            raise MissingParameterData(id_lst) from None

        return dict(zip(id_lst, src_arr_dat))

    def _get_persistent_parameter_set_status(
        self, id_lst: Iterable[int]
    ) -> Dict[int, bool]:
        base_arr = self._get_parameter_base_array(mode="r")
        try:
            param_arr_dat = base_arr.get_coordinate_selection(list(id_lst))
        except zarr.errors.BoundsCheckError:
            raise MissingParameterData(id_lst) from None

        return dict(zip(id_lst, [i is not None for i in param_arr_dat]))

    def _get_persistent_parameter_IDs(self) -> List[int]:
        # we assume the row index is equivalent to ID, might need to revisit in future
        base_arr = self._get_parameter_base_array(mode="r")
        return list(range(len(base_arr)))

    def get_ts_fmt(self):
        with self.using_resource("attrs", action="read") as attrs:
            return attrs["ts_fmt"]

    def get_ts_name_fmt(self):
        with self.using_resource("attrs", action="read") as attrs:
            return attrs["ts_name_fmt"]

    def get_creation_info(self):
        with self.using_resource("attrs", action="read") as attrs:
            return copy.deepcopy(attrs["creation_info"])

    def get_fs_path(self):
        with self.using_resource("attrs", action="read") as attrs:
            return attrs["fs_path"]

    def to_zip(self, log=None):
        # TODO: need to update `fs_path` in the new store (because this used to get
        # `Workflow.name`), but can't seem to open `dst_zarr_store` below:
        console = Console()
        status = console.status(f"Zipping workflow {self.workflow.name!r}...")
        status.start()
        src_zarr_store = self.zarr_store
        new_fs_path = f"{self.workflow.fs_path}.zip"
        zfs, _ = ask_pw_on_auth_exc(
            ZipFileSystem,
            fo=new_fs_path,
            mode="w",
            target_options={},
            add_pw_to="target_options",
        )
        dst_zarr_store = zarr.storage.FSStore(url="", fs=zfs)
        zarr.convenience.copy_store(
            src_zarr_store,
            dst_zarr_store,
            excludes="execute",
            log=log,
        )
        del zfs  # ZipFileSystem remains open for instance lifetime
        status.stop()
        return new_fs_path


class ZarrZipPersistentStore(ZarrPersistentStore):
    """A store designed mainly as an archive format that can be uploaded to e.g. Zenodo."""

    _name = "zip"
    _features = PersistentStoreFeatures(
        create=False,
        edit=False,
        jobscript_parallelism=False,
        EAR_parallelism=False,
        schedulers=False,
        submission=False,
    )

    # TODO: enforce read-only nature

    def to_zip(self):
        raise NotImplementedError("Already a zip store!")

    def copy(self, path=None) -> str:
        # not sure how to do this.
        raise NotImplementedError()

    def delete_no_confirm(self) -> None:
        # `ZipFileSystem.rm()` does not seem to be implemented.
        raise NotImplementedError()
