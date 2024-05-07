import sqlite3

conn = sqlite3.connect('accounts_data.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Accounts (
                account_number INTEGER PRIMARY KEY,  
                account_name TEXT ,
                account_pin INTEGER,
                user_email TEXT ,
                user_phone_number INTEGER ,
                country TEXT ,
                account_issue_date INTEGER ,
                account_expiry_date INTEGER 

            )''')