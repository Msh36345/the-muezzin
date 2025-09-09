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

from typing import Iterator

def memory_efficient_word_generator(text_file: str) -> Iterator[str]:
    word = ''
    with open(text_file) as text:
        while True:
            character = text.read(1)
            if not character:
                return
            if character.isspace():
                yield word.lower()
                word = ''
            else:
                word += character


def pair_generator(text_file):
    previous_word = ''
    for word in memory_efficient_word_generator(text_file):
        if previous_word and word:
            yield f'{previous_word}-{word}'
        previous_word = word or previous_word


for pair in pair_generator('filename.txt'):
    print(pair)

