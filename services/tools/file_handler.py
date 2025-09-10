from pathlib import Path
from services.tools.my_logger import logger

def delete_file(file_path,file_name):
    Path(file_path).unlink()
    logger.info(f"file {file_name} deleted.")