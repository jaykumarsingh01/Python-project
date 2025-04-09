# this is translator to one language to another


import asyncio
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Async translation function
async def change(text="type", src="english", dest="hindi"):
    translator = Translator()
    translated = await translator.translate(text, src=src.lower(), dest=dest.lower())
    return translated.text

# Run async translation inside Tkinter event
def data():
    src_lang = comb_sor.get()
    dest_lang = comb_dest.get()
    text_input = Sor_txt.get(1.0, END).strip()

    if text_input:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            translated_text = loop.run_until_complete(change(text=text_input, src=src_lang, dest=dest_lang))
            dest_txt.delete(1.0, END)
            dest_txt.insert(END, translated_text)
        finally:
            loop.close()

# GUI setup
root = Tk()
root.title("Translator")
root.geometry("500x700")
root.configure(bg='navy blue')

# Heading
Label(root, text="Translator", font=("times new roman", 40, "bold"), bg="white").place(x=100, y=20, height=60, width=300)

# Source label
Label(root, text="Source Text", font=("times new roman", 20, "bold"), fg="black", bg="navy blue").place(x=150, y=100, height=30, width=200)

# Source Textbox
Sor_txt = Text(root, font=("times new roman", 14), wrap=WORD)
Sor_txt.place(x=10, y=140, height=150, width=480)

# Language selection comboboxes
list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(root, value=list_text, font=("times new roman", 12))
comb_sor.place(x=10, y=310, height=40, width=150)
comb_sor.set("English")

Button(root, text="Translate", relief=RAISED, font=("times new roman", 12), command=data).place(x=170, y=310, height=40, width=150)

comb_dest = ttk.Combobox(root, value=list_text, font=("times new roman", 12))
comb_dest.place(x=330, y=310, height=40, width=150)
comb_dest.set("Hindi")

# Destination label
Label(root, text="Dest Text", font=("times new roman", 20, "bold"), fg="black", bg="navy blue").place(x=150, y=370, height=30, width=200)

# Destination Textbox
dest_txt = Text(root, font=("times new roman", 14), wrap=WORD)
dest_txt.place(x=10, y=410, height=150, width=480)

# Mainloop
root.mainloop()

                                          #Jay Kumar Singh 
