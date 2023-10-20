import random
import string


def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


def generate_password(num_upper, num_lower, num_symbols, num_digits):
    password_characters = (
        [random.choice(string.ascii_uppercase) for _ in range(num_upper)] +
        [random.choice(string.ascii_lowercase) for _ in range(num_lower)] +
        [random.choice(string.punctuation) for _ in range(num_symbols)] +
        [random.choice(string.digits) for _ in range(num_digits)]
    )

    random.shuffle(password_characters)
    return ''.join(password_characters)


if __name__ == '__main__':
    num_upper = get_input(
        "How many capital letters would you like in your password: ")
    num_lower = get_input(
        "How many lowercase letters would you like in your password: ")
    num_symbols = get_input(
        "How many symbols would you like in your password: ")
    num_digits = get_input("How many digits would you like in your password: ")

    password = generate_password(num_upper, num_lower, num_symbols, num_digits)
    print(f"Generated Password: {password}")
