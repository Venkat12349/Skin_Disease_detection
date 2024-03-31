import tkinter as tk
from tkinter import ttk
from googletrans import Translator


def translate_text():
    text_to_translate = input_text.get("1.0", "end-1c")
    target_language = target_language_var.get()

    translator = Translator()
    translated_text = translator.translate(text_to_translate, dest=target_language)

    output_text.delete("1.0", "end")
    output_text.insert("1.0", translated_text.text)


# Create main application window
root = tk.Tk()
root.title("Language Translator")
root.geometry("400x300")

# Create input text area
input_label = ttk.Label(root, text="Enter Text:")
input_label.pack()
input_text = tk.Text(root, height=5, width=40)
input_text.pack()

# Create target language selection
target_language_var = tk.StringVar()
target_language_label = ttk.Label(root, text="Select Target Language:")
target_language_label.pack()
target_language_combobox = ttk.Combobox(root, textvariable=target_language_var,
                                        values=["fr", "es", "de","te","hi","ta","ml","en","kn","ar"])  # Add more language codes as needed
target_language_combobox.pack()

# Create translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Create output text area
output_label = ttk.Label(root, text="Translated Text:")
output_label.pack()
output_text = tk.Text(root, height=5, width=40)
output_text.pack()

# Run the application
root.mainloop()