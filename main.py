import classes
import random






def generate_account_number():
    return random.randint(10**11, (10**12)-1)

random_number = generate_random_12_digit_number()
print(random_number)

	