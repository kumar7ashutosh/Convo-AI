from pymongo import MongoClient
from config.settings import Settings

settings=Settings()
client=MongoClient(settings.MONGO_DB_URL,tz_aware=True)
db=client(settings.MONGO_DB_NAME)

def get_collection(name:str):
    return db[name]