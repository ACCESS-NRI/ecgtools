#!/usr/bin/env python
# flake8: noqa
"""Top-level module for ecgtools ."""

from .builder import Builder, RootDirectory, glob_to_regex

from . import _version

__version__ = _version.get_versions()["version"]
