import os

import pytest

from app.database import (
    add_table,
    add_expense,
    get_all_expenses,
    delete_expense,
    update_expense,
)

TEST_DB = "test_expenses.db"


@pytest.fixture
def clean_db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

    add_table(TEST_DB)

    yield TEST_DB

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)


def test_add_expense(clean_db):
    add_expense(
        100,
        "food",
        "pizza",
        clean_db,
    )

    rows = get_all_expenses(clean_db)

    assert len(rows) == 1

    row = rows[0]
    assert row[1] == 100
    assert row[2] == "food"
    assert row[3] == "pizza"


def test_get_all_expenses(clean_db):
    data = [
        (100, "food", "pizza"),
        (50, "transport", "taxi"),
        (20, "coffee", "latte"),
    ]

    for item in data:
        add_expense(*item, clean_db)

    rows = get_all_expenses(clean_db)

    assert len(rows) == 3

    for amount, category, description in data:
        assert any(
            r[1] == amount and r[2] == category and r[3] == description for r in rows
        )


def test_delete_expense(clean_db):
    add_expense(
        100,
        "food",
        "pizza",
        clean_db,
    )

    rows_before = get_all_expenses(clean_db)
    expense_id = rows_before[0][0]

    delete_expense(expense_id, clean_db)

    rows_after = get_all_expenses(clean_db)
    assert len(rows_after) == 0


def test_update_expense(clean_db):
    # Arrange: insert initial expense
    add_expense(
        100,
        "food",
        "pizza",
        clean_db,
    )

    rows = get_all_expenses(clean_db)
    expense_id = rows[0][0]

    # Act: update expense
    update_expense(
        expense_id,
        250,
        "restaurant",
        "burger",
        clean_db,
    )

    # Assert: verify update
    updated_rows = get_all_expenses(clean_db)

    assert len(updated_rows) == 1

    row = updated_rows[0]
    assert row[0] == expense_id
    assert row[1] == 250
    assert row[2] == "restaurant"
    assert row[3] == "burger"
