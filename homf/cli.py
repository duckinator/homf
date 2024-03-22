"""Command-line interface for Homf.

Usage:

```
homf github [--files FILES] [--directory DIRECTORY] PACKAGE RELEASE
homf pypi   [--files FILES] [--directory DIRECTORY] PACKAGE RELEASE
```

Options that exist for all commands include:

`--version`: print version information.

`--verbose`: enable verbose logging.

"""

import argparse
import logging
import sys

from . import __version__
from . import api

def github(args):
    """
    ### `homf github [--files FILES] [--directory DIRECTORY] PACKAGE RELEASE`

    Download a release of the specified project.

    Arguments:
        --files=FILES:
            (default `*.pyz`)
            A comma-separated list of filenames to download.
            Supports wildcards (* = everything, ? = any single character).
        --directory=DIRECTORY:
            (default `downloads`)
            The directory to save files in. Created if missing.
        PACKAGE:
            The package to download from GitHub.
        RELEASE:
            The release or tag of the package that you want to download.
    """
    files = args.files
    directory = args.directory
    package = args.PACKAGE
    release_tag = args.RELEASE

    api.github.download(package, release_tag, files, directory)


def pypi(args):
    """
    ### `homf github [--files FILES] [--directory DIRECTORY] PACKAGE RELEASE`

    Download a release of the specified project.

    Arguments:
        --files=FILES:
            (default `*.whl`)
            A comma-separated list of filenames to download.
            Supports wildcards (* = everything, ? = any single character).
        --directory=DIRECTORY:
            (default `downloads`)
            The directory to save files in. Created if missing.
        PACKAGE:
            The package to download from PyPi.
        RELEASE:
            The release or tag of the package that you want to download.
    """
    files = args.files
    directory = args.directory
    package = args.PACKAGE
    release_tag = args.RELEASE

    api.pypi.download(package, release_tag, files, directory)


def _arg_parser():
    parser = argparse.ArgumentParser(
            prog="homf",
            description="Asset download tool for GitHub Releases, PyPi, etc.")
    parser.add_argument("--version", action="store_true",
                        help="Print version information and exit.")
    parser.add_argument("--verbose", action="store_true",
                        help="Enable verbose logging.")

    subparsers = parser.add_subparsers(title="Commands")

    githubp = subparsers.add_parser("github",
                                      help="Download an artifact from GitHub.")
    githubp.add_argument("--files", action="store", default="*",
                          help="Comma-separated list of filenames to download."
                               "Supports wildcards (* = everything, ? = any single character).")
    githubp.add_argument("--directory", action="store", default="downloads",
                           help="Directory to save files in. Created if missing. "
                                "(Default: `downloads`)")
    githubp.add_argument("PACKAGE",
                           help="The package to download from GitHub.")
    githubp.add_argument("RELEASE", action="store", nargs='?', default="latest",
                           help="The release or tag to download.")
    githubp.set_defaults(func=github)


    pypip = subparsers.add_parser("pypi",
                                      help="Download an artifact from PyPi.")
    pypip.add_argument("--files", action="store", default="*",
                          help="Comma-separated list of filenames to download."
                               "Supports wildcards (* = everything, ? = any single character).")
    pypip.add_argument("--directory", action="store", default="downloads",
                           help="Directory to save files in. Created if missing. "
                                "(Default: `downloads`)")
    pypip.add_argument("PACKAGE",
                           help="The package to download from GitHub.")
    pypip.add_argument("RELEASE", action="store", nargs='?', default="latest",
                           help="The release or tag to download.")
    pypip.set_defaults(func=pypi)

    return parser


def main(cmd_args=None):
    """
    Command-line entrypoint for Homf.

    `cmd_args` should be either `None`, or equivalent to `sys.argv[1:]`.
    """
    if sys.version_info < (3, 8):
        print("ERROR: Homf requires Python 3.8 or newer.", file=sys.stderr)

    cmd_args = cmd_args or sys.argv[1:]
    if len(cmd_args) == 0:
        cmd_args = ["--help"]
    args = _arg_parser().parse_args(cmd_args)

    if args.version:
        print(f"homf v{__version__}")
        sys.exit()

    try:
        args.func(args)
    except RuntimeError as err:
        (logging.exception if args.verbose else logging.error)(str(err))

        sys.exit(1)
