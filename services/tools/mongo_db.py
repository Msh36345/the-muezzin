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

mongo_connection = mongo_db_connection()
mongo_collection = get_collection()