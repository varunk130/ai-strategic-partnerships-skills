# Example: Negotiation Prep for Northwind Data and Halcyon Cloud

Skill: [negotiation-prep](../skills/negotiation-prep/SKILL.md). All companies and numbers are synthetic.

## The prompt

> We're Northwind Data. Halcyon Cloud proposed a 70/30 revenue share in their favor plus three-year exclusivity across financial services for embedding and reselling our forecasting API. Our CRO approved countering with an OEM structure: $22K wholesale per customer (list is $40K, serving cost $6K), a 40-customer commit, and exclusivity only on the top 50 FS accounts. Fallback is 55/45 with a $20K floor. Next session is 2026-11-19 with their VP Ecosystem and, we think, their SVP of Analytics. Build the plan.

## The output

```markdown
## Negotiation Plan: Northwind Data x Halcyon Cloud
Meeting: 2026-11-19 | Our lead: Sam Whitfield, Head of Partnerships | Approver for concessions: Morgan Reyes, CRO

**Our goal:** sign an OEM deal at $22K wholesale with a 40-customer commit, exclusivity limited
to the top 50 named FS accounts while the commit is met, and no training on our outputs.
**Our BATNA:** revenue-share talks with Bramblefield Analytics (smaller FS footprint) plus our
direct team, which closed 9 FS accounts this year. Strength 2 of 5. | **Their BATNA (est.):**
finish their in-house forecasting beta (not production-ready before their Q2 launch) or license
a second-tier engine. Strength 3 of 5.
**ZOPA:** overlap on the per-customer fee ($20K-$24K) and on the commit if the ramp starts after
their Q2 launch. No overlap on exclusivity: they want all of FS for 3 years, our limit is named
accounts for 2. The new variable is a right of first refusal on the next 25 FS accounts.

Economics at 60 customers: their proposal gives us $360K and them $1.68M. Our target gives us
$960K and them $1.08M. The pie is the same $2.04M ($2.4M revenue less $360K serving), so the $600K
we gain is $600K they lose: the gives below have to carry real value to them.

### Interests
| Side | Position | Interest |
|------|----------|----------|
| Us | $22K wholesale, 40 commit | Cover serving cost with margin; protect the low case if Halcyon underperforms |
| Us | Named-account exclusivity only | Keep selling direct to the rest of FS |
| Them | 70/30 share | Healthy margin on a module their sellers will discount |
| Them | 3-year FS exclusivity | Stop competitors buying the same engine during their launch window |

### Give-get list
| Item | Cost to us | Value to them | Give/Get | Trade for |
|------|------------|---------------|----------|-----------|
| Exclusivity on top 50 named FS accounts while commit is met | 3 | 5 | Give | 40-customer commit |
| Right of first refusal on the next 25 FS accounts | 2 | 4 | Give | Exclusivity capped at 2 years |
| Ramp to the commit starts after their Q2 launch | 2 | 4 | Give | $22K wholesale |
| 2-year wholesale price lock | 2 | 4 | Give | Payout on cash collected, monthly |
| $60K launch MDF (already approved) | 2 | 3 | Give | Co-branded launch and logo rights |
| No training on our outputs or customer data | 1 | 2 | Get | Non-negotiable; trade only the wording |
| 12-month roadmap and API deprecation notice | 1 | 2 | Get | Named incident contacts from us |
| Monthly named-account pipeline report | 1 | 1 | Get | Joint quarterly pipeline review |

### Anchor and concessions
1. Anchor: $25K wholesale, 55-customer commit, exclusivity on the top 30 named accounts, because
   Halcyon keeps $15K per customer (37.5% of list), in line with the 35-40% our existing resellers earn.
2. Concession 2: $23K wholesale, 45-customer commit, top 40 accounts, in exchange for payout on
   cash collected monthly and the 2-year price lock.
3. Final: $22K wholesale, 40-customer commit with the ramp after their Q2 launch, top 50 accounts
   for 2 years plus first refusal on the next 25, in exchange for the no-training clause and
   12-month roadmap notice.
Concession sizes decrease: fee $2K then $1K; commit 10 then 5 customers.

### Their stakeholders
| Role | Person | Cares about | Stance | Our move |
|------|--------|-------------|--------|----------|
| Champion | Dana Okafor, VP Ecosystem | Hitting the Q2 forecasting launch | Supportive | Give her the margin math at $22K: $18K per customer to Halcyon |
| Economic buyer | Elliot Marsh, SVP Analytics | Module margin and attach rate | Neutral | Meet before the final round; lead with the ramp timing |
| Legal | Halcyon commercial counsel | MSA consistency, section 7.3 | Neutral | Pre-share the no-training clause wording |
| Security / privacy | Halcyon CISO office | Data flow through their gateway | Supportive | Send our diligence pack and SOC 2 report early |
| Blocker | Product lead, in-house forecasting beta | Own roadmap survives | Opposed | Frame us as the engine for FS; their beta keeps other segments |

### Walk-away triggers
- Wholesale fee below $20K per customer -> we pause and escalate to Morgan Reyes
- Any exclusivity without a minimum commit, beyond named accounts, or longer than 2 years -> we pause and escalate to Morgan Reyes
- Commit below 30 customers -> we pause and escalate to Morgan Reyes
- Refusal to strike training use of our outputs or customer data -> we pause and escalate to Morgan Reyes and legal
- Payout on bookings rather than cash collected -> we pause and escalate to Morgan Reyes
```

## What to do next

Brief Morgan Reyes before the economic-buyer meeting with [partner-exec-briefing](../skills/partner-exec-briefing/SKILL.md), then capture whatever is agreed in [term-sheet-builder](../skills/term-sheet-builder/SKILL.md).
