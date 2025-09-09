from services.tools.my_logger import logger
import speech_recognition as sr


def get_file_transcription(file_path_to_get_file_transcription):
    r = sr.Recognizer()
    file_path = file_path_to_get_file_transcription
    logger.debug(f"Starting transcription to file : {file_path}")
    try:
        with sr.AudioFile(str(file_path)) as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
            logger.debug(f"transcription : {text}")
        return text
    except ValueError as e:
        logger.error(f"file transcription error : {e}")
        pass
    except Exception as e:
        logger.error(f"file transcription error : {e}")
    return text