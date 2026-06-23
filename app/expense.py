"""Expense input and validation logic."""


def create_expense():
    """Collect and validate expense input from user."""
    amount = input("Please enter amount: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount")
        return None
    category = input("Please enter category: ")
    description = input("Please enter description: ")
    expense = {"amount": amount, "category": category, "description": description}
    return expense
