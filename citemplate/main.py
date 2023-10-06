import click
from citemplate import _version


@click.group()
def cli():
    """Replace this"""


@cli.command()
def version():
    """print application version"""
    click.echo(f"{_version()}")


def main():
    try:
        cli()
    except Exception as ex:
        click.secho(f"{ex}", err=True)


if __name__ == "__main__":
    main()
