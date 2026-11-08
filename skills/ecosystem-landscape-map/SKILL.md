---
name: ecosystem-landscape-map
description: 'Maps the platforms, model providers, agent marketplaces, clouds, SIs, and ISVs around a product, rates each on reach, fit, integration effort, and competitive risk, and outputs a prioritized map that names where the capability must be reachable by agents. Use when: ecosystem map, partner landscape, who should we partner with, map the ecosystem, partner target list, coopetition analysis, where do agents find us.'
---

# Ecosystem Landscape Map

See the whole field before picking partners, so priorities follow reach and fit rather than whoever called last.

## When to Use

- Annual partnership planning, or entering a new segment
- After a partnership thesis names an archetype and you need candidates
- A new agent surface or marketplace appears and you need to know if it matters
- Leadership asks "who are the right partners for us?" and there is no shared list

## What You'll Need

**Critical inputs (ask if not provided):**

- The product or capability being mapped, in one sentence
- The target customer segment and where those buyers already work (tools, clouds, assistants)
- Known competitors, including partners who also compete

**Nice-to-have:**

- Existing partner list and current status per partner
- Data on where current customers run workloads and which assistants or agents they use
- A partnership thesis for the gap being closed

## Process

### Step 1: Enumerate by layer

List candidates in each layer. Aim for breadth first; cut later.

| Layer | What to list | Example (synthetic) |
|-------|-------------|---------------------|
| Platforms | Systems of record and work your buyers live in | Halcyon Workspace |
| Model providers | Providers whose apps, connectors, or tool directories reach users | Kestrel AI |
| Agent marketplaces | Directories and stores where agents or users pick tools | Lumen Agent Hub |
| Clouds | Hyperscalers where buyers hold committed spend | Halcyon Cloud |
| SIs | Integrators who deploy into your segment | Ardent Consulting |
| ISVs | Adjacent software sharing your buyer | Northwind Data |

### Step 2: Rate each candidate

Score 1 to 5. Write one line of evidence per score; a score without evidence is a guess.

| Dimension | 1 | 5 |
|-----------|---|---|
| Reach | Few of our target buyers | Most target buyers, or their agents, pass through it |
| Strategic fit | Tangential to the thesis | Closes the named gap directly |
| Integration effort | Months of custom work (score low) | Standard protocol or existing connector (score high) |
| Competitive risk | Clear competitor or likely to absorb us (score low) | No overlap now or on their roadmap (score high) |

Priority score = Reach x Fit, adjusted down by one tier if competitive risk is 1 or 2. Keep effort visible separately; it sets sequencing, not importance.

### Step 3: Call out coopetition explicitly

For every candidate with competitive risk of 2 or less, answer: what do they gain from our success, what stops them building it, and what data would we hand them? If the answers are "little, nothing, a lot", mark it **guarded** regardless of reach.

### Step 4: Mark the agent-reachability requirements

Ask: when a buyer's agent is solving a problem we solve, where does it look? List each surface where the capability must be callable (MCP server registries, model-provider connector directories, agent marketplaces, assistant extension stores, cloud marketplaces). A surface with high reach and no presence from us is a gap, even if no partner deal is needed to fill it.

### Step 5: Prioritize into tiers

| Tier | Rule | Motion |
|------|------|--------|
| Pursue now | High priority, effort acceptable | Thesis, outreach, business case |
| Build presence | Agent surface, self-serve listing | Ship listing and integration, no deal needed |
| Watch | High reach, low fit or guarded | Monitor quarterly, no investment |
| Skip | Low reach and low fit | Say no explicitly |

## Output Format

```markdown
## Ecosystem Landscape: [product], [date]

### Prioritized map
| Candidate | Layer | Reach | Fit | Effort | Comp. risk | Tier | Evidence |
|-----------|-------|-------|-----|--------|-----------|------|----------|
| Halcyon Cloud | Cloud | 5 | 4 | 4 | 4 | Pursue now | 60% of ICP runs here |
| Kestrel AI | Model provider | 4 | 4 | 5 | 2 | Pursue now (guarded) | Ships adjacent feature |
| Lumen Agent Hub | Agent marketplace | 3 | 4 | 5 | 5 | Build presence | Self-serve listing |

### Where must our capability be reachable by agents
| Surface | Why agents look here | Present today? | Action | Owner |
|---------|---------------------|---------------|--------|-------|

### Coopetition watchlist
- [candidate]: they gain [x], could build [y], we would share [z]. Stance: [open / guarded / avoid]

### Explicit no's
- [candidate]: [reason]
```

## Guardrails

- Do not inflate reach from vanity numbers; tie it to target buyers or agent traffic.
- Do not hide competitive risk to make a big-name partner look attractive. Guarded is a valid tier.
- The map is a snapshot; date it and refresh at least twice a year, since agent surfaces change fast.
- Use synthetic names in shared examples. Never present estimates as a partner's actual numbers.

## Related

- [partnership-thesis](../partnership-thesis/SKILL.md): defines the gap and archetype this map fills
- [agent-ecosystem-distribution](../agent-ecosystem-distribution/SKILL.md): plan the "build presence" agent surfaces
- [cloud-marketplace-gtm](../cloud-marketplace-gtm/SKILL.md): plan the cloud layer
- [partner-due-diligence](../partner-due-diligence/SKILL.md): vet a "pursue now" candidate
- [partner-fit-scorecard](https://github.com/varunk130/ai-ecosystem-partnerships/blob/main/skills/partner-fit-scorecard/SKILL.md): score the portfolio once partners are active
