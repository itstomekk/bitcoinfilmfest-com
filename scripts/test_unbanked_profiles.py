"""Regression checks on the generated Unbanked and Unbankable film profiles."""
import json
import os
import unittest
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(os.environ.get('BFF_TEST_SITE', Path(__file__).resolve().parents[1] / 'site' / '_site'))

class FilmProfilesTest(unittest.TestCase):
    def page(self, slug):
        return BeautifulSoup((ROOT / 'cinema' / 'films' / slug / 'index.html').read_text(encoding='utf-8'), 'html.parser')

    def test_unbanked_shows_both_official_directors(self):
        page = self.page('unbanked')
        credits = page.select_one('.cinema-profile-meta').get_text(' ', strip=True)
        self.assertIn('David Kuhn', credits)
        self.assertIn('Lauren Sieckmann', credits)

    def test_unbanked_schema_has_two_distinct_directors(self):
        page = self.page('unbanked')
        nodes = [node for script in page.select('script[type="application/ld+json"]')
                 for data in [json.loads(script.string)]
                 for node in data.get('@graph', [data])]
        movie = next(node for node in nodes if node.get('@type') == 'Movie')
        self.assertEqual(movie['director'], [
            {'@type': 'Person', 'name': 'David Kuhn'},
            {'@type': 'Person', 'name': 'Lauren Sieckmann'},
        ])

    def test_unbanked_does_not_repeat_unbankable_western_systems_framing(self):
        page = self.page('unbanked')
        self.assertNotIn('Western financial systems are the sole solution', page.get_text(' ', strip=True))

    def test_unbankable_seven_countries_not_all_african(self):
        page = self.page('unbankable')
        self.assertNotIn('seven African countries', page.get_text(' ', strip=True))
        self.assertIn('seven countries', page.get_text(' ', strip=True))

    def test_unbankable_production_company(self):
        page = self.page('unbankable')
        nodes = [node for script in page.select('script[type="application/ld+json"]')
                 for data in [json.loads(script.string)]
                 for node in data.get('@graph', [data])]
        movie = next(node for node in nodes if node.get('@type') == 'Movie')
        self.assertEqual(movie['productionCompany']['name'], 'Mbuntu Media')

    def test_unbankable_links_to_current_bff_archive(self):
        page = self.page('unbankable')
        links = {a.get('href') for a in page.select('a[href]')}
        self.assertIn('https://bitcoinfilmfest.com/25/', links)
        self.assertNotIn('https://bitcoinfilmfest.com/part-one-official-selection-feature-films-at-bff25', links)

    def test_unbankable_keeps_director(self):
        self.assertIn('Luke Willms', self.page('unbankable').select_one('.cinema-profile-meta').get_text(' ', strip=True))

if __name__ == '__main__':
    unittest.main()
