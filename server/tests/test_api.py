import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_all_articles():
    response = client.get("/articles")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_article_by_id():
    res_all = client.get("/articles")
    articles = res_all.json()
    if not articles:
        pytest.skip("No hay artículos en la base de datos")
    
    article_id = articles[0]["_id"]
    res_one = client.get(f"/articles/{article_id}")
    assert res_one.status_code == 200
    one_article = res_one.json()
    assert one_article["_id"] == article_id
