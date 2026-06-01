from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.MONGO_URI)

db = client[settings.MONGO_DB_NAME]

users_collection = db["users"]
vehicles_collection = db["vehicles"]
reviews_collection = db["reviews"]