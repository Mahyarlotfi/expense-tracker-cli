"""Expense input and validation logic."""

import datetime


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
    date = datetime.datetime.now().isoformat()
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date,
    }
    return expense
