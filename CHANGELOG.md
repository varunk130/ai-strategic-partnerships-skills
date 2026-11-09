# Changelog

Notable changes to this project, newest first.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- Worked examples for the remaining nine skills, so every skill now has one. The Northwind Data and Halcyon Cloud examples follow one deal from due diligence through business case, negotiation, term sheet, and exec briefing.

### Fixed
- The deal-structure example's fallback revenue share: 55/45 with a $20K floor always hit the floor at list price. It is now 50/50 with a $16K floor, which only binds when the partner discounts more than 20%.

## 2026-11-08 - v1.0: Initial release

### Added
- Twelve skills across strategy, distribution, diligence, deal design, negotiation, trust, and renewal: partnership-thesis, ecosystem-landscape-map, agent-ecosystem-distribution, cloud-marketplace-gtm, partner-due-diligence, deal-structure-designer, partnership-business-case, negotiation-prep, term-sheet-builder, partner-exec-briefing, agentic-trust-agreement, partnership-renewal-review.
- `install.sh` for user-level, project-level, or selective installs.
- `scripts/validate_skills.py` and a GitHub Actions workflow that runs it with an installer smoke test.
- Three worked examples using synthetic companies.
- Documentation: how to use, partnership lifecycle guide, and the skill template.
