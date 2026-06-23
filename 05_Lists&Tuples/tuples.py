# A tuple is similar to a list
# but tuples cannot be changed after creation.

student = ("Pasang", 20, "AI Engineer")

print(student)

# Accessing values

print(student[0])
print(student[1])
print(student[2])

# Length of tuple

print(len(student))

# Checking if a value exists

print("Pasang" in student)

# Looping through a tuple

for info in student:
    print(info)

# Tuple unpacking

name, age, profession = student

print(name)
print(age)
print(profession)

# Unlike lists, tuples cannot be modified.

# student[0] = "Ace"
# This would cause an error.