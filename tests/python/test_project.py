from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from devtools.project import scan_markers, summarize_project


class ProjectToolsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "src").mkdir()
        (self.root / "src" / "sample.py").write_text(
            "# TODO: finish\nprint('ok')\n# FIXME: edge case\n", encoding="utf-8"
        )
        (self.root / "notes.txt").write_text("plain text\n", encoding="utf-8")
        (self.root / "image.bin").write_bytes(b"\xff\x00\x81")
        (self.root / ".hidden").write_text("XXX hidden\n", encoding="utf-8")
        (self.root / "node_modules").mkdir()
        (self.root / "node_modules" / "ignored.js").write_text("TODO ignored", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_scan_finds_markers_and_skips_generated_and_hidden(self) -> None:
        results = scan_markers(self.root)
        self.assertEqual([item.marker for item in results], ["TODO", "FIXME"])
        self.assertEqual(results[0].path, "src/sample.py")
        self.assertEqual(results[0].line, 1)

    def test_scan_can_include_hidden_files(self) -> None:
        results = scan_markers(self.root, include_hidden=True)
        self.assertEqual([item.marker for item in results], ["TODO", "FIXME", "XXX"])

    def test_summary_counts_text_and_skips_binary(self) -> None:
        result = summarize_project(self.root)
        self.assertEqual(result.files, 2)
        self.assertEqual(result.lines, 4)
        self.assertEqual(result.skipped, 1)
        self.assertEqual(result.by_extension[".py"], 1)
        self.assertEqual(result.by_extension[".txt"], 1)

    def test_missing_directory_raises(self) -> None:
        with self.assertRaises(NotADirectoryError):
            summarize_project(self.root / "missing")


if __name__ == "__main__":
    unittest.main()
