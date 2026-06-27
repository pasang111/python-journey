                                            # Starting with Dictionaries

# What is a Dictionary in Python?
# A dictionary is a built-in Python data structure that stores data
# in key-value pairs.

# Key-Value Pair:
# A key is used to identify and access a value.
# Keys must be unique within a dictionary.
# For example, if a key named "Hello" already exists,
# there cannot be another key with the same name "Hello".
# If a duplicate key is added, the new value will overwrite
# the old value.

# Example:

students = {
    "name" : "John",
    "age" : 51,
    "class" : 9
}
print(students) #now when we print the students it print all the value inside the students dictionaries
#what if we want to print just the age we do

print(students["age"]) #this print the valuer 51

#now for the class how to print it
#we do
print(students["class"])

# Always remember that dictionaries store data in key-value pairs.
# Keys should be unique within a dictionary.

# When creating a dictionary, keys are often written as strings,
# so we use quotes around them, such as "name" instead of name.

# In dictionaries, we use a colon (:) to separate a key from its value,
# not an equals sign (=).

# Example:
# "name": "John"
# key   : value

#Let's see one simple example again of dictionaries


#NOTE: while declaring dictonaries we use (=) sign for assigning the value inside the dictionaries
libraries = {
    "book1" : "Harry Potter", #NOTE: Use (:) also dont forget (,) after finishing declaring the value in it
    "book2" : "Elden's Ring",
    "book3" : "The Record Of Ragnarok",
    "book4" : "The early rise of the bird",
    "book5" : "The litle fighter 2",
    "book6" : "The record of the kings and the knights"
}

print(libraries)

#now lets say i want to see what's in the book 3 we do
# print(libraries("book3")) # haha did error here dont use () we use [] while calling the object from the dictionaries
print(libraries["book3"]) # so the thing is we only get the value of book 3 not let's say i want to print with book 3 : "The Record of Ragnarok "
# we do
print("book3: ", libraries["book3"]) # so simple lets say we want to do the same for book 5 what we do?
#same as above example
#let's say i want to print "The book name is...""
print("The book name is: ", libraries["book5"])

#So here's the thing there is difference in 
# Difference between student = {} and student = dict()

# 1) Using {}
# This is the most common and recommended way to create a dictionary.
# It directly creates an empty dictionary.

student = {}
print(student)  # Output: {}

# We can then add key-value pairs like this:
student["name"] = "John"
student["age"] = 20

print(student)  # Output: {'name': 'John', 'age': 20}


# 2) Using dict()
# This also creates an empty dictionary, but uses the dict() constructor.

student = dict()
print(student)  # Output: {}

# We can also add key-value pairs in the same way:
student["name"] = "John"
student["age"] = 20

print(student)  # Output: {'name': 'John', 'age': 20}


# Key idea:
# Both {} and dict() create an empty dictionary.
# {} is shorter and more commonly used.
# dict() is useful in special cases like converting other data structures.


#another alternative way to use dictionaries is
pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
print(products)
print(products["Laptop"])