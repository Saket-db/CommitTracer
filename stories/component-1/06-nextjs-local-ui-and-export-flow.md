# Story 6 - Next.js Local UI and Export Flow

## Objective
Build a local Next.js interface for downloading the collector script, uploading JSON, validating the export, and previewing the report.

## Why this matters
A local UI makes the workflow usable for non-technical users and gives clear feedback during download, upload, validate, and report steps.

## Scope
- Create a Next.js local frontend.
- Add screens for download, upload, validation, and report preview.
- Consume only the Flask backend API.
- Show user-friendly errors and progress states.
- Keep presentation logic separate from data-fetching logic.

## Non-goals
- No analytics dashboard.
- No AI inference.
- No public hosting concerns.

## Design Constraints
- Keep UI components small and composable.
- Move shared formatting and state logic into hooks or utilities.
- Keep all data mutations behind the backend API.
- Ensure the UI can scale from a few commits to large syncs without blocking.

## Implementation Notes
- Use a clean local-first UX with explicit state transitions.
- Add preview counts and report summaries so users know what was uploaded.
- Keep API hooks and presentation components separate.
- Use loading and error states for each distinct workflow step.

## Acceptance Criteria
- The user can download the collector script from the UI.
- The user can upload exported JSON and see validation results.
- The user can preview report data before saving or sharing.
- The user can see a generated heatmap or summary report.
- UI tests cover the main workflow states.

## Dependencies
- Story 1
- Story 2
- Story 3
- Story 4
- Story 5

## Output of this story
A usable local frontend that completes the collector and report workflow end to end.
