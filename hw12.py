import sqlite3
# Open the books database
conn = sqlite3.connect('books.db')
# Create a cursor
cursor = conn.cursor()
# Execute a query to select all data from the titles table
cursor.execute("SELECT * FROM titles")
# Get the metadata from the description attribute
description = cursor.description
# Get the data from the fetchall method
data = cursor.fetchall()
# Print the results in a tabular format
for row in data:
    print("%-20s%-20s%-20s" % (row[0], row[1], row[2]))