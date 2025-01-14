import pytest

from hpcflow.app import app as hf
from hpcflow.sdk.core.test_utils import P1_parameter_cls as P1


@pytest.fixture
def null_config(tmp_path):
    if not hf.is_config_loaded:
        hf.load_config(config_dir=tmp_path)


def test_null_default_value():
    p1 = hf.Parameter("p1")
    p1_inp = hf.SchemaInput(parameter=p1)
    assert "default_value" not in p1_inp.labels[""]


def test_none_default_value():
    """A `None` default value is set with a value of `None`"""
    p1 = hf.Parameter("p1")
    p1_inp = hf.SchemaInput(parameter=p1, default_value=None)
    def_val_exp = hf.InputValue(parameter=p1, label="", value=None)
    def_val_exp._schema_input = p1_inp
    assert p1_inp.labels[""]["default_value"] == def_val_exp


def test_from_json_like_labels_and_default():
    json_like = {
        "parameter": "p1",
        "labels": {"0": {}},
        "default_value": None,
    }
    inp = hf.SchemaInput.from_json_like(
        json_like=json_like,
        shared_data=hf.template_components,
    )
    assert inp.labels["0"]["default_value"].value == None


def test_element_get_removes_schema_param_trivial_label(null_config, tmp_path):
    p1_val = 101
    label = "my_label"
    s1 = hf.TaskSchema(
        objective="t1", inputs=[hf.SchemaInput(parameter="p1", labels={label: {}})]
    )
    t1 = hf.Task(schemas=[s1], inputs=[hf.InputValue("p1", p1_val, label=label)])
    wk = hf.Workflow.from_template_data(
        tasks=[t1],
        path=tmp_path,
        template_name="temp",
    )
    assert f"inputs.p1[{label}]" in wk.tasks[0].elements[0].get_data_idx("inputs")
    assert wk.tasks[0].elements[0].get("inputs") == {"p1": p1_val}


def test_element_inputs_removes_schema_param_trivial_label(null_config, tmp_path):
    p1_val = 101
    label = "my_label"
    s1 = hf.TaskSchema(
        objective="t1",
        inputs=[hf.SchemaInput(parameter="p1", labels={label: {}})],
        actions=[
            hf.Action(
                environments=[hf.ActionEnvironment(environment=hf.envs.null_env)],
                commands=[hf.Command(command=f"echo <<parameter:p1[{label}]>>")],
            ),
        ],
    )
    t1 = hf.Task(schemas=[s1], inputs=[hf.InputValue("p1", p1_val, label=label)])
    wk = hf.Workflow.from_template_data(
        tasks=[t1],
        path=tmp_path,
        template_name="temp",
    )
    element = wk.tasks[0].elements[0]
    # element inputs:
    assert element.inputs._get_prefixed_names() == ["p1"]

    # element iteration inputs:
    assert element.iterations[0].inputs._get_prefixed_names() == ["p1"]

    # run inputs:
    assert element.iterations[0].action_runs[0].inputs._get_prefixed_names() == ["p1"]


def test_element_get_does_not_removes_multiple_schema_param_label(null_config, tmp_path):
    p1_val = 101
    label = "my_label"
    s1 = hf.TaskSchema(
        objective="t1",
        inputs=[hf.SchemaInput(parameter="p1", labels={label: {}}, multiple=True)],
    )
    t1 = hf.Task(schemas=[s1], inputs=[hf.InputValue("p1", p1_val, label=label)])
    wk = hf.Workflow.from_template_data(
        tasks=[t1],
        path=tmp_path,
        template_name="temp",
    )
    assert f"inputs.p1[{label}]" in wk.tasks[0].elements[0].get_data_idx("inputs")
    assert wk.tasks[0].elements[0].get("inputs") == {f"p1[{label}]": p1_val}


def test_element_inputs_does_not_remove_multiple_schema_param_label(
    null_config, tmp_path
):
    p1_val = 101
    label = "my_label"
    s1 = hf.TaskSchema(
        objective="t1",
        inputs=[hf.SchemaInput(parameter="p1", labels={label: {}}, multiple=True)],
        actions=[
            hf.Action(
                environments=[hf.ActionEnvironment(environment=hf.envs.null_env)],
                commands=[hf.Command(command=f"echo <<parameter:p1[{label}]>>")],
            ),
        ],
    )
    t1 = hf.Task(schemas=[s1], inputs=[hf.InputValue("p1", p1_val, label=label)])
    wk = hf.Workflow.from_template_data(
        tasks=[t1],
        path=tmp_path,
        template_name="temp",
    )
    element = wk.tasks[0].elements[0]
    # element inputs:
    assert element.inputs._get_prefixed_names() == [f"p1[{label}]"]

    # element iteration inputs:
    assert element.iterations[0].inputs._get_prefixed_names() == [f"p1[{label}]"]

    # run inputs:
    assert element.iterations[0].action_runs[0].inputs._get_prefixed_names() == [
        f"p1[{label}]"
    ]


def test_get_input_values_for_multiple_schema_input(null_config, tmp_path):
    p1_val = 101
    label = "my_label"
    s1 = hf.TaskSchema(
        objective="t1",
        inputs=[
            hf.SchemaInput(parameter="p1", labels={label: {}}, multiple=True),
            hf.SchemaInput(parameter="p2", default_value=201),
        ],
        actions=[
            hf.Action(
                environments=[hf.ActionEnvironment(environment=hf.envs.null_env)],
                commands=[
                    hf.Command(command=f"echo <<parameter:p1[{label}]>> <<parameter:p2>>")
                ],
            ),
        ],
    )
    t1 = hf.Task(schemas=[s1], inputs=[hf.InputValue("p1", p1_val, label=label)])
    wk = hf.Workflow.from_template_data(
        tasks=[t1],
        path=tmp_path,
        template_name="temp",
    )
    run = wk.tasks[0].elements[0].iterations[0].action_runs[0]
    assert run.get_input_values() == {"p2": 201, "p1": {label: 101}}


def test_get_input_values_for_multiple_schema_input_with_object(null_config, tmp_path):
    p1_val = P1(a=101)
    label = "my_label"
    s1 = hf.TaskSchema(
        objective="t1",
        inputs=[
            hf.SchemaInput(parameter="p1", labels={label: {}}, multiple=True),
            hf.SchemaInput(parameter="p2", default_value=201),
        ],
        actions=[
            hf.Action(
                environments=[hf.ActionEnvironment(environment=hf.envs.null_env)],
                commands=[
                    hf.Command(command=f"echo <<parameter:p1[{label}]>> <<parameter:p2>>")
                ],
            ),
        ],
    )
    t1 = hf.Task(schemas=[s1], inputs=[hf.InputValue("p1", p1_val, label=label)])
    wk = hf.Workflow.from_template_data(
        tasks=[t1],
        path=tmp_path,
        template_name="temp",
    )
    run = wk.tasks[0].elements[0].iterations[0].action_runs[0]
    assert run.get_input_values() == {"p2": 201, "p1": {label: p1_val}}
