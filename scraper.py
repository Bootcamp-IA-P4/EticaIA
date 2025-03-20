import requests
from bs4 import BeautifulSoup
from mongodb_connection import collection

URL = "https://www.technologyreview.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_articles():
    response = requests.get(URL, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"Error {response.status_code}: No se pudo acceder a la página.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for article_tag in soup.find_all("a", href=True):  # Buscamos enlaces de artículos
        title_tag = article_tag.find("h3")  # Extraer título
        
        # Verificamos si hay un título, si no lo hay, saltamos la iteración
        if not title_tag:
            continue

        # Extraer tema (topic) si existe
        topic_tag = article_tag.find_previous("span", class_="homepageEyebrow__text--e755f0749c2ee2902850fa01b4150520")  
        topic = topic_tag.text.strip() if topic_tag else "Unknown"  

        # Construimos la URL completa si es relativa
        link = article_tag["href"]
        if not link.startswith("http"):
            link = f"https://www.technologyreview.com{link}"

        # Estructura del artículo sin category
        article = {
            "title": title_tag.text.strip(),
            "link": link,
            "topic": topic  # Guardamos la temática del artículo
        }

        articles.append(article)

    return articles

def save_to_mongo(data):
    if data:
        for article in data:
            collection.update_one(
                {"title": article["title"]},  # Si el título ya existe, actualiza los datos
                {"$set": article},  
                upsert=True  # Si no existe, lo inserta
            )
        print(f"{len(data)} artículos guardados en MongoDB.")

if __name__ == "__main__":
    articles = get_articles()
    save_to_mongo(articles)

    print("Proceso completado.")