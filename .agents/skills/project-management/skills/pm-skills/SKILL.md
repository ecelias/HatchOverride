---
name: pm-skills
description: Use when a project-management request needs deterministic lane routing, analysis of a saved Jira snapshot, or validation of a bounded delivery-loop plan or close decision.
---

# PM analytics

Use the three local Python tools for repeatable routing and delivery checks. This skill does not provide an agent harness or live Jira connection.

Run commands from this directory.

## Choose one tool

| Need | Command |
|---|---|
| Classify an ambiguous PM request | `python3 scripts/pm_goal_router.py --text "<goal>" --output json` |
| Convert an existing sanitized Jira snapshot into flow or sprint data | `python3 scripts/jira_snapshot_bridge.py --input <snapshot.json> --to flow` |
| Validate a bounded delivery plan or close decision | `python3 scripts/delivery_loop_gate.py --plan <plan.json> --mode plan` or `--mode close` |

Run `<command> --help` for accepted schemas and options.

## Workflow

1. Select one tool from the requested artifact; do not run all three by default.
2. Use only user-provided, repository-local, or authorized connector output as input.
3. Preserve the tool's exit status and output as verification evidence.
4. Route any selected specialty back through the parent `project-management` skill.
5. Report the input path, command, result, limitations, and next smallest action.

## Boundaries

- Do not invent Jira, Confluence, Linear, GitHub, milestone, forecast, or team state.
- Do not treat imported MCP examples as installed tools. Use live services only through an available authorized connector.
- Do not invoke removed command systems, bootstrap configuration, or absent sibling bundles.
- Forecasts require sufficient real history and remain ranges, never unsupported single-date promises.
- A failed or exhausted gate is an escalation, not success.
- Repository Git, hardware, BLE, and publication approval rules still apply.

## References

- Read `references/flow_forecasting_canon.md` for flow and forecast interpretation.
- Read `references/agentic_delivery_governance.md` for human ownership and audit guidance.
- Read `references/pm_loop_playbook.md` only for reusable loop patterns; ignore references to absent external harnesses.
