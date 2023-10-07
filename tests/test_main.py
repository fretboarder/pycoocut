import pytest
from click.testing import CliRunner

from citemplate import _version, main


@pytest.fixture()
def client() -> CliRunner:
    return CliRunner()


def test_version(client: CliRunner):
    result = client.invoke(main.cli, "version")
    assert result.exit_code == 0
    assert result.output == f"{_version()}\n"
