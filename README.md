# Hatch Restore 2 API

An evidence-first project to discover the Hatch Restore 2 Bluetooth Low Energy protocol and expose it through a small, tested API.

The repository currently contains the Codex team and its operating rules. Product code begins only after protocol observations are recorded and the first transport spike is approved.

Focused v1 is currently on the zero-operation path: the recorded evidence does not justify a Restore 2 command fixture, codec, device-operation API, synthetic GATT shape, or supported-operation example.

## Start here

1. Read [the project charter](docs/PROJECT_CHARTER.md).
2. Read [the focused v1 product requirements](docs/PRD_FOCUSED_V1.md) and [the long-term product vision](END_GOAL.md).
3. Read [the orchestration workflow](docs/ORCHESTRATION.md).
4. Ask Codex: `Have project_manager plan the next milestone and delegate only the evidence-gathering work that can run independently.`

Per [`AGENTS.md`](AGENTS.md), the project team may create milestone branches, focused commits, pushes, and pull requests. Pull-request merges and high-risk publication operations remain human-approved.

## Hardware-free validation

Run the zero-operation evidence check:

```sh
python3 scripts/validate_zero_operation.py
```

Expected result:

- `PASS: zero-operation evidence validation`
- `supported_operations=0`
- `hardware_validation=unavailable/not run`
- `ble_actions=not run`
