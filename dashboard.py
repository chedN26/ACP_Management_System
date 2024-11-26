import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt # Package for using GUI charts 
from data import (sales_data, inventory_data, inventory_month_data, product_data, sales_year_data) # Dummy data for charts

# Color palette of the charts
plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#ADD8E6", "#87CEEB", "#4169E1", "#1E90FF", "#000080"])

# Chart 1: Bar chart of sales data
fig1, ax1 = plt.subplots() # Create a figure for the whole chart (container) and its components (bars)
ax1.bar(sales_data.keys(), sales_data.values()) # Specify the type of chart and its contents/values
ax1.set_title("Sales by Product") # Set the title of the chart
ax1.set_xlabel("Sales") # Set the label for the X axis
ax1.set_ylabel("Product") # Set the label for the Y axis
#plt.show() # Show the chart

# Chart 2: Horizontal bar chart of inventory data
fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), inventory_data.values()) # Horizontal bar chart takes list data type for the first argument
ax2.set_title("Product Inventory") # Set the title of the chart
ax2.set_xlabel("Inventory") # Set the label for the X axis
ax2.set_ylabel("Product") # Set the label for the Y axis
#plt.show() # Show the chart

# Chart 3: Pie chart for product data
fig3, ax3 = plt.subplots()
ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%') # Auto persentage (autopct) shows the percentage of each values
ax3.set_title("Product \nBreakdown")
#plt.show()

# Chart 4: Line chart of sales by year
fig4, ax4 = plt.subplots()
ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
ax4.set_title("Sales by Year") # Set the title of the chart
ax4.set_xlabel("Year") # Set the label for the X axis
ax4.set_ylabel("Sales") # Set the label for the Y axis
#plt.show() # Show the chart

# Chart 5: Area chart of inventory by month
fig5, ax5 = plt.subplots()
ax5.fill_between(inventory_month_data.keys(), inventory_month_data.values())
ax5.set_title("Inventory by Month") # Set the title of the chart
ax5.set_xlabel("Month") # Set the label for the X axis
ax5.set_ylabel("Inventory") # Set the label for the Y axis
#plt.show() # Show the chart


# Create a window and add charts
root = tk.Tk() # Initialize the window
root.title("Dashboard") # Set the name of window
root.state('zoomed') # Set to full screen upon opening the window

side_frame = tk.Frame(root, bg="#87CEEB")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text="Dashboard", bg="#87CEEB", fg="#FFF", font=25)
label.pack(pady=50, padx=20)

charts_frame = tk.Frame(root)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame) # Create a frame inside the window
upper_frame.pack(fill="both", expand=True)  # Layout manager; fill both - fill the X and Y axis of the window; expand - makes the frame expand

canvas1 = FigureCanvasTkAgg(fig1, upper_frame) # Adding fig1 chart to the parent frame - upper_frame
canvas1.draw() # Show the canvas inside the frame similar to plt.show()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True) # Sets the position ang properties of fig1

canvas2 = FigureCanvasTkAgg(fig2, upper_frame) 
canvas2.draw() 
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True) 

canvas3 = FigureCanvasTkAgg(fig3, upper_frame) 
canvas3.draw() 
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True) 

lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig4, lower_frame) 
canvas4.draw() 
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True) 

canvas5 = FigureCanvasTkAgg(fig5, lower_frame) 
canvas5.draw() 
canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

root.mainloop()
