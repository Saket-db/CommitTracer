# Story 1 - Foundation and Architecture

## Objective
Establish the local-first Component 1 codebase with clear boundaries for a collector script, a Flask backend for upload/reporting, and a Next.js frontend for download/upload/report preview.

## Why this matters
This story creates the structural baseline that keeps the extractor scalable. It prevents the codebase from collapsing into one large script and sets the pattern for short, composable functions.

## Scope
- Define the repository layout for backend, frontend, shared contracts, tools, and tests.
- Choose the runtime shape for local execution.
- Define the API boundary between the collector script, the Flask backend, and the Next.js frontend.
- Establish the domain boundaries for collection, normalization, schema validation, fingerprinting, and reporting.
- Set engineering conventions for small functions, typed DTOs, and layered modules.

## Non-goals
- No GitLab API calls yet.
- No schema export logic yet.
- No signing logic yet.
- No UI polish beyond the structural shell.

## Design Constraints
- Keep all functions under 60 lines.
- Avoid circular imports by splitting domain, service, adapter, and presentation layers.
- Prefer dependency injection over hidden globals.
- Keep secrets and tokens out of frontend state.
- Treat the local app as privacy-sensitive from the start.

## Implementation Notes
- Flask should expose a small JSON API for health, download script, upload validation, and report generation.
- Next.js should consume only those local APIs and avoid direct GitLab access.
- Shared contract files should define request and response shapes for the export JSON.
- Any parsing or transformation logic should live outside route handlers.

## Acceptance Criteria
- The repository has a documented folder structure.
- The collector script, backend app, and frontend entry points are defined.
- The module boundaries are documented.
- The code style rule for function length is recorded and enforced by convention.
- A new contributor can understand where each responsibility belongs.

## Suggested File Map
- `backend/` Flask app and services
- `tools/` downloadable collector script and local helpers
- `frontend/` Next.js app
- `shared/` shared schema and DTO definitions
- `tests/` backend and contract tests
- `docs/` product and implementation notes

## Dependencies
- None

## Output of this story
A clear scaffold that later stories can build on without refactoring the whole repository.
