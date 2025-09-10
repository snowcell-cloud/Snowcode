from importlib.metadata import PackageNotFoundError, version as _version

# Must match [tool.poetry].name
_DIST_NAME = "snowcode"

def get_version() -> str:
    try:
        return _version(_DIST_NAME)
    except PackageNotFoundError:
        return "unknown"

__version__ = get_version()
