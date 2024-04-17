import tkinter as tk
import tkinter.ttk as ttk

# Taken from RealPython website, https://realpython.com/python-gui-tkinter/

window = tk.Tk()
label = tk.Label(
    text="Python Rocks!",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    )
label.pack()

label2 = tk.Label(
    text="Try two",
    bg="#34A2FE",
    fg="white",
    width=10,
    height=10,
    )
label2.pack()

window.mainloop()