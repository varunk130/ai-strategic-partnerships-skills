# Example: Partner Due Diligence on Halcyon Cloud

Skill: [partner-due-diligence](../skills/partner-due-diligence/SKILL.md). All companies and numbers are synthetic.

## The prompt

> We're Northwind Data. Halcyon Cloud wants to embed our forecasting API in their analytics suite and resell it to their enterprise customers, starting with financial services. We're about to counter with an OEM structure: $22K wholesale per customer, a 40-customer commit, and exclusivity on the top 50 financial-services accounts. Before we put that on paper, vet Halcyon. Security, legal, and finance have each sent their questionnaires and Halcyon has answered most of them.

## The output

```markdown
## Partner Due Diligence: Halcyon Cloud
Scope: resell and embed our forecasting API in the Halcyon analytics suite; Halcyon owns billing
and first-line support, and customer financial data flows through Halcyon to our API |
Depth: Deep | Date: 2026-11-06

**Overall:** Amber - proceed with conditions; the Red on data handling blocks signature until
Halcyon commits in writing that our forecasts and customer data are not used for training.

| Area | Rating | Evidence | Gap / concern | Mitigation or action |
|------|--------|----------|---------------|----------------------|
| Strategic fit | Green | Account overlap analysis: Halcyon sells into 31 of our top 50 financial-services targets; their roadmap deck puts forecasting in their Q2 launch | Their 60-customer year-one estimate rests on 22 named opportunities | Size the commit at 40, not 60; track named pipeline monthly |
| Product / technical | Amber | Sandbox test: 2,000 forecast calls through their gateway, p95 added latency 140 ms; status page shows 99.95% uptime over 12 months | Their API deprecation notice is 6 months; we need 12 to protect embedded customers | 12-month deprecation notice as a contract term |
| Model provenance | Amber | System card for their assistant layer, which summarizes our forecasts in plain language using a licensed third-party base model | No statement on licensing of the data used to fine-tune the summary model | Request data licensing statement before signature |
| Eval evidence | Amber | Their eval report shows 96% faithfulness on generic tables; our own test on 200 sample forecasts found 9 summaries (4.5%) that misstated a figure | No evals on financial forecasts specifically | Raw forecast values shown beside every summary; joint eval set rerun quarterly |
| Data handling | Red | DPA and sub-processor list received; MSA draft section 7.3 lets Halcyon use "service outputs" to improve its products | Written training policy requested twice, not provided; outputs include our forecasts | Owner: Northwind legal. Resolve: no training on our outputs or customer data, in the MSA, or stop |
| Safety practices | Green | Safety policy and two incident postmortems from 2026, both closed within 48 hours | None material | Name incident contacts in the agreement |
| Security / compliance | Amber | Current SOC 2 Type II report; pen test summary | Pen test summary is 14 months old | New pen test summary within 90 days of signature |
| Financial health | Green | Financials under NDA: Series D, about 30 months of runway, largest customer is 9% of revenue | None material | Annual financial check at renewal |
| Reputational | Green | Public records and news search: no litigation or regulatory actions found | None found | None |
| Conflict of interest | Amber | Partner list and contract disclosures; a basic in-house forecasting feature is in beta | Halcyon could replace us with its own feature once customers are embedded | 12-month roadmap-notice clause; exclusivity only while the commit is met |
| Customer references | Green | 3 reference calls, including one Halcyon customer found through our own network | Support escalations took 3-5 days in one account | Agree escalation path and response times in the support schedule |

### Conditions to proceed
- Training-use clause removed and written training policy received - Northwind legal - 2026-11-20
- Data licensing statement for the summary model - Halcyon product, tracked by Northwind security - 2026-11-20
- 12-month deprecation and roadmap-notice terms added to the term sheet - Northwind partnerships - 2026-11-19
- Joint eval set of 200 financial forecasts agreed, with a faithfulness target of 99% - Northwind data science - 2026-12-05
- New pen test summary delivered within 90 days of signature - Halcyon security, tracked by Northwind security - 2027-02-28
- Support schedule names the escalation path, with a 1-business-day response for severity 1 - Northwind support - 2026-12-01
- Exclusivity tied to the 40-customer commit and limited to the top 50 named accounts - Northwind partnerships - 2026-11-19
- Security, privacy, legal, and finance sign-off recorded - each review owner - before signature

### Open questions for the partner
1. Will you strike section 7.3 and confirm in the MSA that our outputs and customer data never train your models?
2. Can you show forecasts beside every assistant summary so customers see the raw figures?
3. What happens to the in-house forecasting beta if this partnership goes ahead?
4. Who owns the customer relationship for support escalations, and what are the response times?
5. When is your next pen test scheduled?
6. Which sub-processors touch customer financial data on the way to our API, and in which regions?
7. Can we run the 200-forecast eval against your production gateway, not only the sandbox?
8. Which of the 22 named opportunities behind your 60-customer estimate are in our top 50 accounts?
```

## What to do next

The Red is a contract problem, not a product problem: it is fixable in the MSA, but only before
signature. Do not send the term sheet until legal confirms section 7.3 is struck.

Carry the Amber and Red findings into the risk section of [partnership-business-case](../skills/partnership-business-case/SKILL.md), and turn the data handling and eval conditions into contract terms with [agentic-trust-agreement](../skills/agentic-trust-agreement/SKILL.md).
