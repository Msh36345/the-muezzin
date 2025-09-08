import os
from pymongo import MongoClient
import datetime
from time import sleep
from services.tools.my_logger import logger


MONGO_CONN = os.environ.get("MONGO_CONN", "mongodb://localhost:27017/")
MONGO_DATA_BASE = os.environ.get("DATA_BASE", "the_muezzin")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION", "podcasts")


def mongo_db_connection():
    try:
        client = MongoClient(MONGO_CONN)
        logger.info(f"Mongo connect to {client} successfully.")
        db = client[MONGO_DATA_BASE]
        logger.info(f"db : {MONGO_DATA_BASE}")

        return db
    except Exception as e:
        logger.exception(f"Mongo  connection error : {e}")

def get_collection():
    collection = MONGO_COLLECTION
    logger.info(f"collection : {MONGO_COLLECTION}\n")
    return collection


# This saves to MongoDB.
# def insert_list_to_db(news_list):
#     for news_item in news_list:
#         timestamp = datetime.datetime.now().isoformat()
#         collection.insert_one({"time_stemp": timestamp, "news_item": news_item})
#         logger.info("news item insert to mongo DB")
#         sleep(0.5)
#     logger.info("upload interesting news to mongoDB complete")

# This gets all news from MongoDB.
# def get_messages_from_mongo_db():
#     msgs = list(collection.find({}, {"_id": 0}))
#     for msg in msgs:
#         if "time_stemp" in msg and not isinstance(msg["time_stemp"], str):
#             msg["time_stemp"] = msg["time_stemp"].isoformat()
#     return msgs

mongo_connection = mongo_db_connection()
mongo_collection = get_collection()