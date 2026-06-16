# Simple multiplication table

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# prints the multiplication table of 5


# Finding total using a loop

numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total += number

print(total)

# total = 100

# We created the multiplication table for 5 above.
# The same logic can be reused for other numbers by changing the value of number.
# Here we are generating the multiplication table of 6.

number = 6

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# prints the multiplication table of 6