# Function Arguments

# what are function arguments?
# function arguments are the values we pass into a function when calling it

# parameter = parameter are the variable inside the function
# argument = argument are the actual value passed while calling the function


# positional arguments

def greet(name):
    print("Hello", name)

# here "Ace" is the argument
greet("Ace")

# here "John" is another argument
greet("John")

# Python matches the value based on position
# name = "Ace"
# name = "John"

# so when we write greet("Ace")
# Python takes the value "Ace" and stores it in the parameter called name
# then print() displays Hello Ace


# multiple arguments

def student(name, age):
    print(name, age)

student("Ace", 20)
student("Snow", 21)

# first value goes into name and second value goes into age
# for student("Ace", 20)
# name = "Ace"
# age = 20

# for student("Snow", 21)
# name = "Snow"
# age = 21

# Python always matches the values from left to right
# first argument goes to first parameter
# second argument goes to second parameter

# if we pass too few or too many arguments
# Python will show an error because the number of values does not match the parameters