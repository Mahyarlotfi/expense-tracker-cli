"""Main entry point for expense tracker application."""

from app.database import (
    add_table,
    add_expense,
    delete_expense,
    update_expense,
)
from app.expense import create_expense
from app.cli import menu, expense_table

add_table()

while True:
    choice = menu()
    if choice is None:
        print("Invalid input, please enter a number")
        continue

    if choice == 1:
        expense = create_expense()
        if expense is None:
            continue
        add_expense(
            amount=expense["amount"],
            category=expense["category"],
            description=expense["description"],
        )

    elif choice == 2:
        expense_table()

    elif choice == 3:
        try:
            delete_id = int(input("Please enter your id: "))
            delete_expense(delete_id)
        except ValueError:
            print("Please enter a valid id")

    elif choice == 4:
        try:
            update_id = int(input("Please enter your id: "))
            expense = create_expense()
            if expense is None:
                continue
            update_expense(
                expense_id=update_id,
                amount=expense["amount"],
                category=expense["category"],
                description=expense["description"],
            )
        except ValueError:
            print("Please enter a valid id")

    elif choice == 0:
        break
