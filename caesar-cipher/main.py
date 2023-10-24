alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']

message = input("Type your message: ")
shift = int(input("Type the shift number: "))

new = alphabet[shift:]
av = alphabet[0:shift]

alphabet_deca = new + av

new_message = []
for letter in message:
    idx = alphabet.index(letter)
    new_message.append(alphabet_deca[idx])

result = "".join(new_message)
print(new_message)
print(result)
