import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri, server_api=ServerApi('1'))

db = client.pet

result_one = db.cats.insert_one(
    {
        "name": "Gaby",
        "age": 1,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)

print(result_one.inserted_id)

result_many = db.cats.insert_many(
    [
        {
            "name": "Leo",
            "age": 9,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 6,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)
print(result_many.inserted_ids)









