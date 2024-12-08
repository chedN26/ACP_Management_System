import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image
import mysql.connector # Package for using XAMPP MySql; use the command "python3 -m pip install mysql-connector"
from mysql.connector import Error # Handles execution error with the database
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt # Package for using GUI charts
import sys
from datetime import datetime
from sql import mysql_query, retrieve_data, refresh_bill
#from functions import *

# Color palette of the charts
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#1737a7", "#244dbb", "#5d56c1"])

# Functions ========================================================================================================================
# Function to animate frame from top to bottom
def down(y):
    global move_up
    if (move_up > y):
        move_up -= 10
        frame.place(x=0, y=move_up)
        root.after(5, lambda: down(y))

# Function to animate frame from bottom to top
def up(y):
    global move_up
    if (move_up < y):
        move_up += 10
        frame.place(x=0, y=move_up)
        root.after(5, lambda: up(y))

        unit1_button.configure(fg_color="black")
        unit2_button.configure(fg_color="black")
        unit3_button.configure(fg_color="black")
        unit4_button.configure(fg_color="black")
        unit5_button.configure(fg_color="black")
        unit6_button.configure(fg_color="black")
        unit7_button.configure(fg_color="black")
        unit8_button.configure(fg_color="black")

        unit1_button.configure(state="normal")
        unit2_button.configure(state="normal")
        unit3_button.configure(state="normal")
        unit4_button.configure(state="normal")
        unit5_button.configure(state="normal")
        unit6_button.configure(state="normal")
        unit7_button.configure(state="normal")
        unit8_button.configure(state="normal")
    plt.close('all')

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

def login():
    username = user_entry.get()
    password = password_entry.get()

    if (username=="c" and password=="c"):
        user_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        # down_values = {"y": apartment_down, "frame": frame, "root": root}
        # down(down_values)
        down(apartment_down)
        login_welcomelbl.focus_set()
        if (wrong_warning.winfo_exists()):
            wrong_warning.grid_remove()
        else:
            print("Warning doesn't exist.")
        #print("correct")
    else:
        wrong_warning.grid(row=4, column=0, pady=20)
        wrong_warning.configure(text="Incorrect username or password!")
        #print("wrong")
        
        
# Function to stop the program when closed
def on_close():
    sys.exit()
    
# Functions ========================================================================================================================


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

root.protocol("WM_DELETE_WINDOW", on_close) # Dependency on root creation

# Load the image using PIL
original_image = Image.open('sunset-ps.png')  # Replace with your image path

# Set the desired width for the image
new_width = window_width  # Example width you want to set

# Calculate the height based on the aspect ratio
width, height = original_image.size
new_height = int((new_width / width) * height)

global move_up
global apartment_down
#global max_down
move_up = 0
apartment_down = -1530
max_down = -abs(new_height)+window_height

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
login_frame = ctk.CTkFrame(frame, width=login_width, height=login_height, fg_color="#1737a7")
login_frame.place(x=center_width-(login_width/2)+80, y=center_height-(login_height/2))

login_welcomelbl = ctk.CTkLabel(login_frame, text="DueDeet Apartment", font=("Segoe UI", 20, "bold"))
login_welcomelbl.grid(row=0 ,column=0, padx=100, pady=40)

user_entry = ctk.CTkEntry(login_frame, placeholder_text="Enter your username.")
user_entry.grid(row=1 ,column=0, pady=5)

password_entry = ctk.CTkEntry(login_frame, placeholder_text="Enter your password.")
password_entry.grid(row=2 ,column=0, pady=5)

wrong_warning = ctk.CTkLabel(login_frame, text="", text_color="red")

login_button = ctk.CTkButton(login_frame, text="Login", command=login)
login_button.grid(row=3 ,column=0, pady=20)


def unit_details(i):
    #apartment_details_frame.place(x=100,y=2350)
    global save_id
    save_id = i

    # Create Tab View
    global overview_width
    overview_width = ((window_width-300))//3
    apartment_tab = ctk.CTkTabview(frame, width=overview_width)
    apartment_tab.place(x=100,y=2350)

    # Add Tabs to Tab View
    tab_1 = apartment_tab.add("Overview")
    tab_2 = apartment_tab.add("Previous")
    
    # Overview Frames
    apartment_details_frame = ctk.CTkFrame(tab_1, width=window_width-200, height=350, fg_color='white')
    details_overview = ctk.CTkFrame(apartment_details_frame, fg_color="#1737a7", border_width=1, border_color="#1737a7")
    water_overview = ctk.CTkFrame(apartment_details_frame, fg_color="#244dbb", border_width=1, border_color="#244dbb")
    electricity_overview = ctk.CTkFrame(apartment_details_frame, fg_color="#5d56c1", border_width=1, border_color="#5d56c1")
    
    
    def refresh_table():
        refresh_bill()
        refreshed_unit_query = """SELECT * FROM bill_tbl WHERE unit_id = %s ORDER BY month DESC"""
        refreshed_unit_values = (save_id,)
        print("Save ID: ", save_id)
        refreshed_bill = retrieve_data(refreshed_unit_query, refreshed_unit_values)

        # Refresh the table
        for widget in unit_table_frame.winfo_children():  # Iterate over all widgets inside the frame
            widget.destroy()

        if refreshed_bill:
            root.after(10, populate_parent_frame(unit_table_frame, refreshed_bill, labels))
            
        print("Table Refreshed")
        
        
    def refresh_graph():
        for widget in water_overview.winfo_children():  # Iterate over all widgets inside the frame
            widget.destroy()
        for widget in electricity_overview.winfo_children():  # Iterate over all widgets inside the frame
            widget.destroy()
        plt.close('all')
        graphs()

    def graphs():
        # Acessing the query result
        result_query = """SELECT * FROM bill_tbl WHERE unit_id = %s ORDER BY month DESC"""
        result_values = (save_id,)
        result = retrieve_data(result_query, result_values)

        if result:
            first_row = result[0]
            total = first_row[3] + first_row[4] + first_row[5] + first_row[6]
        else:
            first_row = ()
            total = 0.0
        retrieve_water_query = """SELECT * FROM water_tbl WHERE unit_id = %s"""
        retrieve_water_values = (save_id,)
        retrieve_water = retrieve_data(retrieve_water_query, retrieve_water_values)

        retrieve_electricity_query = """SELECT * FROM electricity_tbl WHERE unit_id = %s"""
        retrieve_electricity_values = (save_id,)
        retrieve_electricity = retrieve_data(retrieve_electricity_query, retrieve_electricity_values)

        # Initialize an empty dictionary
        electricity_dict = {}
        water_dict = {}
        dummy_dict = {'Jan' : 0, 'Feb' : 0, 'Mar' : 0, 'Apr' : 0, 'May' : 0, 'Jun' : 0, 'Jul' : 0, 'Aug' : 0, 'Sep' : 0, 'Oct' : 0, 'Nov' : 0, 'Dec' : 0}
        month_abb = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

        if retrieve_water:
        # Loop through each row in the result
            for row in retrieve_water:
                water = row[6]  # Value for the dictionary
                key = row[7]  # Key for the dictionary

                # Add the key-value pair to the dictionary
                water_dict[key] = water
            sorted_water_dict = {key: water_dict[key] for key in sorted(water_dict)} # Sorting the dictionary by keys
            water_month = [month_abb[key.month - 1] for key in list(sorted_water_dict.keys())] # Convert months to abbreviated names
            print("BEFORE AVERAGE WATER")
            average_water = sum(sorted_water_dict.values()) / len(sorted_water_dict)
            print("AFTER AVERAGE WATER")

        if retrieve_electricity:
            for row in retrieve_electricity:
                electricity = row[6]  # Value for the dictionary
                key = row[7]  # Key for the dictionary

                # Add the key-value pair to the dictionary
                electricity_dict[key] = electricity

            sorted_electricity_dict = {key: electricity_dict[key] for key in sorted(electricity_dict)}
            electricity_month = [month_abb[key.month - 1] for key in list(sorted_electricity_dict.keys())]
            print("BEFORE AVERAGE ELECTRICITY")
            average_electricity = sum(sorted_electricity_dict.values()) / len(sorted_electricity_dict)
            print("AFTER AVERAGE ELECTRICITY")


        # Chart 1: Bar chart of electricity ==================================================================================
        fig1, ax1 = plt.subplots(figsize=(5, 3.2)) # Create a figure for the whole chart (container) and its components (bars)
        # Set the size and position of the axes (relative to the figure size)
        # [left, bottom, width, height] in normalized figure coordinates (0 to 1 range)
        # Set the size of the axes
        axes_width = 0.7  # 50% of the figure's width
        axes_height = 0.7  # 50% of the figure's height

        # Calculate the position to center the axes in the figure
        left = (1 - axes_width) / 2  # Center horizontally
        bottom = (1 - axes_height) / 2  # Center vertically
        ax1.set_position([left, bottom, axes_width, axes_height])  # Adjust these values as needed
        if retrieve_electricity:
            ax1.bar(electricity_month, sorted_electricity_dict.values()) # Specify the type of chart and its contents/values
        else:
            ax1.bar(dummy_dict.keys(), dummy_dict.values())
        ax1.set_title("Electricity Bill") # Set the title of the chart
        ax1.set_xlabel("Month") # Set the label for the X axis
        ax1.set_ylabel("Amount") # Set the label for the Y axis
        
        if retrieve_electricity:
            electricity_ytd = ctk.CTkLabel(electricity_overview, text=f"Average YTD Bill: {average_electricity:.2f} Pesos", width=overview_width, corner_radius=10)
        else:
            electricity_ytd = ctk.CTkLabel(electricity_overview, text=f"Average YTD Bill: 0.0 Pesos", width=overview_width, corner_radius=10)
        electricity_ytd.pack()
        canvas1 = FigureCanvasTkAgg(fig1, electricity_overview) # Adding fig1 chart to the parent frame - upper_frame
        canvas1.draw() # Show the canvas inside the frame similar to plt.show()
        canvas1.get_tk_widget().pack(fill="both", padx=5, pady=5) # Sets the position ang properties of fig1
        # Chart 1: Bar chart of electricity ==================================================================================


        # Chart 4: Line chart of water =======================================================================================
        fig4, ax4 = plt.subplots(figsize=(5, 3.2))
        ax4.set_position([left, bottom, axes_width, axes_height])  # Adjust these values as needed
        if retrieve_water:
            ax4.plot(water_month, list(sorted_water_dict.values()))
        else:
            ax4.plot(list(dummy_dict.keys()), list(dummy_dict.values()))
        ax4.set_title("Water Bill") # Set the title of the chart
        ax4.set_xlabel("Month") # Set the label for the X axis
        ax4.set_ylabel("Amount") # Set the label for the Y axis
        
        if retrieve_water:
            water_ytd = ctk.CTkLabel(water_overview, text=f"Average YTD Bill: {average_water:.2f} Pesos", width=overview_width, corner_radius=10)
        else:
            water_ytd = ctk.CTkLabel(water_overview, text=f"Average YTD Bill: 0.0 Pesos", width=overview_width, corner_radius=10)
        water_ytd.pack()
        canvas4 = FigureCanvasTkAgg(fig4, water_overview)
        canvas4.draw()
        canvas4.get_tk_widget().pack(fill="both", padx=5, pady=5)
        # Chart 4: Line chart of water =======================================================================================
        
        water_overview.grid(row= 0, column=1, pady=5, padx=0, ipadx=5)
        electricity_overview.grid(row= 0, column=2, pady=5, padx=5, ipadx=5)
    #END graphs function
    
    
    # TOP LEVEL ======================================================================================== TOP LEVEL
    # Function to open top level window
    def open_new():
        new_window = ctk.CTkToplevel(root)
        new_window.title("New Entry")
        new_window.geometry("720x300")

        # Set the top-level window to always be on top
        new_window.attributes("-topmost", True)

        # Function to close top level window
        def close_top():
            refresh_bill()
            refresh_table()
            new_window.destroy()
        # END close_top function
        
        new_window.protocol("WM_DELETE_WINDOW", close_top)

        # TOP LEVEL WINDOW ENTRY FRAME
        entry_frame = ctk.CTkFrame(new_window)
        entry_frame.grid(row=0 ,column=0, pady=20, padx=40)

        # Entry for Rent Bill
        rent_label = ctk.CTkLabel(entry_frame, text="Rent: ")
        rent_label.grid(row=0, column=0, padx=5)
        rent_entry = ctk.CTkEntry(entry_frame, placeholder_text="Enter Rent")
        rent_entry.grid(row=0, column=1)

        # Entry for Internet Bill
        internet_label = ctk.CTkLabel(entry_frame, text="Internet: ")
        internet_label.grid(row=1, column=0, padx=5)
        internet_entry = ctk.CTkEntry(entry_frame, placeholder_text="Enter Amount")
        internet_entry.grid(row=1, column=1)

        # Entry for Water Bill
        water_label = ctk.CTkLabel(entry_frame, text="Water: ")
        water_label.grid(row=2, column=0, padx=5)
        prev_water_entry = ctk.CTkEntry(entry_frame, placeholder_text="Previous Reading")
        prev_water_entry.grid(row=2, column=1)
        current_water_entry = ctk.CTkEntry(entry_frame, placeholder_text="Current Reading")
        current_water_entry.grid(row=2, column=2)
        rate_water_entry = ctk.CTkEntry(entry_frame, placeholder_text="Rate")
        rate_water_entry.grid(row=2, column=3)
        date_water = ctk.CTkEntry(entry_frame, placeholder_text="YYYY-MM-DD")
        date_water.grid(row=2, column=4)

        # Entry for Electricity Bill
        electricity_label = ctk.CTkLabel(entry_frame, text="Electricity: ")
        electricity_label.grid(row=3, column=0, padx=5)
        prev_electricity_entry = ctk.CTkEntry(entry_frame, placeholder_text="Previous Reading")
        prev_electricity_entry.grid(row=3, column=1)
        current_electricity_entry = ctk.CTkEntry(entry_frame, placeholder_text="Current Reading")
        current_electricity_entry.grid(row=3, column=2)
        rate_electricity_entry = ctk.CTkEntry(entry_frame, placeholder_text="Rate")
        rate_electricity_entry.grid(row=3, column=3)
        date_electricity = ctk.CTkEntry(entry_frame, placeholder_text="YYYY-MM-DD")
        date_electricity.grid(row=3, column=4)

        query_label_water = ctk.CTkLabel(new_window, text="")
        query_label_water.grid(row=4, column=0)
        query_label_electricity = ctk.CTkLabel(new_window, text="")
        query_label_electricity.grid(row=5, column=0)
        # END TOP LEVEL WINDOW ENTRY FRAME ===============================================
    # TOP LEVEL ======================================================================================== TOP LEVEL

        # Function to INSERT data to database
        def create_entry():
            unit = save_id # get function to get the user input from entry
            rent = rent_entry.get()

            prev_water = prev_water_entry.get()
            current_water = current_water_entry.get()
            rate_water = rate_water_entry.get()
            date_water_var = date_water.get()

            prev_electricity = prev_electricity_entry.get()
            current_electricity = current_electricity_entry.get()
            rate_electricity = rate_electricity_entry.get()
            date_electricity_var = date_electricity.get()

            internet = internet_entry.get()

            if unit: 
                insert_query_water = """INSERT INTO water_tbl (unit_id, prev_meter, current_meter, rate, date) VALUES (%s, %s, %s, %s, %s)""" # Query for inserting data
                insert_values_water = (unit, prev_water, current_water, rate_water, date_water_var) # Values of the data

                insert_query_electricity = """INSERT INTO electricity_tbl (unit_id, prev_meter, current_meter, rate, date) VALUES (%s, %s, %s, %s, %s)""" # Query for inserting data
                insert_values_electricity = (unit, prev_electricity, current_electricity, rate_electricity, date_electricity_var) # Values of the data

                refresh_water_query = """UPDATE water_tbl
                                        SET consumption = current_meter - prev_meter,
                                        water_total = rate * consumption;"""

                refresh_electricity_query = """UPDATE electricity_tbl
                                            SET consumption = current_meter - prev_meter,
                                            electricity_total = rate * consumption;"""

                if rate_electricity:
                    #mysql_query(create_table_query) # Create table query
                    mysql_query(insert_query_electricity, insert_values_electricity) # Insert query
                    print("INSERT INTO electricity_tbl query successful.")
                    mysql_query(refresh_electricity_query)
                    print("Refresh electricity successful.")
                    query_label_electricity.configure(text="INSERT INTO electricity_tbl query successful.")
                else:
                    print("Failed to INSERT INTO electricity_tbl.")
                    query_label_electricity.configure(text="Failed to INSERT INTO electricity_tbl.")

                if rate_water:
                    #mysql_query(create_table_query) # Create table query
                    mysql_query(insert_query_water, insert_values_water) # Insert query
                    print("INSERT INTO water_tbl query successful.")
                    mysql_query(refresh_water_query)
                    print("Refresh water successful.")
                    query_label_water.configure(text="INSERT INTO water_tbl query successful.")
                else:
                    print("Failed to INSERT INTO water_tbl.")
                    query_label_water.configure(text="Failed to INSERT INTO water_tbl.")
            else:
                tk.messagebox.showwarning(title="Warning", message="Fill out all fields.")

            # Refresh bill_tbl in database
            refresh_bill()
            
            # Refresh graphs in Overview Tab
            refresh_graph()
            
            # Refresh table
            refresh_table()

            rent_entry.delete(0, ctk.END)
            internet_entry.delete(0, ctk.END)
            prev_water_entry.delete(0, ctk.END)
            current_water_entry.delete(0, ctk.END)
            rate_water_entry.delete(0, ctk.END)
            date_water.delete(0, ctk.END)
            prev_electricity_entry.delete(0, ctk.END)
            current_electricity_entry.delete(0, ctk.END)
            rate_electricity_entry.delete(0, ctk.END)
            date_electricity.delete(0, ctk.END)

            rent_entry.configure(placeholder_text="Enter Rent")
            internet_entry.configure(placeholder_text="Enter Amount")
            prev_water_entry.configure(placeholder_text="Previous Reading")
            current_water_entry.configure(placeholder_text="Current Reading")
            rate_water_entry.configure(placeholder_text="Rate")
            date_water.configure(placeholder_text="YYYY-MM-DD")
            prev_electricity_entry.configure(placeholder_text="Previous Reading")
            current_electricity_entry.configure(placeholder_text="Current Reading")
            rate_electricity_entry.configure(placeholder_text="Rate")
            date_electricity.configure(placeholder_text="YYYY-MM-DD")


        submit_button = ctk.CTkButton(new_window, text="Submit", command=create_entry)
        submit_button.grid(row=2 ,column=0, pady=5)

        close_button = ctk.CTkButton(new_window, text="Close", fg_color="red", command=close_top)
        close_button.grid(row=3 ,column=0 , pady=10)
        #END create_entry function
    # END open_new function
    # TOP LEVEL END ========================================================================================
    
    graphs()

    # Function to update a row in the database
    def update_row(id):
        unit = id

        prev_water_meter = edit_prev_water_entry.get()
        current_water_meter = edit_current_water_entry.get()
        rate_water = edit_rate_water_entry.get()
        date_water = edit_date_water.get()
        
        if date_water:
            convert_date_water = datetime.strptime(date_water, "%Y-%m-%d")
            month_water = convert_date_water.month
            year_water = convert_date_water.year
            print("Date water check.")
            # print("MONTH WATER", month_water)
            # print("YEAR WATER", year_water)

        if rate_water:
            update_water_query = """UPDATE water_tbl SET unit_id = %s, prev_meter = %s, current_meter = %s, rate = %s, date = %s WHERE MONTH(date) = %s AND YEAR(date) = %s"""
            values_water_query = (unit, prev_water_meter, current_water_meter, rate_water, date_water, month_water, year_water)
            mysql_query(update_water_query, values_water_query)

            refresh_water_query = """UPDATE water_tbl
                                        SET consumption = current_meter - prev_meter,
                                        water_total = rate * consumption;"""
            mysql_query(refresh_water_query)

            print(f"Updated water_tbl with month: {month_water} and {year_water}")

            # Refresh graphs in Overview Tab
            refresh_graph()
        # ===============================================================

        prev_electricity_meter = edit_prev_electricity_entry.get()
        current_electricity_meter = edit_current_electricity_entry.get()
        rate_electricity = edit_rate_electricity_entry.get()
        date_electricity = edit_date_electricity.get()

        if date_electricity:
            convert_date_electricity = datetime.strptime(date_electricity, "%Y-%m-%d")
            month_electricity = convert_date_electricity.month
            year_electricity = convert_date_electricity.year
            print("Date electricity check.")

        if rate_electricity:
            update_electricity_query = """UPDATE electricity_tbl SET unit_id = %s, prev_meter = %s, current_meter = %s, rate = %s, date = %s WHERE MONTH(date) = %s AND YEAR(date) = %s"""
            values_electricity_query = (unit, prev_electricity_meter, current_electricity_meter, rate_electricity, date_electricity, month_electricity, year_electricity)
            mysql_query(update_electricity_query, values_electricity_query)

            refresh_electricity_query = """UPDATE electricity_tbl
                                        SET consumption = current_meter - prev_meter,
                                        electricity_total = rate * consumption;"""
            mysql_query(refresh_electricity_query)
            print(f"Updated electricity_tbl with month: {month_electricity} and {year_electricity}")

            # Refresh the graphs
            refresh_graph()

            # Delete existing entry to update bill_tbl
            delete_after_query = """DELETE FROM bill_tbl WHERE month = %s AND year = %s AND unit_id = %s"""
            delete_after_value = (month_electricity, year_electricity, unit)
            mysql_query(delete_after_query, delete_after_value)

            # Refresh the table
            refresh_table()
            print("Table Refreshed")

        edit_date_water.configure(state='normal')
        edit_date_water.configure(state='normal')
        edit_date_electricity.configure(state='normal')
        edit_date_electricity.configure(state='normal')
        remove_text()
    # END update_row function


    # Function to delete a row in the database
    def delete_row(id, month, year):
        delete_water_query = """DELETE FROM water_tbl WHERE MONTH(date) = %s AND YEAR(date) = %s"""
        values_delete_electricity_query = (month, year)
        mysql_query(delete_water_query, values_delete_electricity_query)
        refresh_water_query = """UPDATE water_tbl
                                    SET consumption = current_meter - prev_meter,
                                    water_total = rate * consumption;"""
        mysql_query(refresh_water_query)
        # ============================================================================================
        delete_electricity_query = """DELETE FROM electricity_tbl WHERE MONTH(date) = %s AND YEAR(date) = %s"""
        values_delete_electricity_query = (month, year)
        mysql_query(delete_electricity_query, values_delete_electricity_query)
        refresh_electricity_query = """UPDATE electricity_tbl
                                    SET consumption = current_meter - prev_meter,
                                    electricity_total = rate * consumption;"""
        mysql_query(refresh_electricity_query)
        # ============================================================================================
        delete_query = """DELETE from bill_tbl WHERE bill_id = %s"""
        delete_id = id
        mysql_query(delete_query, (delete_id,))
        print(f"Deleted row with id {id}")
        # ============================================================================================

        # Refresh the table in Previous Tab
        refresh_table()

        # Refresh the graph in Overview Tab
        refresh_graph()
    # END delete_row function
    

    # Function to edit entry
    def edit_row(id, month, year):
        water_list_query = """SELECT * FROM water_tbl WHERE MONTH(date) = %s AND YEAR(date) = %s"""
        water_list_values = (month, year)
        water_list = retrieve_data(water_list_query, water_list_values)

        electricity_list_query = """SELECT * FROM electricity_tbl WHERE MONTH(date) = %s AND YEAR(date) = %s"""
        electricity_list_values = (month, year)
        electricity_list = retrieve_data(electricity_list_query, electricity_list_values)

        remove_text()
        edit_rent_entry.insert(0, "3500")
        edit_internet_entry.insert(0, "300")

        if water_list:
            water_tuple = water_list[0]
            edit_water_prev = water_tuple[2]
            edit_water_current = water_tuple[3]
            edit_water_rate = water_tuple[5]
            edit_water_date = water_tuple[7]

            edit_prev_water_entry.insert(0, edit_water_prev)
            edit_current_water_entry.insert(0, edit_water_current)
            edit_rate_water_entry.insert(0, edit_water_rate)
            edit_date_water.insert(0, edit_water_date)
            edit_date_water.configure(state='disabled')
            edit_date_water.configure(text_color='gray')

        if electricity_list:
            electricity_tuple = electricity_list[0]
            edit_electricity_prev = electricity_tuple[2]
            edit_electricity_current = electricity_tuple[3]
            edit_electricity_rate = electricity_tuple[5]
            edit_electricity_date = electricity_tuple[7]

            edit_prev_electricity_entry.insert(0, edit_electricity_prev)
            edit_current_electricity_entry.insert(0, edit_electricity_current)
            edit_rate_electricity_entry.insert(0, edit_electricity_rate)
            edit_date_electricity.insert(0, edit_electricity_date)
            edit_date_electricity.configure(state='disabled')
            edit_date_electricity.configure(text_color='gray')
    # END edit_row function


    def remove_text():
        edit_date_water.configure(state='normal')
        edit_date_water.configure(text_color='black')
        edit_date_electricity.configure(text_color='black')
        edit_date_electricity.configure(state='normal')

        edit_rent_entry.delete(0, ctk.END)
        edit_internet_entry.delete(0, ctk.END)

        edit_prev_electricity_entry.delete(0, ctk.END)
        edit_current_electricity_entry.delete(0, ctk.END)
        edit_rate_electricity_entry.delete(0, ctk.END)
        edit_date_electricity.delete(0, ctk.END)

        edit_prev_water_entry.delete(0, ctk.END)
        edit_current_water_entry.delete(0, ctk.END)
        edit_rate_water_entry.delete(0, ctk.END)
        edit_date_water.delete(0, ctk.END)

        edit_rent_entry.configure(placeholder_text="Enter Rent")
        edit_internet_entry.configure(placeholder_text="Enter Amount")

        edit_prev_electricity_entry.configure(placeholder_text="Previous Reading")
        edit_current_electricity_entry.configure(placeholder_text="Current Reading")
        edit_rate_electricity_entry.configure(placeholder_text="Rate")
        edit_date_electricity.configure(placeholder_text="YYYY-MM-DD")

        edit_prev_water_entry.configure(placeholder_text="Previous Reading")
        edit_current_water_entry.configure(placeholder_text="Current Reading")
        edit_rate_water_entry.configure(placeholder_text="Rate")
        edit_date_water.configure(placeholder_text="YYYY-MM-DD")
    # END remove_text function


    # Display frames inside Overview Tab ============================================================================ OVERVIEW TAB
    apartment_details_frame.pack() # Display parent frame in Overview Tab
    #Display frames inside apartment_details_frame (Overview Tab\apartment_details_frame\)
    details_overview.grid(row= 0, column=0, pady=5, padx=5, ipadx=5)

    # Display elements inside details_overview (Overview Tab\apartment_details_frame\details_overview\)
    result_overview_query = """SELECT * FROM bill_tbl where unit_id = %s ORDER BY month DESC"""
    result_overview_values = (save_id,)
    result_overview = retrieve_data(result_overview_query, result_overview_values)

    if result_overview:
        first_row = result_overview[0]
        total = first_row[3] + first_row[4] + first_row[5] + first_row[6]
    else:
        first_row = ()
        total = 0.0

    if first_row:
        overview_1_title = ctk.CTkLabel(details_overview, text="Rent and Utilities for this Month", width=overview_width-20, font=("Segoe UI", 20, "bold"))
        overview_1_rent = ctk.CTkLabel(details_overview, text=f"Rent: {first_row[3]:.2f}", font=("Segoe UI", 16))
        overview_1_electricity = ctk.CTkLabel(details_overview, text=f"Electricity: {first_row[4]:.2f}", font=("Segoe UI", 16))
        overview_1_water = ctk.CTkLabel(details_overview, text=f"Water: {first_row[5]:.2f}", font=("Segoe UI", 16))
        overview_1_internet = ctk.CTkLabel(details_overview, text=f"Internet: {first_row[6]:.2f}", font=("Segoe UI", 16))
        overview_1_total = ctk.CTkLabel(details_overview, text=f"TOTAL: {total:.2f}", font=("Segoe UI", 16, "bold"))
        overview_1_button = ctk.CTkButton(details_overview, text="Enter New Data", command=open_new)
        overview_1_button.grid(row=6, column=0, pady=27)
    else:
        overview_1_title = ctk.CTkLabel(details_overview, text="Rent and Utilities for this Month.", width=overview_width-20)
        overview_1_rent = ctk.CTkLabel(details_overview, text=f"Rent: 0.0")
        overview_1_electricity = ctk.CTkLabel(details_overview, text=f"Electricity: 0.0")
        overview_1_water = ctk.CTkLabel(details_overview, text=f"Water: 0.0")
        overview_1_internet = ctk.CTkLabel(details_overview, text=f"Internet: 0.0")
        overview_1_total = ctk.CTkLabel(details_overview, text=f"TOTAL: 0.0")
        overview_1_button = ctk.CTkButton(details_overview, text="Enter new data", command=open_new)
        overview_1_button.grid(row=6, column=0, pady=27)

    overview_1_title.grid(row=0 ,column=0, pady=20)
    overview_1_rent.grid(row=1 ,column=0)
    overview_1_electricity.grid(row=2 ,column=0)
    overview_1_water.grid(row=3 ,column=0)
    overview_1_internet.grid(row=4 ,column=0)
    overview_1_total.grid(row=5 ,column=0)
    # OVERVIEW TAB ================================================================================================== OVERVIEW TAB


    # Display frames inside Previous Tab ===========================+================================================ PREVIOUS TAB
    # Function to create a child frame for each tuple
    def create_child_frame(parent, tuple_data, labels):
        # Create a frame for each tuple (child frame)
        child_frame = ctk.CTkFrame(parent, border_width=1, border_color='white')
        edit_values = []

        # Iterate through the tuple and create a label for each value
        for i, value in enumerate(tuple_data[1:]):  # Skip the ID in the label
            label = ctk.CTkLabel(child_frame, text=f"{labels[i]}: {value}", anchor='w')
            label.pack(side=tk.LEFT, padx=15, pady=3)  # Pack the label into the child frame
            edit_values.append(value)

        # Add "Edit" and "Delete" buttons for each row, passing the ID
        button_edit = ctk.CTkButton(child_frame, text="Edit", command=lambda id=tuple_data[1], month=tuple_data[7], year=tuple_data[8]: edit_row(id, month, year), fg_color='green')
        button_edit.pack(side=tk.RIGHT, padx=5)

        button_delete = ctk.CTkButton(child_frame, text="Delete", command=lambda id=tuple_data[0], month=tuple_data[7], year=tuple_data[8]: delete_row(id, month, year), fg_color='red')
        button_delete.pack(side=tk.RIGHT, padx=5)
        return child_frame
    # END create_child_frame function

    # Function to populate the parent frame with child frames based on data
    def populate_parent_frame(parent, data, labels): # "data"  argument is the "result" variable with 'bill_tbl' argument
        # Clear any existing children in the parent frame (if re-populating)
        for widget in parent.winfo_children():
            widget.destroy()

        # Create child frames for each tuple in the data
        for item in data:
            child_frame = create_child_frame(parent, item, labels)
            child_frame.pack(fill=tk.X, pady=2)  # Add the child frame to the parent
    #END populate_parent_frame function


    unit_edit_frame = ctk.CTkFrame(tab_2)
    unit_table_frame = ctk.CTkScrollableFrame(tab_2, width=window_width-300, height=10)

    # Display frames inside Previous Tab
    unit_edit_frame.grid(row=1, column=0)
    unit_table_frame.grid(row=2, column=0, pady=5)

    # Entry for Rent Bill
    edit_rent_label = ctk.CTkLabel(unit_edit_frame, text="Rent: ")
    edit_rent_label.grid(row=0, column=0, padx=15)

    edit_rent_entry = ctk.CTkEntry(unit_edit_frame, placeholder_text="Enter Rent")
    edit_rent_entry.grid(row=0, column=1, padx=3)

    # Entry for Internet Bill
    edit_internet_label = ctk.CTkLabel(unit_edit_frame, text="Internet: ")
    edit_internet_label.grid(row=1, column=0, padx=15)

    edit_internet_entry = ctk.CTkEntry(unit_edit_frame, placeholder_text="Enter Amount")
    edit_internet_entry.grid(row=1, column=1, padx=3)

    # Entry for Water Bill
    edit_water_label = ctk.CTkLabel(unit_edit_frame, text="Water: ")
    edit_water_label.grid(row=0, column=3, pady=5, padx=15)

    edit_prev_water_entry = ctk.CTkEntry(unit_edit_frame, placeholder_text="Previous Reading")
    edit_prev_water_entry.grid(row=0, column=4, padx=3)

    edit_current_water_entry = ctk.CTkEntry(unit_edit_frame, placeholder_text="Current Reading")
    edit_current_water_entry.grid(row=0, column=5, padx=3)

    edit_rate_water_entry = ctk.CTkEntry(unit_edit_frame, placeholder_text="Rate")
    edit_rate_water_entry.grid(row=0, column=6, padx=3)

    edit_date_water = ctk.CTkEntry(unit_edit_frame, placeholder_text="YYYY-MM-DD")
    edit_date_water.grid(row=0, column=7, padx=3)

    # Entry for Electricity Bill
    edit_electricity_label = ctk.CTkLabel(unit_edit_frame, text="Electricity: ")
    edit_electricity_label.grid(row=1, column=3, pady=5, padx=15)

    edit_prev_electricity_entry = ctk.CTkEntry(unit_edit_frame, placeholder_text="Previous Reading")
    edit_prev_electricity_entry.grid(row=1, column=4, padx=3)

    edit_current_electricity_entry = ctk.CTkEntry(unit_edit_frame, placeholder_text="Current Reading")
    edit_current_electricity_entry.grid(row=1, column=5, padx=3)

    edit_rate_electricity_entry = ctk.CTkEntry(unit_edit_frame, placeholder_text="Rate")
    edit_rate_electricity_entry.grid(row=1, column=6, padx=3)

    edit_date_electricity = ctk.CTkEntry(unit_edit_frame, placeholder_text="YYYY-MM-DD")
    edit_date_electricity.grid(row=1, column=7, padx=3)

    save_edit_button = ctk.CTkButton(unit_edit_frame, text="Save", command=lambda: update_row(save_id))
    save_edit_button.grid(row=1, column=8, padx=20)
    cancel_edit_button = ctk.CTkButton(unit_edit_frame, text="Cancel", fg_color='gray', command=remove_text)
    cancel_edit_button.grid(row=0, column=8, padx=20)

    first_space = ctk.CTkLabel(unit_edit_frame, text=" ")
    first_space.grid(row=0, column=2, padx=15, ipadx=90)
    second_space = ctk.CTkLabel(unit_edit_frame, text=" ")
    second_space.grid(row=1, column=2, padx=10)
    # PREVIOUS TAB ================================================================================================== PREVIOUS TAB

    # Important
    # Pre-requesuite for populate_parent_frame function
    labels = ["Unit#: ", "Name: ", "Rent: ", "Electricity: ", "Water: ", "Internet", "Month: ", "Year: "]
    result_unit_query = """SELECT * FROM bill_tbl WHERE unit_id = %s"""
    result_unit_values = (save_id,)
    result_unit = retrieve_data(result_unit_query, result_unit_values)
    
    # Refresh contents of unit_table_frame
    if result_unit:
        populate_parent_frame(unit_table_frame, result_unit, labels)


    # Create a dictionary that maps logical names to button objects
    buttons_dict = {
        1: unit1_button, # Dependency on unit_button
        2: unit2_button,
        3: unit3_button,
        4: unit4_button,
        5: unit5_button,
        6: unit6_button,
        7: unit7_button,
        8: unit8_button
    }
    # Function to change the button color dynamically using its logical name
    def change_button_color(button_name):
        if button_name in buttons_dict:
            buttons_dict[button_name].configure(fg_color="yellow")  # Modify color


    # Important
    # down_values = {"y": max_down, "move_up": move_up, "frame": frame, "root": root}
    # down(down_values)
    down(max_down)
    
    change_button_color(save_id)
    unit1_button.configure(state="disabled")
    unit2_button.configure(state="disabled")
    unit3_button.configure(state="disabled")
    unit4_button.configure(state="disabled")
    unit5_button.configure(state="disabled")
    unit6_button.configure(state="disabled")
    unit7_button.configure(state="disabled")
    unit8_button.configure(state="disabled")
# END unit_details function


# Apartment Units Button
unit1_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 160))
unit1_button = ctk.CTkButton(frame, text="", image=unit1_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black', command=lambda save_id = 1: unit_details(save_id))
unit1_button.place(x=265, y=2095)

unit2_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 160))
unit2_button = ctk.CTkButton(frame, text="", image=unit2_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black', command=lambda save_id = 2: unit_details(save_id))
unit2_button.place(x=550, y=2095)

unit3_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 160))
unit3_button = ctk.CTkButton(frame, text="", image=unit3_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black', command=lambda save_id = 3: unit_details(save_id))
unit3_button.place(x=835, y=2095)

unit4_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 160))
unit4_button = ctk.CTkButton(frame, text="", image=unit4_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black', command=lambda save_id = 4: unit_details(save_id))
unit4_button.place(x=1120, y=2095)

unit5_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 165))
unit5_button = ctk.CTkButton(frame, text="", image=unit5_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black', command=lambda save_id = 5: unit_details(save_id))
unit5_button.place(x=265, y=1920)

unit6_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 165))
unit6_button = ctk.CTkButton(frame, text="", image=unit6_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black', command=lambda save_id = 6: unit_details(save_id))
unit6_button.place(x=550, y=1920)

unit7_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 165))
unit7_button = ctk.CTkButton(frame, text="", image=unit7_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black', command=lambda save_id = 7: unit_details(save_id))
unit7_button.place(x=835, y=1920)

unit8_image = ctk.CTkImage(light_image=Image.open('apartment-unit.png'), dark_image=Image.open('apartment-unit.png'), size=(245, 165))
unit8_button = ctk.CTkButton(frame, text="", image=unit8_image, width=250, height=170, corner_radius=0, hover_color="yellow", fg_color='black', command=lambda save_id = 8: unit_details(save_id))
unit8_button.place(x=1120, y=1920)

logout_button = ctk.CTkButton(frame, text="Logout", command=lambda: up(0), corner_radius=5)
logout_button.place(x=window_width-305 ,y=1845)

back_button = ctk.CTkButton(frame, text="Back", command=lambda: up(apartment_down))
back_button.place(x=100,y=2320)
# End Apartment Units Button


# Function to run the code repeatedly until the user closes it
root.mainloop()