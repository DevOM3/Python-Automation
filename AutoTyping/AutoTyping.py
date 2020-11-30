import speech_recognition as sr
import pyautogui as pag
import _thread
import time
import os

# Recognizing Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
    except:
        pass


def notepad():
    os.system('notepad')


# writing on the notepad
_thread.start_new_thread(notepad, ())
time.sleep(3)
pag.write(text, interval=0.11)
