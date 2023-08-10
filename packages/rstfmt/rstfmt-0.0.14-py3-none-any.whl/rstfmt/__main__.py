import argparse
import difflib
import glob
import os
import sys
from contextlib import nullcontext
from typing import Any, ContextManager, TextIO, cast

from . import debug, rst_extras, rstfmt
from ._version import __version__

STDIN = "-"


def do_file(args, fn, misformatted):
    cm = cast(ContextManager[TextIO], nullcontext(sys.stdin) if fn == STDIN else open(fn))
    with cm as f:
        inp = f.read()
    doc = rstfmt.parse_string(inp)

    if args.verbose:
        print("=" * 60, fn, file=sys.stderr)
        debug.dump_node(doc, sys.stderr)

    if args.test:
        try:
            debug.run_test(doc)
        except AssertionError as e:
            raise AssertionError(f"Failed consistency test on {fn}!") from e
        return

    output = rstfmt.format_node(args.width, doc)

    if args.check or args.diff:
        if output != inp:
            misformatted.append(("Standard input" if fn == STDIN else fn, inp, output))
        return

    if fn != STDIN and output == inp:
        return

    cm = cast(ContextManager[TextIO], nullcontext(sys.stdout) if fn == STDIN else open(fn, "w"))
    with cm as f:
        f.write(output)


def main() -> None:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--version", action="store_true", help="show rstfmt version and exit")
    parser.add_argument(
        "--check",
        action="store_true",
        help="don't update files, but exit with nonzero status if any files are not formatted",
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="don't update files, but show a diff of what would change",
    )
    parser.add_argument(
        "-w", "--width", type=int, default=72, help="the target line length in characters"
    )
    parser.add_argument(
        "--ext",
        default="rst",
        help="the extension of files to look at when passed a directory (default `rst`)",
    )
    parser.add_argument(
        "--test", action="store_true", help="[internal] run tests instead of updating files"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="[internal] print extra debugging information"
    )
    parser.add_argument("paths", nargs="*", help="files/directories to run on", metavar="path")

    args = parser.parse_args()

    if args.version:
        print(f"rstfmt {__version__}")
        return

    rst_extras.register()

    misformatted = []

    for path in args.paths or [STDIN]:
        if os.path.isdir(path):
            for f in glob.iglob(os.path.join(path, "**", "*." + args.ext), recursive=True):
                do_file(args, f, misformatted)
        else:
            do_file(args, path, misformatted)

    if misformatted:
        for fn, old, new in misformatted:
            if args.diff:
                old = old.splitlines(keepends=True)
                new = new.splitlines(keepends=True)
                sys.stdout.writelines(difflib.unified_diff(old, new, fromfile=fn, tofile=fn))
            else:
                print(fn, "is not correctly formatted!")
        sys.exit(1)


if __name__ == "__main__":
    main()
