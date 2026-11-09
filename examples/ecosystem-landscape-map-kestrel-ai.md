# Example: Ecosystem Landscape Map for Kestrel AI

Skill: [ecosystem-landscape-map](../skills/ecosystem-landscape-map/SKILL.md). All companies and numbers are synthetic.

## The prompt

> We're Kestrel AI. Our contract-review agent sells to mid-market and enterprise legal teams, and our partnership thesis says the gap is distribution inside the tools buyers already use. We have 50 named enterprise target accounts. Map the platforms, model providers, agent marketplaces, clouds, and SIs around us and tell us who to pursue first. Brightline Legal is a CLM vendor that partners with some of our customers but is also building its own review feature.

## The output

```markdown
## Ecosystem Landscape: Kestrel AI contract-review agent, 2026-11-08

Base for reach: 50 named enterprise target accounts. Priority = Reach x Fit, down one tier
if competitive risk is 1 or 2. Effort sets sequencing, not importance.

### Prioritized map
| Candidate | Layer | Reach | Fit | Effort | Comp. risk | Tier | Evidence |
|-----------|-------|-------|-----|--------|-----------|------|----------|
| Halcyon Workspace | Platform | 5 | 5 | 4 | 3 | Pursue now | 31 of 50 targets run legal ops here; MCP-compatible connector directory |
| Ardent Consulting | SI | 4 | 4 | 3 | 5 | Pursue now | Deploys legal-ops workflows at 14 of 50 targets; no review product |
| Corvid Labs | Model provider | 4 | 4 | 5 | 2 | Pursue now (guarded) | Assistant used by legal teams at 27 of 50 targets; ships a basic clause summarizer |
| Lumen Agent Hub | Agent marketplace | 3 | 4 | 5 | 5 | Build presence | Builders at 12 of 50 targets assemble workflows here; self-serve listing |
| Halcyon Cloud | Cloud | 4 | 3 | 4 | 4 | Build presence | 29 of 50 targets hold committed spend; marketplace listing is self-serve |
| Brightline Legal | ISV | 4 | 2 | 2 | 1 | Watch (guarded) | CLM at 22 of 50 targets; review feature on their public roadmap |
| Northwind Data | ISV | 2 | 1 | 3 | 5 | Skip | Sells to finance, not legal; shares buyer at 3 of 50 targets |

Priority scores: Halcyon Workspace 25, Ardent 16, Corvid Labs 16 (guarded), Lumen 12,
Halcyon Cloud 12, Brightline 8 (guarded), Northwind 2.

### Where must our capability be reachable by agents
| Surface | Why agents look here | Present today? | Action | Owner |
|---------|---------------------|---------------|--------|-------|
| Kestrel MCP server (public registry entry) | Developer and power-user agent clients connect directly | No | Ship task-shaped tools, register by 2026-12-07 | Platform eng |
| Halcyon Workspace connector directory | Workspace agents pick connectors when a user opens a contract | No | Submit for review by 2027-01-15 | Partnerships |
| Corvid Labs connector directory | Legal users ask the assistant to "review this NDA" | No | Self-serve listing; no data-sharing deal | Partnerships |
| Lumen Agent Hub | Builders search the catalog for "contract review" | No | List after MCP reliability gates pass | Product |
| Halcyon Cloud marketplace | Buyers burning commit search for approved vendors | No | Public listing for discoverability | Sales ops |

### Coopetition watchlist
- Corvid Labs: they gain a legal capability that lifts assistant usage, could build a
  deeper reviewer on top of their summarizer, we would share contract text and our
  clause taxonomy. Stance: guarded - listing only, no training-use rights, no taxonomy
  export, 12-month roadmap-notice clause if any deal follows.
- Brightline Legal: they gain review inside their CLM, could build it (it is on their
  roadmap), we would share customer playbooks. Stance: avoid a deal for now; keep the
  integration read-only and revisit at the next map refresh.
- Halcyon Workspace: they gain enterprise-tier attach, could build a basic reviewer but
  have no legal team, we would share usage telemetry. Stance: open, with eval-based
  differentiation and a roadmap-notice clause.

### Explicit no's
- Northwind Data: different buyer (finance), overlap at only 3 of 50 targets.
- Brightline Legal partnership deal: competitive risk 1 and active roadmap overlap;
  watch only until 2027-05.
```

## What to do next

Take Halcyon Workspace into [partner-due-diligence](../skills/partner-due-diligence/SKILL.md) as the first "pursue now" candidate, and plan the five agent surfaces with [agent-ecosystem-distribution](../skills/agent-ecosystem-distribution/SKILL.md).
