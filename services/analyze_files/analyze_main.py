import os
from pathlib import Path

from services.analyze_files.download_from_mongo_db import get_data_from_mongo_db,download_file
from services.analyze_files.transcription_file import get_file_transcription
from services.analyze_files.update_to_elastic_search import update_transcription_to_elastic_search
from services.tools.my_logger import logger

TEMP_FOLDER_PATH = os.getenv("TEMP_FOLDER_PATH", Path.home())


if __name__ == '__main__':
    data_list = get_data_from_mongo_db()
    for file in data_list:
        file_name = file['file_name']
        download_file(TEMP_FOLDER_PATH,file_name)
        file_transcription = get_file_transcription(f"{TEMP_FOLDER_PATH}/{file_name}")
        update_transcription_to_elastic_search(file_name,file['unique_id'],file_transcription)
        Path(f"{TEMP_FOLDER_PATH}/{file_name}").unlink()
        logger.debug(f"file {file_name} deleted.")

