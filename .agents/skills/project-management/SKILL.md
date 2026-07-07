---
name: project-management
description: Use when the Hatch Restore 2 project manager is defining milestones, acceptance criteria, delivery risks, status, sprint work, Jira or Confluence work, meeting analysis, or stakeholder communication.
---

# Project management

Coordinate delivery without replacing repository governance.

## Core workflow

1. Read `AGENTS.md`, `docs/PROJECT_CHARTER.md`, `docs/PRD_FOCUSED_V1.md`, and `docs/ORCHESTRATION.md`.
2. Use `restore2-orchestration` for milestone ownership, evidence gates, handoffs, and acceptance.
3. State one observable outcome, one accountable owner per artifact, the proof command or review criterion, and explicit non-goals.
4. Load at most one specialty below when the task needs expertise beyond the core workflow.
5. Return decisions, evidence paths, changed artifacts, checks, risks, and the next smallest action.

## Specialty routing

| Task signal | Read |
|---|---|
| Portfolio health, roadmap, capacity, risk | `skills/senior-pm/SKILL.md` |
| Sprint health, velocity, retrospectives | `skills/scrum-master/SKILL.md` |
| Jira or JQL | `skills/jira-expert/SKILL.md` |
| Confluence structure or content | `skills/confluence-expert/SKILL.md` |
| Atlassian permissions or administration | `skills/atlassian-admin/SKILL.md` |
| Jira or Confluence templates | `skills/atlassian-templates/SKILL.md` |
| Meeting transcript analysis | `skills/meeting-analyzer/SKILL.md` |
| Status updates or stakeholder communications | `skills/team-communications/SKILL.md` |
| PM analytics scripts or imported delivery-loop reference | `skills/pm-skills/SKILL.md` |

Resolve specialty paths relative to this file. Run a bundled Python tool from its own skill directory so relative assets resolve correctly.

## Integration rules

- Use Linear or GitHub only when their installed tools are available and relevant to the assigned task.
- Use Jira or Confluence only through an available, authorized connector. Treat imported MCP names as reference examples, not proof that a tool is installed.
- Do not invoke removed command systems, agent definitions, bootstrap configuration, or absent sibling bundles.
- Do not bulk-load specialties. If a request spans specialties, finish one bounded artifact before loading the next.
- Use the shared-branch workflow in `docs/ORCHESTRATION.md`: `project_manager` may authorize milestone branches and accepted-task commits; `github` may push and open pull requests. Preserve explicit human approval for PR merge, release, package publication, high-risk Git operations, hardware interaction, pairing, and BLE writes.
- Unknown protocol behavior is an acceptable result; never convert schedule pressure into unsupported device claims.
