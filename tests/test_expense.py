"""Tests for expense input logic."""

from unittest.mock import patch

from app.expense import create_expense


def test_create_expense_valid_input():
    """Test valid expense creation from user input."""

    with patch("builtins.input", side_effect=["100", "food", "pizza"]):
        result = create_expense()

    assert result == {
        "amount": 100.0,
        "category": "food",
        "description": "pizza",
    }


def test_create_expense_invalid_amount():
    """Test invalid amount input returns None."""

    with patch("builtins.input", side_effect=["abc"]):
        result = create_expense()

    assert result is None
