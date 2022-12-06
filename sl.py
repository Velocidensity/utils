#!/usr/bin/python3
import argparse
import os
from pathlib import Path


def link(src: Path, dst: Path, hard: bool = False):
    if dst.is_dir():
        dst = dst / src.name

    if hard:
        return os.link(src, dst)

    os.symlink(src, dst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input',
        nargs='*',
        default=[],
        type=Path,
        help='Input file(s)'
    )

    parser.add_argument(
        'output',
        type=Path,
        help='Output path'
    )

    parser.add_argument(
        '-H',
        dest='hard',
        default=False,
        action='store_true',
        help='Create a hard link (default is soft link)'
    )

    args = parser.parse_args()
    if len(args.input) > 1 and not args.output.is_dir():
        raise ValueError('Output must be a directory if multiple input files are given')

    for path in args.input:
        link(path.resolve(), args.output.resolve(), hard=args.hard)
