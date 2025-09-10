from services.analyze_files.config import HOSTILE_LIST,LESS_HOSTILE_LIST
import base64
from services.tools.my_logger import logger

# Decodes the list of words from Base64 encoding
hostile_words = base64.b64decode(HOSTILE_LIST).decode('utf-8').lower().split(',')
less_hostile_words = base64.b64decode(LESS_HOSTILE_LIST).decode('utf-8').lower().split(',')

logger.debug(f"hostile_words : {hostile_words}")
logger.debug(f"less_hostile_words : {less_hostile_words}")
logger.info("word decoding completed successfully.")