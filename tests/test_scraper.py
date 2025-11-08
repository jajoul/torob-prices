import unittest
from src.torob_less_price_finder.cli import scrape_torob_prices

class TestScraper(unittest.TestCase):

    def test_scrape_torob_prices(self):
        # Test with a common search query
        results = scrape_torob_prices("iphone", "https://torob.com/search/")
        self.assertIsInstance(results, list)

if __name__ == '__main__':
    unittest.main()
