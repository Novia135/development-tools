"""Command-line interface for local project inspection tools."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .project import scan_markers, summarize_project


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="devtools",
        description="Small, read-only utilities for inspecting software projects.",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    for name, description in (
        ("scan", "Find TODO, FIXME, and XXX markers."),
        ("stats", "Summarize text files and lines by extension."),
    ):
        command = commands.add_parser(name, description=description)
        command.add_argument("path", type=Path, help="Directory to inspect.")
        command.add_argument("--include-hidden", action="store_true")
        command.add_argument("--json", action="store_true", help="Print JSON.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.path.exists():
        parser.error(f"path does not exist: {args.path}")
    if not args.path.is_dir():
        parser.error(f"path is not a directory: {args.path}")

    try:
        if args.command == "scan":
            results = scan_markers(args.path, include_hidden=args.include_hidden)
            data = [
                {"path": item.path, "line": item.line, "marker": item.marker, "text": item.text}
                for item in results
            ]
            if args.json:
                print(json.dumps(data, indent=2))
            else:
                for item in results:
                    print(f"{item.path}:{item.line}: {item.marker}: {item.text}")
                print(f"Found {len(results)} marker(s).")
        else:
            result = summarize_project(args.path, include_hidden=args.include_hidden)
            data = {
                "root": result.root,
                "files": result.files,
                "lines": result.lines,
                "skipped_binary_or_unreadable": result.skipped,
                "by_extension": result.by_extension,
            }
            if args.json:
                print(json.dumps(data, indent=2, sort_keys=True))
            else:
                print(f"Project: {result.root}")
                print(f"Text files: {result.files}")
                print(f"Lines: {result.lines}")
                print(f"Skipped binary/unreadable files: {result.skipped}")
                for extension, count in sorted(result.by_extension.items()):
                    print(f"  {extension}: {count} file(s)")
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
