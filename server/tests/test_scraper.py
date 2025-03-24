import unittest
from scraper import get_articles

class TestScraper(unittest.TestCase):
    def test_scraper_returns_articles(self):
        articles = get_articles()
        self.assertIsInstance(articles, list)
        self.assertGreater(len(articles), 0)

    def test_article_structure(self):
        article = get_articles()[0]
        self.assertIn("title", article)
        self.assertIsInstance(article["title"], str)
        self.assertIn("link", article)
        self.assertTrue(article["link"].startswith("http"))
        self.assertIn("topic", article)
        self.assertIn("excerpt", article)
