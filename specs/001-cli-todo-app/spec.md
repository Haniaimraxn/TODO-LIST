# Feature Specification: CLI Todo Application

**Feature Branch**: `001-cli-todo-app`
**Created**: 2026-02-08
**Status**: Draft
**Input**: User description: "/sp.specify project: The Evolution of Todo phase: Phase I title: Todo In-Memory Python Console App short_name: cli-todo-app description: | A simple, interactive command-line todo list application that stores all tasks in memory only. The app must support basic task management operations through a text-based menu. No persistence (no files, no database), no external libraries beyond Python standard library. Focus on clean, modular code and proper error handling. features: - name: add description: Add a new task details: | User enters title (required) and description (optional). System automatically assigns a unique incremental ID starting from 1. Task is added to in-memory list with default status "incomplete". - name: view description: View all tasks details: | Display a numbered list of all tasks. Show: ID, status indicator ([X] for complete, [ ] for incomplete), title, description. If no tasks, show friendly message "No tasks yet." - name: update description: Update an existing task details: | User provides task ID. Allow updating any combination of: title, description, status. Fields are optional — only changed fields are updated. Show error if ID does not exist. - name: delete description: Delete a task details: | User provides task ID. Remove task from list. Show confirmation message or error if ID invalid. - name: mark_complete description: Toggle complete/incomplete status details: | User provides task ID. Toggle the complete status (incomplete → complete, complete → incomplete). Show updated status message. Error if ID not found. entities: - name: Task fields: - id: integer (unique, auto-increment) - title: string (required, non-empty) - description: string (optional, can be empty) - complete: boolean (default: false) storage: type: in-memory structure: list of Task dictionaries persistence: none — data resets on program exit tech_stack: - language: Python 3.13+ - environment: uv (for virtual environment and dependency management) - ai_assistant: qwen - toolkit: spec-kit-plus - dependencies: only Python standard library (no pip installs allowed) project_structure: - src/ - main.py: entry point with interactive CLI menu loop - todo_manager.py: class or functions handling all task operations (add, view, update, delete, mark_complete) constraints: - no_external_dependencies: true - coding_standards: PEP 8 compliant, type hints where helpful, docstrings for public functions - error_handling: validate all user inputs (especially IDs), graceful messages for invalid cases - test_strategy: test-first development (write tests before code for core functions) - cli_style: simple numbered menu (1. Add, 2. View, 3. Update, 4. Delete, 5. Toggle complete, 6. Exit) success_criteria: - All 5 features work correctly in a single run - Unique IDs are maintained - No crashes on invalid input - Clean separation between logic (todo_manager) and presentation (main CLI loop) - Code is readable, modular, and follows constitution principles edge_cases_to_consider: - Empty title attempt - Non-existent ID for update/delete/mark - No tasks when viewing - Toggling status multiple times - Very long title/description (should still handle gracefully)"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add New Tasks (Priority: P1)

As a user, I want to add new tasks to my todo list with a title and description so that I can keep track of what I need to do. The system assigns a unique ID to each task for future reference, starting from 1 and incrementing for each new task.

**Why this priority**: This is the foundational functionality that enables all other features - without the ability to add tasks, the app has no purpose.

**Independent Test**: The user can successfully add a new task with a title and description, and the system assigns it a unique ID that appears in the task list with an incomplete status [ ].

**Acceptance Scenarios**:

1. **Given** an empty todo list, **When** I add a new task with title "Buy groceries" and description "Milk, bread, eggs", **Then** the task appears in the list with ID 1 and status [ ].
2. **Given** I have existing tasks in the system, **When** I add another task, **Then** the new task gets the next sequential ID and appears in the list with status [ ].

---

### User Story 2 - View All Tasks (Priority: P1)

As a user, I want to view all my tasks with their IDs, titles, descriptions, and completion status so that I can see what I need to do and what I've completed.

**Why this priority**: Essential for user awareness of their tasks and progress - without viewing capabilities, users can't effectively manage their todo list.

**Independent Test**: The user can see a complete list of all tasks with their ID, status indicator ([X] for complete, [ ] for incomplete), title, and description. If no tasks exist, a friendly message "No tasks yet." is displayed.

**Acceptance Scenarios**:

1. **Given** I have multiple tasks in the system, **When** I request to view all tasks, **Then** all tasks appear with their ID, status indicator, title, and description.
2. **Given** I have no tasks in the system, **When** I request to view all tasks, **Then** the message "No tasks yet." is displayed.

---

### User Story 3 - Update Task Information (Priority: P2)

As a user, I want to update existing tasks by ID, changing the title, description, or status as needed so that I can keep my todo list accurate and current.

**Why this priority**: Allows for task refinement and maintenance, which is important for long-term usability but secondary to basic CRUD operations.

**Independent Test**: The user can update any combination of task properties (title, description, status) using the task's unique ID. Only the specified fields are updated, leaving others unchanged.

**Acceptance Scenarios**:

1. **Given** I have a task with ID 1, **When** I update its title to "Updated title", **Then** the task's title changes while other properties remain the same.
2. **Given** I have a task with ID 2, **When** I update multiple properties (title and description), **Then** both properties update correctly while others remain unchanged.

---

### User Story 4 - Delete Tasks (Priority: P2)

As a user, I want to remove tasks I no longer need by specifying their ID so that my todo list stays relevant and clutter-free.

**Why this priority**: Important for managing the todo list lifecycle, but not as critical as adding and viewing tasks.

**Independent Test**: The user can remove a specific task by its ID, and it disappears from the task list. An appropriate confirmation or error message is shown.

**Acceptance Scenarios**:

1. **Given** I have a task with ID 3, **When** I delete it, **Then** the task no longer appears in the task list and a confirmation message is shown.
2. **Given** I try to delete a non-existent task, **When** I specify an invalid ID, **Then** the system reports an error and no changes occur.

---

### User Story 5 - Mark Tasks Complete/Incomplete (Priority: P2)

As a user, I want to toggle the completion status of tasks by ID so that I can track my progress and mark what I've accomplished.

**Why this priority**: Core functionality for tracking progress, which is essential to the todo app concept.

**Independent Test**: The user can toggle a task's status from incomplete [ ] to complete [X] and vice versa using the task's ID.

**Acceptance Scenarios**:

1. **Given** I have an incomplete task with ID 1, **When** I mark it complete, **Then** its status changes from [ ] to [X] and an updated status message is shown.
2. **Given** I have a complete task with ID 2, **When** I mark it incomplete, **Then** its status changes from [X] to [ ] and an updated status message is shown.

### Edge Cases

- What happens when trying to update/delete a task with an invalid/non-existent ID?
- How does the system handle attempts to add a task with an empty title?
- How does the system handle attempts to add titles or descriptions that exceed length limits (title > 100 chars, description > 500 chars)?
- What occurs when the system tries to assign the next sequential ID?
- How does the system behave when toggling status multiple times?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add new tasks with a required title (max 100 chars, case-sensitive with normalized leading/trailing whitespace) and optional description (max 500 chars, case-sensitive with normalized leading/trailing whitespace), assigning each a unique incremental ID that continues incrementing from the highest used ID (no ID reuse even after deletion)
- **FR-002**: System MUST display all tasks with their ID, status indicator ([X] for complete, [ ] for incomplete), title, and description
- **FR-003**: System MUST display a friendly "No tasks yet." message when viewing an empty task list
- **FR-004**: Users MUST be able to update any combination of task properties (title, description, status) by specifying the task ID
- **FR-005**: System MUST allow deletion of tasks by specifying the task ID, but MUST require user confirmation before performing the deletion
- **FR-006**: System MUST provide a way to toggle task completion status by specifying the task ID
- **FR-007**: System MUST handle invalid task IDs gracefully with specific, actionable error messages (e.g., "Task with ID X does not exist")
- **FR-008**: System MUST prevent adding tasks with empty titles and provide specific error messages
- **FR-009**: System MUST store all tasks in memory only (no persistent storage)
- **FR-010**: System MUST use only Python standard library (no external dependencies)

### Key Entities

- **Task**: Represents a single todo item with id (integer, unique, auto-increment), title (string, required, non-empty, max 100 chars, case-sensitive with normalized leading/trailing whitespace), description (string, optional, can be empty, max 500 chars, case-sensitive with normalized leading/trailing whitespace), and complete (boolean, default: false)
- **TaskList**: Collection of Task objects stored in memory as a list of dictionaries

## Clarifications

### Session 2026-02-08

- Q: What are the maximum allowed lengths for task titles and descriptions? → A: Set reasonable length limits (title: 100 chars, description: 500 chars)
- Q: Should error messages be generic or specific and actionable? → A: Provide specific, actionable error messages
- Q: Should the system reuse IDs of deleted tasks? → A: Do not reuse IDs, continue incrementing from the highest used ID
- Q: Should task deletion require user confirmation? → A: Require user confirmation before deleting
- Q: How should the system handle case sensitivity and whitespace for task titles/descriptions? → A: Be case-sensitive but normalize leading/trailing whitespace

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All 5 features (add, view, update, delete, mark_complete) work correctly in a single run
- **SC-002**: Unique IDs are maintained and increment properly starting from 1
- **SC-003**: No crashes occur on invalid input, with graceful error handling
- **SC-004**: Clean separation exists between logic (todo_manager) and presentation (main CLI loop)
- **SC-005**: Code is readable, modular, follows PEP 8 standards, and includes type hints and docstrings where helpful
