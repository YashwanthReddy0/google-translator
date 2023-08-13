import tkinter as tk
from translate import Translator

def get_languages():
    languages = [
        "hi - Hindi",
        "bn - Bengali",
        "ta - Tamil",
        "te - Telugu",
        "mr - Marathi",
        "ur - Urdu",
        "gu - Gujarati",
        "kn - Kannada",
        "ml - Malayalam",
        "pa - Punjabi",
        "en - English",
        "fr - French",
        "es - Spanish",
        "de - German",
        "it - Italian",
        "ja - Japanese",
        "ko - Korean",
        "pt - Portuguese",
        "ru - Russian",
        "zh - Chinese",
    ]
    language_listbox.delete(0, tk.END)
    for lang in languages:
        language_listbox.insert(tk.END, lang)

def translate_text():
    lang_selection = language_listbox.get(tk.ACTIVE)
    target_lang = lang_selection.split(' - ')[0]
    translator = Translator(to_lang=target_lang)
    translated_text = translator.translate(text_entry.get())
    translated_label.config(text="Translated Text: " + translated_text)

# Create the GUI
app = tk.Tk()
app.title("Google Translator App") 
# Set the window size
app.geometry("500x400") 
# Set the background color
app.configure(bg="cyan")

text_entry = tk.Entry(app, width=50)
# Adjust the padding
text_entry.pack(pady=10)

translate_button = tk.Button(app, text="Translate", command=translate_text)
# Adjust the padding
translate_button.pack(pady=5)  
language_listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=10)
# Adjust the padding
language_listbox.pack(pady=10)

get_languages_button = tk.Button(app, text="Get Languages", command=get_languages)
# Adjust the padding
get_languages_button.pack(pady=5)

# Set the background color
translated_label = tk.Label(app, text="", bg="#808088")  
# Adjust the padding
translated_label.pack(pady=10)  

app.mainloop()
