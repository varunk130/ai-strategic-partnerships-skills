---
name: partnership-thesis
description: 'Produces a one-page strategic rationale for a partnership before any outreach: the gap it closes, why partner over build or buy, the partner archetype, the value exchange, and falsifiable 6- and 12-month success tests. Use when: partnership thesis, why partner, partner vs build vs buy, should we partner, partnership rationale, strategic partnership memo, before partner outreach.'
---

# Partnership Thesis

Decide whether a partnership deserves to exist, and what would prove it wrong, before anyone sends the first email.

## When to Use

- A leader says "we should partner with someone for X" and nobody has written down why
- Before outreach to a named partner, or before building a target list
- A build-vs-buy debate has stalled and partnering is the unexamined third option
- An existing partnership is being renewed and the original rationale is lost

## What You'll Need

**Critical inputs (ask if not provided):**

- The gap: a capability, distribution channel, or data asset you lack today
- The customer or segment that feels the gap, and the evidence they feel it (lost deals, churn reasons, requests)
- Rough cost and time to build it yourself

**Nice-to-have:**

- Candidate partners already in mind, even informal ones
- Acquisition appetite and budget, if buy is on the table
- Current strategy priorities, to check the thesis against them

## Process

### Step 1: Name the gap in one sentence

Write it as "Customers in [segment] cannot [outcome] because we lack [capability or reach]." If it takes two sentences, there are two theses. Split them.

Classify the gap: **capability** (something the product cannot do), **distribution** (buyers or agents you cannot reach), or **data** (inputs you cannot get). The type drives the archetype in Step 3.

### Step 2: Run partner vs build vs buy

Score each option honestly. Partnering wins only when it is clearly better on the dimensions that matter for this gap.

| Factor | Build | Buy | Partner |
|--------|-------|-----|---------|
| Time to customer value | | | |
| Cost (12-month, fully loaded) | | | |
| Control of roadmap and quality | | | |
| Is this core differentiation? | | | |
| Reversibility if wrong | | | |
| Dependency or lock-in risk | | | |

Rules of thumb:
- If it is core differentiation, partnering is usually a bridge, not an answer. Say so.
- If speed matters more than control and the gap is not core, partner.
- If the only good partner is also your fastest-growing competitor, revisit buy or build.

### Step 3: Choose the archetype

| Archetype | Closes which gap | Typical value exchange | Watch out for |
|-----------|-----------------|-----------------------|---------------|
| Platform | Distribution, surface area | Reach for you, ecosystem depth for them | Platform rule changes, feature absorption |
| Model provider | Capability (reasoning, generation) | Usage revenue for them, capability for you | Price and model changes outside your control |
| Cloud | Distribution, procurement, infra | Committed spend consumption for them, buyer access for you | Co-sell attention goes to bigger partners |
| SI (systems integrator) | Delivery capacity, enterprise access | Services revenue for them, deployments for you | Margin pressure, inconsistent delivery |
| ISV | Adjacent capability, shared customer | Joint value for both customer bases | Overlapping roadmaps |
| Data provider | Data | Licensing revenue for them, differentiated outputs for you | Rights, provenance, and renewal pricing |

Pick one primary archetype. A thesis that needs three archetypes is a strategy, not a partnership.

### Step 4: Write the value exchange

State what each side gets in their terms, not yours. If you cannot name what the partner's sales team or product team gains, the partnership will stall at the second meeting.

### Step 5: Set falsifiable success tests

Each test is a number, a date, and a kill condition. "Strong engagement" is not a test.

| Horizon | Leading indicator | Target | Kill or rethink if |
|---------|------------------|--------|-------------------|
| 6 months | e.g. joint customers live, agent invocations, sourced pipeline | | |
| 12 months | e.g. attributed revenue, retention lift, win rate in segment | | |

## Output Format

```markdown
## Partnership Thesis: [gap name]
Author: [name] | Date: [date] | Status: draft / reviewed / approved

**Gap:** Customers in [segment] cannot [outcome] because we lack [capability/reach/data].
**Evidence:** [3 data points: lost deals, requests, churn reasons]

**Why partner:** [one paragraph on why partner beats build and buy]
| Option | Time to value | 12-mo cost | Control | Verdict |
|--------|--------------|-----------|---------|---------|
| Build  | | | | |
| Buy    | | | | |
| Partner| | | | Chosen |

**Archetype:** [platform / model provider / cloud / SI / ISV / data provider]
**Example target profile:** [e.g. "a mid-size ISV like Northwind Data serving our ICP"]

**Value exchange**
- We get: [...]
- They get: [...] (in their metrics: [quota, consumption, attach rate])

**Success tests**
- 6 months: [metric] reaches [target] by [date]. Rethink if below [floor].
- 12 months: [metric] reaches [target] by [date]. Exit if below [floor].

**Biggest risk:** [one line] | **Mitigation:** [one line]
**Decision needed:** [approve outreach / fund discovery / reject]
```

## Guardrails

- Do not write a thesis backward from a partner someone already wants. Start from the gap.
- Do not soften success tests to make approval easier. A test that cannot fail is not a test.
- The build-vs-buy call belongs to the product and finance owners; this skill frames it, it does not make it.
- Use synthetic or anonymized evidence in shared drafts; never paste customer names into examples.

## Related

- [ecosystem-landscape-map](../ecosystem-landscape-map/SKILL.md): find and rank candidates once the archetype is set
- [partnership-business-case](../partnership-business-case/SKILL.md): turn the thesis into numbers
- [partner-due-diligence](../partner-due-diligence/SKILL.md): vet a specific candidate
- [deal-structure-designer](../deal-structure-designer/SKILL.md): shape the deal once a partner says yes
- [partnership-renewal-review](../partnership-renewal-review/SKILL.md): test the original thesis at renewal
- [product-partnership-evaluator](https://github.com/varunk130/ai-ecosystem-partnerships/blob/main/skills/product-partnership-evaluator/SKILL.md): evaluate a specific product partnership
