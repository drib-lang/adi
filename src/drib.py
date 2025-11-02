import sys
import argparse

from lexer import Lexer
from pathlib import Path
from parser import Parser
from builtins_ import env


def compile_to_python(source: str) -> str:
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse_program()


def run_code(python_code: str) -> int:
    try:
        exec(python_code, env, env)
        return 0
    except Exception as e:
        print(f"Error while executing Drib code: {e}", file=sys.stderr)
        return 1


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(2)
    except OSError as e:
        print(f"Could not read {path}: {e}", file=sys.stderr)
        sys.exit(2)


def write_text(path: Path, content: str) -> None:
    try:
        path.write_text(content, encoding="utf-8")
    except OSError as e:
        print(f"Could not write {path}: {e}", file=sys.stderr)
        sys.exit(2)


def build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="drib",
        description="Run Drib files, emit Python, or start the REPL.",
    )
    p.add_argument(
        "file",
        nargs="?",
        type=Path,
        help="Path to a .drib source file. If omitted, starts the REPL.",
    )
    p.add_argument(
        "-p",
        "--python",
        action="store_true",
        help="Print translated Python to stdout and exit.",
    )
    p.add_argument(
        "-o",
        "--out",
        type=Path,
        help="Write translated Python to this path.",
    )
    p.add_argument(
        "-v",
        "--version",
        action="version",
        version="drib 0.2.0",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_argparser().parse_args(argv)

    if not args.file and not args.eval:
        from repl import run_repl

        run_repl(Lexer, Parser, env)
        return 0

    source = read_text(args.file)
    python_code = compile_to_python(source)

    if args.out:
        if args.out.parent and not args.out.parent.exists():
            print(
                f"Output directory does not exist: {args.out.parent}",
                file=sys.stderr,
            )
            return 2
        write_text(args.out, python_code)
        return 0

    if args.python:
        print(python_code)
        return 0

    return run_code(python_code)


if __name__ == "__main__":
    raise SystemExit(main())
