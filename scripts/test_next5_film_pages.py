import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILT = ROOT / 'site' / '_site'

# slug -> (strings that must appear on the page, expected schema duration or None)
PAGES = {
    'the-man-who-wouldnt-cry': (
        ['Emil T. Jonsson', 'Björn Boström', 'Stig Dagerman', 'Sweden',
         'Västerås', 'the-man-who-wouldnt-cry-poster.jpg', 'Official Selection'],
        'PT16M',
    ),
    'my-trust-in-you-is-broken': (
        ['Parker Worthington', 'Documentary', 'BTCPay Server', 'Audience Choice',
         'my-trust-in-you-is-broken-title-card.jpg', 'CjpfAZdFbOw'],
        'PT42M',
    ),
    'finding-home': (
        ['Avi Burra', 'Documentary Series', 'Roger9000', 'IndeeHub',
         'finding-home-episode-4-poster.jpg'],
        None,
    ),
    'bitcoin-castle': (
        ['Bruno Schiebel', 'Schloss Bitcoin', 'Germany', 'Best Movie', 'Audience Choice',
         'hf97ofTlZhk'],
        'PT28M',
    ),
    'bitcoin-video-magazine': (
        ['Bitcoin Video Magazine', 'Documentary Series', 'The Bitcoin Motorcycle Diaries',
         'Tim Tayshun', 'bitcoin-video-magazine-logo.jpg'],
        None,
    ),
}


class NextFivePagesTest(unittest.TestCase):
    def test_pages_listing_and_sitemap(self):
        listing = (BUILT / 'cinema' / 'films' / 'index.html').read_text(encoding='utf-8')
        sitemap = (BUILT / 'sitemap.xml').read_text(encoding='utf-8')
        for slug, (needles, duration) in PAGES.items():
            with self.subTest(slug=slug):
                route = BUILT / 'cinema' / 'films' / slug / 'index.html'
                self.assertTrue(route.exists(), slug + ' film route must be generated')
                page = route.read_text(encoding='utf-8')
                self.assertEqual(len(re.findall(r'<h1(?:\s[^>]*)?>', page, re.I)), 1)
                for needle in needles:
                    self.assertIn(needle, page)
                movie = self._movie_schema(page)
                self.assertEqual(movie.get('duration'), duration)
                self.assertNotIn('\u2014', self._main(page))
                self.assertIn('/cinema/films/' + slug + '/', listing)
                self.assertIn('/cinema/films/' + slug + '/', sitemap)

    def test_type_values(self):
        types = {}
        for slug in PAGES:
            page = (BUILT / 'cinema' / 'films' / slug / 'index.html').read_text(encoding='utf-8')
            m = re.search(r'class="cinema-hero-type">([^<]*)<', page) or re.search(r'class="page-context">([^<]*)<', page)
            types[slug] = m.group(1).strip()
        self.assertTrue(types['my-trust-in-you-is-broken'].startswith('Documentary \u00b7 2024'))
        self.assertTrue(types['the-man-who-wouldnt-cry'].startswith('Short'))
        self.assertTrue(types['bitcoin-castle'].startswith('Short'))
        self.assertTrue(types['finding-home'].startswith('Documentary Series'))
        self.assertTrue(types['bitcoin-video-magazine'].startswith('Documentary Series'))

    def test_castle_is_not_listed_as_documentary(self):
        page = (BUILT / 'cinema' / 'films' / 'bitcoin-castle' / 'index.html').read_text(encoding='utf-8')
        self.assertNotEqual(self._movie_schema(page).get('genre'), 'Documentary')

    @staticmethod
    def _main(page):
        return page.split('<main', 1)[-1].split('</main>', 1)[0]

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
