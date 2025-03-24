import pytest
from httpx import AsyncClient
from api.main import app

@pytest.mark.asyncio
async def test_get_articles():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/articles")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "title" in data[0]
        assert "link" in data[0]
