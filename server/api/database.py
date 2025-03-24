from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv() 

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
MONGO_DB_NAME_TEST = os.getenv("MONGO_DB_NAME_TEST")

# Validar si las variables están definidas correctamente
if not MONGO_URI or not DB_NAME or not MONGO_DB_NAME_TEST:
    raise ValueError("Error: MONGO_URI, DB_NAME o MONGO_DB_NAME_TEST no están configuradas en .env")

client = AsyncIOMotorClient(MONGO_URI)


# Configurar la conexión a MongoDB y utilizar la colección adecuada según el entorno
def get_collection(test=False):
    db_name = MONGO_DB_NAME_TEST if test else DB_NAME
    database = client[db_name]
    return database["articles"]