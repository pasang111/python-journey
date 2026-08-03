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

# to add value in set we use .add
#for example

my_set2 = {1,2,34,5,6,7,7,}
my_set2.add(9) #adds the new value 

# We are also checking if my_set is a superset of your_set. This is also False because my_set does not have all the elements of your_set:
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False

print(my_set2) #never forget to print to see the actual output

#now we learned how to add now for removing just replace .add with .remove
my_set2.remove(1) #remove 1 from the set
print(my_set2)

#now for discard
my_set2.discard(34)
print(my_set2)

#NOTE : SO whats the difference between .remove and .discard in the above example
#.remove will show KeyError if the element is not found
#but
#.discard will not show any KeyError if the element is not found

#for example
my_set2.remove(56)#value which is not in the element
print(my_set2)

my_set2.discard(90)#also not in the elements
print(my_set2)

#.clear helps to remove all the elements from the set
my_set2.clear()
print(my_set2) 

