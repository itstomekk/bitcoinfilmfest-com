import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILT = ROOT / 'site' / '_site'
SLUG = 'satoshi-jason-zada'


class SatoshiZadaPageTest(unittest.TestCase):
    def test_film_page_and_listing(self):
        route = BUILT / 'cinema' / 'films' / SLUG / 'index.html'
        self.assertTrue(route.exists(), 'Jason Zada film route must be generated')
        page = route.read_text(encoding='utf-8')
        self.assertEqual(len(re.findall(r'<h1(?:\s[^>]*)?>', page, re.I)), 1)
        self.assertIn('Jason Zada', page)
        self.assertIn('spring 2027', page)
        self.assertIn('release date', page.lower())
        self.assertIn('variety.com/2026/film/global/tristan-thompson-bitcoin-creator-movie-satoshi-producer-1236938246/', page)
        self.assertNotIn('datePublished', self._movie_schema(page))
        listing = (BUILT / 'cinema' / 'films' / 'index.html').read_text(encoding='utf-8')
        self.assertIn('/cinema/films/' + SLUG + '/', listing)

    @staticmethod
    def _movie_schema(page):
        for text in re.findall(r'<script type="application/ld\+json">(.*?)</script>', page, re.S):
            data = json.loads(text)
            for node in data.get('@graph', [data]):
                if node.get('@type') == 'Movie':
                    return node
        raise AssertionError('Movie JSON-LD missing')


if __name__ == '__main__':
    unittest.main()
