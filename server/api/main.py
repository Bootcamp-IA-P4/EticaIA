from fastapi import FastAPI
from api.routes.articles import router as articles_router

app = FastAPI(title="EticaIA API")

# Incluir las rutas
app.include_router(articles_router, prefix="/articles")

@app.get("/")
def home():
    return {"message": "Bienvenido a la API de EticaIA"}
