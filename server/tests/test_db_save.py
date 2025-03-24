import pytest
from scraper import get_articles, save_to_mongo
from api.database import get_collection

@pytest.mark.asyncio
async def test_save_to_test_db():
    test_collection = get_collection(test=True)
    await test_collection.delete_many({})  # Limpiar antes

    articles = get_articles()
    assert articles

    await save_to_mongo(articles)

    count = await test_collection.count_documents({})
    assert count >= len(articles) * 0.8
