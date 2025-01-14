from __future__ import annotations
import copy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union

from valida.rules import Rule


from hpcflow.sdk import app
from hpcflow.sdk.core.task_schema import TaskSchema
from .json_like import ChildObjectSpec, JSONLike
from .element import ElementGroup
from .errors import (
    ExtraInputs,
    MissingInputs,
    TaskTemplateInvalidNesting,
    TaskTemplateMultipleInputValues,
    TaskTemplateMultipleSchemaObjectives,
    TaskTemplateUnexpectedInput,
    TaskTemplateUnexpectedSequenceInput,
    UnrequiredInputSources,
    UnsetParameterDataError,
)
from .parameters import InputSourceType
from .utils import (
    get_duplicate_items,
    get_in_container,
    get_item_repeat_index,
    get_relative_path,
    group_by_dict_key_values,
    set_in_container,
)


INPUT_SOURCE_TYPES = ["local", "default", "task", "import"]


@dataclass
class InputStatus:
    """Information about a given schema input and its parametrisation within an element
    set.

    Parameters
    ----------
    has_default
        True if a default value is available.
    is_required
        True if the input is required by one or more actions. An input may not be required
        if it is only used in the generation of inputs files, and those input files are
        passed to the element set directly.
    is_provided
        True if the input is locally provided in the element set.

    """

    has_default: bool
    is_required: bool
    is_provided: bool

    @property
    def is_extra(self):
        """Return True if the input is provided but not required."""
        return self.is_provided and not self.is_required


class ElementSet(JSONLike):
    """Class to represent a parametrisation of a new set of elements."""

    _child_objects = (
        ChildObjectSpec(
            name="inputs",
            class_name="InputValue",
            is_multiple=True,
            dict_key_attr="parameter",
            dict_val_attr="value",
            parent_ref="_element_set",
        ),
        ChildObjectSpec(
            name="input_files",
            class_name="InputFile",
            is_multiple=True,
            parent_ref="_element_set",
        ),
        ChildObjectSpec(
            name="resources",
            class_name="ResourceList",
            parent_ref="_element_set",
        ),
        ChildObjectSpec(
            name="sequences",
            class_name="ValueSequence",
            is_multiple=True,
            parent_ref="_element_set",
        ),
        ChildObjectSpec(
            name="input_sources",
            class_name="InputSource",
            is_multiple=True,
            is_dict_values=True,
            is_dict_values_ensure_list=True,
        ),
        ChildObjectSpec(
            name="groups",
            class_name="ElementGroup",
            is_multiple=True,
        ),
    )

    def __init__(
        self,
        inputs: Optional[List[app.InputValue]] = None,
        input_files: Optional[List[app.InputFile]] = None,
        sequences: Optional[List[app.ValueSequence]] = None,
        resources: Optional[Dict[str, Dict]] = None,
        repeats: Optional[List[Dict]] = None,
        groups: Optional[List[app.ElementGroup]] = None,
        input_sources: Optional[Dict[str, app.InputSource]] = None,
        nesting_order: Optional[List] = None,
        sourceable_elem_iters: Optional[List[int]] = None,
        allow_non_coincident_task_sources: Optional[bool] = False,
    ):
        """
        Parameters
        ----------
        sourceable_elem_iters
            If specified, a list of global element iteration indices from which inputs for
            the new elements associated with this element set may be sourced. If not
            specified, all workflow element iterations are considered sourceable.
        allow_non_coincident_task_sources
            If True, if more than one parameter is sourced from the same task, then allow
            these sources to come from distinct element sub-sets. If False (default),
            only the intersection of element sub-sets for all parameters are included.

        """

        if isinstance(resources, dict):
            resources = self.app.ResourceList.from_json_like(resources)
        elif isinstance(resources, list):
            resources = self.app.ResourceList(resources)
        elif not resources:
            resources = self.app.ResourceList([self.app.ResourceSpec()])

        self.inputs = inputs or []
        self.input_files = input_files or []
        self.repeats = repeats or []
        self.groups = groups or []
        self.resources = resources
        self.sequences = sequences or []
        self.input_sources = input_sources or {}
        self.nesting_order = nesting_order or {}
        self.sourceable_elem_iters = sourceable_elem_iters
        self.allow_non_coincident_task_sources = allow_non_coincident_task_sources

        self._validate()
        self._set_parent_refs()

        self._task_template = None  # assigned by parent Task
        self._defined_input_types = None  # assigned on _task_template assignment
        self._element_local_idx_range = None  # assigned by WorkflowTask._add_element_set

    def __deepcopy__(self, memo):
        dct = self.to_dict()
        orig_inp = dct.pop("original_input_sources", None)
        orig_nest = dct.pop("original_nesting_order", None)
        elem_local_idx_range = dct.pop("_element_local_idx_range", None)
        obj = self.__class__(**copy.deepcopy(dct, memo))
        obj._task_template = self._task_template
        obj._defined_input_types = self._defined_input_types
        obj.original_input_sources = copy.deepcopy(orig_inp)
        obj.original_nesting_order = copy.deepcopy(orig_nest)
        obj._element_local_idx_range = copy.deepcopy(elem_local_idx_range)
        return obj

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.to_dict() == other.to_dict():
            return True
        return False

    @classmethod
    def _json_like_constructor(cls, json_like):
        """Invoked by `JSONLike.from_json_like` instead of `__init__`."""
        orig_inp = json_like.pop("original_input_sources", None)
        orig_nest = json_like.pop("original_nesting_order", None)
        elem_local_idx_range = json_like.pop("_element_local_idx_range", None)
        obj = cls(**json_like)
        obj.original_input_sources = orig_inp
        obj.original_nesting_order = orig_nest
        obj._element_local_idx_range = elem_local_idx_range
        return obj

    def prepare_persistent_copy(self):
        """Return a copy of self, which will then be made persistent, and save copies of
        attributes that may be changed during integration with the workflow."""
        obj = copy.deepcopy(self)
        obj.original_nesting_order = self.nesting_order
        obj.original_input_sources = self.input_sources
        return obj

    def to_dict(self):
        dct = super().to_dict()
        del dct["_defined_input_types"]
        del dct["_task_template"]
        return dct

    @property
    def task_template(self):
        return self._task_template

    @task_template.setter
    def task_template(self, value):
        self._task_template = value
        self._validate_against_template()

    @property
    def input_types(self):
        return [i.labelled_type for i in self.inputs]

    @property
    def element_local_idx_range(self):
        """Used to retrieve elements belonging to this element set."""
        return tuple(self._element_local_idx_range)

    def _validate(self):
        inp_paths = [i.normalised_inputs_path for i in self.inputs]
        dup_inp_paths = get_duplicate_items(inp_paths)
        if dup_inp_paths:
            raise TaskTemplateMultipleInputValues(
                f"The following inputs parameters are associated with multiple input value "
                f"definitions: {dup_inp_paths!r}."
            )

        inp_seq_paths = [i.normalised_inputs_path for i in self.sequences if i.input_type]
        dup_inp_seq_paths = get_duplicate_items(inp_seq_paths)
        if dup_inp_seq_paths:
            raise TaskTemplateMultipleInputValues(
                f"The following input parameters are associated with multiple sequence "
                f"value definitions: {dup_inp_seq_paths!r}."
            )

        inp_and_seq = set(inp_paths).intersection(inp_seq_paths)
        if inp_and_seq:
            raise TaskTemplateMultipleInputValues(
                f"The following input parameters are specified in both the `inputs` and "
                f"`sequences` lists: {list(inp_and_seq)!r}, but must be specified in at "
                f"most one of these."
            )

        for src_key, sources in self.input_sources.items():
            if not sources:
                raise ValueError(
                    f"If specified in `input_sources`, at least one input source must be "
                    f"provided for parameter {src_key!r}."
                )

    def _validate_against_template(self):
        unexpected_types = (
            set(self.input_types) - self.task_template.all_schema_input_types
        )
        if unexpected_types:
            raise TaskTemplateUnexpectedInput(
                f"The following input parameters are unexpected: {list(unexpected_types)!r}"
            )

        seq_inp_types = []
        for seq_i in self.sequences:
            inp_type = seq_i.labelled_type
            if inp_type:
                bad_inp = {inp_type} - self.task_template.all_schema_input_types
                allowed_str = ", ".join(
                    f'"{i}"' for i in self.task_template.all_schema_input_types
                )
                if bad_inp:
                    raise TaskTemplateUnexpectedSequenceInput(
                        f"The input type {inp_type!r} specified in the following sequence"
                        f" path is unexpected: {seq_i.path!r}. Available input types are: "
                        f"{allowed_str}."
                    )
                seq_inp_types.append(inp_type)
            if seq_i.path not in self.nesting_order:
                self.nesting_order.update({seq_i.path: seq_i.nesting_order})

        for rep_spec in self.repeats:
            reps_path_i = f'repeats.{rep_spec["name"]}'
            if reps_path_i not in self.nesting_order:
                self.nesting_order[reps_path_i] = rep_spec["nesting_order"]

        for k, v in self.nesting_order.items():
            if v < 0:
                raise TaskTemplateInvalidNesting(
                    f"`nesting_order` must be >=0 for all keys, but for key {k!r}, value "
                    f"of {v!r} was specified."
                )

        self._defined_input_types = set(self.input_types + seq_inp_types)

    @classmethod
    def ensure_element_sets(
        cls,
        inputs=None,
        input_files=None,
        sequences=None,
        resources=None,
        repeats=None,
        groups=None,
        input_sources=None,
        nesting_order=None,
        element_sets=None,
        sourceable_elem_iters=None,
    ):
        args = (
            inputs,
            input_files,
            sequences,
            resources,
            repeats,
            groups,
            input_sources,
            nesting_order,
        )
        args_not_none = [i is not None for i in args]

        if any(args_not_none):
            if element_sets is not None:
                raise ValueError(
                    "If providing an `element_set`, no other arguments are allowed."
                )
            else:
                element_sets = [cls(*args, sourceable_elem_iters=sourceable_elem_iters)]
        else:
            if element_sets is None:
                element_sets = [cls(*args, sourceable_elem_iters=sourceable_elem_iters)]

        return element_sets

    @property
    def defined_input_types(self):
        return self._defined_input_types

    @property
    def undefined_input_types(self):
        return self.task_template.all_schema_input_types - self.defined_input_types

    def get_sequence_from_path(self, sequence_path):
        for i in self.sequences:
            if i.path == sequence_path:
                return i

    def get_defined_parameter_types(self):
        out = []
        for inp in self.inputs:
            if not inp.is_sub_value:
                out.append(inp.normalised_inputs_path)
        for seq in self.sequences:
            if seq.parameter and not seq.is_sub_value:  # ignore resource sequences
                out.append(seq.normalised_inputs_path)
        return out

    def get_defined_sub_parameter_types(self):
        out = []
        for inp in self.inputs:
            if inp.is_sub_value:
                out.append(inp.normalised_inputs_path)
        for seq in self.sequences:
            if seq.parameter and seq.is_sub_value:  # ignore resource sequences
                out.append(seq.normalised_inputs_path)
        return out

    def get_locally_defined_inputs(self):
        return self.get_defined_parameter_types() + self.get_defined_sub_parameter_types()

    def get_sequence_by_path(self, path):
        for seq in self.sequences:
            if seq.path == path:
                return seq

    @property
    def index(self):
        for idx, element_set in enumerate(self.task_template.element_sets):
            if element_set is self:
                return idx

    @property
    def task(self):
        return self.task_template.workflow_template.workflow.tasks[
            self.task_template.index
        ]

    @property
    def elements(self):
        return self.task.elements[slice(*self.element_local_idx_range)]

    @property
    def element_iterations(self):
        return [j for i in self.elements for j in i.iterations]

    @property
    def elem_iter_IDs(self):
        return [i.id_ for i in self.element_iterations]

    def get_task_dependencies(self, as_objects=False):
        """Get upstream tasks that this element set depends on."""
        deps = []
        for element in self.elements:
            for dep_i in element.get_task_dependencies(as_objects=False):
                if dep_i not in deps:
                    deps.append(dep_i)
        deps = sorted(deps)
        if as_objects:
            deps = [self.task.workflow.tasks.get(insert_ID=i) for i in deps]

        return deps

    def is_input_type_provided(self, labelled_path: str) -> bool:
        """Check if an input is provided locally as an InputValue or a ValueSequence."""

        for inp in self.inputs:
            if labelled_path == inp.normalised_inputs_path:
                return True

        for seq in self.sequences:
            if seq.parameter:
                # i.e. not a resource:
                if labelled_path == seq.normalised_inputs_path:
                    return True

        return False


class OutputLabel(JSONLike):
    """Class to represent schema input labels that should be applied to a subset of task
    outputs"""

    _child_objects = (
        ChildObjectSpec(
            name="where",
            class_name="ElementFilter",
        ),
    )

    def __init__(
        self,
        parameter: str,
        label: str,
        where: Optional[List[app.ElementFilter]] = None,
    ) -> None:
        self.parameter = parameter
        self.label = label
        self.where = where


class Task(JSONLike):
    """Parametrisation of an isolated task for which a subset of input values are given
    "locally". The remaining input values are expected to be satisfied by other
    tasks/imports in the workflow."""

    _child_objects = (
        ChildObjectSpec(
            name="schemas",
            class_name="TaskSchema",
            is_multiple=True,
            shared_data_name="task_schemas",
            shared_data_primary_key="name",
            parent_ref="_task_template",
        ),
        ChildObjectSpec(
            name="element_sets",
            class_name="ElementSet",
            is_multiple=True,
            parent_ref="task_template",
        ),
        ChildObjectSpec(
            name="output_labels",
            class_name="OutputLabel",
            is_multiple=True,
        ),
    )

    def __init__(
        self,
        schemas: Union[app.TaskSchema, str, List[app.TaskSchema], List[str]],
        repeats: Optional[List[Dict]] = None,
        groups: Optional[List[app.ElementGroup]] = None,
        resources: Optional[Dict[str, Dict]] = None,
        inputs: Optional[List[app.InputValue]] = None,
        input_files: Optional[List[app.InputFile]] = None,
        sequences: Optional[List[app.ValueSequence]] = None,
        input_sources: Optional[Dict[str, app.InputSource]] = None,
        nesting_order: Optional[List] = None,
        element_sets: Optional[List[app.ElementSet]] = None,
        output_labels: Optional[List[app.OutputLabel]] = None,
        sourceable_elem_iters: Optional[List[int]] = None,
    ):
        """
        Parameters
        ----------
        schema
            A (list of) `TaskSchema` object(s) and/or a (list of) strings that are task
            schema names that uniquely identify a task schema. If strings are provided,
            the `TaskSchema` object will be fetched from the known task schemas loaded by
            the app configuration.

        """

        # TODO: allow init via specifying objective and/or method and/or implementation
        # (lists of) strs e.g.: Task(
        #   objective='simulate_VE_loading',
        #   method=['CP_FFT', 'taylor'],
        #   implementation=['damask', 'damask']
        # )
        # where method and impl must be single strings of lists of the same length
        # and method/impl are optional/required only if necessary to disambiguate
        #
        # this would be like Task(schemas=[
        #   'simulate_VE_loading_CP_FFT_damask',
        #   'simulate_VE_loading_taylor_damask'
        # ])

        if not isinstance(schemas, list):
            schemas = [schemas]

        _schemas = []
        for i in schemas:
            if isinstance(i, str):
                try:
                    i = self.app.TaskSchema.get_by_key(
                        i
                    )  # TODO: document that we need to use the actual app instance here?
                except KeyError:
                    raise KeyError(f"TaskSchema {i!r} not found.")
            elif not isinstance(i, TaskSchema):
                raise TypeError(f"Not a TaskSchema object: {i!r}")
            _schemas.append(i)

        self._schemas = _schemas

        self._element_sets = self.app.ElementSet.ensure_element_sets(
            inputs=inputs,
            input_files=input_files,
            sequences=sequences,
            resources=resources,
            repeats=repeats,
            groups=groups,
            input_sources=input_sources,
            nesting_order=nesting_order,
            element_sets=element_sets,
            sourceable_elem_iters=sourceable_elem_iters,
        )
        self._output_labels = output_labels or []

        # appended to when new element sets are added and reset on dump to disk:
        self._pending_element_sets = []

        self._validate()
        self._name = self._get_name()

        self.workflow_template = None  # assigned by parent WorkflowTemplate
        self._insert_ID = None
        self._dir_name = None

        self._set_parent_refs()

    def _reset_pending_element_sets(self):
        self._pending_element_sets = []

    def _accept_pending_element_sets(self):
        self._element_sets += self._pending_element_sets
        self._reset_pending_element_sets()

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.to_dict() == other.to_dict():
            return True
        return False

    def _add_element_set(self, element_set: app.ElementSet):
        """Invoked by WorkflowTask._add_element_set."""
        self._pending_element_sets.append(element_set)
        self.workflow_template.workflow._store.add_element_set(
            self.insert_ID, element_set.to_json_like()[0]
        )

    @classmethod
    def _json_like_constructor(cls, json_like):
        """Invoked by `JSONLike.from_json_like` instead of `__init__`."""
        insert_ID = json_like.pop("insert_ID", None)
        dir_name = json_like.pop("dir_name", None)
        obj = cls(**json_like)
        obj._insert_ID = insert_ID
        obj._dir_name = dir_name
        return obj

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"

    def __deepcopy__(self, memo):
        kwargs = self.to_dict()
        _insert_ID = kwargs.pop("insert_ID")
        _dir_name = kwargs.pop("dir_name")
        # _pending_element_sets = kwargs.pop("pending_element_sets")
        obj = self.__class__(**copy.deepcopy(kwargs, memo))
        obj._insert_ID = _insert_ID
        obj._dir_name = _dir_name
        obj._name = self._name
        obj.workflow_template = self.workflow_template
        obj._pending_element_sets = self._pending_element_sets
        return obj

    def to_persistent(self, workflow, insert_ID):
        """Return a copy where any schema input defaults are saved to a persistent
        workflow. Element set data is not made persistent."""

        obj = copy.deepcopy(self)
        new_refs = []
        source = {"type": "default_input", "task_insert_ID": insert_ID}
        for schema in obj.schemas:
            new_refs.extend(schema.make_persistent(workflow, source))

        return obj, new_refs

    def to_dict(self):
        out = super().to_dict()
        return {
            k.lstrip("_"): v
            for k, v in out.items()
            if k not in ("_name", "_pending_element_sets")
        }

    def set_sequence_parameters(self, element_set):
        # set ValueSequence Parameter objects:
        for seq in element_set.sequences:
            if seq.input_type:
                for schema_i in self.schemas:
                    for inp_j in schema_i.inputs:
                        if inp_j.typ == seq.input_type:
                            seq._parameter = inp_j.parameter

    def _validate(self):
        # TODO: check a nesting order specified for each sequence?

        names = set(i.objective.name for i in self.schemas)
        if len(names) > 1:
            raise TaskTemplateMultipleSchemaObjectives(
                f"All task schemas used within a task must have the same "
                f"objective, but found multiple objectives: {list(names)!r}"
            )

    def _get_name(self):
        out = f"{self.objective.name}"
        for idx, schema_i in enumerate(self.schemas, start=1):
            need_and = idx < len(self.schemas) and (
                self.schemas[idx].method or self.schemas[idx].implementation
            )
            out += (
                f"{f'_{schema_i.method}' if schema_i.method else ''}"
                f"{f'_{schema_i.implementation}' if schema_i.implementation else ''}"
                f"{f'_and' if need_and else ''}"
            )
        return out

    @staticmethod
    def get_task_unique_names(tasks: List[app.Task]):
        """Get the unique name of each in a list of tasks.

        Returns
        -------
        list of str

        """

        task_name_rep_idx = get_item_repeat_index(
            tasks,
            item_callable=lambda x: x.name,
            distinguish_singular=True,
        )

        names = []
        for idx, task in enumerate(tasks):
            add_rep = f"_{task_name_rep_idx[idx]}" if task_name_rep_idx[idx] > 0 else ""
            names.append(f"{task.name}{add_rep}")

        return names

    def _get_nesting_order(self, seq):
        """Find the nesting order for a task sequence."""
        return self.nesting_order[seq.normalised_path] if len(seq.values) > 1 else -1

    def _prepare_persistent_outputs(self, workflow, local_element_idx_range):
        # TODO: check that schema is present when adding task? (should this be here?)

        # allocate schema-level output parameter; precise EAR index will not be known
        # until we initialise EARs:
        output_data_indices = {}
        for schema in self.schemas:
            for output in schema.outputs:
                # TODO: consider multiple schemas in action index?

                path = f"outputs.{output.typ}"
                output_data_indices[path] = []
                for idx in range(*local_element_idx_range):
                    # iteration_idx, action_idx, and EAR_idx are not known until
                    # `initialise_EARs`:
                    param_src = {
                        "type": "EAR_output",
                        # "task_insert_ID": self.insert_ID,
                        # "element_idx": idx,
                        # "run_idx": 0,
                    }
                    data_ref = workflow._add_unset_parameter_data(param_src)
                    output_data_indices[path].append(data_ref)

        return output_data_indices

    def prepare_element_resolution(self, element_set, input_data_indices):
        multiplicities = []
        for path_i, inp_idx_i in input_data_indices.items():
            multiplicities.append(
                {
                    "multiplicity": len(inp_idx_i),
                    "nesting_order": element_set.nesting_order.get(path_i, -1),
                    "path": path_i,
                }
            )

        return multiplicities

    @property
    def index(self):
        if self.workflow_template:
            return self.workflow_template.tasks.index(self)
        else:
            return None

    @property
    def output_labels(self):
        return self._output_labels

    @property
    def _element_indices(self):
        return self.workflow_template.workflow.tasks[self.index].element_indices

    def get_available_task_input_sources(
        self,
        element_set: app.ElementSet,
        source_tasks: Optional[List[app.WorkflowTask]] = None,
    ) -> List[app.InputSource]:
        """For each input parameter of this task, generate a list of possible input sources
        that derive from inputs or outputs of this and other provided tasks.

        Note this only produces a subset of available input sources for each input
        parameter; other available input sources may exist from workflow imports."""

        if source_tasks:
            # ensure parameters provided by later tasks are added to the available sources
            # list first, meaning they take precedence when choosing an input source:
            source_tasks = sorted(source_tasks, key=lambda x: x.index, reverse=True)
        else:
            source_tasks = []

        available = {}
        for inputs_path, inp_status in self.get_input_statuses(element_set).items():
            # local specification takes precedence:
            if inputs_path in element_set.get_locally_defined_inputs():
                if inputs_path not in available:
                    available[inputs_path] = []
                available[inputs_path].append(self.app.InputSource.local())

            # search for task sources:
            for src_wk_task_i in source_tasks:
                # ensure we process output types before input types, so they appear in the
                # available sources list first, meaning they take precedence when choosing
                # an input source:
                src_task_i = src_wk_task_i.template
                for in_or_out, labelled_path in sorted(
                    src_task_i.provides_parameters(),
                    key=lambda x: x[0],
                    reverse=True,
                ):
                    if inputs_path in labelled_path:
                        avail_src_path = labelled_path
                        if in_or_out == "input":
                            # input parameter might not be provided e.g. if it only used
                            # to generate an input file, and that input file is passed
                            # directly, so consider only source task element sets that
                            # provide the input locally:
                            es_idx = src_task_i.get_param_provided_element_sets(
                                labelled_path
                            )
                        else:
                            # outputs are always available, so consider all source task
                            # element sets:
                            es_idx = list(range(src_task_i.num_element_sets))

                        if not es_idx:
                            continue
                        else:
                            src_elem_iters = []
                            for es_idx_i in es_idx:
                                es_i = src_task_i.element_sets[es_idx_i]
                                src_elem_iters += es_i.elem_iter_IDs

                        if element_set.sourceable_elem_iters is not None:
                            # can only use a subset of element iterations (this is the
                            # case where this element set is generated from an upstream
                            # element set, in which case we only want to consider newly
                            # added upstream elements when adding elements from this
                            # element set):
                            src_elem_iters = list(
                                set(element_set.sourceable_elem_iters)
                                & set(src_elem_iters)
                            )

                    elif labelled_path in inputs_path and in_or_out == "output":
                        avail_src_path = inputs_path

                        inputs_path_label = None
                        out_label = None
                        try:
                            inputs_path_label = inputs_path.split("[")[1].split("]")[0]
                        except IndexError:
                            pass
                        if inputs_path_label:
                            for out_lab_i in src_task_i.output_labels:
                                if out_lab_i.label == inputs_path_label:
                                    out_label = out_lab_i
                        if out_label:
                            # find element iteration IDs that match the output label
                            # filter:
                            param_path = ".".join(
                                i.condition.callable.kwargs["value"]
                                for i in out_label.where.path
                            )
                            param_path_split = param_path.split(".")

                            src_elem_iters = []
                            for elem_i in src_wk_task_i.elements[:]:
                                params = getattr(elem_i, param_path_split[0])
                                param_dat = getattr(params, param_path_split[1]).value

                                # for remaining paths components try both getattr and getitem:
                                for path_k in param_path_split[2:]:
                                    try:
                                        param_dat = param_dat[path_k]
                                    except TypeError:
                                        param_dat = getattr(param_dat, path_k)

                                rule = Rule(
                                    path=[0],
                                    condition=out_label.where.condition,
                                    cast=out_label.where.cast,
                                )
                                if rule.test([param_dat]).is_valid:
                                    src_elem_iters.append(elem_i.iterations[0].id_)

                    else:
                        continue

                    if not src_elem_iters:
                        continue

                    task_source = self.app.InputSource.task(
                        task_ref=src_task_i.insert_ID,
                        task_source_type=in_or_out,
                        element_iters=src_elem_iters,
                    )

                    if avail_src_path not in available:
                        available[avail_src_path] = []

                    available[avail_src_path].append(task_source)

            if inp_status.has_default:
                if inputs_path not in available:
                    available[inputs_path] = []
                available[inputs_path].append(self.app.InputSource.default())

        return available

    @property
    def schemas(self):
        return self._schemas

    @property
    def element_sets(self):
        return self._element_sets + self._pending_element_sets

    @property
    def num_element_sets(self):
        return len(self.element_sets)

    @property
    def insert_ID(self):
        return self._insert_ID

    @property
    def dir_name(self):
        "Artefact directory name."
        return self._dir_name

    @property
    def name(self):
        return self._name

    @property
    def objective(self):
        return self.schemas[0].objective

    @property
    def all_schema_inputs(self) -> Tuple[app.SchemaInput]:
        return tuple(inp_j for schema_i in self.schemas for inp_j in schema_i.inputs)

    @property
    def all_schema_outputs(self) -> Tuple[app.SchemaOutput]:
        return tuple(inp_j for schema_i in self.schemas for inp_j in schema_i.outputs)

    @property
    def all_schema_input_types(self):
        """Get the set of all schema input types (over all specified schemas)."""
        return {inp_j for schema_i in self.schemas for inp_j in schema_i.input_types}

    @property
    def all_schema_input_normalised_paths(self):
        return {f"inputs.{i}" for i in self.all_schema_input_types}

    @property
    def all_schema_output_types(self):
        """Get the set of all schema output types (over all specified schemas)."""
        return {out_j for schema_i in self.schemas for out_j in schema_i.output_types}

    def get_schema_action(self, idx):
        _idx = 0
        for schema in self.schemas:
            for action in schema.actions:
                if _idx == idx:
                    return action
                _idx += 1
        raise ValueError(f"No action in task {self.name!r} with index {idx!r}.")

    def all_schema_actions(self) -> Iterator[Tuple[int, app.Action]]:
        idx = 0
        for schema in self.schemas:
            for action in schema.actions:
                yield (idx, action)
                idx += 1

    @property
    def num_all_schema_actions(self) -> int:
        num = 0
        for schema in self.schemas:
            for _ in schema.actions:
                num += 1
        return num

    @property
    def all_sourced_normalised_paths(self):
        sourced_input_types = []
        for elem_set in self.element_sets:
            for inp in elem_set.inputs:
                if inp.is_sub_value:
                    sourced_input_types.append(inp.normalised_path)
            for seq in elem_set.sequences:
                if seq.is_sub_value:
                    sourced_input_types.append(seq.normalised_path)
        return set(sourced_input_types) | self.all_schema_input_normalised_paths

    def is_input_type_required(self, typ: str, element_set: app.ElementSet) -> bool:
        """Check if an given input type must be specified in the parametrisation of this
        element set.

        A schema input need not be specified if it is only required to generate an input
        file, and that input file is passed directly."""

        provided_files = [i.file for i in element_set.input_files]
        for schema in self.schemas:
            if not schema.actions:
                return True  # for empty tasks that are used merely for defining inputs
            for act in schema.actions:
                if act.is_input_type_required(typ, provided_files):
                    return True

        return False

    def get_param_provided_element_sets(self, labelled_path: str) -> List[int]:
        """Get the element set indices of this task for which a specified parameter type
        is locally provided."""
        es_idx = []
        for idx, src_es in enumerate(self.element_sets):
            if src_es.is_input_type_provided(labelled_path):
                es_idx.append(idx)
        return es_idx

    def get_input_statuses(self, elem_set: app.ElementSet) -> Dict[str, InputStatus]:
        """Get a dict whose keys are normalised input paths (without the "inputs" prefix),
        and whose values are InputStatus objects.

        Parameters
        ----------
        elem_set
            The element set for which input statuses should be returned.

        """

        status = {}
        for schema_input in self.all_schema_inputs:
            for lab_info in schema_input.labelled_info():
                labelled_type = lab_info["labelled_type"]
                status[labelled_type] = InputStatus(
                    has_default="default_value" in lab_info,
                    is_provided=elem_set.is_input_type_provided(labelled_type),
                    is_required=self.is_input_type_required(labelled_type, elem_set),
                )

        for inp_path in elem_set.get_defined_sub_parameter_types():
            root_param = ".".join(inp_path.split(".")[:-1])
            # If the root parameter is required then the sub-parameter should also be
            # required, otherwise there would be no point in specifying it:
            status[inp_path] = InputStatus(
                has_default=False,
                is_provided=True,
                is_required=status[root_param].is_required,
            )

        return status

    @property
    def universal_input_types(self):
        """Get input types that are associated with all schemas"""
        raise NotImplementedError()

    @property
    def non_universal_input_types(self):
        """Get input types for each schema that are non-universal."""
        raise NotImplementedError()

    @property
    def defined_input_types(self):
        return self._defined_input_types

    @property
    def undefined_input_types(self):
        return self.all_schema_input_types - self.defined_input_types

    @property
    def undefined_inputs(self):
        return [
            inp_j
            for schema_i in self.schemas
            for inp_j in schema_i.inputs
            if inp_j.typ in self.undefined_input_types
        ]

    @property
    def unsourced_inputs(self):
        """Get schema input types for which no input sources are currently specified."""
        return self.all_schema_input_types - set(self.input_sources.keys())

    def provides_parameters(self) -> Tuple[Tuple[str, str]]:
        """Get all provided parameter labelled types and whether they are inputs and
        outputs, considering all element sets.

        """
        out = []
        for schema in self.schemas:
            for in_or_out, labelled_type in schema.provides_parameters:
                out.append((in_or_out, labelled_type))

        # add sub-parameter input values and sequences:
        for es_i in self.element_sets:
            for inp_j in es_i.inputs:
                if inp_j.is_sub_value:
                    out.append(("input", inp_j.normalised_inputs_path))
            for seq_j in es_i.sequences:
                if seq_j.is_sub_value:
                    out.append(("input", seq_j.normalised_inputs_path))

        return tuple(out)

    def add_group(
        self, name: str, where: app.ElementFilter, group_by_distinct: app.ParameterPath
    ):
        group = ElementGroup(name=name, where=where, group_by_distinct=group_by_distinct)
        self.groups.add_object(group)


class WorkflowTask:
    """Class to represent a Task that is bound to a Workflow."""

    _app_attr = "app"

    def __init__(
        self,
        workflow: app.Workflow,
        template: app.Task,
        index: int,
        element_IDs: List[int],
    ):
        self._workflow = workflow
        self._template = template
        self._index = index
        self._element_IDs = element_IDs

        # appended to when new elements are added and reset on dump to disk:
        self._pending_element_IDs = []

        self._elements = None  # assigned on `elements` first access

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.unique_name!r})"

    def _reset_pending_element_IDs(self):
        self._pending_element_IDs = []

    def _accept_pending_element_IDs(self):
        self._element_IDs += self._pending_element_IDs
        self._reset_pending_element_IDs()

    @classmethod
    def new_empty_task(cls, workflow: app.Workflow, template: app.Task, index: int):
        obj = cls(
            workflow=workflow,
            template=template,
            index=index,
            element_IDs=[],
        )
        return obj

    @property
    def workflow(self):
        return self._workflow

    @property
    def template(self):
        return self._template

    @property
    def index(self):
        return self._index

    @property
    def element_IDs(self):
        return self._element_IDs + self._pending_element_IDs

    @property
    def num_elements(self):
        return len(self.element_IDs)

    @property
    def num_actions(self):
        return self.template.num_all_schema_actions

    @property
    def name(self):
        return self.template.name

    @property
    def unique_name(self):
        return self.workflow.get_task_unique_names()[self.index]

    @property
    def insert_ID(self):
        return self.template.insert_ID

    @property
    def dir_name(self):
        return self.template.dir_name

    @property
    def num_element_sets(self):
        return self.template.num_element_sets

    @property
    def elements(self):
        if self._elements is None:
            self._elements = self.app.Elements(self)
        return self._elements

    def get_dir_name(self, loop_idx: Dict[str, int] = None) -> str:
        if not loop_idx:
            return self.dir_name
        return self.dir_name + "_" + "_".join((f"{k}-{v}" for k, v in loop_idx.items()))

    def get_all_element_iterations(self):
        return [j for i in self.elements[:] for j in i.iterations]

    def _make_new_elements_persistent(self, element_set, element_set_idx):
        """Save parameter data to the persistent workflow."""

        # TODO: rewrite. This method is a little hard to follow and results in somewhat
        # unexpected behaviour: if a local source and task source are requested for a
        # given input, the local source element(s) will always come first, regardless of
        # the ordering in element_set.input_sources.

        input_data_idx = {}
        sequence_idx = {}
        source_idx = {}

        # Assign first assuming all locally defined values are to be used:
        param_src = {
            "type": "local_input",
            "task_insert_ID": self.insert_ID,
            "element_set_idx": element_set_idx,
        }
        loc_inp_src = self.app.InputSource.local()
        for res_i in element_set.resources:
            key, dat_ref, _ = res_i.make_persistent(self.workflow, param_src)
            input_data_idx[key] = dat_ref

        for inp_i in element_set.inputs:
            key, dat_ref, _ = inp_i.make_persistent(self.workflow, param_src)
            input_data_idx[key] = dat_ref
            key_ = key.split("inputs.")[1]
            try:
                # TODO: wouldn't need to do this if we raise when an InputValue is
                # provided for a parameter whose inputs sources do not include the local
                # value.
                source_idx[key] = [element_set.input_sources[key_].index(loc_inp_src)]
            except ValueError:
                pass

        for inp_file_i in element_set.input_files:
            key, dat_ref, _ = inp_file_i.make_persistent(self.workflow, param_src)
            input_data_idx[key] = dat_ref

        for seq_i in element_set.sequences:
            key, dat_ref, _ = seq_i.make_persistent(self.workflow, param_src)
            input_data_idx[key] = dat_ref
            sequence_idx[key] = list(range(len(dat_ref)))
            try:
                key_ = key.split("inputs.")[1]
            except IndexError:
                pass
            try:
                # TODO: wouldn't need to do this if we raise when an ValueSequence is
                # provided for a parameter whose inputs sources do not include the local
                # value.
                source_idx[key] = [
                    element_set.input_sources[key_].index(loc_inp_src)
                ] * len(dat_ref)
            except ValueError:
                pass

        for rep_spec in element_set.repeats:
            seq_key = f"repeats.{rep_spec['name']}"
            num_range = list(range(rep_spec["number"]))
            input_data_idx[seq_key] = num_range
            sequence_idx[seq_key] = num_range

        # Now check for task- and default-sources and overwrite or append to local sources:
        inp_stats = self.template.get_input_statuses(element_set)
        for labelled_path_i, sources_i in element_set.input_sources.items():
            path_i_split = labelled_path_i.split(".")
            is_path_i_sub = len(path_i_split) > 1
            if is_path_i_sub:
                path_i_root = path_i_split[0]
            else:
                path_i_root = labelled_path_i
            if not inp_stats[path_i_root].is_required:
                continue

            inp_group_name, def_val = None, None
            for schema_input in self.template.all_schema_inputs:
                for lab_info in schema_input.labelled_info():
                    if lab_info["labelled_type"] == path_i_root:
                        inp_group_name = lab_info["group"]
                        if "default_value" in lab_info:
                            def_val = lab_info["default_value"]
                        break

            key = f"inputs.{labelled_path_i}"

            for inp_src_idx, inp_src in enumerate(sources_i):
                if inp_src.source_type is InputSourceType.TASK:
                    src_task = inp_src.get_task(self.workflow)
                    src_elem_iters = src_task.get_all_element_iterations()

                    if inp_src.element_iters:
                        # only include "sourceable" element iterations:
                        src_elem_iters = [
                            i for i in src_elem_iters if i.id_ in inp_src.element_iters
                        ]

                        src_elem_set_idx = [
                            i.element.element_set_idx for i in src_elem_iters
                        ]

                    if not src_elem_iters:
                        continue

                    task_source_type = inp_src.task_source_type.name.lower()
                    if task_source_type == "output" and "[" in labelled_path_i:
                        src_key = f"{task_source_type}s.{labelled_path_i.split('[')[0]}"
                    else:
                        src_key = f"{task_source_type}s.{labelled_path_i}"

                    grp_idx = [
                        iter_i.get_data_idx()[src_key] for iter_i in src_elem_iters
                    ]

                    if inp_group_name:
                        group_dat_idx = []
                        for dat_idx_i, src_set_idx_i, src_iter in zip(
                            grp_idx, src_elem_set_idx, src_elem_iters
                        ):
                            src_es = src_task.template.element_sets[src_set_idx_i]
                            if inp_group_name in [i.name for i in src_es.groups or []]:
                                # print(f"IN GROUP; {dat_idx_i}; {src_set_idx_i=}")
                                group_dat_idx.append(dat_idx_i)
                            else:
                                # if for any recursive iteration dependency, this group is
                                # defined, assign:
                                src_iter_i = src_iter
                                src_iter_deps = (
                                    self.workflow.get_element_iterations_from_IDs(
                                        src_iter_i.get_element_iteration_dependencies(),
                                    )
                                )

                                src_iter_deps_groups = [
                                    j
                                    for i in src_iter_deps
                                    for j in i.element.element_set.groups
                                ]

                                if inp_group_name in [
                                    i.name for i in src_iter_deps_groups or []
                                ]:
                                    group_dat_idx.append(dat_idx_i)

                                # also check input dependencies
                                for (
                                    k,
                                    v,
                                ) in src_iter.element.get_input_dependencies().items():
                                    k_es_idx = v["element_set_idx"]
                                    k_task_iID = v["task_insert_ID"]
                                    k_es = self.workflow.tasks.get(
                                        insert_ID=k_task_iID
                                    ).template.element_sets[k_es_idx]
                                    if inp_group_name in [
                                        i.name for i in k_es.groups or []
                                    ]:
                                        group_dat_idx.append(dat_idx_i)

                                # TODO: this only goes to one level of dependency

                        grp_idx = [group_dat_idx]  # TODO: generalise to multiple groups

                    if self.app.InputSource.local() in sources_i:
                        # add task source to existing local source:
                        input_data_idx[key] += grp_idx
                        source_idx[key] += [inp_src_idx] * len(grp_idx)

                    else:
                        # overwrite existing local source (if it exists):
                        input_data_idx[key] = grp_idx
                        source_idx[key] = [inp_src_idx] * len(grp_idx)
                        if key in sequence_idx:
                            sequence_idx.pop(key)
                            seq = element_set.get_sequence_by_path(key)

                elif inp_src.source_type is InputSourceType.DEFAULT:
                    grp_idx = [def_val._value_group_idx]
                    if self.app.InputSource.local() in sources_i:
                        input_data_idx[key] += grp_idx
                        source_idx[key] += [inp_src_idx] * len(grp_idx)

                    else:
                        input_data_idx[key] = grp_idx
                        source_idx[key] = [inp_src_idx] * len(grp_idx)

        # sort smallest to largest path, so more-specific items overwrite less-specific
        # items parameter retrieval:
        input_data_idx = dict(sorted(input_data_idx.items()))

        return (input_data_idx, sequence_idx, source_idx)

    def ensure_input_sources(self, element_set):
        """Check valid input sources are specified for a new task to be added to the
        workflow in a given position. If none are specified, set them according to the
        default behaviour.

        This method mutates `element_set.input_sources`.

        """

        # this depends on this schema, other task schemas and inputs/sequences:
        available_sources = self.template.get_available_task_input_sources(
            element_set=element_set,
            source_tasks=self.workflow.tasks[: self.index],
        )

        unreq_sources = set(element_set.input_sources.keys()) - set(
            available_sources.keys()
        )
        if unreq_sources:
            unreq_src_str = ", ".join(f"{i!r}" for i in unreq_sources)
            raise UnrequiredInputSources(
                message=(
                    f"The following input sources are not required but have been "
                    f"specified: {unreq_src_str}."
                ),
                unrequired_sources=unreq_sources,
            )

        # TODO: get available input sources from workflow imports

        all_stats = self.template.get_input_statuses(element_set)

        # an input is not required if it is only used to generate an input file that is
        # passed directly:
        req_types = set(k for k, v in all_stats.items() if v.is_required)

        # check any specified sources are valid, and replace them with those computed in
        # `available_sources` since these will have `element_iters` assigned:
        for path_i, avail_i in available_sources.items():
            # for each sub-path in available sources, if the "root-path" source is
            # required, then add the sub-path source to `req_types` as well:
            path_i_split = path_i.split(".")
            is_path_i_sub = len(path_i_split) > 1
            if is_path_i_sub:
                path_i_root = path_i_split[0]
                if path_i_root in req_types:
                    req_types.add(path_i)

            for s_idx, specified_source in enumerate(
                element_set.input_sources.get(path_i, [])
            ):
                self.workflow._resolve_input_source_task_reference(
                    specified_source, self.unique_name
                )
                avail_idx = specified_source.is_in(avail_i)
                if avail_idx is None:
                    raise ValueError(
                        f"The input source {specified_source.to_string()!r} is not "
                        f"available for input path {path_i!r}. Available "
                        f"input sources are: {[i.to_string() for i in avail_i]}."
                    )
                else:
                    # overwrite with the source from available_sources, since it will have
                    # the `element_iters` attribute assigned:
                    element_set.input_sources[path_i][s_idx] = avail_i[avail_idx]

        unsourced_inputs = req_types - set(element_set.input_sources.keys())

        extra_types = set(k for k, v in all_stats.items() if v.is_extra)
        if extra_types:
            extra_str = ", ".join(f"{i!r}" for i in extra_types)
            raise ExtraInputs(
                message=(
                    f"The following inputs are not required, but have been passed: "
                    f"{extra_str}."
                ),
                extra_inputs=extra_types,
            )

        # set source for any unsourced inputs:
        missing = []
        for input_type in unsourced_inputs:
            inp_i_sources = available_sources.get(input_type, [])

            source = None
            try:
                # first element is defined by default to take precedence in
                # `get_available_task_input_sources`:
                source = inp_i_sources[0]
            except IndexError:
                missing.append(input_type)

            if source is not None:
                element_set.input_sources.update({input_type: [source]})

        # TODO: collate all input sources separately, then can fall back to a different
        # input source (if it was not specified manually) and if the "top" input source
        # results in no available elements due to `allow_non_coincident_task_sources`.

        if not element_set.allow_non_coincident_task_sources:
            sources_by_task = {}
            for inp_type, sources in element_set.input_sources.items():
                source = sources[0]
                if source.source_type is InputSourceType.TASK:
                    if source.task_ref not in sources_by_task:
                        sources_by_task[source.task_ref] = {}
                    sources_by_task[source.task_ref][inp_type] = source

            # if multiple parameters are sourced from the same upstream task, only use
            # element iterations for which all parameters are available (the set
            # intersection):
            for sources in sources_by_task.values():
                # if a parameter has multiple labels, disregard from this by removing all
                # parameters:
                seen_labelled = {}
                for src_i in sources.keys():
                    if "[" in src_i:
                        unlabelled = src_i.split("[")[0]
                        if unlabelled not in seen_labelled:
                            seen_labelled[unlabelled] = 1
                        else:
                            seen_labelled[unlabelled] += 1

                for unlabelled, count in seen_labelled.items():
                    if count > 1:
                        # remove:
                        sources = {
                            k: v
                            for k, v in sources.items()
                            if not k.startswith(unlabelled)
                        }

                if len(sources) < 2:
                    continue

                first_src = next(iter(sources.values()))
                intersect_task_i = set(first_src.element_iters)
                for src_i in sources.values():
                    intersect_task_i.intersection_update(src_i.element_iters)

                # now change elements for the affected input sources:
                for inp_type in sources.keys():
                    element_set.input_sources[inp_type][0].element_iters = list(
                        intersect_task_i
                    )

        if missing:
            missing_str = ", ".join(f"{i!r}" for i in missing)
            raise MissingInputs(
                message=f"The following inputs have no sources: {missing_str}.",
                missing_inputs=missing,
            )

    def generate_new_elements(
        self,
        input_data_indices,
        output_data_indices,
        element_data_indices,
        sequence_indices,
        source_indices,
    ):
        new_elements = []
        element_sequence_indices = {}
        element_src_indices = {}
        for i_idx, i in enumerate(element_data_indices):
            elem_i = {k: input_data_indices[k][v] for k, v in i.items()}
            elem_i.update({k: v[i_idx] for k, v in output_data_indices.items()})
            new_elements.append(elem_i)

            for k, v in i.items():
                # track which sequence value indices (if any) are used for each new
                # element:
                if k in sequence_indices:
                    if k not in element_sequence_indices:
                        element_sequence_indices[k] = []
                    element_sequence_indices[k].append(sequence_indices[k][v])

                # track original InputSource associated with each new element:
                if k in source_indices:
                    if k not in element_src_indices:
                        element_src_indices[k] = []
                    element_src_indices[k].append(source_indices[k][v])

        return new_elements, element_sequence_indices, element_src_indices

    @property
    def upstream_tasks(self):
        """Get all workflow tasks that are upstream from this task."""
        return [task for task in self.workflow.tasks[: self.index]]

    @property
    def downstream_tasks(self):
        """Get all workflow tasks that are downstream from this task."""
        return [task for task in self.workflow.tasks[self.index + 1 :]]

    @staticmethod
    def resolve_element_data_indices(multiplicities):
        """Find the index of the Zarr parameter group index list corresponding to each
        input data for all elements.

        # TODO: update docstring; shouldn't reference Zarr.

        Parameters
        ----------
        multiplicities : list of dict
            Each list item represents a sequence of values with keys:
                multiplicity: int
                nesting_order: int
                path : str

        Returns
        -------
        element_dat_idx : list of dict
            Each list item is a dict representing a single task element and whose keys are
            input data paths and whose values are indices that index the values of the
            dict returned by the `task.make_persistent` method.

        """

        # order by nesting order (so lower nesting orders will be fastest-varying):
        multi_srt = sorted(multiplicities, key=lambda x: x["nesting_order"])
        multi_srt_grp = group_by_dict_key_values(
            multi_srt, "nesting_order"
        )  # TODO: is tested?

        element_dat_idx = [{}]
        for para_sequences in multi_srt_grp:
            # check all equivalent nesting_orders have equivalent multiplicities
            all_multis = {i["multiplicity"] for i in para_sequences}
            if len(all_multis) > 1:
                raise ValueError(
                    f"All inputs with the same `nesting_order` must have the same "
                    f"multiplicity, but for paths "
                    f"{[i['path'] for i in para_sequences]} with "
                    f"`nesting_order` {para_sequences[0]['nesting_order']} found "
                    f"multiplicities {[i['multiplicity'] for i in para_sequences]}."
                )

            new_elements = []
            for val_idx in range(para_sequences[0]["multiplicity"]):
                for element in element_dat_idx:
                    new_elements.append(
                        {
                            **element,
                            **{i["path"]: val_idx for i in para_sequences},
                        }
                    )
            element_dat_idx = new_elements

        return element_dat_idx

    def initialise_EARs(self) -> List[int]:
        """Try to initialise any uninitialised EARs of this task."""
        initialised = []
        for element in self.elements[:]:
            # We don't yet cache Element objects, so `element`, and also it's
            # `ElementIterations, are transient. So there is no reason to update these
            # objects in memory to account for the new EARs. Subsequent calls to
            # `WorkflowTask.elements` will retrieve correct element data from the store.
            # This might need changing once/if we start caching Element objects.
            for iter_i in element.iterations:
                if not iter_i.EARs_initialised:
                    try:
                        self._initialise_element_iter_EARs(iter_i)
                        initialised.append(iter_i.id_)
                    except UnsetParameterDataError:
                        # raised by `test_action_rule`; cannot yet initialise EARs
                        pass
        return initialised

    def _initialise_element_iter_EARs(self, element_iter: app.ElementIteration) -> None:
        schema_data_idx = element_iter.data_idx

        # keys are (act_idx, EAR_idx):
        all_data_idx = {}
        action_runs = {}

        # keys are parameter indices, values are EAR_IDs to update those sources to
        param_src_updates = {}

        count = 0
        for act_idx, action in self.template.all_schema_actions():
            log_common = f"for action {act_idx} of element iteration {element_iter.index} of element {element_iter.element.index} of task {self.unique_name!r}."
            if all(self.test_action_rule(i, schema_data_idx) for i in action.rules):
                self.app.logger.info(f"All action rules evaluated to true {log_common}")
                EAR_ID = self.workflow.num_EARs + count
                param_source = {
                    "type": "EAR_output",
                    "EAR_ID": EAR_ID,
                }
                psrc_update = (
                    action.generate_data_index(  # adds an item to `all_data_idx`
                        act_idx=act_idx,
                        EAR_ID=EAR_ID,
                        schema_data_idx=schema_data_idx,
                        all_data_idx=all_data_idx,
                        workflow=self.workflow,
                        param_source=param_source,
                    )
                )
                # with EARs initialised, we can update the pre-allocated schema-level
                # parameters with the correct EAR reference:
                for i in psrc_update:
                    param_src_updates[i] = {"EAR_ID": EAR_ID}
                run_0 = {
                    "elem_iter_ID": element_iter.id_,
                    "action_idx": act_idx,
                    "metadata": {},
                }
                action_runs[(act_idx, EAR_ID)] = run_0
                count += 1
            else:
                self.app.logger.info(f"Some action rules evaluated to false {log_common}")

        # `generate_data_index` can modify data index for previous actions, so only assign
        # this at the end:
        for (act_idx, EAR_ID_i), run in action_runs.items():
            self.workflow._store.add_EAR(
                elem_iter_ID=element_iter.id_,
                action_idx=act_idx,
                data_idx=all_data_idx[(act_idx, EAR_ID_i)],
                metadata={},
            )

        for pid, src in param_src_updates.items():
            self.workflow._store.update_param_source(pid, src)

    def _add_element_set(self, element_set):
        """
        Returns
        -------
        element_indices : list of int
            Global indices of newly added elements.

        """

        self.template.set_sequence_parameters(element_set)

        self.ensure_input_sources(element_set)  # may modify element_set.input_sources

        (input_data_idx, seq_idx, src_idx) = self._make_new_elements_persistent(
            element_set=element_set,
            element_set_idx=self.num_element_sets,
        )

        element_set.task_template = self.template  # may modify element_set.nesting_order

        multiplicities = self.template.prepare_element_resolution(
            element_set, input_data_idx
        )

        element_inp_data_idx = self.resolve_element_data_indices(multiplicities)

        local_element_idx_range = [
            self.num_elements,
            self.num_elements + len(element_inp_data_idx),
        ]

        element_set._element_local_idx_range = local_element_idx_range
        self.template._add_element_set(element_set)

        output_data_idx = self.template._prepare_persistent_outputs(
            workflow=self.workflow,
            local_element_idx_range=local_element_idx_range,
        )

        (element_data_idx, element_seq_idx, element_src_idx) = self.generate_new_elements(
            input_data_idx,
            output_data_idx,
            element_inp_data_idx,
            seq_idx,
            src_idx,
        )

        iter_IDs = []
        elem_IDs = []
        for elem_idx, data_idx in enumerate(element_data_idx):
            schema_params = set(i for i in data_idx.keys() if len(i.split(".")) == 2)
            elem_ID_i = self.workflow._store.add_element(
                task_ID=self.insert_ID,
                es_idx=self.num_element_sets - 1,
                seq_idx={k: v[elem_idx] for k, v in element_seq_idx.items()},
                src_idx={k: v[elem_idx] for k, v in element_src_idx.items()},
            )
            iter_ID_i = self.workflow._store.add_element_iteration(
                element_ID=elem_ID_i,
                data_idx=data_idx,
                schema_parameters=list(schema_params),
            )
            iter_IDs.append(iter_ID_i)
            elem_IDs.append(elem_ID_i)

        self._pending_element_IDs += elem_IDs
        self.initialise_EARs()

        return iter_IDs

    def add_elements(
        self,
        base_element=None,
        inputs=None,
        input_files=None,
        sequences=None,
        resources=None,
        repeats=None,
        input_sources=None,
        nesting_order=None,
        element_sets=None,
        sourceable_elem_iters=None,
        propagate_to=None,
        return_indices=False,
    ):
        propagate_to = self.app.ElementPropagation._prepare_propagate_to_dict(
            propagate_to, self.workflow
        )
        with self.workflow.batch_update():
            return self._add_elements(
                base_element=base_element,
                inputs=inputs,
                input_files=input_files,
                sequences=sequences,
                resources=resources,
                repeats=repeats,
                input_sources=input_sources,
                nesting_order=nesting_order,
                element_sets=element_sets,
                sourceable_elem_iters=sourceable_elem_iters,
                propagate_to=propagate_to,
                return_indices=return_indices,
            )

    def _add_elements(
        self,
        base_element=None,
        inputs=None,
        input_files=None,
        sequences=None,
        resources=None,
        repeats=None,
        input_sources=None,
        nesting_order=None,
        element_sets=None,
        sourceable_elem_iters=None,
        propagate_to: Dict[str, app.ElementPropagation] = None,
        return_indices: bool = False,
    ):
        """Add more elements to this task.

        Parameters
        ----------
        sourceable_elem_iters : list of int, optional
            If specified, a list of global element iteration indices from which inputs
            may be sourced. If not specified, all workflow element iterations are
            considered sourceable.
        propagate_to : dict of [str, ElementPropagation]
            Propagate the new elements downstream to the specified tasks.
        return_indices : bool, optional
            If True, return the list of indices of the newly added elements. False by
            default.

        """

        if base_element is not None:
            if base_element.task is not self:
                raise ValueError("If specified, `base_element` must belong to this task.")
            b_inputs, b_resources = base_element.to_element_set_data()
            inputs = inputs or b_inputs
            resources = resources or b_resources

        element_sets = self.app.ElementSet.ensure_element_sets(
            inputs=inputs,
            input_files=input_files,
            sequences=sequences,
            resources=resources,
            repeats=repeats,
            input_sources=input_sources,
            nesting_order=nesting_order,
            element_sets=element_sets,
            sourceable_elem_iters=sourceable_elem_iters,
        )

        elem_idx = []
        for elem_set_i in element_sets:
            elem_set_i = elem_set_i.prepare_persistent_copy()
            elem_idx += self._add_element_set(elem_set_i)

        for task in self.get_dependent_tasks(as_objects=True):
            elem_prop = propagate_to.get(task.unique_name)
            if elem_prop is None:
                continue

            task_dep_names = [
                i.unique_name
                for i in elem_prop.element_set.get_task_dependencies(as_objects=True)
            ]
            if self.unique_name not in task_dep_names:
                # TODO: why can't we just do
                #  `if self in not elem_propagate.element_set.task_dependencies:`?
                continue

            # TODO: generate a new ElementSet for this task;
            #       Assume for now we use a single base element set.
            #       Later, allow combining multiple element sets.
            src_elem_iters = elem_idx + [
                j for i in element_sets for j in i.sourceable_elem_iters or []
            ]
            elem_set_i = self.app.ElementSet(
                inputs=elem_prop.element_set.inputs,
                input_files=elem_prop.element_set.input_files,
                sequences=elem_prop.element_set.sequences,
                resources=elem_prop.element_set.resources,
                repeats=elem_prop.element_set.repeats,
                nesting_order=elem_prop.nesting_order,
                sourceable_elem_iters=src_elem_iters,
            )

            del propagate_to[task.unique_name]
            prop_elem_idx = task._add_elements(
                element_sets=[elem_set_i],
                return_indices=True,
                propagate_to=propagate_to,
            )
            elem_idx.extend(prop_elem_idx)

        if return_indices:
            return elem_idx

    def get_element_dependencies(
        self,
        as_objects: bool = False,
    ) -> List[Union[int, app.Element]]:
        """Get elements from upstream tasks that this task depends on."""

        deps = []
        for element in self.elements[:]:
            for iter_i in element.iterations:
                for dep_elem_i in iter_i.get_element_dependencies(as_objects=True):
                    if (
                        dep_elem_i.task.insert_ID != self.insert_ID
                        and dep_elem_i not in deps
                    ):
                        deps.append(dep_elem_i.id_)

        deps = sorted(deps)
        if as_objects:
            deps = self.workflow.get_elements_from_IDs(deps)

        return deps

    def get_task_dependencies(
        self,
        as_objects: bool = False,
    ) -> List[Union[int, app.WorkflowTask]]:
        """Get tasks (insert ID or WorkflowTask objects) that this task depends on.

        Dependencies may come from either elements from upstream tasks, or from locally
        defined inputs/sequences/defaults from upstream tasks."""

        # TODO: this method might become insufficient if/when we start considering a
        # new "task_iteration" input source type, which may take precedence over any
        # other input source types.

        deps = []
        for element_set in self.template.element_sets:
            for sources in element_set.input_sources.values():
                for src in sources:
                    if (
                        src.source_type is InputSourceType.TASK
                        and src.task_ref not in deps
                    ):
                        deps.append(src.task_ref)

        deps = sorted(deps)
        if as_objects:
            deps = [self.workflow.tasks.get(insert_ID=i) for i in deps]

        return deps

    def get_dependent_elements(
        self,
        as_objects: bool = False,
    ) -> List[Union[int, app.Element]]:
        """Get elements from downstream tasks that depend on this task."""
        deps = []
        for task in self.downstream_tasks:
            for element in task.elements[:]:
                for iter_i in element.iterations:
                    for dep_i in iter_i.get_task_dependencies(as_objects=False):
                        if dep_i == self.insert_ID and element.id_ not in deps:
                            deps.append(element.id_)

        deps = sorted(deps)
        if as_objects:
            deps = self.workflow.get_elements_from_IDs(deps)

        return deps

    def get_dependent_tasks(
        self,
        as_objects: bool = False,
    ) -> List[Union[int, app.WorkflowTask]]:
        """Get tasks (insert ID or WorkflowTask objects) that depends on this task."""

        # TODO: this method might become insufficient if/when we start considering a
        # new "task_iteration" input source type, which may take precedence over any
        # other input source types.

        deps = []
        for task in self.downstream_tasks:
            for element_set in task.template.element_sets:
                for sources in element_set.input_sources.values():
                    for src in sources:
                        if (
                            src.source_type is InputSourceType.TASK
                            and src.task_ref == self.insert_ID
                            and task.insert_ID not in deps
                        ):
                            deps.append(task.insert_ID)
        deps = sorted(deps)
        if as_objects:
            deps = [self.workflow.tasks.get(insert_ID=i) for i in deps]
        return deps

    @property
    def inputs(self):
        return self.app.TaskInputParameters(self)

    @property
    def outputs(self):
        return self.app.TaskOutputParameters(self)

    def get(self, path, raise_on_missing=False, default=None):
        return self.app.Parameters(
            self,
            path=path,
            return_element_parameters=False,
            raise_on_missing=raise_on_missing,
            default=default,
        )

    def _path_to_parameter(self, path):
        if len(path) != 2 or path[0] == "resources":
            return

        if path[0] == "inputs":
            try:
                path_1 = path[1].split("[")[0]
            except IndexError:
                path_1 = path[1]
            for i in self.template.schemas:
                for j in i.inputs:
                    if j.parameter.typ == path_1:
                        return j.parameter

        elif path[0] == "outputs":
            for i in self.template.schemas:
                for j in i.outputs:
                    if j.parameter.typ == path[1]:
                        return j.parameter

    def _get_merged_parameter_data(
        self,
        data_index,
        path=None,
        raise_on_missing=False,
        raise_on_unset=False,
        default: Any = None,
    ):
        """Get element data from the persistent store."""

        path = [] if not path else path.split(".")

        parameter = self._path_to_parameter(path)
        sources = []
        current_value = None
        is_cur_val_assigned = False
        is_obj_multi = False
        for path_i, data_idx_i in data_index.items():
            path_i = path_i.split(".")
            is_parent = False
            is_update = False
            try:
                rel_path = get_relative_path(path, path_i)
                is_parent = True
            except ValueError:
                try:
                    update_path = get_relative_path(path_i, path)
                    is_update = True

                except ValueError:
                    # no intersection between paths
                    continue

            is_multi = False
            if isinstance(data_idx_i, list):
                is_multi = True
                if path_i == path:
                    # print(f"{is_obj_multi=}")
                    is_obj_multi = True
            else:
                data_idx_i = [data_idx_i]

            data = []
            for data_idx_i_j in data_idx_i:
                if path_i[0] == "repeats":
                    # data is an integer repeats index, rather than a parameter ID:
                    data_j = data_idx_i_j
                else:
                    param_j = self.workflow.get_parameter(data_idx_i_j)
                    if param_j.file:
                        if param_j.file["store_contents"]:
                            data_j = Path(self.workflow.path) / param_j.file["path"]
                        else:
                            data_j = Path(param_j.file["path"])
                        data_j = data_j.as_posix()
                    else:
                        data_j = param_j.data
                        if parameter and len(path_i) == 2:
                            # retrieve the source if this is a non-sub parameter, so we can,
                            # in the case that there is an associated `ParameterValue` class,
                            # get the class method that should be invoked to initialise the
                            # object:
                            if is_multi:
                                sources.append(param_j.source)
                            else:
                                sources = param_j.source
                    if raise_on_unset and not param_j.is_set:
                        raise UnsetParameterDataError(
                            f"Element data path {path!r} resolves to unset data for (at "
                            f"least) data index path: {path_i!r}."
                        )
                if not is_multi:
                    data = data_j
                else:
                    data.append(data_j)

            if is_parent:
                # replace current value:
                try:
                    current_value = get_in_container(data, rel_path, cast_indices=True)
                    is_cur_val_assigned = True
                except (KeyError, IndexError, ValueError):
                    continue

            elif is_update:
                # update sub-part of current value
                current_value = current_value or {}
                set_in_container(current_value, update_path, data, ensure_path=True)
                is_cur_val_assigned = True

        if not is_cur_val_assigned:
            if raise_on_missing:
                # TODO: custom exception?
                raise ValueError(f"Path {path!r} does not exist in the element data.")
            else:
                current_value = default

        if parameter and parameter._value_class:
            # TODO: retrieve value class method case-insensitively!
            if isinstance(current_value, dict):
                # return a ParameterValue instance:
                method_name = sources.get("value_class_method")
                if method_name:
                    method = getattr(parameter._value_class, method_name)
                else:
                    method = parameter._value_class
                current_value = method(**current_value)

            elif is_obj_multi and isinstance(current_value[0], dict):
                # return a list of ParameterValue instances:
                current_value_ = []
                for cur_val, src in zip(current_value, sources):
                    method_name = src.get("value_class_method")
                    if method_name:
                        method = getattr(parameter._value_class, method_name)
                    else:
                        method = parameter._value_class
                    current_value_.append(method(**cur_val))
                current_value = current_value_

        return current_value

    def test_action_rule(self, act_rule: app.ActionRule, data_idx: Dict) -> bool:
        check = act_rule.check_exists or act_rule.check_missing
        if check:
            param_s = check.split(".")
            if len(param_s) > 2:
                # sub-parameter, so need to try to retrieve parameter data
                try:
                    self._get_merged_parameter_data(data_idx, raise_on_missing=True)
                    return True if act_rule.check_exists else False
                except ValueError:
                    return False if act_rule.check_exists else True
            else:
                if act_rule.check_exists:
                    return act_rule.check_exists in data_idx
                elif act_rule.check_missing:
                    return act_rule.check_missing not in data_idx

        else:
            rule = act_rule.rule
            param_path = ".".join(i.condition.callable.kwargs["value"] for i in rule.path)
            element_dat = self._get_merged_parameter_data(
                data_idx,
                path=param_path,
                raise_on_missing=True,
                raise_on_unset=True,
            )
            # test the rule:
            # note: valida can't `rule.test` scalars yet, so wrap it in a list and set
            # path to first element (see: https://github.com/hpcflow/valida/issues/9):
            rule = Rule(path=[0], condition=rule.condition, cast=rule.cast)
            return rule.test([element_dat]).is_valid


class Elements:
    __slots__ = ("_task",)

    def __init__(self, task: app.WorkflowTask):
        self._task = task

        # TODO: cache Element objects

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(task={self.task.unique_name!r}, "
            f"num_elements={self.task.num_elements})"
        )

    @property
    def task(self):
        return self._task

    def _get_selection(self, selection):
        if isinstance(selection, int):
            start, stop, step = selection, selection + 1, 1

        elif isinstance(selection, slice):
            start, stop, step = selection.start, selection.stop, selection.step
            stop = self.task.num_elements if stop is None else stop
            start = start or 0
            step = 1 if step is None else step

        else:
            raise RuntimeError(
                f"{self.__class__.__name__} selection must be an `int` or a `slice` "
                f"object, but received type {type(selection)}."
            )

        selection = slice(start, stop, step)
        length = len(range(*selection.indices(self.task.num_elements)))

        return selection, length

    def islice(
        self,
        start: int = None,
        end: int = None,
    ) -> Iterator[app.Element]:
        selection, _ = self._get_selection(slice(start, end))
        for i in self.task.workflow.get_task_elements_islice(self.task, selection):
            yield i

    def __len__(self):
        return self.task.num_elements

    def __iter__(self):
        return self.islice()

    def __getitem__(
        self,
        selection: Union[int, slice],
    ) -> Union[app.Element, List[app.Element]]:
        sel_normed, _ = self._get_selection(selection)
        elements = self.task.workflow.get_task_elements(self.task, sel_normed)

        if isinstance(selection, int):
            return elements[0]
        else:
            return elements


@dataclass
class Parameters:
    _app_attr = "_app"

    task: app.WorkflowTask
    path: str
    return_element_parameters: bool
    raise_on_missing: Optional[bool] = False
    default: Optional[Any] = None

    def islice(self, start=None, end=None):
        for i in self.task.workflow.pIO.task_parameter_islice(
            self.task, self.path, start, end
        ):
            yield i

    def _get_selection(self, selection):
        if isinstance(selection, int):
            start, stop, step = selection, selection + 1, 1

        elif isinstance(selection, slice):
            start, stop, step = selection.start, selection.stop, selection.step
            stop = self.task.num_elements if stop is None else stop
            start = start or 0
            step = 1 if step is None else step

        else:
            raise RuntimeError(
                f"{self.__class__.__name__} selection must be an `int` or a `slice` "
                f"object, but received type {type(selection)!r}."
            )

        selection = slice(start, stop, step)
        length = len(range(*selection.indices(self.task.num_elements)))

        return selection, length

    def __iter__(self):
        return self.islice()

    def __getitem__(self, selection: Union[int, slice]) -> Union[Any, List[Any]]:
        selection, length = self._get_selection(selection)
        elements = self.task.workflow.get_task_elements(self.task, selection)
        if self.return_element_parameters:
            params = [
                self._app.ElementParameter(
                    task=self.task,
                    path=self.path,
                    parent=self,
                    element=i,
                    data_idx=i.get_data_idx(self.path),
                )
                for i in elements
            ]
        else:
            params = [
                i.get(
                    path=self.path,
                    raise_on_missing=self.raise_on_missing,
                    default=self.default,
                )
                for i in elements
            ]

        if length == 1:
            return params[0]
        else:
            return params


@dataclass
class TaskInputParameters:
    """For retrieving schema input parameters across all elements."""

    _app_attr = "_app"

    task: app.WorkflowTask

    def __getattr__(self, name):
        if name not in self._get_input_names():
            raise ValueError(f"No input named {name!r}.")
        return self._app.Parameters(self.task, f"inputs.{name}", True)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"{', '.join(f'{i!r}' for i in self._get_input_names())})"
        )

    def __dir__(self):
        return super().__dir__() + self._get_input_names()

    def _get_input_names(self):
        return sorted(self.task.template.all_schema_input_types)


@dataclass
class TaskOutputParameters:
    """For retrieving schema output parameters across all elements."""

    _app_attr = "_app"

    task: app.WorkflowTask

    def __getattr__(self, name):
        if name not in self._get_output_names():
            raise ValueError(f"No output named {name!r}.")
        return self._app.Parameters(self.task, f"outputs.{name}", True)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"{', '.join(f'{i!r}' for i in self._get_output_names())})"
        )

    def __dir__(self):
        return super().__dir__() + self._get_output_names()

    def _get_output_names(self):
        return sorted(self.task.template.all_schema_output_types)


@dataclass
class ElementPropagation:
    """Class to represent how a newly added element set should propagate to a given
    downstream task."""

    _app_attr = "app"

    task: app.Task
    nesting_order: Optional[Dict] = None

    @property
    def element_set(self):
        # TEMP property; for now just use the first element set as the base:
        return self.task.template.element_sets[0]

    def __deepcopy__(self, memo):
        return self.__class__(
            task=self.task,
            nesting_order=copy.deepcopy(self.nesting_order, memo),
        )

    @classmethod
    def _prepare_propagate_to_dict(cls, propagate_to, workflow):
        propagate_to = copy.deepcopy(propagate_to)
        if not propagate_to:
            propagate_to = {}
        elif isinstance(propagate_to, list):
            propagate_to = {i.task.unique_name: i for i in propagate_to}

        for k, v in propagate_to.items():
            if not isinstance(v, ElementPropagation):
                propagate_to[k] = cls.app.ElementPropagation(
                    task=workflow.tasks.get(unique_name=k),
                    **v,
                )
        return propagate_to
