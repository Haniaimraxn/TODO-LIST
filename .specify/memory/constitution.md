<!-- SYNC IMPACT REPORT
Version change: N/A (new constitution) → 1.0.0
Modified principles: None (new constitution)
Added sections: All sections (new constitution)
Removed sections: None
Templates requiring updates: 
  - ✅ .specify/templates/plan-template.md - Updated to reflect new principles
  - ✅ .specify/templates/spec-template.md - Updated to reflect new principles  
  - ✅ .specify/templates/tasks-template.md - Updated to reflect new principles
Follow-up TODOs: None
-->
# Todo In-Memory Python Console App Constitution

## Core Principles

### I. Minimalist Design
Every feature must serve a clear user need; implementations should be as simple as possible while maintaining functionality; unnecessary complexity is forbidden.

### II. CLI-First Interface
All functionality must be accessible through a command-line interface; text-based input/output protocols ensure maximum compatibility and debuggability; support both human-readable and structured (JSON) output formats.

### III. Test-First Development (NON-NEGOTIABLE)
All features must have tests written before implementation; TDD cycle strictly enforced: write tests → ensure they fail → implement feature → make tests pass → refactor as needed.

### IV. Memory-Only Storage
Data persistence limited to in-memory structures (lists, dictionaries); no external databases or file storage; focus on core functionality without persistence complexity.

### V. Clean Code Standards
All code must comply with PEP8 standards; modular architecture with clear separation of concerns; comprehensive error handling for all user inputs and operations.

### VI. Dependency Restraint
No external dependencies beyond Python 3.13+ standard library; all functionality implemented using built-in modules only; maintain maximum portability and simplicity.

## Additional Constraints

Technology Stack: Python 3.13+, uv environment manager, Qwen AI assistance, Spec Kit Plus toolkit
Project Structure: src/main.py (CLI entry point), src/todo_manager.py (core logic)
Storage: In-memory list of dictionaries for task management
Features: Add/view/update/delete/mark_complete tasks with ID, title, description, and status

## Development Workflow

Code Review: All changes must pass automated checks for PEP8 compliance and test coverage
Quality Gates: All tests must pass, code must be clean and well-documented
Testing: Unit tests for all core functions, integration tests for CLI interactions

## Governance

This constitution governs all development practices for the Todo In-Memory Python Console App; all PRs and reviews must verify compliance with these principles; amendments require documentation and approval following the established versioning policy.

**Version**: 1.0.0 | **Ratified**: 2026-02-08 | **Last Amended**: 2026-02-08