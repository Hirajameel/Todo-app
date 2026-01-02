"""
Main entry point for the Console Todo Application.

This module implements the main application loop that integrates
the CLI interface with the core business logic.
"""
import sys
import os

# Add the project root to sys.path to allow imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from src.core.manager import TodoManager
from src.cli.menu import TodoMenu


def main():
    """Main function to run the todo application."""
    # Initialize the application components
    manager = TodoManager()
    menu = TodoMenu(manager)

    # Main application loop
    while True:
        menu.display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        # Handle the user's choice
        should_continue = menu.handle_command(choice)

        if not should_continue:
            break


if __name__ == "__main__":
    main()