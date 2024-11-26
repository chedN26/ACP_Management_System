from tkinter import *
import customtkinter as ctk
from PIL import Image

# Set the themes and color options
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Variables for window size
window_x = 1080
window_y = 720

# Variables for window center
center_x = window_x/2
center_y = window_y/2

# Create a parent window
root = ctk.CTk() # Instatiate the window
root.title("Image") # Set the window title
root.geometry(f'{window_x}x{window_y}') # Set the window size

root.wm_attributes('-transparent', 'brown')
# Load the image using PIL
original_image = Image.open("night-bg.png")  # Replace with your image path

# Set the desired width for the image
new_width = window_x  # Example width you want to set

# Calculate the height based on the aspect ratio
width, height = original_image.size
new_height = int((new_width / width) * height)

# Resize the image while maintaining aspect ratio
resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)


# Create a frame (container) inside the window
frame = ctk.CTkFrame(root, border_color='yellow', border_width=1, width=window_x, height=window_y)
frame.pack(pady=20)

my_image = ctk.CTkImage(light_image=Image.open('night-bg.png'), dark_image=Image.open('night-bg.png'), size=(new_width, new_height))
my_image2 = ctk.CTkImage(light_image=Image.open('apartment.png'), dark_image=Image.open('apartment.png'), size=(500, 200))

my_label = ctk.CTkLabel(frame, text="", image=my_image)
my_label.pack(expand=True)
my_label.place(x=0 ,y=0)

my_label2 = ctk.CTkLabel(frame, text="", image=my_image2)
my_label2.pack(expand=True)
my_label2.place(x=center_x-250 ,y=center_y)

another_label = ctk.CTkLabel(frame, text="Hello World!")
another_label.place(x=center_x, y=5)

# Create a Canvas widget
canvas = ctk.CTkCanvas(frame, width=190, height=190)
#Add a text in Canvas
canvas.create_text(50, 50, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))
canvas.place(x=50 ,y=50)

second_frame = ctk.CTkFrame(frame, width=100, height=100, border_color="blue", border_width=1)
second_frame.place(x=center_x-50, y=center_y-50)

button_image = ctk.CTkImage(light_image=Image.open('night-bg.png'), dark_image=Image.open('night-bg.png'), size=(400, 100))
my_button = ctk.CTkButton(frame, text="", image=button_image, width=400, height=100, corner_radius=0)
my_button.place(x=250, y=450)

root.mainloop()