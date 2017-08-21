# fixwhitespace
Trim whitespace or convert tabs to spaces in a file or files in a directory.

run the tests in a container:
> $ docker run --rm -v $(pwd):/code --entrypoint python fixwhitespace -m pytest /code/tests

run them without a container:
> $ pytest

trim whitespace on all files in a directory with a matching extension:
> $ fixwhitespace trim /path/to/dir .ext1 .ext2

convert tabs to spaces on all files in a directory with a matching extension:
> $ fixwhitespace tabs2spaces /path/to/dir .ext1 .ext2
