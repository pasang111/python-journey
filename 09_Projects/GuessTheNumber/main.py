import random

def play_game():
    print("\nGuess the Secret Number!")

    difficulty = input(
        "Choose difficulty (easy/medium/hard): "
    ).lower()

    if difficulty == "easy":
        max_number = 10
        attempts = 5
    elif difficulty == "medium":
        max_number = 50
        attempts = 7
    elif difficulty == "hard":
        max_number = 100
        attempts = 8
    else:
        print("Invalid choice. Using medium difficulty.")
        max_number = 50
        attempts = 7

    secret_number = random.randint(1, max_number)

    print(f"\nGuess a number between 1 and {max_number}.")
    print(f"You have {attempts} attempts.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"\nAttempt {attempt}/{attempts}: "))

            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}.")
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {attempt} attempts.")
                return True

            remaining = attempts - attempt

            if remaining > 0:
                print(f"You have {remaining} attempt(s) left.")

        except ValueError:
            print("Please enter a valid number.")

    print(f"\nGame over! The secret number was {secret_number}.")
    return False


while True:
    play_game()

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break
