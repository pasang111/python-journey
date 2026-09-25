class Category:

    def __init__(self, name):
        # Store category name and create an empty ledger
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        # Add money to the category
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        # Withdraw only if enough money is available
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        # Calculate the current balance
        total = 0

        for item in self.ledger:
            total += item["amount"]

        return total

    def transfer(self, amount, destination):
        # Transfer money to another category
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        # Check if there is enough money
        return amount <= self.get_balance()


def create_spend_chart(categories):
    # Create a spending chart for the categories
    pass
