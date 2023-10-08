import nox


@nox.session
def ruff(session: nox.Session):
    """Running ruff"""
    session.install("ruff", "click")
    session.run("ruff", "check", "citemplate")


@nox.session
def mypy(session: nox.Session):
    """Running ruff"""
    session.install("mypy", "click")
    session.run("mypy", "citemplate")


@nox.session()
def pytest(session: nox.Session):
    """Running pytest"""
    session.install("pytest")
    session.install(".")
    session.run("pytest")
