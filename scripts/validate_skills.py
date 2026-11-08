#!/usr/bin/env python3
"""Validate every SKILL.md in skills/ against docs/SKILL_TEMPLATE.md.

Checks:
  - YAML frontmatter with `name` and `description`
  - `name` is kebab-case and matches the skill's folder name
  - `description` includes explicit "Use when:" triggers
  - the six required sections are present, in order
  - every skill is listed in the root README

Exit code is 1 if any check fails. Standard library only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
REQUIRED_SECTIONS = [
    "## When to Use",
    "## What You'll Need",
    "## Process",
    "## Output Format",
    "## Guardrails",
    "## Related",
]
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip("'\"")
    return fields


def check_skill(path: Path, root_readme: str) -> list[str]:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        return [f"{rel}: missing or malformed YAML frontmatter"]

    errors = []
    name = fm.get("name", "")
    if not KEBAB.match(name):
        errors.append(f"{rel}: name '{name}' is not kebab-case")
    if name != path.parent.name:
        errors.append(f"{rel}: name '{name}' does not match folder '{path.parent.name}'")
    if "Use when:" not in fm.get("description", ""):
        errors.append(f"{rel}: description has no 'Use when:' triggers")

    positions = [text.find(f"\n{s}\n") for s in REQUIRED_SECTIONS]
    for section, pos in zip(REQUIRED_SECTIONS, positions):
        if pos == -1:
            errors.append(f"{rel}: missing section '{section}'")
    found = [p for p in positions if p != -1]
    if found != sorted(found):
        errors.append(f"{rel}: sections are out of order")

    if f"skills/{name}/SKILL.md" not in root_readme:
        errors.append(f"{rel}: not listed in README.md")
    return errors


def main() -> int:
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    errors = [e for path in skill_files for e in check_skill(path, root_readme)]

    for error in errors:
        print(f"FAIL {error}")
    print(f"{len(skill_files)} skills checked, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
