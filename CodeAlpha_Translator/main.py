import tkinter as tk
import googletrans
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    text_to_translate = input_text.get("1.0", tk.END).strip()
    target_lang = lang_combobox.get()
    
    if not text_to_translate:
        messagebox.showwarning("Input Error", "Please enter some text to translate.")
        return

    # Map language name back to code
    target_code = [code for code, name in LANGUAGES.items() if name == target_lang][0]
    
    try:
        translator = Translator()
        translated = translator.translate(text_to_translate, dest=target_code)
        
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
        output_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

# UI Setup
root = tk.Tk()
root.title("CodeAlpha - AI Language Translator")
root.geometry("400x450")

tk.Label(root, text="Enter Text:").pack(pady=5)
input_text = tk.Text(root, height=8, width=45)
input_text.pack(pady=5)

tk.Label(root, text="Select Target Language:").pack(pady=5)
lang_list = [name.capitalize() for name in LANGUAGES.values()]
lang_combobox = ttk.Combobox(root, values=lang_list, state="readonly")
lang_combobox.set("english")
lang_combobox.pack(pady=5)

tk.Button(root, text="Translate", command=translate_text).pack(pady=15)

tk.Label(root, text="Translation:").pack(pady=5)
output_text = tk.Text(root, height=8, width=45, state=tk.DISABLED)
output_text.pack(pady=5)

root.mainloop()