from tkinter import * # import all components of tkinter
import customtkinter as ctk

# Set the themes and color options
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Variables for window size
window_x = 700
window_y = 450

# Variables for window center
center_x = window_x/2
center_y = window_y/2

# Variables for maximum move in X and Y axis
global hide_y # Use global if the variable is used inside a function
global hide_x
hide_y = center_y
hide_x = center_x

# Create a parent window
root = ctk.CTk() # Instatiate the window
root.title("GUI") # Set the window title
root.geometry(f'{window_x}x{window_y}') # Set the window size

# Create a frame (container) inside the window
frame = ctk.CTkFrame(root, border_color='blue', border_width=1)
frame.pack(pady=20)

# Functions to move textbox in  X and Y axis
def up():
    global hide_y
    if hide_y > 225:
        hide_y -= 6
        text_box.place(x=hide_x, y=hide_y, anchor='center')
        #up_button.configure(text=hide_y)
        root.after(16, up)

def down():
    global hide_y
    if hide_y < 585:
        hide_y += 6
        text_box.place(x=hide_x, y=hide_y, anchor='center')
        #down_button.configure(text=hide_y)
        root.after(16, down)
        
def left():
    global hide_x
    if hide_x > 206:
        hide_x -= 6
        text_box.place(x=hide_x, y=hide_y, anchor='center')
        #left_button.configure(text=hide_x)
        root.after(16, left)

def right():
    global hide_x
    if hide_x < 494:
        hide_x += 6
        text_box.place(x=hide_x, y=hide_y, anchor='center')
        #right_button.configure(text=hide_x)
        root.after(16, right)

# Buttons 
up_button = ctk.CTkButton(frame, text="Up", command=up)
up_button.grid(row=0, column=1, padx=10)

down_button = ctk.CTkButton(frame, text="Down", command=down)
down_button.grid(row=2, column=1, padx=10)

right_button = ctk.CTkButton(frame, text="Right", command=right)
right_button.grid(row=1, column=2, padx=10)

left_button = ctk.CTkButton(frame, text="Left", command=left)
left_button.grid(row=1, column=0, padx=10)

# Text box
text_box = ctk.CTkTextbox(root, width=400, height=200)
text_box.place(x=center_x , y=center_y , anchor='center')


root.mainloop()
