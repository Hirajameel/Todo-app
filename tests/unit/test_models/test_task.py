"""
Unit tests for the Task model in the Console Todo Application.

These tests verify the Task class functionality and validation.
"""
import pytest
from src.models.task import Task


def test_task_creation_with_valid_data():
    """Test creating a task with valid data."""
    task = Task(id="1", title="Test task")

    assert task.id == "1"
    assert task.title == "Test task"
    assert task.status == "pending"


def test_task_creation_with_completed_status():
    """Test creating a task with completed status."""
    task = Task(id="1", title="Test task", status="completed")

    assert task.id == "1"
    assert task.title == "Test task"
    assert task.status == "completed"


def test_task_creation_fails_with_empty_title():
    """Test that creating a task with empty title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
        Task(id="1", title="")


def test_task_creation_fails_with_whitespace_only_title():
    """Test that creating a task with whitespace-only title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty or contain only whitespace"):
        Task(id="1", title="   ")


def test_task_creation_fails_with_invalid_status():
    """Test that creating a task with invalid status raises ValueError."""
    with pytest.raises(ValueError, match="Task status must be either 'pending' or 'completed'"):
        Task(id="1", title="Test task", status="invalid")


def test_mark_completed_changes_status():
    """Test that marking a task as completed changes its status."""
    task = Task(id="1", title="Test task")

    task.mark_completed()

    assert task.status == "completed"


def test_mark_pending_changes_status():
    """Test that marking a task as pending changes its status."""
    task = Task(id="1", title="Test task", status="completed")

    task.mark_pending()

    assert task.status == "pending"


def test_task_string_representation():
    """Test the string representation of a task."""
    task = Task(id="1", title="Test task", status="pending")

    expected = "1. [ ] Test task"
    assert str(task) == expected


def test_completed_task_string_representation():
    """Test the string representation of a completed task."""
    task = Task(id="1", title="Test task", status="completed")

    expected = "1. [x] Test task"
    assert str(task) == expected