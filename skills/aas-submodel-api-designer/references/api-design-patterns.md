# AAS API Design Patterns for Submodel Templates

## Canonical files to consult

- `SubmodelServiceSpecification/V3.1_SSP-001.yaml`
- `SubmodelServiceSpecification/V3.1_SSP-002.yaml`
- `SubmodelRepositoryServiceSpecification/V3.1_SSP-001.yaml`
- `SubmodelRepositoryServiceSpecification/V3.1_SSP-002.yaml`
- `Part1-MetaModel-Schemas/openapi.yaml`
- `Part2-API-Schemas/openapi.yaml`

## Baseline endpoint families

- Submodel root retrieval/update.
- Submodel element traversal.
- Operation invocation.
- Value-only representation access.
- Metadata and content negotiation support.

## Reuse-first schema policy

1. Reference Part1/Part2 schema components where semantically compatible.
2. Introduce template-specific schema components only for true extensions.
3. Keep identifiers, references, and error payload shapes compatible with existing AAS conventions.

## Naming conventions

- Path segments: lowercase, hyphen-free, AAS-aligned wording.
- `operationId`: unique verb-object style (e.g., `getSubmodelElementsByPath`).
- Component schemas: PascalCase.

## Compatibility notes

- Ensure generated API can coexist with existing AAS service specifications.
- Favor additive changes for merge-friendly evolution.
