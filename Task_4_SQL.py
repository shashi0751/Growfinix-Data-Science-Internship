import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("travel.db")
cursor = conn.cursor()

# Create Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    UserID INTEGER PRIMARY KEY,
    Name TEXT,
    City TEXT
)
""")

# Create Bookings table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Bookings(
    BookingID INTEGER PRIMARY KEY,
    UserID INTEGER,
    Destination TEXT,
    Amount INTEGER
)
""")

# Insert sample data
cursor.execute("DELETE FROM Users")
cursor.execute("DELETE FROM Bookings")

users = [
    (1,"Aman","Delhi"),
    (2,"Priya","Mumbai"),
    (3,"Rahul","Jaipur"),
    (4,"Sneha","Pune")
]

bookings = [
    (101,1,"Goa",15000),
    (102,2,"Manali",18000),
    (103,3,"Kerala",22000),
    (104,4,"Jaipur",12000)
]

cursor.executemany("INSERT INTO Users VALUES(?,?,?)",users)
cursor.executemany("INSERT INTO Bookings VALUES(?,?,?,?)",bookings)

conn.commit()

# JOIN Query
query = """
SELECT Users.Name,
Users.City,
Bookings.Destination,
Bookings.Amount
FROM Users
INNER JOIN Bookings
ON Users.UserID = Bookings.UserID
"""

df = pd.read_sql_query(query,conn)

print("\nBooking Details\n")
print(df)

conn.close()