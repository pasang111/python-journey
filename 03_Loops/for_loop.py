                                                    # LOOP NOTE : HOW DO LOOPS WORK IN PY
#loops are used to repeat a block of code for a set number of times. 

qq_q = ['qsd', 1, "asdasd", 'asdasd', 'asdasd']

for q in qq_q:
    print(q)

# q is the loop variable.
# It stores each item from the list one by one.

# Note:
# We print the loop variable (q), not the original list (qq_q).
# If we print qq_q inside the loop, the whole list will be printed every time.

for char in "code":
    print(char)

pop = [1, 2, 3, 43, 45, 5, 6, 6, 6, 5, 4]

for p in pop:
    print(p)

for sr in "asdasdasd":
    print(sr)

# Nested loops

qa = ["Pasang", "Ace"]
qsa = [
    "is great in python",
    "will be an AI engineer one day for sure",
    "will be a part of Guardware"
]

for w in qa:
    for s in qsa:
        print(w, s)

# Another nested loop example

aq = ["Pasang is 21 years old", "Pasang"]
qqa = [
    "and will join Guardware at the age of 22",
    "will be happy when he becomes part of Guardware"
]

for b in aq:
    for c in qqa:
        print(b, c)

# First the outer loop takes one value from aq.
# Then the inner loop runs completely for that value.
# After all inner loop values finish, the outer loop moves to the next value.

io = ["Pasang", 1, 12, 1243, 123]

for i in io:
    print(i)

# Break statement

# break is used to stop the loop when a condition is met.

developer_name = ["shyam", "ram", "hari"]

for developers in developer_name:
    if developers == "shyam":
        break
    print(developers)

# Continue statement

# continue skips the current iteration and moves to the next one.

my_name = ["Ace", "Snow", "Gaming"]

for name in my_name:
    if name == "Snow":
        continue
    print(name)

she = ["Alice", "panda", "Cheetah"]

for s in she:
    if s == "panda":
        continue
    print(s)

# Difference between break and continue:
# break stops the loop completely.
# continue skips only the current iteration.

words = ['sky', 'pasang', 'sunshine', 'carrot', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowel")

words = ['apple', 'sky', 'orange', 'fly', 'banana']

for word in words:
    if word[0].lower() in 'aeiou':
        print(f"'{word}' starts with a vowel")
    else:
        print(f"'{word}' starts with a consonant")

# If the first letter is a, e, i, o, or u,
# the word starts with a vowel.
# Otherwise it starts with a consonant.