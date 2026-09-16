#!/usr/bin/env python3
"""Regression checks for the revised manuscript (stdlib only).

Focuses on the defects found in the 2026-09-16 developmental audit:
corrupted case-study shell blocks, broken scaffolding commands, stale
Part/Appendix references, uv interface drift, the degenerate notebook
case study, and the series-standard build and link issues.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHAPTERS = [
    "index.qmd",
    "copyright.qmd",
    "chapters/foundation.qmd",
    "chapters/workflow.qmd",
    "chapters/documentation.qmd",
    "chapters/case-study.qmd",
    "chapters/advanced-techniques.qmd",
    "chapters/project-management.qmd",
    "chapters/distribution.qmd",
    "chapters/notebooks.qmd",
    "chapters/notebook-case-study.qmd",
    "chapters/conclusion.qmd",
    "acknowledgments.qmd",
    "about-author.qmd",
    "appendices/glossary.qmd",
    "appendices/distribution-templates.qmd",
    "appendices/ai-tools.qmd",
    "appendices/checklist.qmd",
    "appendices/editors.qmd",
    "appendices/tools.qmd",
    "appendices/tool-comparison.qmd",
    "appendices/bash-scaffold-script.qmd",
    "appendices/cookiecutter.qmd",
    "appendices/hatch.qmd",
    "appendices/conda.qmd",
    "appendices/venv.qmd",
    "appendices/uv.qmd",
    "appendices/poetry.qmd",
]

STALE_LINKS = (
    "michaelborck.dev",
    "michaelborck.education",
)


def skip_appledouble(paths):
    return [p for p in paths if not p.name.startswith("._")]


def chapter_text(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


class ManuscriptChecks(unittest.TestCase):
    def test_no_stale_links(self):
        for name in CHAPTERS:
            text = chapter_text(name)
            for target in STALE_LINKS:
                with self.subTest(file=name, target=target):
                    self.assertNotIn(target, text)

    def test_no_mermaid_diagrams(self):
        for name in CHAPTERS:
            with self.subTest(file=name):
                self.assertNotIn("{mermaid}", chapter_text(name))

    def test_no_stale_part_or_appendix_references(self):
        for name in CHAPTERS:
            text = chapter_text(name)
            for pattern in (r"\bPart \d\b", r"\bAppendix [A-Z]\b"):
                match = re.search(pattern, text)
                with self.subTest(file=name, pattern=pattern):
                    self.assertIsNone(match, match.group(0) if match else "")

    def test_no_bash_echo_newline_redirects(self):
        # echo does not interpret \n under bash; these commands wrote
        # literal backslash-n into .gitignore/README files.
        for name in CHAPTERS:
            text = chapter_text(name)
            for match in re.finditer(r'echo "[^"]*\\n[^"]*"\s*>>?', text):
                with self.subTest(file=name, cmd=match.group(0)[:60]):
                    self.fail(f"echo with \\n redirect: {match.group(0)}")

    def test_case_study_shell_blocks_are_not_corrupted(self):
        text = chapter_text("chapters/case-study.qmd")
        # The old corruption: file contents dumped into bash fences with
        # announcement comments and orphan EOF lines.
        self.assertNotIn("with the following contents:d", text)
        self.assertNotIn("## Create a file named", text)
        for fence in re.findall(r"```bash\n(.*?)```", text, re.S):
            with self.subTest(block=fence.strip().splitlines()[0][:60]):
                self.assertNotIn("EOF", fence)
                self.assertFalse(fence.lstrip().startswith("# Create a file"))

    def test_case_study_listings_are_labelled(self):
        text = chapter_text("chapters/case-study.qmd")
        for target in ("src/simplebot/core.py", "tests/test_core.py",
                       ".github/workflows/ci.yml"):
            with self.subTest(file=target):
                self.assertIn(f"Create a file named `{target}`", text)

    def test_notebook_case_study_is_qmd_with_anchor(self):
        self.assertFalse((ROOT / "chapters/notebook-case-study.ipynb").exists())
        text = chapter_text("chapters/notebook-case-study.qmd")
        self.assertIn("{#sec-notebook-case-study}", text)

    def test_uv_modes_are_bridged(self):
        text = chapter_text("chapters/workflow.qmd")
        self.assertIn("Two Ways to Drive uv", text)

    def test_download_links_are_site_absolute(self):
        config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
        for target in ("ship-python-orchestrate-ai.pdf",
                       "ship-python-orchestrate-ai.epub"):
            with self.subTest(target=target):
                self.assertIn(f"href: /{target}", config)
                self.assertNotIn(f"href: {target}", config)

    def test_no_stale_action_versions_in_documentation(self):
        text = chapter_text("chapters/documentation.qmd")
        for stale in ("checkout@v3", "setup-python@v4", "codecov-action@v3",
                      "actions-gh-pages@v3", "action-gh-release@v1"):
            with self.subTest(stale=stale):
                self.assertNotIn(stale, text)

    def test_source_encoding_is_utf8(self):
        paths = skip_appledouble(sorted(ROOT.glob("**/*.qmd")))
        for path in paths:
            if "_book" in path.parts or "_print_source" in path.parts:
                continue
            with self.subTest(file=str(path)):
                path.read_text(encoding="utf-8")


if __name__ == "__main__":
    unittest.main(verbosity=2)
