#pip install googletrans
#pip install textblob
#pip install pyttsx3
#pip install pywin32

import googletrans
import textblob
from tkinter import ttk, messagebox
import pyttsx3

def translate_it():
    #Delete any previous translations
    translated_text.delete(1.0, END)

    try:
        #Get Languages From Dictionary Keys
        #Get the From Language Key
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key

        #Get the To Language Key
        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key

        #Turn Original Text into a TextBlob
        words = textblob.TextBlob(original_text.get(1.0, END))

        #Translate Text
        words = words.translate(from_lang=from_language_key , to=to_language_key)

        #Output Translates text to screen
        translated_text.insert(1.0, words)

        # Initialie the speech engine
        engine = pyttsx3.init()

        #play with voices
        #voices = engine.getProperty("Voices")
        #for voice in voices:
            #engine.setProperty('voice', voice.id)
            #engine.say(words)


        #Pass text the speech engine
        engine.say(translated_text.get(1.0, END))

        #Run the Engine
        engine.runAndWait()


    except Exception as e:
        messagebox.showerror("Translator", e)

def clear():
    #clear the text boxes
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

langauge_list = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)

#Grab Language List from GoogleTrans
languages = googletrans.LANGUAGES

#Convert to list
langauge_list = list(languages.values())

#text boxes
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

#combo boxes
origninal_combo = ttk.Combobox(root, width=50, value=language_list)
origninal_combo.current(21)
origninal_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)

#clear
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()