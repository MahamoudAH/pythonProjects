from hangman_art import logo, stages
from hangman_words import word_list


def play_hangman():
    import random

    print(logo)

    word = random.choice(word_list)
    display = ["_" for _ in word]
    guessed_letters = []

    lives = len(stages) - 1

    print(' '.join(display))
    # print(word)

    while lives > 0 and "_" in display:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You've already guessed {guess}")
            continue
        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    display[index] = guess
        else:
            print(
                f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1

        print(' '.join(display))
        print(stages[lives])

    if "_" not in display:
        print("You win!")
    else:
        print("You lose.")


play_hangman()
