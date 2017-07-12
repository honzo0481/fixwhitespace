"""Unittests for trim whitespace."""

from trimwhitespace import trim_whitespace


def test_trim_with_trailing_whitespace(tmpdir):
    """Trimming files with trailing whitespace should remove the whitespace."""
    folder = tmpdir.mkdir('sub')
    file_handle = folder.join('whitespace.txt')

    with open(file_handle, 'w') as f:
        f.write('a line  \na line  \n')

    trim_whitespace('/tmp/pytest-of-root/pytest-0/test_trim_without_trailing_whi0/sub/*.txt')

    with open(file_handle, 'r') as f:
        for line in f:
            assert line == 'a line\n'


def test_trim_without_trailing_whitespace(tmpdir):
    """Trimming files without trailing whitespace shouldn't change them."""
    folder = tmpdir.mkdir('sub')
    file_handle = folder.join('nowhitespace.txt')
    with open(file_handle, 'w') as f:
        f.write('a line\na line\n')

    trim_whitespace('/tmp/pytest-of-root/pytest-0/test_trim_without_trailing_whi0/sub/*.txt')
    with open(file_handle, 'r') as f:
        for line in f:
            assert line == 'a line\n'
