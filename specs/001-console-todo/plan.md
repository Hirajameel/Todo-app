# Implementation Plan: Console Todo Application (Phase 1)

**Branch**: `001-console-todo` | **Date**: 2026-01-02 | **Spec**: [specs/001-console-todo/spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-console-todo/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a CLI-based Python todo application with in-memory storage supporting core CRUD operations (Add, View, Update, Delete, Mark Complete). The application will follow Python 3.13+ standards with type hints, Google-style docstrings, and proper error handling.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None required beyond standard library (with uv for dependency management)
**Storage**: In-memory only using Python dict/list structures
**Testing**: pytest for unit and integration testing
**Target Platform**: Cross-platform CLI application (Windows, macOS, Linux)
**Project Type**: Single CLI application
**Performance Goals**: Fast response times (<100ms for all operations), minimal memory usage
**Constraints**: <200ms response time for all operations, no persistent storage, <50MB memory usage
**Scale/Scope**: Single-user application, up to 10,000 tasks in memory

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Based on project constitution requirements for type-safe state management, Python 3.13+ with type hints will be used. The modular architecture with separate CLI and logic modules will be implemented as specified.

## Project Structure

### Documentation (this feature)

```text
specs/001-console-todo/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── models/
│   └── task.py          # Task data model with ID, title, status
├── core/
│   └── manager.py       # TodoManager with CRUD operations
├── cli/
│   └── menu.py          # Interactive CLI menu loop and command parsing
└── main.py              # Application entry point and menu controller

tests/
├── unit/
│   ├── test_models/
│   │   └── test_task.py
│   └── test_core/
│       └── test_manager.py
├── integration/
│   └── test_cli.py
└── conftest.py

pyproject.toml
README.md
```

**Structure Decision**: Single project structure selected to match the specified modular architecture. The application will have a clear separation of concerns with models in `src/models/`, business logic in `src/core/`, and CLI interface in `src/cli/`. The main entry point will be in `src/main.py`.

## Implementation Tasks

### Task T-1.1: Initialize project with uv init
- Create pyproject.toml with project metadata
- Set up Python 3.13+ requirement
- Configure basic dependencies
- Initialize git repository structure

### Task T-1.2: Create folder structure: src/models/, src/core/, src/cli/
- Create the required directory structure
- Add __init__.py files where needed
- Set up basic project organization

### Task T-1.3: Define Task model in src/models/task.py (UUID, title, status)
- Create Task data class with ID, title, and status attributes
- Implement proper type hints
- Add Google-style docstrings
- Include validation for non-empty titles
- Ensure proper status management (pending/completed)

### Task T-1.4: Implement TodoManager in src/core/manager.py with CRUD methods
- Implement add(title) method with unique ID generation
- Implement list() method to return all tasks
- Implement update(id, title) method with validation
- Implement delete(id) method
- Implement toggle(id) method to mark tasks complete/incomplete
- Add proper error handling for invalid operations
- Include comprehensive docstrings and type hints

### Task T-1.5: Create interactive CLI loop in src/main.py with error handling
- Implement main CLI menu loop with options: Add task, View tasks, Update task, Delete task, Mark complete/incomplete, Exit
- Create commands for add, list, update, delete, toggle (corresponding to menu options)
- Add proper error handling and user-friendly messages
- Implement interactive loop for continuous operation (while True menu)
- Include input validation and user feedback
- Display menu options clearly to guide user interaction

### Task T-1.6: Verify Type hints, PEP 8, and Docstrings across all files
- Run linters (flake8, mypy) to validate code quality
- Ensure all functions have proper type hints
- Verify Google-style docstrings are present
- Confirm PEP 8 compliance across all modules

## Quality Assurance Plan

- Unit tests for all model and core logic functions
- Integration tests for CLI functionality
- Error handling verification for edge cases
- Type checking validation with mypy
- Code style verification with flake8

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| In-memory only storage | Requirement specifies strictly in-memory for this phase | Persistent storage would add unnecessary complexity for Phase 1 |
| Modular architecture | Requirement specifies modular structure for maintainability | Single-file implementation would not meet architectural requirements |