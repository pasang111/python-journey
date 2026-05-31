secret_number = 6
guess = 0

while guess != secret_number:
    guess = int(input("Please guess the secret number: "))
    if guess != secret_number:
        print("It is not the secret number")
    else:
        print("Correct it is the secret number")