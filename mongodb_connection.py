from pymongo import MongoClient

# conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["eticalia_db"]
collection = db["cases"]
