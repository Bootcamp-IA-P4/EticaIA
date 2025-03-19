import requests
from bs4 import BeautifulSoup
from mongodb_connection import collection

# URL de MIT Tech Review
URL = "https://www.technologyreview.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_articles():
    response = requests.get(URL, headers=HEADERS)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Obtenemos los artículos
        articles = soup.find_all("h3")

        # Extraemos el título de cada artículo
        extracted_data = [{"title": article.text.strip()} for article in articles]
        return extracted_data
    
    else:
        print(f"Error {response.status_code}: No se pudo acceder a la página.")
        return []

def save_to_mongo(data):
    if data:
        collection.insert_many(articles)
        print("Artículos guardados en MongoDB.")

# Ejecutar la función y mostrar los resultados
if __name__ == "__main__":
    articles = get_articles()
    save_to_mongo(articles)
    