from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv() 

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Validar si las variables están definidas correctamente
if not MONGO_URI or not DB_NAME:
    raise ValueError("Error: MONGO_URI y DB_NAME no están configuradas en .env")

# Configurar la conexión a MongoDB
client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
collection = database["articles"]