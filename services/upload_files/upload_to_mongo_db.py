from services.tools.my_logger import logger
from services.tools.mongo_db import mongo_connection,mongo_collection
from gridfs import GridFS

def put_files_to_mongo_db(list_white_files_metadata):
    inserted = 0
    fs = GridFS(mongo_connection, collection=mongo_collection)
    for file_metadata in list_white_files_metadata:
        with open(file_metadata['file_path'], 'rb') as file_data:
            file = file_data.read()
            fs.put(file, file_name=f"{file_metadata['file_name']}.{file_metadata['file_type']}",unique_id=file_metadata['unique_id'])
            logger.debug(f"file {file_metadata['file_name']} uploaded to MongoDB.")
            inserted+=1
    logger.info(f"---Inserted {inserted} files to MongoDB----\n")


