import unittest
import asyncio
from httpx import AsyncClient, ASGITransport
from api.main import app

transport = ASGITransport(app=app)

class TestArticlesAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(cls.loop)
        cls.client = AsyncClient(transport=transport, base_url="http://test")

    @classmethod
    def tearDownClass(cls):
        cls.loop.run_until_complete(cls.client.aclose())
        cls.loop.close()

    def test_get_all_articles(self):
        async def run_test():
            response = await self.client.get("/articles/")
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json(), list)

        self.loop.run_until_complete(run_test())

    def test_get_article_by_id(self):
        async def run_test():
            res_all = await self.client.get("/articles/")
            articles = res_all.json()
            if not articles:
                self.skipTest("No hay artículos en la base de datos")
            article_id = articles[0]["_id"]
            res_one = await self.client.get(f"/articles/{article_id}")
            self.assertEqual(res_one.status_code, 200)
            self.assertEqual(res_one.json()["_id"], article_id)

        self.loop.run_until_complete(run_test())
