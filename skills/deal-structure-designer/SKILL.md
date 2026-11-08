---
name: deal-structure-designer
description: 'Compares candidate commercial structures for a partnership on two-sided economics, risk, effort, and lock-in, then recommends one with a low/base/high volume model and red flags. Use when: deal structure, commercial model, referral vs resell, revenue share, OEM or embed deal, usage-based pass-through, minimum commit, MDF, joint development, how should we structure this partnership.'
---

# Deal Structure Designer

Pick the commercial structure that both sides can still live with at low volume, not just the one that looks best at high volume.

## When to Use

- A partnership thesis is agreed and the next question is "how do we make money together"
- The partner has proposed a structure and you need to test it before responding
- An existing deal is under-performing and the structure may be the cause
- An agent or model provider wants to embed or resell your product inside theirs

## What You'll Need

**Critical inputs (ask if not provided):**

- What each side brings: product, distribution, data, model capacity, services
- Your list price and gross margin, and the partner's if known
- A volume estimate (customers, seats, or usage units) for year one, even a rough range

**Nice-to-have:**

- The partner's opening proposal, if any
- Your existing partner program terms, so the deal does not break precedent silently
- Inference or hosting cost per unit, for usage-based or embedded AI products

## Process

### Step 1: Shortlist structures

Start from the full menu and eliminate what does not fit the value exchange. Keep two or three.

| Structure | How money flows | Best when | Typical lock-in |
|-----------|-----------------|-----------|-----------------|
| Referral fee | You pay partner a % of first-year deal | Partner sources, you sell and support | Low |
| Resell / margin | Partner buys at discount, sells at list | Partner owns the customer and billing | Medium |
| Revenue share | Ongoing % of recurring revenue to partner | Joint value persists past the first sale | Medium |
| OEM / embed | Partner pays per unit to ship your product inside theirs | Your capability is a feature of their product | High |
| Usage-based pass-through | Partner meters usage, passes cost plus margin | Agent or API consumption varies widely | Medium |
| Minimum commit | Partner pre-commits spend or volume for better rates | Partner wants pricing or exclusivity | High |
| MDF / co-marketing funds | One side funds joint demand gen | Launching a new joint motion | Low |
| Joint development | Shared cost to build a new capability | Neither side can build it alone | High |

### Step 2: Score each shortlisted structure

Score 1 (bad for us) to 5 (good for us). Score the partner's view separately; a deal one side scores 1 will not survive.

| Dimension | Question |
|-----------|----------|
| Our economics | Net margin after partner payout and support cost |
| Their economics | Is it worth their sellers' time versus their alternatives |
| Risk | Who carries the downside if volume misses |
| Effort | Billing, contracting, enablement, and integration work to stand it up |
| Lock-in | How hard it is for either side to exit or renegotiate |
| Incentive alignment | Does each side get paid for the behavior the partnership needs |

### Step 3: Model both sides at three volumes

Use the same unit for both sides. Show annual figures.

| Volume case | Units | Our revenue | Our cost (COGS + payout + support) | Our net | Partner revenue | Partner cost | Partner net |
|-------------|-------|-------------|-------------------------------------|---------|-----------------|--------------|-------------|
| Low (50% of plan) | | | | | | | |
| Base (plan) | | | | | | | |
| High (200% of plan) | | | | | | | |

Read the table for asymmetry: if one side is net negative at Low, the structure needs a floor (minimum commit), a ramp, or a different model. For usage-based AI products, check that inference cost per unit does not exceed the pass-through price at High.

### Step 4: Check red flags

| Red flag | Why it hurts | Fix |
|----------|--------------|-----|
| Exclusivity without minimums | You give up the market and get no guaranteed volume | Tie exclusivity to an annual commit; lapse it if missed |
| Uncapped liability or indemnity | One incident can exceed lifetime deal value | Cap at 12 months of fees; carve out only what counsel requires |
| Misaligned incentives | Partner is paid on first sale, you need retention | Shift payout to recurring rev share or add a renewal kicker |
| Most-favored-nation pricing | Every future deal resets this one | Limit scope to same product, same volume tier, same term |
| Payout on bookings not collections | You pay for revenue you never receive | Pay on cash collected |
| Usage pass-through with no price floor | Model cost changes erase your margin | Add a cost-indexed price review clause |
| Joint IP with no ownership rule | Neither side can ship the result alone | Decide ownership and license-back before build starts |

### Step 5: Recommend

Pick one primary structure, name one fallback, and state what would make you switch.

## Output Format

```markdown
## Deal Structure: [Our company] x [Partner, e.g. Halcyon Cloud]

**Recommendation:** [structure], with [modifier, e.g. 12-month ramp to minimum commit]
**Fallback:** [structure], if [condition]

### Structures compared
| Structure | Our econ | Their econ | Risk | Effort | Lock-in | Alignment | Verdict |
|-----------|----------|------------|------|--------|---------|-----------|---------|

### Two-sided economics (annual, [unit])
| Case | Units | Our net | Partner net | Notes |
|------|-------|---------|-------------|-------|
| Low | | | | |
| Base | | | | |
| High | | | | |

### Red flags found
- [flag]: [where it appears] - [proposed fix]

### Open questions for the partner
- [question]
```

## Guardrails

- Do not present the model as a forecast. It is a sensitivity check on assumptions you must state.
- Never show the partner your internal margin table; share only their side of the model.
- Pricing, discount, and exclusivity decisions need sign-off from finance and the deal desk, not this skill.
- Synthetic examples only. Do not paste real partner pricing into shared repos.

## Related

- [partnership-thesis](../partnership-thesis/SKILL.md): the value exchange this structure has to monetize
- [partnership-business-case](../partnership-business-case/SKILL.md): turns the base case into an investment ask
- [term-sheet-builder](../term-sheet-builder/SKILL.md): writes the chosen structure into terms
- [negotiation-prep](../negotiation-prep/SKILL.md): plans how to get the partner to agree
- [cloud-marketplace-gtm](../cloud-marketplace-gtm/SKILL.md): when the deal transacts through a marketplace
- [ai-ecosystem-partnerships](https://github.com/varunk130/ai-ecosystem-partnerships): joint business plans once the deal is signed
