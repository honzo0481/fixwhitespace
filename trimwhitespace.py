"""Trim trailing whitespace."""

import os
import glob
import re
import fire


def trim_whitespace(dir, recurse=True):
    """Trim whitespace from a file.

    dir (str): The directory to trim whitespace in.
    recurse (bool): Flag for recursive operation. Defaults to true.
    """
    files = glob.iglob(dir, recursive=recurse)
    for f in files:
        print(f)


if __name__ == '__main__':
    fire.Fire()
