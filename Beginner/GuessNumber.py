import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    guess_the_number()
