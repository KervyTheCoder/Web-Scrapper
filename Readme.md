TASK MANAGER CLI 

■ Description

The Task Manager CLI is a simple command-line interface (CLI) application written in Python that allows users to manage their daily tasks efficiently. Users can add, list, mark as complete, and delete tasks directly from the terminal. Tasks are stored persistently in a `tasks.json` file.

■ Features

- Add new tasks with a description and due date.
- List all tasks with their status (complete/incomplete) and due dates.
- Mark tasks as complete.
- Delete tasks.
- Persistent storage of tasks using a JSON file.

■ Project Structure

The project is organized as follows:


task-manager-cli/
│
├── tasks.json          # Stores tasks in JSON format (auto-generated)
├── task_manager.py     # Main application logic
├── utils.py            # Helper functions used across the project
└── README.md           # Project documentation (this file)


■ Requirements

To run this project, you will need the following installed:

- Python 3.x

■ Installation

1. Clone this repository to your local machine:

   git clone https://github.com/your-username/task-manager-cli.git
   cd task-manager-cli
   

2. No additional dependencies are required since the project uses standard Python libraries (`json`, `datetime`, `os`).

■ Usage

1. Run the application:

   ● python task_manager.py
   

2. You will be presented with a menu to manage your tasks. Choose an option by typing the corresponding number and following the prompts.

■ Example Menu:


● Please choose an option:
1. Add Task
2. List Tasks
3. Mark Task as Complete
4. Delete Task
5. Exit
`

● Example of Adding a Task:


Enter task description: Write the project report
Enter due date (YYYY-MM-DD): 2024-09-15
Task 'Write the project report' added successfully!


■ How Tasks are Stored

All tasks are stored in the `tasks.json` file in the following format:

[
    {
        "description": "Write the project report",
        "due_date": "2024-09-15",
        "status": "incomplete",
        "created_at": "2024-09-06 10:35:21"
    },
    {
        "description": "Prepare for meeting",
        "due_date": "2024-09-10",
        "status": "complete",
        "created_at": "2024-09-06 11:00:00"
    }
]


■ Future Improvements

Here are some features that can be added in future versions:

- Edit an existing task.
- Add priority levels for tasks (low, medium, high).
- Sort tasks by due date or priority.
- Set reminders for tasks.

■ Contribution

Contributions are welcome! To contribute:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:
   ● git checkout -b feature-name
   
3. Commit your changes:
   ● git commit -m "Add some feature"
   
4. Push to the branch:
   ● git push origin feature-name
   
5. Open a pull request.

■  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by Cadet John Kervensley 
