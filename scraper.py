import requests
from bs4 import BeautifulSoup
from mongodb_connection import collection

# URL de MIT Tech Review
URL = "https://www.technologyreview.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Obtener los artículos de la página
def get_articles():
    response = requests.get(URL, headers=HEADERS)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Buscamos el contenedor de los artículos
        sections = soup.find_all("section")

        articles = []
        for section in sections:
            for h3 in section.find_all("h3"):
                title = h3.text.strip()

                # filtrar títulos vacíos

                if len(title) > 0:
                    articles.append({"title": title})

        return articles
    
    else:
        print(f"Error {response.status_code}: No se pudo acceder a la página {URL}")
        
        return []


# Guardar los datos en MongoDB
def save_to_mongo(data):
    if data:
        for article in data:
            collection.update_one(
                {"title": article["title"]},
                {"$set": article},
                upsert=True
            )
        print(f"{len(data)} artículos guardados en MongoDB.")


# Ejecutar la función y mostrar los resultados
if __name__ == "__main__":
    articles = get_articles()
    save_to_mongo(articles)
    