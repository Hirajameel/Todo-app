"""
TodoManager for the Console Todo Application.

This module implements the TodoManager with CRUD operations
using in-memory storage with a dictionary for O(1) task lookup.
"""
from typing import Dict, List, Optional
from src.models.task import Task


class TodoManager:
    """
    Manages the collection of tasks with CRUD operations.

    Attributes:
        tasks: Dictionary mapping task IDs to Task objects
        next_id: Counter for generating unique numeric IDs
    """

    def __init__(self) -> None:
        """Initialize the TodoManager with empty task storage."""
        self.tasks: Dict[str, Task] = {}
        self.next_id: int = 1

    def add_task(self, title: str) -> str:
        """
        Create a new task and return its ID.

        Args:
            title: The title of the task to be created

        Returns:
            The ID of the newly created task

        Raises:
            ValueError: If the title is empty or contains only whitespace
        """
        # Generate unique ID
        task_id = str(self.next_id)
        self.next_id += 1

        # Create and store the task
        task = Task(id=task_id, title=title)
        self.tasks[task_id] = task

        return task_id

    def get_all_tasks(self) -> List[Task]:
        """
        Return all tasks in creation order.

        Returns:
            A list of all tasks in the order they were created
        """
        # Sort tasks by their numeric ID to maintain creation order
        return sorted(self.tasks.values(), key=lambda t: int(t.id))

    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Retrieve a specific task by ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task if found, None otherwise
        """
        return self.tasks.get(task_id)

    def update_task(self, task_id: str, title: str) -> bool:
        """
        Update a task's title.

        Args:
            task_id: The ID of the task to update
            title: The new title for the task

        Returns:
            True if the task was updated, False if the task was not found
        """
        if task_id not in self.tasks:
            return False

        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or contain only whitespace")

        self.tasks[task_id].title = title
        return True

    def toggle_task(self, task_id: str) -> bool:
        """
        Toggle a task's completion status.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if the task status was toggled, False if the task was not found
        """
        if task_id not in self.tasks:
            return False

        task = self.tasks[task_id]
        if task.status == "pending":
            task.mark_completed()
        else:
            task.mark_pending()

        return True

    def delete_task(self, task_id: str) -> bool:
        """
        Remove a task from storage.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if the task was not found
        """
        if task_id not in self.tasks:
            return False

        del self.tasks[task_id]
        return True