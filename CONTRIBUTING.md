# Contributing

This repository is maintained by [@varunk130](https://github.com/varunk130).

## Suggesting a change

Open an issue that describes the partnership decision you are trying to make and where the current skills fall short. Pull requests are welcome.

## Adding or changing a skill

1. Copy the shape in [docs/SKILL_TEMPLATE.md](docs/SKILL_TEMPLATE.md) into `skills/<skill-name>/SKILL.md`.
2. Keep the folder name and the `name` field identical and kebab-case.
3. Add the skill to the table in the [README](README.md).
4. Run the validator before opening a pull request:

```bash
python scripts/validate_skills.py
```

## Ground rules

- **Synthetic data only.** Never commit real partner names, customer lists, deal terms, or pipeline numbers.
- **Decisions, not theory.** Every skill should end in an output someone can act on or take into a meeting.
- **Humans stay accountable.** Skills that touch contracts, security, or legal terms must say so in their guardrails.
- **No dependencies.** Scripts run on the Python standard library.
