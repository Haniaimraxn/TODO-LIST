# Tasks: CLI Todo Application

**Input**: Design documents from `/specs/001-cli-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan: mkdir src/ and tests/unit/ and tests/integration/
- [X] T002 Initialize Python project with basic configuration
- [X] T003 [P] Create src/todo_manager.py file with basic TodoManager class skeleton

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Implement TodoManager class skeleton in src/todo_manager.py with empty methods
- [X] T005 [P] Implement _validate_title() and _normalize_text() helper methods in src/todo_manager.py
- [X] T006 [P] Implement _get_next_id() method for ID management in src/todo_manager.py
- [X] T007 Create basic test file tests/unit/test_todo_manager.py with import statements

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with title and description, assigning unique IDs

**Independent Test**: The user can successfully add a new task with a title and description, and the system assigns it a unique ID that appears in the task list with an incomplete status [ ].

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T008 [P] [US1] Create test skeleton for add_task functionality in tests/unit/test_todo_manager.py
- [X] T009 [US1] Write test for valid task addition in tests/unit/test_todo_manager.py
- [X] T010 [US1] Write test for empty title validation in tests/unit/test_todo_manager.py
- [X] T011 [US1] Write test for title length validation in tests/unit/test_todo_manager.py

### Implementation for User Story 1

- [X] T012 [US1] Implement add_task() method in src/todo_manager.py with validation
- [X] T013 [US1] Implement get_all_tasks() method in src/todo_manager.py
- [X] T014 [US1] Implement get_task_by_id() method with error handling in src/todo_manager.py
- [X] T015 [US1] Add ID assignment logic to ensure unique incremental IDs in src/todo_manager.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to view all tasks with their IDs, titles, descriptions, and completion status

**Independent Test**: The user can see a complete list of all tasks with their ID, status indicator ([X] for complete, [ ] for incomplete), title, and description. If no tasks exist, a friendly message "No tasks yet." is displayed.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T016 [P] [US2] Create test skeleton for view tasks functionality in tests/unit/test_todo_manager.py
- [ ] T017 [US2] Write test for displaying multiple tasks in tests/unit/test_todo_manager.py
- [ ] T018 [US2] Write test for displaying empty list message in tests/unit/test_todo_manager.py

### Implementation for User Story 2

- [ ] T019 [US2] Enhance get_all_tasks() method to format output appropriately in src/todo_manager.py
- [ ] T020 [US2] Implement logic to display status indicators [X] or [ ] in src/todo_manager.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Information (Priority: P2)

**Goal**: Enable users to update existing tasks by ID, changing title, description, or status

**Independent Test**: The user can update any combination of task properties (title, description, status) using the task's unique ID. Only the specified fields are updated, leaving others unchanged.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T021 [P] [US3] Create test skeleton for update task functionality in tests/unit/test_todo_manager.py
- [X] T022 [US3] Write test for updating task title in tests/unit/test_todo_manager.py
- [X] T023 [US3] Write test for updating multiple fields in tests/unit/test_todo_manager.py

### Implementation for User Story 3

- [X] T024 [US3] Implement update_task() method in src/todo_manager.py
- [X] T025 [US3] Add validation for update operations in src/todo_manager.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Enable users to remove tasks by specifying their ID with confirmation

**Independent Test**: The user can remove a specific task by its ID, and it disappears from the task list. An appropriate confirmation or error message is shown.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T026 [P] [US4] Create test skeleton for delete task functionality in tests/unit/test_todo_manager.py
- [X] T027 [US4] Write test for successful task deletion in tests/unit/test_todo_manager.py
- [X] T028 [US4] Write test for deletion of non-existent task in tests/unit/test_todo_manager.py

### Implementation for User Story 4

- [X] T029 [US4] Implement delete_task() method in src/todo_manager.py
- [ ] T030 [US4] Add confirmation prompt logic for deletion in src/main.py
- [X] T031 [US4] Ensure ID management continues from highest used ID after deletion in src/todo_manager.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Enable users to toggle the completion status of tasks by ID

**Independent Test**: The user can toggle a task's status from incomplete [ ] to complete [X] and vice versa using the task's ID.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T032 [P] [US5] Create test skeleton for toggle status functionality in tests/unit/test_todo_manager.py
- [X] T033 [US5] Write test for toggling incomplete to complete in tests/unit/test_todo_manager.py
- [X] T034 [US5] Write test for toggling complete to incomplete in tests/unit/test_todo_manager.py

### Implementation for User Story 5

- [X] T035 [US5] Implement toggle_task_status() method in src/todo_manager.py
- [X] T036 [US5] Add status validation and update logic in src/todo_manager.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: CLI Integration

**Goal**: Implement the command-line interface to connect all features

- [X] T037 Create src/main.py file with basic structure
- [X] T038 [P] Implement CLI menu loop in src/main.py
- [X] T039 [P] Implement input handling for menu options in src/main.py
- [X] T040 Connect CLI functions to TodoManager methods in src/main.py
- [X] T041 Add error handling and user feedback in src/main.py
- [X] T042 Implement confirmation prompts for destructive operations in src/main.py

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T043 Add comprehensive error messages throughout the application
- [X] T044 [P] Write integration tests in tests/integration/test_cli_flow.py
- [X] T045 [P] Perform end-to-end testing of complete user workflows
- [X] T046 [P] Add input sanitization and additional validation
- [X] T047 Run all unit tests to ensure functionality
- [X] T048 [P] Code cleanup and documentation updates
- [X] T049 Final testing and debugging

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **CLI Integration (Phase 8)**: Depends on all core functionality being complete
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

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
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Add CLI Integration → Test end-to-end → Deploy/Demo
8. Each story adds value without breaking previous stories

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