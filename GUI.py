import main
from tkinter import *
from tkinter import ttk


root = Tk()

root.title("Naruto Character Generator")
label = ttk.Label(root, text='Please enter in the village you want to be from')
label.grid(column=0, row=0)

choice = StringVar(value="")

C_Option = Radiobutton(root, text="Cloud Village", variable=choice, value="Cloud")
G_Option = Radiobutton(root, text="Grass Village", variable=choice, value="Grass")
R_Option = Radiobutton(root, text="Rain Village", variable=choice, value="Rain")
S_Option = Radiobutton(root, text="Sand Village", variable=choice, value="Sand")

C_Option.grid(column=2, row=0)
G_Option.grid(column=2, row=1)
R_Option.grid(column=2, row=2)
S_Option.grid(column=2, row=3)

def run_randomizer():
    starting_village = choice.get()
    if starting_village:
        main.main(starting_village)
    else:
        print("Please select a village to be born into")


button = ttk.Button(root, text="Randomize", command=run_randomizer)
button.grid(column=1, row=4)


root.mainloop()