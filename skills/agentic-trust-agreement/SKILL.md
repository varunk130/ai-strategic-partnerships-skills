---
name: agentic-trust-agreement
description: 'Defines shared-responsibility terms when one company''s AI agent acts inside another company''s systems, producing a responsibilities matrix and a readiness checklist. Use when: agent-to-agent partnership, partner agent access, AI agent in our systems, agent permissions, shared responsibility model, agent governance terms, agentic integration risk.'
---

# Agentic Trust Agreement

Agree who is responsible for what before a partner's agent takes actions in our systems, or ours in theirs.

## When to Use

- A partner's AI agent will read, write, or transact in our product, APIs, or customer tenants
- Our agent will operate inside a partner's platform or marketplace
- A pilot is moving from sandbox to production data
- An incident or model change exposed gaps in an existing agent integration

## What You'll Need

**Critical inputs (ask if not provided):**

- Which agents, on which side, and what each is meant to do (synthetic in examples, e.g. "Northwind Data's reconciliation agent")
- Systems and data the agent will touch
- Who on each side owns security, legal, and the integration

**Nice-to-have:**

- Existing data processing or API terms between the parties
- The agent's evaluation results and model/version history
- Customer contracts that limit automated actions

## Process

### Step 1: Inventory permitted actions per agent

List every action, not every capability. Default deny anything not listed.

| Agent | Action | System | Read / write / transact | Reversible? | Approval needed |
|-------|--------|--------|------------------------|-------------|-----------------|
| Northwind recon agent | Read invoices | Our billing API | Read | n/a | No |
| Northwind recon agent | Flag mismatch | Our billing API | Write | Yes | No |
| Northwind recon agent | Issue credit | Our billing API | Transact | No | Human, above threshold |

### Step 2: Define agent identity and authentication

Each agent gets its own identity, never a shared human account. Agree on credential type, scope, rotation period, how the agent identifies itself per request, and how either side revokes access within minutes.

### Step 3: Map data flows and retention

For each flow: what data, which direction, where it is processed, whether it can be used for model training, and how long each side keeps it. Training use defaults to no unless agreed in writing.

### Step 4: Set human approval thresholds

| Trigger | Threshold | Approver | Response time |
|---------|-----------|----------|---------------|
| Monetary action | Over [amount] | Customer admin | |
| Irreversible change | Any | Our ops on-call | |
| Bulk action | Over [n] records | Partner owner | |
| Low confidence | Below [score] | Queue for review | |

### Step 5: Agree audit trails and incident response

Both sides must be able to inspect a shared log: agent identity, model version, action, input reference, outcome, approver. Then agree severity levels, notification windows, who can pause the agent, and who tells affected customers.

### Step 6: Require change notice and evaluation evidence

Model or prompt changes can alter behavior without a code change. Agree notice periods for model/version changes, which changes need re-evaluation, and what evidence (task success, error rates, red-team results) is shared before and after.

### Step 7: Assign responsibilities

Build the matrix in the output. Every row needs exactly one accountable party, even when work is joint.

## Output Format

```markdown
# Agentic Trust Agreement: [Us] x [Partner]
Agents in scope: [list] | Systems: [list] | Status: draft for security and legal review

## Responsibilities matrix
| Area | Us | Partner | Joint | Accountable |
|------|----|---------|-------|-------------|
| Permitted action list | | | | |
| Agent identity and credentials | | | | |
| Credential revocation | | | | |
| Data flows and retention | | | | |
| Training-use restrictions | | | | |
| Human approval enforcement | | | | |
| Audit log storage and access | | | | |
| Incident detection | | | | |
| Agent pause / kill switch | | | | |
| Customer notification | | | | |
| Model/version change notice | | | | |
| Evaluation evidence | | | | |

## Readiness checklist
- [ ] Every agent action listed; unlisted actions denied
- [ ] Each agent has its own identity and scoped credentials
- [ ] Revocation tested end to end
- [ ] Data retention and training use agreed in writing
- [ ] Approval thresholds enforced in code, not policy alone
- [ ] Shared audit log live and inspectable by both sides
- [ ] Incident runbook with named contacts and notice windows
- [ ] Model change notice period agreed: [n] days
- [ ] Baseline evaluation evidence exchanged
- [ ] Security and legal sign-off recorded

## Open issues
| Issue | Owner | Due |
```

## Guardrails

- This is not legal advice. Security and legal teams own the final terms; this skill produces a working draft for them.
- Do not approve production access with any checklist item open; flag it as a blocker.
- Never let an agent inherit a human's credentials or broader permissions than its action list.
- Do not assume the partner's evaluation results; ask for the evidence.

## Related

- [partner-due-diligence](../partner-due-diligence/SKILL.md): security and AI practices review before this agreement
- [agent-ecosystem-distribution](../agent-ecosystem-distribution/SKILL.md): when the agent is distributed through a partner platform
- [term-sheet-builder](../term-sheet-builder/SKILL.md): carrying agreed terms into the deal
- [Integration launch plan](https://github.com/varunk130/ai-ecosystem-partnerships/blob/main/skills/integration-launch-plan/SKILL.md): gating launch on this checklist
