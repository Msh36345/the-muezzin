import os
import time
from elasticsearch import  Elasticsearch

ES_HOST = os.environ.get("ES_HOST", "http://elasticsearch:9200/")

# This class talks to Elasticsearch
class ElasticDAL:
    # This starts the class and connects to Elasticsearch
    def __init__(self, host= ES_HOST):
        self.es = Elasticsearch(host)
        self._wait_until_ready()

    # This waits until Elasticsearch is ready
    def _wait_until_ready(self):
        while not self.es.ping():
            print("Waiting for Elasticsearch...")
            time.sleep(1)
        print("---Elasticsearch is up!---\n")

    def get_client(self):
        return self.es

es_instance = ElasticDAL().get_client()