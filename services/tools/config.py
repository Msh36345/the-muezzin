import os

MONGO_CONN = os.environ.get("MONGO_CONN", "mongodb://localhost:27017/")
MONGO_DATA_BASE = os.environ.get("DATA_BASE", "the_muezzin")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION", "podcasts")

KAFKA_SERVERS = os.environ.get("KAFKA_SERVERS", 'kafka:9092')

ES_HOST = os.environ.get("ES_HOST", "http://elastic:9200")

INDEX_LOG_NAME = os.environ.get("INDEX_LOG_NAME", "the_muezzin_logs")
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
