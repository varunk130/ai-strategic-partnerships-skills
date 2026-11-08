# Example: Deal Structure for Northwind Data and Halcyon Cloud

Skill: [deal-structure-designer](../skills/deal-structure-designer/SKILL.md). All companies and numbers are synthetic.

## The prompt

> Northwind Data sells a revenue-forecasting product. Halcyon Cloud wants to embed our forecasting API in their analytics suite and resell it to their enterprise customers. They proposed a 70/30 revenue share in their favor with three-year exclusivity in financial services. Our list price is $40K per customer per year and serving cost is about $6K. They estimate 60 customers in year one. Help us decide what to counter with.

## The output

```markdown
## Deal Structure: Northwind Data x Halcyon Cloud

**Recommendation:** OEM embed with a per-customer wholesale fee of $22K, a 12-month ramp to a
minimum commit of 40 customers, and exclusivity limited to the top 50 financial-services
accounts, conditional on hitting the commit.
**Fallback:** revenue share at 55/45 in their favor with a $20K per-customer floor, if Halcyon
will not accept a minimum commit.

### Structures compared
| Structure | Our econ | Their econ | Risk | Effort | Lock-in | Alignment | Verdict |
|-----------|----------|------------|------|--------|---------|-----------|---------|
| Their proposal: 70/30 share + 3-yr exclusivity | Low | High | High | Low | High | Weak | Reject as-is |
| Referral fee (15%) | Medium | Low | Low | Low | None | Weak | Too small for them |
| Revenue share 55/45 + floor | Medium | Medium | Medium | Medium | Medium | Medium | Fallback |
| OEM wholesale + min commit | Medium-high | High | Medium | Medium | Medium | Strong | Recommended |

### Two-sided economics (annual, per year one volume)
| Case | Customers | Our net | Partner net | Notes |
|------|-----------|---------|-------------|-------|
| Their proposal, base | 60 | $360K | $1.68M | 30% of $2.4M, minus $6K serving each |
| OEM, low | 30 (commit applies: 40) | $700K | $320K | Halcyon pays for 40; commit protects us |
| OEM, base | 60 | $960K | $1.08M | $16K net per customer to us |
| OEM, high | 120 | $1.92M | $2.16M | Both sides scale together |

### Red flags found
- Exclusivity without minimums: three-year financial-services exclusivity with no commit
  would lock us out of the segment if Halcyon underperforms. Fix: tie exclusivity to the
  commit and narrow it to named accounts.
- Payout on bookings: their draft pays our share on bookings, not cash collected. Fix: pay on
  cash collected, monthly.
- Pass-through with no floor: a pure share lets discounting push our per-customer take below
  serving cost. Fix: $20K floor in the fallback structure.

### Open questions for the partner
- What discount authority do Halcyon sellers have on the analytics suite?
- Would they accept the commit if the ramp started after their Q2 launch?
- Who owns the customer relationship for support escalations?
```

## What to do next

Take the recommendation into [partnership-business-case](../skills/partnership-business-case/SKILL.md) for approval, then [negotiation-prep](../skills/negotiation-prep/SKILL.md) before the next session with Halcyon.
