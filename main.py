import accounts

End = False

def Run():
	global End
	account=accounts.Account()
	command = input("Enter a command: \n")
	if command == "a -new":
		account.create_account()
	if command == "-q" or command == "-e":
		End = True
	if command=="show":
		account.show_info()
while not End:
	Run()