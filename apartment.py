import customtkinter as ctk
import tkinter as tk
from tkinter import *

def on_drag():
    # Get the position of the window relative to the screen
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    # Update the label with the new position
    position_label.config(text=f'X: {x}, Y: {y}')

# Set the window size
window_width = 1535
window_height = 785


# Create a parent window
root = ctk.CTk() # Instatiate the window
root.title("Apartment") # Set the window title
root.resizable(False, False)
x = (((root.winfo_screenwidth()+384)//2)-(window_width//2)) # +384
y = (((root.winfo_screenheight()+216)//2)-(window_height//2)) # +216
#root.geometry(f"{window_width}x{window_height}") # Set the window size
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, -9, 0))
#sy = root.winfo_screenwidth() #1536
#sx = root.winfo_screenheight() #864
#print(f"{sy}x{sx}")
#print(f"{y}x{x}")
#root.state('zoomed')
# Set the window to full screen
#root.attributes('-fullscreen', True)

frame = ctk.CTkFrame(root)
frame.pack()

label = ctk.CTkLabel(frame, text="Hello World!")
label.pack()

# Create a label to display the current position
position_label = tk.Label(root, text=f"X: {x}, Y: {y}", font=("Arial", 14))
position_label.pack(pady=20)

# Create a button to trigger position retrieval
position_button = ctk.CTkButton(frame, text="Get Position", command=on_drag)
position_button.pack(pady=20)

root.mainloop()