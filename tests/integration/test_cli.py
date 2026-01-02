"""
Integration tests for the CLI functionality in the Console Todo Application.

These tests verify the integration between the CLI interface and the core logic.
"""
import io
import sys
from unittest.mock import patch
from src.core.manager import TodoManager
from src.cli.menu import TodoMenu


def test_add_task_through_cli():
    """Test adding a task through the CLI interface."""
    manager = TodoManager()
    menu = TodoMenu(manager)

    # Mock user input for the task title
    with patch('builtins.input', return_value='Test task'):
        # Capture the printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        menu.handle_add_task()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify the task was added
        output = captured_output.getvalue()
        assert "Task added with ID: 1" in output

        # Verify the task exists in the manager
        tasks = manager.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Test task"
        assert tasks[0].id == "1"


def test_add_task_with_empty_title_through_cli():
    """Test adding a task with empty title through the CLI interface."""
    manager = TodoManager()
    menu = TodoMenu(manager)

    # Mock user input for an empty task title
    with patch('builtins.input', return_value=''):
        # Capture the printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        menu.handle_add_task()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify the error message
        output = captured_output.getvalue()
        assert "Error: Task title cannot be empty." in output

        # Verify no task was added
        tasks = manager.get_all_tasks()
        assert len(tasks) == 0


def test_view_tasks_through_cli():
    """Test viewing tasks through the CLI interface."""
    manager = TodoManager()
    menu = TodoMenu(manager)

    # Add a task first
    manager.add_task("Test task")

    # Capture the printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    menu.handle_view_tasks()

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Verify the task is displayed
    output = captured_output.getvalue()
    assert "1. [ ] Test task" in output


def test_view_empty_tasks_through_cli():
    """Test viewing tasks when no tasks exist."""
    manager = TodoManager()
    menu = TodoMenu(manager)

    # Capture the printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    menu.handle_view_tasks()

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Verify the appropriate message is displayed
    output = captured_output.getvalue()
    assert "No tasks found." in output


def test_menu_command_parsing():
    """Test that the menu correctly handles different commands."""
    manager = TodoManager()
    menu = TodoMenu(manager)

    # Add a task first
    task_id = manager.add_task("Test task")

    # Test the command handling for viewing tasks
    result = menu.handle_command("2")  # View tasks option
    assert result is True  # Should continue running


def test_menu_command_parsing_exit():
    """Test that the menu correctly handles the exit command."""
    manager = TodoManager()
    menu = TodoMenu(manager)

    # Test the command handling for exit
    result = menu.handle_command("6")  # Exit option
    assert result is False  # Should stop running


def test_menu_command_parsing_invalid():
    """Test that the menu correctly handles invalid commands."""
    manager = TodoManager()
    menu = TodoMenu(manager)

    # Test the command handling for an invalid option
    result = menu.handle_command("99")  # Invalid option
    assert result is True  # Should continue running with error message