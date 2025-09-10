from gridfs import GridFS
from services.tools.my_logger import logger
from services.tools.mongo_db import mongo_connection,mongo_collection

collection_files = f"{mongo_collection}.files"

# Uploading files to MongoDB
def put_files_to_mongo_db(list_white_files_metadata):
    inserted = 0
    fs = GridFS(mongo_connection, collection=mongo_collection)
    unique_id_set = create_unique_id_set()
    for file_metadata in list_white_files_metadata:
        if not file_metadata['unique_id'] in unique_id_set:
            with open(file_metadata['file_path'], 'rb') as file_data:
                file = file_data.read()
                fs.put(file, file_name=f"{file_metadata['file_name']}.{file_metadata['file_type']}",unique_id=file_metadata['unique_id'])
                logger.debug(f"file {file_metadata['file_name']} uploaded to MongoDB.")
                inserted+=1
        else:
            logger.debug(f"file {file_metadata['file_name']} already in MongoDB.")
    logger.info(f"---Inserted {inserted} files to MongoDB----\n")

# Creates a set of all unique id found in Mongo
# so it doesn't upload the same file twice
def create_unique_id_set():
    unique_id_data = list(mongo_connection[collection_files].find({}, {'unique_id': 1}))
    unique_id_list = []
    for unique_id in unique_id_data:
        unique_id_list.append(unique_id['unique_id'])
    return set(unique_id_list)