import os
import time
from elasticsearch import  Elasticsearch
from services.tools.my_logger import logger


ES_HOST = os.environ.get("ES_HOST", "http://localhost:9200/")
INDEX_NAME = os.environ.get("INDEX_NAME", "the_muezzin")

# This class talks to Elasticsearch
class ElasticDAL:
    # This starts the class and connects to Elasticsearch
    def __init__(self, host= ES_HOST):
        self.es = Elasticsearch(host)
        self._wait_until_ready()

    # This waits until Elasticsearch is ready
    def _wait_until_ready(self):
        while not self.es.ping():
            logger.info("Waiting for Elasticsearch...")
            time.sleep(1)
        logger.info("---Elasticsearch is up!---\n")

    def get_client(self):
        return self.es

es_instance = ElasticDAL().get_client()