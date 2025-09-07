from pathlib import Path
from datetime import datetime

podcasts_folder = Path.home() / "podcasts"
print(podcasts_folder)

files_meta_data_list = []
for file in podcasts_folder.iterdir():
    file_meta_data = {
        "file_name" : file.stem,
        "file_type" : file.suffix[1:],
        "file_size" : file.stat().st_size,
        "file_create_time" : datetime.fromtimestamp(file.stat().st_birthtime).strftime('%Y-%m-%d %H:%M')

    }
    files_meta_data_list.append(file_meta_data)
print(files_meta_data_list)

