# Implementation Plan: CLI Todo Application

**Branch**: `001-cli-todo-app` | **Date**: 2026-02-08 | **Spec**: [link to spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-cli-todo-app/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Detailed technical implementation plan for the in-memory CLI Todo application based on the finalized specification. This plan covers architecture, data model, class breakdown, CLI flow, error handling strategy, test outline, and step-by-step implementation sequence as required.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Python standard library only (no external dependencies)
**Storage**: In-memory list of dictionaries (no persistent storage)
**Testing**: pytest for unit and integration tests
**Target Platform**: Cross-platform (Windows, macOS, Linux) console application
**Project Type**: Single project with CLI interface
**Performance Goals**: Instantaneous response for all operations (sub-second execution)
**Constraints**: No external dependencies, PEP 8 compliance, in-memory storage only, CLI interface
**Scale/Scope**: Single-user application, single-session usage, up to 1000 tasks per session

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Compliance Verification:
- **I. Minimalist Design**: ✅ Confirmed - Simple CLI todo app with basic CRUD operations
- **II. CLI-First Interface**: ✅ Confirmed - All functionality accessible via command-line interface
- **III. Test-First Development**: ✅ Confirmed - Tests will be written before implementation
- **IV. Memory-Only Storage**: ✅ Confirmed - Tasks stored in-memory as dictionaries
- **V. Clean Code Standards**: ✅ Confirmed - Will follow PEP 8 standards with modular architecture
- **VI. Dependency Restraint**: ✅ Confirmed - Using only Python standard library

## 1. High-Level Architecture Diagram

```
┌─────────────────┐    ┌──────────────────┐
│                 │    │                  │
│   main.py       │────│  todo_manager.py │
│                 │    │                  │
│  CLI Loop       │    │  TodoManager     │
│  Menu Handler   │    │  - add_task()    │
│  Input/Output   │    │  - get_tasks()   │
│  Validation     │    │  - update_task() │
│                 │    │  - delete_task() │
│                 │    │  - toggle_task() │
└─────────────────┘    │  - Internal      │
                       │    storage: []   │
                       └──────────────────┘
```

## 2. Proposed File Structure and Module Responsibilities

### Source Code Structure
```
src/
├── main.py              # CLI loop, user input handling, calls to todo_manager
└── todo_manager.py      # Contains TodoManager class for all CRUD + toggle operations

tests/
├── unit/
│   ├── test_todo_manager.py    # Unit tests for todo manager functions
│   └── test_main.py            # Unit tests for CLI interface
├── integration/
│   └── test_cli_flow.py        # Integration tests for CLI interactions
└── conftest.py                # Test configuration and fixtures
```

### Module Responsibilities
- **main.py**: Handles user interaction, menu display, input validation, and calling appropriate methods from todo_manager
- **todo_manager.py**: Contains all business logic for task management, data validation, and storage operations

## 3. Data Model / Task Representation

Each task is represented as a dictionary with the following structure:
```python
{
    "id": int,           # Unique identifier, auto-incremented starting from 1
    "title": str,        # Required, max 100 chars, normalized whitespace
    "description": str,  # Optional, max 500 chars, normalized whitespace
    "complete": bool     # Boolean status, default False
}
```

The TodoManager maintains a list of these dictionaries in memory.

## 4. Core Class or Functions Breakdown

### TodoManager Class
```python
class TodoManager:
    def __init__(self):
        """Initialize with empty task list and next_id counter"""
        
    def add_task(self, title: str, description: str = "") -> dict:
        """Add a new task with validation and auto-ID assignment"""
        
    def get_all_tasks(self) -> list:
        """Return all tasks in the list"""
        
    def get_task_by_id(self, task_id: int) -> dict:
        """Get a specific task by its ID, raises ValueError if not found"""
        
    def update_task(self, task_id: int, title: str = None, 
                   description: str = None, complete: bool = None) -> dict:
        """Update specified fields of a task, returns updated task"""
        
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID, returns True if successful"""
        
    def toggle_task_status(self, task_id: int) -> dict:
        """Toggle the completion status of a task, returns updated task"""
        
    def _validate_title(self, title: str) -> None:
        """Validate title meets requirements (not empty, length limit)"""
        
    def _normalize_text(self, text: str) -> str:
        """Normalize text by stripping whitespace"""
        
    def _get_next_id(self) -> int:
        """Get the next available ID (never reuse deleted IDs)"""
```

## 5. CLI Flow / Menu Options Mapping

The main CLI loop presents users with a numbered menu:
```
CLI Todo Application
====================
1. Add Task
2. View Tasks  
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit
Choose an option (1-6):
```

### Menu Option Mapping:
- **Option 1**: Call `add_task()` with user-provided title and description
- **Option 2**: Call `get_all_tasks()` and display formatted list
- **Option 3**: Get task ID from user, then get updated fields, call `update_task()`
- **Option 4**: Get task ID from user, confirm deletion, call `delete_task()`
- **Option 5**: Get task ID from user, call `toggle_task_status()`
- **Option 6**: Exit the application

## 6. Error Handling Strategy Per Feature

### Input Validation
- **Empty titles**: Prevent with specific error message "Title cannot be empty"
- **Length limits**: Validate title (≤100 chars) and description (≤500 chars)
- **Invalid IDs**: Catch and report "Task with ID X does not exist"
- **Menu selection**: Handle invalid choices with "Please select a valid option (1-6)"

### Error Messages
- All error messages will be specific and actionable
- Format: "[Error Type]: [Specific description of what went wrong and how to fix]"

### Exception Handling
- Use try/catch blocks around operations that might fail
- Validate inputs before processing
- Provide graceful fallbacks where appropriate

## 7. Test Outline (Key Unit Tests to Write First)

### TodoManager Tests
1. **test_add_task_valid_input**: Verify task is added with correct properties
2. **test_add_task_empty_title**: Verify ValueError raised for empty titles
3. **test_add_task_long_inputs**: Verify length validation works
4. **test_get_task_by_id**: Verify retrieving existing and non-existing tasks
5. **test_update_task**: Verify partial and full updates work correctly
6. **test_delete_task**: Verify task deletion and proper ID management
7. **test_toggle_task_status**: Verify status toggling works correctly
8. **test_get_all_tasks**: Verify all tasks are returned correctly

### Main Module Tests
9. **test_display_formatting**: Verify tasks are displayed in correct format
10. **test_input_validation**: Verify CLI input validation works

## 8. Step-by-Step Implementation Sequence

### Phase 1: Core Data Layer
1. Create `todo_manager.py` file
2. Implement `TodoManager` class skeleton
3. Implement `_validate_title()` and `_normalize_text()` helper methods
4. Implement `_get_next_id()` method for ID management
5. Implement `add_task()` method with validation
6. Implement `get_all_tasks()` method
7. Write unit tests for basic functionality
8. Implement `get_task_by_id()` method with error handling

### Phase 2: CRUD Operations
9. Implement `update_task()` method
10. Implement `delete_task()` method
11. Implement `toggle_task_status()` method
12. Write comprehensive unit tests for all operations
13. Test edge cases (invalid IDs, empty titles, etc.)

### Phase 3: CLI Interface
14. Create `main.py` file
15. Implement CLI menu loop
16. Implement input handling for each menu option
17. Connect CLI functions to TodoManager methods
18. Implement error handling and user feedback
19. Add confirmation prompts for destructive operations

### Phase 4: Integration and Polish
20. Write integration tests
21. Test complete user workflows
22. Implement input sanitization
23. Add comprehensive error messages
24. Perform final testing and debugging

## 9. Potential Risks and Trade-offs

### Risks
- **Memory usage**: Large numbers of tasks could consume significant memory (mitigated by max 1000 tasks per session)
- **Data loss**: All data is lost on exit (by design, as per requirements)
- **Concurrency**: Single-user application, no concurrent access concerns

### Trade-offs
- **No persistence**: Trading permanent storage for simplicity
- **Basic UI**: Trading advanced interface for minimal implementation
- **Simple validation**: Trading complex validation for straightforward implementation

## Project Structure

### Documentation (this feature)

```text
specs/001-cli-todo-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── main.py              # Entry point with interactive CLI menu loop
└── todo_manager.py      # Class/functions handling all task operations (add, view, update, delete, mark_complete)

tests/
├── unit/
│   ├── test_todo_manager.py    # Unit tests for todo manager functions
│   └── test_main.py            # Unit tests for CLI interface
├── integration/
│   └── test_cli_flow.py        # Integration tests for CLI interactions
└── conftest.py                # Test configuration and fixtures
```

**Structure Decision**: Single project with CLI interface following the project structure specified in the feature requirements. The application consists of a main CLI module and a todo manager module handling all business logic.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| (None) | (No violations identified) | (All constitution principles followed) |
