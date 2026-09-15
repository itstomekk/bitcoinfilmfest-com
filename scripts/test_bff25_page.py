from pathlib import Path
import unittest


PAGE = Path(__file__).parents[1] / "site" / "bff25.md"
LEGACY_PAGE = Path(__file__).parents[1] / "site" / "bff25-legacy.md"


class Bff25PageContractTests(unittest.TestCase):
    def setUp(self):
        self.source = PAGE.read_text(encoding="utf-8")

    def test_page_has_archive_programme_contract(self):
        required = (
            "edition-page--bff25",
            "Beyond the Frame",
            "European Bitcoin Pizza Day",
            "Official selection",
            "PoWies",
            "UNBANKABLE",
            "SATOSHI: THE CREATION OF BITCOIN",
            "Archive-only ticket tiers",
            "Why Bitcoin FilmFest?",
            "Why Warsaw?",
            "Travel &amp; Commute",
            "Bitcoin in Warsaw",
            "Why sponsor?",
            "How to submit my film?",
            "Best Movie",
            "Best Story",
            "Best Short",
            "Audience Choice",
            "Bitcoin Cinema Digest",
            "bff25-photo-rail",
            "Results &amp; press",
            "No More Inflation",
            "Mempool",
            "Network Effect",
            "200+ attendees",
        )
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker, self.source)

    def test_page_uses_only_shared_layout_shell(self):
        self.assertIn("layout: default", self.source)
        self.assertNotRegex(self.source, r"<(?:(?:html)|(?:head)|(?:body)|nav|footer)\\b")
        self.assertNotIn("<script", self.source)
        self.assertNotIn("<style", self.source)

    def test_page_uses_canonical_route(self):
        self.assertIn("permalink: /25/", self.source)
        self.assertNotIn("permalink: /bff25/", self.source)
    def test_legacy_route_redirects_to_canonical(self):
        legacy = LEGACY_PAGE.read_text(encoding="utf-8")
        self.assertIn("permalink: /bff25/", legacy)
        self.assertIn("redirect_to: /25/", legacy)
        self.assertIn("{{ '/25/' | relative_url }}", legacy)


if __name__ == "__main__":
    unittest.main()
