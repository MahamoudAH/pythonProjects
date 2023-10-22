import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
guess = input("Guess a letter: ")

word = random.choice(word_list)
i = len(stages)

while i >= 1:
    if guess in word:
        guess = input("Guess a letter: ")
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    i -= 1
    print(i)

# print(word)
