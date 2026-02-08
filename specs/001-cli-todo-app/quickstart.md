# Quickstart Guide: CLI Todo Application

## Overview
This guide provides instructions for setting up and running the CLI Todo Application.

## Prerequisites
- Python 3.13+ installed on your system
- Basic familiarity with command-line interfaces

## Setup Instructions

### 1. Clone or Access the Project
The project files are located in the repository:
```
src/
├── main.py              # Entry point with interactive CLI menu loop
└── todo_manager.py      # Class/functions handling all task operations
```

### 2. Environment Setup
No external dependencies are required. The application uses only Python's standard library.

### 3. Running the Application
Execute the main.py file to start the CLI application:
```bash
python src/main.py
```

## Usage Instructions

### Main Menu
Once the application starts, you'll see the main menu with the following options:
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

### Available Operations

#### 1. Add Task
- Prompts for a title (required, max 100 characters)
- Optionally prompts for a description (max 500 characters)
- Automatically assigns a unique incremental ID
- Sets the task status to incomplete [ ]

#### 2. View Tasks
- Displays all tasks with their ID, status indicator ([X] for complete, [ ] for incomplete), title, and description
- Shows "No tasks yet." if the list is empty

#### 3. Update Task
- Prompts for a task ID
- Allows updating title, description, and/or status
- Only specified fields are updated, leaving others unchanged

#### 4. Delete Task
- Prompts for a task ID
- Asks for confirmation before deletion
- Removes the task from the list

#### 5. Mark Complete/Incomplete
- Prompts for a task ID
- Toggles the completion status of the task
- Shows the updated status message

#### 6. Exit
- Exits the application
- Note: All data is lost upon exit as tasks are stored only in memory

## Example Workflow

1. Start the application: `python src/main.py`
2. Choose option 1 to add a task:
   - Enter title: "Buy groceries"
   - Enter description: "Milk, bread, eggs"
3. Choose option 2 to view tasks:
   - You'll see: "1 [ ] Buy groceries - Milk, bread, eggs"
4. Choose option 5 to mark the task complete:
   - Enter ID: 1
   - The task status changes to [X]
5. Choose option 6 to exit the application

## Error Handling
- Invalid inputs are handled gracefully with specific, actionable error messages
- Attempting to operate on non-existent tasks will show appropriate error messages
- Input validation prevents empty titles and enforces character limits

## Limitations
- Data is stored only in memory and is lost when the application exits
- No persistent storage mechanism
- Single-user application for single-session usage