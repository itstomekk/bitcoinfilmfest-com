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
         'Västerås', 'the-man-who-wouldnt-cry-poster.jpg', 'Official Selection',
         'player.vimeo.com/video/638899496', 'the-man-who-wouldnt-cry-still-1.jpg',
         'the-man-who-wouldnt-cry-still-4.jpg', 'Oddvar Fågelsson', 'Peter Nylander',
         'Bucharest ShortCut Cinefest', 'imdb.com/title/tt8960272'],
        'PT16M',
    ),
    'my-trust-in-you-is-broken': (
        ['Parker Worthington', 'Documentary', 'BTCPay Server', 'Audience Choice',
         'my-trust-in-you-is-broken-title-card.jpg', '8ywHizrZfAo', 'CjpfAZdFbOw'],
        'PT42M',
    ),
    'finding-home': (
        ['Avi Burra', 'Documentary Series', 'Roger9000', 'IndeeHub',
         'finding-home-poster.jpg', 'finding-home-episode-4-poster.jpg',
         'finding-home-episode-2-poster.jpg', 'finding-home-episode-3-poster.jpg',
         'Parker Worthington', 'Grafton Clark', 'Lahav Levi',
         'indeehub.studio/watch/trailer/7f4395ae-b380-4797-a573-0e25283e16ca'],
        None,
    ),
    'bitcoin-castle': (
        ['Bruno Schiebel', 'Schloss Bitcoin', 'Germany', 'Best Movie', 'Audience Choice',
         'hf97ofTlZhk', 'Sami Hammi', 'Fernando Tábora', 'Michael Ep', 'Q-pZWvbNLa0'],
        'PT28M',
    ),
    'bitcoin-video-magazine': (
        ['Bitcoin Video Magazine', 'Documentary Series', 'The Bitcoin Motorcycle Diaries',
         'Tim Tayshun', 'bitcoin-video-magazine-logo.jpg', 'GVwE-h6ZTHY', 'Jv4QECI6cSA'],
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

    def test_sitemap_lastmod_is_set_from_front_matter(self):
        sitemap = (BUILT / 'sitemap.xml').read_text(encoding='utf-8')
        for slug in list(PAGES) + ['forging-a-country']:
            with self.subTest(slug=slug):
                m = re.search(r'<loc>[^<]*/cinema/films/' + slug + r'/</loc>\s*<lastmod>([^<]*)</lastmod>', sitemap)
                self.assertIsNotNone(m, slug + ' needs a lastmod in sitemap.xml')
                self.assertTrue(m.group(1).startswith('2026-11-07'), m.group(1))

    def test_imdb_ids_are_in_schema(self):
        for slug, imdb in (('the-man-who-wouldnt-cry', 'tt8960272'), ('forging-a-country', 'tt34094710')):
            with self.subTest(slug=slug):
                page = (BUILT / 'cinema' / 'films' / slug / 'index.html').read_text(encoding='utf-8')
                self.assertEqual(self._movie_schema(page).get('sameAs'), 'https://www.imdb.com/title/' + imdb + '/')

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
