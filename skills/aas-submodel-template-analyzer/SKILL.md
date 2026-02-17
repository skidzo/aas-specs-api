---
name: aas-submodel-template-analyzer
description: Analyze an Asset Administration Shell submodel template or metamodel input and produce a structured API requirement profile (identifiers, operations, payload constraints, and repository/service boundaries). Use when preparing a new submodel-template-specific API or when extending an existing AAS API skill set with template-derived requirements.
---

# AAS Submodel Template Analyzer

## Workflow

1. Collect template inputs and map them to API impact categories:
   - identity and addressing
   - query/filter semantics
   - operation invocation
   - file/blob handling
   - pagination and result shaping
2. Load `references/template-to-api-mapping.md` and build a requirement profile.
3. Emit a machine-actionable output section with:
   - required endpoints
   - optional endpoints
   - required schema components
   - conformance assumptions
4. Hand over to `aas-submodel-api-designer` with explicit unresolved questions.

## Output contract

Produce the result in this structure:

```markdown
# Submodel API Requirement Profile

## Input assumptions
- ...

## Required API capabilities
- capability: ...
  rationale: ...
  source-template-element: ...

## Endpoint candidates
- method/path: ...
  required: true|false
  notes: ...

## Schema requirements
- schema: ...
  fields: ...
  constraints: ...

## Open questions
- ...
```

## Constraints

- Reuse existing AAS API semantics before introducing new patterns.
- Prefer compatibility with `Part1-MetaModel-Schemas` and `Part2-API-Schemas` from this repository.
- Avoid inventing non-standard error models when standard response patterns already exist.
