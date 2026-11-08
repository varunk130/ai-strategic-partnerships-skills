---
name: partner-due-diligence
description: 'Runs structured diligence on a prospective partner across strategy, product, AI practices, security, finance, reputation, and references, and outputs a red/amber/green summary with evidence and open questions. Use when: partner due diligence, vet a partner, should we commit to this partner, AI vendor assessment, model provenance check, partner risk review, before we sign.'
---

# Partner Due Diligence

Decide whether to commit to a partner based on evidence you collected, not the pitch you were given.

## When to Use

- Before signing a term sheet or definitive agreement
- Before embedding a partner's model, agent, or API in your product
- When a partner asks for exclusivity, deep data access, or a joint roadmap
- When something about an existing partner changes (funding, acquisition, incident)

## What You'll Need

**Critical inputs (ask if not provided):**

- The partner name and the proposed scope (what you will depend on them for)
- Who on your side owns security, privacy, legal, and finance review
- Access to the partner for a diligence questionnaire and documents

**Nice-to-have:**

- Their security attestations, model or system cards, eval reports, and DPA
- Two or three customer references, ideally ones they did not hand-pick
- Prior incident history, public filings, or funding announcements

## Process

### Step 1: Scope depth to dependency

Go deeper where you depend more. A co-marketing partner needs less than an embedded model provider.

| Dependency level | Example | Diligence depth |
|------------------|---------|-----------------|
| Light | Referral, co-marketing | Strategic, reputational, references |
| Medium | Integration, resell | Add product, security, financial |
| Deep | OEM, embedded model, data sharing, joint development | All areas, with documents, not just answers |

### Step 2: Collect evidence by area

Every rating needs a source. "They told us" is weaker evidence than a document; a document is weaker than a test you ran.

| Area | What to check | Evidence that counts |
|------|---------------|----------------------|
| Strategic fit | Shared ICP, roadmap direction, competing priorities | Their roadmap deck, account overlap analysis |
| Product / technical | API maturity, versioning and deprecation policy, uptime history, roadmap stability | Public status history, API changelog, a working sandbox test |
| AI-specific: model provenance | Which base models, training data sources, licensing of data | Model or system card, data licensing statement |
| AI-specific: eval evidence | Accuracy, robustness, bias evals on tasks like yours | Eval reports, your own test on a sample set |
| AI-specific: data handling | Whether your data trains their models, retention, sub-processors | DPA, sub-processor list, written training policy |
| AI-specific: safety practices | Red-teaming, misuse monitoring, incident response for model failures | Safety policy, incident postmortems |
| Security / compliance | Attestations, pen tests, access controls, regulatory scope | Current attestation reports, pen test summary |
| Financial health | Runway, revenue concentration, funding stage | Financials under NDA, funding history, credit check |
| Reputational | Litigation, regulatory actions, press, employee signals | Public records, news search |
| Conflict of interest | Ties to your competitors, exclusivities elsewhere, overlapping products | Their partner list, contract disclosures |
| Customer references | Real outcomes, support quality, how they handle problems | Reference calls, at least one not supplied by them |

### Step 3: Rate each area

| Rating | Meaning |
|--------|---------|
| Green | Evidence collected and meets our bar |
| Amber | Gap or weak evidence; acceptable with a mitigation or contract term |
| Red | Fails our bar or evidence refused; blocks commitment until resolved |

A refusal to provide evidence in a deep-dependency area is Red, not Amber.

### Step 4: Convert gaps into actions

Each Amber needs a mitigation (contract term, technical control, or phased scope). Each Red needs an owner and a decision: resolve, descope, or stop.

## Output Format

```markdown
## Partner Due Diligence: [Partner, e.g. Kestrel AI]
Scope: [what we will depend on them for] | Depth: [Light / Medium / Deep] | Date: [date]

**Overall:** [Green / Amber / Red] - [one-sentence recommendation: proceed, proceed with conditions, pause]

| Area | Rating | Evidence | Gap / concern | Mitigation or action |
|------|--------|----------|---------------|----------------------|
| Strategic fit | | | | |
| Product / technical | | | | |
| Model provenance | | | | |
| Eval evidence | | | | |
| Data handling | | | | |
| Safety practices | | | | |
| Security / compliance | | | | |
| Financial health | | | | |
| Reputational | | | | |
| Conflict of interest | | | | |
| Customer references | | | | |

### Conditions to proceed
- [condition] - owner - due

### Open questions for the partner
1. [question]
```

## Guardrails

- Do not rate an area Green without citing the evidence. No evidence means Amber at best.
- This skill organizes diligence; it does not replace your security, privacy, legal, or finance reviews. Their sign-off is required for Deep dependencies.
- Handle partner documents under NDA as confidential. Never paste them into public repos or prompts outside approved tools.
- Reputational checks use public, lawful sources only. Do not investigate individuals' private lives.
- Synthetic examples only.

## Related

- [partnership-thesis](../partnership-thesis/SKILL.md): defines the strategic fit you are testing
- [agentic-trust-agreement](../agentic-trust-agreement/SKILL.md): turns AI and data findings into contract terms
- [term-sheet-builder](../term-sheet-builder/SKILL.md): Amber mitigations often become terms
- [partnership-business-case](../partnership-business-case/SKILL.md): risk findings adjust the case
- [ai-ecosystem-partnerships](https://github.com/varunk130/ai-ecosystem-partnerships): portfolio scoring and integration launch after commitment
