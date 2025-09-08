from pathlib import Path
from datetime import datetime
from services.tools.my_logger import logger


# Returns a list of all files in a folder.
# Gets the folder path from the home path location.
def get_list_of_files_path_from_folder(folder_path_from_home):
    podcasts_folder = Path.home() / folder_path_from_home
    list_of_files_path = []
    if podcasts_folder.exists():
        logger.info(f"Folder path is : {podcasts_folder}.")
        for file_path in podcasts_folder.iterdir():
            list_of_files_path.append(file_path)
        logger.info(f"Total files in folder : {len(list_of_files_path)}.")
        return list_of_files_path
    else:
        logger.info("Folder path does not exist.")
        return list_of_files_path

# Returns a list of json's with all the metadata of all the files
def create_list_with_all_files_metadata(list_of_files):
    list_of_files_metadata = []
    for file in list_of_files:
        list_of_files_metadata.append(get_json_with_file_metadata(file))
    return list_of_files_metadata

# Accepts a file path and returns a Gson with metadata
def get_json_with_file_metadata(file_path):
    file_metadata = {
        "file_path": str(file_path),
        "file_name": file_path.stem,
        "file_type": file_path.suffix[1:],
        "file_size": file_path.stat().st_size,
        "file_create_time": datetime.fromtimestamp(file_path.stat().st_birthtime).strftime('%Y-%m-%d %H:%M'),
        "unique_id" : file_path.stat().st_ino
    }
    logger.debug(file_metadata)
    return file_metadata


def get_list_with_all_files_metadata(folder_path):
    list_of_files = get_list_of_files_path_from_folder(folder_path)
    all_files_metadata = create_list_with_all_files_metadata(list_of_files)
    return all_files_metadata

