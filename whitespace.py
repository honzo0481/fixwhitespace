"""Trim trailing whitespace."""

import os
import sys
import re

def find_files(top, exts):
    """Return a generator that yields

    """
    return (os.path.join(dirpath, name)
            for dirpath, dirnames, filenames in os.walk(top)
            for name in filenames
            if name.endswith(exts))


def trim(top, exts):
    """Trim whitespace from files.

    top (str): The top level directory to operate in.
    exts (tuple): A tuple of extensions to process.
    """
    files = [os.path.join(dirpath, name)
             for dirpath, dirnames, filenames in os.walk(top)
             for name in filenames
             if name.endswith(exts)]

    for item in files:
        lines = []
        with open(item, 'r') as f:
            for line in f:
                lines.append(re.sub(r'[ \t]+$', '', line))
        with open(item, 'w') as f:
            f.writelines(lines)


def tabs2spaces(top, exts, n=2):
    """Convert tabs to spaces in a set of files. Ignores tabs enclosed in quotes.

    top (str): The top level directory to operate in.
    exts (tuple): A tuple of extensions to process.
    n (optional): The number of spaces to replace each tab with. Default is 2.
    """
    files = [os.path.join(dirpath, name)
             for dirpath, dirnames, filenames in os.walk(top)
             for name in filenames
             if name.endswith(exts)]

    for item in files:
        lines = []
        with open(item, 'r') as f:
            for line in f:
                lines.append(re.sub(r'\t', ' ' * n, line))
        with open(item, 'w') as f:
            f.writelines(lines)


def spaces2tabs(top, exts):
    """Raise an exception. All in good fun."""
    raise Exception('Nope!')


def main():
    """CLI hook."""
    trim(sys.argv[1])


if __name__ == '__main__':
    main()
