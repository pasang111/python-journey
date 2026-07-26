expenses = []

while True:
    name = input("Expense name: ")
    amount = float(input("Amount: $"))

    expenses.append({
        "name": name,
        "amount": amount
    })

    choice = input("Add another? (y/n): ")
    if choice.lower() != "y":
        break

print(expenses)


# eg : 2
# Simple Expense Tracker

expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append((name, amount))
        print("Expense added!")

    elif choice == "2":
        total = 0
        print("\nExpenses:")
        for item in expenses:
            print(item[0], "-", item[1])
            total += item[1]
        print("Total Expense:", total)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

# Expense Tracker
# 1. Add Expense
# 2. View Expenses
# 3. Exit
# Enter your choice: 1

# Enter expense name: Food
# Enter amount: 15
# Expense added!

# Expense Tracker
# 1. Add Expense
# 2. View Expenses
# 3. Exit
# Enter your choice: 1

# Enter expense name: Transport
# Enter amount: 8
# Expense added!

# Expense Tracker
# 1. Add Expense
# 2. View Expenses
# 3. Exit
# Enter your choice: 2

# Expenses:
# Food - 15.0
# Transport - 8.0
# Total Expense: 23.0
