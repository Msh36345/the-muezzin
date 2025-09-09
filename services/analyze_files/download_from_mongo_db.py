from gridfs import GridFS
from services.tools.my_logger import logger
from services.tools.mongo_db import mongo_connection,mongo_collection

collection_files = f"{mongo_collection}.files"

# This gets data files from MongoDB.
def get_data_from_mongo_db():
    data = list(mongo_connection[collection_files].find({}, {"_id": 1, 'unique_id': 1, 'file_name': 1}))
    logger.info(f"data len from mongo DB : {len(data)}")
    for file_data in data:
       logger.debug(f"file data : {file_data}")
    return data

def download_file(folder_path,file_name):
    fs = GridFS(mongo_connection, collection=mongo_collection)
    data = mongo_connection[collection_files].find_one({"file_name": file_name})
    out_data = fs.get(data['_id']).read()
    with open(f"{folder_path}/{file_name}", 'wb') as output:
        output.write(out_data)
    logger.info(f"download completed for file : {file_name}.")


if __name__ == '__main__':
    data_list = get_data_from_mongo_db()
    download_file('download (9).wav')

