def encode_message(message, shift, alphabet):
    """Encode the message using Caesar cipher."""
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    encoded = []

    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            encoded.append(shifted_alphabet[position])
        else:
            encoded.append(letter)

    return "".join(encoded)


def decode_message(message, shift, alphabet):
    """Decode the message using Caesar cipher."""
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    decoded = []

    for letter in message:
        if letter in shifted_alphabet:
            position = shifted_alphabet.index(letter)
            decoded.append(alphabet[position])
        else:
            decoded.append(letter)

    return "".join(decoded)


def get_user_input():
    """Get input from user for the Caesar cipher."""
    user_choice = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt, or 'exit' to quit: ").lower()
    if user_choice == "exit":
        return "exit", "", 0
    message = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    return user_choice, message, shift


def continue_prompt():
    """Ask the user if they want to continue."""
    choice = input("Do you want to continue? (yes/no): ").lower()
    return choice == "yes"


def main():
    while True:
        from art import logo
        print(logo)
        user_choice, message, shift = get_user_input()

        if user_choice == "exit":
            print("Goodbye!")
            break
        elif user_choice == 'encode':
            result = encode_message(message, shift, alphabet_list)
            print(f"Encoded Message: {result}")
        elif user_choice == 'decode':
            result = decode_message(message, shift, alphabet_list)
            print(f"Decoded Message: {result}")
        else:
            print("Choix invalide!")

        # Ask user if they want to continue
        if not continue_prompt():
            print("Goodbye!")
            break


alphabet_list = list('abcdefghijklmnopqrstuvwxyz')
main()
