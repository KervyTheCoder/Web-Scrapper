import os
from datetime import datetime

def is_valid_date(date_str):
    """Validate if the provided date string is in the correct format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu(options):
    """Displays a menu with numbered options."""
    print("\nPlease choose an option:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    return input("Your choice: ")

def confirm_action(prompt):
    """Asks the user for confirmation before performing an action."""
    confirmation = input(f"{prompt} (y/n): ").lower()
    return confirmation == 'y'

def format_task(task):
    """Formats a task for display."""
    status = '✔️' if task['status'] == 'complete' else '❌'
    return f"{task['description']} - Due: {task['due_date']} - Status: {status}"


