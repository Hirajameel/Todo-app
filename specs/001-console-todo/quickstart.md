# Quickstart Guide: Console Todo Application

## Prerequisites
- Python 3.13+ installed
- `uv` package manager installed

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Run the application:
   ```bash
   uv run python src/main.py
   ```

## Usage

### Available Commands
- `add "Task title"` - Add a new task
- `list` - View all tasks
- `update <id> "New title"` - Update a task's title
- `toggle <id>` - Mark a task as complete/incomplete
- `delete <id>` - Remove a task
- `help` - Show available commands
- `quit` or `exit` - Exit the application

### Menu Options (Interactive Mode)
- Add task
- View tasks
- Update task
- Delete task
- Mark complete/incomplete
- Exit

### Example Workflow
```bash
# Add tasks
> add "Buy groceries"
Task added with ID: 1

# View all tasks
> list
1. [ ] Buy groceries

# Mark task as complete
> toggle 1
Task 1 marked as complete

# View updated list
> list
1. [x] Buy groceries

# Exit application
> quit
```

## Development

### Running Tests
```bash
uv run pytest
```

### Running with Type Checking
```bash
uv run mypy src/
```

### Code Formatting
```bash
uv run black src/
```