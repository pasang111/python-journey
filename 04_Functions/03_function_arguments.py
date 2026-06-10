# Default arguments are used when no value is provided.

def welcome(name="Ace"):
    print("Welcome", name)

# In welcome(), no argument is passed, so Python uses the default value "Ace".
welcome()

# The default value is replaced by "John" because "John" is passed as an argument.
welcome("John")


# Return values

# print() displays output on the screen.
# return sends a value back to the caller.

# Example:
def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# The returned value is stored in the variable result.
# This allows us to reuse it later in the program.

# To call the function again, pass the required arguments to the function.

print(add(20, 30))
print(add(19, 40))

# Python calculates the result, and print() displays it.


# Multiple return values

def get_user():
    return "Ace", 20

name, age = get_user()

print(name)
print(age)

# The function returns two values.
# name receives "Ace".
# age receives 20.


# Another example of multiple return values

def calculate(a, b):
    return a + b, a * b

sum_result, multiply_result = calculate(5, 10)

print(sum_result)
print(multiply_result)

# The first value is stored in sum_result.
# The second value is stored in multiply_result.