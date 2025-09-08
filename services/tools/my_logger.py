import os

ES_HOST = os.environ.get("ES_HOST", "http://localhost:9200/")
INDEX_LOGGER_NAME = os.environ.get("INDEX_LOGGER_NAME", "the_muezzin_logs")
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

# from loguru import logger
# import sys
# def init_logger(
#     level: str = "INFO",
#     show_date: bool = True,
#     show_line: bool = True,
#     colorize: bool = True,
#     write_to_elastic_search: bool = True,
# ):
#     """
#     Returns a configured logger based on the given settings.
#     Each parameter is True/False to enable or disable parts of the format.
#
#     Log levels:
#     1. DEBUG
#     2. INFO
#     3. WARNING
#     4. ERROR
#     5. CRITICAL
#     """
#
#     logger.remove()
#
#     parts = []
#     if show_date:
#         parts.append("<green>{time:YYYY-MM-DD HH:mm:ss}</green>")
#     if show_line:
#         parts.append("<cyan>{name}</cyan>:<cyan>{line}</cyan>")
#     parts.append("<level>{level: <8}</level>")
#     parts.append("<level>{message}</level>")
#
#     fmt = " | ".join(parts)
#
#     logger.add(sys.stdout, level=level, format=fmt, colorize=colorize)
#
#     if write_to_elastic_search:
#         pass
#
#     return logger
#
# logger = init_logger(level = LOG_LEVEL)

import logging
from elasticsearch import Elasticsearch
from datetime import datetime
class Logger:
    _logger = None
    @classmethod
    def get_logger(cls, name="my_logger", es_host=ES_HOST,
        index=INDEX_LOGGER_NAME, level=logging.DEBUG):
        if cls._logger:
            return cls._logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if not logger.handlers:
            es = Elasticsearch(es_host)
        class ESHandler(logging.Handler):
            def emit(self, record):
                try:
                    es.index(index=index, document={"timestamp": datetime.utcnow().isoformat(),
                                                    "level": record.levelname,
                                                    "logger": record.name,
                                                    "message": record.getMessage()})
                except Exception as e:
                    print(f"ES log failed: {e}")
        logger.addHandler(ESHandler())
        logger.addHandler(logging.StreamHandler())


        cls._logger = logger
        return logger

logger = Logger.get_logger()