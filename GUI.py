import main
from tkinter import *
from tkinter import ttk


root = Tk()

root.title("Naruto Character Generator")
button = ttk.Button(root, text="Randomize", command=main.main)
button.grid(column=1, row=0)


root.mainloop()