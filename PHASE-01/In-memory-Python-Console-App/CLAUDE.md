# Claude Code Development Guide

This file provides guidance for continuing development with Claude Code.

## Project Structure

- `src/todo/` - Main application source code
- `src/todo/models.py` - Data models (Task class)
- `src/todo/storage.py` - In-memory storage and CRUD operations
- `src/todo/cli.py` - Command-line interface functions
- `src/todo/main.py` - Main application entry point

## Development Workflow

1. Run the application: `python -m src.todo.main`
2. Follow the existing patterns for new features
3. Maintain the separation of concerns (models, storage, CLI, main)
4. Use type hints consistently
5. Follow PEP 8 style guidelines

## Key Design Decisions

- In-memory storage only (no persistence)
- Sequential ID assignment starting from 1
- Graceful error handling with user-friendly messages
- Menu-driven CLI interface
- Task model with id, title, description, completed fields

## Testing

Manual testing is recommended for this application:
- Test all menu options
- Verify error handling with invalid inputs
- Confirm all CRUD operations work correctly
- Test edge cases (empty lists, invalid IDs, etc.)

## Next Steps

- Implement remaining user stories from the specification
- Add comprehensive error handling
- Refine the user interface and experience
- Add help/instructions to the main menu