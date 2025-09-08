import os
from loguru import logger
import sys

def init_logger(
    level: str = "INFO",
    show_date: bool = True,
    show_line: bool = True,
    colorize: bool = True,
    write_to_file: bool = False,
    log_file_path: str = "app.log"
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

    if write_to_file:
        logger.add(
            log_file_path,
            level=level,
            format=fmt,
            colorize=False,
            rotation="10 MB",
            retention="14 days",
            compression="zip",
            enqueue=True,
        )

    return logger

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

logger = init_logger(level = LOG_LEVEL)