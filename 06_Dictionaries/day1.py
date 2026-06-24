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