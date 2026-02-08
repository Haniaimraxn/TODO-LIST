"""
Module for managing todo tasks in memory.
"""


class TodoManager:
    """
    Manages a list of todo tasks in memory.
    """
    
    def __init__(self):
        """
        Initialize with empty task list and next_id counter.
        """
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title: str, description: str = "") -> dict:
        """
        Add a new task with validation and auto-ID assignment.
        """
        # Normalize and validate inputs
        title = self._normalize_text(title)
        description = self._normalize_text(description)
        
        self._validate_title(title)
        
        # Check description length
        if len(description) > 500:
            raise ValueError("Description cannot exceed 500 characters")
        
        # Create task with next available ID
        task_id = self._get_next_id()
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "complete": False  # Default to incomplete
        }
        
        # Add to tasks list
        self.tasks.append(task)
        
        # Update next_id to ensure we don't reuse IDs
        self.next_id = max(self.next_id, task_id + 1)
        
        return task
    
    def get_all_tasks(self) -> list:
        """
        Return all tasks in the list.
        """
        return self.tasks.copy()  # Return a copy to prevent external modification
    
    def get_task_by_id(self, task_id: int) -> dict:
        """
        Get a specific task by its ID, raises ValueError if not found.
        """
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        raise ValueError(f"Task with ID {task_id} does not exist")
    
    def update_task(self, task_id: int, title: str = None, 
                   description: str = None, complete: bool = None) -> dict:
        """
        Update specified fields of a task, returns updated task.
        """
        # Find the task to update
        task_index = None
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                task_index = i
                break
        
        if task_index is None:
            raise ValueError(f"Task with ID {task_id} does not exist")
        
        # Get the task to update
        task = self.tasks[task_index]
        
        # Update fields if provided
        if title is not None:
            title = self._normalize_text(title)
            self._validate_title(title)
            task['title'] = title
        
        if description is not None:
            description = self._normalize_text(description)
            if len(description) > 500:
                raise ValueError("Description cannot exceed 500 characters")
            task['description'] = description
        
        if complete is not None:
            task['complete'] = complete
        
        # Return the updated task
        return task.copy()
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID, returns True if successful.
        """
        # Find the task to delete
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                # Remove the task from the list
                del self.tasks[i]
                
                # Update next_id to ensure we don't reuse IDs
                # We need to find the highest ID currently in use
                if self.tasks:
                    max_id = max(t['id'] for t in self.tasks)
                    self.next_id = max(max_id + 1, task_id + 1)
                else:
                    # If no tasks remain, start from the next ID after the deleted one
                    self.next_id = task_id + 1
                
                return True
        
        # Task not found
        return False
    
    def toggle_task_status(self, task_id: int) -> dict:
        """
        Toggle the completion status of a task, returns updated task.
        """
        # Find the task to toggle
        task_index = None
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                task_index = i
                break
        
        if task_index is None:
            raise ValueError(f"Task with ID {task_id} does not exist")
        
        # Get the task and toggle its status
        task = self.tasks[task_index]
        task['complete'] = not task['complete']
        
        # Return the updated task
        return task.copy()
    
    def _validate_title(self, title: str) -> None:
        """
        Validate title meets requirements (not empty, length limit).
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if len(title.strip()) > 100:
            raise ValueError("Title cannot exceed 100 characters")
    
    def _normalize_text(self, text: str) -> str:
        """
        Normalize text by stripping whitespace.
        """
        if text is None:
            return ""
        return text.strip()
    
    def _get_next_id(self) -> int:
        """
        Get the next available ID (never reuse deleted IDs).
        """
        # Find the highest ID currently in use
        if not self.tasks:
            return self.next_id
        
        max_id = max(task['id'] for task in self.tasks)
        return max(max_id + 1, self.next_id)