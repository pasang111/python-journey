# NOTE : While Loop

# Difference between for loop and while loop:
# A for loop runs through a collection like a list or string.
# A while loop keeps running as long as the condition remains True.

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-5): "))

    if guess != secret_number:
        print("Your guess is incorrect")

print("You have made the right guess")

# Another example

mystery_number = 92
guess = 0

while guess != mystery_number:
    guess = int(input("Please enter the mystery number to win the lucky draw: "))

    if guess != mystery_number:
        print("Sorry, please try next time")

print("Congratulations, you have won the lottery ticket")

# input() always takes user input as a string.

# Password checker project

password = "PasangLama"
guess = ""

while guess != password:
    guess = input("Can you guess the password please: ")

    if guess != password:
        print("Sorry, your password does not match the credentials")

print("Your password matches our database. You are logged in.")

# Guess the number project

number = 111
guess = 0

while guess != number:
    guess = int(input("Please guess the number: "))

    if guess != number:
        print("Sorry, you are out of the game")
    else:
        print("Correct answer. Hurray!")

# Another example

pasang_number = 123
guess = 0

while guess != pasang_number:
    guess = int(input("Please enter Pasang's number: "))

    if guess != pasang_number:
        print("Sorry, this is not the number Pasang chose")

print("Yes, the number is correct")