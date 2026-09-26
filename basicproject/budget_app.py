class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True

        return False

    def get_balance(self):
        total = 0

        for item in self.ledger:
            total += item["amount"]

        return total

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True

        return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True

        return False

    def __str__(self):
        title = self.name.center(30, "*")

        items = ""

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"

            items += f"{description:<23}{amount:>7}\n"

        total = f"Total: {self.get_balance():.2f}"

        return title + "\n" + items + total


def create_spend_chart(categories):

    spending = []

    for category in categories:
        total_spent = 0

        for item in category.ledger:
            if item["amount"] < 0:
                total_spent += -item["amount"]

        spending.append(total_spent)

    total_spending = sum(spending)

    percentages = []

    for amount in spending:
        if total_spending == 0:
            percentages.append(0)
        else:
            percentage = int((amount / total_spending) * 100)
            percentage = (percentage // 10) * 10
            percentages.append(percentage)

    chart = "Percentage spent by category\n"

    for percent in range(100, -1, -10):
        chart += f"{percent:>3}|"

        for percentage in percentages:
            if percentage >= percent:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"

    chart += "    -" + "---" * len(categories) + "\n"

    max_length = 0

    for category in categories:
        if len(category.name) > max_length:
            max_length = len(category.name)

    for i in range(max_length):
        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        if i < max_length - 1:
            chart += "\n"

    return chart