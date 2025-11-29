from tkinter import *
from tkinter import ttk
import generator
import random
from tkinter import scrolledtext as st
import sys
import webbrowser


def run_randomizer():
    starting_village = choice.get()
    if starting_village == "Random": #Select a random village
        villages = ["Cloud", "Grass", "Rain", "Sand", "Leaf"]
        starting_village = starting_village.replace("Random", (random.choice(villages)))
        generator.main(starting_village)
    elif starting_village != "Random": #Select the chosen village
        starting_village = choice.get()
        if starting_village:
            generator.main(starting_village)
        else:
            print("Please select a village to be born into")

root = Tk()

root.title("Naruto Character Generator")
label = ttk.Label(root, text='Select a Village', font=("Arial", 16, "bold"))
label.grid(column=2, row=0)

choice = StringVar(value="")

C_Option = Radiobutton(root, text="Cloud", variable=choice, value="Cloud", font=("Arial", 12, "bold"))
G_Option = Radiobutton(root, text="Grass", variable=choice, value="Grass", font=("Arial", 12, "bold"))
R_Option = Radiobutton(root, text="Rain", variable=choice, value="Rain", font=("Arial", 12, "bold"))
S_Option = Radiobutton(root, text="Sand", variable=choice, value="Sand", font=("Arial", 12, "bold"))
L_Option = Radiobutton(root, text="Leaf", variable=choice, value="Leaf", font=("Arial", 12, "bold"))
Random_Option = Radiobutton(root, text="Random", variable=choice, value="Random", font=("Arial", 12, "bold"))

C_Option.grid(column=0, row=2)
G_Option.grid(column=1, row=2)
R_Option.grid(column=2, row=2)
S_Option.grid(column=3, row=2)
L_Option.grid(column=4, row=2)
Random_Option.grid(column=5, row=2)


class RedirectText:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert(END, text)
        self.widget.see(END)

    def flush(self):
        pass

console_box = st.ScrolledText(root, width=100, height=10, font=("Arial", 12))
console_box.grid(column=0, row=1, columnspan=6, pady=10)

sys.stdout = RedirectText(console_box)

def insert_link(display_text, url):
    # Insert the text
    start_index = console_box.index("insert")
    console_box.insert("insert", display_text)

    # Make a unique tag for this link text
    tag_name = "link_" + start_index.replace(".", "_")

    console_box.tag_add(tag_name, start_index, f"{start_index} + {len(display_text)}c")

    # Styling (blue + underline)
    console_box.tag_config(
        tag_name,
        foreground="blue",
        underline=True
    )

    # Click action
    def open_link(event, link=url):
        webbrowser.open(link)

    console_box.tag_bind(tag_name, "<Button-1>", open_link)


button = ttk.Button(root, text="Randomize!", command = lambda: (console_box.delete(1.0, END), run_randomizer()))
button.grid(column=2, row=100)

root.mainloop()