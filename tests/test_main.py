from click.testing import CliRunner
import citemplate.main as main
from citemplate import _version
import pytest as pt


@pt.fixture
def client() -> CliRunner:
    yield CliRunner()


def test_version(client: CliRunner):
    result = client.invoke(main.cli, "version")
    assert result.exit_code == 0
    assert result.output == f"{_version()}\n"
