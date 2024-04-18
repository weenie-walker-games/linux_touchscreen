import customtkinter as ctk

# From video "Modern Graphical User Interfaces in Python" by NeuralNine

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x350")


def login():
    print("Test")


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Login System")
label.pack()

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack()

entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack()

button = ctk.CTkButton(master=frame, text="Login", command=login)
button.pack()

checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack()

root.mainloop()
