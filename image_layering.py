import customtkinter as ctk
from PIL import Image, ImageTk

win = ctk.CTk()
win.geometry("550x450")
canvas = ctk.CTkCanvas(win, height=500, width=500)

half_tile = 50
tile_x = 0
tile_y = 0


def move_player():
    tile_x = tile_x + 25
    tile_y += 25
    canvas.coords(tile, )


def update_location(x_distance, y_distance):
    tile_x += x_distance
    tile_y += y_distance


# Create a rectangle on the right side of the canvas
offset = 25
rect = canvas.create_rectangle(offset, offset, 250, 500, width=2, fill="red")

# Load an image (replace 'sprite.png' with your image file)
SPRITE = Image.open("testing.png")
tilePIL = SPRITE.resize((100, 100))
tilePI = ImageTk.PhotoImage(tilePIL)
tile = canvas.create_image(half_tile * 2, half_tile * 2, image=tilePI, tags="a_tag")
update_location(offset, offset)

# Place the canvas
canvas.grid(row=1, column=0, rowspan=5)

# Move the tile to the right (it will go on top of the red rectangle)
canvas.coords(tile, (25 + 125 / 2, 125))

canvas = (ctk.CTkCanvas(master=win))
canvas.grid(row=6, column=0, rowspan=5)
button = ctk.CTkButton(label="Move", command=move_player)

win.mainloop()
