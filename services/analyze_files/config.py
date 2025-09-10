import os
from pathlib import Path

INDEX_NAME = os.environ.get("INDEX_NAME", "the_muezzin")
TEMP_FOLDER_PATH = os.getenv("TEMP_FOLDER_PATH", Path.home())
HOSTILE_LIST = os.getenv("HOSTILE_LIST", "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
LESS_HOSTILE_LIST = os.getenv("LESS_HOSTILE_LIST", "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==")
THRESHOLD = os.getenv("THRESHOLD", 20)
THRESHOLD_PERCENT = os.getenv("THRESHOLD_PERCENT", 75)