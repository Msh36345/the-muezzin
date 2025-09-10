from services.tools.config import INDEX_LOG_NAME,ES_HOST,LOG_LEVEL
from datetime import datetime
from elasticsearch import Elasticsearch
from loguru import logger as log
import sys

# My custom logger
# integrated with uploading logs to Elastic
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
        try:
            if not es.indices.exists(index=INDEX_LOG_NAME):
                es.indices.create(index=INDEX_LOG_NAME)
        except (ConnectionError) as e:
            if "resource_already_exists_exception" in str(e):
                pass
            else:
                raise

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