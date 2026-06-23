"""Database layer for expense tracker."""

import sqlite3

DB_NAME = "expenses.db"
def get_connection():
    return sqlite3.connect(DB_NAME)

def add_table():
    """Create expenses table if it does not exist."""
    con = get_connection()
    try:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL
            )
            """)
        con.commit()
    finally:
        con.close()


def add_expense(amount, category, description):
    """Insert a new expense into database."""
    con = get_connection()
    try:
        cur = con.cursor()
        cur.execute(
            """
            INSERT INTO expenses (amount, category, description)
            VALUES (?, ?, ?)
            """,
            (amount, category, description),
        )
        con.commit()
    finally:
        con.close()


def get_all_expenses():
    """Fetch all expenses from database."""
    con = get_connection()
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM expenses")
        rows = cur.fetchall()
    finally:
        con.close()
    return rows
    


def delete_expense(expense_id):
    """Delete expense by ID."""
    con = get_connection()
    try:
        cur = con.cursor()
        cur.execute(
            "DELETE FROM expenses WHERE expense_id = ?",
            (expense_id,),
        )
        con.commit()
    finally:
        con.close()


def update_expense(expense_id, amount, category, description):
    """Update an existing expense."""
    con = get_connection()
    try:
        cur = con.cursor()
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
    finally:
        con.close()

