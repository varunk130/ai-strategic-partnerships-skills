# Example: Renewal Review of Ardent Procurement and Northwind Supply

Skill: [partnership-renewal-review](../skills/partnership-renewal-review/SKILL.md). All companies and numbers are synthetic.

## The prompt

> We're Ardent Procurement. Our purchasing agent has placed orders in the Northwind Supply portal for two years under the agentic trust agreement, and the term ends 2028-12-31 with 90 days notice. The business case planned 40 joint customers, $60M of agent-placed orders, and $600K in fees to us at 1% of order value, on $350K of investment. We're at 34 customers, $48M, and $480K, and we spent $410K. Northwind's approval-token check went live three months late, and a lot of orders hit the $25K per-order limit. Should we renew?

## The output

```markdown
# Renewal Review: Northwind Supply
Term end: 2028-12-31 | Notice deadline: 2028-10-02 | Recommendation: Renegotiate

## Performance vs thesis
| Target | Planned | Actual | % |
|--------|---------|--------|---|
| Joint pipeline (customers in active evaluation) | 60 | 51 | 85% |
| Attributable revenue (1% fee on agent orders) | $600K | $480K | 80% |
| Agent-placed order value | $60M | $48M | 80% |
| Joint customers live | 40 | 34 | 85% |
| Integration adoption (share of POs placed by agent) | 70% | 62% | 89% |
| Leading indicators hit | 5 of 5 | 4 of 5 | 80% |
Thesis status: holds - customers who switched from emailed PDFs to the agent stayed and moved
most of their orders over, and order accuracy ran at 99.7%. The miss traces to two fixable
causes: the approval-token check went live 2027-03-15 instead of 2026-12-15, and 22% of agent
orders exceeded the $25K per-order limit and waited a median 2.5 days for buyer approval. The
missed leading indicator is median order cycle time: planned under 1 day, actual 1.6 days.

## Economics
Invested: $410K vs planned $350K | Return: $480K vs planned $600K
Net: $70K realized vs $250K planned. The $60K overrun (17% over plan) is the manual review
queue Ardent staffed for three months while the approval token was not enforced in code.

## Strategic relevance
Yes, we would sign today. Northwind is the third-largest supplier across our customer base,
and our customers asked for this integration by name. The only alternative supplier API,
Harrow Industrial Supply, cannot enforce approval tokens, so switching would recreate the
problem that cost us three months. One watch item: Northwind launched its own buyer
assistant in 2028, limited to catalog search. It does not place orders today; we want 12
months notice if that changes.

## Relationship and switching costs
| Factor | Rating | Evidence |
|--------|--------|----------|
| Exec sponsorship on both sides | 4 | Quarterly exec reviews held 7 of 8 quarters |
| Commitments met by partner | 3 | Approval token 3 months late; audit log and revocation drills on time |
| Commitments met by us | 4 | Evals shared every quarter; one model-change notice sent 21 days out, not 30 |
| Field team engagement | 3 | 6 of 9 Northwind account managers active in joint deals |
| Customer dependency on integration | 5 | 34 customers route 62% of POs through the agent |
| Cost to replace or rebuild | 4 | New supplier integration estimated at 9 months and $300K |
| Contract exit cost | 2 | No exit fee; 90 days notice; 7-year order data retention continues |

## Recommendation
Renegotiate because the thesis holds and customers depend on the integration, but the
spending limits and the cost of Northwind's late delivery make the current terms
underperform. Renew for two years only with these changes:
- Raise the per-order limit to $50K and the daily limit to $200K per customer for customers
  with 6 months of clean audit history; keep $25K and $100K for new customers.
- Northwind credits Ardent $60K against year-three fees for the delayed approval token.
- Add a delivery date to every control Northwind commits to, with a fee credit if one slips
  by more than 30 days.
- Add 12 months notice before Northwind's buyer assistant places orders.
- Keep the 1% fee; shipping-address changes and price edits stay prohibited for the agent.
If Northwind declines the limit change and the credit by 2028-09-30, rerun this review as
Sunset before the 2028-10-02 notice deadline.

## Wind-down plan (sunset only)
Not applicable: the decision is Renegotiate. If the review is rerun as Sunset, the
34 live customers are the first rows of the joint customer list.
```

## What to do next

Brief Ardent's executive sponsor with [partner-exec-briefing](../skills/partner-exec-briefing/SKILL.md) before the terms are raised with Northwind's exec, then plan the limit change and credit as trades in [negotiation-prep](../skills/negotiation-prep/SKILL.md). Raise the limits only after the new thresholds are enforced in code by the approval token, as the [agentic trust agreement](agentic-trust-agreement-procurement.md) requires.
