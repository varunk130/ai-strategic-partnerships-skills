---
name: cloud-marketplace-gtm
description: 'Plans go-to-market through hyperscaler cloud marketplaces: listing types, committed-spend drawdown, co-sell eligibility, pricing and metering, fees, and the internal motion for private offers and seller credit. Use when: cloud marketplace, marketplace listing, private offer, committed spend, cloud co-sell, sell through the cloud, marketplace GTM, transact through marketplace.'
---

# Cloud Marketplace GTM

Decide whether, how, and on which cloud marketplace to transact, and build the internal motion so deals actually close there.

## When to Use

- Buyers ask to purchase through their cloud provider
- Deals stall in procurement and the buyer has committed cloud spend to burn
- Planning co-sell with a cloud partner's field team
- Marketplace listing exists but few deals transact through it

## What You'll Need

**Critical inputs (ask if not provided):**

- Which clouds your target buyers hold committed spend on, and roughly how much
- Your pricing model (subscription, usage, hybrid) and typical deal size
- Where the product runs: in your cloud, the buyer's account, or both

**Nice-to-have:**

- Pipeline that has asked for marketplace purchase
- Current reseller or channel partners who may want to transact
- Finance and legal owners for contracts and revenue recognition

## Process

### Step 1: Confirm the buying motive

Marketplace transactions are worth the effort when at least one of these holds. If none do, list for discoverability and stop there.

| Motive | Signal | Strength |
|--------|-------|---------|
| Committed-spend drawdown | Buyer has a cloud commit and eligible purchases count against it | Strongest |
| Procurement shortcut | Buyer can skip new vendor onboarding | Strong |
| Consolidated billing | Buyer wants one invoice | Moderate |
| Cloud field co-sell | Cloud sellers get credit when your deal transacts | Strong if eligible |

Check current program terms for which purchases count toward commitments; rules differ by cloud and change.

### Step 2: Pick listing types

| Listing type | Use for | Notes |
|-------------|--------|------|
| Public SaaS listing | Self-serve and discoverability | Public price; fine for small deals |
| Private offer | Negotiated enterprise deals | Custom price, terms, and schedule per buyer |
| Consulting or channel partner private offer | A reseller or SI transacts on your behalf | Partner sets their margin; check current program terms |
| Container or deployable listing | Product runs in buyer's account | Extra packaging and security review |

### Step 3: Check co-sell eligibility

Co-sell programs usually require some combination of a technical validation, a listing that can transact, a minimum of marketplace revenue or referenced customers, and joint solution content. Map each requirement to an owner and date. Check current program terms; do not assume last year's requirements.

### Step 4: Set pricing and metering

| Decision | Options | Recommendation |
|---------|--------|---------------|
| Price dimension | Per seat, per unit of usage, tiered, flat contract | Match your direct price list to avoid channel conflict |
| Metering | Report usage to the marketplace via its metering API | Automate; manual reporting breaks at scale |
| Fees | Marketplace keeps a percentage; private offers may differ | Check current program terms; model fees into deal margin |
| Price parity | Same price direct and marketplace | Default yes; gross up only with a stated reason |

### Step 5: Build the internal motion

| Question | Decide |
|---------|-------|
| Who files private offers? | Usually deal desk or sales ops, not the AE |
| Turnaround SLA | e.g. offer issued within 2 business days of approval |
| How do sellers get credit? | Marketplace deals count toward quota the same as direct |
| Who registers deals with the cloud? | Partner manager, at stage [x] |
| How is revenue recognized? | Finance confirms gross vs net treatment |
| Where is it tracked? | CRM field: transaction route, cloud, offer ID |

Sellers avoid motions that hurt their comp. Fix credit before launch.

## Output Format

```markdown
## Cloud Marketplace GTM Plan: [product], [date]

**Clouds in scope:** Halcyon Cloud (primary), [second cloud] (later)
**Buying motive:** [committed-spend drawdown / procurement / co-sell]
**Evidence:** [n] open deals asked to buy via marketplace, [$] in pipeline

### Listings
| Cloud | Listing type | Price model | Metering | Live date | Owner |
|-------|-------------|------------|---------|----------|-------|

### Co-sell eligibility
| Requirement (per current terms) | Status | Owner | Due |
|-------------------------------|-------|------|-----|

### Economics
- Fee assumption: [x]% (verify against current program terms)
- Net margin impact per $100k deal: [$]

### Internal motion
- Private offers filed by: [team], SLA [x] days
- Seller credit: [rule]
- Deal registration: [owner, stage]
- CRM tracking: [fields]

### 90-day targets
- [n] private offers transacted | [$] marketplace revenue | [n] co-sell referrals
```

## Guardrails

- Do not quote marketplace fees, commit eligibility, or co-sell program names as fact; they vary by cloud and change. Always point to current program terms.
- Do not price the marketplace above direct without a stated reason; buyers notice and procurement escalates.
- Revenue recognition and tax treatment are finance and legal calls; flag them, do not decide them.
- Use synthetic examples; never name a real cloud partner's internal program data.

## Related

- [ecosystem-landscape-map](../ecosystem-landscape-map/SKILL.md): confirm which clouds your buyers use
- [deal-structure-designer](../deal-structure-designer/SKILL.md): structure reseller and channel margins
- [partnership-business-case](../partnership-business-case/SKILL.md): model marketplace economics
- [agent-ecosystem-distribution](../agent-ecosystem-distribution/SKILL.md): when agent channels bill through the marketplace
- [co-sell-account-mapping](https://github.com/varunk130/ai-ecosystem-partnerships/blob/main/skills/co-sell-account-mapping/SKILL.md): pick target accounts with the cloud field team
- [joint-business-plan](https://github.com/varunk130/ai-ecosystem-partnerships/blob/main/skills/joint-business-plan/SKILL.md): set joint targets with the cloud partner
