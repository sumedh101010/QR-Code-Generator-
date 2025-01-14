from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

root = Tk()

def generate():
    link_name = name_entry.get()  # Get the link name from the entry box
    link = link_entry.get()  # Get the link from the entry box
    file_name = link_name + ".png"  # Create the file name for the QR code image
    url = pyqrcode.create(link)  # Generate the QR code
    url.png(file_name, scale=8)  # Save the QR code as a PNG file with a scale of 8
    image = ImageTk.PhotoImage(Image.open(file_name))  # Open and convert the image for Tkinter
    image_label = Label(image=image)  # Create a label to display the image
    image_label.image = image  # Keep a reference to the image
    canvas.create_window(200, 450, window=image_label)  # Place the image label on the canvas

canvas = Canvas(root, width=400, height=600)  # Initialize the canvas
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg='blue', font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="Link name")
link_label = Label(root, text="Link")

canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)  # Entry box for the link name
link_entry = Entry(root)  # Entry box for the link

canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

button = Button(text="Generate QR code", command=generate)
canvas.create_window(200, 250, window=button)

root.mainloop()
