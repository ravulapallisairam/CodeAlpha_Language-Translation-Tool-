# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 11:52:20 2025

@author: saira
"""

# -- coding: utf-8 --
"""
Created on Tue Jul 16 2025
@author: saira
"""

import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pygame
import pyperclip
import os
import time

# Initialize Translator
translator = Translator()

# Create main window
root = tk.Tk()
root.title("Language Translator with Voice")
root.geometry("600x400")
root.resizable(False, False)

# Languages list
languages = list(LANGUAGES.values())
language_keys = list(LANGUAGES.keys())

# ==== Functions ====

def translate_text():
    src_lang = language_keys[languages.index(from_combo.get())]
    dest_lang = language_keys[languages.index(to_combo.get())]
    input_text = input_box.get("1.0", tk.END).strip()

    if input_text:
        translated = translator.translate(input_text, src=src_lang, dest=dest_lang)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated.text)

def speak_translated_text():
    text = output_box.get("1.0", tk.END).strip()
    to_lang = language_keys[languages.index(to_combo.get())]

    if text:
        filename = f"spoken_{int(time.time())}.mp3"
        tts = gTTS(text=text, lang=to_lang)
        tts.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Wait for audio to finish
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.stop()
        pygame.mixer.quit()
        os.remove(filename)

def copy_to_clipboard():
    text = output_box.get("1.0", tk.END).strip()
    if text:
        pyperclip.copy(text)

# ==== GUI Widgets ====

# Input Label
input_label = tk.Label(root, text="Enter Text", font=("Arial", 12))
input_label.pack()

# Input Text Box
input_box = tk.Text(root, height=4, font=("Arial", 12))
input_box.pack(padx=10, pady=5)

# Language selection frame
frame = tk.Frame(root)
frame.pack(pady=5)

# From Language
from_label = tk.Label(frame, text="From:", font=("Arial", 10))
from_label.grid(row=0, column=0, padx=5)

from_combo = ttk.Combobox(frame, values=languages, width=20)
from_combo.grid(row=0, column=1)
from_combo.set("english")

# To Language
to_label = tk.Label(frame, text="To:", font=("Arial", 10))
to_label.grid(row=0, column=2, padx=5)

to_combo = ttk.Combobox(frame, values=languages, width=20)
to_combo.grid(row=0, column=3)
to_combo.set("telugu")

# Translate Button
translate_btn = tk.Button(root, text="Translate", command=translate_text, bg="green", fg="white", font=("Arial", 11))
translate_btn.pack(pady=10)

# Output Text Box
output_box = tk.Text(root, height=4, font=("Arial", 12))
output_box.pack(padx=10, pady=5)

# Speak and Copy buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

speak_btn = tk.Button(btn_frame, text="🔊 Speak", command=speak_translated_text, bg="lightblue", width=10)
speak_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(btn_frame, text="📋 Copy", command=copy_to_clipboard, bg="lightyellow", width=10)
copy_btn.grid(row=0, column=1, padx=10)

# Start the GUI loop
root.mainloop()