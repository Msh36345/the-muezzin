import os
from pymongo import MongoClient
import datetime
from time import sleep
from services.tools.my_logger import logger


MONGO_DB = os.environ.get("MONGO_DB", "mongodb://mongodb:27017/")

client = MongoClient(MONGO_DB)
db = client["news"]
collection = db["interesting"]


# This saves to MongoDB.
def insert_list_to_db(news_list):
    for news_item in news_list:
        timestamp = datetime.datetime.now().isoformat()
        collection.insert_one({"time_stemp": timestamp, "news_item": news_item})
        logger.info("news item insert to mongo DB")
        sleep(0.5)
    logger.info("upload interesting news to mongoDB complete")

# This gets all news from MongoDB.
def get_messages_from_mongo_db():
    msgs = list(collection.find({}, {"_id": 0}))
    for msg in msgs:
        if "time_stemp" in msg and not isinstance(msg["time_stemp"], str):
            msg["time_stemp"] = msg["time_stemp"].isoformat()
    return msgs