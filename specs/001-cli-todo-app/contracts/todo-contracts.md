# API Contracts: CLI Todo Application

## Overview
This document defines the API contracts for the CLI Todo Application. Since this is a CLI application, the "API" refers to the function interfaces and data contracts used within the application.

## Function Interfaces

### TodoManager Class
The TodoManager class provides all the core functionality for managing tasks.

#### Constructor
```python
def __init__(self):
    """
    Initializes the TodoManager with an empty task list.
    """
```

#### add_task(title: str, description: str = "") -> dict
```python
def add_task(self, title: str, description: str = "") -> dict:
    """
    Adds a new task to the task list.
    
    Args:
        title (str): The task title (required, max 100 chars)
        description (str): The task description (optional, max 500 chars)
        
    Returns:
        dict: The created task object with id, title, description, and complete status
        
    Raises:
        ValueError: If title is empty or exceeds length limits
    """
```

#### get_all_tasks() -> list
```python
def get_all_tasks(self) -> list:
    """
    Retrieves all tasks from the task list.
    
    Returns:
        list: A list of all task dictionaries
    """
```

#### update_task(task_id: int, title: str = None, description: str = None, complete: bool = None) -> dict
```python
def update_task(self, task_id: int, title: str = None, description: str = None, complete: bool = None) -> dict:
    """
    Updates an existing task with the provided values.
    
    Args:
        task_id (int): The ID of the task to update
        title (str, optional): New title for the task
        description (str, optional): New description for the task
        complete (bool, optional): New completion status for the task
        
    Returns:
        dict: The updated task object
        
    Raises:
        ValueError: If task_id does not exist or if title is empty
    """
```

#### delete_task(task_id: int) -> bool
```python
def delete_task(self, task_id: int) -> bool:
    """
    Deletes a task from the task list.
    
    Args:
        task_id (int): The ID of the task to delete
        
    Returns:
        bool: True if the task was successfully deleted, False otherwise
    """
```

#### toggle_task_status(task_id: int) -> dict
```python
def toggle_task_status(self, task_id: int) -> dict:
    """
    Toggles the completion status of a task.
    
    Args:
        task_id (int): The ID of the task to toggle
        
    Returns:
        dict: The updated task object with toggled completion status
        
    Raises:
        ValueError: If task_id does not exist
    """
```

#### get_next_id() -> int
```python
def get_next_id(self) -> int:
    """
    Gets the next available ID for a new task.
    IDs are unique and continue from the highest used ID (no reuse).
    
    Returns:
        int: The next available task ID
    """
```

## Data Contracts

### Task Object
All tasks in the system conform to the following structure:

```json
{
  "id": {
    "type": "integer",
    "required": true,
    "description": "Unique identifier for the task, auto-incremented"
  },
  "title": {
    "type": "string",
    "required": true,
    "maxLength": 100,
    "caseSensitive": true,
    "whitespaceNormalized": true,
    "description": "Task title, cannot be empty"
  },
  "description": {
    "type": "string",
    "required": false,
    "maxLength": 500,
    "caseSensitive": true,
    "whitespaceNormalized": true,
    "description": "Optional task description"
  },
  "complete": {
    "type": "boolean",
    "required": true,
    "default": false,
    "description": "Completion status of the task"
  }
}
```

### Error Response
When an error occurs, the system responds with a standardized error object:

```json
{
  "error": {
    "type": "string",
    "required": true,
    "description": "Type of error that occurred"
  },
  "message": {
    "type": "string",
    "required": true,
    "description": "Specific, actionable message about the error"
  }
}
```

## CLI Interface Contracts

### Menu Options
The CLI presents the following numbered options to users:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

### Input Validation
All user inputs are validated according to these rules:
- Task titles: Required, 1-100 characters, cannot be empty
- Task descriptions: Optional, 0-500 characters
- Task IDs: Must be positive integers that correspond to existing tasks
- Menu selections: Must be integers between 1 and 6