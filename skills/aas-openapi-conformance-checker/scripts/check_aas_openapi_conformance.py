#!/usr/bin/env python3
"""Lightweight structural checker for AAS-style OpenAPI files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_TOP_LEVEL_KEYS = ("openapi", "info", "paths")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def detect_top_level_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for line in text.splitlines():
        if not line or line.startswith((" ", "\t", "#")):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):", line)
        if match:
            keys.add(match.group(1))
    return keys


def extract_operation_ids(text: str) -> list[str]:
    operation_ids: list[str] = []
    pattern = re.compile(r"^\s*operationId:\s*['\"]?([^'\"\n]+)['\"]?\s*$")
    for line in text.splitlines():
        match = pattern.match(line)
        if match:
            operation_ids.append(match.group(1).strip())
    return operation_ids


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/check_aas_openapi_conformance.py <openapi-file>")
        return 2

    target = Path(sys.argv[1])
    if not target.exists():
        print(f"ERROR: file not found: {target}")
        return 2

    text = read_text(target)
    top_level = detect_top_level_keys(text)
    operation_ids = extract_operation_ids(text)

    errors: list[str] = []
    warnings: list[str] = []

    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key not in top_level:
            errors.append(f"Missing top-level key: {key}")

    seen: set[str] = set()
    duplicates: set[str] = set()
    for operation_id in operation_ids:
        if operation_id in seen:
            duplicates.add(operation_id)
        seen.add(operation_id)

    if duplicates:
        dupes = ", ".join(sorted(duplicates))
        errors.append(f"Duplicate operationId values: {dupes}")

    if "version:" not in text:
        warnings.append("No explicit 'version' field detected; ensure info.version is set.")

    if "submodel" not in text.lower():
        warnings.append("No 'submodel' token detected; verify this is intended for non-submodel APIs.")

    if errors:
        for item in errors:
            print(f"ERROR: {item}")
    if warnings:
        for item in warnings:
            print(f"WARN: {item}")

    print(
        f"Summary: {len(errors)} error(s), {len(warnings)} warning(s), "
        f"{len(operation_ids)} operationId entr{'y' if len(operation_ids) == 1 else 'ies'} scanned."
    )

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
