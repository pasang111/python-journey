# creating dictionaries
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

#using enumerate 
for product in enumerate(products):
    print(product)
# (0, 'Laptop')
# (1, 'Smartphone')
# (2, 'Tablet')
# (3, 'Headphones')
  
for index, product in enumerate(products):
    print(index, product)

# if we need to iterate over the values, we can replace products by products.values():
for price in enumerate(products.values()):
    print(price)
