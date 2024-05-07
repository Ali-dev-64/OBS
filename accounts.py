import sqlite3

class Account():
	def __init__(self,account_name,account_number,account_pin,user_email,user_phone_number,country, account_issue_date , account_expiry_date):
		
		self.con = sqlite3.connect("database/accounts_data.db")
		self.cursor = self.con.cursor()
		self.account_name=account_name
		self.account_number=account_number
		self.account_pin=account_pin
		self.user_email=user_email
		self.user_phone_number=user_phone_number
		self.country=country
		self.account_issue_date=account_issue_date
		self.account_expiry_date=account_expiry_date
		
	def Add_To_database(self):
		self.cursor.execute(f'''INSERT INTO Accounts (
                account_number,  
                account_name,
                account_pin,
                user_email,
                user_phone_number,
                country,
                account_issue_date,
                account_expiry_date) 
                VALUES (
                {self.account_number},
                '{self.account_name}',
                {self.account_pin},
                '{self.user_email}',
                {self.user_phone_number},
                '{self.country}',
                {self.account_issue_date},
                {self.account_expiry_date}
                )''')

				


	def show_info(self):
		account_number=input("Enter Your Account number: \n")
		account_pin=input("Enter Pin: \n")
		