import os
from loguru import logger
from services.tools.elastic_search import es_instance as es
import sys

INDEX_LOGGER_NAME = os.environ.get("INDEX_LOGGER_NAME", "the_muezzin")

def init_logger(
    level: str = "INFO",
    show_date: bool = True,
    show_line: bool = True,
    colorize: bool = True,
    write_to_elastic_search: bool = True,
):
    """
    Returns a configured logger based on the given settings.
    Each parameter is True/False to enable or disable parts of the format.

    Log levels:
    1. DEBUG
    2. INFO
    3. WARNING
    4. ERROR
    5. CRITICAL
    """

    logger.remove()

    parts = []
    if show_date:
        parts.append("<green>{time:YYYY-MM-DD HH:mm:ss}</green>")
    if show_line:
        parts.append("<cyan>{name}</cyan>:<cyan>{line}</cyan>")
    parts.append("<level>{level: <8}</level>")
    parts.append("<level>{message}</level>")

    fmt = " | ".join(parts)

    logger.add(sys.stdout, level=level, format=fmt, colorize=colorize)

    if write_to_elastic_search:
        try:
            es.index(index=INDEX_LOGGER_NAME, document={
                "timestamp": datetime.utcnow().isoformat(),
                "level": record.levelname,
                "logger": record.name,
                "message": record.getMessage()

            })
        except Exception as e:
            print(f"ES log failed: {e}")

        )

    return logger


LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

logger = init_logger(level = LOG_LEVEL)