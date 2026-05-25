# Story 7 - Testing, Packaging, and Release Hardening

## Objective
Harden Component 1 with tests, packaging, and release safeguards so it can be run repeatedly with confidence.

## Why this matters
The extractor will be used on sensitive data. It needs strong tests, predictable packaging, and reliable release behavior before any broader rollout.

## Scope
- Add unit tests for collection, normalization, schema, fingerprinting, reporting, and UI helpers.
- Add integration tests for the local download-upload-report workflow.
- Package the Flask backend and Next.js frontend for local use.
- Document environment setup and run commands.
- Add guardrails for logging, errors, and unsupported states.

## Non-goals
- No Component 2 work.
- No AI inference work.
- No public deployment story.
- No year-end wrap report yet; that will be a later derived summary layer.

## Design Constraints
- Keep tests fast and isolated.
- Avoid test fixtures that depend on live GitLab responses.
- Keep runtime configuration explicit.
- Enforce the function-length rule through code review and structure.

## Implementation Notes
- Test the backend as a service boundary, not as a set of internal implementation details.
- Add mock GitLab responses for all critical paths.
- Document how to run the collector script, Flask backend, and Next.js frontend locally.
- Define the release artifact and what is included or excluded.

## Acceptance Criteria
- Core flows are covered by tests.
- The app can be started locally from a documented procedure.
- Logging does not leak secrets.
- Packaging is repeatable.
- A release checklist exists for the collector and report workflow.

## Dependencies
- Story 1 through Story 6

## Output of this story
A hardened, repeatable local collector and reporting workflow that is ready for broader use.
