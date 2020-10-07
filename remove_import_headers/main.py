#!/usr/bin/env python3
"""
Python script to remove import comment headers from python source files
"""
import pathlib
import re
import sys

def remove_comments(files):
    """
    Remove import comments, 'Import Python libs', 'Import salt libs', etc
    """
    _files = []
    for path in files:
        if not path:
            continue
        _files.append(path)
    if not _files:
        sys.exit(0)

    # Resolve paths
    _files = [
        pathlib.Path(fname).resolve() for fname in _files
    ]

    comments_regex = re.compile(
        r"^# ([I|i])mports? .*(([L|l])ibs)\n",
        re.MULTILINE
    )

    for path in _files:
        contents = path.read_text()
        fixed = comments_regex.sub("", contents)
        if fixed == contents:
            continue
        path.write_text(fixed)
    sys.exit(0)


def main():
    remove_comments(sys.argv[1:])


if __name__ == "__main__":
    main()
