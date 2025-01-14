# -*- coding: utf-8 -*-

"""A getter for miRBase."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "MirbaseGetter",
]

PREFIX = "0_THIS_IS_RELEASE_"


class MirbaseGetter(Getter):
    """A getter for miRBase."""

    bioregistry_id = "mirbase"
    name = "miRBase"
    homepage_fmt = "https://www.mirbase.org/download/PREVIOUS_RELEASES/{version}"
    version_type = VersionType.semver_minor

    def get(self):
        """Get the latest miRBase version number."""
        url = "http://www.mirbase.org/download_readme/"
        soup = get_soup(url, verify=False)
        return soup.find("p").text.splitlines()[0].split()[-1]


if __name__ == "__main__":
    MirbaseGetter.print()
