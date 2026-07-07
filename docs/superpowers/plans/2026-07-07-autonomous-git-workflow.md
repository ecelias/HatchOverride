# Autonomous Git Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan inline. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let `project_manager` and `github` autonomously coordinate local branches, focused commits, pushes, and PR creation while reserving PR merge and high-risk Git operations for explicit human approval.

**Architecture:** One shared milestone branch is active in the shared checkout. `project_manager` defines scope and acceptance; `github` serializes branch changes, records base/head, communicates branch context, commits accepted work, pushes, and opens PRs. Existing approval language is updated consistently across repository governance.

**Tech Stack:** Markdown governance and TOML project-agent configuration.

## Global Constraints

- Branch names use `codex/<milestone>`.
- Only one branch switch occurs at a time; no switch while another write agent is active.
- Unrelated working-tree changes are never staged.
- PR merge, release, force-push, history rewrite, remote change, and destructive branch deletion require explicit human approval.
- Hardware, BLE, evidence, privacy, and safety gates remain unchanged.

### Task 1: Define agent authority and coordination

**Files:**
- Modify: `.codex/agents/project-manager.toml`
- Modify: `.codex/agents/github.toml`
- Modify: `docs/ORCHESTRATION.md`

- [ ] Give `project_manager` authority to request milestone branches and accepted-task commits.
- [ ] Give `github` authority to create/switch branches, create focused commits, push, and open PRs without per-action approval.
- [ ] Require base/head recording and branch-context communication to affected agents.
- [ ] Serialize branch switching across the shared checkout.

### Task 2: Align repository-wide approval language

**Files:**
- Modify: `AGENTS.md`
- Modify: `README.md`
- Modify: `docs/PROJECT_CHARTER.md`
- Modify: `docs/PRD_FOCUSED_V1.md`
- Modify: `END_GOAL.md`
- Modify: `.agents/skills/restore2-orchestration/SKILL.md`
- Modify: `.agents/skills/delivery-gate/SKILL.md`
- Modify: `.agents/skills/project-management/SKILL.md`

- [ ] Replace obsolete per-action approval requirements for branch, commit, push, and PR creation.
- [ ] Preserve explicit approval for PR merge and high-risk/public release actions.
- [ ] Preserve hardware and BLE approval boundaries verbatim.

### Task 3: Verify and publish

- [ ] Search active governance for contradictory Git approval statements.
- [ ] Validate TOML parsing and Markdown links.
- [ ] Review the diff for unrelated changes.
- [ ] Create one focused commit, push the branch, and open a PR for human merge approval.
