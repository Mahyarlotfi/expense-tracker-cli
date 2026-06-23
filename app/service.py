"""Service layer for expense business logic."""

from .database import get_all_expenses


def list_expenses():
    """Return all expenses formatted as dictionaries."""
    return [
        {
            "id": e[0],
            "amount": e[1],
            "category": e[2],
            "description": e[3],
        }
        for e in get_all_expenses()
    ]
