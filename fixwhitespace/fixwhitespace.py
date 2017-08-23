"""Fix whitespace issues."""

import os
import re


def find_files(top, exts):
    """Return a list of file paths with one of the given extensions.

    Args:
        top (str): The top level directory to search in.
        exts (tuple): a tuple of extensions to search for.
    Returns:
        a list of matching file paths.
    """
    return [os.path.join(dirpath, name)
            for dirpath, dirnames, filenames in os.walk(top)
            for name in filenames
            if name.endswith(exts)]


def fix_whitespace(issue, exts, top, n=0):
    """Loop over a file and fix whitespace.

    Args:
        issue (str): the whitespace issue to fix.
            `trim`: trim whitespace from the ends of lines. Preserves line endings.
            `tabs2spaces`: Convert tabs at the fronts of lines.

        top (str): The top level directory to operate in.
        exts (tuple): A tuple of extensions to process.
        n (optional): The number of spaces to replace each tab with. Default is 2.
    """
    issue_map = {
        'trim': r'[ \t]+$',
        'tabs2spaces': r'^\t',
    }

    files = find_files(top, exts)

    for f in files:
        lines = []
        with open(f, 'r') as f:
            for line in f:
                lines.append(re.sub(issue_map[issue], ' ' * n, line))
        with open(f, 'w') as f:
            f.writelines(lines)


def main(issue, top, exts, n=None):
    """CLI hook."""
    if n:
        fix_whitespace(issue, top, exts, n)
    else:
        fix_whitespace(issue, top, exts)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('issue')
    parser.add_argument('top')
    parser.add_argument('-n')
    parser.add_argument('exts', nargs=argparse.REMAINDER)

    kwargs = vars(parser.parse_args())
    kwargs['exts'] = tuple(kwargs['exts'])

    main(**kwargs)
