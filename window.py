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

entry = tk.Entry(
    fg="yellow",
    bg="blue",
    width=50
)
entry.pack()


button = tk.Button(
    text="Try two",
    bg="#34A2FE",
    fg="white",
    width=25,
    height=5,
    )
button.pack()

entry.insert(0, "Real")
entry.delete(0, tk.END)

entry.insert(7, "Real")


name = entry.get()
print(name)

window.mainloop()