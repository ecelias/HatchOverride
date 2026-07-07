---
name: restore2-orchestration
description: Coordinate milestones and evidence-gated handoffs for the Hatch Restore 2 API project.
---

# Restore 2 orchestration

1. Read `AGENTS.md`, `docs/PROJECT_CHARTER.md`, and the current research/decision records.
2. State one milestone, one owner per artifact, acceptance criteria, and explicit non-goals.
3. Delegate only independent tasks. Protocol research precedes protocol implementation.
4. Require each handoff to contain: decisions, evidence, changed artifacts, checks, open risks, and next action.
5. Send implementation through `code_reviewer`; send behavior changes through `documentation_agent`.
6. After acceptance, `github` may create focused commits, push the milestone branch, and open a pull request. Stop for human approval before PR merge, release, package publication, high-risk Git operations, or real-device BLE interaction.
