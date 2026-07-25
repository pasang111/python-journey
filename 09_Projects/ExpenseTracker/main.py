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
