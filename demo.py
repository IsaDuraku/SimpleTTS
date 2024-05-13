from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()

def text_to_speech():
    text = entry.get()
    language = language_var.get()  # Get the selected language from the dropdown menu
    output = gTTS(text=text, lang=language, slow=False)
    output.save('output.mp3')
    os.system("start output.mp3")

entry = Entry(root, width=50)
canvas.create_window(200, 180, window=entry)

language_var = StringVar(root)
language_var.set("en")  # Set the default language to English
languages = ["en", "de", "tr"]  # List of languages: English, German, Turkish
language_menu = OptionMenu(root, language_var, *languages)
canvas.create_window(200, 130, window=language_menu)

button = Button(text="Start", command=text_to_speech)
canvas.create_window(200, 230, window=button)

root.mainloop()