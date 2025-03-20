from fastapi import APIRouter
from api.database import collection
from api.models import Article

router = APIRouter()

# Definimos la ruta para obtener todos los artículos
@router.get("/")
async def get_articles():
    articles = []
    articles = await collection.find().to_list(100)
    return articles

# Definimos la ruta para crear un nuevo artículo
@router.post("/")
async def add_article(article: Article):
    existing_article = await collection.find_one({"title": article.title})
    if existing_article:
        await collection.update_one(
            {"title": article.title}, {"$set": article.model_dump()}
        )
        return {"message": "Artículo actualizado"}
    else:
        await collection.insert_one(article.model_dump())
        return {"message": "Artículo añadido"}
    