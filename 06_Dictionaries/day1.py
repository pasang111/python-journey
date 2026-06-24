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