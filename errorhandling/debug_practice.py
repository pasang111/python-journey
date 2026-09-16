# Modern way of using a debugging breakpoint: breakpoint()
# Example:

def calculate_total(price, quantity):
    discount= 10
    total = price * quantity
    final_price = total - discount

    breakpoint()

    return final_price

price = 100
quantity = 3

result = calculate_total(price,quantity)
print("Final price:", result)


# Traditional way of using a debugging breakpoint: pdb.set_trace()

import pdb

def calculate_total(price, quantity):
    discount= 10
    total = price * quantity
    final_price = total - discount

    pdb.set_trace()

    return final_price

price = 100
quantity = 3

result = calculate_total(price,quantity)
print("Final price:", result)