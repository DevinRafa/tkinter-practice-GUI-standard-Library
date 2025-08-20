'''Belajar tkinter termasuk macam GUI pada python di STANDAR LIBRARY'''
# GUI -> Grapical User Interface
# GUI itu sebagai aplikasi yang ditampilkan seperti pada umumnya
# gunanya untuk mempermudah user, yang tidak memiliki skill program
# tidak seperti CLI(Command Line Interface) yang memiliki
# tampilan seperti terminal yang harus di ketik manual untuk bisa memakai fiturnya


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(background="white")
window.geometry("400x300")
window.resizable(False,False)
window.title("ih siapa ya?")

FRONT_NAME = tk.StringVar()
BACK_NAME = tk.StringVar()

def display_name():
    '''summon diplay the name front and backed'''
    display = f"Hallo {FRONT_NAME.get(),BACK_NAME.get()}, wellcome to my simple GUI"
    showinfo(title="Output",message=display)

## Frame (summon penempatan)
input_frame = ttk.Frame()

#3 Penempatan Grid, Pack, Place (settings penempatan)
input_frame.pack(padx=15,pady=15,fill="x",expand=True)

## Componen Essential (display)
# 1. label (Ask Front Name)
front_name_label = ttk.Label(input_frame, text="Front Name: ")
front_name_label.pack(padx=10,fill="x",expand=True)
# 2. entry/input data front name
front_name_entry = ttk.Entry(input_frame,textvariable=FRONT_NAME)
front_name_entry.pack(padx=10,pady=4,fill="x",expand=True)
# 3. label (Ask Back Name)
back_name_label = ttk.Label(input_frame, text="Back Name: ")
back_name_label.pack(padx=10,fill="x",expand=True)
# 4. entry/input data back name
back_name_entry = ttk.Entry(input_frame,textvariable=BACK_NAME)
back_name_entry.pack(padx=10,pady=4,fill="x",expand=True)
# 5. button "enter"
tombol_entry = ttk.Button(input_frame,command=display_name,text="Enter")
tombol_entry.pack(padx=10,pady=4,fill="x",expand=True)


window.mainloop()
