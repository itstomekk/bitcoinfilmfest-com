from pathlib import Path
import unittest

ROOT = Path(__file__).parents[1]
PAGE = ROOT / "site" / "404.html"


class Bff404PageContractTests(unittest.TestCase):
    def setUp(self):
        self.source = PAGE.read_text(encoding="utf-8")

    def test_page_uses_shared_paper_screen_shell(self):
        for marker in ("layout: default", 'screen: paper', 'robots: "noindex, nofollow"'):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.source)

    def test_page_has_useful_programme_navigation(self):
        for marker in (
            "This reel's missing a frame.",
            "Back to the lobby",
            "Explore the Cinema hub",
            "Enter BFF’27",
            "{{ '/' | relative_url }}",
            "{{ '/cinema/' | relative_url }}",
            "{{ '/27/' | relative_url }}",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.source)

    def test_page_reuses_site_shell_without_duplicate_global_markup(self):
        self.assertNotRegex(self.source, r"<(?:html|head|body|footer)\b")
        self.assertIn('aria-label="Find your way around"', self.source)
        self.assertNotIn("<style", self.source)
        self.assertNotIn("<script", self.source)


if __name__ == "__main__":
    unittest.main()
