# Agent orchestration

Codex loads project agents from `.codex/agents/`. The human asks for delegation explicitly; agents do not fan out merely because they exist.

## Team

| Agent | Owns | Must not own |
|---|---|---|
| `project_manager` | scope, sequence, acceptance, synthesis, local Git checkpoint authorization | specialist implementation, PR merge approval |
| `protocol_researcher` | cited public evidence and falsifiable questions | edits or hardware interaction |
| `embedded_engineer` | BLE evidence, transport, macOS test double | public API product scope |
| `fullstack_engineer` | .NET API, tooling, tests, later inspector | unsupported protocol claims |
| `code_reviewer` | correctness and KISS/Ponytail review | edits |
| `documentation_agent` | intent, usage, decisions, evidence docs | product behavior |
| `github` | shared branches, focused commits, pushes, PR creation, repository state | PR merges, releases, force/history operations |

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
  -> github: focused commit, push, and PR creation
  -> human approval before PR merge
```

## Shared branch coordination

1. `project_manager` defines the milestone, acceptance criteria, and branch slug.
2. `github` confirms no write-capable agent is active, then creates or switches to `codex/<milestone>`.
3. `github` records the base branch, base commit, active branch, and head commit in the handoff.
4. `project_manager` includes that branch context when assigning work to every affected agent.
5. No agent switches branches directly. Branch changes are serialized through `github` because all agents share one checkout.
6. After acceptance criteria and checks pass, `github` creates focused commits, pushes the branch, and opens a pull request.
7. The human explicitly approves any PR merge, release, package publication, force-push, history rewrite, remote change, or destructive branch deletion.

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
