"""Tests for database layer."""

# pylint: disable=redefined-outer-name

import os

import pytest

from app.database import (
    add_table,
    add_expense,
    get_all_expenses,
    delete_expense,
    update_expense,
)

from app.database import get_connection
from app.models import Expense

TEST_DB = "test_expenses.db"


@pytest.fixture
def clean_db():
    """Create a temporary clean database for each test."""
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    add_table(TEST_DB)

    yield TEST_DB

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


def test_add_expense(clean_db):
    """Test adding a new expense."""
    expense = Expense(
        amount=100,
        category="food",
        description="pizza",
        date="2026-01-01",
    )

    add_expense(expense, clean_db)

    rows = get_all_expenses(clean_db)

    assert len(rows) == 1

    row = rows[0]
    assert row[1] == 100
    assert row[2] == "food"
    assert row[3] == "pizza"
    assert row[4] == "2026-01-01"


def test_get_all_expenses(clean_db):
    """Test retrieving all expenses."""
    data = [
        Expense(100, "food", "pizza", "2026-01-01"),
        Expense(50, "transport", "taxi", "2026-01-01"),
        Expense(20, "coffee", "latte", "2026-01-01"),
    ]

    for expense in data:
        add_expense(expense, clean_db)

    rows = get_all_expenses(clean_db)

    assert len(rows) == 3

    for expense in data:
        assert any(
            r[1] == expense.amount
            and r[2] == expense.category
            and r[3] == expense.description
            and r[4] == expense.date
            for r in rows
        )


def test_delete_expense(clean_db):
    """Test deleting an expense."""
    expense = Expense(
        amount=100,
        category="food",
        description="pizza",
        date="2026-01-01",
    )

    add_expense(expense, clean_db)

    rows_before = get_all_expenses(clean_db)
    expense_id = rows_before[0][0]

    delete_expense(expense_id, clean_db)

    rows_after = get_all_expenses(clean_db)
    assert len(rows_after) == 0


def test_update_expense(clean_db):
    """Test updating an expense."""
    # Arrange: insert initial expense
    expense = Expense(
        amount=100,
        category="food",
        description="pizza",
        date="2026-01-01",
    )

    add_expense(expense, clean_db)

    rows = get_all_expenses(clean_db)
    expense_id = rows[0][0]

    # Act: update expense
    expense = Expense(250, "restaurant", "burger", "2026-01-02")
    update_expense(expense_id, expense, clean_db)

    # Assert: verify update
    updated_rows = get_all_expenses(clean_db)

    assert len(updated_rows) == 1

    row = updated_rows[0]
    assert row[0] == expense_id
    assert row[1] == 250
    assert row[2] == "restaurant"
    assert row[3] == "burger"
    assert row[4] == "2026-01-02"


def test_get_all_expenses_empty_db(clean_db):
    """Test fetching expenses from an empty database."""

    rows = get_all_expenses(clean_db)

    assert rows == []


def test_delete_nonexistent_expense(clean_db):
    """Test deleting a non-existent expense."""

    delete_expense(999, clean_db)

    rows = get_all_expenses(clean_db)

    assert rows == []


def test_update_nonexistent_expense(clean_db):
    """Test updating a non-existent expense."""

    expense = Expense(
        amount=100,
        category="food",
        description="pizza",
        date="2026-01-01",
    )

    update_expense(
        999,
        expense,
        clean_db,
    )

    rows = get_all_expenses(clean_db)

    assert rows == []


def test_add_table_creates_expenses_table(clean_db):
    """Test that add_table creates the expenses table."""

    con = get_connection(clean_db)

    try:
        cur = con.cursor()

        cur.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name='expenses'
        """)

        table = cur.fetchone()

    finally:
        con.close()

    assert table is not None
    assert table[0] == "expenses"
