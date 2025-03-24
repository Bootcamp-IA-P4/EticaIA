from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.articles import router as articles_router

app = FastAPI(title="EticaIA API")

# Configuración CORS para permitir al frontend acceder
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permitir el frontend
    allow_credentials=True,
    allow_methods=["*"],                     # Permitir todos los métodos (GET, POST...)
    allow_headers=["*"],                     # Permitir todos los headers
)


# Incluir las rutas
app.include_router(articles_router, prefix="/articles")

@app.get("/")
def home():
    return {"message": "Bienvenido a la API de EticaIA"}
