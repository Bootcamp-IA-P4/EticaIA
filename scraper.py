import requests
from bs4 import BeautifulSoup

# URL de MIT Tech Review
URL = "https://www.technologyreview.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_articles():
    response = requests.get(URL, headers=HEADERS)
    
    if response.status_code == 200;
        soup = BeautifulSoup(response.text, "html.parser")

        # Obtenemos los artículos
        articles = soup.find_all("h2")

        # Imprimimos los títulos
        return [article.text.strip() for article in articles]
    
    else:
        print(f"Error {response.status_code}: No se pudo acceder a la página.")
        return []

# Ejecutar la función y mostrar los resultados
if __name__ == "__main__":
    extracted_articles = get_articles()
    print("Artículos extraidos:")
    for title in extracted_articles:
        print("-", title)
    