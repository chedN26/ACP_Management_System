import tkinter # Python library for constructing basic graphical user interface (GUI) applications
from tkinter import ttk # Package for other components of tkinter (ttk - themed tkinter)
from tkinter import messagebox # Package for tkinter messageBox Popup
import mysql.connector # Package for using XAMPP MySql; use the command "python3 -m pip install mysql-connector"
from mysql.connector import Error # Handles execution error with the database

# Function to establish a new connection
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='acp_management_db'
    )

# Function to execute a query with error handling
def mysql_query(query, values=None):
    conn = None # Initialize the connection variable
    try:
        # Create the connection if it doesn't exist
        if conn is None or not conn.is_connected():
            conn = create_connection()
        
        # Check if the connection is successful
        if conn.is_connected():
            print("Connected to the database.")
        
        # The query to be exceuted
        execute_query = query
        
        # Execute a query
        cursor = conn.cursor()
        
        # If values are provided, use them in the query
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
            
        conn.commit() # Commit the query
        print("Query executed successfully")

        # Now close the connection after the query is done
        cursor.close()
        conn.close()
        print("Connection closed.")
        
    except Error as e:
        print(f"Error: {e}") # Shows the error in the termninal in any occurs

    finally: # Secure the connection is close
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed.")

# Function to get the data from Entry input box, combo box, spin box, and check button and insert into database
def enter_data():
    terms = terms_var.get() # get function to get the user input from entry
    
    if terms=="I accept.": # Condition to require check button (terms) to be checked
        first_name = firstNameEntry.get()
        second_name = secondNameEntry.get()
        title = title_comboBox.get()
        age = age_spinbox.get()
        infinity = infinity_spinbox.get()
        check = check_var.get()
              
        insert_query = """INSERT INTO mytable (firstName, secondName, title, age, infinity, check_register) VALUES (%s, %s, %s, %s, %s, %s)""" # Query for inserting data
        insert_values = (first_name, second_name, title, age, infinity, check) # Values of the data
        
        mysql_query(create_table_query) # Create table query
        mysql_query(insert_query, insert_values) # Insert query
        
        print(f"First Name: ", first_name, "\nSecond Name: ", second_name, "\nTitle: ", title)
        print(f"Age: ", age, "\nInfinity: ", infinity, " Check: ", check, " Terms: ", terms)
        print("---------------------------------")
    else:
        tkinter.messagebox.showwarning(title="Warning", message="Fill out all fields.")

# Query to create database table
create_table_query = """
                    CREATE TABLE IF NOT EXISTS mytable (
                        firstName VARCHAR(100),
                        secondName VARCHAR(100),
                        title VARCHAR(50),
                        age INT,
                        infinity INT,
                        check_register VARCHAR(50))"""
                        
def retrieve_data():
    # Query to select all data from the table
    query = "SELECT * FROM mytable"
    
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


def delete_data(row_id):
    # Query to delete a row from the table based on a specific condition
    query = "DELETE FROM mytable WHERE age = %s"  # Assuming 'id' is the primary key column

    # Create connection to the database
    conn = create_connection()

    try:
        if conn.is_connected():
            print("Connected to the database.")
        
        cursor = conn.cursor()  # Create cursor object
        
        # Execute the delete query with the row_id value
        cursor.execute(query, (row_id,))
        
        conn.commit()  # Commit the transaction
        print(f"Row with ID {row_id} DELETED successfully.")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and connection after the operation
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed.")
            

def edit_data(first_name, second_name, age):
    # Query to delete a row from the table based on a specific condition
    query = """UPDATE mytable 
                SET firstName = %s, secondName = %s
                WHERE age = %s;
                """  # Assuming 'id' is the primary key column

    # Create connection to the database
    conn = create_connection()

    try:
        if conn.is_connected():
            print("Connected to the database.")
        
        cursor = conn.cursor()  # Create cursor object
        
        # Execute the delete query with the row_id value
        cursor.execute(query, (first_name, second_name, age))
        
        conn.commit()  # Commit the transaction
        print(f"Row with ID {age} EDITED successfully.")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and connection after the operation
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed.")


window = tkinter.Tk() # Create the main GUI window
window.title("ACP Management System") # Set the window title

# IMPORTANT: When creating tkinter widgets, FIRST create and define the widget; SECOND Use a geometry/layout manager for the widget (pack/place/grid)
frame = tkinter.Frame(window) # Create a widget inside the window; window is the parent of the frame
frame.pack() # Layout Manager | IMPORTANT: Always use layout manager for every widget created

firstLabelFrame = tkinter.LabelFrame(frame, text="First Label Frame") # Create a widget inside the frame; frame is the parent of the labelFrame
#padx - horizontal padding, pady - vertical padding
firstLabelFrame.grid(row=0, column=0, padx=20, pady=20) # Layout manager for labelFrames; arguments/parameters specify the position of labelFrame inside the grid

second_label_frame = tkinter.LabelFrame(frame, text="Second Label Frame")
second_label_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20) # sticky adapts to the size of the window based on "news" or north east west south (literally up, down, left, right based on each letter)

third_label_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
third_label_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

fourth_label_frame = tkinter.LabelFrame(frame)
fourth_label_frame.grid(row=3, column=0)

firstNameLabel = tkinter.Label(firstLabelFrame, text="First Name Label") # Create internal widget (label) inside firstLabelFrame
firstNameLabel.grid(row=0, column=0)
secondNameLabel = tkinter.Label(firstLabelFrame, text="Second Name Label")
secondNameLabel.grid(row=0, column=1)

firstNameEntry = tkinter.Entry(firstLabelFrame) # Create a text box (entry) for user input inside firstLabelFrame
firstNameEntry.grid(row=1, column=0)
secondNameEntry = tkinter.Entry(firstLabelFrame)
secondNameEntry.grid(row=1, column=1)

title_label = tkinter.Label(firstLabelFrame, text="Title")
title_label.grid(row=0, column=2)
title_comboBox = ttk.Combobox(firstLabelFrame, values=["", "Mr.", "Mrs.", "Ms."]) # Create a combo box using ttk; arguments/parameters specify the parent of the widget and combo box values
title_comboBox.grid(row=1, column=2)

age_label = tkinter.Label(firstLabelFrame, text="Age")
age_label.grid(row=3, column=0)
age_spinbox = tkinter.Spinbox(firstLabelFrame, from_=18, to=110)
age_spinbox.grid(row=4, column=0)

check_var = tkinter.StringVar(value="Unchecked") # Variable to store the value of check_check (can be any data type); put a default argument to uncheck the checkbutton upon running
check_label = tkinter.Label(second_label_frame, text="Check Box")
check_label.grid(row=0, column=0)
check_check = tkinter.Checkbutton(second_label_frame, text="Check me!", variable=check_var, onvalue="Checked", offvalue="Unchecked") # bind the variable using "variable" parameter and put values to checked and unchecked
check_check.grid(row=1, column=0)

infinity_label = tkinter.Label(second_label_frame, text="Infinity Spin")
infinity_label.grid(row=0, column=1)
infinity_spinbox = tkinter.Spinbox(second_label_frame, from_=0, to="infinity") # put any string to the value of "to=" to remove the maximum
infinity_spinbox.grid(row=1, column=1)

terms_var = tkinter.StringVar(value="I do not accept.")
terms_check = tkinter.Checkbutton(third_label_frame, text="I accept the terms and conditions.", variable=terms_var, onvalue="I accept.", offvalue="I do not accept.")
terms_check.grid(row=0, column=0)

enter_button = tkinter.Button(frame, text="Submit", command=enter_data)
enter_button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

retrieve_button = tkinter.Button(frame, text="Retrieve", command=retrieve_data)
retrieve_button.grid(row=5, column=0, sticky="news", padx=20, pady=10)

delete_button = tkinter.Button(frame, text="delete", command=lambda: delete_data(21))
delete_button.grid(row=6, column=0, sticky="news", padx=20, pady=10)

edit_button = tkinter.Button(frame, text="edit", command=lambda: edit_data("John", "Doe", 18))
edit_button.grid(row=7, column=0, sticky="news", padx=20, pady=10)

# For Loop to add same padding to all widgets inside firstLabelFrame
for widget in firstLabelFrame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop() # Function to run the code repeatedly until the user closes it
