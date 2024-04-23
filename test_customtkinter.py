import customtkinter as ctk
from PIL import Image, ImageTk
from CTkTable import CTkTable


# From video "Modern Graphical User Interfaces in Python" by NeuralNine

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("500x500")

# stats_frame = ctk.CTkFrame(master=root, fg_color="transparent").pack(padx=(54, 0), pady=(18, 0), anchor="nw")
# stats_label = ctk.CTkLabel(master=stats_frame, text="This text").pack()
value = [[1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5],
         [1, 2, 3, 4, 5]]


def login():
    print("Test", progressbar_1.get())


def slider_callback(value):
    progressbar_1.set(value)


tabview = ctk.CTkTabview(master=root)
tabview.pack(padx=20, pady=20)

tabview.add("Tab 1")
tabview.add("Tab 2")
tabview.add("Tab 3")
tabview.add("Tab 4")

top = ctk.CTkToplevel(root)

table = CTkTable(master=tabview.tab("Tab 3"), row=5, column=5, values=value)
table.pack(expand=True, fill="both", padx=20, pady=20)

frame = ctk.CTkFrame(master=tabview.tab("Tab 1"))
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Login System", font=("Arial", 24))
label.pack(pady=12, padx=10)

progressbar_1 = ctk.CTkProgressBar(master=tabview.tab("Tab 2"))
progressbar_1.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

img = Image.open("WeenieLogo_blue.png")

button = ctk.CTkButton(
    master=frame, text="Login", command=login, fg_color="#2b2b2b", hover_color="#C850C0",
    border_color="#444444", border_width=2, corner_radius=32, image=ctk.CTkImage(dark_image=img, light_image=img))

button.pack(pady=12, padx=10)

slider_1 = ctk.CTkSlider(master=tabview.tab("Tab 2"), command=slider_callback, from_=0, to=1)
slider_1.pack(pady=12, padx=10)
slider_1.set(0.5)

checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()
