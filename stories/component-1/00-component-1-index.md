# Component 1 Backlog Index

This folder breaks Component 1 into implementation stories that can be consumed one at a time by an agent or a developer.

## Scope
- Local-first collector script only
- Flask as the backend surface for upload, validation, and reporting
- Next.js as the local UI layer for download, upload, and report preview
- Corporate GitLab ingestion on the user's machine
- Schema-locked export of commit metadata
- Tamper detection and report generation from uploaded JSON

## Delivery Principles
- Keep every function under 60 lines.
- Prefer small services, validators, and serializers over monolithic modules.
- Use explicit boundaries between API, domain logic, persistence, and UI.
- Make every story independently implementable and testable.
- Keep the local extractor privacy-preserving by default.

## Story Order
1. [Story 1 - Foundation and Architecture](01-foundation-and-architecture.md)
2. [Story 2 - Local Collector Script and GitLab Access](02-gitlab-auth-and-client.md)
3. [Story 3 - Commit Sync and Normalization](03-commit-sync-and-normalization.md)
4. [Story 4 - JSON Schema and Validation](04-json-schema-and-validation.md)
5. [Story 5 - Signing and Tamper Detection](05-signing-and-tamper-detection.md)
6. [Story 6 - Next.js Local UI and Upload Flow](06-nextjs-local-ui-and-export-flow.md)
7. [Story 7 - Testing, Packaging, and Release Hardening](07-testing-packaging-and-release-hardening.md)

## Suggested Execution Rule
Work strictly in order unless a dependency is already satisfied. Do not begin downstream stories until the prior story has a clear acceptance pass.
