"""In-memory storage manager for tasks."""

from typing import List, Optional
from .models import Task


class TaskManager:
    """Manages in-memory storage of tasks with CRUD operations."""

    def __init__(self):
        """Initialize the task manager with empty task list and ID counter."""
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task with the given title and optional description.

        Args:
            title: The task title (required)
            description: The task description (optional)

        Returns:
            The created Task object with assigned ID
        """
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            completed=False
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks in the system.

        Returns:
            List of all Task objects
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """Update a task's title or description by ID.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if task was updated, False if task not found
        """
        for task in self._tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was deleted, False if task not found
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                del self._tasks[i]
                return True
        return False

    def mark_task_completed(self, task_id: int, completed: bool) -> bool:
        """Mark a task as completed or incomplete by ID.

        Args:
            task_id: The ID of the task to update
            completed: True to mark as completed, False to mark as incomplete

        Returns:
            True if task was updated, False if task not found
        """
        for task in self._tasks:
            if task.id == task_id:
                task.completed = completed
                return True
        return False