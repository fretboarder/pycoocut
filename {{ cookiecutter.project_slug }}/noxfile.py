import nox


@nox.session
def ruff(session: nox.Session):
    """Running ruff"""
    session.install("ruff", "click")
    {% if cookiecutter.project_layout == "src" -%}
    session.run("ruff", "check", "src")
    {%- else -%}
    session.run("ruff", "check", "{{cookiecutter.project_slug}}")
    {%- endif %}


@nox.session
def mypy(session: nox.Session):
    """Running mypy"""
    session.install("mypy", "click")
    {% if cookiecutter.project_layout == "src" -%}
    session.run("mypy", "src")
    {%- else -%}
    session.run("mypy", "{{cookiecutter.project_slug}}")
    {%- endif %}


@nox.session()
def pytest(session: nox.Session):
    """Running pytest"""
    session.install("pytest")
    session.install(".")
    session.run("pytest")
