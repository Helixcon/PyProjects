import random

def choose_random_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    return random.choice(words)

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_random_word()
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    while attempts < max_attempts:
        display_word = "".join(letter if letter in guessed_letters else "_" for letter in secret_word)
        print("Current word:", display_word)

        if display_word == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            attempts += 1
            print(f"Incorrect guess! You have {max_attempts - attempts} attempts left.")

    else:
        print("Game over. The word was:", secret_word)


if __name__ == "__main__":
    hangman()
