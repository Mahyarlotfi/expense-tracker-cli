"""Domain models for expense tracker."""

from dataclasses import dataclass


@dataclass
class Expense:
    """Represents an expense entity."""
    amount: float
    category: str
    description: str
    date: str
