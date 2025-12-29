"""Main entry point for the Todo Console Application."""

from typing import Optional
from .storage import TaskManager
from .cli import (
    display_menu, get_user_choice, display_tasks, get_task_input,
    get_task_id, display_success, display_error, display_help
)


def main():
    """Main application entry point."""
    print("Welcome to the Todo Console Application!")
    print("Type 'help' for instructions or select an option from the menu.")

    task_manager = TaskManager()

    while True:
        try:
            display_menu()
            choice = get_user_choice()

            if choice == '1':
                add_task(task_manager)
            elif choice == '2':
                view_tasks(task_manager)
            elif choice == '3':
                update_task(task_manager)
            elif choice == '4':
                delete_task(task_manager)
            elif choice == '5':
                mark_task_completed(task_manager, True)
            elif choice == '6':
                mark_task_completed(task_manager, False)
            elif choice == '7':
                display_help()
            elif choice == '8':
                print("\nThank you for using the Todo Console Application. Goodbye!")
                break
            else:
                display_error("Invalid choice. Please enter a number between 1-8.")

        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            display_error(f"An unexpected error occurred: {str(e)}")
            print("The application will continue running.")


def add_task(task_manager: TaskManager):
    """Handle adding a new task."""
    try:
        print("\n--- Add New Task ---")
        title, description = get_task_input()

        task = task_manager.add_task(title, description)
        display_success(f"Task '{task.title}' added successfully with ID {task.id}")

    except ValueError as e:
        display_error(str(e))
    except Exception as e:
        display_error(f"Failed to add task: {str(e)}")


def view_tasks(task_manager: TaskManager):
    """Handle viewing all tasks."""
    try:
        print("\n--- All Tasks ---")
        tasks = task_manager.get_all_tasks()
        display_tasks(tasks)

    except Exception as e:
        display_error(f"Failed to view tasks: {str(e)}")


def update_task(task_manager: TaskManager):
    """Handle updating a task."""
    try:
        print("\n--- Update Task ---")
        task_id = get_task_id()

        # Check if task exists
        existing_task = task_manager.get_task_by_id(task_id)
        if not existing_task:
            display_error(f"Task with ID {task_id} not found.")
            return

        print(f"Current task: {existing_task.title}")
        title_input = input(f"Enter new title (current: '{existing_task.title}', press Enter to keep current): ").strip()
        description_input = input(f"Enter new description (current: '{existing_task.description or 'None'}', press Enter to keep current): ").strip()

        # Prepare updates
        new_title = title_input if title_input else None
        new_description = description_input if description_input else None

        # If user wants to clear the description, they should enter "None" or a special command
        if description_input == "":
            new_description = existing_task.description  # Keep current description

        if description_input.lower() == "none":
            new_description = None

        # Update the task
        success = task_manager.update_task(
            task_id,
            title=new_title,
            description=new_description
        )

        if success:
            display_success(f"Task ID {task_id} updated successfully")
        else:
            display_error(f"Failed to update task with ID {task_id}")

    except ValueError as e:
        display_error(str(e))
    except Exception as e:
        display_error(f"Failed to update task: {str(e)}")


def delete_task(task_manager: TaskManager):
    """Handle deleting a task."""
    try:
        print("\n--- Delete Task ---")
        task_id = get_task_id()

        # Check if task exists
        existing_task = task_manager.get_task_by_id(task_id)
        if not existing_task:
            display_error(f"Task with ID {task_id} not found.")
            return

        success = task_manager.delete_task(task_id)

        if success:
            display_success(f"Task ID {task_id} deleted successfully")
        else:
            display_error(f"Failed to delete task with ID {task_id}")

    except ValueError as e:
        display_error(str(e))
    except Exception as e:
        display_error(f"Failed to delete task: {str(e)}")


def mark_task_completed(task_manager: TaskManager, completed: bool):
    """Handle marking a task as completed or incomplete."""
    try:
        status = "complete" if completed else "incomplete"
        print(f"\n--- Mark Task as {status.title()} ---")
        task_id = get_task_id()

        # Check if task exists
        existing_task = task_manager.get_task_by_id(task_id)
        if not existing_task:
            display_error(f"Task with ID {task_id} not found.")
            return

        success = task_manager.mark_task_completed(task_id, completed)

        if success:
            action = "completed" if completed else "incomplete"
            display_success(f"Task ID {task_id} marked as {action} successfully")
        else:
            display_error(f"Failed to update task status for ID {task_id}")

    except ValueError as e:
        display_error(str(e))
    except Exception as e:
        display_error(f"Failed to update task status: {str(e)}")


if __name__ == "__main__":
    main()