#gi Building a Simple Bill Splitter

# We start with a bill total of 0.
running_total = 0

# Number of friends sharing the bill.
num_of_friends = 4

# Cost of each item ordered.
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Adding all food and drink costs to get the total bill.
running_total += appetizers + main_courses + desserts + drinks
print("Total bill so far:", running_total)

# Calculating a 25% tip.
tip = running_total * 0.25
print("Tip amount:", tip)

# Adding the tip to the bill.
running_total += tip
print("Total with tip:", running_total)

# Dividing the total bill equally among friends.
final_bill = running_total / num_of_friends
print("Bill per person:", final_bill)

# Rounding the result to 2 decimal places.
each_pays = round(final_bill, 2)
print("Each person pays:", each_pays)