import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri, server_api=ServerApi('1'))
db = client.pet

def print_all_cats():
    try:
        result_all = db.cats.find({})
        if result_all.count() > 0:
            for el in result_all:
                print(el)
        else:
            print("У колекції немає жодного запису.")
    except Exception as e:
        print(f"Помилка при спробі вивести всі записи: {e}")

def find_cat_by_name(name):
    try:
        result_name = db.cats.find_one({"name": name})
        if result_name:
            print(result_name)
        else:
            print(f"Кота з ім'ям '{name}' не знайдено.")
    except Exception as e:
        print(f"Помилка при спробі знайти кота за ім'ям '{name}': {e}")

print_all_cats()

cat_name = input("Введіть ім'я кота: ")
find_cat_by_name(cat_name)
