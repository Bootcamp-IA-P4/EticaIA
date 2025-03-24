import requests
from bs4 import BeautifulSoup
from api.database import get_collection
import asyncio

URL = "https://www.technologyreview.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}
collection = get_collection()


def get_articles():
    response = requests.get(URL, headers=HEADERS)

    if response.status_code != 200:
        print(f"Error {response.status_code}: No se pudo acceder a la página.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for article_tag in soup.find_all("a", href=True):
        title_tag = article_tag.find("h3")
        if not title_tag or not title_tag.text.strip():
            continue

        link = article_tag["href"]
        if not link.startswith("http"):
            link = f"https://www.technologyreview.com{link}"

        topic_tag = article_tag.find_previous(
            "span", class_="homepageEyebrow__text--e755f0749c2ee2902850fa01b4150520"
        )
        topic = topic_tag.text.strip() if topic_tag else "Unknown"

        # Buscamos un excerpt
        parent = article_tag.find_parent()
        excerpt_div = parent.find("div", class_="homepageStoryCard__dek--7c9e3c85841df43b5fb2385cdf2b46e3") if parent else None
        excerpt = excerpt_div.p.get_text(strip=True) if excerpt_div and excerpt_div.p else None


        articles.append({
            "title": title_tag.text.strip(),
            "link": link,
            "topic": topic,
            "excerpt": excerpt
        })

    return articles


async def save_to_mongo(data):
    saved_count = 0
    updated_count = 0

    for article in data:
        result = await collection.update_one(
            {"title": article["title"]},
            {"$set": article},
            upsert=True,
        )

        if result.matched_count == 0:
            print(f"✅ Guardado: {article['title']}")
            saved_count += 1
        else:
            print(f"♻️ Actualizado: {article['title']}")
            updated_count += 1

    print(f"🗃️ Total guardados: {saved_count}, actualizados: {updated_count}")


if __name__ == "__main__":
    articles = get_articles()
    print(f"📥 Artículos extraídos: {len(articles)}")
    asyncio.run(save_to_mongo(articles))
    print("🆗 Proceso completado.")
