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
    
    
def retrieve_data(query, values=None):
    # Create connection to the database
    conn = create_connection()
    
    try:
        # If the connection is successful
        if conn.is_connected():
            print("Connected to the database.")
        
        cursor = conn.cursor()  # Create cursor object
        
        # Execute the query with values if provided
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        
        # Fetch all rows from the result
        rows = cursor.fetchall()
        
        # Check if there are any rows
        if rows:
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
            
            
def refresh_bill():
    refresh_bill_query = """
        INSERT IGNORE INTO bill_tbl (unit_id, name, rent, electricity, water, internet, month, year)
        SELECT 
            u.unit_id,
            u.name,
            3000 AS rent,
            e.electricity_total AS electricity,
            w.water_total AS water,  -- If no match, will be NULL
            300 AS internet,
            COALESCE(EXTRACT(MONTH FROM e.date), EXTRACT(MONTH FROM w.date)) AS month,
            COALESCE(EXTRACT(YEAR FROM e.date), EXTRACT(YEAR FROM w.date)) AS year
        FROM 
            unit_tbl u
        LEFT JOIN 
            electricity_tbl e ON u.unit_id = e.unit_id
        LEFT JOIN 
            water_tbl w ON u.unit_id = w.unit_id AND EXTRACT(MONTH FROM e.date) = EXTRACT(MONTH FROM w.date) AND EXTRACT(YEAR FROM e.date) = EXTRACT(YEAR FROM w.date)
        WHERE 
            e.unit_id IS NOT NULL  -- Ensure unit_id exists in electricity_tbl
            AND w.unit_id IS NOT NULL  -- Ensure unit_id exists in water_tbl
            AND NOT EXISTS (
                SELECT 1
                FROM bill_tbl b
                WHERE b.unit_id = u.unit_id
                AND b.month = EXTRACT(MONTH FROM e.date)
                AND b.year = EXTRACT(YEAR FROM e.date)
            )
        UNION
        SELECT 
            u.unit_id,
            u.name,
            3000 AS rent,
            e.electricity_total AS electricity,
            w.water_total AS water,  -- If no match, will be NULL
            300 AS internet,
            COALESCE(EXTRACT(MONTH FROM e.date), EXTRACT(MONTH FROM w.date)) AS month,
            COALESCE(EXTRACT(YEAR FROM e.date), EXTRACT(YEAR FROM w.date)) AS year
        FROM 
            unit_tbl u
        RIGHT JOIN 
            electricity_tbl e ON u.unit_id = e.unit_id
        RIGHT JOIN 
            water_tbl w ON u.unit_id = w.unit_id AND EXTRACT(MONTH FROM e.date) = EXTRACT(MONTH FROM w.date) AND EXTRACT(YEAR FROM e.date) = EXTRACT(YEAR FROM w.date)
        WHERE 
            e.unit_id IS NOT NULL  -- Ensure unit_id exists in electricity_tbl
            AND w.unit_id IS NOT NULL  -- Ensure unit_id exists in water_tbl
            AND NOT EXISTS (
                SELECT 1
                FROM bill_tbl b
                WHERE b.unit_id = u.unit_id
                AND b.month = EXTRACT(MONTH FROM e.date)
                AND b.year = EXTRACT(YEAR FROM e.date)
            );
        """
    mysql_query(refresh_bill_query)
    delete_blank_query = """DELETE FROM bill_tbl WHERE name = '';"""
    mysql_query(delete_blank_query)
