"""Database layer for expense tracker."""

import sqlite3

DB_NAME = "expenses.db"


def get_connection(db_name=None):
    """Return a SQLite database connection.

    Args:
        db_name: Optional database file name. Uses the default database
            when not provided.

    Returns:
        sqlite3.Connection: An active SQLite connection object.
    """
    if db_name is None:
        db_name = DB_NAME
    return sqlite3.connect(db_name)


def add_table(db_name=None):
    """Create expenses table if it does not exist."""
    con = get_connection(db_name)
    try:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                date TEXT NOT NULL
            )
            """)
        con.commit()
    finally:
        con.close()


def add_expense(amount, category, description, date, db_name=None):
    """Insert a new expense into database."""
    con = get_connection(db_name)
    try:
        cur = con.cursor()
        cur.execute(
            """
            INSERT INTO expenses (amount, category, description, date)
            VALUES (?, ?, ?, ?)
            """,
            (amount, category, description, date),
        )
        con.commit()
    finally:
        con.close()


def get_all_expenses(db_name=None):
    """Fetch all expenses from database."""
    con = get_connection(db_name)
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM expenses")
        rows = cur.fetchall()
    finally:
        con.close()
    return rows


def delete_expense(expense_id, db_name=None):
    """Delete expense by ID."""
    con = get_connection(db_name)
    try:
        cur = con.cursor()
        cur.execute(
            "DELETE FROM expenses WHERE expense_id = ?",
            (expense_id,),
        )
        con.commit()
    finally:
        con.close()


def update_expense(expense_id, amount, category, description, date, db_name=None):
    """Update an existing expense."""
    con = get_connection(db_name)
    try:
        cur = con.cursor()
        cur.execute(
            """
            UPDATE expenses
            SET amount = ?,
                category = ?,
                description = ?,
                date = ?
            WHERE expense_id = ?
            """,
            (amount, category, description, date, expense_id),
        )
        con.commit()
    finally:
        con.close()
