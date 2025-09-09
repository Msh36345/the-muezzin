import os
import base64
from services.tools.my_logger import logger


HOSTILE_LIST = os.getenv("HOSTILE_LIST", "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT")
LESS_HOSTILE_LIST = os.getenv("LESS_HOSTILE_LIST", "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==")

def identify_pair_words(raw_words_list):
    words_list = []
    pair_list = []
    for word in raw_words_list:
        if " " in word:
            pair_list.append(word.split())
        else:
            words_list.append(word)
    return set(words_list),pair_list

raw_hostile_words = base64.b64decode(HOSTILE_LIST).decode('utf-8').lower().split(',')
raw_less_hostile_words = base64.b64decode(LESS_HOSTILE_LIST).decode('utf-8').lower().split(',')

hostile_words,hostile_words_pairs = identify_pair_words(raw_hostile_words)
less_hostile_words,less_hostile_words_pairs = identify_pair_words(raw_less_hostile_words)

logger.debug(f"hostile_words : {hostile_words}")
logger.debug(f"less_hostile_words : {less_hostile_words}")
logger.debug(f"hostile_words_pairs : {hostile_words_pairs}")
logger.debug(f"less_hostile_words_pairs : {less_hostile_words_pairs}")