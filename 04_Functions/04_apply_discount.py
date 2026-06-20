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



# Apply Discount Function

def apply_discount(price, discount):

    # checking if price is a number or not
    if not isinstance(price, (int, float)):
        return "The price should be a number"

    # checking if discount is a number or not
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


# asking user for input
price = float(input("Enter the product price: "))
discount = float(input("Enter the discount percentage: "))

# calling the function
final_price = apply_discount(price, discount)

print("Final price after discount:", final_price)


#tax calculator

def calculator_tax(price, tax_percentage):
    if not isinstance(price,(int, float)):
        return "Price must be a number"
    
    if not isinstance(tax_percentage,(int, float)):
        return "Tax percentage must be a number"
    
    if price < 0:
        print("Price cannot be negative")
    
    if tax_percentage < 0:
        print("Tax percentage cannot be negative")
    
    return price + (price * tax_percentage / 100)

price = float(input("Enter product price: "))
tax = float(input("Enter tax percentage: "))

final_price = calculator_tax(price,tax)

price("Final price with tax:", final_price)


#grade calculator

def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Marks should be between 0 and 100"
    
    if marks >=80:
        print("Grade A")
    
    if marks >=60:
        print("Grade B")
    
    if marks >=40:
        print("Grade C")
    
    else:
        return "Grade F"

marks = int(input("Please Enter your marks: ")) # ask the user to input their marks

result = calculate_grade(marks) #call the function and store the returned value in result

print(result) #Display the returned value