"""Unittests for trim whitespace."""

from fixwhitespace import trim, tabs2spaces, find_files


def test_trim_with_trailing_whitespace(tmpdir):
    """Trimming files with trailing whitespace should remove the whitespace."""
    folder = tmpdir.mkdir('sub')
    file_handle = folder.join('whitespace.txt')
    file_handle.write('a line  \na line  \n')

    trim(folder, ('.txt'))

    with open(file_handle, 'r') as f:
        for line in f:
            print(repr(line))
            assert line == 'a line\n'


def test_trim_without_trailing_whitespace(tmpdir):
    """Trimming files without trailing whitespace shouldn't change them."""
    folder = tmpdir.mkdir('sub')
    file_handle = folder.join('nowhitespace.txt')
    file_handle.write('a line\na line\n')

    trim(folder, ('.txt'))

    with open(file_handle, 'r') as f:
        for line in f:
            assert line == 'a line\n'


def test_tabs2spaces_without_tabs(tmpdir):
    """Converting tabs in a file without tabs shouldn't alter the file."""
    folder = tmpdir.mkdir('sub')
    file_handle = folder.join('notabs.txt')
    file_handle.write('    a line\n    a line\n')

    tabs2spaces(folder, ('.txt'))

    with open(file_handle, 'r') as f:
        for line in f:
            assert line == '    a line\n'


def test_tabs2spaces_with_tabs(tmpdir):
    """Converting tabs in a file containing tabs should replace them."""
    folder = tmpdir.mkdir('sub')
    file_handle = folder.join('tabs.txt')
    file_handle.write('	line 1\n		line 2\n')
    n = 2

    tabs2spaces(folder, ('.txt'), n=n)

    with open(file_handle, 'r') as f:
        for i, line in enumerate(f, start=1):
            assert line == '%sline %s\n' % (' ' * i * n, i)


def test_find_files_returns_only_files_with_correct_extensions(tmpdir):
    """All files with extensions in `exts` should be returned and no others."""
    folder = tmpdir.mkdir('sub')
    txt = folder.join('file1.txt').write('foo') #noqa
    py = folder.join('file2.py').write('foo') # noqa

    exts = ('.txt')
    files = find_files(folder, exts=exts)

    # only keep the extensions - makes the assert simpler.
    files = [f[-4:] for f in files]

    assert '.txt' in files


def test_find_files_returns_files_in_nested_folders(tmpdir):
    """Matching files in nested folders should be returned."""
