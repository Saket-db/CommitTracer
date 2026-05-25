# Story 5 - Signing and Tamper Detection

## Objective
Add tamper-evident fingerprinting to the export flow so generated JSON can be verified later.

## Why this matters
The collector is only useful if the platform can trust that the file was produced by the official local workflow and not edited after the fact.

## Scope
- Generate a canonical payload fingerprint for exported payloads.
- Store fingerprint metadata alongside the payload.
- Verify fingerprints before upload or ingestion.
- Define the failure behavior for modified files.
- Keep fingerprinting and verification code isolated from business logic.

## Non-goals
- No public platform deployment yet.
- No UI polish.
- No cryptography research beyond the chosen fingerprint approach.

## Design Constraints
- Use standard, auditable hashing primitives.
- Keep key handling explicit and local-first if a future signature is added.
- Avoid mixing fingerprint logic with schema validation.
- Make verification available both in backend APIs and in tests.

## Implementation Notes
- Fingerprinting should happen only after schema validation passes.
- Verification should fail closed if metadata or payload bytes change.
- The API should return a clear reason when a fingerprint check fails.
- Keep any hashing helper small and isolated.

## Acceptance Criteria
- Exported files include tamper-evidence metadata.
- Edited files fail verification.
- Valid fingerprinted files verify successfully.
- Tests cover valid hash, invalid hash, and missing hash cases.

## Dependencies
- Story 4

## Output of this story
A trustworthy export artifact that can be validated before it leaves the local machine or is uploaded.
