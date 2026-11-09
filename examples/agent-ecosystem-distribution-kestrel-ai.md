# Example: Agent Ecosystem Distribution for Kestrel AI

Skill: [agent-ecosystem-distribution](../skills/agent-ecosystem-distribution/SKILL.md). All companies and numbers are synthetic.

## The prompt

> Kestrel AI wants agents to call our contract-review capability. Plan is an MCP server first, then the Halcyon Workspace connector directory, then Lumen Agent Hub. Our API uses OAuth, allows 20 requests per second per account, p95 latency is 6.2s on a 30-page contract, and a review costs us about $0.60 in compute. We ran 50 test prompts per tool across three agent clients. Draft the distribution plan.

## The output

```markdown
## Agent Distribution Plan: Kestrel contract review, 2026-11-08

**Core jobs agents call us for:** extract key clauses from a contract, flag risky terms
against a standard, compare a contract to the customer's negotiation playbook,
summarize a contract for an approver

### Channels
| Channel | Priority | Listing owner | Launch date | Status |
|---------|---------|--------------|------------|--------|
| Kestrel MCP server | 1 | Platform eng | 2026-12-07 | Beta with 6 design partners |
| Halcyon Workspace connector directory | 2 | Partnerships | 2027-01-25 | Submission drafted; OAuth review pending |
| Lumen Agent Hub | 3 | Product | 2027-03-01 | Not started; gated on channel 1 evals |

### Tool surface
Selection test: 50 prompts per tool across three agent clients, 30 where the tool
should be picked and 20 where it should not.
| Tool name | Description (as agents see it) | Selection test result |
|-----------|-------------------------------|----------------------|
| `extract_contract_clauses` | Returns parties, term, renewal, termination, liability cap, and governing law with page refs. Use on a single signed or draft contract. Not for comparing two documents. | Picked 29/30, false picks 2/20; precision 29/31 = 93.5% |
| `flag_risky_terms` | Flags clauses that deviate from a chosen standard (mutual NDA, SaaS MSA, DPA) with severity and reason. Not legal advice; returns no edits. | Picked 27/30, false picks 1/20; precision 27/28 = 96.4% |
| `compare_to_playbook` | Compares a contract to the customer's stored playbook and lists each fallback position triggered. Requires a playbook ID. | Picked 24/30, false picks 0/20; precision 100%, recall 80%: rewrite description |
| `summarize_for_approval` | One-page summary of commercial and legal terms for a non-lawyer approver. Read-only. | Picked 28/30, false picks 3/20; precision 28/31 = 90.3% |

All four tools are read-only. No tool writes to the contract or the customer's system.

### Reliability gates (must pass before listing)
- Selection precision >= 90% | Task success >= 85% | p95 latency <= 8s
- Also: recall >= 85% per tool, and agent recovers from our errors without user help
  in >= 90% of injected-error runs
- Current: all four tools pass precision; `compare_to_playbook` fails recall (80%);
  task success 88% on 120 end-to-end runs (106/120); p95 6.2s. Re-test after the
  description rewrite and on every known client model update.

### Telemetry
- Dashboard: internal agent-channels dashboard | Tags: channel, client, partner workflow
- Per channel: connections, active accounts, calls per account, task success, errors by
  type, conversion to paid seats

### Commercial model
- Usage-based at $3.00 per contract reviewed (cost $0.60, so 80% gross margin per
  review), included free for existing seat customers up to their seat allowance
- Caps of 200 reviews per account per day (max $600 per account per day) to contain
  agent loops; review at 2027-03-31
- Revenue share with Lumen Agent Hub only if it bills; check its current terms first

### Risks
- Partner model update breaks tool selection: rerun selection tests on each known
  update; alert if weekly selection rate drops more than 10% in any channel
- Agent loops spike usage: per-account daily cap plus a duplicate-document check
- Contract text leaves customer control: no retention beyond 30 days, no training use,
  terms set in an [agentic trust agreement](../skills/agentic-trust-agreement/SKILL.md)
- Directory review slips: MCP channel carries launch; Halcyon date moves, not the eval bar
```

## What to do next

Set data, liability, and action limits with Halcyon Workspace using [agentic-trust-agreement](../skills/agentic-trust-agreement/SKILL.md) before submitting the listing. If Lumen Agent Hub bills through a cloud marketplace, plan that route with [cloud-marketplace-gtm](../skills/cloud-marketplace-gtm/SKILL.md).
