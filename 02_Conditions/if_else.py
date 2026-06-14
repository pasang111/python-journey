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