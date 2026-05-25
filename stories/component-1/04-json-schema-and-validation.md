# Story 4 - JSON Schema and Validation

## Objective
Define and enforce the Component 1 export schema so the JSON output is stable, versioned, and safe to upload later.

## Why this matters
The schema is the contract between the local collector and the platform upload flow. Without strong validation, the output becomes hard to trust and hard to evolve.

## Scope
- Define the export schema for generator metadata and commit records.
- Add versioning rules.
- Validate all export payloads before they are written.
- Provide clear validation errors for malformed data.
- Keep the schema reusable across backend tests and frontend previews.

## Non-goals
- No signing yet.
- No public hosting concerns.
- No GitHub integration.

## Design Constraints
- Schema definitions should live in a dedicated contract layer.
- Validation should be strict by default.
- Backward compatibility must be explicit through versioning.
- Avoid duplicated field definitions across backend code paths.

## Implementation Notes
- Use one source of truth for the schema.
- Generate or hand-maintain a compact validator that can be exercised in tests.
- Keep exported payloads minimal and deterministic.
- Return machine-readable validation failures for the UI and upload API.

## Acceptance Criteria
- Invalid payloads are rejected before export.
- Valid payloads round-trip through validation successfully.
- Schema versioning is explicit.
- Tests cover missing fields, type mismatches, and boundary cases.

## Dependencies
- Story 1
- Story 3

## Output of this story
A validated JSON contract that downstream stories can trust during upload and reporting.
