# Agent plugin requirements

## Decision

Record role-specific plugin requirements in agent instructions and orchestration documentation. Do not add an unverified `plugins` key to agent TOML files. Runtime availability remains authoritative.

## Role mapping

| Work | Required plugins |
|---|---|
| Planning | Linear, Superpowers, GitHub |
| Coding | Ponytail, Build macOS Apps, Build Web Apps, Superpowers, GitHub, Codex Security |
| Documentation | Superpowers, Linear, GitHub |

The mapping applies by work performed, not only by agent name. An agent crossing roles must use the union needed for that task.

## Runtime behavior

Before delegation, the project manager checks whether required capabilities are available:

- Use an available plugin only when relevant to the assigned task.
- If a missing plugin is optional for the task, record the fallback in the handoff.
- If the missing plugin supplies an acceptance gate, stop that task and report the dependency.
- Never claim a plugin ran when it was unavailable.

GitHub access does not change repository authority: only the `github` agent performs approved Git mutations or publication. Other agents may inspect GitHub context when needed.

## Scope

This change documents requirements and availability checks only. Plugin installation and unsupported agent-runtime configuration are excluded.

## Verification

Confirm every agent definition identifies its work category and required bundle, and `docs/ORCHESTRATION.md` describes the availability and fallback rules without weakening Git or BLE approval boundaries.
