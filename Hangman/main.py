import random
from hangman_art import logo, stages
from hangman_words import word_list


guess = input("Guess a letter: ")

word = random.choice(word_list)

if guess in word:
    print("Yes")
else:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")

print(word)
