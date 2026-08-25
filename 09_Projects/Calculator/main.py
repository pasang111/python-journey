# Enhanced Calculator

def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate(num1, operator, num2):
    """Perform the requested calculation."""
    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

    elif operator == "%":
        if num2 == 0:
            return "Error: Modulo by zero is not allowed."
        return num1 % num2

    elif operator == "**":
        return num1 ** num2

    else:
        return "Error: Invalid operator."


def main():
    print("=" * 40)
    print("        ENHANCED CALCULATOR")
    print("=" * 40)
    print("Operators: +  -  *  /  %  **")
    print("Type 'q' at any prompt to quit.")
    print()

    while True:
        first_input = input("Enter the first number: ").strip()

        if first_input.lower() == "q":
            print("Goodbye!")
            break

        try:
            num1 = float(first_input)
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        operator = input("Enter an operator (+, -, *, /, %, **): ").strip()

        if operator.lower() == "q":
            print("Goodbye!")
            break

        if operator not in ["+", "-", "*", "/", "%", "**"]:
            print("Invalid operator.\n")
            continue

        second_input = input("Enter the second number: ").strip()

        if second_input.lower() == "q":
            print("Goodbye!")
            break

        try:
            num2 = float(second_input)
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        result = calculate(num1, operator, num2)

        print(f"\nResult: {num1:g} {operator} {num2:g} = {result}")
        print("-" * 40)


if __name__ == "__main__":
    main()
