from pathlib import Path
import unittest

ROOT = Path(__file__).parents[1]
PAGE = ROOT / "site" / "27.md"


class Bff27PageContractTests(unittest.TestCase):
    def setUp(self):
        self.source = PAGE.read_text(encoding="utf-8")

    def test_page_has_landing_page_contract(self):
        required = (
            "layout: default",
            "permalink: /27/",
            "edition-page--current",
            "BFF’27",
            "The next frame",
            "24–27 June 2027",
            "Warsaw",
            "Tickets coming soon",
            "Kinoteka, Warsaw",
            "bff27-btn--soon",
            "BFF27%20tickets%20-%20tell%20me%20first",
            "Opening party",
            "Films &amp; panels",
            "Gala, awards &amp; goodbye party",
            "BFF27%20film%20submission",
            "BFF27%20collaboration",
            "What is BFF?",
        )
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker, self.source)

    def test_page_uses_shared_shell(self):
        self.assertNotRegex(self.source, r"<(?:html|head|body|nav|footer)\b")
        self.assertNotIn("<script", self.source)
        self.assertNotIn("<style", self.source)

    def test_page_uses_existing_local_archive_assets(self):
        for asset in (
            "/26/26-assets/rabbit.png",
            "/26/26-assets/photos/e25-04.jpg",
            "/26/26-assets/photos/e24-06.jpg",
            "/26/26-assets/photos/e25-06.jpg",
        ):
            self.assertIn(asset, self.source)


if __name__ == "__main__":
    unittest.main()
