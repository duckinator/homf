import fnmatch
import json
import logging
from urllib.request import urlopen

import packaging.version

from . import asset_manager


def relevant_asset(asset, file_pattern):
    file_patterns = file_pattern.split(',')
    for pattern in file_patterns:
        if fnmatch.fnmatch(asset['name'], pattern):
            return True
    return False


def get_release_info(repo, name, draft=False, prerelease=False):
    if '/' not in repo:
        raise ValueError(
            f"repo must be of format <user>/<repo>, got '{repo}'",
        )

    url = f"https://api.github.com/repos/{repo}/releases"
    with urlopen(url) as f:
        req = f.read().decode()
    releases = json.loads(req)

    try:
        if name == 'latest':
            # Filter out prereleases and drafts (unless specified in the arguments)
            releases = (
                r for r in releases
                if (draft or not r['draft'])
                and (prerelease or not r['prerelease'])  # noqa: W503
            )
            # Find the latest
            release = max(
                releases,
                key=lambda x: packaging.version.parse(x['tag_name']).public,
            )
            logging.info("Selected release '%s' as latest", release['name'])
        else:
            release = list(filter(lambda x: x['tag_name'] == name, releases))[0]

    except (IndexError, ValueError) as e:
        raise RuntimeError(f"No such Github release: '{name}'") from e

    return release


def download(repo, release, file_pattern, directory):
    release_info = get_release_info(repo, release, file_pattern)
    assets = filter(lambda x: relevant_asset(x, file_pattern),
                    release_info['assets'])
    asset_manager.download(assets, directory, url_key='browser_download_url')
