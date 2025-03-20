import requests
from bs4 import BeautifulSoup
from mongodb_connection import collection

URL = "https://www.technologyreview.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_articles():
    response = requests.get(URL, headers=HEADERS)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        articles = []
        for article_tag in soup.find_all("a", href=True):
            title_tag = article_tag.find("h3")
            topic_tag = article_tag.find_previous("span", class_="homepageEyebrow__text--e755f0749c2ee2902850fa01b4150520")  
            topic = topic_tag.text.strip() if topic_tag else "Unknown"

            link = article_tag["href"] if article_tag["href"].startswith("http") else f"https://www.technologyreview.com{article_tag['href']}"

            if title_tag and title_tag.text.strip():  # Verifica que haya título válido
                articles.append({
                    "title": title_tag.text.strip(),
                    "link": link,
                    "topic": topic  
                })
            else:
                print(f"⚠️ Artículo ignorado por no tener título: {link}")

        return articles
    else:
        print(f"Error {response.status_code}: No se pudo acceder a la página.")
        return []

def save_to_mongo(data):
    saved_count = 0
    for article in data:
        result = collection.update_one(
            {"title": article["title"]}, 
            {"$set": article},
            upsert=True
        )
        
        if result.upserted_id:  
            print(f"✅ Guardado: {article['title']}")
            saved_count += 1
        else:
            print(f"♻️ Actualizado: {article['title']}")

    print(f"Total de artículos guardados o actualizados: {saved_count}")

if __name__ == "__main__":
    articles = get_articles()
    print(f"📥 Artículos extraídos: {len(articles)}")
    save_to_mongo(articles)
    print("🚀 Proceso completado.")