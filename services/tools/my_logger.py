import os
from datetime import datetime
from elasticsearch import Elasticsearch
from loguru import logger as log
import sys

ES_HOST = os.environ.get("ES_HOST", "http://localhost:9200/")
INDEX_LOG_NAME = os.environ.get("INDEX_LOG_NAME", "the_muezzin_logs")
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
RESET_INDEX = os.getenv("RESET_INDEX",True)

def init_logger(
    level: str = "INFO",
    show_date: bool = True,
    show_line: bool = True,
    colorize: bool = True,
    write_to_elastic_search: bool = True,
):
    """
    Returns a configured log based on the given settings.
    Each parameter is True/False to enable or disable parts of the format.

    Log levels:
    1. DEBUG
    2. INFO
    3. WARNING
    4. ERROR
    5. CRITICAL
    """

    log.remove()

    parts = []
    if show_date:
        parts.append("<green>{time:YYYY-MM-DD HH:mm:ss}</green>")
    if show_line:
        parts.append("<cyan>{name}</cyan>:<cyan>{line}</cyan>")
    parts.append("<level>{level: <8}</level>")
    parts.append("<level>{message}</level>")

    fmt = " | ".join(parts)

    log.add(sys.stdout, level=level, format=fmt, colorize=colorize)

    if write_to_elastic_search:
        es = Elasticsearch(ES_HOST)
        if RESET_INDEX:
            if es.indices.exists(index=INDEX_LOG_NAME):
                es.indices.delete(index=INDEX_LOG_NAME)
            es.indices.create(index=INDEX_LOG_NAME)
        def elastic_sink(log_data):
                record = log_data.record
                log_json = {
                    "timestamp": datetime.now().isoformat(),
                    "level": record['level'].name,
                    "log": f"{record['file'].name} : {record["line"]}",
                    "message":  record['message']
                }
                es.index(index=INDEX_LOG_NAME, document=log_json)
                es.indices.refresh(index=INDEX_LOG_NAME)

        log.add(elastic_sink, level=level)

    return log

logger = init_logger(level = LOG_LEVEL)

# import logging
# from elasticsearch import Elasticsearch
# from datetime import datetime
# class Logger:
#     _logger = None
#     @classmethod
#     def get_logger(cls, name="my_logger", es_host=ES_HOST,
#         index=INDEX_LOG_NAME, level=logging.DEBUG):
#         if cls._logger:
#             return cls._logger
#         logger = logging.getLogger(name)
#         logger.setLevel(level)
#         if not logger.handlers:
#             es = Elasticsearch(es_host)
#         class ESHandler(logging.Handler):
#             def emit(self, record):
#                 try:
#                     es.index(index=index, document={"timestamp": datetime.utcnow().isoformat(),
#                                                     "level": record.levelname,
#                                                     "logger": record.name,
#                                                     "message": record.getMessage()})
#                 except Exception as e:
#                     print(f"ES log failed: {e}")
#         logger.addHandler(ESHandler())
#         logger.addHandler(logging.StreamHandler())
#
#
#         cls._logger = logger
#         return logger
#
# logger = Logger.get_logger()

