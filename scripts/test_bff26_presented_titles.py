from pathlib import Path
import re
import unittest

ROOT = Path(__file__).parents[1]


class Bff26PresentedTitlesTests(unittest.TestCase):
    def test_recap_counts_presented_titles_not_finished_screenings(self):
        recap = (ROOT / 'site' / '26.md').read_text(encoding='utf-8')
        landing = (ROOT / 'site' / '27.md').read_text(encoding='utf-8')
        self.assertIn('18 titles presented at different stages of development, including concepts.', recap)
        lineup = next(line for line in recap.splitlines() if 'titles presented across the weekend:' in line)
        titles = re.search(r'<em>(.*?)</em>', lineup).group(1).split(', ')
        self.assertEqual(len(titles), 18)
        self.assertEqual(len(set(titles)), 18)
        self.assertIn('<span class="n">18</span><span class="l">titles presented</span>', recap)
        self.assertIn('<strong>18</strong><span>titles presented</span>', landing)
        self.assertIn('Titles at different stages of development, including concepts.', landing)
        for page in (recap, landing):
            self.assertNotIn('16 finished films screened', page)
            self.assertNotIn('Sixteen finished films screened', page)
            self.assertNotIn('18 finished films screened', page)


if __name__ == '__main__':
    unittest.main()
