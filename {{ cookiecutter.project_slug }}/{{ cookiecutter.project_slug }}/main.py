"""Tool description."""

import click

from {{cookiecutter.project_slug}} import _version


class Point2D:
    """A point in 2-dimensional space."""

    def __init__(self, x: float, y: float) -> None:
        """Initialize a Point.

        Args:
            x (float): x
            y (float): y
        """
        self._a, self._b = x, y


@click.group()
def cli() -> None:
    """CLI arguments and options."""


@cli.command()
def version() -> None:
    """Print application version."""
    click.echo(f"{_version()}")


def main() -> None:
    """Entry function."""
    try:
        cli()
    except Exception as ex:  # noqa: BLE001
        click.secho(f"{ex}", err=True)


if __name__ == "__main__":
    main()
