"""Main entry point for expense tracker application."""

from app.expense import create_expense
from app.cli import menu, expense_table
from app.repository import ExpenseRepository

repo = ExpenseRepository()

repo.create_table()

while True:
    choice = menu()
    if choice is None:
        print("Invalid input, please enter a number")
        continue

    if choice == 1:
        expense = create_expense()
        if expense is None:
            continue
        repo.add_expense(expense)

    elif choice == 2:
        expense_table(repo)

    elif choice == 3:
        try:
            delete_id = int(input("Please enter your id: "))
            repo.delete_expense(delete_id)
        except ValueError:
            print("Please enter a valid id")

    elif choice == 4:
        try:
            update_id = int(input("Please enter your id: "))
            expense = create_expense()
            if expense is None:
                continue
            repo.update_expense(
                update_id,
                expense,
            )
        except ValueError:
            print("Please enter a valid id")

    elif choice == 0:
        break
