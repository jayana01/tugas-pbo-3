from tkinter import *
from gtts import gTTS
import pygame

root = Tk()
root.title("Teks ke suara")
root.geometry("500x300")

def convert_to_speech():
    text_to_convert = text_entry.get()
    
    if text_to_convert:
        language = language_var.get()
        tts = gTTS(text=text_to_convert, lang=language)
        tts.save("output.mp3")
        
        pygame.mixer.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()

# GUI Elements
label = Label(root, text="masukan teks:")
label.pack(pady=10)

text_entry = Entry(root, width=40)
text_entry.pack(pady=10)

language_var = StringVar()
language_var.set("en")  # Default language is English

language_label = Label(root, text="pilih bahasa:")
language_label.pack()

language_menu = OptionMenu(root, language_var, "en", "id", "es")  # Adjust the language options as needed
language_menu.pack(pady=10)

convert_button = Button(root, text="Convert teks", command=convert_to_speech)
convert_button.pack(pady=10)

stop_button = Button(root, text="Stop", command=stop_audio)
stop_button.pack(pady=10)

root.mainloop()