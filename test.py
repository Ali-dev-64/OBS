def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Test the function
age = get_integer_input("Please enter your age: ")
print("Your age is:", age)
