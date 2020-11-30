import speech_recognition as sr
import pyautogui
import _thread
from tkinter import *
from tkinter.messagebox import showinfo


def recognize():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("listening")
            audio = r.listen(source)
            try:
                print("recognizing")
                text = r.recognize_google(audio)
            except:
                text = "error"

            print(text)
            if text.length > 15:
                if "type first name" in text:
                    first_name.focus_set()
                    pyautogui.write(text.split("name ")[1])
                elif "type last name" in text:
                    last_name.focus_set()
                    pyautogui.write(text.split("name ")[1])
            elif text == "click submit":
                call_submit(first_name.get(), last_name.get())
            elif text == "click reset":
                call_reset()
            else:
                pass


def call_submit(f_n, l_n):
    showinfo("Auto Form Fill", "Hello, " + f_n + " " + l_n)


def call_reset():
    first_name.delete(0, END)
    last_name.delete(0, END)


root = Tk()

f_name = StringVar
l_name = StringVar

first_name = Entry(textvariable=f_name, width=31)
first_name.pack(side=TOP, padx=21, pady=11)

last_name = Entry(textvariable=l_name, width=31)
last_name.pack(side=TOP, padx=21, pady=11)

reset = Button(text="Reset", command=call_reset)
reset.pack(side=LEFT, padx=21, pady=11)

submit = Button(text="Submit", command=call_submit)
submit.pack(side=RIGHT, padx=21, pady=11)

_thread.start_new_thread(recognize, ())

root.mainloop()
