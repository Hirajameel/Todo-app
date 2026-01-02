# Console Todo Application

A simple command-line interface (CLI) todo application built with Python.

## Features

- Add new tasks
- View all tasks
- Update task titles
- Delete tasks
- Mark tasks as complete/incomplete
- Input validation and error handling

## Requirements

- Python 3.13 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Hirajameel/Todo-app.git
```

2. Navigate to the project directory:
```bash
cd Todo-app
```

## Usage

Run the application:
```bash
python src/main.py
```

The application will display a menu with the following options:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark tasks complete
6. Exit

## Project Structure

```
src/
├── main.py                 # Main application entry point
├── models/
│   └── task.py            # Task data model
├── core/
│   └── manager.py         # TodoManager with CRUD operations
└── cli/
    └── menu.py            # CLI interface
```

## Tests

Run the tests:
```bash
python -m pytest tests/
```

## License

This project is open source and available under the MIT License.