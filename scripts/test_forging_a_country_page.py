import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILT = ROOT / 'site' / '_site'
SLUG = 'forging-a-country'


class ForgingACountryPageTest(unittest.TestCase):
    def test_film_page_and_listing(self):
        route = BUILT / 'cinema' / 'films' / SLUG / 'index.html'
        self.assertTrue(route.exists(), 'Forging a Country film route must be generated')
        page = route.read_text(encoding='utf-8')
        self.assertEqual(len(re.findall(r'<h1(?:\s[^>]*)?>', page, re.I)), 1)
        self.assertIn('Jessica Solce', page)
        self.assertIn('Encode Productions', page)
        self.assertIn('youtu.be/CvzSx5xfNIo', page)
        self.assertIn('forging-a-country-title-card.jpg', page)
        self.assertNotIn('Official Selection', page)
        self.assertNotIn('BFF', page.split('<main', 1)[-1].split('</main>', 1)[0])
        self.assertEqual(self._movie_schema(page).get('duration'), 'PT33M')
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
