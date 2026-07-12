# A nested dictionary representing a restaurant menu
menu = {
    "appetizers": {
        "soup": 5.00,
        "salad": 6.50
    },
    "entrees": {
        "steak": 20.00,
        "pasta": 15.50
    }
}

# Access the price of pasta
print(menu["entrees"]["pasta"]) 
# Output: 15.50

# Update the price of salad
menu["appetizers"]["salad"] = 7.00

# Add a new dessert to the menu
menu["desserts"] = {
    "cake": 8.00
}