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

# The .isdisjoint() method checks if two sets are disjoint, which means they don't have any elements in common. 
# In this case, that's False because my_set and your_set do have common elements – 2, 3, and 4:

print(my_set.isdisjoint(your_set)) # False

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

# Python sets also have powerful methods that perform common mathematical set operations.

# The .issubset() and the .issuperset() methods check if a set is a subset or superset of another set, respectively.

# Here, we are checking if your_set is a subset of my_set, which is False because not all the elements of your_set are in my_set.

# We are also checking if my_set is a superset of your_set. This is also False because my_set does not have all the elements of your_set:
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False

# The .isdisjoint() method checks if two sets are disjoint,
# which means they don't have any elements in common. In this case, 
# that's False because my_set and your_set do have common elements – 2, 3, and 4:

print(my_set.isdisjoint(your_set)) # False

# The union operator | returns a new set with all the elements from both sets:

my_set | your_set # {1, 2, 3, 4, 5, 6}

# The intersection operator & returns a new set with only the elements that the sets have in common:
my_set & your_set # {2, 3, 4}

# he symmetric difference operator ^ returns a new set with the elements that are either in the first or the second set, but not both. 
# In this case, 1 and 5 are in my_set but not in your_set, so they are included. And the number 6 is in your_set but not in my_set, so it's included as well:

my_set ^ your_set # {1, 5, 6}

#q.a for set
# Which of the following is a core characteristic of Python sets?


# Elements are ordered and accessed by index.

# Elements are stored as key-value pairs.

# Elements are unique and unordered.
# Correct!


# # Elements can be of any data type, including lists and dictionaries.

# 2 What operator is used to check if an element is present in a set?


# ==

# in
# Correct!


# get()

# find()

# Which set operation returns a new set with the elements that are present in either one of the two sets, but not in both of them?

# Which set operation returns a new set with the elements that are present in either one of the two sets, but not in both of them?


# Union

# Intersection

# Difference

# Symmetric Difference
# Correct!

# .add() adds one element
my_set = {1, 2, 3}
my_set.add(4)

print(my_set)
# {1, 2, 3, 4}


# .update() adds multiple elements
my_set.update([5, 6, 7])

print(my_set)
# {1, 2, 3, 4, 5, 6, 7}

.add()      # adds one element
.update()   # adds multiple elements

my_set = {1, 2, 3, 4}

my_set.pop()

print(my_set)

my_set = {1, 2, 3, 4, 5}

print(len(my_set))
# 5

numbers = [1, 2, 2, 3, 3, 4, 4]

numbers = set(numbers)

print(numbers)
# {1, 2, 3, 4}
