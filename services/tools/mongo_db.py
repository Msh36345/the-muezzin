from pymongo import MongoClient
from services.tools.config import MONGO_CONN,MONGO_DATA_BASE,MONGO_COLLECTION
from services.tools.my_logger import logger

# Mongo DB connection
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