# Example: Cloud Marketplace GTM for Northwind Data

Skill: [cloud-marketplace-gtm](../skills/cloud-marketplace-gtm/SKILL.md). All companies and numbers are synthetic.

## The prompt

> Northwind Data sells a revenue-forecasting SaaS product. Enterprise deals average $60K per year and the product runs in our own cloud account. Nine open deals have asked to buy through their cloud marketplace, most of them on Halcyon Cloud, where they hold committed spend. A few are on Meridian Cloud. We list at the same price direct and want to keep it that way. Plan our marketplace go-to-market.

## The output

```markdown
## Cloud Marketplace GTM Plan: Northwind revenue forecasting, 2026-11-08

**Clouds in scope:** Halcyon Cloud (primary), Meridian Cloud (later)
**Buying motive:** committed-spend drawdown, with procurement shortcut as a secondary motive
**Evidence:** 9 open deals asked to buy via marketplace, $540K in pipeline (7 on Halcyon
Cloud = $420K, 2 on Meridian Cloud = $120K; average $60K per deal)

### Listings
| Cloud | Listing type | Price model | Metering | Live date | Owner |
|-------|-------------|------------|---------|----------|-------|
| Halcyon Cloud | Public SaaS listing | Annual contract from $40K, same as direct list | None for flat contract | 2026-12-15 | Product marketing |
| Halcyon Cloud | Private offer | Negotiated annual contract, multi-year schedule allowed | Forecast-run overage reported via metering API, automated | 2027-01-15 | Deal desk |
| Meridian Cloud | Public SaaS listing | Annual contract from $40K | None for flat contract | 2027-Q2 | Product marketing |
| Halcyon Cloud | Channel partner private offer (Ardent Consulting) | Ardent sets its margin on top of our price | As above | 2027-Q2, after first direct offers | Partner manager |

### Co-sell eligibility
| Requirement (per current terms) | Status | Owner | Due |
|-------------------------------|-------|------|-----|
| Technical validation of the integration | Not started; confirm current checklist | Solutions eng | 2027-01-31 |
| Transactable listing live | Public listing in build | Product marketing | 2026-12-15 |
| Marketplace revenue or referenced customers (threshold to confirm) | 0 today; target 4 offers in 90 days | Sales lead | 2027-02-06 |
| Joint solution content | Draft one-pager on forecasting with Halcyon Cloud data services | Partner marketing | 2027-01-31 |

### Economics
- Fee assumption: 5% (planning placeholder only; verify against current program terms)
- Net margin impact per $100k deal: -$5,000. Net revenue $95,000; with serving cost at
  15% of contract value ($15,000), contribution falls from $85,000 direct to $80,000
- Per average $60K deal: fee $3,000, serving cost $9,000, contribution $48,000 vs
  $51,000 direct
- On the $540K pipeline, if all 9 transact: fees of $27,000 at the placeholder rate
- Price parity kept: we absorb the fee rather than gross up the marketplace price
- Revenue recognition (gross vs net) and tax: flagged to finance and legal, not decided here

### Internal motion
- Private offers filed by: deal desk, SLA 2 business days from pricing approval
- Seller credit: marketplace deals count toward quota at the same rate as direct, no
  deduction for the fee
- Deal registration: partner manager registers with Halcyon Cloud at stage 3 (technical win)
- CRM tracking: transaction route, cloud, offer ID, commit-drawdown eligible (Y/N)
- Discount approval: same thresholds as direct; the marketplace fee is not a discount
- Commit eligibility: confirm per buyer with the cloud account team before quoting it

### 90-day targets
- 4 private offers transacted | $240K marketplace revenue (4 x $60K) | 3 co-sell referrals
- Checkpoint 2027-02-06 (90 days): if fewer than 2 offers have transacted, review seller
  credit and offer turnaround before adding Meridian Cloud
```

## What to do next

Model the fee and channel-partner margin in [partnership-business-case](../skills/partnership-business-case/SKILL.md), and use [deal-structure-designer](../skills/deal-structure-designer/SKILL.md) to set Ardent Consulting's margin before the channel partner private offer goes live.
