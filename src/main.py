"""
Main CLI interface for the Todo Application.
"""
from todo_manager import TodoManager


def display_menu():
    """
    Display the main menu options.
    """
    print("\nCLI Todo Application")
    print("====================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print("Choose an option (1-6): ", end="")


def get_user_choice():
    """
    Get and validate user menu choice.
    """
    try:
        choice = int(input().strip())
        if 1 <= choice <= 6:
            return choice
        else:
            print("Please select a valid option (1-6)")
            return None
    except ValueError:
        print("Please enter a number between 1 and 6")
        return None


def add_task_ui(todo_manager):
    """
    UI for adding a new task.
    """
    print("\n--- Add New Task ---")
    title = input("Enter task title: ").strip()
    
    if not title:
        print("Title cannot be empty")
        return
    
    if len(title) > 100:
        print("Title cannot exceed 100 characters")
        return
    
    description = input("Enter task description (optional): ").strip()
    
    if len(description) > 500:
        print("Description cannot exceed 500 characters")
        return
    
    try:
        task = todo_manager.add_task(title, description)
        print(f"Task added successfully with ID {task['id']}")
    except ValueError as e:
        print(f"Error: {e}")


def view_tasks_ui(todo_manager):
    """
    UI for viewing all tasks.
    """
    print("\n--- View Tasks ---")
    tasks = todo_manager.get_all_tasks()
    
    if not tasks:
        print("No tasks yet.")
        return
    
    for task in tasks:
        status = "[X]" if task['complete'] else "[ ]"
        print(f"{task['id']}. {status} {task['title']} - {task['description']}")


def update_task_ui(todo_manager):
    """
    UI for updating a task.
    """
    print("\n--- Update Task ---")
    try:
        task_id = int(input("Enter task ID to update: ").strip())
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    print("Leave fields empty to keep current values.")
    new_title = input(f"Enter new title (current: '{todo_manager.get_task_by_id(task_id)['title']}'): ").strip()
    new_description = input(f"Enter new description (current: '{todo_manager.get_task_by_id(task_id)['description']}'): ").strip()
    
    # Handle status separately
    current_status = todo_manager.get_task_by_id(task_id)['complete']
    status_input = input(f"Change status? Current: {'Complete' if current_status else 'Incomplete'} (y/n): ").strip().lower()
    
    # Prepare update parameters
    update_params = {}
    if new_title:
        update_params['title'] = new_title
    if new_description:
        update_params['description'] = new_description
    if status_input in ['y', 'yes']:
        update_params['complete'] = not current_status
    
    if not update_params:
        print("No changes to make.")
        return
    
    try:
        updated_task = todo_manager.update_task(task_id, **update_params)
        print(f"Task {task_id} updated successfully")
    except ValueError as e:
        print(f"Error: {e}")


def delete_task_ui(todo_manager):
    """
    UI for deleting a task with confirmation.
    """
    print("\n--- Delete Task ---")
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    try:
        task = todo_manager.get_task_by_id(task_id)
        print(f"You are about to delete task: {task['title']}")
        confirm = input("Are you sure? (y/N): ").strip().lower()
        
        if confirm in ['y', 'yes']:
            result = todo_manager.delete_task(task_id)
            if result:
                print(f"Task {task_id} deleted successfully")
            else:
                print("Task deletion failed")
        else:
            print("Deletion cancelled")
    except ValueError as e:
        print(f"Error: {e}")


def toggle_task_status_ui(todo_manager):
    """
    UI for toggling task status.
    """
    print("\n--- Toggle Task Status ---")
    try:
        task_id = int(input("Enter task ID to toggle: ").strip())
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return
    
    try:
        task = todo_manager.get_task_by_id(task_id)
        current_status = "Complete" if task['complete'] else "Incomplete"
        new_status = "Incomplete" if task['complete'] else "Complete"
        
        print(f"Toggling task '{task['title']}' from {current_status} to {new_status}")
        
        updated_task = todo_manager.toggle_task_status(task_id)
        new_status_indicator = "[X]" if updated_task['complete'] else "[ ]"
        print(f"Task {task_id} status updated to {new_status_indicator}")
    except ValueError as e:
        print(f"Error: {e}")


def main():
    """
    Main application loop.
    """
    todo_manager = TodoManager()
    
    print("Welcome to the CLI Todo Application!")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice is None:
            continue  # Invalid input, show menu again
        
        if choice == 1:
            add_task_ui(todo_manager)
        elif choice == 2:
            view_tasks_ui(todo_manager)
        elif choice == 3:
            update_task_ui(todo_manager)
        elif choice == 4:
            delete_task_ui(todo_manager)
        elif choice == 5:
            toggle_task_status_ui(todo_manager)
        elif choice == 6:
            print("Exiting the application. Goodbye!")
            break


if __name__ == "__main__":
    main()