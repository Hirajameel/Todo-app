"""
Interactive CLI menu for the Console Todo Application.

This module implements the CLI command handlers for all user interactions.
"""
from typing import Optional
from src.core.manager import TodoManager


# Define menu constants
MENU_ADD_TASK = "Add Task"
MENU_VIEW_TASKS = "View Tasks"
MENU_UPDATE_TASK = "Update Task"
MENU_DELETE_TASK = "Delete Task"
MENU_TOGGLE_TASK = "Mark tasks complete"
MENU_EXIT = "Exit"


class TodoMenu:
    """
    Handles the CLI menu and command parsing for the todo application.
    """

    def __init__(self, manager: TodoManager) -> None:
        """
        Initialize the TodoMenu with a TodoManager instance.

        Args:
            manager: The TodoManager to interact with
        """
        self.manager = manager

    def display_menu(self) -> None:
        """Display the available menu options to the user."""
        print("\n--- Console Todo Application ---")
        print(f"1. {MENU_ADD_TASK}")
        print(f"2. {MENU_VIEW_TASKS}")
        print(f"3. {MENU_UPDATE_TASK}")
        print(f"4. {MENU_DELETE_TASK}")
        print(f"5. {MENU_TOGGLE_TASK}")
        print(f"6. {MENU_EXIT}")
        print("--------------------------------")

    def handle_add_task(self) -> None:
        """Handle the add task command."""
        try:
            title = input("Enter task title: ").strip()
            if not title:
                print("Error: Task title cannot be empty.")
                return

            task_id = self.manager.add_task(title)
            print(f"Task added with ID: {task_id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error adding task: {e}")

    def handle_view_tasks(self) -> None:
        """Handle the view tasks command."""
        tasks = self.manager.get_all_tasks()
        if not tasks:
            print("No tasks found.")
            return

        print("\nYour Tasks:")
        for task in tasks:
            print(task)

    def handle_update_task(self) -> None:
        """Handle the update task command."""
        try:
            task_id = input("Enter task ID to update: ").strip()
            if not task_id:
                print("Error: Task ID cannot be empty.")
                return

            # Check if task exists
            task = self.manager.get_task(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            new_title = input("Enter new task title: ").strip()
            if not new_title:
                print("Error: Task title cannot be empty.")
                return

            success = self.manager.update_task(task_id, new_title)
            if success:
                print(f"Task {task_id} updated successfully.")
            else:
                print(f"Error: Failed to update task {task_id}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error updating task: {e}")

    def handle_delete_task(self) -> None:
        """Handle the delete task command."""
        try:
            task_id = input("Enter task ID to delete: ").strip()
            if not task_id:
                print("Error: Task ID cannot be empty.")
                return

            success = self.manager.delete_task(task_id)
            if success:
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except Exception as e:
            print(f"Unexpected error deleting task: {e}")

    def handle_toggle_task(self) -> None:
        """Handle the toggle task command."""
        try:
            task_id = input("Enter task ID to toggle: ").strip()
            if not task_id:
                print("Error: Task ID cannot be empty.")
                return

            success = self.manager.toggle_task(task_id)
            if success:
                task = self.manager.get_task(task_id)
                status = "completed" if task and task.status == "completed" else "pending"
                print(f"Task {task_id} marked as {status}.")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except Exception as e:
            print(f"Unexpected error toggling task: {e}")

    def handle_command(self, choice: str) -> bool:
        """
        Handle the user's menu choice.

        Args:
            choice: The user's menu choice (1-6)

        Returns:
            True if the application should continue, False to exit
        """
        try:
            option = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 6.")
            return True

        if option == 1:
            self.handle_add_task()
        elif option == 2:
            self.handle_view_tasks()
        elif option == 3:
            self.handle_update_task()
        elif option == 4:
            self.handle_delete_task()
        elif option == 5:
            self.handle_toggle_task()
        elif option == 6:
            print("Goodbye!")
            return False
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

        return True