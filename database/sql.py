import sqlite3

# Connect to the SQLite database
con = sqlite3.connect("accounts_data.db")
cursor = con.cursor()

# Create the Accounts table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Accounts (
                account_number INTEGER PRIMARY KEY,
                account_name TEXT,
                account_pin INTEGER,
                user_email TEXT,
                user_phone_number INTEGER,
                country TEXT,
                account_issue_date TEXT,
                account_expiry_date TEXT
                )''')

# Commit the changes
con.commit()
