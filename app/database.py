"""Database layer for expense tracker."""

import sqlite3

con = sqlite3.connect("expenses.db")
cur = con.cursor()


def add_table():
    """Create expenses table if it does not exist."""
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL
        )
        """)
    con.commit()


def add_expense(amount, category, description):
    """Insert a new expense into database."""
    cur.execute(
        """
        INSERT INTO expenses (amount, category, description)
        VALUES (?, ?, ?)
        """,
        (amount, category, description),
    )
    con.commit()


def get_all_expenses():
    """Fetch all expenses from database."""
    cur.execute("SELECT * FROM expenses")
    return cur.fetchall()


def delete_expense(expense_id):
    """Delete expense by ID."""
    cur.execute(
        "DELETE FROM expenses WHERE expense_id = ?",
        (expense_id,),
    )
    con.commit()


def update_expense(expense_id, amount, category, description):
    """Update an existing expense."""
    cur.execute(
        """
        UPDATE expenses
        SET amount = ?,
            category = ?,
            description = ?
        WHERE expense_id = ?
        """,
        (amount, category, description, expense_id),
    )
    con.commit()


def close_connection():
    """Close database connection."""
    con.close()
