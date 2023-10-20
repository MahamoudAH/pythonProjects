print("Welcome to the PyPassword Generator")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

symbols = ["~", "!", "@", "#", "$", "%", "^", "&", "*",
           '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', ':', ';', '<', '>', '.', '?', '/']

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


user_capital_l = get_input(
    "How many capital letters would you like in your password: ")
user_lowercase_l = get_input(
    "How many lowercase letters would you like in your password: ")

user_s = get_input("How many symbols would you like: ")
user_n = get_input("How many numbers would you like: ")

password = user_capital_l + user_lowercase_l + user_s + user_n

print(f"Here is your password: {password}")
