"""Service layer for expense business logic."""

from .repository import ExpenseRepository


def list_expenses(repo: ExpenseRepository):
    """Return all expenses from repository."""
    return repo.get_all_expenses()
