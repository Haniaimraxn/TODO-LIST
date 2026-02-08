# Data Model: CLI Todo Application

## Overview
This document defines the data structures and relationships for the CLI Todo Application.

## Entity Definitions

### Task
Represents a single todo item with the following attributes:

- **id**: integer (unique, auto-increment)
  - Automatically assigned when a new task is created
  - Starts from 1 and increments for each new task
  - Never reused even after deletion (continues from highest used ID)
  
- **title**: string (required, non-empty, max 100 chars)
  - Case-sensitive with normalized leading/trailing whitespace
  - Cannot be empty (validation required)
  - Maximum length of 100 characters
  
- **description**: string (optional, can be empty, max 500 chars)
  - Case-sensitive with normalized leading/trailing whitespace
  - Can be empty or omitted when creating a task
  - Maximum length of 500 characters
  
- **complete**: boolean (default: false)
  - Indicates whether the task is completed or not
  - Default value is false when a new task is created
  - Can be toggled using the mark_complete feature

### TaskList
Collection of Task objects stored in memory as a list of dictionaries:

- **tasks**: list of Task objects
  - Maintains all tasks in memory during the session
  - Provides methods for CRUD operations on tasks
  - Tracks the highest assigned ID for proper incrementation

## Relationships
- Each Task object exists independently within the TaskList
- TaskList manages the collection and provides operations on the tasks

## Validation Rules
- Task title must be between 1 and 100 characters (inclusive)
- Task description must be between 0 and 500 characters (inclusive)
- Task title cannot be empty or consist only of whitespace
- Task ID must be unique within the TaskList
- Task ID must be positive integer

## State Transitions
- A Task starts with `complete: false`
- A Task can transition from `complete: false` to `complete: true` via mark_complete feature
- A Task can transition from `complete: true` to `complete: false` via mark_complete feature
- A Task is removed from TaskList when deleted