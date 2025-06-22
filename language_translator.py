import sys
!{sys.executable} -m pip install googletrans==4.0.0-rc1


from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1100x400')
root.resizable(0, 0)
root['bg'] = 'skyblue'
root.title('Language translator by Prachi Chaturvedi')

# Title
Label(root, text="Language Translator", font="Arial 20 bold", bg='skyblue').pack(pady=10)

# Left Side Input
Label(root, text="Enter Text", font='Arial 13 bold', bg='white smoke').place(x=100, y=90)
Input_text = Text(root, font='Arial 10', height=5, width=50, wrap=WORD, padx=5, pady=5)
Input_text.place(x=100, y=130)

# Right Side Output
Label(root, text="Output", font='Arial 13 bold', bg='white smoke').place(x=780, y=90)
Output_text = Text(root, font='Arial 10', height=5, width=50, wrap=WORD, padx=5, pady=5)
Output_text.place(x=700, y=130)

# Language Dropdown - just below input box
language = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.place(x=220, y=250)  # x is center-ish under input box
dest_lang.set("choose language")

# Translate Button - center between the two boxes
def Translate():
    translator = Translator()
    text = Input_text.get("1.0", END)
    lang = dest_lang.get()
    for key, value in LANGUAGES.items():
        if value == lang:
            dest_lang_code = key
            break
    translated = translator.translate(text, dest=dest_lang_code)
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

Button(root, text="Translate", font='Arial 12 bold', bg='dark blue', fg='white', command=Translate).place(x=540, y=150)

root.mainloop()
