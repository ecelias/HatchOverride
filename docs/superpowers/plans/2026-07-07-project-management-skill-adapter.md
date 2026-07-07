# Project-Management Skill Adapter Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the imported project-management bundle discoverable and usable by the existing Hatch Restore 2 `project_manager` agent.

**Architecture:** Add one thin Codex skill adapter that routes repository planning through existing Hatch governance and progressively loads at most one nested PM specialty. Remove duplicate Claude-facing entry points while retaining specialty skills, references, assets, and working stdlib Python tools.

**Tech Stack:** Markdown Codex skills, TOML agent configuration, Python 3 standard library.

## Global Constraints

- Preserve the nine nested PM skills and 15 Python tools.
- Do not activate Atlassian access unless a compatible connector is available and the task needs it.
- Do not weaken Git, hardware, BLE, evidence, or publication approval boundaries.
- Do not commit or push without explicit human approval.

---

### Task 1: Add the Codex adapter

**Files:**
- Create: `.agents/skills/project-management/SKILL.md`
- Modify: `.codex/agents/project-manager.toml`

**Interfaces:**
- Consumes: `AGENTS.md`, `docs/PROJECT_CHARTER.md`, `docs/ORCHESTRATION.md`, `.agents/skills/restore2-orchestration/SKILL.md`, and nested `project-management/skills/*/SKILL.md` files.
- Produces: one discoverable `project-management` skill and an explicit activation rule for `project_manager`.

- [ ] **Step 1: Verify the adapter is absent**

Run: `test ! -f .agents/skills/project-management/SKILL.md`

Expected: exit 0.

- [ ] **Step 2: Create the minimal adapter**

Add valid `name` and `description` frontmatter; require repository governance first; route ordinary delivery planning through `restore2-orchestration`; load at most one nested specialty based on an explicit task signal; reject unavailable integrations and unsupported sibling-repository references.

- [ ] **Step 3: Connect the existing agent**

Add to `project-manager.toml` instructions that project planning and delivery-management tasks require `.agents/skills/project-management/SKILL.md`, while protocol milestones still require `restore2-orchestration`.

- [ ] **Step 4: Validate adapter structure and references**

Run a local validator that checks frontmatter fields, adapter length, and every referenced relative path.

Expected: exit 0 with all references present.

### Task 2: Remove obsolete Claude surfaces

**Files:**
- Delete: `.agents/skills/project-management/agents/`
- Delete: `.agents/skills/project-management/commands/`
- Delete: `.agents/skills/project-management/.mcp.json`
- Delete: `.agents/skills/project-management/.codex/instructions.md`
- Delete: `.agents/skills/project-management/AGENTS_PM.md`
- Delete: `.agents/skills/project-management/README.md`
- Delete: `.agents/skills/project-management/IMPLEMENTATION_SUMMARY.md`
- Delete: `.agents/skills/project-management/INSTALLATION_GUIDE.txt`
- Delete: `.agents/skills/project-management/REAL_WORLD_SCENARIO.md`
- Delete: `.agents/skills/project-management/.DS_Store`
- Delete: `.agents/skills/project-management/skills/.DS_Store`
- Delete: `.agents/skills/project-management/skills/team-communications/.DS_Store`

**Interfaces:**
- Consumes: the approved removal list.
- Produces: a skill bundle with one Codex entry point and no duplicate Claude command/agent/bootstrap surface.

- [ ] **Step 1: Record the obsolete-file baseline**

Run: `find .agents/skills/project-management/agents .agents/skills/project-management/commands -type f`

Expected: imported Claude agent and command files are listed.

- [ ] **Step 2: Delete only the approved obsolete paths**

Use the exact file list above; preserve `skills/`, `references/`, scripts, assets, and specialty `SKILL.md` files.

- [ ] **Step 3: Verify removals and retained inventory**

Run checks asserting each obsolete path is absent, nine nested `SKILL.md` files remain, and 15 Python files remain.

Expected: exit 0; counts are 9 and 15.

### Task 3: Validate retained functionality

**Files:**
- Test: `.agents/skills/project-management/SKILL.md`
- Test: `.agents/skills/project-management/skills/**/*.py`

**Interfaces:**
- Consumes: the adapter and retained tools.
- Produces: verification evidence for discoverability, tool syntax, and CLI availability.

- [ ] **Step 1: Compile retained Python without writing bytecode**

Run `compile()` against every retained `.py` source.

Expected: all 15 compile successfully.

- [ ] **Step 2: Exercise every CLI help path**

Run `python3 <script> --help` for every retained Python tool.

Expected: all 15 exit 0.

- [ ] **Step 3: Check for reachable foreign runtime assumptions**

Search the new adapter and `project-manager.toml` for Claude commands, missing `engineering/agent-harness`, missing sibling repositories, or direct `.mcp.json` activation.

Expected: no matches.

- [ ] **Step 4: Review the final diff**

Confirm changes match the approved spec, preserve unrelated untracked files, and leave Git history and remotes unchanged.

Expected: only the adapter, project-manager instruction, approved deletions, design, and plan appear in scope.
