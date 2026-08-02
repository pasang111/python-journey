                                            # Set in Python
#set are one of the Python's built in data structure. One of the core characteristics of sets is that they don't store duplicate value.
#if we try to add a duplicate value in the set, only one of the value will be stored in it.

#sets are mutable and unordered, which mean that their elements are not stored in any specific order, so you cannot use indices or key to access them. They can only contain values of immutable data types like numbers, strings, and tuples. and they support mathematical set operations, including union, intersection, difference, and symmetric difference.

#To define a set, we need to write its elements with in curly braces {} and separate them with commas.

#For the example:

my_set = {1,2,3,4,5,}

#also if we ever need to define an empty set, we must use the set() function. but if we write empty curly braces {} python will automatically create an dictionary.


empty_set = set()   # Creates an empty set
empty_dict = {}     # Creates an empty dictionary

set() #set
{} #dictionary...

# Difference:
# A set stores only unique values.
# A dictionary stores key-value pairs, where each key maps to a corresponding value.