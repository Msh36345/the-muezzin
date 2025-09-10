import os

INDEX_NAME = os.environ.get("INDEX_NAME", "the_muezzin")
METADATA_TOPIC = os.getenv("METADATA_TOPIC","metadata")
RESET_INDEX = os.getenv("RESET_INDEX",True)

