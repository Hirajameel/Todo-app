"""
Task data model for the Console Todo Application.

This module implements the Task class with validation and string representation.
"""
from typing import Literal


class Task:
    """
    Represents a single task in the todo application.

    Attributes:
        id: Unique identifier for the task
        title: The task description
        status: Current status of the task ('pending' or 'completed')
    """

    def __init__(self, id: str, title: str, status: Literal["pending", "completed"] = "pending") -> None:
        """
        Initialize a Task instance with validation.

        Args:
            id: Unique identifier for the task
            title: The task description
            status: Current status of the task ('pending' or 'completed')

        Raises:
            ValueError: If title is empty or contains only whitespace,
                       or if status is not 'pending' or 'completed'
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

        if status not in ["pending", "completed"]:
            raise ValueError("Task status must be either 'pending' or 'completed'")

        self.id = id
        self.title = title.strip()
        self.status = status

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.status = "completed"

    def mark_pending(self) -> None:
        """Mark the task as pending."""
        self.status = "pending"

    def __str__(self) -> str:
        """
        Return a string representation of the task.

        Returns:
            String in the format "ID. [ ] Title" for pending tasks
            or "ID. [x] Title" for completed tasks
        """
        status_symbol = "x" if self.status == "completed" else " "
        return f"{self.id}. [{status_symbol}] {self.title}"