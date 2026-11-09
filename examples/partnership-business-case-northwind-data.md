# Example: Business Case for the Northwind Data x Halcyon Cloud OEM Deal

Skill: [partnership-business-case](../skills/partnership-business-case/SKILL.md). All companies and numbers are synthetic.

## The prompt

> We're Northwind Data. We want CRO approval to counter Halcyon Cloud with the OEM structure from our deal-structure work: $22K wholesale per customer against our $40K list, $6K serving cost, a 40-customer minimum commit, exclusivity only on the top 50 financial-services accounts. We'd need a partner manager, a solutions engineer, an integration build, and some launch MDF. Diligence came back Amber with one Red on data handling. Write the approval memo for the 2026-11-17 decision.

## The output

```markdown
# Business Case: Halcyon Cloud partnership
Decision-maker: Morgan Reyes, CRO | Decision date: 2026-11-17 | Author: Head of Partnerships

## The ask
Approve 2 FTE, $80K of engineering, and $60K of MDF ($540K cash in year one), plus authority
to sign an OEM deal at no less than $22K wholesale per customer with a 40-customer minimum
commit, for a two-year term, to reach 60 financial-services customers through Halcyon in year one.

## Problem and thesis
We cannot reach enterprise financial-services buyers at scale: they buy forecasting inside the
analytics suite they already run, and our direct team closed 9 such accounts this year. Halcyon
launches a forecasting module in Q2 and needs a proven engine now. Embedding ours gives us
distribution into 31 of our top 50 target accounts without building a channel ourselves.

## Options considered
| Option | Cost | Time to value | Verdict |
|--------|------|---------------|---------|
| Do nothing | $0 | n/a | We stay at about 9 FS accounts a year and Halcyon picks another engine |
| Build: dedicated FS direct team | $1.2M a year for 6 sellers | 12-18 months | Slow, and still outside the suite |
| Buy: acquire a small analytics suite | $15M+ | 12 months | No credible target |
| Partner: Halcyon Cloud OEM | $540K cash plus discount | 4-6 months | Recommended |
| Partner: Bramblefield Analytics revenue share | About $400K cash | 6-9 months | Smaller FS footprint; keep as BATNA |

## Investment
| Line | Year 1 | Year 2 |
|------|--------|--------|
| Partner team: 2 FTE x $200K loaded | $400K | $400K |
| Engineering: 16 weeks build, then 6 weeks maintenance, at $5K a week | $80K | $30K |
| MDF: launch campaign, committed | $60K | $40K |
| Discount given up: $18K below list x 60 base customers | $1.08M | $1.08M |
| Marketplace or platform fees | $0 | $0 |
| Total | $1.62M | $1.55M |
Total: $3.17M over two years, of which $1.01M is cash and $2.16M is discount given up.
The discount is non-cash and is already reflected because revenue below is counted at $22K
wholesale, so it is not subtracted a second time.

## Expected return
| | Low | Base | High |
|---|-----|------|------|
| Joint opportunities created | 100 | 150 | 240 |
| Win rate on joint deals | 30% | 40% | 50% |
| Customers live (year one) | 30 (billed at 40 commit) | 60 | 120 |
| Average deal size to us | $22K | $22K | $22K |
| Attributable revenue | $880K | $1.32M | $2.64M |
| Less serving cost ($6K x customers live) | $180K | $360K | $720K |
| Contribution | $700K | $960K | $1.92M |
| Net return after $540K cash investment | $160K | $420K | $1.38M |
| Payback at full run rate (months) | 9.3 | 6.8 | 3.4 |
Key assumptions:
- Opportunity counts: Halcyon's pipeline estimate (base), cut by a third for low; a guess for high
- Win rates: our pilot rate inside a partner suite was 40%; low and high are plus or minus 10 points
- Base of 60 customers is Halcyon's estimate, not ours; diligence found 22 named opportunities behind it
- $22K wholesale, $40K list, $6K serving cost: deal-structure analysis and finance's cost model
- Low case depends on the commit: without it, 30 customers x $16K = $480K, a $60K loss

## Leading indicators
| Day | Indicator | Target |
|-----|-----------|--------|
| 90 | Integration live in the Halcyon suite, Halcyon sellers trained | Live, 20 trained |
| 90 | Joint FS accounts mapped and engaged | 15 |
| 180 | Qualified joint opportunities | 60 |
| 180 | Joint customers live | 5 |

## Kill criteria
- Integration not live by 2027-03-01 triggers a scope reset
- Fewer than 18 qualified joint opportunities (30% of the day-180 target) by 2027-05-31 triggers a kill review
- No joint customer live by 2027-05-31 triggers a kill review
- Training-use clause not removed before signature triggers a stop

## Risks
| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| Halcyon trains on our forecast outputs | Medium | High | No-training clause required before signature | Legal |
| Halcyon replaces us with its in-house beta | Medium | High | 12-month roadmap notice; exclusivity only while the commit is met | Partnerships |
| Assistant summaries misstate forecasts (4.5% in our test) | High | Medium | Raw figures beside every summary; quarterly joint evals | Data science |
| Halcyon discounts below our economics | Low | Medium | Fixed wholesale fee; $16K floor in the fallback | Finance |

## What we are not asking for
Exclusivity beyond the top 50 named FS accounts, any term over two years, payment on bookings
rather than cash collected, or headcount beyond the 2 FTE above.
```

## What to do next

Once approved, prepare the Halcyon session with [negotiation-prep](../skills/negotiation-prep/SKILL.md), then put the agreed terms into [term-sheet-builder](../skills/term-sheet-builder/SKILL.md).
