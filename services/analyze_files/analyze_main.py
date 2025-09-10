from services.analyze_files.config import TEMP_FOLDER_PATH
from services.analyze_files.download_from_mongo_db import get_data_from_mongo_db,download_file_from_mongo_db
from services.analyze_files.transcription_file import get_file_transcription
from services.analyze_files.update_to_elastic_search import update_transcription_to_elastic_search
from services.analyze_files.threat_classification import detect_threat
from services.tools.my_logger import logger
from services.tools.file_handler import delete_file

# Receives a list from MongoDB and starts analyzing file by file
# During each analysis : downloads ,transcribes and deletes the file
# analyzes the threat level and uploads the updated metadata to Elastic
def run_analyzer():
    logger.info("---start analyze files---")
    data_list = get_data_from_mongo_db()
    for file_data in data_list:
        file_name = file_data['file_name']
        file_path = f"{TEMP_FOLDER_PATH}/{file_name}"
        download_file_from_mongo_db(TEMP_FOLDER_PATH,file_name)
        text = get_file_transcription(file_path)
        delete_file(file_path,file_name)
        if text != "":
            threat_data = detect_threat(text)
            file_data.update(threat_data)
            update_transcription_to_elastic_search(file_data)
    logger.info("---end analyze files---")



if __name__ == '__main__':
    run_analyzer()