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
# from pdb import set_trace as s optional
def calculate_total(price, quantity):
    discount= 10
    total = price * quantity
    final_price = total - discount

    pdb.set_trace()
    # s() do this when u use line 23

    return final_price

price = 100
quantity = 3

result = calculate_total(price,quantity)
print("Final price:", result)

#using ipdb 
#way to install it pip install ipdb
from ipdb import set_trace as s

x = 10
y = 20

s()

result = x + y

print(result)