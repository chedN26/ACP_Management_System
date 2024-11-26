import customtkinter as ctk
import tkinter as tk
from tkinter import *
from PIL import Image
import mysql.connector # Package for using XAMPP MySql; use the command "python3 -m pip install mysql-connector"
from mysql.connector import Error # Handles execution error with the database
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt # Package for using GUI charts 

# Color palette of the charts
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#ADD8E6", "#87CEEB", "#4169E1", "#1E90FF", "#000080"])

# Function to establish a new connection
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='acp_management_db'
    )
    
def retrieve_data():
    # Query to select all data from the table
    query = "SELECT * FROM bill_tbl"
    
    # Create connection to the database
    conn = create_connection()
    
    try:
        # If the connection is successful
        if conn.is_connected():
            print("Connected to the database.")
        
        cursor = conn.cursor()  # Create cursor object
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch all rows from the result
        rows = cursor.fetchall()
        
        # Check if there are any rows
        if rows:
            # Print the rows (you can also display them in a Tkinter widget)
            for row in rows:
                print(row)  # Each row is a tuple
            return rows
        else:
            print("No data found in the table.")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and connection after the operation
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed.")
#END SQL ###############

# Set the themes and color options
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Set the window size
window_width = 1536
window_height = 786

# Variable to identify the screen center
center_width = window_width/2
center_height = window_height/2

# Create a parent window
root = ctk.CTk() # Instatiate the window
root.title("DueDeet") # Set the window title
#root.iconbitmap('dd.ico')
root.resizable(False, False) # Disable resizable window
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, -9, -1)) # Set the window size and position


# Load the image using PIL
original_image = Image.open('sunset-ps.png')  # Replace with your image path

# Set the desired width for the image
new_width = window_width  # Example width you want to set

# Calculate the height based on the aspect ratio
width, height = original_image.size
new_height = int((new_width / width) * height)

# Create a frame container
frame = ctk.CTkFrame(root, width=window_width, height=new_height)
frame.place(x=0, y=0)

# Open the background image
my_image = ctk.CTkImage(light_image=original_image, dark_image=original_image, size=(new_width, new_height))

# Image container
image_label = ctk.CTkLabel(frame, text="", image=my_image)
image_label.place(x=0 , y=0)

# Login frame
login_height = 360
login_width = login_height * 1.618
login_frame = ctk.CTkFrame(frame, width=login_width, height=login_height, fg_color="#3b358b")
login_frame.place(x=center_width-(login_width/2), y=center_height-(login_height/2))

login_welcomelbl = ctk.CTkLabel(login_frame, text="Welcome!")
login_welcomelbl.grid(row=0 ,column=0)

user_entry = ctk.CTkEntry(login_frame, placeholder_text="Enter your username.")
user_entry.grid(row=1 ,column=0)

password_entry = ctk.CTkEntry(login_frame, placeholder_text="Enter your password.")
password_entry.grid(row=2 ,column=0)

wrong_warning = ctk.CTkLabel(login_frame, text="")

# visual_frame_test = ctk.CTkFrame(login_frame, width=50, height=50)
# visual_frame_test.grid(row=0, column=1)

# visual_label = ctk.CTkLabel(visual_frame_test, text="Hello World!")
# visual_label.pack()

def login():
    username = user_entry.get()
    password = password_entry.get()
    
    if (username=="c" and password=="c"):
        user_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        # visual_frame_test.grid(row=0, column=1)
        # visual_label.configure(text="I'm back!")
        down(apartment_down)
        login_welcomelbl.focus_set()
        if (wrong_warning.winfo_exists()):
            wrong_warning.grid_remove()
        else:
            print("Warning doesn't exist.")
        #print("correct")
    else:
        wrong_warning.grid(row=4, column=0)
        wrong_warning.configure(text="Incorrect username or password!")
        #print("wrong")

login_button = ctk.CTkButton(login_frame, text="Login", command=login)
login_button.grid(row=3 ,column=0)

# Test Frame
global x_test
global y_test
x_test = 265
y_test = 2095
# test_frame = ctk.CTkFrame(frame, width=250, height=170)
# test_frame.place(x=x_test, y=y_test)

#TEST ##############
overview_width = (window_width-200-(5*3))//3
overview_height = 340

apartment_details_frame = ctk.CTkFrame(frame, width=window_width-200, height=350, fg_color='white')
details_overview = ctk.CTkFrame(apartment_details_frame, width=overview_width ,height=overview_height, fg_color="#1737a7")
water_overview = ctk.CTkFrame(apartment_details_frame, width=overview_width ,height=overview_height, fg_color="#244dbb")
electricity_overview = ctk.CTkFrame(apartment_details_frame, width=overview_width ,height=overview_height, fg_color="#5d56c1")

# Acessing the query result
result = retrieve_data()
first_row = result[0]
#print(f"result is {result}")
total = first_row[3] + first_row[4] + first_row[5] + first_row[6]

# Initialize an empty dictionary
electricity_dict = {}
water_dict = {}

# Loop through each row in the result
for row in result:
    water = row[5]  # Value for the dictionary
    key = row[7]  # Key for the dictionary
    
    # Add the key-value pair to the dictionary
    water_dict[key] = water

for row in result:
    electricity = row[4]  # Value for the dictionary
    key = row[7]  # Key for the dictionary
    
    # Add the key-value pair to the dictionary
    electricity_dict[key] = electricity

# Print the resulting dictionary
#print(electricity_dict)

# Sorting the dictionary by keys
sorted_electricity_dict = {key: electricity_dict[key] for key in sorted(electricity_dict)}
sorted_water_dict = {key: water_dict[key] for key in sorted(water_dict)}

print(sorted_electricity_dict)

# Chart 1: Bar chart of sales data
fig1, ax1 = plt.subplots(figsize=(5, 2)) # Create a figure for the whole chart (container) and its components (bars)
ax1.bar(sorted_electricity_dict.keys(), sorted_electricity_dict.values()) # Specify the type of chart and its contents/values
ax1.set_title("Electricity Bill") # Set the title of the chart
ax1.set_xlabel("Month") # Set the label for the X axis
ax1.set_ylabel("Amount") # Set the label for the Y axis

# Chart 4: Line chart of sales by year
fig4, ax4 = plt.subplots(figsize=(5, 2))
ax4.plot(list(sorted_water_dict.keys()), list(sorted_water_dict.values()))
ax4.set_title("Water Bill") # Set the title of the chart
ax4.set_xlabel("Month") # Set the label for the X axis
ax4.set_ylabel("Amount") # Set the label for the Y axis
#plt.show() # Show the chart

canvas1 = FigureCanvasTkAgg(fig1, electricity_overview) # Adding fig1 chart to the parent frame - upper_frame
canvas1.draw() # Show the canvas inside the frame similar to plt.show()
canvas1.get_tk_widget().pack(side="left", fill="both") # Sets the position ang properties of fig1

water_ytd = ctk.CTkLabel(water_overview, text="Average YTD Bill: 1000")
water_ytd.pack()

canvas4 = FigureCanvasTkAgg(fig4, water_overview) 
canvas4.draw() 
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True) 

# electricitydb = retrieve_data("electricity", "bill_tbl", "bill_id=1")
# waterdb = retrieve_data("water", "bill_tbl", "bill_id=1")
# internetdb = retrieve_data("internet", "bill_tbl", "bill_id=1")
# totaldb = retrieve_data("total", "bill_tbl", "bill_id=1")

def open_new():
    new_window = ctk.CTkToplevel(root)
    new_window.title("New Entry")
    new_window.geometry("300x200")
    
    # Set the top-level window to always be on top
    new_window.attributes("-topmost", True)
    new_window.lift()
    
    # Add widgets to the top-level window
    label = tk.Label(new_window, text="This is a new window!")
    label.pack(pady=20)
    button = tk.Button(new_window, text="Close", command=new_window.destroy)
    button.pack(pady=10)

overview_1_title = ctk.CTkLabel(details_overview, text="Rent and Utilities for this Month.")
overview_1_rent = ctk.CTkLabel(details_overview, text=f"Rent: {first_row[3]}")
overview_1_electricity = ctk.CTkLabel(details_overview, text=f"Electricity: {first_row[4]}")
overview_1_water = ctk.CTkLabel(details_overview, text=f"Water: {first_row[5]}")
overview_1_internet = ctk.CTkLabel(details_overview, text=f"Internet: {first_row[6]}")
overview_1_total = ctk.CTkLabel(details_overview, text=f"TOTAL: {total}")
overview_1_button = ctk.CTkButton(details_overview, text="Enter new data", command=open_new)

overview_1_title.grid(row=0 ,column=0)
overview_1_rent.grid(row=1 ,column=0)
overview_1_electricity.grid(row=2 ,column=0)
overview_1_water.grid(row=3 ,column=0)
overview_1_internet.grid(row=4 ,column=0)
overview_1_total.grid(row=5 ,column=0)
overview_1_button.grid(row=6, column=0)

#END TEST ##############


def unit_1_details():
    apartment_details_frame.place(x=100,y=2350)
    details_overview.grid(row= 0, column=0, pady=5, padx=5)
    water_overview.grid(row= 0, column=1, pady=5, padx=0)
    electricity_overview.grid(row= 0, column=2, pady=5, padx=5)
    down(max_down)

# Apartment Units Button
unit1_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 160))
unit1_button = ctk.CTkButton(frame, text="", image=unit1_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black', command=unit_1_details)
unit1_button.place(x=265, y=2095)

unit2_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 160))
unit2_button = ctk.CTkButton(frame, text="", image=unit2_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black')
unit2_button.place(x=550, y=2095)

unit3_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 160))
unit3_button = ctk.CTkButton(frame, text="", image=unit3_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black')
unit3_button.place(x=835, y=2095)

unit4_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 160))
unit4_button = ctk.CTkButton(frame, text="", image=unit4_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black')
unit4_button.place(x=1120, y=2095)

unit5_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 165))
unit5_button = ctk.CTkButton(frame, text="", image=unit5_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black')
unit5_button.place(x=265, y=1920)

unit6_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 165))
unit6_button = ctk.CTkButton(frame, text="", image=unit6_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black')
unit6_button.place(x=550, y=1920)

unit7_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 165))
unit7_button = ctk.CTkButton(frame, text="", image=unit7_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black')
unit7_button.place(x=835, y=1920)

unit8_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 165))
unit8_button = ctk.CTkButton(frame, text="", image=unit8_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black')
unit8_button.place(x=1120, y=1920)
# End Apartment Units Button

#TEST
global move_up
global apartment_down
global max_down
move_up = 0
apartment_down = -1530
max_down = -abs(new_height)+window_height

# Function to animate frame from top to bottom
def down(y):
    global move_up
    if (move_up > y):
        move_up -= 10
        frame.place(x=0, y=move_up)
        root.after(5, lambda: down(y))
        #print(move_up)
        #down_button.configure(text=move_up)

# Function to animate frame from bottom to top
def up(y):
    global move_up
    if (move_up < y):
        move_up += 10
        frame.place(x=0, y=move_up)
        root.after(5, lambda: up(y))
        #print(move_up)
        #up_button.configure(text=move_up)
 
## TEST FUNCTIONS ##
logout_button = ctk.CTkButton(frame, text="Logout", command=lambda: up(0))
logout_button.place(x=265 ,y=1800)

back_button = ctk.CTkButton(frame, text="Back", command=lambda: up(apartment_down))
back_button.place(x=100,y=2320)
# def up_test():
#     global y_test
#     #if y_test > 225:
#     y_test -= 10
#     test_frame.place(x=x_test, y=y_test)
#         #up_button.configure(text=y_test)
#         #root.after(16, up)
#     up_button.configure(text=y_test)

# def down_test():
#     global y_test
#     #if y_test < 585:
#     y_test += 10
#     test_frame.place(x=x_test, y=y_test)
#         #down_button.configure(text=y_test)
#         #root.after(16, down)
#     down_button.configure(text=y_test)
        
# def left_test():
#     global x_test
#     #if x_test > 206:
#     x_test -= 10
#     test_frame.place(x=x_test, y=y_test)
#         #left_button.configure(text=x_test)
#         #root.after(16, left)
#     left_button.configure(text=x_test)

# def right_test():
#     global x_test
#     #if x_test < 494:
#     x_test += 10
#     test_frame.place(x=x_test, y=y_test)
#         #right_button.configure(text=x_test)
#         #root.after(16, right)  
#     right_button.configure(text=x_test)
            
# FIRST STOP 1210
# SECOND STOP 1960

#1920 x 265 second floor
#2095 x 265 first floor

# UNIT column 0, 1, 2, 3
# 265, 550, 835, 1120

# ROOM SIZE LENGTH 265 - 515
# 250 px

# ROOM SIZE HEIGHT 2095 - 2265
# 170px
#END TEST 

#TEST
# down_button = ctk.CTkButton(root, text="DOWN", command=down_test)
# down_button.place(x=50, y=600)

# up_button = ctk.CTkButton(root, text="UP", command=up_test)
# up_button.place(x=50, y=500)

# left_button = ctk.CTkButton(root, text="LEFT", command=left_test)
# left_button.place(x=200, y=500)

# right_button = ctk.CTkButton(root, text="RIGHT", command=right_test)
# right_button.place(x=200, y=600)
#down()
#END

# Function to run the code repeatedly until the user closes it
root.mainloop()