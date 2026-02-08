"""
Integration tests for the CLI Todo Application.
"""
import sys
import os
# Add src to the path so we can import todo_manager
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from todo_manager import TodoManager


def test_end_to_end_workflow():
    """
    Test a complete end-to-end workflow.
    """
    tm = TodoManager()
    
    # Add a few tasks
    task1 = tm.add_task("First Task", "Description for first task")
    task2 = tm.add_task("Second Task", "Description for second task")
    
    # Verify tasks were added
    all_tasks = tm.get_all_tasks()
    assert len(all_tasks) == 2
    
    # Update a task
    updated_task = tm.update_task(task1['id'], title="Updated First Task", complete=True)
    assert updated_task['title'] == "Updated First Task"
    assert updated_task['complete'] is True
    
    # Toggle status
    toggled_task = tm.toggle_task_status(task2['id'])
    assert toggled_task['complete'] is True
    
    # Delete a task
    result = tm.delete_task(task1['id'])
    assert result is True
    
    # Verify only one task remains
    remaining_tasks = tm.get_all_tasks()
    assert len(remaining_tasks) == 1
    
    print("End-to-end workflow test passed!")


if __name__ == "__main__":
    test_end_to_end_workflow()
    print("Integration test passed!")