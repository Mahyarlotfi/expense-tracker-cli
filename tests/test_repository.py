"""Tests for repository layer."""

# pylint: disable=redefined-outer-name

import os
import pytest

from app.repository import ExpenseRepository
from app.database import add_table
from app.models import Expense


TEST_DB = "test_expenses.db"


@pytest.fixture
def repo():
    """Create a clean repository instance with a fresh test database."""
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    add_table(TEST_DB)
    repository = ExpenseRepository(TEST_DB)

    yield repository

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


def test_create_table(repo):
    """Test creating expenses table."""

    repo.create_table()

    rows = repo.get_all_expenses()

    assert rows == []


def test_add_expense(repo):
    """Test adding an expense to repository."""

    expense = Expense(
        amount=100,
        category="food",
        description="pizza",
        date="2026-01-01",
    )

    repo.add_expense(expense)

    rows = repo.get_all_expenses()

    assert len(rows) == 1

    row = rows[0]
    assert row["amount"] == 100
    assert row["category"] == "food"
    assert row["description"] == "pizza"
    assert row["date"] == "2026-01-01"


def test_get_all_expenses(repo):
    """Test retrieving multiple expenses."""

    data = [
        (100, "food", "pizza", "2026-01-01"),
        (50, "transport", "taxi", "2026-01-02"),
        (20, "coffee", "latte", "2026-01-03"),
    ]

    for amount, category, description, date in data:
        expense = Expense(
            amount=amount,
            category=category,
            description=description,
            date=date
            )
        repo.add_expense(expense)

    rows = repo.get_all_expenses()

    assert len(rows) == 3

    for amount, category, description, date in data:
        assert any(
            r["amount"] == amount
            and r["category"] == category
            and r["description"] == description
            and r["date"] == date
            for r in rows
        )


def test_delete_expense(repo):
    """Test deleting an expense."""

    expense = Expense(
        amount=100,
        category="food",
        description="pizza",
        date="2026-01-01",
    )

    repo.add_expense(expense)

    rows_before = repo.get_all_expenses()
    expense_id = rows_before[0]["id"]

    repo.delete_expense(expense_id)

    rows_after = repo.get_all_expenses()

    assert len(rows_after) == 0


def test_update_expense(repo):
    """Test updating an expense."""

    expense = Expense(
        amount=100,
        category="food",
        description="pizza",
        date="2026-01-01",
    )

    repo.add_expense(expense)

    rows = repo.get_all_expenses()
    expense_id = rows[0]["id"]

    repo.update_expense(
        expense_id,
        250,
        "restaurant",
        "burger",
        "2026-01-03",
    )

    updated_rows = repo.get_all_expenses()

    assert len(updated_rows) == 1

    row = updated_rows[0]
    assert row["id"] == expense_id
    assert row["amount"] == 250
    assert row["category"] == "restaurant"
    assert row["description"] == "burger"
    assert row["date"] == "2026-01-03"


def test_empty_repository(repo):
    """Test repository returns empty list when no data exists."""

    rows = repo.get_all_expenses()

    assert rows == []
