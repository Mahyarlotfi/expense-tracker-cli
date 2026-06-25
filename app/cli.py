"""Command line interface for expense tracker."""

from tabulate import tabulate
from .service import list_expenses


def menu():
    """Display menu and return user choice."""
    choice = input(
        "=====================\n"
        " 1 - Add Expense\n"
        " 2 - View Expense\n"
        " 3 - Delete Expense\n"
        " 4 - Update Expense\n"
        " 0 - Exit\n"
        "=====================\n"
        "Enter your choice: "
    )

    if not choice.isdigit():
        return None
    return int(choice)


def expense_table(repo):
    """Display all expenses in tabular format."""
    expenses = list_expenses(repo)
    print(tabulate(expenses, headers="keys", tablefmt="grid"))
