import re
from services.analyze_files.config import THRESHOLD,THRESHOLD_PERCENT
from services.analyze_files.analyze_hostile_words import hostile_words,less_hostile_words
from services.tools.my_logger import logger
from services.tools.stop_words import stop_words

# The main function that analyzes the threat level from the text
def detect_threat(raw_text):
    clean_text =  re.sub(r'[^\w\s]', '', raw_text).lower()
    count_hostile_words = count_words_from_text(clean_text, hostile_words)
    count_less_hostile_words = count_words_from_text(clean_text, less_hostile_words)
    count_clean_text = len([word for word in clean_text.split() if word not in stop_words])
    logger.debug(f"clean text : {count_clean_text}, hostile words : { count_hostile_words}, less hostile words : {count_less_hostile_words} .")
    bds_percent = ((count_hostile_words * 4)+(count_less_hostile_words) * 2)/count_clean_text * 100
    is_bds =  bds_percent>THRESHOLD
    bds_threat_level = threat_level_calculator(is_bds,count_hostile_words,count_less_hostile_words,bds_percent)
    logger.info(f"bds percent : {bds_percent:.2f}%, is bds : {is_bds}, bds threat level : {bds_threat_level} .")
    threat_data = {'text' : raw_text,
                   "bds_percent": bds_percent,
                   "is_bds": is_bds,
                   "bds_threat_level": bds_threat_level
                   }
    return threat_data

# Counts the number of times a word from the list appears in the text
def count_words_from_text(text_to_count, words_set):
    counts_words = 0
    for word in words_set:
        counts_words += text_to_count.count(word)
    return counts_words

# Classifies threat level based on word count and threat percentage
def threat_level_calculator(is_bds,hostile,less_hostile,bds_percent):
    if not is_bds :
        return "None"
    elif hostile >= less_hostile or THRESHOLD_PERCENT < bds_percent:
        return "High"
    else:
        return "Medium"

text = "This is a sample ? sentence !!!  showing , stopword removal."
detect_threat(text)
