# Example: Term Sheet for Northwind Data and Halcyon Cloud

Skill: [term-sheet-builder](../skills/term-sheet-builder/SKILL.md). All companies and numbers are synthetic.

## The prompt

> We're Northwind Data. We countered Halcyon Cloud's 70/30 revenue-share proposal with an OEM structure: a $22K per-customer wholesale fee, a 12-month ramp to a 40-customer minimum commit, exclusivity limited to the top 50 financial-services accounts and only while they hit the commit, and payment on cash collected. Halcyon wants to see it on paper. Draft the term sheet so we can align internally before counsel reviews it. Halcyon will send customer financial data to our API, so the data and model terms matter.

## The output

```markdown
# Term Sheet (Non-Binding): Northwind Data and Halcyon Cloud
Draft 1, 2026-11-18. For discussion only. Subject to definitive agreement and counsel review.

| # | Term | Proposed position | Mark | If traded, we want |
|---|------|-------------------|------|--------------------|
| 1 | Parties | Northwind Data, Inc. and Halcyon Cloud, Inc. Halcyon affiliates covered only if they resell the analytics suite; excludes any affiliate offering a competing forecasting model | Tradeable | Named affiliate list in a schedule |
| 2 | Scope | Northwind forecasting API embedded in the Halcyon analytics suite and resold to Halcyon enterprise customers. Out: standalone resale, other Halcyon products, white-labeling the Northwind UI | Tradeable | Adding Halcyon's planning module raises the commit by 10 customers |
| 3 | Exclusivity | Limited to the top 50 financial-services accounts on a named list (Schedule A). Applies only while Halcyon meets the minimum commit; lapses if Halcyon is below commit for two consecutive quarters. No exclusivity outside the list | Must-have | - |
| 4 | Territory | North America and UK, through Halcyon direct sales and Halcyon's cloud marketplace listing. Other regions by written amendment | Tradeable | Halcyon funds first-line support in any new region |
| 5 | Economics | OEM wholesale fee of $22K per customer per year; Halcyon sets its own resale price. 12-month ramp from Halcyon commercial launch, then a minimum commit of 40 customers ($880K per year). Paid monthly on cash collected, net 30 | Must-have | Only if the commit is refused: 50/50 revenue share with a $16K per-customer floor and no exclusivity |
| 6 | IP rights | Each party keeps pre-existing IP. Northwind owns its forecasting models and all improvements to them; Halcyon owns the suite and the integration code it writes. No joint IP planned; any joint work needs a separate written agreement with a license-back | Must-have | - |
| 7 | Data rights | Halcyon sends customer financial time-series solely to receive forecasts. Northwind retains inputs 30 days for support, then deletes; full deletion within 30 days of termination, with written certification. Northwind may share only usage counts and latency metrics, never customer content | Must-have | - |
| 8 | AI and model usage | Northwind may not train or fine-tune on Halcyon customer inputs or outputs without per-customer opt-in; may evaluate de-identified outputs for accuracy monitoring only. Halcyon may not train, fine-tune, or distill models on Northwind API outputs. Sub-processor: Northwind's named cloud host only. 60 days notice before changing the underlying forecasting model | Must-have | - |
| 9 | SLAs | 99.9% monthly uptime, p95 latency under 800 ms, Sev 1 response within 1 hour. 60 days notice of model changes, 180 days of API deprecations. Service credit mechanics flagged for counsel | Tradeable | Credits capped at 10% of that month's fees |
| 10 | Branding | In-product attribution "Forecasting by Northwind Data". Co-marketing approved in writing within 10 business days. No "powered by" claims beyond approved copy | Tradeable | One joint financial-services case study within 6 months of launch |
| 11 | Term and termination | 2 years from signature, then 1-year auto-renewals unless either party gives 90 days notice. For cause: uncured material breach after 30 days. No for-convenience exit in the initial term. 12-month customer wind-down at the then-current wholesale fee | Tradeable | If Halcyon wants a for-convenience exit: only after month 12, with 180 days notice |
| 12 | Governance | Exec sponsors: Northwind CEO and Halcyon SVP of Analytics Products. Monthly operating review against named pipeline, quarterly exec review. Halcyon gives 12 months notice before launching a forecasting feature that competes with the embedded API. Escalation: partner managers, then sponsors within 10 business days | Tradeable | Named Halcyon partner manager before launch; roadmap notice not below 9 months |

### Walk-away triggers
- Exclusivity: we stop if Halcyon requires exclusivity across all of financial services, or
  any exclusivity not conditional on the 40-customer commit.
- Economics: we stop if our payout is calculated on bookings instead of cash collected, or if
  our effective take falls below $20K per customer.
- AI and model usage: we stop if Halcyon requires the right to train or distill models on
  Northwind outputs or customer data, including through a broad "service outputs" clause.
- Term: we stop if Halcyon requires an initial term over two years, which is outside the
  approved business case.

### Open items
- Discount authority of Halcyon sellers on the analytics suite - Halcyon partner lead - 2026-11-28
- Ramp start date relative to Halcyon's Q2 2027 launch - Northwind deal owner - 2026-11-24
- Support escalation ownership (first line Halcyon, second line Northwind proposed) - both product leads - 2026-12-01
- MSA draft section 7.3 "service outputs" wording conflicts with term 8 - Northwind legal - 2026-11-25
- Written Halcyon training policy, requested twice in diligence - Halcyon partner lead - 2026-11-25
- Schedule A: named list of 50 financial-services accounts - Halcyon partner lead - 2026-12-01
- Indemnities, warranties, liability cap, governing law: not drafted here, flagged for counsel - Northwind counsel - 2026-12-05

### Internal approvals required
- [ ] Finance  - [ ] Security  - [ ] Privacy  - [ ] Product  - [ ] Counsel
```

## What to do next

This is a business-terms draft, not legal advice. Counsel reviews it before anything goes to
Halcyon, and drafts the indemnity, warranty, liability, and governing-law language this sheet
deliberately leaves out. Strip the Mark and "If traded" columns into a clean external version
before sending; the partner never sees them.

The Economics row ties back to the deal structure: the 40-customer commit is worth
40 x $22K = $880K a year, and the 60-customer base case is 60 x ($22K - $6K serving) = $960K.

Use the marks to build the give-get list in [negotiation-prep](../skills/negotiation-prep/SKILL.md), and brief the CEO on the must-haves with [partner-exec-briefing](../skills/partner-exec-briefing/SKILL.md).
