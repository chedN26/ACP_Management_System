import tkinter as tk

# Function to change the color of the house when mouse hovers over it
def on_hover(event):
    # Get the mouse coordinates
    x, y = event.x, event.y
    
    # Check if the mouse is over a part of the house and change color accordingly
    if 100 <= x <= 400 and 150 <= y <= 350:  # Base of the house (rectangle)
        canvas.itemconfig(house_base, fill="goldenrod")
    else:
        canvas.itemconfig(house_base, fill="yellow")
    
    if 100 <= x <= 400 and 150 <= y <= 250:  # Roof area (triangle)
        canvas.itemconfig(roof, fill="darkorange")
    else:
        canvas.itemconfig(roof, fill="red")
    
    if 230 <= x <= 270 and 250 <= y <= 350:  # Door area (rectangle)
        canvas.itemconfig(door, fill="saddlebrown")
    else:
        canvas.itemconfig(door, fill="brown")
    
    if 150 <= x <= 200 and 180 <= y <= 230:  # Window area (rectangle)
        canvas.itemconfig(window, fill="skyblue")
    else:
        canvas.itemconfig(window, fill="lightblue")

    if 175 <= x <= 175 and 180 <= y <= 230:  # Vertical window line
        canvas.itemconfig(window_vertical, fill="black")
    else:
        canvas.itemconfig(window_vertical, fill="black")
        
    if 150 <= x <= 200 and 205 <= y <= 205:  # Horizontal window line
        canvas.itemconfig(window_horizontal, fill="black")
    else:
        canvas.itemconfig(window_horizontal, fill="black")

    if 300 <= x <= 330 and 80 <= y <= 140:  # Chimney area (rectangle)
        canvas.itemconfig(chimney, fill="darkred")
    else:
        canvas.itemconfig(chimney, fill="brown")

# Create the main window
root = tk.Tk()
root.title("Interactive House Drawing")

# Create a Canvas widget
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# Draw the base of the house (rectangle)
house_base = canvas.create_rectangle(100, 150, 400, 350, fill="yellow", outline="black")

# Draw the roof (triangle)
roof = canvas.create_polygon(100, 150, 250, 50, 400, 150, fill="red", outline="black")

# Draw the door (rectangle)
door = canvas.create_rectangle(230, 250, 270, 350, fill="brown", outline="black")

# Draw a window (rectangle)
window = canvas.create_rectangle(150, 180, 200, 230, fill="lightblue", outline="black")

# Draw the window panes (lines)
window_vertical = canvas.create_line(175, 180, 175, 230, fill="black", width=2)  # Vertical line
window_horizontal = canvas.create_line(150, 205, 200, 205, fill="black", width=2)  # Horizontal line

# Optional: Draw a chimney (rectangle)
chimney = canvas.create_rectangle(300, 80, 330, 140, fill="brown", outline="black")

# Bind the mouse motion event to the on_hover function
canvas.bind("<Motion>", on_hover)

# Run the Tkinter event loop
root.mainloop()
