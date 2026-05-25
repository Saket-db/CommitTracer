# Story 2 - Local Collector Script and GitLab Access

## Objective
Build the downloadable collector script and the small GitLab-facing client layer it uses to retrieve commit metadata from one or more local accounts.

## Why this matters
The collector cannot do anything useful without reliable access to GitLab. This story isolates account configuration and transport concerns so the rest of the system never needs to know how tokens are handled.

## Scope
- Add a downloadable local collector script.
- Support configurable GitLab base URLs for self-hosted instances.
- Build a dedicated client for GitLab commit requests.
- Store secrets only on the local machine.
- Support multiple accounts with bounded concurrency.
- Return clear errors for invalid tokens, rate limits, and unreachable hosts.

## Non-goals
- No upload UI.
- No schema export.
- No report generation.
- No cross-platform packaging yet.

## Design Constraints
- Never log raw secrets.
- Keep account configuration and request logic separate from route handlers.
- Make the client retryable and testable.
- Keep each function short and single-purpose.

## Implementation Notes
- The website should expose a download endpoint for the collector script.
- The collector should read local account configuration and collect each account independently.
- The client should accept host, token, and timeout settings through a config object.
- Errors should be normalized into user-friendly API responses or CLI messages.

## Acceptance Criteria
- A user can download the collector script and run it locally.
- The collector can verify connectivity without normalizing commits.
- Invalid host and invalid token cases are handled cleanly.
- Tests cover success, configuration failure, and network failure paths.

## Dependencies
- Story 1

## Output of this story
A safe and reusable GitLab client and collector entry point that later sync logic can call without embedding transport details.
