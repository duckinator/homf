# homf [![Build Status][build-status-img]][build-status-link] [![PyPI][pypi-version-img]][pypi-version-link] [![Documentation Status][docs-img]][docs-link]

Homf is a tool for downloading artifacts from online services, like a ZipApp from GitHub Releases or a Wheel from PyPi.

Documentation: <https://homf.readthedocs.io/>

The recommended way to install Homf is via [pipx](https://pipx.pypa.io/).
If you have pipx installed, you can install Homf via `pipx install homf`.

The basic syntax is `homf SOURCE [OPTIONS] PACKAGE RELEASE`. `SOURCE` is one of `github` or `pypi`.
For GitHub, `PACKAGE` is the repository and `RELEASE` is the tag used by GitHub Releases.
For PyPi, `PACKAGE` is the package name on PyPi and `RELEASE` is the version number.

By default, Homf downloads all files for the release into `./downloads`.

See the [documentation](https://homf.readthedocs.io/) for details on `OPTIONS`.

```
$ homf github ppb/pursuedpybear
INFO     Selected release 'v3.2.0 - The Bear Awakens!' as latest
INFO     Downloaded 'downloads/examples.zip'
INFO     Downloaded 'downloads/ppb-3.2.0-py3-none-any.whl'
INFO     Downloaded 'downloads/ppb-3.2.0.tar.gz'
$ tree downloads/
downloads/
├── examples.zip
├── ppb-3.2.0-py3-none-any.whl
└── ppb-3.2.0.tar.gz

1 directory, 3 files
$ rm -r downloads/
$ homf pypi emanate
INFO     Selected release '8.0.2' as latest
INFO     Downloaded 'downloads/emanate-8.0.2-py3-none-any.whl'
INFO     Downloaded 'downloads/emanate-8.0.2.tar.gz'
$ tree downloads/
downloads/
├── emanate-8.0.2-py3-none-any.whl
└── emanate-8.0.2.tar.gz

1 directory, 2 files
$
```

Homf requires Python 3.8 or newer.

[build-status-img]: https://api.cirrus-ci.com/github/duckinator/homf.svg
[build-status-link]: https://cirrus-ci.com/github/duckinator/homf

[pypi-version-img]: https://img.shields.io/pypi/v/homf
[pypi-version-link]: https://pypi.org/project/homf

[docs-img]: https://readthedocs.org/projects/homf/badge/?version=latest
[docs-link]: https://homf.readthedocs.io/en/latest/?badge=latest


## Contributing

Bug reports and pull requests are welcome on GitHub at <https://github.com/duckinator/homf>.

The code for Homf is available under the [MIT License](http://opensource.org/licenses/MIT).
