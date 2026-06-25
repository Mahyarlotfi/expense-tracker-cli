"""Tests for service layer."""

from unittest.mock import patch

from app.service import list_expenses


def test_list_expenses_returns_formatted_dicts():
    """Test converting database rows to dictionaries."""

    fake_rows = [
        (1, 100, "food", "pizza"),
        (2, 50, "transport", "taxi"),
    ]

    with patch("app.service.get_all_expenses", return_value=fake_rows):
        result = list_expenses()

    assert len(result) == 2

    assert result[0] == {
        "id": 1,
        "amount": 100,
        "category": "food",
        "description": "pizza",
    }

    assert result[1] == {
        "id": 2,
        "amount": 50,
        "category": "transport",
        "description": "taxi",
    }
