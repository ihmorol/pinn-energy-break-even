"""Regression tests for the repository checker, using small temporary checkouts."""

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_workspace.py"
checker = None
if SCRIPT.is_file():
    spec = importlib.util.spec_from_file_location("check_workspace", SCRIPT)
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)


class WorkspaceChecksTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(checker, "The workspace checker is not implemented yet")
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        for relative in checker.REQUIRED_FILES:
            self.write(relative, "# Shared file\n" if relative.endswith(".md") else "")
        self.write("README.md", "# Project\n\n[Plan](docs/research-plan.md)\n")
        self.write("docs/research-plan.md", "# Research plan\n\n## Fixed scope\n")
        for name in ("research-writing", "literature-check", "experiment-run", "research-review"):
            self.write(
                f".agents/skills/{name}/SKILL.md",
                f"---\nname: {name}\ndescription: Read the project rules for this task.\n---\n\n# Skill\n",
            )
        files = []
        for extension in ("pdf", "docx"):
            relative = f"docs/proposal/ENERGY_CROSSOVER_PROPOSAL.{extension}"
            content = f"Small {extension} fixture".encode()
            (self.root / relative).write_bytes(content)
            files.append({
                "path": relative,
                "sha256": hashlib.sha256(content).hexdigest(),
                "size_bytes": len(content),
            })
        self.manifest = {"schema_version": 1, "files": files}
        self.save_manifest()

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def save_manifest(self):
        self.write("docs/proposal/manifest.json", json.dumps(self.manifest))

    def assert_problem(self, fragment):
        problems = checker.check_workspace(self.root)
        self.assertTrue(problems, "Expected a validation failure")
        self.assertIn(fragment, "\n".join(problems))

    def test_valid_checkout_passes(self):
        self.assertEqual(checker.check_workspace(self.root), [])

    def test_missing_shared_file_is_reported(self):
        (self.root / "AGENTS.md").unlink()
        self.assert_problem("AGENTS.md: missing required file")

    def test_broken_link_reports_its_line(self):
        self.write("README.md", "# Project\n\n[Plan](missing.md)\n")
        self.assert_problem("README.md:3: missing local target")

    def test_links_resolve_from_the_document_directory(self):
        self.write("docs/note.md", "[Home](../README.md)\n[Scope](research-plan.md#fixed-scope)\n")
        self.assertEqual(checker.check_workspace(self.root), [])

    def test_links_allow_encoded_spaces_and_optional_titles(self):
        self.write("docs/a note.md", "# Note\n")
        self.write("README.md", '[Note](docs/a%20note.md "Reading note")\n[Note](<docs/a note.md>)\n')
        self.assertEqual(checker.check_workspace(self.root), [])

    def test_links_allow_balanced_parentheses(self):
        self.write("docs/note(pilot).md", "# Note\n")
        self.write("README.md", "[Note](docs/note(pilot).md)\n")
        self.assertEqual(checker.check_workspace(self.root), [])

    def test_reference_links_are_checked(self):
        self.write("README.md", "[Plan][scope]\n\n[scope]: missing.md\n")
        self.assert_problem("missing local target")

    def test_images_are_checked(self):
        self.write("README.md", "![Result](missing.png)\n")
        self.assert_problem("missing local target")

    def test_external_links_and_fragment_only_links_are_skipped(self):
        self.write("README.md", "[Web](https://example.org/a?q=1)\n[Mail](mailto:team@example.org)\n[Here](#local)\n")
        self.assertEqual(checker.check_workspace(self.root), [])

    def test_code_examples_are_not_treated_as_links(self):
        self.write("README.md", "`[example](missing.md)`\n```markdown\n[Example](missing.md)\n```\n~~~\n![Example](missing.png)\n~~~\n")
        self.assertEqual(checker.check_workspace(self.root), [])

    def test_ignored_directories_are_not_scanned(self):
        for directory in (".git", ".zcode", ".gstack", ".venv", "outputs", "downloads"):
            self.write(f"{directory}/bad.md", "[Bad](missing.md)\n")
        self.assertEqual(checker.check_workspace(self.root), [])

    def test_link_cannot_escape_the_checkout(self):
        self.write("README.md", "[Outside](../outside.md)\n")
        Path(self.temp.name, "outside.md").write_text("outside", encoding="utf-8")
        self.assert_problem("outside the workspace")

    def test_symlink_target_cannot_escape_the_checkout(self):
        outside = Path(self.temp.name, "outside.md")
        outside.write_text("outside", encoding="utf-8")
        link = self.root / "outside-link.md"
        try:
            link.symlink_to(outside)
        except OSError as error:
            self.skipTest(f"Symlinks are unavailable on this machine: {error}")
        self.write("README.md", "[Outside](outside-link.md)\n")
        self.assert_problem("outside the workspace")

    def test_changed_proposal_bytes_fail(self):
        (self.root / "docs/proposal/ENERGY_CROSSOVER_PROPOSAL.pdf").write_bytes(b"changed")
        self.assert_problem("SHA-256 mismatch")

    def test_wrong_proposal_size_fails(self):
        self.manifest["files"][0]["size_bytes"] += 1
        self.save_manifest()
        self.assert_problem("size mismatch")

    def test_malformed_manifest_is_reported(self):
        self.write("docs/proposal/manifest.json", "not json")
        self.assert_problem("invalid JSON")

    def test_manifest_requires_the_two_original_files(self):
        self.manifest["files"].pop()
        self.save_manifest()
        self.assert_problem("must list each submitted file exactly once")

    def test_manifest_rejects_duplicate_paths(self):
        self.manifest["files"].append(self.manifest["files"][0].copy())
        self.save_manifest()
        self.assert_problem("must list each submitted file exactly once")

    def test_manifest_rejects_an_outside_path(self):
        self.manifest["files"][0]["path"] = "../outside.pdf"
        self.save_manifest()
        self.assert_problem("outside the workspace")

    def test_manifest_rejects_invalid_hash_and_size_types(self):
        self.manifest["files"][0]["sha256"] = "not a hash"
        self.manifest["files"][0]["size_bytes"] = True
        self.save_manifest()
        self.assert_problem("invalid hash or size")

    def test_skill_name_must_match_its_directory(self):
        self.write(".agents/skills/research-writing/SKILL.md", "---\nname: wrong-name\ndescription: Write clearly.\n---\n")
        self.assert_problem("skill name must match its directory")

    def test_skill_requires_a_description(self):
        self.write(".agents/skills/research-writing/SKILL.md", "---\nname: research-writing\n---\n")
        self.assert_problem("skill needs a single-line description")

    def test_skill_requires_frontmatter(self):
        self.write(".agents/skills/research-writing/SKILL.md", "# Skill\n")
        self.assert_problem("skill needs YAML frontmatter")

    def test_machine_paths_are_reported_in_docs(self):
        for value in (r"C:\Users\Someone\skill.md", "E:/local/data", "/home/someone/data", "/Users/someone/data"):
            with self.subTest(value=value):
                self.write("docs/note.md", f"Use {value}.\n")
                self.assert_problem("machine-specific path")

    def test_non_utf8_markdown_is_reported(self):
        (self.root / "README.md").write_bytes(b"\xff\xfe")
        self.assert_problem("cannot read UTF-8 text")

    def test_cli_runs_from_another_directory(self):
        result = subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(SCRIPT), "--root", str(self.root)],
            cwd=self.temp.name, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Workspace checks passed", result.stdout)

    def test_cli_fails_for_an_invalid_checkout(self):
        (self.root / "AGENTS.md").unlink()
        result = subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(SCRIPT), "--root", str(self.root)],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("AGENTS.md", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
