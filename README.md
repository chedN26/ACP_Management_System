 **FINAL PROJECT DOCUMENTATION**

## **DueDeet: Tenant Management and Billing Solution**

CS211: OBJECT-ORIENTED PROGRAMMING

Submitted By:

GARCIA, CHED NEO H. 

IT – 2106

## 1. **PROJECT OVERVIEW**

The Tenant Management and Utility Billing Solution exists to address the challenges faced in managing rental properties, particularly in maintaining accurate and timely billing for tenants. It was created in response to personal frustrations with inconsistencies in monthly billings—such as delays and inaccurate meter readings—that impacted the rental experience. The system centralizes the management of essential tenant information, including rent and utility bills (e.g., water, electricity, and internet), ensuring that billing is accurate and timely. By providing a platform that tracks utility readings and automates the billing process, the system eliminates the potential for errors and ensures a smooth experience for both tenants and apartment managers.

The primary goal of the system is to eliminate billing inefficiencies, offer transparency in charges, and improve tenant satisfaction by providing a reliable and consistent method for billing. It supports the university's mission by promoting innovation in problem-solving and offering an example of a technological solution that addresses real-world challenges. The system reflects the university's commitment to producing leaders who can apply creative solutions to problems, and contributing to sustainable development by enhancing the rental management process in a modern, efficient manner.

-----

The Tenant Management and Utility Billing Solution is a system designed specifically to assist apartment managers in automating and tracking tenants’ monthly utility bills and rent. It offers a set of core features and functionalities, while also having clearly defined boundaries to manage expectations.

**Included Features:**

- ***Manual Input for Electricity and Water Meter:*** Allows apartment managers to manually input meter readings for electricity and water.
- ***Automatic Calculation of Electricity and Water Bill:*** The system calculates the electricity and water bills based on the provided meter readings, ensuring accuracy in billing.
- ***User-Friendly GUI:*** A graphical user interface designed for ease of use, allowing apartment managers to input and display tenant records efficiently.
- ***Secure Application:*** The system is password-protected to ensure only authorized apartment managers have access to the tenant information and billing details.

**Excluded Features:**

- ***Invoicing and Printing:*** The system does not handle the generation of invoices or print tenant bills. It only tracks and records the current and previous bills.
- ***Automated Payment Processing:*** The system does not handle payment collection or processing for the utilities and rent. It focuses solely on record-keeping and calculation.
- ***Scope of Use:*** The system is meant to be a supportive tool for apartment managers, rather than a full-fledged accounting or payment management platform. Its main purpose is to automate the calculation and tracking of bills, not to manage financial transactions.

**Target Users:**

The target users of the system are apartment managers. They are the primary audience, as they will be responsible for inputting tenant records, meter readings, and managing the billing process. The system is designed to make their job more efficient by automating the calculation of utility bills and tracking rent payments, thus reducing administrative workload and potential for errors.

-----

The Tenant Management and Utility Billing Solution project aims to achieve several specific, measurable outcomes using the SMART criteria. These outcomes are designed to ensure the system meets its goals efficiently and effectively.

**Specific:**

- The system will automate the calculation of rent and utility bills (electricity and water) for each tenant, ensuring that all charges are tracked accurately.
- The system will offer a simple and intuitive graphical user interface (GUI) for apartment managers to input and view tenant records, making the process more efficient.
- The system will track previous and current utility readings, calculating bills based on meter information to eliminate errors in tenant billing.

**Measurable:**

- The system aims to reduce billing errors by 90% within the first 4 months of use.
- The time spent by apartment managers on entering and calculating utility bills will be reduced by at least 50% after the system is implemented.

**Achievable:**

- This application will come with comprehensive and easy-to-understand documentation and instructions to ensure that users can effectively use the system. The system's user-friendly design and intuitive GUI will support the ease of adoption and efficient usage.

**Relevant:**

- The project directly addresses the problem of inconsistent and inaccurate billing, a core issue faced by apartment managers. By automating the calculation and tracking of bills, it aligns with the goal of improving operational efficiency.
- The project aligns with the university's mission of producing leaders through innovation, as it uses technology to solve real-world problems in property management.

**Time-bound:**

- A review of system performance, including billing accuracy and time saved on tasks, will be handled after implementation to measure success against the initial goals.

The project aims to automate tenant billing, reduce manual errors by 90%, and save 50% of billing-related time within 4 months of implementation, with the goal of improving overall efficiency for apartment managers. 

<br>

## 2. **PYTHON CONCEPTS AND LIBRARIES**

   **Python Tkinter**

   Tkinter is the standard Python library for creating graphical user interfaces (GUIs). It provides a set of tools to build windows, dialogs, buttons, text fields, labels, and other interactive elements in desktop applications. Tkinter is built on the Tk GUI toolkit, which is widely used for creating cross-platform applications.

   **Python CustomTkinter**

   CustomTkinter is an enhanced version of the standard Tkinter library, designed to provide a more modern and customizable look for GUI applications in Python. It offers a set of themed widgets that allow for greater control over the appearance of elements like buttons, labels, sliders, and entry fields, making them more visually appealing and user-friendly. CustomTkinter simplifies the process of creating modern, attractive interfaces while still utilizing Tkinter's functionality, and it supports features such as custom colors, rounded corners, and a dark mode.

   **MySQL**

   The import statement “*import mysql.connector*” brings in the mysql.connector module, which is a Python library that allows the program to connect to and interact with MySQL databases. It provides functions for establishing a connection, executing SQL queries, and handling results within a MySQL database. While “*from mysql.connector import Error*” imports the Error class from the mysql.connector module, which is used to handle exceptions related to MySQL operations. It is used to catch and manage database connection issues, query errors, or other exceptions that may occur when interacting with a MySQL database in your Python program.

   **MathPlotLib**

   Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

   The “*import import matplotlib.pyplot as plt*” brings in the Matplotlib library's plotting interface, commonly abbreviated as plt. This is the standard way to create static, interactive, and animated visualizations in Python. With plt, a wide range of plots, such as line charts and bar graphs, to visualize data can be generated. These plots can then be embedded in various graphical environments, such as Tkinter, using FigureCanvasTkAgg.

   The “*import from matplotlib.backends.backend\_tkagg import FigureCanvasTkAgg*” is used to integrate Matplotlib plots into Tkinter applications. FigureCanvasTkAgg acts as a bridge, allowing Matplotlib figures to be embedded and displayed within a Tkinter GUI window. This makes it possible to create interactive data visualizations within a desktop application.

   **Python Imaging Library (PIL or Pillow)**

   The “*import from PIL import Image*” brings in the Image module from the Pillow library (a fork of the Python Imaging Library, or PIL). The Image module provides powerful tools for opening, manipulating, and saving many different image file formats, such as JPEG, PNG, and GIF. It allows the program to perform various image processing tasks, including resizing, cropping, rotating, applying filters, and converting between formats, making it essential for working with images in Python applications.

   **Python Sys Module**

   The import “*import sys”* brings in the sys module, which provides access to system-specific parameters and functions. It allows Python programs to interact with the underlying operating system. The sys module is often used for error handling, script termination (sys.exit()), and modifying the behavior of the Python interpreter.

   **Python datetime module**

   The “*import from datetime import datetime”* brings in the datetime class from Python's datetime module. This class provides a way to work with dates and times in a variety of formats. It allows the program to create, manipulate, and format date and time objects, as well as perform operations like getting the current date and time, comparing dates, and formatting them for display. The datetime class is essential for handling time-related data in Python applications.

<br>

## 3. **SUSTAINABLE DEVELOPMENT GOALS**

The Tenant Management and Utility Billing Solution aligns with both SDG 9: Industry, Innovation, and Infrastructure and SDG 11: Sustainable Cities and Communities.

- **SDG 9: Industry, Innovation, and Infrastructure**: This goal emphasizes the need for innovation and the development of resilient infrastructure. The Tenant Management and Utility Billing Solution addresses these by introducing technological innovation to improve the efficiency of property management. It automates billing calculation, ensuring accuracy and reducing human error. By improving the infrastructure for rental management through automation and centralized data management, the system supports the creation of a more efficient, modern, and sustainable approach to managing residential properties. It helps create a robust, innovative system that reduces operational inefficiencies, aligning with the goal of fostering innovation in industry.
- **SDG 11: Sustainable Cities and Communities**: SDG 11 focuses on making cities and human settlements inclusive, safe, resilient, and sustainable. This project contributes to this goal by improving the management of urban housing, enhancing tenant satisfaction, and reducing inefficiencies in the billing process. By automating and streamlining utility billing, the system ensures fairness, transparency, and accountability in urban property management. Additionally, it supports the sustainable use of resources (like electricity and water) by promoting accurate billing, encouraging responsible consumption, and ensuring that tenants and apartment managers have clear insights into their utility usage, which contributes to more sustainable living practices within communities.

<br>

## 4. **PROGRAM/SYSTEM INSTRUCTIONS**

**How to run the program:**

1. Download the zip file (<https://github.com/chedN26/ACP_Management_System.git>)
1. Extract the file, it should be named "*ACP\_Management\_System-main*" folder
1. Open XAMPP Control Panel and start Apache and MySQL
1. Open PHPMyAdmin (*http://localhost/phpmyadmin*)
1. Create a database with name “*acp\_management\_db*”
1. Import acp\_management\_db.sql file to your newly created database (*ACP\_Management\_System-main/database/acp\_management\_db.sql*)
1. Using any code editor (VS Code, PyCharm) run main.py

<br>

**How to use the program:**

1. When you have successfully opened the program, you will see the initial interface for logging in. Use the credentials below to login.
1. You will now see the GUI for the apartment unit selection. Just select any unit to see the unit’s detail.
1. Below the apartment is the details of the unit. You will now have the option to view the Overview Tab and Previous Tab.

   **Overview Tab**

    - Contains the billing information for the current month.
    - Shows statistics about the previous water and electricity bills.
    - Allows you to create new records. Note that when inputting new records, there should be unique month and date for each, as the system treats each record based on the month and date of the bill

    - After inputting all the details and submitting the information, the program will automatically calculate the bill based on the user input. It will reflect immediately on the charts and it will also be added to the Previous Bills Table on the Previous Tab.

   **Previous Tab**

    - Contains the previous records of the unit you selected.
    - Allows you to edit, update, and delete records.
      
1. After viewing a specific apartment unit details, you can select another unit by clicking “back” button on the upper left corner of the information frame and click another unit.
1. Logout button is located at the upper right corner of the apartment model.

<br>

\*\*LOGIN DETAILS\*\*

user: admin

password: 1234

