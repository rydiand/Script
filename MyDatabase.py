# MyDatabase
import sqlite3
conn = sqlite3.connect('Employees.db')
print("Opened Database")

cursor = conn.execute("SELECT ID, fname, lname, phone from Employee")
for row in cursor:
   print("ID = ", row[0])
   print("Name = ", row[1], row[2])
   print("Phone = ", row[3], "\n")

print("Operation done successfully")
conn.close()
