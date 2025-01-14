# vim: set ts=4
#
# Copyright 2021-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import argparse
import re
import sys
import os
from abc import ABC, abstractmethod
from pathlib import Path
from urllib.parse import urlparse

from tuxrun import xdg


class ProgressIndicator(ABC):
    @abstractmethod
    def progress(self, percent):
        """
        This method should display the current percentage to the user
        """

    @abstractmethod
    def finish(self):
        """
        This method should display to the user that the process has finished
        """

    @classmethod
    def get(cls, name: str) -> "ProgressIndicator":
        if sys.stderr.isatty():
            return TTYProgressIndicator(name)
        else:
            return NoProgressIndicator()


class NoProgressIndicator(ProgressIndicator):
    def progress(self, percent):
        pass

    def finish(self):
        pass


class TTYProgressIndicator(ProgressIndicator):
    def __init__(self, name):
        self.name = name

    def progress(self, percent: int) -> None:
        sys.stderr.write(f"\r{self.name} ... %3d%%" % percent)

    def finish(self) -> None:
        sys.stderr.write("\n")


COMPRESSIONS = {
    ".tar.xz": ("tar", "xz"),
    ".tar.gz": ("tar", "gz"),
    ".tgz": ("tar", "gz"),
    ".gz": (None, "gz"),
    ".xz": (None, "xz"),
    ".zst": (None, "zstd"),
}


def compression(path):
    for ext, ret in COMPRESSIONS.items():
        if path.endswith(ext):
            return ret
    return (None, None)


def notnone(value, fallback):
    if value is None:
        return fallback
    return value


def get_new_output_dir(cache_dir):
    base = xdg.get_cache_dir() / "tests"
    if cache_dir:
        base = Path(f"{os.path.abspath(cache_dir)}/tests")
    base.mkdir(parents=True, exist_ok=True)
    existing = [int(f.name) for f in base.glob("[0-9]*")]
    if existing:
        new = max(existing) + 1
    else:
        new = 1
    while True:
        new_dir = base / str(new)
        try:
            new_dir.mkdir()
            break
        except FileExistsError:
            new += 1
    return new_dir


def slugify(s):
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    s = re.sub(r"^-+|-+$", "", s)
    return s


def pathurlnone(string):
    if string is None:
        return None
    url = urlparse(string)
    if url.scheme in ["http", "https"]:
        return string
    if url.scheme not in ["", "file"]:
        raise argparse.ArgumentTypeError(f"Invalid scheme '{url.scheme}'")

    path = Path(string if url.scheme == "" else url.path)
    if not path.exists():
        raise argparse.ArgumentTypeError(f"{path} no such file or directory")
    return f"file://{path.expanduser().resolve()}"


def pathnone(string):
    if string is None:
        return None

    path = Path(string)
    if not path.exists():
        raise argparse.ArgumentTypeError(f"{path} no such file or directory")
    return path.expanduser().resolve()
