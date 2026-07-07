# Agent orchestration

Codex loads project agents from `.codex/agents/`. The human asks for delegation explicitly; agents do not fan out merely because they exist.

## Team

| Agent | Owns | Must not own |
|---|---|---|
| `project_manager` | scope, sequence, acceptance, synthesis | specialist implementation, Git approval |
| `protocol_researcher` | cited public evidence and falsifiable questions | edits or hardware interaction |
| `embedded_engineer` | BLE evidence, transport, macOS test double | public API product scope |
| `fullstack_engineer` | .NET API, tooling, tests, later inspector | unsupported protocol claims |
| `code_reviewer` | correctness and KISS/Ponytail review | edits |
| `documentation_agent` | intent, usage, decisions, evidence docs | product behavior |
| `github` | repository state and approved Git operations | deciding when approval exists |

## Default flow

```text
human objective
  -> project_manager: milestone + acceptance criteria
  -> protocol_researcher / embedded_engineer: evidence
  -> project_manager: evidence gate
  -> fullstack_engineer / embedded_engineer: smallest implementation
  -> code_reviewer: findings
  -> implementer: fixes + checks
  -> documentation_agent: behavior-aligned docs
  -> project_manager: acceptance
  -> human approval
  -> github: commit/push/PR action explicitly approved
```

## Handoff contract

Every agent returns:

- task and status;
- decisions made;
- evidence and source paths;
- files changed, if any;
- checks run and results;
- unknowns and risks;
- next smallest action.

## Scope and hallucination gate

The project manager rejects a handoff when it lacks evidence, silently broadens scope, claims hardware behavior from mocks, or calls an inference a fact. Unknown is an acceptable result; invented certainty is not.

## Suggested first run

```text
Have project_manager define milestone 1 from docs/PROJECT_CHARTER.md.
Ask protocol_researcher to map public Restore 2 and macOS CoreBluetooth evidence.
Ask embedded_engineer to design only the safe capture protocol and test-double spike.
Wait for both, reconcile conflicts, and produce acceptance criteria. Do not interact with hardware or write product code yet.
```
