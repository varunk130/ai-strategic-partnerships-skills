# Example: Agentic Trust Agreement for a Procurement Agent

Skill: [agentic-trust-agreement](../skills/agentic-trust-agreement/SKILL.md). All companies and numbers are synthetic.

## The prompt

> Ardent Procurement runs a purchasing agent for its enterprise customers. Northwind Supply wants Ardent's agent to place and track orders directly in the Northwind supplier portal instead of emailing PDFs. The agent would read the catalog and prices, create purchase orders, and check order status. Draft the trust terms we need before turning this on.

## The output

```markdown
# Agentic Trust Agreement: Ardent Procurement x Northwind Supply
Agents in scope: Ardent purchasing agent v3 | Systems: Northwind supplier portal (catalog,
orders, order status APIs) | Status: draft for security and legal review

## Permitted actions
| Action | Allowed | Limit | Human approval |
|--------|---------|-------|----------------|
| Read catalog and contract prices | Yes | Customer's contracted items only | No |
| Create purchase order | Yes | Up to $25K per order, $100K per day per customer | Above limit: customer buyer approves |
| Cancel purchase order | Yes | Within 2 hours of creation, before fulfilment | No |
| Change shipping address | No | - | - |
| Modify prices or terms | No | - | - |
| Anything not listed | No | Denied by default | - |

## Responsibilities matrix
| Area | Us (Ardent) | Partner (Northwind) | Joint | Accountable |
|------|-------------|---------------------|-------|-------------|
| Permitted action list | Propose | Enforce in API scopes | Approve | Joint |
| Agent identity and credentials | Request per-customer credentials | Issue and scope them | | Northwind |
| Credential revocation | Revoke on customer offboarding | Revoke on misuse within 15 min | Test quarterly | Joint |
| Data flows and retention | Keep order data 7 years for customer audit | Keep agent logs 1 year | | Each for own systems |
| Training-use restrictions | No Northwind pricing used to train models | No customer order data used to train models | | Each |
| Human approval enforcement | Route over-limit orders to the customer buyer | Reject over-limit orders without an approval token | | Northwind (hard stop) |
| Audit log storage and access | Log every agent decision with reason | Log every API call | Shared read access | Joint |
| Incident detection | Monitor agent behavior and error rates | Monitor API anomalies | | Joint |
| Agent pause / kill switch | Pause per customer | Block agent credentials | | Either side, without notice |
| Customer notification | Notify affected customers within 24 hours | Provide incident details within 12 hours | | Ardent |
| Model/version change notice | 30 days notice of agent model changes | 30 days notice of API changes | | Each |
| Evaluation evidence | Share order-accuracy evals quarterly | Share API reliability metrics | Review together | Joint |

## Readiness checklist
- [x] Every agent action listed; unlisted actions denied
- [x] Each agent has its own identity and scoped credentials
- [ ] Revocation tested end to end
- [x] Data retention and training use agreed in writing
- [ ] Approval thresholds enforced in code, not policy alone
- [ ] Shared audit log live and inspectable by both sides
- [x] Incident runbook with named contacts and notice windows
- [x] Model change notice period agreed: 30 days
- [ ] Baseline evaluation evidence exchanged
- [ ] Security and legal sign-off recorded

## Open issues
| Issue | Owner | Due |
|-------|-------|-----|
| Northwind API cannot yet reject over-limit orders without an approval token | Northwind platform team | 2026-12-15 |
| Shared audit log format not agreed | Both security leads | 2026-12-01 |
| Revocation drill not yet run | Ardent security | 2026-12-08 |
```

## What to do next

Do not switch the agent on until the open issues close and both security and legal sign-offs are recorded. The approval-token check is the gate: until Northwind enforces it, the spending limit exists only in policy.
