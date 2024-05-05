import classes
import create_new_account
End = False

def Run():
    global End  
    command = input("Enter a command: \n")
    
    if command == "a -new":
        create_new_account.Create_account()
        
    if command == "-q" or command == "-e":
        End = True

while not End:
    Run()