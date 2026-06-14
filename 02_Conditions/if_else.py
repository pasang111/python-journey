# Day 1: Learning If, Elif and Else Statements

# if statement

age = 20

if age >= 18:
    print("You are eligible to vote.")

# if else statement

temperature = 15

if temperature > 20:
    print("The weather is warm.")
else:
    print("The weather is cold.")

# if elif else statement

marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Grade F")

# Another example

hour = 14

if hour < 12:
    print("Good Morning")
elif hour < 18:
    print("Good Afternoon")
else:
    print("Good Evening")

# Checking a username

username = "Ace"

if username == "Admin":
    print("Welcome Admin")
elif username == "Ace":
    print("Welcome Ace")
else:
    print("Unknown User")

# more example for if else
# checking weather a number is positive negative or zero

number = -5

if number > 0:
    print("Positive number")
elif number <0 :
    print("Negative number")
else:
    print("Zero")

# checking whether a number is positive, negative or zero
# the program keeps asking for input until the user enters 999 to quit

while True:
    number = int(input("Enter the number to check if the number is positive negative or zero (999 to quit): "))

    if number == 999:
        print("Program ended")
        break

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")

# Checking even or odd number

num = 8

# % gives the remainder.
if num % 2 == 0:  
    print("Even Number")
else:
    print("Odd Number")

# If remainder is 0 the number is even.
# Otherwise it is odd.

#simple password checking method using if else

password = "Ace123"

if password == "Ace123":
    print("User logged in successfully")
else:
    print("Password incorrect")

#asking user input to enter the password

passcode = "Myaceacademy"

while True:
    user_one = input("Please enter your password to log-in: ")

    if user_one == "Myaceacademy":
        print("Logged in successfully")
        break
    else:
        print("Incorrect password") 