"""Data models for the Todo Console Application."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """Represents a todo task with id, title, description, and completion status."""

    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False