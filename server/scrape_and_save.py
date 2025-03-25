from scraper import scrape_articles
from dotenv import load_dotenv
import os

load_dotenv()

def run():
    print("🔄 Ejecutando scraper desde tarea programada...")
    scrape_articles()
    print("✅ Scrapeo completado.")

if __name__ == "__main__":
    run()
