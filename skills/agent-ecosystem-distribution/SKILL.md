---
name: agent-ecosystem-distribution
description: 'Plans distribution of a capability through agent channels: MCP servers, model-provider connector directories, agent marketplaces, agent-to-agent integrations, and assistant extension stores, covering discoverability, reliability evals, listing requirements, telemetry, and the commercial model. Use when: agent distribution, MCP server launch, connector directory listing, agent marketplace, A2A integration, get picked by agents, tool descriptions, agentic channel strategy.'
---

# Agent Ecosystem Distribution

When an agent picks your capability and runs it inside another company's workflow, the integration is the product experience. Plan it like one.

## When to Use

- Launching an MCP server, connector, or agent integration for an existing product
- Deciding which agent channels to list in first
- Usage through agent channels is flat, erratic, or failing silently
- A partner wants to call your capability from their agent and you need terms and guardrails

## What You'll Need

**Critical inputs (ask if not provided):**

- The capability, as the jobs an agent would call it for (not the product name)
- Candidate channels, or an ecosystem landscape map that lists them
- Current API surface: auth model, rate limits, latency, error behavior

**Nice-to-have:**

- Sample agent transcripts or partner workflows where the capability would be called
- Current per-call cost, to set a floor for pricing
- Existing telemetry on API usage by client type

## Process

### Step 1: Pick channels

| Channel | How agents reach you | Who controls the listing | Best for |
|---------|---------------------|-------------------------|----------|
| MCP server (self-hosted or registry) | Agent client connects to your server | You, plus any registry rules | Developer and power-user reach |
| Model-provider connector or app directory | Users enable you inside an assistant | The provider's review process | Broad end-user reach |
| Agent marketplace | Agents or builders select you from a catalog | Marketplace operator | Builders assembling workflows |
| A2A integration | A partner's agent calls your agent directly | Bilateral agreement | Deep, high-volume partner workflows |
| Copilot or assistant extension store | Extension inside a work tool | Store operator | Buyers who live in one suite |

Start with one self-controlled channel (usually MCP) and one high-reach directory. More channels before reliability is proven multiplies failure modes.

### Step 2: Design for discoverability

Agents select tools from names, descriptions, and parameter schemas. Treat them as the storefront.

| Element | Good | Bad |
|---------|------|-----|
| Tool name | `verify_vendor_tax_id` | `northwind_api_v2` |
| Description | When to use it, what it returns, when not to use it | Marketing copy |
| Parameters | Typed, constrained, with examples | Free-text blobs |
| Tool count | A small set of task-shaped tools | One tool per endpoint |
| Errors | Actionable messages the agent can recover from | Stack traces or silent nulls |

Test selection: give a set of realistic prompts to several agent clients and record how often your tool is chosen when it should be, and not chosen when it should not.

### Step 3: Run reliability evals inside partner workflows

Unit tests on your API are not enough. Evaluate end to end in the partner's context.

| Eval | Measures | Target to set |
|------|----------|--------------|
| Selection precision and recall | Picked when right, skipped when wrong | |
| Task success | Agent completes the job using your output | |
| Latency p95 | Within the agent's timeout budget | |
| Error recovery | Agent recovers from your errors without user help | |
| Safety | No unintended writes, data leakage, or scope creep | |

Rerun on every model or client update you know about; partner model changes can break selection without any change on your side.

### Step 4: Meet listing requirements

Expect review on: security and auth (often OAuth), privacy policy and data handling, scope of permissions, uptime and support contacts, and content or brand rules. Check each channel's current terms; they change often.

### Step 5: Instrument usage telemetry

Track per channel: installs or connections, active accounts, calls per account, task success, errors by type, and conversion to paid. Tag every call with channel and client so you can tell which partner surface drives value.

### Step 6: Set the commercial model

| Model | Fits when | Risk |
|-------|----------|------|
| Free, drives core product | Channel is top of funnel | Cost of calls with no conversion |
| Usage-based per call or task | Value is per outcome | Agent loops can spike bills; add caps |
| Subscription, agent access included | Buyer already pays you | Hard to attribute channel value |
| Revenue share with channel | Marketplace handles billing | Margin and pricing control |

## Output Format

```markdown
## Agent Distribution Plan: [capability], [date]

**Core jobs agents call us for:** [job 1], [job 2], [job 3]

### Channels
| Channel | Priority | Listing owner | Launch date | Status |
|---------|---------|--------------|------------|--------|
| MCP server | 1 | Platform eng | | |
| Kestrel AI connector directory | 2 | Partnerships | | |

### Tool surface
| Tool name | Description (as agents see it) | Selection test result |
|-----------|-------------------------------|----------------------|

### Reliability gates (must pass before listing)
- Selection precision >= [x]% | Task success >= [x]% | p95 latency <= [x]s

### Telemetry
- Dashboard: [link] | Tags: channel, client, partner workflow

### Commercial model
- [model], with caps of [x] per account per day; review at [date]

### Risks
- [risk]: [mitigation]
```

## Guardrails

- Do not game tool descriptions to win selection for tasks you cannot do well. Wrong selection damages trust with the agent operator and the user.
- Do not list in a channel before reliability gates pass; a public failure in a partner workflow is your failure.
- Scope permissions to the minimum the job needs; any write action should be explicit and reversible where possible.
- Listing terms, fees, and review rules vary by channel and change often. Check current terms; do not quote them from memory.

## Related

- [ecosystem-landscape-map](../ecosystem-landscape-map/SKILL.md): find the agent surfaces where you must be reachable
- [agentic-trust-agreement](../agentic-trust-agreement/SKILL.md): define liability, data, and action limits with the partner
- [cloud-marketplace-gtm](../cloud-marketplace-gtm/SKILL.md): when the agent channel bills through a cloud marketplace
- [deal-structure-designer](../deal-structure-designer/SKILL.md): structure revenue share for A2A deals
- [integration-launch-plan](https://github.com/varunk130/ai-ecosystem-partnerships/blob/main/skills/integration-launch-plan/SKILL.md): run the launch itself
