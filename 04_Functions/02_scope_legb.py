# What Is Scope in Python?

# Scope determines where a variable can be accessed in a program.

# Python follows the LEGB rule:
# L = Local
# E = Enclosing
# G = Global
# B = Built-in


# Local Scope

def greet():
    message = "Hello"

    # message can only be used inside this function
    print(message)

greet()

# print(message)
# this will cause an error because message only exists inside greet()


# Enclosing Scope

def outer():
    name = "Ram"

    def inner():
        # inner() can access variables from outer()
        print(name)

    inner()

outer()


def outer():
    name = "Noone"

    def inner():
        print(name)

    inner()

outer()

# the variable name belongs to outer()
# but inner() can still use it because of enclosing scope


# Global Scope

country = "Nepal"

def show():
    print(country)

show()

print(country)

# country is a global variable
# it can be used inside and outside functions


# Built-in Scope

pa = "Pasang"

print(len(pa))

# len() is a built-in Python function

lol = "this is all in lowercase turning it into upper case"
print(lol.upper())

asa = "THIS IS ALL IN CAPITAL FORM NOW TURNING IT INTO LOWERCASE"
print(asa.lower())

# len(), upper() and lower() are built-in functions/methods
# we can use them without creating them ourselves