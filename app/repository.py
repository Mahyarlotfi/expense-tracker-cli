"""Repository layer for expense database operations."""

from app.database import (
    add_table as db_add_table,
    add_expense as db_add_expense,
    get_all_expenses as db_get_all_expenses,
    delete_expense as db_delete_expense,
    update_expense as db_update_expense,
)


def _row_to_dict(row):
    return {
        "id": row[0],
        "amount": row[1],
        "category": row[2],
        "description": row[3],
        "date": row[4],
    }


class ExpenseRepository:
    """Handles all database operations for expenses."""

    def __init__(self, db_name=None):
        self.db_name = db_name

    def create_table(self):
        """Create expenses table if it does not exist."""
        db_add_table(self.db_name)

    def add_expense(self, amount, category, description, date):
        """Insert a new expense."""
        db_add_expense(amount, category, description, date, self.db_name)

    def get_all_expenses(self):
        """Fetch all expenses."""
        rows = db_get_all_expenses(self.db_name)
        return [_row_to_dict(r) for r in rows]

    def delete_expense(self, expense_id):
        """Delete expense by id."""
        db_delete_expense(expense_id, self.db_name)

    def update_expense(self, expense_id, amount, category, description, date):
        """Update expense by id."""
        db_update_expense(
            expense_id,
            amount,
            category,
            description,
            date,
            self.db_name,
        )
