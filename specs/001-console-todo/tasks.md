---
description: "Task list for Console Todo Application implementation"
---

# Tasks: Console Todo Application (Phase 1)

**Input**: Design documents from `/specs/001-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Tests**: Unit and integration tests will be included per quality assurance plan.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize Python project with uv and pyproject.toml
- [x] T002 Create project structure: src/, tests/, src/models/, src/core/, src/cli/
- [x] T003 [P] Create __init__.py files in src/ directories
- [x] T004 Configure development dependencies (pytest, mypy, black, flake8)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create Task data model with type hints and validation in src/models/task.py
- [x] T006 Create TodoManager with in-memory storage in src/core/manager.py
- [x] T007 [P] Configure project dependencies in pyproject.toml
- [x] T008 [P] Set up basic configuration and constants

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list with unique IDs and non-empty titles

**Independent Test**: Can be fully tested by adding a new task via the CLI and verifying it appears in the list, delivering core value of task creation.

### Implementation for User Story 1

- [x] T009 [P] [US1] Implement add_task method in src/core/manager.py with validation
- [x] T010 [P] [US1] Create CLI command handler for adding tasks in src/cli/menu.py
- [x] T011 [US1] Add task addition functionality to main menu loop in src/main.py
- [x] T012 [US1] Implement error handling for empty titles in src/models/task.py
- [x] T013 [US1] Add unit tests for task creation in tests/unit/test_models/test_task.py
- [x] T014 [US1] Add integration tests for add functionality in tests/integration/test_cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to view all tasks in their todo list with ID, title, and completion status

**Independent Test**: Can be fully tested by viewing the list of tasks and verifying all tasks are displayed with their status, delivering core value of task visibility.

### Implementation for User Story 2

- [ ] T015 [P] [US2] Implement get_all_tasks method in src/core/manager.py
- [ ] T016 [P] [US2] Create CLI command handler for listing tasks in src/cli/menu.py
- [ ] T017 [US2] Add task listing functionality to main menu loop in src/main.py
- [ ] T018 [US2] Implement proper display formatting for tasks in src/models/task.py
- [ ] T019 [US2] Add unit tests for task listing in tests/unit/test_core/test_manager.py
- [ ] T020 [US2] Add integration tests for list functionality in tests/integration/test_cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks Complete (Priority: P2)

**Goal**: Enable users to mark tasks as complete/incomplete to track their progress

**Independent Test**: Can be fully tested by marking a task as complete and verifying its status changes, delivering value of task status management.

### Implementation for User Story 3

- [ ] T021 [P] [US3] Implement toggle_task method in src/core/manager.py
- [ ] T022 [P] [US3] Create CLI command handler for toggling tasks in src/cli/menu.py
- [ ] T023 [US3] Add task toggle functionality to main menu loop in src/main.py
- [ ] T024 [US3] Add error handling for invalid task IDs in src/core/manager.py
- [ ] T025 [US3] Add unit tests for task toggle in tests/unit/test_core/test_manager.py
- [ ] T026 [US3] Add integration tests for toggle functionality in tests/integration/test_cli.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Enable users to update task details to correct mistakes or modify task information

**Independent Test**: Can be fully tested by updating a task's title and verifying the change persists, delivering value of task maintenance.

### Implementation for User Story 4

- [ ] T027 [P] [US4] Implement update_task method in src/core/manager.py with validation
- [ ] T028 [P] [US4] Create CLI command handler for updating tasks in src/cli/menu.py
- [ ] T029 [US4] Add task update functionality to main menu loop in src/main.py
- [ ] T030 [US4] Add validation for non-empty titles in src/core/manager.py
- [ ] T031 [US4] Add unit tests for task update in tests/unit/test_core/test_manager.py
- [ ] T032 [US4] Add integration tests for update functionality in tests/integration/test_cli.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P2)

**Goal**: Enable users to delete tasks to remove items that are no longer relevant

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears in the list, delivering value of list management.

### Implementation for User Story 5

- [ ] T033 [P] [US5] Implement delete_task method in src/core/manager.py
- [ ] T034 [P] [US5] Create CLI command handler for deleting tasks in src/cli/menu.py
- [ ] T035 [US5] Add task delete functionality to main menu loop in src/main.py
- [ ] T036 [US5] Add error handling for non-existent tasks in src/core/manager.py
- [ ] T037 [US5] Add unit tests for task deletion in tests/unit/test_core/test_manager.py
- [ ] T038 [US5] Add integration tests for delete functionality in tests/integration/test_cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T039 [P] Add comprehensive docstrings following Google style in all modules
- [ ] T040 [P] Implement consistent error handling across all modules
- [ ] T041 [P] Add input validation and sanitization in src/cli/menu.py
- [ ] T042 [P] Add type checking validation with mypy
- [ ] T043 [P] Run code formatting with black on src/ directory
- [ ] T044 [P] Add comprehensive logging for user actions
- [ ] T045 Run linter checks with flake8
- [ ] T046 Test application end-to-end using quickstart.md scenarios

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before CLI interface
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement add_task method in src/core/manager.py with validation"
Task: "Create CLI command handler for adding tasks in src/cli/menu.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence