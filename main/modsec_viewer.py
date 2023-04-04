import sqlite3
from tkinter import *

# Connect to the database
conn = sqlite3.connect('modsec.db')
c = conn.cursor()

# Create a function to query the database and display the results
def view_records():
    # Clear any existing data from the listbox
    record_listbox.delete(0, END)

    # Query the database and fetch all the records
    c.execute("SELECT * FROM modsec_logs")
    records = c.fetchall()

    # Insert each record into the listbox
    for record in records:
        record_listbox.insert(END, record)

# Create the main window
root = Tk()
root.title("ModSecurity Logs Viewer")

# Create a frame for the record listbox
record_frame = Frame(root)
record_frame.pack(padx=10, pady=10)

# Create the record listbox
record_listbox = Listbox(record_frame, width=80, height=20)
record_listbox.pack(side=LEFT, fill=Y)

# Create a scrollbar for the record listbox
record_scrollbar = Scrollbar(record_frame)
record_scrollbar.pack(side=RIGHT, fill=Y)

# Link the scrollbar to the record listbox
record_listbox.config(yscrollcommand=record_scrollbar.set)
record_scrollbar.config(command=record_listbox.yview)

# Create a button to refresh the record listbox
refresh_button = Button(root, text="Refresh", command=view_records)
refresh_button.pack(padx=10, pady=10)

# Populate the record listbox initially
view_records()

# Start the main event loop
root.mainloop()

# Close the database connection
conn.close()



