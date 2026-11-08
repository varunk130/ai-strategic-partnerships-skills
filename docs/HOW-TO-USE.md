# How to Use

## Install

The skills are plain Markdown folders. Install them with the script or copy them by hand.

```bash
./install.sh                         # all skills, user level (~/.claude/skills)
./install.sh --project               # all skills, current project (.claude/skills)
./install.sh partnership-thesis      # only the named skills
cp -r skills/negotiation-prep ~/.claude/skills/   # manual install
```

For GitHub Copilot or another agent that reads instruction files, point it at the `SKILL.md` you want, or paste its contents into the agent's custom instructions.

## Invoke

You do not need to name the skill. Each `description` lists its triggers after `Use when:`, and Claude Code loads the skill when your request matches. Naming it still works:

> Use the deal-structure-designer skill to compare a revenue share against a referral fee for the Halcyon Cloud deal.

Every skill opens by asking for its critical inputs if you have not given them. Give it what you have; it will say what is missing rather than guess.

## Chain skills

The output of one skill is written to be the input of the next. A typical new-partnership sequence:

1. `partnership-thesis` produces the thesis and success test.
2. `ecosystem-landscape-map` confirms the partner is the right one to approach first.
3. `partner-due-diligence` checks them before you invest time.
4. `deal-structure-designer` picks the commercial model.
5. `partnership-business-case` gets internal approval with that model.
6. `negotiation-prep`, `partner-exec-briefing`, and `term-sheet-builder` carry the negotiation.
7. `agentic-trust-agreement` sets the operating terms if agents act across both companies.
8. `partnership-renewal-review` closes the loop at term end, against the original thesis.

See [partnership-lifecycle.md](partnership-lifecycle.md) for when to skip steps.

## What the skills will not do

- Give legal advice. Term sheets and trust agreements are drafts for your counsel and security teams.
- Invent market data. Where a number is needed and not given, the skill marks it as an assumption.
- Name real companies in examples. Bring your own data; keep it out of public forks.
