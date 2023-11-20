import os

import pytest
from helpers import homf_check, python_check, check_zipfile, check_tgz


@pytest.mark.network
def test_download(tmpdir):
    os.chdir(tmpdir)

    # Download a pyz file from GitHub, saved to ./downloads, and check
    # that it can be run with Python.
    homf_check("github", "duckinator/emanate", "v7.0.0")
    python_check("downloads/emanate-7.0.0.pyz", "--help")

    # Download a pyz file for a specific version from GitHub, saved to ./bin
    homf_check("github", "duckinator/emanate", "v7.0.0", "--directory", "bin/")
    python_check("bin/emanate-7.0.0.pyz", "--help")

    # Download a .tar.gz file from GitHub, saved to ./downloads
    homf_check("github",
               "ppb/pursuedpybear", "v0.6.0",
               "--files", "*.tar.gz",
               "--directory", "downloads")
    assert check_tgz("downloads/ppb-0.6.0.tar.gz")

    # Download a .whl file from PyPi, and verify it's uncorrupted.
    homf_check("pypi", "emanate", "v6.0.0", "--files", "*.whl")
    assert check_zipfile("downloads/emanate-6.0.0-py3-none-any.whl")
