import pytest
from click.testing import CliRunner

{% if cookiecutter.project_layout == "src" -%}
from src import _version
from src.cli import main
{%- else -%}
from {{cookiecutter.project_slug}} import _version, main
{%- endif %}


@pytest.fixture()
def client() -> CliRunner:
    return CliRunner()


def test_version(client: CliRunner):
    result = client.invoke(main.cli, "version")
    assert result.exit_code == 0
    assert result.output == f"{_version()}\n"
