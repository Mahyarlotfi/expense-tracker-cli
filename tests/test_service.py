"""Tests for service layer."""

# pylint: disable=redefined-outer-name

from unittest.mock import Mock
from app.service import list_expenses


def test_list_expenses_returns_formatted_dicts():
    """Test listing expenses through repository."""

    repo = Mock()

    repo.get_all_expenses.return_value = [
        {
            "id": 1,
            "amount": 100,
            "category": "food",
            "description": "pizza",
        },
        {
            "id": 2,
            "amount": 50,
            "category": "transport",
            "description": "taxi",
        },
    ]

    result = list_expenses(repo)

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
