import random
import re
import accounts
import datetime

def  issue_and_expiry_date():
    account_issue_date = datetime.date.today()
    account_expiry_date = account_issue_date + datetime.timedelta(days=365 * 4)
    return account_issue_date , account_expiry_date



def User_email(email):
    # Regular expression to match email pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


def User_phone_number():
	while True:
		try:
			user_phone_number=int(input("Enter Your Phone Number : \n "))
			return user_phone_number
		except ValueError:
			print("Invalid input. Please enter an integer.")



def Create_account():
	account_name=input("Enter Your name: \n ")
	while True:	
		user_email=input("Enter Your Email: \n ")
		if not User_email(user_email):
			print("Invalid email address.")
		else:
			break
	user_phone_number=User_phone_number()
	country=input("Enter Your country: \n ")
	account_number=random.randint(10**11, (10**12)-1)
	account_pin =random.randint(1000, 9999)
	account_issue_date , account_expiry_date = issue_and_expiry_date()
	account= accounts.Account(account_name,account_number,account_pin,user_email,user_phone_number,country, account_issue_date , account_expiry_date)
	print(f"Welcome {account_name}! You have a new Bank account under the name of {account_name} other info is down \n Account Number: {account_number} \n Pin: {account_pin} \n Issue Date: {account_issue_date} \n Expiry Date: {account_expiry_date}")	
	account.Add_To_database()

