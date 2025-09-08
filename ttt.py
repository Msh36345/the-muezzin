import logging
from elasticsearch import Elasticsearch
from datetime import datetime
class Logger:
    _logger = None
    @classmethod
    def get_logger(cls, name="your_logger_name", es_host="your_es_host_name",
        index="your_index_logs_name", level=logging.DEBUG):
        if cls._logger:
            return cls._logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            es = Elasticsearch(es_host)

        logger.addHandler(ESHandler())
        logger.addHandler(logging.StreamHandler())


        cls._logger = logger
        return logger