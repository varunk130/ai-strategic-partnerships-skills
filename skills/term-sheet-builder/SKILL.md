---
name: term-sheet-builder
description: 'Drafts a non-binding term sheet or MOU outline for a partnership, with each term marked must-have, tradeable, or walk-away, ready for counsel review. Use when: term sheet, MOU, memorandum of understanding, letter of intent, partnership terms, draft the key terms, what should we ask for, AI data usage terms.'
---

# Term Sheet Builder

Get the business terms agreed in plain language before lawyers turn them into a contract.

## When to Use

- Both sides agree in principle and want the key terms on one page
- You need to align internally on what you will and will not give before talks
- A partner sent their term sheet and you need a structured redline position
- An AI partnership raises data and model-usage questions nobody has written down yet

## What You'll Need

**Critical inputs (ask if not provided):**

- The two parties and the partnership type (integration, resell, OEM, co-sell, joint development)
- The commercial structure, ideally from [deal-structure-designer](../deal-structure-designer/SKILL.md)
- What data, models, or IP each side will expose to the other

**Nice-to-have:**

- Your standard partner agreement or prior term sheets, for consistency
- Internal policy on exclusivity, data use, and liability caps
- The partner's draft, if they sent one

## Process

### Step 1: Fill each term

Work through every row. Leave none blank; write "Not applicable" with a reason if a term truly does not apply.

| Term | What to settle | Common AI-era trap |
|------|----------------|--------------------|
| Parties | Legal entities, affiliates covered | Affiliate that runs a competing model is included |
| Scope | Products, use cases, what is explicitly out | "Any AI features" scope that grows silently |
| Exclusivity | None, category, or named-competitor; tied to what | Exclusivity with no minimum or end date |
| Territory | Regions, segments, channels (incl. marketplaces) | Global by default with no local support |
| Economics | Structure, rates, payment terms, minimums | Payout on bookings, not collections |
| IP rights | Who owns pre-existing IP, joint work, improvements | Joint IP with no license-back |
| Data rights | What data is shared, purpose, retention, deletion | "Aggregated" data defined so broadly it is not |
| AI and model usage | May either side train, fine-tune, or evaluate models on the other's data or outputs | Silent on training means you lose the argument later |
| SLAs | Uptime, latency, support response, model change notice | No notice period for model or API deprecations |
| Branding | Logo use, naming, co-marketing approvals | Partner markets "powered by" claims you never approved |
| Term and termination | Length, renewal, for-cause and for-convenience exits, wind-down | No transition period for customers on termination |
| Governance | Exec sponsors, operating cadence, escalation path | No named owner on either side |

### Step 2: Mark each term

| Mark | Meaning | Rule of thumb |
|------|---------|---------------|
| Must-have | We will not sign without it | Keep to five or fewer, or nothing is |
| Tradeable | We want it but will exchange it for something | Note what you would take in return |
| Walk-away | If the partner insists on this, we stop | Write the specific trigger, not a vague concern |

### Step 3: Write the AI and data terms precisely

These are the terms most likely to be missing and most costly later. For each party state:
- Data shared and purpose limitation
- Training: allowed, allowed with opt-in, or prohibited, on inputs and on outputs
- Retention period and deletion on termination, with certification
- Sub-processors and model providers that will touch the data
- Notice required before changing the underlying model

### Step 4: Check internal sign-off

List who must approve before this leaves the building: deal owner, finance, security, privacy, product, and counsel.

## Output Format

```markdown
# Term Sheet (Non-Binding): [Our company] and [Partner, e.g. Kestrel AI]
Draft [n], [date]. For discussion only. Subject to definitive agreement and counsel review.

| # | Term | Proposed position | Mark | If traded, we want |
|---|------|-------------------|------|--------------------|
| 1 | Parties | | | |
| 2 | Scope | | | |
| 3 | Exclusivity | | | |
| 4 | Territory | | | |
| 5 | Economics | | | |
| 6 | IP rights | | | |
| 7 | Data rights | | | |
| 8 | AI and model usage | | | |
| 9 | SLAs | | | |
| 10 | Branding | | | |
| 11 | Term and termination | | | |
| 12 | Governance | | | |

### Walk-away triggers
- [term]: we stop if [specific condition]

### Open items
- [item] - owner - due

### Internal approvals required
- [ ] Finance  - [ ] Security  - [ ] Privacy  - [ ] Product  - [ ] Counsel
```

## Guardrails

- This is not legal advice. The output is a business-terms draft. Counsel must review it before anything is sent to the partner.
- Label every draft "Non-binding" and "Subject to definitive agreement". Do not remove those labels.
- Never send the Mark column or the "If traded" column to the partner. Strip them into a clean external version.
- Do not invent legal language (indemnities, warranties, governing law). Flag them for counsel instead.
- Synthetic examples only. Do not commit real term sheets to shared repos.

## Related

- [deal-structure-designer](../deal-structure-designer/SKILL.md): source for the Economics term
- [agentic-trust-agreement](../agentic-trust-agreement/SKILL.md): deeper treatment of AI, agent, and data terms
- [negotiation-prep](../negotiation-prep/SKILL.md): uses the Mark column to build the give-get list
- [partner-due-diligence](../partner-due-diligence/SKILL.md): confirms the partner can meet the terms you ask for
- [partner-exec-briefing](../partner-exec-briefing/SKILL.md): summarizes the terms for your sponsor
