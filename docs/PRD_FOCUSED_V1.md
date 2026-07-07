# Product requirements: focused v1

## Product summary

Build the smallest documented, testable API for a personally owned Hatch Restore 2 while preserving a traceable path from sanitized Bluetooth Low Energy observations to supported behavior.

V1 is one evidence-backed vertical slice, not a complete Restore 2 SDK. If evidence permits an operation, it succeeds by encoding that behavior deterministically, exposing it through a small C# API, and testing it on macOS without routine physical-hardware access. If evidence permits no operation, it succeeds by preserving reproducible negative or inconclusive results without introducing speculative behavior.

## Governing documents

This PRD defines product requirements. Repository safety rules and task completion remain governed by:

- [`AGENTS.md`](../AGENTS.md)
- [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md)
- [`ORCHESTRATION.md`](ORCHESTRATION.md)
- [`ADR 0001`](decisions/0001-evidence-first-stack.md)

If this PRD conflicts with `AGENTS.md`, `AGENTS.md` wins.

## Problem

The repository has no captured evidence establishing Restore 2 services, characteristics, commands, framing, responses, authentication, timing, or firmware-specific behavior. Prior work for other Hatch generations is useful design inspiration but is not protocol evidence for the Restore 2.

The product must therefore make unsupported behavior difficult to implement accidentally. Contributors need a repeatable path from observation to evidence, fixture, implementation, and hardware-free verification.

## Users

### Primary user

A technical owner of an authorized Hatch Restore 2 who wants a safe, local, testable C# API for an evidenced device operation.

### Secondary users

- A protocol contributor recording reproducible, sanitized observations.
- An API maintainer testing behavior without physical hardware.
- A reviewer auditing whether public behavior is supported by evidence.

## User outcome

Given an evidenced Restore 2 operation, a developer can call one documented C# API operation and verify its deterministic protocol behavior against a macOS GATT peripheral test double. If no operation can be observed safely and reproducibly, v1 must report that result and ship no speculative command.

## V1 scope

### Evidence and discovery

- A versioned evidence ledger with claim status labeled `observed`, `inferred`, `disproved`, or `unknown` and, where applicable, a separate maturity stage of `reproduced`, `fixture-backed`, `supported`, or `hardware-validated`.
- A sanitized inventory of observed advertisements, services, characteristics, properties, and descriptors when authorized evidence is available.
- A safe capture procedure that separates passive observation, pairing, reads, writes, and notifications.
- One reproduced command/notification pair if it can be observed safely after explicit human approval.
- Negative or inconclusive results recorded without converting them into implementation behavior.

### Protocol and fixtures

- A deterministic codec for exactly one evidenced operation, if the evidence gate passes.
- A generated fixture derived from sanitized evidence and clearly marked as synthetic, when an operation passes the evidence gate.
- Traceability from every implemented byte and field to an evidence-ledger entry.
- Explicit errors for unsupported, malformed, or unavailable behavior.

### Public API

- A small modern .NET/C# library exposing exactly one supported operation, unless the evidence gate correctly results in zero operations.
- Asynchronous cancellation and error behavior appropriate to BLE transport.
- Separation of BLE transport, protocol encoding, and public API only where the hardware-free test boundary requires it.
- No public claim broader than the supporting evidence.

### macOS test boundary

- A minimal native macOS CoreBluetooth `CBPeripheralManager` GATT peripheral test double for the evidenced synthetic GATT shape, when an operation passes the evidence gate.
- The smallest viable .NET/native integration or documented process boundary.
- A hardware-free automated check covering the supported API path, when one exists.
- Documentation of which controller, timing, radio, authentication, and firmware behaviors the test double does not reproduce.

### Contributor documentation

- Setup and execution instructions for the documented macOS and .NET environment.
- A runnable example for the supported API operation, when one exists.
- Instructions for running default hardware-free checks.
- Separate, opt-in instructions for any hardware check, including approval and safety prerequisites.

## Functional requirements

| ID | Requirement |
|---|---|
| FR-1 | Every implemented command, field, and response must link to sanitized, reproducible evidence. |
| FR-2 | The system must preserve raw sanitized observations separately from interpretations and generated fixtures. |
| FR-3 | The codec must produce deterministic bytes for the supported fixture and reject malformed input explicitly. |
| FR-4 | The public C# API must expose no more than one evidenced device operation in v1. |
| FR-5 | The supported API path must run against the macOS GATT test double without physical hardware. |
| FR-6 | Default build and test commands must not scan, pair, connect to, read from, or write to a physical device. |
| FR-7 | Hardware-dependent checks must be opt-in and require explicit human approval before BLE interaction. |
| FR-8 | Unsupported behavior must fail clearly rather than guess, silently degrade, or reuse another Hatch model's protocol. |

## Evidence requirements

Every evidence record must include:

- status label;
- interpretation and confidence;
- a falsifying or confirming experiment;
- links to derived fixtures and supported code when those artifacts exist, or an explicit statement that they do not.

An `observed` or `disproved` record must also include:

- a sanitized source artifact or reference;
- capture method, timestamp, conditions, and result;
- observed direction, timing, repetition, and errors when applicable.

Device model and relevant firmware/app versions must be recorded when available; their absence must be explicit.

Private identifiers, credentials, proprietary captures, and unrelated personal data must not enter fixtures or documentation. Generated fixtures must never be presented as device captures.

An observation becomes eligible for implementation only after reproduction under documented conditions. Hardware behavior must not be inferred from a test double.

## Safety and authorization

- Work is limited to owned or explicitly authorized devices and accounts.
- Authentication, encryption, firmware protection, and device safety controls must not be bypassed.
- Pairing, BLE transmission, and device writes require explicit human approval for that action.
- Git commits, pushes, pull requests, releases, and package publication require explicit human approval for that action.
- Hardware tests must be safe by default, isolated from normal tests, and honest about side effects.

## Quality requirements

- Deterministic protocol serialization and fixtures.
- Explicit cancellation, timeout, transport, protocol, and unsupported-operation failures.
- The smallest relevant runnable checks for each non-trivial behavior.
- No new dependency, interface, service, or language without a demonstrated v1 need.
- Documentation must match source, tests, and recorded evidence.
- Unavailable hardware verification must be reported as unavailable, not passed.

## Terminology

- **Observed:** directly captured or measured with recorded conditions.
- **Inferred:** consistent with evidence but not directly established; includes confidence and a falsifying experiment.
- **Disproved:** contradicted by reproducible evidence.
- **Unknown:** not established by current evidence.
- **Generated fixture:** synthetic test data derived from documented evidence.
- **Supported:** observed, reproduced, documented, fixture-backed, implemented, and tested.
- **GATT peripheral test double:** a synthetic CoreBluetooth peripheral used at the API test boundary.
- **Bluetooth emulator:** reserved for demonstrated reproduction of the relevant real system layer; v1 does not claim controller-level emulation.

## Non-goals

- Full Restore 2 protocol or feature coverage.
- Compatibility claims based on the 2017 Hatch Baby Rest protocol.
- A browser inspector, consumer application, cloud service, account automation, or database.
- Firmware modification or bypass of authentication, encryption, or safety controls.
- Controller-level Bluetooth emulation.
- Windows, Linux, mobile, or multi-device support.
- Rust or C++ without a measured platform requirement.
- Public package distribution or production-readiness claims.
- Abstractions for hypothetical future transports or device models.

## Evidence-gate outcomes

Ownership, sequencing, and handoffs follow [`ORCHESTRATION.md`](ORCHESTRATION.md).

If one operation passes the evidence gate, v1 includes its deterministic fixture, codec, C# API operation, GATT test-double path, hardware-free automated check, and runnable example.

If no operation passes the evidence gate, v1 includes the completed sanitized evidence ledger, capture procedure, reproducible negative or inconclusive results, open risks, and next falsifiable experiment. It includes no command fixture, codec, device-operation API, GATT shape, or supported-operation example. Its hardware-free check validates only documentation or evidence tooling that actually exists. This zero-operation result is acceptable when the project manager confirms that the approved evidence work was completed and no unsupported behavior was introduced.

## Acceptance criteria

V1 is accepted only when all applicable criteria pass:

- [ ] Every implemented byte, field, command, and response traces to a sanitized evidence-ledger entry and deterministic fixture.
- [ ] The public API contains exactly one supported operation, or zero when the evidence gate did not justify implementation.
- [ ] When an operation is supported, its path passes a documented hardware-free automated check on the supported macOS/.NET setup.
- [ ] When no operation is supported, the zero-operation handoff records the required negative or inconclusive result and contains no speculative protocol or API behavior.
- [ ] Default checks perform no physical-device BLE interaction.
- [ ] Hardware checks are separate, opt-in, approval-gated, and report their side effects.
- [ ] No fixture contains prohibited identifiers, credentials, personal data, or proprietary captures.
- [ ] Test-double results are not presented as real-device results.
- [ ] Public usage, errors, limitations, and evidence links are documented.
- [ ] ADR 0001 is accepted or superseded after its evidence conditions are resolved and before v1 acceptance.
- [ ] The code reviewer reports no unresolved correctness, safety, evidence, or focused-test findings.
- [ ] Documentation links resolve, terminology is consistent, governing rules are linked rather than redefined, and focused-v1 scope remains distinct from [`END_GOAL.md`](../END_GOAL.md).
- [ ] The project manager accepts the complete handoff.

Git publication and hardware interaction remain separate human-approved actions and are not implied by product acceptance.

## Open questions and evidence gates

- Does an authorized Restore 2 advertise BLE services under reproducible conditions?
- Which services, characteristics, properties, and descriptors are observable?
- What authentication, encryption, sequencing, timing, or firmware constraints exist?
- Can one operation and its response be observed safely and reproduced?
- Can CoreBluetooth advertise the required synthetic GATT shape accurately enough for the v1 API boundary?
- Is an in-process native bridge smaller and more reliable than a process boundary?

These questions must remain `unknown` until answered by recorded evidence. The next safe experiment is selected by the project manager and requires human approval whenever it involves hardware.

## Success measures

- 100% evidence traceability for implemented protocol behavior.
- One deterministic, hardware-free API vertical slice, if evidence permits.
- Zero unsupported protocol claims in public behavior and documentation.
- A new contributor can reproduce the default supported API path when evidence permits one, or reproduce the zero-operation evidence checks when it does not.
