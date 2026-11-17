"""Tests for the Markdown cache script. Fake converters stand in for MarkItDown."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "to_markdown.py"
spec = importlib.util.spec_from_file_location("to_markdown", SCRIPT)
to_markdown = importlib.util.module_from_spec(spec)
spec.loader.exec_module(to_markdown)


class CompactTests(unittest.TestCase):
    def test_token_estimate_counts_non_ascii_heavier(self):
        self.assertEqual(to_markdown.approx_tokens("abcdefgh"), 2)
        self.assertEqual(to_markdown.approx_tokens("শক্তি"), 5)


    def test_table_padding_is_removed_but_cells_kept(self):
        text = "| a      | bb   |\n| ------ | ---- |\n| 1.25   | x    |\n\n\n\nend   \n"
        self.assertEqual(
            to_markdown.compact_markdown(text),
            "| a | bb |\n| --- | --- |\n| 1.25 | x |\n\nend\n",
        )

    def test_pdf_cleanup_fixes_ligatures_and_keeps_numbers_apart(self):
        page = "diﬀerential ﬁeld\n" + "\n".join("1234567") + "\nnext\n12\n34\n"
        cleaned = to_markdown.clean_pdf_page(page)
        self.assertIn("differential field", cleaned)
        self.assertIn("1 2 3 4 5 6 7", cleaned)
        self.assertIn("12\n34", cleaned)  # short runs are left alone

    def test_pdf_cleanup_joins_stamp_split_by_blank_lines(self):
        page = "7\n1\n0\n2\n\nv\no\nN\n\nTitle of paper\n"
        self.assertEqual(to_markdown.clean_pdf_page(page), "7 1 0 2 v o N\n\nTitle of paper\n")

    def test_pages_get_markers(self):
        text = to_markdown.pages_to_markdown(["first", "second"])
        self.assertIn("<!-- page 1 -->\n\nfirst", text)
        self.assertIn("<!-- page 2 -->\n\nsecond", text)


class CacheTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        self.out = self.root / "outputs" / "markdown-cache"
        self.calls = []
        self.converters = {
            "pdf_pages": lambda path: self.calls.append(path.name) or ["page one", "page two"],
            "generic": lambda path: self.calls.append(path.name) or "# Title\n\nBody",
        }
        (self.root / "papers" / "a").mkdir(parents=True)
        (self.root / "papers" / "a" / "paper.pdf").write_bytes(b"%PDF fake")
        (self.root / "papers" / "notes.docx").write_bytes(b"fake docx")
        (self.root / "papers" / "data.csv").write_text("x,y\n1,2\n", encoding="utf-8")

    def run_convert(self, **kwargs):
        return to_markdown.convert_paths(
            [self.root / "papers"], self.out, root=self.root,
            converters=self.converters, log=lambda message: None, **kwargs,
        )

    def test_converts_mirrors_paths_and_skips_unchanged(self):
        self.assertEqual(self.run_convert(), (2, 0, 0))
        cached = self.out / "papers" / "a" / "paper.pdf.md"
        self.assertTrue(cached.read_text(encoding="utf-8").startswith("<!-- page 1 -->"))
        self.assertTrue((self.out / "papers" / "notes.docx.md").is_file())
        self.assertFalse((self.out / "papers" / "data.csv.md").exists())  # CSV is already text
        index = json.loads((self.out / "index.json").read_text(encoding="utf-8"))["files"]
        self.assertEqual(index["papers/a/paper.pdf"]["pages"], 2)
        self.assertIn("papers/notes.docx", (self.out / "INDEX.md").read_text(encoding="utf-8"))

        self.calls.clear()
        self.assertEqual(self.run_convert(), (0, 2, 0))
        self.assertEqual(self.calls, [])

        (self.root / "papers" / "notes.docx").write_bytes(b"changed docx")
        self.assertEqual(self.run_convert(), (1, 1, 0))

    def test_removed_source_drops_its_cache(self):
        self.run_convert()
        (self.root / "papers" / "notes.docx").unlink()
        self.run_convert()
        self.assertFalse((self.out / "papers" / "notes.docx.md").exists())
        index = json.loads((self.out / "index.json").read_text(encoding="utf-8"))["files"]
        self.assertNotIn("papers/notes.docx", index)

    def test_one_failure_does_not_stop_the_batch(self):
        def broken(path):
            raise ValueError("bad file")

        self.converters["pdf_pages"] = broken
        self.assertEqual(self.run_convert(), (1, 0, 1))

    def test_overview_reports_costs_without_converting(self):
        self.run_convert()
        text = to_markdown.overview([self.root / "papers"], self.out, root=self.root)
        self.assertIn("3 file(s)", text)
        self.assertIn("cached: papers/a/paper.pdf.md", text)
        self.assertIn("papers/data.csv", text)
        self.assertIn("tok text", text)


if __name__ == "__main__":
    unittest.main()
