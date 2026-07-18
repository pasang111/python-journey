products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for price in products.values():
    print(price)

#the outpyut is this
# 990
# 600
# 250
# 70

for product in products.keys():
    print(product)

# Or

for product in products:
    print(product)
