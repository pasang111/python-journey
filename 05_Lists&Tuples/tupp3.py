# 1. Tuples representing immutable data records (Product ID, Name, Unit Price)
item_1 = (101, "Wireless Mouse", 29.99)
item_2 = (102, "Mechanical Keyboard", 89.99)
item_3 = (103, "USB-C Cable", 14.99)

# 2. A List representing a dynamic collection (The Shopping Cart)
# We nest our tuples inside a list.
shopping_cart = [item_1, item_2]

# Mid-Level Operation 1: Mutating the list (Adding an item)
shopping_cart.append(item_3) 
print(f"Cart after append: {shopping_cart}")

# Mid-Level Operation 2: Tuple unpacking & List Comprehension
# Suppose we want to extract only the names of products costing more than $20
expensive_products = [name for prod_id, name, price in shopping_cart if price > 20]
print(f"Products > $20: {expensive_products}")

# Mid-Level Operation 3: Sorting a list of tuples using a lambda key
# We sort the cart dynamically by the price element (index 2 of the tuple)
shopping_cart.sort(key=lambda item: item[2])
print(f"Cart sorted by price: {shopping_cart}")

# Mid-Level Operation 4: Immutability Safety Check
try:
    # Attempting to change the price of the first item inside the tuple
    shopping_cart[0][2] = 9.99  
except TypeError as e:
    print(f"Error caught as expected: {e}")
