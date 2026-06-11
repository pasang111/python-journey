# Apply Discount Function

# What is the difference between print() and return()?
# print() is used to display output on the screen.
# return() sends the result back to the program so we can store it or reuse it later.

# Function = defines the logic
# return = sends the result back
# Calling a function = using the function with arguments

def apply_discount(price, discount):

    # checking if price is a number or not
    if not isinstance(price, (int, float)):
        return "The price should be a number"

    # checking if discount is a number or not
    # isinstance() checks whether a value belongs to a certain data type
    elif not isinstance(discount, (int, float)):
        return "The discount should be a number"

    # price should be greater than 0
    elif price <= 0:
        return "The price should be greater than 0"

    # discount must be between 0 and 100
    elif discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    # calculate the final price after discount
    return price - (price * discount / 100)


print(apply_discount(100, 20))
print(apply_discount(74.5, 20.0))
print(apply_discount(100, 100))

# Example:
# price = 100
# discount = 20
# discount amount = 20
# final price = 80