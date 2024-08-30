import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri, server_api=ServerApi('1'))

db = client.pet

def delete_cat_by_name(name):
    result = db.cats.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кіт з ім'ям '{name}' був успішно видалений.")
    else:
        print(f"Кота з ім'ям '{name}' не знайдено.")

def delete_all_cats():
    result = db.cats.delete_many({})
    print(f"Було видалено {result.deleted_count} записів.")

delete_cat_by_name("Leo")  
delete_all_cats()  

result_all = db.cats.find({})
for el in result_all:
    print(el)
