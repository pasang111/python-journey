from datetime import datetime

# Store all expenses
expenses = []


# Add a new expense
def add_expense():
    name = input("Enter expense name: ").strip()

    if not name:
        print("Expense name cannot be empty.")
        return

    # Get a valid amount
    while True:
        try:
            amount = float(input("Enter amount: $"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Get expense category
    category = input("Enter category: ").strip()

    if not category:
        category = "Other"

    # Get current date
    date = datetime.now().strftime("%Y-%m-%d")

    # Create an expense dictionary
    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)

    print("Expense added successfully.")


# Display all expenses
def view_expenses():
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\nExpenses:")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['name']} - "
            f"${expense['amount']:.2f} - "
            f"{expense['category']} - "
            f"{expense['date']}"
        )


# Calculate total expense
def show_total():
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expense: ${total:.2f}")


# Find the highest expense
def show_highest():
    if not expenses:
        print("\nNo expenses found.")
        return

    highest = max(expenses, key=lambda expense: expense["amount"])

    print("\nHighest Expense:")
    print(f"Name: {highest['name']}")
    print(f"Amount: ${highest['amount']:.2f}")
    print(f"Category: {highest['category']}")
    print(f"Date: {highest['date']}")


# Show spending by category
def category_summary():
    if not expenses:
        print("\nNo expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in categories:
            categories[category] = 0

        categories[category] += amount

    print("\nCategory Summary:")

    for category, total in categories.items():
        print(f"{category}: ${total:.2f}")


# Delete an expense
def delete_expense():
    if not expenses:
        print("\nNo expenses found.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        removed = expenses.pop(number - 1)

        print(
            f"Deleted: {removed['name']} "
            f"- ${removed['amount']:.2f}"
        )

    except ValueError:
        print("Please enter a valid number.")


# Main menu
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Show Highest Expense")
    print("5. Category Summary")
    print("6. Delete Expense")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        show_highest()

    elif choice == "5":
        category_summary()

    elif choice == "6":
        delete_expense()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")