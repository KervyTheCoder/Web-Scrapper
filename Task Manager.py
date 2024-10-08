import json
import os
from datetime import datetime
from utils import is_valid_date, clear_screen, display_menu, confirm_action, format_task  # Import des utilitaires

# Constants
TASKS_FILE = 'tasks.json'

class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Loads tasks from the tasks.json file, or creates an empty list if the file doesn't exist."""
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        """Saves the current task list to the tasks.json file."""
        with open(TASKS_FILE, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description, due_date):
        """Adds a new task to the task list."""
        task = {
            'description': description,
            'due_date': due_date,
            'status': 'incomplete',
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{description}' added successfully!")

    def list_tasks(self):
        """Prints all tasks with their status and due date."""
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {format_task(task)}")  # Utilisation de format_task()

    def mark_task_complete(self, task_number):
        """Marks a task as complete."""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['status'] = 'complete'
            self.save_tasks()
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        """Deletes a task from the task list."""
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task '{removed_task['description']}' deleted successfully.")
        else:
            print("Invalid task number.")

def main():
    manager = TaskManager()

    while True:
        clear_screen()  # Efface l'écran pour rendre l'affichage propre
        options = ["Add Task", "List Tasks", "Mark Task as Complete", "Delete Task", "Exit"]
        choice = display_menu(options)  # Utilisation de display_menu()

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            if is_valid_date(due_date):  # Validation de la date
                manager.add_task(description, due_date)
            else:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to mark complete: "))
            if confirm_action("Are you sure you want to mark this task as complete?"):  # Confirmation avant action
                manager.mark_task_complete(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            if confirm_action("Are you sure you want to delete this task?"):  # Confirmation avant suppression
                manager.delete_task(task_number)
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")  # Pause avant de continuer

if __name__ == '__main__':
    main()
