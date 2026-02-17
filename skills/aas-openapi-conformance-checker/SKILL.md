---
name: aas-openapi-conformance-checker
description: Validate generated or edited AAS OpenAPI files for structural conformance and repository-aligned conventions (openapi/info/paths presence, operationId uniqueness, and AAS pattern hints). Use after generating submodel-template APIs or before merging OpenAPI changes into an AAS specification repository.
---

# AAS OpenAPI Conformance Checker

## Quick start

Run:

```bash
python scripts/check_aas_openapi_conformance.py <openapi-file>
```

## Workflow

1. Run the checker on the generated OpenAPI file.
2. Read errors first; fix until zero errors.
3. Review warnings and decide whether deviations are intentional.
4. Re-run checker and attach result to the handoff.

## Validation scope

- Required top-level sections:
  - `openapi`
  - `info`
  - `paths`
- Unique `operationId` values.
- Presence hints for submodel-related path families.

## References

Use `references/conformance-rules.md` to interpret findings and choose fixes.
