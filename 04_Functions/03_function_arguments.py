# Function Arguments

# What are function arguments?
# Function arguments are the values we pass into a function when calling it.

# Parameter = variable inside the function definition
# Argument = actual value passed while calling the function


# Positional arguments

def greet(name):
    print("Hello", name)

# "Ace" is the argument passed to the parameter name
greet("Ace")

# "Snow" is another argument passed to the same parameter
greet("Snow")

# Python matches arguments based on position.
# The first value goes into the first parameter.
# The second value goes into the second parameter.


# Default arguments

# Default arguments are used when no value is provided.

def welcome(name="Ace"):
    print("Welcome", name)

# No argument is passed, so Python uses the default value "Ace"
welcome()

# The default value is replaced by "John"
# because "John" is passed as an argument
welcome("John")


# Return values

# print() displays output on the screen.
# return sends a value back to the caller.

def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# The returned value is stored in the variable result.
# We can print it, save it, or reuse it later in the program.

# Calling the function again with different arguments

print(add(20, 30))
print(add(19, 40))

# Python calculates the result and returns it.
# print() is used to display the returned value.


# Multiple return values

def get_user():
    return "Ace", 20

name, age = get_user()

print(name)
print(age)

# The function returns two values at the same time.
# name receives "Ace"
# age receives 20


# Another example of multiple return values

def calculate(a, b):
    return a + b, a * b

sum_result, multiply_result = calculate(5, 10)

print(sum_result)
print(multiply_result)

# The first returned value is stored in sum_result.
# The second returned value is stored in multiply_result.

# calculate(5, 10) returns:
# 5 + 10 = 15
# 5 * 10 = 50

# So:
# sum_result = 15
# multiply_result = 50