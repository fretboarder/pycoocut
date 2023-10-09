import shutil  # noqa: INP001
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter


@pytest.fixture()
def cutter_kwargs():
    def call(**kwargs):
        return dict(  # noqa: C408
            template=str(Path(__file__).parent.parent),
            checkout=None,
            no_input=True,
            extra_context={
                "project_name": "PyCoocut Pytest",
                "project_slug": kwargs["slug"] + "_" + kwargs["project_layout"],
                "initial_version": "0.1.0",
                "author": "Anonymous <nobody@nobody.com>",
                "cli_command": "pt",
                "python_dep": "^3.12",
                "github_user": "pytester",
                "project_layout": kwargs["project_layout"],
                "publish_workflow": True,
            },
            replay=None,
            overwrite_if_exists=True,
            output_dir=str(Path(__file__).parent),
            config_file=str(Path(__file__).parent.parent / "cookiecutter.json"),
            default_config=False,
            password=None,
            directory=None,
            skip_if_file_exists=False,
            accept_hooks=True,
            keep_project_on_failure=False,
        )

    return call


def test_cutter_execution_src(cutter_kwargs):
    kwargs = cutter_kwargs(project_layout="src", slug="pycoocut")
    res = cookiecutter(**kwargs)
    shutil.rmtree(Path(res))


def test_cutter_execution_flat(cutter_kwargs):
    kwargs = cutter_kwargs(project_layout="flat", slug="pycoocut")
    res = cookiecutter(**kwargs)
    shutil.rmtree(Path(res))


def test_cutter_execution_invalid_layout(cutter_kwargs):
    kwargs = cutter_kwargs(project_layout="invalid", slug="pycoocut_invalid")
    with pytest.raises(ValueError) as ex:  # noqa: PT011
        cookiecutter(**kwargs)

    assert ex.typename == "ValueError"
