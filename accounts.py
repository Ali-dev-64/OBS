import sqlite3
import random
import re
import accounts
import datetime
#,account_name,account_number,account_pin,user_email,user_phone_number,country, account_issue_date , account_expiry_date

class Account():
	def __init__(self):
		
		self.con = sqlite3.connect("database/accounts_data.db")
		self.cursor = self.con.cursor()
		
		#self.account_name=account_name
		#self.account_number=account_number
		#self.account_pin=account_pin
		#self.user_email=user_email
		#self.user_phone_number=user_phone_number
		#self.country=country
		#self.account_issue_date=account_issue_date
		#self.account_expiry_date=account_expiry_date
	
	
	def create_account(self):
		def issue_and_expiry_date():
			self.account_issue_date = datetime.date.today()
			self.account_expiry_date = self.account_issue_date + datetime.timedelta(days=365 * 4)
			return self.account_issue_date, self.account_expiry_date
	
		def user_email(email):
			# Regular expression to match email pattern
			pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
			
			# Check if the email matches the pattern
			if re.match(pattern, email):
				return True
			else:
				return False
	
		self.account_name = input("Enter Your name: \n ")
		while True:	
			self.user_email_input = input("Enter Your Email: \n ")
			if not user_email(self.user_email_input):
				print("Invalid email address.")
			else:
				self.user_email_address = self.user_email_input
				break
	
		while True:
			try:
				self.user_phone_number = int(input("Enter Your Phone Number : \n "))
				break
			except ValueError:
				print("Invalid input. Please enter an integer.")
	
		self.country = input("Enter Your country: \n ")
		self.account_number = random.randint(10**11, (10**12)-1)
		self.account_pin = random.randint(1000, 9999)
		self.account_issue_date, self.account_expiry_date = issue_and_expiry_date()
		self.account = self.Add_To_database()
		print(f"Welcome {self.account_name}! You have a new Bank account under the name of {self.account_name} other info is down \n Account Number: {self.account_number} \n Pin: {self.account_pin} \n Issue Date: {self.account_issue_date} \n Expiry Date: {self.account_expiry_date}") 

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
                '{self.user_email_address}',
                {self.user_phone_number},
                '{self.country}',
                {self.account_issue_date},
                {self.account_expiry_date}
                )''')
		self.con.commit()

				

	def show_info(self):
		a_number = input("Enter Your Account number: \n")
		a_pin = input("Enter Pin: \n")
		self.cursor.execute("SELECT * FROM Accounts")
		#self.cursor.execute("SELECT * FROM Accounts WHERE account_number = ? AND account_pin = ?", (a_number, a_pin))
		return self.cursor.fetchall()
		#if accounts:
		#	for account in accounts:
		#		print("Account Name:", account[1])
		#		print("Account Number:", account[0])
        #        # Print other details as needed
		#else:
		#	print("Account not found.")