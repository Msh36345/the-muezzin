import time
from elasticsearch import  Elasticsearch
from services.tools.my_logger import logger
from services.tools.config import ES_HOST

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