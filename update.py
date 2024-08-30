import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri, server_api=ServerApi('1'))

db = client.pet

def update_cat_age(name, new_age):
    result = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count > 0:
        print(f"Вік кота '{name}' було успішно оновлено до {new_age} років.")
    else:
        print(f"Кота з ім'ям '{name}' не знайдено.")

def add_feature_to_cat(name, new_feature):
    result = db.cats.update_one({"name": name}, {"$addToSet": {"features": new_feature}})
    if result.matched_count > 0:
        print(f"Характеристика '{new_feature}' була додана до кота '{name}'.")
    else:
        print(f"Кота з ім'ям '{name}' не знайдено.")

update_cat_age("Leo", 10) 
add_feature_to_cat("Leo", "любитиме рибу")  

result_all = db.cats.find({})
for el in result_all:
    print(el)

result_name = db.cats.find_one({"name": "Leo"})
print(result_name)
