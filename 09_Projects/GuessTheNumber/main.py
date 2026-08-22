SECRET_NUMBER = 6
guess = None

print("Guess the Secret Number!")
print("Try to guess a number between 1 and 10.")

while guess != SECRET_NUMBER:
    try:
        guess = int(input("Enter your guess: "))

        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
        elif guess < SECRET_NUMBER:
            print("Too low! Try again.")
        elif guess > SECRET_NUMBER:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the secret number.")

    except ValueError:
        print("Please enter a valid number.")    
