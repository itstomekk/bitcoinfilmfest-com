from pathlib import Path
import unittest

ROOT = Path(__file__).parents[1]


class ArchivePageContractTests(unittest.TestCase):
    cases = {
        "24": {
            "page": "site/24.md",
            "route": "/24/",
            "class_name": "edition-page--bff24",
            "markers": (
                "BFF’24", "European Halving Party", "19–21 April 2024", "Kinoteka",
                "block 840,000", "Official selection", "Menger. Notes on the Margin",
                "My Trust in You Is Broken", "Dirty Coin", "Death Athletic", "Bitcoiners",
                "HODL", "Golden Rabbits", "Best Movie", "Best Story", "Best Short",
                "Audience Choice", "reported metrics", "Archive sources",
            ),
        },
        "23": {
            "page": "site/23.md",
            "route": "/23/",
            "class_name": "edition-page--bff23",
            "markers": (
                "BFF’23", "world’s first Bitcoin FilmFest", "24–26 March 2023", "Kinoteka",
                "The Satoshi Mystery", "HUMAN B", "The Bitcoin Farmer",
                "The Great Reset and the Rise of Bitcoin", "Bond to Unbind",
                "A Sly Roundabout Way", "Open Bitcoin Workshops", "Golden Rabbits",
                "Best Movie", "Audience Choice", "Archive sources",
            ),
        },
    }

    def test_pages_use_shared_layout_and_canonical_routes(self):
        for edition, case in self.cases.items():
            source = (ROOT / case["page"]).read_text(encoding="utf-8")
            with self.subTest(edition=edition):
                self.assertIn("layout: default", source)
                self.assertIn(f"permalink: {case['route']}", source)
                self.assertIn(case["class_name"], source)
                self.assertNotRegex(source, r"<(?:html|head|body|nav|footer)\b")
                self.assertNotIn("<script", source)
                self.assertNotIn("<style", source)
                for marker in case["markers"]:
                    self.assertIn(marker.lower(), source.lower())

    def test_pages_keep_assets_local(self):
        for edition, case in self.cases.items():
            source = (ROOT / case["page"]).read_text(encoding="utf-8")
            with self.subTest(edition=edition):
                self.assertNotIn("wp-content/uploads", source)
                self.assertIn(f"/{edition}/{edition}-assets/", source)


if __name__ == "__main__":
    unittest.main()
