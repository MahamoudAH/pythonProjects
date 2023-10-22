import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
guess = input("Guess a letter: ")

word = random.choice(word_list)
liste = []
for i in range(1, len(stages)):
    liste.append('_')

i = len(stages) - 1

liste = ' '.join(liste)
print(liste)

print(word)

while i >= 1:
    if guess in word:
        index = word.index(guess)
        print(liste)
        print(stages[i])
        guess = input("Guess a letter: ")
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(liste)
        print(stages[i])
        guess = input("Guess a letter: ")

    i -= 1
    print(i)
