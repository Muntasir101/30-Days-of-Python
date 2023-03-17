import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Prompt user to enter username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the entered credentials are valid
c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
if c.fetchone() is not None:
    print("Login successful!")
else:
    print("Invalid username or password.")

# Close the database connection
conn.close()
