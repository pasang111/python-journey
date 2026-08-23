import secrets
import string

# Display the title
print("=== Password Generator ===")

# Ask the user how long they want the password to be
length = int(input("Password length: "))

# Check if the password is long enough
if length < 4:
    print("Password must be at least 4 characters long.")

else:
    # Ask the user if they want numbers
    use_numbers = input("Include numbers? (y/n): ").lower()

    # Ask the user if they want symbols
    use_symbols = input("Include symbols? (y/n): ").lower()

    # Create a collection of uppercase and lowercase letters
    letters = string.ascii_letters

    # Create a collection of numbers (0-9)
    numbers = string.digits

    # Create a collection of symbols (!, @, #, $, etc.)
    symbols = string.punctuation

    # Start with letters as the default characters
    characters = letters

    # Add numbers if the user chose "y"
    if use_numbers == "y":
        characters += numbers

    # Add symbols if the user chose "y"
    if use_symbols == "y":
        characters += symbols

    # Start with an empty password
    password = ""

    # Add at least one number if numbers were selected
    if use_numbers == "y":
        password += secrets.choice(numbers)

    # Add at least one symbol if symbols were selected
    if use_symbols == "y":
        password += secrets.choice(symbols)

    # Keep adding random characters until we reach the requested length
    while len(password) < length:
        password += secrets.choice(characters)

    # Display the finished password
    print("Your password:", password)
