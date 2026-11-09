# Example: Exec Briefing for the Halcyon Cloud OEM Deal

Skill: [partner-exec-briefing](../skills/partner-exec-briefing/SKILL.md). All companies and numbers are synthetic.

## The prompt

> Our CEO, Rhea Calloway, meets Elliot Marsh, Halcyon Cloud's SVP of Analytics Products, on November 24 for 45 minutes, after the deal teams meet on the 19th. It's their first exec meeting. Halcyon proposed a 70/30 revenue share with three-year exclusivity in financial services; we countered with a $22K per-customer OEM fee, a 12-month ramp to a 40-customer commit, and exclusivity limited to the top 50 financial-services accounts while they hit the commit. Rhea needs to get the commit agreed in principle. Prep her.

## The output

```markdown
# Exec Brief: Rhea Calloway x Elliot Marsh, Halcyon Cloud
2026-11-24 | 45 min | Attendees: Rhea Calloway (CEO, Northwind Data), Sam Whitfield (Head of
Partnerships, Northwind Data), Elliot Marsh (SVP Analytics Products, Halcyon Cloud),
Dana Okafor (VP Ecosystem, Halcyon Cloud)

**Relationship state:** New: no joint customers yet, and proposals have only been exchanged
at deal-team level.
**Meeting goal:** Elliot agrees in principle to the 40-customer minimum commit in exchange for
exclusivity on the top 50 financial-services accounts.

## Their strategy and pressures
- AI roadmap: their forecasting module launches in Q2 2027 and needs a proven engine; their
  in-house forecasting is a basic beta (from diligence). Embedding ours closes the gap now.
- Financial-services growth: their recent launch messaging leads with financial services; a
  named-account exclusivity helps them, a segment lockout from us does not.
- Margin: at $22K wholesale against a $40K reference price, Halcyon keeps $18K per customer
  (45%). Lower than their 70/30 ask, so expect pushback here.

## Wants
| | Us | Them |
|-|----|------|
| From this meeting | Commit agreed in principle; Elliot as sponsor | Broad exclusivity; no commit before launch |
| This quarter | Signed term sheet; named 50-account list | Integration started before their Q2 2027 launch |
| Where we conflict | Exclusivity tied to commit; pay on cash collected | Segment-wide exclusivity; pay on bookings |

## Talking points
1. The commit sits below their own forecast: Halcyon estimated 60 customers in year one, and
   40 is two-thirds of that -> ask him to back his team's number with the commit.
2. Both sides scale together: at 60 customers Halcyon keeps $1.08M a year at $18K each, and
   there is no cap on their upside -> the commit is what earns exclusivity.
3. No risk before they sell: the 12-month ramp starts at their commercial launch, so the
   commit is first measured a year after launch -> nothing is owed before customers exist.

## Landmines
- Their 70/30 proposal: if raised, say a share with no floor lets discounting erode both
  sides, and that under OEM they set resale price and keep the margin. Do not reopen numbers.
- Exclusivity across all financial services: if raised, do not concede; offer to expand the
  named list once they exceed the commit for two consecutive quarters.
- Bookings vs cash collected: if raised, acknowledge and hand to the deal teams.
- Their in-house forecasting beta: if raised, welcome it as a fit for smaller accounts and
  ask for the 12-month roadmap-notice clause. Do not frame it as a threat.
- Other platform talks: if asked, say we do not discuss other partners. Give no names.

## The ask
Agree in principle to a 40-customer minimum commit after a 12-month ramp from launch, and send
the named 50-account list by 2026-12-01, owned by Elliot Marsh.

## Follow-up
Owner: Sam Whitfield | Recap sent by: 2026-11-26
```

Post-meeting capture, filled in on 2026-11-24:

```markdown
## Exec Meeting Capture: Halcyon Cloud, 2026-11-24
- Ask outcome: yes, in principle - Elliot accepts the 40-customer commit if the 12-month ramp
  starts at their commercial launch (2027-04-15), not at signature. Commit first measured
  2028-04-15.
- Commitments made by us: recap email - Sam Whitfield - 2026-11-26; term sheet draft 2 with ramp
  tied to launch - Sam Whitfield - 2026-12-01
- Commitments made by them: named 50-account list - Dana Okafor - 2026-12-01; answer on seller
  discount authority - Dana Okafor - 2026-11-28
- New information: analytics products moved under Elliot in October (stated by Elliot). He
  called the in-house beta "a lightweight option" but would not commit to roadmap notice.
- Relationship state now: New, with sponsorship confirmed - changed because Elliot named Dana
  as owner and accepted the commit in principle.
- Next exec touchpoint: 2027-01-14, after term sheet signature
```

## What to do next

Send the recap by 2026-11-26, then update [term-sheet-builder](../skills/term-sheet-builder/SKILL.md) draft 2 with the launch-based ramp. If Halcyon reopens exclusivity breadth, prepare the trade with [negotiation-prep](../skills/negotiation-prep/SKILL.md).
