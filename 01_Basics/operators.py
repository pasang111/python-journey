# Day 1: Learning Operators in Python

# Operators are symbols that help us perform different operations on values.

# Arithmetic Operators

a = 20
b = 5

print(a + b)  # Adds two numbers
print(a - b)  # Subtracts one number from another
print(a * b)  # Multiplies two numbers
print(a / b)  # Divides two numbers
print(a % b)  # Gives the remainder after division
print(a ** b) # Raises a number to a power
print(a // b) # Returns only the whole number part after division


# Comparison Operators

age = 18

print(age == 18) # Checks if age is equal to 18
print(age != 18) # Checks if age is not equal to 18
print(age > 18)  # Checks if age is greater than 18
print(age < 18)  # Checks if age is less than 18
print(age >= 18) # Checks if age is greater than or equal to 18
print(age <= 18) # Checks if age is less than or equal to 18

# These operators always return True or False.


# Logical Operators

has_license = True
has_helmet = False

print(has_license and has_helmet)
# Both conditions must be True.

print(has_license or has_helmet)
# At least one condition must be True.

print(not has_license)
# Reverses the value. True becomes False and False becomes True.


# Assignment Operators

score = 50

score += 10
print(score) # Same as score = score + 10

score -= 5
print(score) # Same as score = score - 5

score *= 2
print(score) # Same as score = score * 2


# Membership Operators

text = "Python Programming"

print("Python" in text)
# Checks if the word Python exists in the string.

print("Java" in text)
# Java does not exist in the string so it returns False.

print("Java" not in text)
# Returns True because Java is not present in the string.

# Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
# True because both variables point to the same object in memory.

print(a is c)
# False because they are different objects even though the values are the same.

print(a is not c)
# True because a and c are not the same object.


# More Assignment Operators

marks = 20

marks /= 2
print(marks)  # Same as marks = marks / 2

marks %= 3
print(marks)  # Same as marks = marks % 3