# Story 3 - Commit Sync and Normalization

## Objective
Fetch commit metadata from GitLab and normalize it into the local export domain model.

## Why this matters
This is the core extraction workflow. The raw API payload should be transformed into a minimal, privacy-preserving record that contains only approved fields and can be uploaded safely.

## Scope
- Query commit history from GitLab.
- Extract only the allowed metadata fields.
- Derive safe convenience fields such as day of week and hour from timestamps.
- Deduplicate records when necessary.
- Preserve deterministic sorting and pagination behavior.

## Non-goals
- No file paths.
- No commit messages.
- No repo names in exported output.
- No AI inference.

## Design Constraints
- Keep raw API models separate from exported models.
- Put date and timezone logic in dedicated helpers.
- Avoid business logic inside route handlers.
- Keep transformations pure where possible.

## Implementation Notes
- The collector should pull only the fields needed for the final schema.
- Normalization should convert timestamps into a canonical timezone before deriving day and hour.
- Large syncs should be processed in bounded concurrency to avoid memory spikes.
- If commit IDs are kept, treat them as opaque identifiers and never enrich them with project context.

## Acceptance Criteria
- A collector run produces normalized commit records from GitLab API data.
- The final record set contains only approved metadata.
- Timezone handling is predictable and tested.
- Duplicate or malformed API entries are safely rejected.

## Dependencies
- Story 1
- Story 2

## Output of this story
A normalized local commit dataset that is ready for schema validation, upload, and reporting.
