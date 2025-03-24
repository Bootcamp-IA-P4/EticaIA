from fastapi import APIRouter, HTTPException
from api.database import get_collection 
from api.models import Article
from bson import ObjectId
from api.utils.serializers import article_serializer

router = APIRouter()
collection = get_collection()

# Ruta para obtener todos los artículos
@router.get("/")
async def get_articles():
    articles = await collection.find().to_list(100)
    return [article_serializer(article) for article in articles]

# Ruta para crear o actualizar un artículo
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

# Ruta para obtener un artículo por su ID
@router.get("/{article_id}")
async def get_article(article_id: str):
    if not ObjectId.is_valid(article_id):
        raise HTTPException(status_code=400, detail="ID de artículo no válido")

    obj_id = ObjectId(article_id)
    article = await collection.find_one({"_id": obj_id})
    
    if not article:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    
    # Convertimos _id de ObjectId a str antes de devolver
    article["_id"] = str(article["_id"])
    return article