---
name: aas-submodel-api-designer
description: Design or generate OpenAPI specifications for AAS submodel-template-specific APIs by reusing patterns from the official AAS API specifications and domains. Use when implementing a new submodel template API, extending an existing AAS API, or preparing Claude Haiku/Sonnet prompts for agentic API authoring.
---

# AAS Submodel API Designer

## Workflow decision

- If requirements are not yet explicit, first run `aas-submodel-template-analyzer`.
- If requirements are explicit, proceed directly to design.

## Design workflow

1. Load `references/api-design-patterns.md`.
2. Select closest baseline specification:
   - `SubmodelServiceSpecification` for direct submodel APIs.
   - `SubmodelRepositoryServiceSpecification` for repository patterns.
3. Reuse shared schemas from Part1/Part2 domains before defining new components.
4. Generate OpenAPI draft with:
   - path set
   - operationIds
   - parameter and response structures
   - reusable components
5. Emit a change log documenting each divergence from baseline AAS patterns.
6. Run `aas-openapi-conformance-checker`.

## Claude interaction mode

Use one of these assets as scaffolds before generation:

- `assets/claude-sonnet-system-prompt.md`
- `assets/claude-haiku-task-prompt.md`

Fill placeholders with template details and output target.

## Output expectations

- Produce OpenAPI YAML only, unless the caller asks for explanation.
- Keep all reusable pieces under `components`.
- Minimize custom extension fields.
