"""Command-line interface utilities for the Todo Console Application."""

from typing import List, Optional, Tuple
from .models import Task


def display_menu() -> None:
    """Display the main menu with available options."""
    print("\n" + "="*50)
    print("           TODO CONSOLE APPLICATION")
    print("="*50)
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Mark task as complete")
    print("6. Mark task as incomplete")
    print("7. Help")
    print("8. Exit")
    print("="*50)


def get_user_choice() -> str:
    """Get user's menu choice.

    Returns:
        The user's choice as a string
    """
    return input("Enter your choice (1-8): ").strip()


def display_tasks(tasks: List[Task]) -> None:
    """Display all tasks in a formatted table.

    Args:
        tasks: List of Task objects to display
    """
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n" + "-"*80)
    print(f"{'ID':<4} {'Status':<8} {'Title':<30} {'Description':<30}")
    print("-"*80)

    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        title = task.title[:27] + "..." if len(task.title) > 30 else task.title
        desc = (task.description or "")[:27] + "..." if task.description and len(task.description) > 30 else (task.description or "")
        print(f"{task.id:<4} {status:<8} {title:<30} {desc:<30}")

    print("-"*80)


def get_task_input() -> Tuple[str, Optional[str]]:
    """Get task input from user.

    Returns:
        A tuple of (title, description) where description can be None
    """
    title = input("Enter task title: ").strip()

    if not title:
        raise ValueError("Title cannot be empty")

    description_input = input("Enter task description (optional, press Enter to skip): ").strip()
    description = description_input if description_input else None

    return title, description


def get_task_id() -> int:
    """Get task ID from user.

    Returns:
        The task ID as an integer
    """
    id_input = input("Enter task ID: ").strip()

    try:
        task_id = int(id_input)
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        return task_id
    except ValueError:
        if id_input.isdigit():
            raise ValueError("Task ID must be a positive integer")
        else:
            raise ValueError("Please enter a valid number for task ID")


def display_success(message: str) -> None:
    """Display a success message.

    Args:
        message: The success message to display
    """
    print(f"\n[SUCCESS] {message}")


def display_error(message: str) -> None:
    """Display an error message.

    Args:
        message: The error message to display
    """
    print(f"\n[ERROR] {message}")


def display_help() -> None:
    """Display help information for the application."""
    print("\n" + "="*60)
    print("                        HELP")
    print("="*60)
    print("This is a simple todo console application.")
    print()
    print("Features:")
    print("• Add new tasks with required title and optional description")
    print("• View all tasks with ID, status indicator, title, and description")
    print("• Update task title or description by ID")
    print("• Delete tasks by ID")
    print("• Mark tasks as complete or incomplete by ID")
    print()
    print("Tips:")
    print("• Task IDs are assigned sequentially starting from 1")
    print("• Completed tasks show [✓], incomplete tasks show [ ]")
    print("• Empty descriptions are allowed")
    print("• Use 'Exit' option to quit the application")
    print("="*60)