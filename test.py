# import speech_recognition as sr
#
# r = sr.Recognizer()
#
# try:
#     from speech_recognition.recognizers import google, whisper
# except (ModuleNotFoundError, ImportError):
#     pass
# else:
#     r.recognize_google = google.recognize_legacy
#     r.recognize_whisper_api = whisper.recognize_whisper_api
# try:
#     with sr.AudioFile('/Users/mosheshulman/Downloads/Test instructions/שלב ג.PDF') as source:
#         audio = r.record(source)
#         text = r.recognize_google(audio)
#         print(f"text: {text}")
# except ValueError as e:
#     print("not good")
# except Exception as e:
#     print(f"error : {e}")
import os

a = ["a","b","c","d"]
if "a" in a:
    print("111")

