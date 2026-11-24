"""Read-only project scanning helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

SKIP_DIRS = {
    ".git", ".hg", ".svn", ".venv", "venv", "__pycache__",
    "node_modules", "vendor", "dist", "build", ".mypy_cache",
    ".pytest_cache", ".ruff_cache",
}
MARKERS = ("TODO", "FIXME", "XXX")


@dataclass(frozen=True)
class Marker:
    path: str
    line: int
    marker: str
    text: str


@dataclass(frozen=True)
class ProjectSummary:
    root: str
    files: int
    lines: int
    skipped: int
    by_extension: dict[str, int]


def iter_files(root: Path, include_hidden: bool = False) -> Iterator[Path]:
    """Yield files in stable order, excluding common generated directories."""
    for current, directories, filenames in os.walk(root):
        directories[:] = sorted(
            name for name in directories
            if name not in SKIP_DIRS and (include_hidden or not name.startswith("."))
        )
        for filename in sorted(filenames):
            if include_hidden or not filename.startswith("."):
                yield Path(current) / filename


def read_utf8(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def scan_markers(root: Path, include_hidden: bool = False) -> list[Marker]:
    """Find marker words in UTF-8 text files without modifying them."""
    root = root.resolve()
    if not root.is_dir():
        raise NotADirectoryError(root)

    found: list[Marker] = []
    for path in iter_files(root, include_hidden):
        content = read_utf8(path)
        if content is None:
            continue
        for line_number, line in enumerate(content.splitlines(), start=1):
            for marker in MARKERS:
                if marker in line:
                    found.append(Marker(str(path.relative_to(root)), line_number, marker, line.strip()))
    return found


def summarize_project(root: Path, include_hidden: bool = False) -> ProjectSummary:
    """Count readable UTF-8 files and lines, grouped by suffix."""
    root = root.resolve()
    if not root.is_dir():
        raise NotADirectoryError(root)

    file_count = 0
    line_count = 0
    skipped = 0
    extensions: dict[str, int] = {}
    for path in iter_files(root, include_hidden):
        content = read_utf8(path)
        if content is None:
            skipped += 1
            continue
        file_count += 1
        line_count += len(content.splitlines())
        extension = path.suffix.lower() or "[no extension]"
        extensions[extension] = extensions.get(extension, 0) + 1

    return ProjectSummary(str(root), file_count, line_count, skipped, extensions)
