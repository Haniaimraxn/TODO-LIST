"""
Unit tests for the TodoManager class.
"""
import sys
import os
# Add src to the path so we can import todo_manager
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from todo_manager import TodoManager


def test_todo_manager_import():
    """
    Basic test to ensure TodoManager can be imported and instantiated.
    """
    tm = TodoManager()
    assert tm is not None
    assert hasattr(tm, 'tasks')
    assert hasattr(tm, 'next_id')


def test_add_task_valid_input():
    """
    Verify task is added with correct properties.
    """
    tm = TodoManager()
    task = tm.add_task("Test Title", "Test Description")
    
    assert task is not None
    assert task['id'] == 1
    assert task['title'] == "Test Title"
    assert task['description'] == "Test Description"
    assert task['complete'] is False


def test_add_task_empty_title():
    """
    Verify ValueError raised for empty titles.
    """
    tm = TodoManager()
    try:
        tm.add_task("")
        assert False, "Expected ValueError for empty title"
    except ValueError as e:
        assert "Title cannot be empty" in str(e)


def test_add_task_long_inputs():
    """
    Verify length validation works.
    """
    tm = TodoManager()
    long_title = "A" * 101  # 101 characters, exceeding the 100 limit
    try:
        tm.add_task(long_title)
        assert False, "Expected ValueError for long title"
    except ValueError as e:
        assert "Title cannot exceed 100 characters" in str(e)
    
    # Test long description
    long_description = "A" * 501  # 501 characters, exceeding the 500 limit
    try:
        tm.add_task("Valid Title", long_description)
        assert False, "Expected ValueError for long description"
    except ValueError as e:
        assert "Description cannot exceed 500 characters" in str(e)


def test_get_task_by_id():
    """
    Verify retrieving existing and non-existing tasks.
    """
    tm = TodoManager()
    # Add a task first
    task = tm.add_task("Test Task", "Test Description")
    task_id = task['id']
    
    # Retrieve the task
    retrieved_task = tm.get_task_by_id(task_id)
    assert retrieved_task == task
    
    # Try to retrieve a non-existing task
    try:
        tm.get_task_by_id(999)
        assert False, "Expected ValueError for non-existing task"
    except ValueError as e:
        assert "Task with ID 999 does not exist" in str(e)


def test_update_task_functionality():
    """
    Verify update task functionality works correctly.
    """
    tm = TodoManager()
    # Add a task first
    original_task = tm.add_task("Original Title", "Original Description")
    task_id = original_task['id']
    
    # Verify original task
    assert original_task['title'] == "Original Title"
    assert original_task['description'] == "Original Description"
    assert original_task['complete'] is False
    
    # Update the task title
    updated_task = tm.update_task(task_id, title="Updated Title")
    assert updated_task['title'] == "Updated Title"
    assert updated_task['description'] == "Original Description"  # Should remain unchanged
    assert updated_task['complete'] is False  # Should remain unchanged
    
    # Update multiple fields
    updated_task2 = tm.update_task(task_id, description="Updated Description", complete=True)
    assert updated_task2['title'] == "Updated Title"  # Should remain unchanged
    assert updated_task2['description'] == "Updated Description"
    assert updated_task2['complete'] is True


def test_update_nonexistent_task():
    """
    Verify updating a non-existent task raises an error.
    """
    tm = TodoManager()
    try:
        tm.update_task(999, title="New Title")
        assert False, "Expected ValueError for non-existent task"
    except ValueError as e:
        assert "Task with ID 999 does not exist" in str(e)


def test_delete_task_functionality():
    """
    Verify successful task deletion.
    """
    tm = TodoManager()
    # Add a task first
    original_task = tm.add_task("Task to Delete", "Description to Delete")
    task_id = original_task['id']
    
    # Verify task exists
    assert len(tm.get_all_tasks()) == 1
    assert tm.get_task_by_id(task_id) is not None
    
    # Delete the task
    result = tm.delete_task(task_id)
    assert result is True
    
    # Verify task is gone
    assert len(tm.get_all_tasks()) == 0
    try:
        tm.get_task_by_id(task_id)
        assert False, "Expected ValueError for deleted task"
    except ValueError:
        pass  # Expected


def test_delete_nonexistent_task():
    """
    Verify deletion of non-existent task returns False.
    """
    tm = TodoManager()
    result = tm.delete_task(999)
    assert result is False  # Should return False for non-existent task


def test_toggle_task_status_functionality():
    """
    Verify toggling incomplete to complete.
    """
    tm = TodoManager()
    # Add a task first
    original_task = tm.add_task("Task to Toggle", "Description")
    task_id = original_task['id']
    
    # Verify task starts as incomplete
    assert original_task['complete'] is False
    
    # Toggle to complete
    toggled_task = tm.toggle_task_status(task_id)
    assert toggled_task['complete'] is True
    
    # Toggle back to incomplete
    toggled_back_task = tm.toggle_task_status(task_id)
    assert toggled_back_task['complete'] is False


def test_toggle_nonexistent_task():
    """
    Verify toggling non-existent task raises an error.
    """
    tm = TodoManager()
    try:
        tm.toggle_task_status(999)
        assert False, "Expected ValueError for non-existent task"
    except ValueError as e:
        assert "Task with ID 999 does not exist" in str(e)


if __name__ == "__main__":
    test_todo_manager_import()
    print("Basic import test passed!")
    
    test_add_task_valid_input()
    print("Add task with valid input test passed!")
    
    test_add_task_empty_title()
    print("Add task with empty title test passed!")
    
    test_add_task_long_inputs()
    print("Add task with long inputs test passed!")
    
    test_get_task_by_id()
    print("Get task by ID test passed!")
    
    test_update_task_functionality()
    print("Update task functionality test passed!")
    
    test_update_nonexistent_task()
    print("Update nonexistent task test passed!")
    
    test_delete_task_functionality()
    print("Delete task functionality test passed!")
    
    test_delete_nonexistent_task()
    print("Delete nonexistent task test passed!")
    
    test_toggle_task_status_functionality()
    print("Toggle task status functionality test passed!")
    
    test_toggle_nonexistent_task()
    print("Toggle nonexistent task test passed!")
    
    print("All tests passed!")