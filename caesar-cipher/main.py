alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']

user_choice = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
message = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

new = alphabet[shift:]
av = alphabet[0:shift]

alphabet_deca = new + av


new_message = []

if user_choice == 'encode':
    for letter in message:
        if letter in alphabet:
            new_message.append(alphabet_deca[alphabet.index(letter)])
        else:
            new_message.append(letter)
elif user_choice == 'decrypt':
    for letter in message:
        if letter in alphabet_deca:
            new_message.append(alphabet[alphabet_deca.index(letter)])
        else:
            new_message.append(letter)

result = "".join(new_message)
print(result)
