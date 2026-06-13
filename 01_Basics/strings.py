# now we are in day one and we will learn about strings
# how do we declare them?
# in python we can use both single and double quotes

p = "ace snow"
q = 'ace snow'
print(p, q)  # quotes do not matter for normal strings

# now if we want to write strings in different lines we use triple quotes

e = """
sodfnsdf
sdfsdf
sdfsd
fs
dfsd
"""
print(e)

# checking if a string contains a character or word using the 'in' operator

f = 'Hello world'
print('hello' in f)   # False
print('Hello' in f)   # True
print('f' in f)       # False
print('rld' in f)     # True
print('d' in f)       # True
print('Hell' in f)    # True
print('w' in f)       # True

# the 'in' operator checks whether a word or character exists in a string
# it is case-sensitive

text = "Python Programming"

print('Python' in text)   # True
print('python' in text)   # False
print('gram' in text)     # True
print('Pro' in text)      # True
print('z' in text)        # False

# another example

pa = "ace snow"
print('ace' in pa)        # True
print('Snow' in pa)       # False
print('anG' in pa)        # False
print('snow' in pa)       # True
print('acesnow' in pa)    # False (space missing)

# note: always use the variable name while checking
# example: print('ace' in pa)

# checking the length of a string

p = "ace snow is a good student in the class"
print(len(p))  # spaces are also counted

# indexing and slicing

d = "Sakalaka boom"
print(d[0:7:1])  # prints characters from index 0 to 6

qs = "Ace snow"
print('ace' in qs)    # False
print('snow' in qs)   # True
print('ow' in qs)     # True
print('Now' in qs)    # False

saad = "ace snow"
print(len(saad))
print(saad[1:4:2])

hap = "RUMPUM"
print(hap[1::3])

# string methods

name = "ace snow"

print(name.upper())
# converts all characters to uppercase

print(name.lower())
# converts all characters to lowercase

print(name.title())
# makes the first letter of each word uppercase

print(name.replace("ace", "hero"))
# replaces one word with another

print(name.startswith("ace"))
# checks if the string starts with "ace"

print(name.endswith("snow"))

# joining strings together

first_name = "Ace"
last_name = "Snow"

full_name = first_name + " " + last_name

print(full_name)

# + is used to combine strings together

# f-string example

name = "Ace"
age = 20

print(f"My name is {name} and I am {age} years old")

# f-strings allow us to insert variables directly into a string

# accessing a single character using index

name = "Pasang"

print(name[0])   # P
print(name[1])   # a
print(name[-1])  # g (last character)

# negative indexing starts from the end of the string

# removing extra spaces

text = "   hello world   "

print(text.strip())

# strip() removes spaces from the beginning and end

# checking if all characters are letters

word = "Python"

print(word.isalpha())  # True

# checking if all characters are numbers

num = "12345"

print(num.isdigit())   # True