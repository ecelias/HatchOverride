# Repository instructions

## Mission

Build a documented, testable API for the Hatch Restore 2 without claiming unsupported protocol facts. Separate observed bytes from hypotheses and generated test fixtures.

## Working rules

- `project_manager` owns scope, task boundaries, and acceptance criteria.
- Use project-scoped agents in `.codex/agents/`; delegate only bounded, independent work.
- Record device/protocol evidence in `docs/` before turning it into implementation behavior.
- Prefer .NET/C# for the public API and native macOS CoreBluetooth for a peripheral emulator spike. Rust or C++ must earn their place with a measured platform need.
- Keep BLE transport, protocol encoding, and public API separable, but do not add interfaces until a second implementation or a test boundary requires one.
- Never use real patient data, credentials, private device identifiers, or proprietary captures in fixtures.
- Do not commit, push, open a PR, publish, pair with hardware, or transmit BLE writes without explicit human approval for that action.
- Run the smallest relevant build/test/check. Report unavailable hardware checks honestly.
- Review findings lead with correctness, safety, protocol evidence, and missing tests; style-only findings are noise.

## Definition of done

A task is done only when its acceptance criteria pass, documentation matches behavior, unsupported assumptions are marked, and the project manager accepts the handoff.
