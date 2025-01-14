from __future__ import annotations

from collections import defaultdict
import contextlib
from dataclasses import dataclass, fields
from datetime import datetime

from typing import Any, Dict, List, Optional, Tuple


class PendingChanges:
    """Class to store pending changes and merge them into a persistent store.

    Parameters
    ----------
    add_tasks
        Keys are new task IDs
    add_elem_iter_EAR_IDs
        Keys are element iteration IDs, then EAR action index, and values are EAR IDs.
        This is a list of EAR IDs to add to a given element iteration action.
    add_elem_iter_IDs
        Keys are element IDs, and values are iteration IDs to add to that element.
    add_elem_IDs
        Keys are task IDs, and values are element IDs to add to that task.
    add_parameters
        Keys are parameter indices and values are tuples whose first element is data to
        add and whose second element is the source dict for the new data.
    update_param_sources
        Keys are parameter indices and values are dict parameter sources to merge with
        existing source of that parameter.
    set_EAR_starts
        Keys are EAR IDs and values are tuples of start time, and start dir snapshot.
    set_EAR_ends
        Keys are EAR IDs and values are tuples of end time, end dir snapshot, exit
        code, and success boolean.
    """

    def __init__(self, app, store, resource_map):
        self.app = app
        self.store = store
        self.resource_map = resource_map

        self.add_tasks: Dict[int, AnySTask] = None
        self.add_loops: Dict[int, Dict] = None
        self.add_submissions: Dict[int, Dict] = None
        self.add_elements: Dict[int, AnySElement] = None
        self.add_elem_iters: Dict[int, AnySElementIter] = None
        self.add_EARs: Dict[int, AnySEAR] = None
        self.add_parameters: Dict[int, AnySParameter] = None
        self.add_files: List[Dict] = None
        self.add_template_components: Dict[str, Dict[str, Dict]] = None
        self.add_element_sets: Dict[int, Dict] = None

        self.add_elem_IDs: Dict[int, List] = None
        self.add_elem_iter_IDs: Dict[int, List] = None
        self.add_elem_iter_EAR_IDs: Dict[int, Dict[int, List]] = None
        self.add_submission_parts: Dict[int, Dict[str, List[int]]] = None

        self.set_EAR_submission_indices: Dict[int, int] = None
        self.set_EAR_skips: List[int] = None
        self.set_EAR_starts: Dict[int, Tuple[datetime, Dict]] = None
        self.set_EAR_ends: Dict[int, Tuple[datetime, Dict, int, bool]] = None

        self.set_js_metadata: Dict[int, Dict[int, Any]] = None

        self.set_parameters: Dict[int, AnySParameter] = None

        self.update_param_sources: Dict[int, Dict] = None
        self.update_loop_indices: Dict[int, Dict] = None
        self.update_loop_num_iters: Dict[int, int] = None

        self.reset(is_init=True)  # set up initial data structures

    def __bool__(self):
        """Returns True if there are any outstanding pending items."""
        return (
            bool(self.add_tasks)
            or bool(self.add_loops)
            or bool(self.add_submissions)
            or bool(self.add_elements)
            or bool(self.add_elem_iters)
            or bool(self.add_EARs)
            or bool(self.add_elem_IDs)
            or bool(self.add_elem_iter_IDs)
            or bool(self.add_elem_iter_EAR_IDs)
            or bool(self.add_submission_parts)
            or bool(self.add_parameters)
            or bool(self.add_files)
            or bool(self.add_template_components)
            or bool(self.add_element_sets)
            or bool(self.set_EAR_submission_indices)
            or bool(self.set_EAR_starts)
            or bool(self.set_EAR_ends)
            or bool(self.set_EAR_skips)
            or bool(self.set_js_metadata)
            or bool(self.set_parameters)
            or bool(self.update_param_sources)
            or bool(self.update_loop_indices)
            or bool(self.update_loop_num_iters)
        )

    def where_pending(self) -> List[str]:
        return [
            k
            for k, v in self.__dict__.items()
            if k not in ("app", "store", "resource_map") and bool(v)
        ]

    @property
    def logger(self):
        return self.app.persistence_logger

    def commit_all(self):
        """Commit all pending changes to disk."""
        self.logger.info(f"committing all pending changes: {self.where_pending()}")

        if not self:
            self.logger.debug("commit: no pending changes to commit.")
            return

        for resources, methods in self.resource_map.groups.items():
            # for each resource, enter `using_resource` context manager in "update" mode:
            with contextlib.ExitStack() as stack:
                for res in resources:
                    # TODO: only enter required resources!
                    stack.enter_context(self.store.using_resource(res, "update"))
                for meth in methods:
                    getattr(self, meth)()

        assert not (self)

    def commit_tasks(self) -> None:
        """Commit pending tasks to disk."""
        if self.add_tasks:
            tasks = self.store.get_tasks_by_IDs(self.add_tasks)
            task_ids = list(self.add_tasks.keys())
            self.logger.debug(f"commit: adding pending tasks with IDs: {task_ids!r}")
            self.store._append_tasks(tasks)
            # pending element IDs that belong to pending tasks are now committed:
            self.add_elem_IDs = {
                k: v for k, v in self.add_elem_IDs.items() if k not in task_ids
            }
        self.clear_add_tasks()

    def commit_loops(self) -> None:
        """Commit pending loops to disk."""
        if self.add_loops:
            # retrieve pending loops, including pending changes to num_added_iterations:
            loops = self.store.get_loops_by_IDs(self.add_loops)
            loop_ids = list(self.add_loops.keys())
            self.logger.debug(f"commit: adding pending loops with indices {loop_ids!r}")
            self.store._append_loops(loops)
        self.clear_add_loops()

    def commit_submissions(self) -> None:
        """Commit pending submissions to disk."""
        if self.add_submissions:
            # retrieve pending submissions:
            subs = self.store.get_submissions_by_ID(self.add_submissions)
            sub_ids = list(self.add_submissions.keys())
            self.logger.debug(
                f"commit: adding pending submissions with indices {sub_ids!r}"
            )
            self.store._append_submissions(subs)
        self.clear_add_submissions()

    def commit_submission_parts(self) -> None:
        if self.add_submission_parts:
            self.logger.debug(f"commit: adding pending submission parts")
            self.store._append_submission_parts(self.add_submission_parts)
        self.clear_add_submission_parts()

    def commit_elem_IDs(self) -> None:
        # TODO: could be batched up?
        for task_ID, elem_IDs in self.add_elem_IDs.items():
            self.logger.debug(
                f"commit: adding pending element IDs to task {task_ID!r}: {elem_IDs!r}."
            )
            self.store._append_task_element_IDs(task_ID, elem_IDs)
        self.clear_add_elem_IDs()

    def commit_elements(self) -> None:
        if self.add_elements:
            elems = self.store.get_elements(self.add_elements)
            elem_ids = list(self.add_elements.keys())
            self.logger.debug(f"commit: adding pending elements with IDs: {elem_ids!r}")
            self.store._append_elements(elems)
            # pending iter IDs that belong to pending elements are now committed:
            self.add_elem_iter_IDs = {
                k: v for k, v in self.add_elem_iter_IDs.items() if k not in elem_ids
            }
        self.clear_add_elements()

    def commit_element_sets(self) -> None:
        # TODO: could be batched up?
        for task_id, es_js in self.add_element_sets.items():
            self.logger.debug(f"commit: adding pending element sets.")
            self.store._append_element_sets(task_id, es_js)
        self.clear_add_element_sets()

    def commit_elem_iter_IDs(self) -> None:
        # TODO: could be batched up?
        for elem_ID, iter_IDs in self.add_elem_iter_IDs.items():
            self.logger.debug(
                f"commit: adding pending element iteration IDs to element {elem_ID!r}: "
                f"{iter_IDs!r}."
            )
            self.store._append_elem_iter_IDs(elem_ID, iter_IDs)
        self.clear_add_elem_iter_IDs()

    def commit_elem_iters(self) -> None:
        if self.add_elem_iters:
            iters = self.store.get_element_iterations(self.add_elem_iters.keys())
            iter_ids = list(self.add_elem_iters.keys())
            self.logger.debug(
                f"commit: adding pending element iterations with IDs: {iter_ids!r}"
            )
            self.store._append_elem_iters(iters)
            # pending EAR IDs that belong to pending iters are now committed:
            self.add_elem_iter_EAR_IDs = {
                k: v for k, v in self.add_elem_iter_EAR_IDs.items() if k not in iter_ids
            }
        self.clear_add_elem_iters()

    def commit_elem_iter_EAR_IDs(self) -> None:
        # TODO: could be batched up?
        for iter_ID, act_EAR_IDs in self.add_elem_iter_EAR_IDs.items():
            self.logger.debug(
                f"commit: adding pending EAR IDs to element iteration {iter_ID!r}: "
                f"{dict(act_EAR_IDs)!r}."
            )
            for act_idx, EAR_IDs in act_EAR_IDs.items():
                self.store._append_elem_iter_EAR_IDs(iter_ID, act_idx, EAR_IDs)
        self.clear_add_elem_iter_EAR_IDs()

    def commit_EARs(self) -> None:
        if self.add_EARs:
            EARs = self.store.get_EARs(self.add_EARs)
            EAR_ids = list(self.add_EARs.keys())
            self.logger.debug(f"commit: adding pending EARs with IDs: {EAR_ids!r}")
            self.store._append_EARs(EARs)
            # pending start/end times/snapshots, submission indices, and skips that belong
            # to pending EARs are now committed (accounted for in `get_EARs` above):
            self.set_EAR_submission_indices = {
                k: v
                for k, v in self.set_EAR_submission_indices.items()
                if k not in EAR_ids
            }
            self.set_EAR_skips = [i for i in self.set_EAR_skips if i not in EAR_ids]
            self.set_EAR_starts = {
                k: v for k, v in self.set_EAR_starts.items() if k not in EAR_ids
            }
            self.set_EAR_ends = {
                k: v for k, v in self.set_EAR_ends.items() if k not in EAR_ids
            }

        self.clear_add_EARs()

    def commit_EAR_submission_indices(self) -> None:
        # TODO: could be batched up?
        for EAR_id, sub_idx in self.set_EAR_submission_indices.items():
            self.logger.debug(
                f"commit: adding pending submission index ({sub_idx!r}) to EAR ID "
                f"{EAR_id!r}."
            )
            self.store._update_EAR_submission_index(EAR_id, sub_idx)
        self.clear_set_EAR_submission_indices()

    def commit_EAR_starts(self) -> None:
        # TODO: could be batched up?
        for EAR_id, (time, snap) in self.set_EAR_starts.items():
            self.logger.debug(
                f"commit: adding pending start time ({time!r}) and "
                f"directory snapshot to EAR ID {EAR_id!r}."
            )
            self.store._update_EAR_start(EAR_id, time, snap)
        self.clear_set_EAR_starts()

    def commit_EAR_ends(self) -> None:
        # TODO: could be batched up?
        for EAR_id, (time, snap, ext, suc) in self.set_EAR_ends.items():
            self.logger.debug(
                f"commit: adding pending end time ({time!r}), directory snapshot, "
                f"exit code ({ext!r}), and success status {suc!r} to EAR ID {EAR_id!r}."
            )
            self.store._update_EAR_end(EAR_id, time, snap, ext, suc)
        self.clear_set_EAR_ends()

    def commit_EAR_skips(self) -> None:
        # TODO: could be batched up?
        for EAR_id in self.set_EAR_skips:
            self.logger.debug(f"commit: setting EAR ID {EAR_id!r} as skipped.")
            self.store._update_EAR_skip(EAR_id)
        self.clear_set_EAR_skips()

    def commit_js_metadata(self) -> None:
        if self.set_js_metadata:
            self.logger.debug(
                f"commit: setting jobscript metadata: {self.set_js_metadata!r}"
            )
            self.store._update_js_metadata(self.set_js_metadata)
        self.clear_set_js_metadata()

    def commit_parameters(self) -> None:
        """Make pending parameters persistent."""
        if self.add_parameters:
            params = self.store.get_parameters(self.add_parameters)
            param_ids = list(self.add_parameters.keys())
            self.logger.debug(f"commit: adding pending parameters IDs: {param_ids!r}")
            self.store._append_parameters(params)
        self.clear_add_parameters()

        for param_id, (value, is_file) in self.set_parameters.items():
            # TODO: could be batched up?
            self.logger.debug(f"commit: setting value of parameter ID {param_id!r}.")
            self.store._set_parameter_value(param_id, value, is_file)
        self.clear_set_parameters()

    def commit_files(self) -> None:
        """Add pending files to the files directory."""
        if self.add_files:
            self.logger.debug(f"commit: adding pending files to the files directory.")
            self.store._append_files(self.add_files)
        self.clear_add_files()

    def commit_template_components(self) -> None:
        if self.add_template_components:
            self.logger.debug(f"commit: adding template components.")
            self.store._update_template_components(self.store.get_template_components())
        self.clear_add_template_components()

    def commit_param_sources(self) -> None:
        """Make pending changes to parameter sources persistent."""
        for param_id, src in self.update_param_sources.items():
            # TODO: could be batched up?
            self.logger.debug(f"commit: updating source of parameter ID {param_id!r}.")
            self.store._update_parameter_source(param_id, src)
        self.clear_update_param_sources()

    def commit_loop_indices(self) -> None:
        """Make pending update to element iteration loop indices persistent."""
        for iter_ID, loop_idx in self.update_loop_indices.items():
            self.logger.debug(
                f"commit: updating loop indices of iteration ID {iter_ID!r} with "
                f"{loop_idx!r}."
            )
            self.store._update_loop_index(iter_ID, loop_idx)
        self.clear_update_loop_indices()

    def commit_loop_num_iters(self) -> None:
        """Make pending update to the number of loop iterations."""
        for index, num_iters in self.update_loop_num_iters.items():
            self.logger.debug(
                f"commit: updating loop {index!r} number of iterations to {num_iters!r}."
            )
            self.store._update_loop_num_iters(index, num_iters)
        self.clear_update_loop_num_iters()

    def clear_add_tasks(self):
        self.add_tasks = {}

    def clear_add_loops(self):
        self.add_loops = {}

    def clear_add_submissions(self):
        self.add_submissions = {}

    def clear_add_submission_parts(self):
        self.add_submission_parts = defaultdict(dict)

    def clear_add_elements(self):
        self.add_elements = {}

    def clear_add_element_sets(self):
        self.add_element_sets = defaultdict(list)

    def clear_add_elem_iters(self):
        self.add_elem_iters = {}

    def clear_add_EARs(self):
        self.add_EARs = {}

    def clear_add_elem_IDs(self):
        self.add_elem_IDs = defaultdict(list)

    def clear_add_elem_iter_IDs(self):
        self.add_elem_iter_IDs = defaultdict(list)

    def clear_add_elem_iter_EAR_IDs(self):
        self.add_elem_iter_EAR_IDs = defaultdict(lambda: defaultdict(list))

    def clear_set_EAR_submission_indices(self):
        self.set_EAR_submission_indices = {}

    def clear_set_EAR_starts(self):
        self.set_EAR_starts = {}

    def clear_set_EAR_ends(self):
        self.set_EAR_ends = {}

    def clear_set_EAR_skips(self):
        self.set_EAR_skips = []

    def clear_set_js_metadata(self):
        self.set_js_metadata = defaultdict(lambda: defaultdict(dict))

    def clear_add_parameters(self):
        self.add_parameters = {}

    def clear_add_files(self):
        self.add_files = []

    def clear_add_template_components(self):
        self.add_template_components = defaultdict(dict)

    def clear_set_parameters(self):
        self.set_parameters = {}

    def clear_update_param_sources(self):
        self.update_param_sources = {}

    def clear_update_loop_indices(self):
        self.update_loop_indices = {}

    def clear_update_loop_num_iters(self):
        self.update_loop_num_iters = {}

    def reset(self, is_init=False) -> None:
        """Clear all pending data and prepare to accept new pending data."""

        if not is_init and not self:
            # no pending changes
            return

        if not is_init:
            self.logger.info("resetting pending changes.")

        self.clear_add_tasks()
        self.clear_add_loops()
        self.clear_add_submissions()
        self.clear_add_submission_parts()
        self.clear_add_elements()
        self.clear_add_element_sets()
        self.clear_add_elem_iters()
        self.clear_add_EARs()

        self.clear_add_elem_IDs()
        self.clear_add_elem_iter_IDs()
        self.clear_add_elem_iter_EAR_IDs()

        self.clear_add_parameters()
        self.clear_add_files()
        self.clear_add_template_components()

        self.clear_set_EAR_submission_indices()
        self.clear_set_EAR_starts()
        self.clear_set_EAR_ends()
        self.clear_set_EAR_skips()

        self.clear_set_js_metadata()
        self.clear_set_parameters()

        self.clear_update_param_sources()
        self.clear_update_loop_indices()
        self.clear_update_loop_num_iters()


@dataclass
class CommitResourceMap:
    """Map of `PendingChanges` commit method names to store resource labels, representing
    the store resources required by each commit method, for a given `PersistentStore`

    When `PendingChanges.commit_all` is called, the resources specified will be opened in
    "update" mode, for each `commit_` method.

    """

    commit_tasks: Optional[Tuple[str]] = tuple()
    commit_loops: Optional[Tuple[str]] = tuple()
    commit_submissions: Optional[Tuple[str]] = tuple()
    commit_submission_parts: Optional[Tuple[str]] = tuple()
    commit_elem_IDs: Optional[Tuple[str]] = tuple()
    commit_elements: Optional[Tuple[str]] = tuple()
    commit_element_sets: Optional[Tuple[str]] = tuple()
    commit_elem_iter_IDs: Optional[Tuple[str]] = tuple()
    commit_elem_iters: Optional[Tuple[str]] = tuple()
    commit_elem_iter_EAR_IDs: Optional[Tuple[str]] = tuple()
    commit_EARs: Optional[Tuple[str]] = tuple()
    commit_EAR_submission_indices: Optional[Tuple[str]] = tuple()
    commit_EAR_skips: Optional[Tuple[str]] = tuple()
    commit_EAR_starts: Optional[Tuple[str]] = tuple()
    commit_EAR_ends: Optional[Tuple[str]] = tuple()
    commit_js_metadata: Optional[Tuple[str]] = tuple()
    commit_parameters: Optional[Tuple[str]] = tuple()
    commit_files: Optional[Tuple[str]] = tuple()
    commit_template_components: Optional[Tuple[str]] = tuple()
    commit_param_sources: Optional[Tuple[str]] = tuple()
    commit_loop_indices: Optional[Tuple[str]] = tuple()
    commit_loop_num_iters: Optional[Tuple[str]] = tuple()

    def __post_init__(self):
        self.groups = self.group_by_resource()

    def group_by_resource(self) -> Dict[Tuple[str], List[str]]:
        """Return a dict whose keys are tuples of resource labels and whose values are
        lists of `PendingChanges` commit method names that require those resource.

        This grouping allows us to batch up commit methods by resource requirements, which
        in turn means we can potentially minimise e.g. the number of network requests.

        """
        groups = {}
        cur_res_group = None
        for fld in fields(self):
            res_labels = getattr(self, fld.name)

            if not cur_res_group:
                # start a new resource group: a mapping between resource labels and the
                # commit methods that require those resources:
                cur_res_group = [list(res_labels), [fld.name]]

            elif not res_labels or set(res_labels).intersection(cur_res_group[0]):
                # there is some overlap between resource labels required in the current
                # group and this commit method, so we merge resource labels and add the
                # new commit method:
                cur_res_group[0] = list(set(cur_res_group[0] + list(res_labels)))
                cur_res_group[1].append(fld.name)

            else:
                # no overlap between resource labels required in the current group and
                # those required by this commit method, so append the current group, and
                # start a new group for this commit method:
                if tuple(cur_res_group[0]) not in groups:
                    groups[tuple(cur_res_group[0])] = []
                groups[tuple(cur_res_group[0])].extend(cur_res_group[1])
                cur_res_group = [list(res_labels), [fld.name]]

        if cur_res_group:
            if tuple(cur_res_group[0]) not in groups:
                groups[tuple(cur_res_group[0])] = []

            groups[tuple(cur_res_group[0])].extend(cur_res_group[1])

        return groups
