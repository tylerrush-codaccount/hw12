import sqlite3
# Open the books database
conn = sqlite3.connect('books.db')

cursor = conn.cursor()
cursor.execute("SELECT * FROM titles")
# Get description
description = cursor.description
# Fetchall
table = cursor.fetchall()
# Print the results
for line in table:
    print("%-20s%-20s%-20s" % (line[0], line[1], line[2]))