# Expose `homf.version.__version__` as `homf.__version__`.
from .version import __version__  # noqa: F401

from .api import github, pypi
