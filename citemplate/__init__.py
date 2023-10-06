from importlib.metadata import version


def _version():
    return version(__package__)
