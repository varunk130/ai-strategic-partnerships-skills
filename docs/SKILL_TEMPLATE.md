# Skill Template

Every skill lives in `skills/<skill-name>/SKILL.md` and follows this shape. `scripts/validate_skills.py` checks it.

```markdown
---
name: skill-name
description: 'One sentence on what the skill produces. Use when: trigger phrase, trigger phrase, trigger phrase.'
---

# Skill Title

One line on the decision this skill helps a partnerships leader make.

## When to Use

- Situation that calls for it
- Another situation

## What You'll Need

**Critical inputs (ask if not provided):**

- Input the skill cannot work without

**Nice-to-have:**

- Input that sharpens the output

## Process

### Step 1: Name of step

What to do and why. Tables beat paragraphs for scoring or comparison.

### Step 2: Name of step

...

## Output Format

A fenced markdown block showing the exact deliverable.

## Guardrails

- What the skill must not do, and where human judgment stays in charge

## Related

- Other skills in this library or sibling repos that feed into or follow this one
```

## Conventions

- `name` is kebab-case and matches the folder name.
- `description` includes an explicit `Use when:` list of triggers.
- All six sections above are present, in order.
- Examples use synthetic companies only. Never name a real partner, customer, or deal.
- Keep a skill under roughly 150 lines. Link out instead of growing it.
