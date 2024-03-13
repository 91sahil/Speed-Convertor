from tkinter import *
from tkinter.messagebox import *
import re

root = Tk()
root.title("Speed Converter By Sahil")
root.geometry("800x600+50+50")
f = ("Times New Roman", 30, "bold")

header_label = Label(root, text="Speed Converter", font=f)
header_label.pack(pady=20)


formula = {
    "kph to mach": 0.00081,
    "mach to kph": 1 / 0.00081
}

option = StringVar(root)
option.set("kph to mach")  # Default selection
conversion_type_menu = OptionMenu(root, option, *formula.keys())
conversion_type_menu.config(font=f)
conversion_type_menu.pack(pady=15)

lab_input = Label(root, text="Enter Value", font=f)
lab_input.pack(pady=5)

special_char_pattern = r'[!@#$%^&*()+=/\|"\'\',?]'

def convert():
    try:
        kph = ent_input.get()
        conversion_type = option.get()
        if kph == "":
            showerror("Issue", f"{conversion_type} kph cannot be empty")
            ent_input.delete(0, "end")
            ent_input.focus_set()
        elif re.search(special_char_pattern, kph):
            showerror("issue", f"{conversion_type} kph cannot be special character")
            ent_input.delete(0, "end")
            ent_input.focus_set()
        elif " " in kph:
            showerror("Issue", f"{conversion_type} Speed in km/hr cannot contain spaces")
            ent_input.delete(0, "end")
            ent_input.focus_set()
        elif float(kph) < 0:
            showerror("Issue", f"{conversion_type} Speed in km/hr should be positive")
            ent_input.delete(0, "end")
            ent_input.focus_set()
        elif not kph.replace(".", "").isdigit():
            showerror("Issue", f"{conversion_type} Speed in km/hr cannot be text")
            ent_input.delete(0, "end")
            ent_input.focus_set()
        else:
            kph_float = float(kph)
            mp = kph_float * formula[conversion_type]
            
            output_mp.configure(text=f"Conversion = {mp:.4f}")
    except ValueError as e:
        showerror("Issue", "Speed in km/hr should be a number")
        ent_input.delete(0, "end")
        ent_input.focus_set()

ent_input = Entry(root, font=f)
ent_input.pack(pady=5)

output_mp = Label(root, text="Conversion = ", font=f)
output_mp.pack(pady=20)

con_button = Button(root, text="Click To Convert", font=f, command=convert)
con_button.pack(pady=20)

def f1():
    if askokcancel("Quit", "Do you want to exit"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", f1)

root.mainloop()
