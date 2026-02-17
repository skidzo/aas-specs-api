# AAS Submodel API Skill Set

This folder provides a merge-friendly skill set to extend an existing agent skill collection (for example an `aas-specs-metamodel` skill set).

## Included skills

1. `aas-submodel-template-analyzer`
   - Extracts API-relevant constraints from a submodel template.
2. `aas-submodel-api-designer`
   - Builds API drafts for a submodel template by reusing AAS API patterns and domains from this repository.
3. `aas-openapi-conformance-checker`
   - Performs fast conformance checks for generated OpenAPI files and reports actionable fixes.

## Merge strategy

- Copy each skill directory into your existing skills root.
- Keep existing skills unchanged; these skills are additive and can be invoked independently.
- Preferred execution order for a new template:
  1. analyze template
  2. design API
  3. run conformance checks

## Claude Haiku/Sonnet usage

The `aas-submodel-api-designer/assets/` folder includes prompt scaffolds tuned for agentic interaction with Claude Haiku/Sonnet:

- `claude-sonnet-system-prompt.md`
- `claude-haiku-task-prompt.md`

Use these as seed prompts and inject your concrete submodel template and target output path.
