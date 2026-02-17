# AAS OpenAPI Conformance Rules (Lightweight)

## Structural rules

1. Top-level keys MUST include `openapi`, `info`, and `paths`.
2. `operationId` values SHOULD be unique repository-wide per file.

## AAS-oriented guidance

- For submodel-centric APIs, at least one path SHOULD contain `submodel`.
- Version metadata SHOULD be explicit in `info.version`.
- Avoid introducing error payload patterns that diverge from existing Part2 conventions without rationale.

## Recommended remediation order

1. Resolve missing required top-level keys.
2. Resolve duplicate operationIds.
3. Address warnings and document justified exceptions.
