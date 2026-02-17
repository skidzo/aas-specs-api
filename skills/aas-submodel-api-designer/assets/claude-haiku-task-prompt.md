Task: Generate an AAS-compatible OpenAPI draft for this submodel template.

Inputs:
- Template summary: {{TEMPLATE_SUMMARY}}
- Mandatory endpoints: {{MANDATORY_ENDPOINTS}}
- Optional endpoints: {{OPTIONAL_ENDPOINTS}}
- Reusable schemas: {{REUSABLE_SCHEMAS}}

Instructions:
1. Start from existing Submodel API patterns.
2. Create only required custom schemas.
3. Keep paths and operationIds deterministic.
4. Ensure compatibility with versioned AAS API style.

Return:
- OpenAPI YAML draft.
- Checklist of assumptions and unresolved questions.
