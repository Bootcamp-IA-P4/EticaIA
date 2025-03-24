import unittest
import asyncio
from api.database import get_collection

class TestMongoSave(unittest.TestCase):
    def test_force_insert_article(self):
        async def run():
            test_collection = get_collection(test=True)

            await test_collection.delete_many({})  # Limpia la colección

            dummy_article = {
                "title": "Test Article",
                "link": "https://example.com/test-article",
                "excerpt": "This is a test article.",
                "topic": "Test"
            }

            await test_collection.insert_one(dummy_article)
            count = await test_collection.count_documents({})
            print(f"🗃️ Artículos en la colección de test: {count}")
            self.assertGreaterEqual(count, 1)

        # 👇 Usa un nuevo bucle solo para este test
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(run())
        loop.close()
