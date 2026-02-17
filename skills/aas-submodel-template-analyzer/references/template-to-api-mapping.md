# Template-to-API Mapping Reference

Use this reference to derive API-relevant requirements from a submodel template.

## Core source files in this repository

- `Part1-MetaModel-Schemas/openapi.yaml`: canonical metamodel schemas.
- `Part2-API-Schemas/openapi.yaml`: common API payload and response schemas.
- `SubmodelServiceSpecification/V3.1_SSP-001.yaml`: template for direct submodel element interactions.
- `SubmodelRepositoryServiceSpecification/V3.1_SSP-001.yaml`: repository-level patterns.
- `Entire-API-Collection/V3.1.yaml`: integrated endpoint view.

## Mapping rules

1. **Template element cardinality** -> list/read/search requirements.
2. **Template-defined operations** -> operation invocation endpoints and payload schemas.
3. **Semantic IDs / concept references** -> filtering and lookup patterns.
4. **Blob/File elements** -> media transfer patterns and content-type handling.
5. **Versioning constraints** -> `info.version` + path versioning consistency.

## Requirement profile heuristics

- If template includes executable functions, require operation invocation path coverage.
- If template includes nested collections, require path traversal and pagination guidance.
- If template references external concept descriptions, require concept-description compatibility notes.
