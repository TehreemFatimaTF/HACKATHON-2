# In-Memory Todo Console Application

A simple command-line todo application with in-memory storage.

## Setup

1. Ensure you have Python 3.13+ installed
2. Install UV package manager if not already installed:
   ```bash
   pip install uv
   ```
3. Install the project dependencies:
   ```bash
   uv sync
   ```
4. Run the application:
   ```bash
   uv run python -m src.todo.main
   ```

## Features

- Add new tasks with required title and optional description
- View all tasks with ID, status indicator, title, and description
- Update task title or description by ID
- Delete tasks by ID
- Mark tasks as complete or incomplete by ID
- Clear, text-based menu interface
- Graceful error handling

## Usage

The application provides a menu-driven interface with numbered options for all operations.