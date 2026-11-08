---
name: partnership-business-case
description: 'Writes the internal approval memo for a strategic partnership: thesis, options, full investment, scenario returns with stated assumptions, leading indicators, risks, kill criteria, and the explicit ask. Use when: partnership business case, approval memo, investment committee, leadership sign-off, funding a partnership, justify partner investment, partnership ROI.'
---

# Partnership Business Case

Get a yes or no from leadership on a partnership, with the cost, the bet, and the exit stated before anyone signs.

## When to Use

- A partnership needs headcount, engineering, MDF, or revenue share that someone above you must approve
- A thesis is agreed in principle and now needs funding
- Leadership asked "what do we get for this?" and the answer is a slide of logos
- Re-approving a partnership whose scope or cost has materially changed

## What You'll Need

**Critical inputs (ask if not provided):**

- The partner (synthetic in examples, e.g. "Halcyon Cloud") and the one-sentence thesis
- What we would give: people, engineering weeks, MDF, revenue share or discount
- The decision-maker and the date of the decision

**Nice-to-have:**

- Pipeline or usage data from a pilot or comparable partner
- The output of [partnership-thesis](../partnership-thesis/SKILL.md) and [deal-structure-designer](../deal-structure-designer/SKILL.md)
- Finance's hurdle rate or payback expectation

## Process

### Step 1: State the problem and thesis

Lead with the business problem, not the partner. One paragraph: what we cannot do alone, why now, and why this partner. If the thesis needs more than three sentences, it is not ready.

### Step 2: Show the options considered

Leadership trusts a recommendation more when the alternatives were real.

| Option | What it looks like | Cost | Time to value | Why not (or why) |
|--------|--------------------|------|---------------|------------------|
| Do nothing | Status quo | 0 | n/a | Name the cost of standing still |
| Build | Own team builds capability | High | Slow | |
| Buy / acquire | Acquire a smaller player | Highest | Medium | |
| Partner: Halcyon Cloud | Recommended structure | Medium | Fast | |
| Partner: alternative | Second-best partner | | | |

### Step 3: Count the full investment

Include what is easy to forget. Revenue share given up is a cost even if no cash moves.

| Line | Year 1 | Year 2 | Notes |
|------|--------|--------|-------|
| Partner team (FTE x loaded cost) | | | Partner manager, SE, ops |
| Engineering (weeks x cost) | | | Integration build plus maintenance |
| MDF and co-marketing | | | Committed vs discretionary |
| Revenue share / discount given up | | | Applied to expected partner-sourced revenue |
| Marketplace or platform fees | | | |
| Total | | | |

### Step 4: Model return in three scenarios

Every number carries an assumption a skeptic can challenge. Keep the base case honest: it should be the outcome you would bet your own budget on.

| Driver | Low | Base | High | Assumption source |
|--------|-----|------|------|-------------------|
| Joint opportunities created | | | | Pilot rate, comparable partner |
| Win rate on joint deals | | | | |
| Average deal size | | | | |
| Attributable revenue | | | | |
| Net return after investment | | | | |
| Payback (months) | | | | |

### Step 5: Set leading indicators and kill criteria

Revenue lags. Pick indicators you can read at 90 and 180 days, and agree now what result ends the partnership. Kill criteria written after launch never get used.

| Checkpoint | Indicator | Target | Kill / reset trigger |
|------------|-----------|--------|----------------------|
| 90 days | Integration live, sellers trained | Live, 20 trained | Not live: reset scope |
| 90 days | Joint accounts mapped and engaged | 15 | Under 5: escalate |
| 180 days | Qualified joint pipeline | | Under 30% of base: kill review |
| 180 days | First joint customer live | 1 | None: kill review |

### Step 6: Name risks and the ask

List the top risks with owner and mitigation, then write the ask as a sentence leadership can approve verbatim.

## Output Format

```markdown
# Business Case: [Partner] partnership
Decision-maker: [name] | Decision date: [date] | Author: [name]

## The ask
Approve [people / budget / revenue share] for [term] to [outcome].

## Problem and thesis
[One paragraph]

## Options considered
| Option | Cost | Time to value | Verdict |

## Investment
| Line | Year 1 | Year 2 |
Total: [x]

## Expected return
| | Low | Base | High |
Key assumptions: [list, each with source]

## Leading indicators
| Day | Indicator | Target |

## Kill criteria
- [Condition] by [date] triggers [kill / reset]

## Risks
| Risk | Likelihood | Impact | Mitigation | Owner |

## What we are not asking for
[Scope explicitly excluded]
```

## Guardrails

- Do not inflate the base case to clear a hurdle. If it only works in the high case, say so.
- Every revenue figure needs a stated assumption and source; flag any that are guesses.
- Do not omit revenue share or engineering maintenance to make the investment look smaller.
- Kill criteria must be measurable and dated, not "if it is not working."
- The memo informs the decision; leadership owns it.

## Related

- [partnership-thesis](../partnership-thesis/SKILL.md): the thesis this case funds
- [deal-structure-designer](../deal-structure-designer/SKILL.md): the structure the investment lines come from
- [partner-due-diligence](../partner-due-diligence/SKILL.md): evidence behind the risk section
- [partnership-renewal-review](../partnership-renewal-review/SKILL.md): where these targets get checked at term end
- [Joint business plan](https://github.com/varunk130/ai-ecosystem-partnerships/blob/main/skills/joint-business-plan/SKILL.md): turning the approved case into a shared plan
