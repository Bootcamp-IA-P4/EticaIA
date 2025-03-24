from scraper import get_articles

def test_scraper_returns_articles():
    articles = get_articles()
    assert isinstance(articles, list)
    assert len(articles) > 0

def test_article_structure():
    article = get_articles()[0]
    assert "title" in article and isinstance(article["title"], str)
    assert "link" in article and article["link"].startswith("http")
    assert "topic" in article
    assert "excerpt" in article
