#!/usr/bin/env python3
"""Tests for scripts/build_markdown_copies.py. Run: python3 scripts/test_build_markdown_copies.py"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "build_markdown_copies.py"


def page(href, body_chars=400, canonical="https://bitcoinfilmfest.com/about/", robots=None):
    para = "<p>" + ("Bitcoin film text. " * (body_chars // 18 + 1)) + "</p>"
    link = f'<link rel="alternate" type="text/markdown" href="{href}">' if href else ""
    meta = f'<meta name="robots" content="{robots}">' if robots else ""
    return ("<!DOCTYPE html><html><head><title>T</title>" + meta
            + f'<link rel="canonical" href="{canonical}">' + link + "</head>"
            + f"<body><main><h1>Title</h1>{para}</main><footer>site footer</footer></body></html>")


class BuildMarkdownCopiesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.site = self.root / "_site"
        self.site.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel, text):
        f = self.site / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text, encoding="utf-8")

    def run_script(self, *extra):
        return subprocess.run([sys.executable, str(SCRIPT), "--site", str(self.site), *extra],
                              capture_output=True, text=True, encoding="utf-8")

    def test_writes_copy_at_linked_path(self):
        self.write("about/index.html", page("/about/index.md"))
        r = self.run_script()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        md = (self.site / "about" / "index.md").read_text(encoding="utf-8")
        self.assertIn("Source: https://bitcoinfilmfest.com/about/", md)
        self.assertNotIn("site footer", md)

    def test_fails_on_short_copy(self):
        self.write("about/index.html", page("/about/index.md", body_chars=10))
        r = self.run_script()
        self.assertEqual(r.returncode, 1)
        self.assertIn("< 300", r.stdout)

    def test_fails_on_link_to_other_host(self):
        self.write("about/index.html", page("https://evil.example/x.md"))
        r = self.run_script()
        self.assertEqual(r.returncode, 1)
        self.assertIn("outside the site", r.stdout)

    def test_fails_on_path_escape_and_writes_nothing_outside(self):
        self.write("about/index.html", page("/../escape.md"))
        r = self.run_script()
        self.assertEqual(r.returncode, 1)
        self.assertFalse((self.root / "escape.md").exists())

    def test_fails_when_no_page_links(self):
        self.write("index.html", page(None))
        r = self.run_script()
        self.assertEqual(r.returncode, 1)
        self.assertIn("no built page carries", r.stdout)

    def test_fails_on_noindex_page_with_link(self):
        self.write("x/index.html", page("/x/index.md", robots="noindex, follow"))
        r = self.run_script()
        self.assertEqual(r.returncode, 1)
        self.assertIn("noindex", r.stdout)

    def test_baseurl_is_stripped_for_the_file_path(self):
        self.write("about/index.html", page("/proj/about/index.md"))
        r = self.run_script("--baseurl", "/proj")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue((self.site / "about" / "index.md").exists())

    def test_link_outside_baseurl_fails(self):
        self.write("about/index.html", page("/other/about/index.md"))
        r = self.run_script("--baseurl", "/proj")
        self.assertEqual(r.returncode, 1)


if __name__ == "__main__":
    unittest.main()
