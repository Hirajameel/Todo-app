# Data Model: Console Todo Application

## Task Model

### Attributes
- **id**: `str` - Unique identifier for the task (numeric string or UUID)
- **title**: `str` - Non-empty string representing the task description
- **status**: `str` - Task completion status ("pending" or "completed")

### Constraints
- Title must not be empty or contain only whitespace
- ID must be unique within the application session
- Status can only be "pending" or "completed"

## Task Manager Model

### Attributes
- **tasks**: `dict[str, Task]` - Dictionary mapping task IDs to Task objects
- **next_id**: `int` - Counter for generating unique numeric IDs

### Operations
- **add_task(title: str) -> str**: Creates a new task and returns its ID (for "Add task" menu option)
- **get_all_tasks() -> list[Task]**: Returns all tasks in creation order (for "View tasks" menu option)
- **get_task(task_id: str) -> Task | None**: Retrieves a specific task by ID
- **update_task(task_id: str, title: str) -> bool**: Updates a task's title (for "Update task" menu option)
- **toggle_task(task_id: str) -> bool**: Toggles a task's completion status (for "Mark complete/incomplete" menu option)
- **delete_task(task_id: str) -> bool**: Removes a task from storage (for "Delete task" menu option)

### Constraints
- All operations must maintain data consistency
- Invalid operations must return appropriate status without modifying state
- Error conditions must be handled gracefully