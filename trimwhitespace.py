"""Trim trailing whitespace."""

import os
import sys
import re


def trim_whitespace(top, exts):
    """Trim whitespace from a file.

    path (str): The directory to operate in.
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


def main():
    """CLI hook."""
    trim_whitespace(sys.argv[1])


if __name__ == '__main__':
    main()
