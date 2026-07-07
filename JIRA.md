# Hatch Restore 2 focused v1 backlog

This is a lightweight personal-project backlog derived from [`docs/PRD_FOCUSED_V1.md`](docs/PRD_FOCUSED_V1.md). The PRD is the source of truth. The repository currently contains governance, planning, and agent configuration only; it has no evidence ledger, captures, fixtures, product source, native test double, build configuration, or tests. Existing governance documents are therefore treated as context, not as proof that product requirements are complete.

The backlog has one required evidence gate. After PROJ-007, follow either the one-operation path or the zero-operation path. Conditional tickets stay `Blocked` until that decision. Zero operations is a valid v1 outcome; unsupported protocol behavior must never be implemented to make the positive path appear complete.

## Ticket completion and Git workflow

Work is sequential in the shared checkout and uses one active write branch. For each activated ticket:

1. The project manager confirms that every dependency is merged into current `master`, the ticket is unblocked, and its acceptance criteria still match the selected evidence-gate path.
2. After confirming no write-capable agent is active, `github` updates local `master` and creates `codex/proj-###-short-slug` from that exact commit. No other agent creates or switches branches.
3. `github` records the base branch, base commit, ticket branch, and starting head, then communicates that context to every agent assigned to the ticket.
4. Agents complete only that ticket. Blocked work is documented without speculative implementation; no commit or PR represents a blocked ticket as complete.
5. After the project manager confirms all acceptance criteria and smallest relevant checks pass, `github` commits only the ticket's accepted work, pushes the branch, opens a PR to `master`, records base/head and the PR URL, and communicates the state.
6. The next ticket branch does not begin until the current ticket PR and all dependency PRs have explicit human merge approval and are merged. Once approved, `github` may merge the PR, update local `master`, and delete the ticket branch. Releases, force-pushes, history rewrites, and destructive remote changes still require separate explicit human approval.

Documentation-only tickets use the same branch, review, and merge gate. Conditional tickets on the unselected PROJ-007 path are marked not applicable in the gate record and receive no branch. A ticket blocked after branch creation keeps its branch and PR unmerged; `github` records the blocker and resumes that branch only after the blocker clears. Closely coupled tickets may share one branch only when the project manager records the reason before branch creation, all included ticket IDs, their combined acceptance checks, and a single human-approved PR; no such grouping is planned below.

## Branch and Merge Plan

| Ticket | Branch created only after | Branch name | Merge gate / conditional handling |
|---|---|---|---|
| PROJ-001 | Current `master` | `codex/proj-001-evidence-ledger` | Merge after PROJ-001 acceptance and checks pass. |
| PROJ-002 | PROJ-001 merged | `codex/proj-002-admission-rules` | Documentation-only; merge after checklist/link review passes. |
| PROJ-003 | PROJ-001 and PROJ-002 merged | `codex/proj-003-capture-procedure` | Documentation-only; merge after safety/approval review passes. |
| PROJ-004 | PROJ-001–PROJ-003 merged and hardware approval granted | `codex/proj-004-advertisement-evidence` | If blocked, retain branch unmerged; merge only recorded positive, negative, or inconclusive evidence. |
| PROJ-005 | PROJ-004 merged and action approval granted | `codex/proj-005-gatt-inventory` | If blocked, retain branch unmerged; merge only evidence-backed inventory/results. |
| PROJ-006 | PROJ-005 merged and per-action approval granted | `codex/proj-006-candidate-experiment` | Merge reproduced or documented negative/inconclusive result; never merge unsupported behavior. |
| PROJ-007 | PROJ-006 merged | `codex/proj-007-evidence-gate` | Merge only after PM selects exactly one path and marks the other path not applicable. |
| PROJ-008 | PROJ-002 and PROJ-007 merged; one-operation path selected | `codex/proj-008-generated-fixture` | No branch on zero-operation path; merge after provenance/privacy review. |
| PROJ-009 | PROJ-007 merged; one-operation path selected | `codex/proj-009-dotnet-structure` | No branch on zero-operation path; merge after restore/build/test checks pass. |
| PROJ-010 | PROJ-008 and PROJ-009 merged | `codex/proj-010-operation-codec` | No branch on zero-operation path; merge after deterministic and rejection tests pass. |
| PROJ-011 | PROJ-007 and PROJ-008 merged; one-operation path selected | `codex/proj-011-corebluetooth-spike` | No branch on zero-operation path; merge success, limitation, or failure evidence after focused check. |
| PROJ-012 | PROJ-009 and PROJ-011 merged | `codex/proj-012-native-boundary` | No branch on zero-operation path; merge after boundary proof and failure propagation checks pass. |
| PROJ-013 | PROJ-011 and PROJ-012 merged | `codex/proj-013-gatt-test-double` | No branch on zero-operation path; merge after native checks and cleanup validation pass. |
| PROJ-014 | PROJ-010, PROJ-012, and PROJ-013 merged | `codex/proj-014-transport-seam` | No branch on zero-operation path; merge after focused happy/failure-path tests pass. |
| PROJ-015 | PROJ-010 and PROJ-014 merged | `codex/proj-015-public-operation` | No branch on zero-operation path; merge after API-surface and public-contract tests pass. |
| PROJ-016 | PROJ-013–PROJ-015 merged | `codex/proj-016-hardware-free-check` | No branch on zero-operation path; merge after repeatable end-to-end check passes. |
| PROJ-017 | PROJ-015 and PROJ-016 merged | `codex/proj-017-operation-example` | Documentation/example ticket; no branch on zero-operation path; merge after the documented example passes. |
| PROJ-018 | PROJ-007 merged; zero-operation path selected | `codex/proj-018-zero-operation-check` | No branch on one-operation path; merge after the validator proves zero supported operations. |
| PROJ-019 | PROJ-018 merged | `codex/proj-019-zero-operation-handoff` | Documentation-only; no branch on one-operation path; merge after handoff/link checks pass. |
| PROJ-020 | PROJ-016 merged on one-operation path, or PROJ-018 merged on zero-operation path | `codex/proj-020-default-validation` | Merge after the selected-path default command passes without physical BLE interaction. |
| PROJ-021 | PROJ-003, PROJ-007, and PROJ-020 merged | `codex/proj-021-hardware-check-isolation` | Merge either isolated opt-in check or documented decision that none ships; add no speculative check. |
| PROJ-022 | PROJ-007 merged; plus PROJ-011–PROJ-012 merged on one-operation path or negative boundary recorded on zero-operation path | `codex/proj-022-resolve-adr` | Documentation-only; merge after ADR is accepted or superseded with evidence links. |
| PROJ-023 | PROJ-017 merged on one-operation path, or PROJ-019 merged on zero-operation path; PROJ-020–PROJ-022 merged | `codex/proj-023-contributor-docs` | Documentation-only; merge after commands, links, terminology, and path-specific claims validate. |
| PROJ-024 | PROJ-020–PROJ-023 and every activated path ticket merged | `codex/proj-024-final-audit` | Merge only when traceability/privacy/scope audit passes; failures block merge. |
| PROJ-025 | PROJ-024 merged | `codex/proj-025-acceptance-handoff` | Merge only after reviewer findings resolve and PM accepts the complete handoff. |

## Milestone 1: Evidence foundation

### PROJ-001 — Establish the versioned evidence ledger and artifact layout

- **ID:** PROJ-001
- **Title:** Establish the versioned evidence ledger and artifact layout
- **Goal / requirement addressed:** “A versioned evidence ledger” under **V1 scope / Evidence and discovery**; FR-1 and FR-2; **Evidence requirements**.
- **Category:** Infrastructure
- **Priority:** High
- **Status:** Not Started
- **Description:** Create the smallest repository-native structure that separates sanitized source observations, interpretations, and generated fixtures. Give each claim a stable identifier and use only the PRD status and maturity vocabulary.
- **Acceptance criteria:**
  - A ledger template records claim ID, `observed`/`inferred`/`disproved`/`unknown` status, optional maturity, interpretation, confidence, confirming or falsifying experiment, and links to derived artifacts or an explicit statement that none exist.
  - `observed` and `disproved` records require a sanitized source reference plus capture method, timestamp, conditions, result, direction, timing, repetition, and errors when applicable.
  - Device model and firmware/app versions are recorded when available; absence is explicit.
  - Paths and labels make sanitized observations, interpretations, and generated fixtures distinguishable without reading their contents.
  - Seed records cover every PRD open evidence question as `unknown`; no service, characteristic, command, or byte value is asserted.
  - All repository-relative links resolve.
- **Relevant code areas:** New `docs/evidence/` ledger, templates, and artifact directories.
- **Dependencies / blockers:** None.
- **Estimated effort:** Medium
- **Notes:** Inferred from repository structure. Markdown is sufficient until actual artifact volume proves a tooling need.

### PROJ-002 — Define sanitization and provenance admission rules

- **ID:** PROJ-002
- **Title:** Define sanitization and provenance admission rules
- **Goal / requirement addressed:** FR-2; **Evidence requirements** privacy and generated-fixture rules; acceptance criterion prohibiting identifiers, credentials, personal data, and proprietary captures.
- **Category:** Documentation
- **Priority:** High
- **Status:** Not Started
- **Description:** Define a reviewable evidence-admission checklist before any observation is committed. Originals remain outside the repository; only sanitized artifacts and required provenance metadata may enter it.
- **Acceptance criteria:**
  - The checklist prohibits private device identifiers, credentials, unrelated personal data, proprietary captures, and unsanitized source material.
  - The checklist defines how retained sanitized excerpts preserve method, conditions, time, and result without retaining prohibited data.
  - Generated fixtures must be labeled synthetic and linked to ledger claims; they cannot be described as captures.
  - A manual review and repository-search step can be recorded in a handoff without claiming automated detection is complete.
  - A dry run against the empty evidence layout passes without hardware interaction.
- **Relevant code areas:** `docs/evidence/`, contributor evidence instructions.
- **Dependencies / blockers:** PROJ-001.
- **Estimated effort:** Small
- **Notes:** “Proprietary captures” is not precisely defined by the PRD; this ticket must document the accepted transformed-evidence boundary before capture.

### PROJ-003 — Write the staged safe BLE capture procedure

- **ID:** PROJ-003
- **Title:** Write the staged safe BLE capture procedure
- **Goal / requirement addressed:** “A safe capture procedure that separates passive observation, pairing, reads, writes, and notifications”; FR-6, FR-7; **Safety and authorization**.
- **Category:** Documentation
- **Priority:** High
- **Status:** Not Started
- **Description:** Document discrete observation stages, approval points, sanitization, side effects, and abort conditions. The procedure must be reviewable without contacting a device.
- **Acceptance criteria:**
  - Passive advertisement observation, connection, pairing, reads, notification subscription, and writes are separate stages.
  - Each stage states prerequisites, expected BLE side effects, collected fields, output path, sanitization step, and error/abort recording.
  - Pairing, transmission, and device writes stop for explicit human approval for that action.
  - Work is limited to owned or explicitly authorized devices/accounts and does not bypass authentication, encryption, firmware protection, or safety controls.
  - Default build/test commands are explicitly excluded from every physical-device stage.
  - A manual dry run verifies the procedure without scanning, pairing, connecting, reading, subscribing, or writing.
- **Relevant code areas:** New `docs/evidence/capture-procedure.md`, ledger templates from PROJ-001.
- **Dependencies / blockers:** PROJ-001, PROJ-002.
- **Estimated effort:** Medium
- **Notes:** The PRD explicitly approval-gates pairing/transmission/writes but also refers broadly to approval for hardware experiments. Project-manager approval is required before passive scanning until that ambiguity is resolved.

## Milestone 2: Authorized discovery and reproduction

### PROJ-004 — Record sanitized Restore 2 advertisement observations

- **ID:** PROJ-004
- **Title:** Record sanitized Restore 2 advertisement observations
- **Goal / requirement addressed:** **Evidence and discovery** inventory; open question “Does an authorized Restore 2 advertise BLE services under reproducible conditions?”
- **Category:** Research
- **Priority:** High
- **Status:** Blocked
- **Description:** Under explicit approval, perform only the passive stage and record reproducible positive, negative, or inconclusive advertisement observations without connecting to the device.
- **Acceptance criteria:**
  - Approval for the planned physical-device observation is recorded before execution.
  - The ledger records model/version context or explicit absence, timestamp, conditions, repetitions, errors, and sanitized advertisement fields.
  - The experiment plan defines the repetition threshold before execution; results do not invent a universal threshold.
  - No pairing, connection, read, notification subscription, or write occurs.
  - Negative or inconclusive observations remain negative or inconclusive and include the next falsifiable experiment.
  - PROJ-002 privacy/provenance review passes before artifacts are committed.
- **Relevant code areas:** `docs/evidence/` sanitized observations, inventory, and ledger.
- **Dependencies / blockers:** PROJ-001–PROJ-003; owned/authorized Restore 2; explicit human approval; available macOS BLE capability.
- **Estimated effort:** Medium
- **Notes:** Cannot be validated from the current repository. Unavailable hardware is reported as unavailable, not passed.

### PROJ-005 — Inventory observed GATT services and characteristics

- **ID:** PROJ-005
- **Title:** Inventory observed GATT services and characteristics
- **Goal / requirement addressed:** Sanitized inventory under **Evidence and discovery**; PRD open questions about services, characteristics, properties, descriptors, authentication, encryption, sequencing, timing, and firmware constraints; ADR 0001 evidence.
- **Category:** Research
- **Priority:** High
- **Status:** Blocked
- **Description:** If authorized discovery is feasible, record only observed GATT services, characteristics, properties, and descriptors. Keep interpretations and unknowns separate from source observations.
- **Acceptance criteria:**
  - Explicit approval is recorded before connection, pairing, reads, notification subscription, or transmission as applicable.
  - Sanitized artifacts and ledger records include method, time, conditions, repetitions, direction, timing, errors, and model/firmware/app context or explicit absence.
  - UUIDs and properties appear as facts only when observed; interpretations use `inferred` or `unknown` with confidence and a falsifying experiment.
  - Authentication/encryption prompts or failures are recorded without bypass attempts.
  - A reproducible inventory or a reproducible negative/inconclusive result is produced.
  - PROJ-002 privacy/provenance review passes.
- **Relevant code areas:** `docs/evidence/` sanitized observations, GATT inventory, and ledger.
- **Dependencies / blockers:** PROJ-004; explicit action approval; hardware and GATT access.
- **Estimated effort:** Large
- **Notes:** Another Hatch generation’s UUIDs are design context only and must not populate this inventory.

### PROJ-006 — Define and execute one safe candidate-operation experiment

- **ID:** PROJ-006
- **Title:** Define and execute one safe candidate-operation experiment
- **Goal / requirement addressed:** “One reproduced command/notification pair if it can be observed safely”; reproduction eligibility under **Evidence requirements**; open question about observing one operation safely.
- **Category:** Research
- **Priority:** High
- **Status:** Blocked
- **Description:** Select at most one candidate from observed evidence, define pass/fail/inconclusive rules before execution, obtain the required approval, and reproduce it in a separate documented observation. If no candidate is safe or reproducible, preserve that result without implementation behavior.
- **Acceptance criteria:**
  - The project manager selects exactly one candidate or records that no safe candidate exists.
  - The experiment links observed ledger claims and defines preconditions, permitted action, expected direction/timing/repetition, safety bounds, abort criteria, sanitization, and confirming/falsifying outcomes before execution.
  - Approval is recorded before pairing, transmission, or write activity.
  - A positive result includes sanitized request/notification evidence and at least one documented repeat under the predefined conditions before maturity becomes `reproduced`.
  - A failed, unsafe, or inconsistent repeat remains `unknown`, `inferred`, or `disproved` as warranted and records open risks plus the next falsifiable experiment.
  - No fixture, codec, public operation, or GATT test-double shape is created by this ticket.
- **Relevant code areas:** `docs/evidence/` experiment plan, sanitized observations, and ledger.
- **Dependencies / blockers:** PROJ-005; project-manager selection; owned/authorized hardware; explicit per-action human approval.
- **Estimated effort:** Large
- **Notes:** The PRD does not prescribe an independent-session/device count or tolerance; define sufficiency in the experiment plan rather than fabricating it in advance.

## Milestone 3: Evidence gate

### PROJ-007 — Decide and freeze the focused-v1 evidence-gate outcome

- **ID:** PROJ-007
- **Title:** Decide and freeze the focused-v1 evidence-gate outcome
- **Goal / requirement addressed:** **Evidence-gate outcomes**; FR-4 and FR-8; acceptance criterion requiring exactly one supported operation or zero.
- **Category:** Research
- **Priority:** High
- **Status:** Blocked
- **Description:** Audit the evidence and choose exactly one v1 path: one operation eligible for implementation, or a zero-operation handoff. This is the scope boundary for all subsequent work.
- **Acceptance criteria:**
  - The decision record assesses observed and reproduced evidence, sanitization, documented conditions, byte/field completeness, safety constraints, fixture feasibility, and remaining unknowns.
  - A one-operation decision names exactly one operation and stable ledger claim IDs; all request/response fields needed for deterministic behavior are evidenced.
  - A zero-operation decision links the negative/inconclusive result, open risks, and next falsifiable experiment and prohibits a command fixture, codec, device-operation API, synthetic GATT shape, and supported-operation example.
  - Test-double behavior is not used as hardware evidence.
  - The project manager accepts the decision and records which conditional tickets are activated.
- **Relevant code areas:** `docs/evidence/` gate decision and ledger.
- **Dependencies / blockers:** PROJ-006.
- **Estimated effort:** Medium
- **Notes:** The PRD defines no numeric confidence threshold. Eligibility is based on evidence completeness, not an invented score.

## Milestone 4A: One-operation vertical slice — conditional

All tickets in this milestone remain blocked unless PROJ-007 selects the one-operation path.

### PROJ-008 — Create the synthetic generated fixture

- **ID:** PROJ-008
- **Title:** Create the synthetic generated fixture
- **Goal / requirement addressed:** **Protocol and fixtures**; FR-1, FR-2, FR-3; deterministic-fixture acceptance criterion.
- **Category:** Testing
- **Priority:** High
- **Status:** Blocked
- **Description:** Derive the smallest deterministic generated fixture for the selected operation from sanitized, reproduced evidence. It is synthetic test data, never a device capture.
- **Acceptance criteria:**
  - The fixture is labeled generated/synthetic and links the exact ledger claim IDs.
  - Every byte and field maps to evidence; unknown bytes receive no invented semantics.
  - Exact expected request and response/notification vectors are deterministic.
  - Malformed and unsupported cases needed for later codec tests are specified without inventing device responses.
  - Manual review and repository searches find no prohibited identifiers, credentials, personal data, or proprietary capture material.
- **Relevant code areas:** New generated-fixture directory, evidence ledger, fixture metadata.
- **Dependencies / blockers:** PROJ-002; PROJ-007 one-operation decision.
- **Estimated effort:** Medium
- **Notes:** Must not be created for the zero-operation path.

### PROJ-009 — Create the minimal modern .NET solution and test structure

- **ID:** PROJ-009
- **Title:** Create the minimal modern .NET solution and test structure
- **Goal / requirement addressed:** **Public API** small modern .NET/C# library; **Quality requirements** smallest relevant checks and no unjustified dependencies.
- **Category:** Infrastructure
- **Priority:** High
- **Status:** Blocked
- **Description:** Add only the library and smallest test project needed by the evidenced vertical slice. Do not scaffold services, frontends, databases, containers, speculative transports, or future device models.
- **Acceptance criteria:**
  - The supported .NET SDK is selected and documented; restore, build, and test commands are reproducible.
  - A library and smallest test project compile before protocol behavior is added.
  - The initial public surface exposes no device operation until PROJ-015.
  - No new dependency or abstraction lacks a demonstrated vertical-slice need.
  - The structure supports the fixture/codec and actual hardware-free test boundary without claiming physical-device support.
- **Relevant code areas:** New solution, `src/`, `tests/`, optional SDK pin only when needed.
- **Dependencies / blockers:** PROJ-007 one-operation decision; supported .NET SDK availability.
- **Estimated effort:** Medium
- **Notes:** Inferred from repository structure. The current repository has no .NET files, and the currently inspected environment has no `dotnet` executable; verification is unavailable until provisioned.

### PROJ-010 — Implement the deterministic one-operation codec

- **ID:** PROJ-010
- **Title:** Implement the deterministic one-operation codec
- **Goal / requirement addressed:** **Protocol and fixtures**; FR-1, FR-3, FR-8; explicit malformed/unsupported errors.
- **Category:** Feature
- **Priority:** High
- **Status:** Blocked
- **Description:** Implement encoding and any evidenced decoding for exactly the selected operation, with byte-level provenance and explicit validation failures.
- **Acceptance criteria:**
  - Repeated serialization of valid input is byte-for-byte identical to PROJ-008.
  - Every implemented byte/field cites a ledger claim and generated fixture.
  - Focused tests cover the deterministic vector plus malformed, truncated, extra, out-of-range, and unsupported inputs that are meaningful for the evidenced format.
  - Failures are explicit protocol/unsupported errors; the codec does not guess, silently degrade, or reuse another Hatch model’s protocol.
  - No second command or speculative field is implemented.
- **Relevant code areas:** Protocol code under `src/`, fixture-backed unit tests under `tests/`.
- **Dependencies / blockers:** PROJ-008, PROJ-009.
- **Estimated effort:** Large
- **Notes:** Field names and semantics remain unknown until PROJ-007; they cannot be supplied by this backlog.

### PROJ-011 — Prove the minimal CoreBluetooth synthetic GATT shape

- **ID:** PROJ-011
- **Title:** Prove the minimal CoreBluetooth synthetic GATT shape
- **Goal / requirement addressed:** **macOS test boundary**; FR-5; open question about CoreBluetooth fidelity; ADR 0001 evidence.
- **Category:** Research
- **Priority:** High
- **Status:** Blocked
- **Description:** Spike the smallest native macOS `CBPeripheralManager` program needed to represent only the evidenced synthetic GATT shape and determine whether CoreBluetooth can satisfy the API test boundary.
- **Acceptance criteria:**
  - The spike advertises only the evidenced synthetic service/characteristic shape and implements only required callbacks.
  - Manager state, readiness, subscription, read/write, and notification handling are included only where the selected operation requires them.
  - A documented local check records success, limitation, or failure without using a Restore 2.
  - Results are labeled test-double evidence, not hardware evidence or controller-level emulation.
  - Swift/Objective-C is used for the thinnest native component; Rust/C++ is not added without a measured need.
- **Relevant code areas:** New minimal native macOS test-double spike and focused checks/docs.
- **Dependencies / blockers:** PROJ-007 one-operation decision, PROJ-008, supported macOS/CoreBluetooth development environment.
- **Estimated effort:** Large
- **Notes:** Full Xcode/toolchain availability and exact CoreBluetooth fidelity are not established by the current repository.

### PROJ-012 — Select and prove the smallest .NET/native boundary

- **ID:** PROJ-012
- **Title:** Select and prove the smallest .NET/native boundary
- **Goal / requirement addressed:** “The smallest viable .NET/native integration or documented process boundary”; ADR 0001 evidence.
- **Category:** Research
- **Priority:** High
- **Status:** Blocked
- **Description:** Compare only the in-process bridge and documented process boundary against the concrete vertical slice, select the smaller reliable option, and leave a runnable proof.
- **Acceptance criteria:**
  - The comparison uses the selected operation’s actual startup, readiness, request/notification, cancellation, shutdown, and error needs.
  - The chosen boundary has a runnable proof and documents startup/handshake/readiness/shutdown behavior.
  - Native/process failures, timeout, and cancellation can be propagated to .NET explicitly.
  - No Rust/C++ or generic IPC framework is added without a measured need.
  - The decision and evidence are recorded for ADR resolution.
- **Relevant code areas:** Native spike, .NET test harness, ADR evidence/decision documentation.
- **Dependencies / blockers:** PROJ-009, PROJ-011.
- **Estimated effort:** Medium
- **Notes:** The PRD intentionally leaves bridge versus process boundary open.

### PROJ-013 — Implement the minimal macOS GATT peripheral test double

- **ID:** PROJ-013
- **Title:** Implement the minimal macOS GATT peripheral test double
- **Goal / requirement addressed:** **macOS test boundary** minimal native `CBPeripheralManager` GATT peripheral test double; FR-5.
- **Category:** Feature
- **Priority:** High
- **Status:** Blocked
- **Description:** Convert the proven spike into the smallest deterministic test double that serves the generated fixture for the selected operation.
- **Acceptance criteria:**
  - The test double exposes only the PROJ-008 synthetic GATT shape and deterministic behavior required by the selected operation.
  - It provides a reliable readiness signal and deterministic request/response or notification behavior.
  - Startup and shutdown are repeatable and clean up on success or failure.
  - Controller, radio, real timing, authentication, encryption, pairing, firmware, interference, and other unmodeled behaviors are explicitly not claimed.
  - Focused native checks pass without a Restore 2.
- **Relevant code areas:** Native macOS test-double implementation and focused checks.
- **Dependencies / blockers:** PROJ-011, PROJ-012.
- **Estimated effort:** Large
- **Notes:** Preserve the PRD term “GATT peripheral test double,” not “Bluetooth emulator.”

### PROJ-014 — Implement the BLE transport test seam and failure model

- **ID:** PROJ-014
- **Title:** Implement the BLE transport test seam and failure model
- **Goal / requirement addressed:** **Public API** asynchronous cancellation/error behavior and separation only where the test boundary requires it; **Quality requirements** explicit cancellation, timeout, transport, protocol, and unsupported failures.
- **Category:** Feature
- **Priority:** High
- **Status:** Blocked
- **Description:** Add only the transport seam required to target the synthetic test double. Prevent silent physical-device fallback and make each required failure observable.
- **Acceptance criteria:**
  - The automated path targets only the configured synthetic service/test-double boundary and cannot silently select a physical Restore 2.
  - Cancellation reaches the active operation and bounded timeout behavior is explicit.
  - Cancellation, timeout, unavailable/native/transport, malformed/protocol, and unsupported outcomes are distinguishable and tested.
  - No interface exists for hypothetical transports or device models beyond the actual test boundary.
  - Focused tests cover cancellation, timeout/unavailable behavior, and the synthetic happy path at the narrowest viable layer.
- **Relevant code areas:** .NET library transport boundary, failure types, focused tests.
- **Dependencies / blockers:** PROJ-010, PROJ-012, PROJ-013.
- **Estimated effort:** Large
- **Notes:** Exception hierarchy versus result types and timeout ownership are unspecified; decide narrowly from the proven boundary.

### PROJ-015 — Expose exactly one evidence-backed asynchronous C# operation

- **ID:** PROJ-015
- **Title:** Expose exactly one evidence-backed asynchronous C# operation
- **Goal / requirement addressed:** **Public API**; FR-4; FR-8; acceptance criterion requiring exactly one supported operation.
- **Category:** Feature
- **Priority:** High
- **Status:** Blocked
- **Description:** Expose the single selected operation through the smallest public C# API, using the evidenced codec and transport boundary.
- **Acceptance criteria:**
  - Exactly one device operation is public; an API-surface check verifies there is no second operation.
  - The operation is asynchronous, accepts cancellation, and maps the deterministic supported response correctly.
  - Unsupported, unavailable, timeout, cancellation, transport, and malformed/protocol outcomes fail explicitly.
  - Public documentation links the exact evidence and fixture and makes no compatibility or production-readiness claim beyond it.
  - Focused tests cover the public success and failure contract without hardware.
- **Relevant code areas:** Public .NET library API and tests.
- **Dependencies / blockers:** PROJ-010, PROJ-014.
- **Estimated effort:** Medium
- **Notes:** Exact operation name and input/output types remain unknown until PROJ-007.

### PROJ-016 — Add the end-to-end hardware-free macOS API check

- **ID:** PROJ-016
- **Title:** Add the end-to-end hardware-free macOS API check
- **Goal / requirement addressed:** FR-5, FR-6; **macOS test boundary** hardware-free automated check; positive-path acceptance criterion.
- **Category:** Testing
- **Priority:** High
- **Status:** Blocked
- **Description:** Prove the vertical slice from the public C# API through transport and codec to the synthetic CoreBluetooth test double without a physical device.
- **Acceptance criteria:**
  - One documented command starts the test double, waits for readiness, calls the public operation, and shuts the test double down.
  - The check asserts exact fixture request bytes and deterministic response/result.
  - It covers cancellation and at least one explicit boundary failure without broadening into a full suite.
  - It requires no Restore 2 and performs no general physical-device scan, pair, connect, read, or write.
  - Cleanup occurs on pass and failure; repeated runs are reliable on the documented macOS/.NET setup.
  - Output says the result came from a test double, not real hardware.
- **Relevant code areas:** .NET integration tests, native test-double harness, test documentation.
- **Dependencies / blockers:** PROJ-013–PROJ-015; supported macOS/.NET environment.
- **Estimated effort:** Large
- **Notes:** CoreBluetooth discovery behavior must be constrained or isolated so default checks do not observe unrelated physical peripherals.

### PROJ-017 — Add the runnable supported-operation example

- **ID:** PROJ-017
- **Title:** Add the runnable supported-operation example
- **Goal / requirement addressed:** **Contributor documentation** runnable example “when one exists”; public usage acceptance criterion.
- **Category:** Documentation
- **Priority:** Medium
- **Status:** Blocked
- **Description:** Add the smallest C# example that calls the single operation against the test double and demonstrates cancellation and actionable failure handling.
- **Acceptance criteria:**
  - The example builds and runs with a documented command against the synthetic test double.
  - It calls only the supported operation and demonstrates cancellation plus explicit error handling.
  - It links the evidence, fixture, and limitations.
  - It makes no real-hardware, full-protocol, compatibility, distribution, or production-readiness claim.
- **Relevant code areas:** New `examples/` project or equivalent, README usage link.
- **Dependencies / blockers:** PROJ-015, PROJ-016.
- **Estimated effort:** Small
- **Notes:** Must not exist for the zero-operation path.

## Milestone 4B: Zero-operation handoff — conditional

These tickets activate only if PROJ-007 selects the zero-operation path.

### PROJ-018 — Implement the zero-operation evidence validation check

- **ID:** PROJ-018
- **Title:** Implement the zero-operation evidence validation check
- **Goal / requirement addressed:** Zero-operation **Evidence-gate outcomes**; acceptance criterion requiring the negative/inconclusive handoff with no speculative behavior.
- **Category:** Testing
- **Priority:** High
- **Status:** Blocked
- **Description:** Add the smallest hardware-free check for the evidence artifacts that actually exist. Do not scaffold .NET or a fake protocol merely to create a test target.
- **Acceptance criteria:**
  - One documented command validates required ledger fields, PRD status terminology, artifact links, and generated-versus-observed labeling.
  - The check verifies that no command fixture, codec, device-operation API, synthetic GATT shape, or supported-operation example exists.
  - The check performs no BLE scan, pair, connect, read, notification subscription, or write.
  - Output explicitly reports zero supported operations and hardware validation as unavailable/not run.
  - The check uses the standard library or an already-required runtime unless a dependency is demonstrably necessary.
- **Relevant code areas:** Evidence validation script/check and evidence documentation.
- **Dependencies / blockers:** PROJ-007 zero-operation decision.
- **Estimated effort:** Medium
- **Notes:** Inferred from repository structure. Automated privacy scanning may assist review but cannot claim complete detection.

### PROJ-019 — Publish the zero-operation contributor handoff

- **ID:** PROJ-019
- **Title:** Publish the zero-operation contributor handoff
- **Goal / requirement addressed:** Zero-operation **Evidence-gate outcomes**; **Contributor documentation**; zero-operation acceptance criterion.
- **Category:** Documentation
- **Priority:** High
- **Status:** Blocked
- **Description:** Document the reproducible negative/inconclusive outcome, open risks, next falsifiable experiment, and evidence-only validation path without implying a supported device operation.
- **Acceptance criteria:**
  - The handoff links the completed ledger, capture procedure, negative/inconclusive result, open risks, and next falsifiable experiment.
  - It records model/firmware/app versions or their explicit absence.
  - It gives the exact PROJ-018 hardware-free command and expected zero-operation result.
  - It distinguishes sanitized observations, interpretations, and generated data and contains no supported-operation usage example.
  - A new contributor can reproduce the evidence checks from the documented setup.
- **Relevant code areas:** README focused-v1 status and `docs/evidence/` handoff.
- **Dependencies / blockers:** PROJ-018.
- **Estimated effort:** Small
- **Notes:** Negative or inconclusive evidence is a valid deliverable, not a failed positive implementation.

## Milestone 5: Shared quality, documentation, and acceptance

### PROJ-020 — Provide one safe default validation entry point

- **ID:** PROJ-020
- **Title:** Provide one safe default validation entry point
- **Goal / requirement addressed:** FR-6; **Contributor documentation** default checks; success measure that a contributor can reproduce the selected path.
- **Category:** Infrastructure
- **Priority:** High
- **Status:** Blocked
- **Description:** Provide one repository-level command that runs the applicable hardware-free checks for the selected evidence-gate outcome and nothing else.
- **Acceptance criteria:**
  - The documented command exits nonzero on failure and runs PROJ-016 for the one-operation path or PROJ-018 for the zero-operation path.
  - No physical-device BLE interaction is reachable from the default test selection.
  - The command works on the documented supported environment and reports missing prerequisites honestly.
  - It does not report unavailable hardware verification as passed.
  - No task runner or dependency is added when a standard tool or small script suffices.
- **Relevant code areas:** Root validation entry point, README setup/check instructions.
- **Dependencies / blockers:** PROJ-016 or PROJ-018.
- **Estimated effort:** Small
- **Notes:** Inferred from repository structure because no command convention exists. CI is not a PRD requirement and is intentionally omitted until local reproducibility demonstrates a need.

### PROJ-021 — Isolate and document any opt-in hardware check

- **ID:** PROJ-021
- **Title:** Isolate and document any opt-in hardware check
- **Goal / requirement addressed:** FR-7; **Safety and authorization**; acceptance criterion for separate, approval-gated hardware checks.
- **Category:** Testing
- **Priority:** High
- **Status:** Blocked
- **Description:** If a hardware validation command is retained after discovery, isolate it from defaults and require an explicit acknowledgment before any BLE interaction. Do not create speculative device-write behavior merely to satisfy this ticket.
- **Acceptance criteria:**
  - Any hardware command is separately named/tagged and excluded from PROJ-020.
  - It refuses to interact without explicit opt-in/approval acknowledgment and prints intended side effects before execution.
  - Documentation requires owned/authorized hardware and identifies separate pairing/transmission/write approval points.
  - No identifiers or credentials are embedded; unavailable hardware is reported as unavailable/skipped, not passed.
  - If no hardware check is shipped, the decision and absence are documented and this ticket is closed without adding one.
- **Relevant code areas:** Optional hardware-test selection/configuration and safety documentation.
- **Dependencies / blockers:** PROJ-003; selected evidence-gate path; existence of an approved hardware check.
- **Estimated effort:** Small
- **Notes:** Conditional applicability is explicit in the PRD phrase “any hardware check.”

### PROJ-022 — Resolve ADR 0001 from recorded evidence

- **ID:** PROJ-022
- **Title:** Resolve ADR 0001 from recorded evidence
- **Goal / requirement addressed:** Acceptance criterion “ADR 0001 is accepted or superseded after its evidence conditions are resolved and before v1 acceptance.”
- **Category:** Documentation
- **Priority:** High
- **Status:** Blocked
- **Description:** Accept ADR 0001 only when its evidence conditions are met, or supersede it with the smallest evidence-backed alternative. Do not wave through missing native-boundary evidence.
- **Acceptance criteria:**
  - Restore 2 observation evidence links to PROJ-004–PROJ-007 results.
  - The one-operation path links CoreBluetooth feasibility and .NET/native boundary evidence from PROJ-011 and PROJ-012.
  - The zero-operation path records which ADR conditions could not be resolved and accepts or supersedes the proposal without claiming an untested vertical slice.
  - The resulting ADR status is `accepted` or `superseded` before final acceptance.
  - No controller-level emulation or Rust/C++ need is claimed without evidence.
- **Relevant code areas:** `docs/decisions/0001-evidence-first-stack.md` and, only if needed, a superseding ADR.
- **Dependencies / blockers:** PROJ-007; PROJ-011–PROJ-012 for the positive path; documented negative/inconclusive boundary for the zero path.
- **Estimated effort:** Small
- **Notes:** The exact zero-operation ADR resolution is ambiguous because ADR 0001 asks for native-boundary evidence while the PRD forbids a GATT shape when the evidence gate fails; the resolution must record that constraint explicitly.

### PROJ-023 — Complete contributor setup, usage, error, and limitation documentation

- **ID:** PROJ-023
- **Title:** Complete contributor setup, usage, error, and limitation documentation
- **Goal / requirement addressed:** **Contributor documentation**; acceptance criterion “Public usage, errors, limitations, and evidence links are documented”; documentation quality requirements.
- **Category:** Documentation
- **Priority:** High
- **Status:** Blocked
- **Description:** Document the selected path from a clean contributor perspective and keep governing rules linked rather than duplicated.
- **Acceptance criteria:**
  - Setup names supported macOS, .NET, and native-toolchain versions or explicitly states unresolved prerequisites.
  - Instructions cover PROJ-020 and, for the positive path, starting the test double, calling the API/example, cancellation, and every public error category.
  - Positive-path docs link operation evidence/fixture and list controller, timing, radio, authentication, encryption, pairing, firmware, interference, and other behaviors the test double does not reproduce.
  - Zero-path docs contain no API usage claim and link the negative/inconclusive handoff.
  - Hardware steps, if any, are separate and opt-in; all commands and relative links are checked.
  - Terminology matches the PRD and focused-v1 scope remains distinct from `END_GOAL.md`.
- **Relevant code areas:** `README.md`, `docs/evidence/`, API/example docs when applicable.
- **Dependencies / blockers:** PROJ-017 or PROJ-019; PROJ-020–PROJ-022.
- **Estimated effort:** Medium
- **Notes:** Supported toolchain versions are currently unspecified and cannot be fabricated from the repository.

### PROJ-024 — Audit evidence traceability, privacy, and public scope

- **ID:** PROJ-024
- **Title:** Audit evidence traceability, privacy, and public scope
- **Goal / requirement addressed:** FR-1–FR-8; all applicable **Acceptance criteria**; success measures for 100% traceability and zero unsupported claims.
- **Category:** Testing
- **Priority:** High
- **Status:** Blocked
- **Description:** Run a final cross-artifact audit tailored to the selected evidence-gate outcome before code review and project-manager acceptance.
- **Acceptance criteria:**
  - Positive path: every implemented byte, field, command, and response maps ledger → generated fixture → code → focused test → usage documentation, with no orphan implementation.
  - Positive path: an API-surface check confirms exactly one public operation; test-double results are labeled synthetic.
  - Zero path: the audit confirms no command fixture, codec, device-operation API, synthetic GATT shape, or supported-operation example exists.
  - Both paths: prohibited-data review is recorded, links resolve, terminology is consistent, default checks pass, and physical hardware checks are absent or separately approval-gated.
  - Unavailable hardware verification is reported unavailable rather than passed.
  - Any failed criterion blocks acceptance and names the artifact requiring correction.
- **Relevant code areas:** Evidence ledger, fixtures, source/tests or zero-operation validator, README/docs, validation output.
- **Dependencies / blockers:** PROJ-020–PROJ-023 and all activated path tickets.
- **Estimated effort:** Medium
- **Notes:** A small audit script is justified only where it provides a reliable failure signal; manual evidence/privacy review remains necessary.

### PROJ-025 — Perform final review and project-manager acceptance handoff

- **ID:** PROJ-025
- **Title:** Perform final review and project-manager acceptance handoff
- **Goal / requirement addressed:** Final **Acceptance criteria** requiring no unresolved reviewer findings and project-manager acceptance; repository **Definition of done**.
- **Category:** Testing
- **Priority:** High
- **Status:** Blocked
- **Description:** Run the delivery gate, obtain evidence-focused code review, reconcile documentation with behavior, and produce the auditable v1 handoff. Publication and merge remain separate human-approved actions.
- **Acceptance criteria:**
  - The applicable PROJ-020 command passes on the documented setup and its output is recorded.
  - The code reviewer reports no unresolved correctness, safety, protocol-evidence, or focused-test findings; style-only work does not block delivery.
  - Documentation matches source/tests or the zero-operation artifact set.
  - The handoff records decisions, evidence paths, changed artifacts, checks, unavailable checks, open risks, and next falsifiable action.
  - The project manager verifies every applicable PRD acceptance criterion and explicitly accepts the selected-path handoff.
  - Any commit/push/PR follows `docs/ORCHESTRATION.md`; PR merge, release, package publication, and hardware interaction remain human-approved.
- **Relevant code areas:** Entire focused-v1 artifact set; delivery/review records.
- **Dependencies / blockers:** PROJ-024; code-review and documentation-agent handoffs.
- **Estimated effort:** Medium
- **Notes:** Public package distribution, release, and production-readiness claims are v1 non-goals and are not completion tasks.

## Project Goal Traceability

| PRD major goal or requirement | Tickets | Validation / ambiguity flag |
|---|---|---|
| Product summary and user outcome: one evidence-backed vertical slice or honest zero-operation result | PROJ-004–PROJ-007, PROJ-008–PROJ-019, PROJ-025 | Positive and zero-operation paths are mutually exclusive until PROJ-007. |
| Versioned evidence ledger and claim maturity | PROJ-001, PROJ-007, PROJ-024 | No ledger currently exists. |
| Sanitized advertisement/GATT inventory | PROJ-002–PROJ-005 | Hardware access, authorization, firmware/app context, and observability are currently unavailable or unknown. |
| Safe capture procedure | PROJ-002, PROJ-003 | Passive-scan approval semantics are broader/less explicit than pairing/write semantics and must be resolved before execution. |
| One reproduced command/notification pair, if safely observable | PROJ-006, PROJ-007 | Candidate operation, repetition threshold, timing tolerance, authentication, and safe observability are unknown. |
| Negative/inconclusive evidence preserved without implementation | PROJ-004–PROJ-007, PROJ-018, PROJ-019 | Zero-operation v1 is explicitly valid. |
| FR-1: all implemented behavior links to evidence | PROJ-001, PROJ-008, PROJ-010, PROJ-024 | Applicable only after a positive evidence gate. |
| FR-2: observations separate from interpretations/fixtures | PROJ-001, PROJ-002, PROJ-008, PROJ-024 | “Proprietary captures” boundary needs definition in PROJ-002. |
| FR-3: deterministic codec and malformed rejection | PROJ-008, PROJ-010 | Codec does not exist and is forbidden on the zero-operation path. |
| FR-4: no more than one C# operation | PROJ-007, PROJ-009, PROJ-015, PROJ-024 | Exact API shape is unknown until evidence exists. |
| Public API cancellation and explicit error behavior | PROJ-014, PROJ-015, PROJ-023 | Exception/result design, timeout ownership, and cancellation semantics are unspecified. |
| FR-5: API path against macOS GATT test double | PROJ-011–PROJ-016 | CoreBluetooth fidelity and native-boundary choice remain unknown. |
| FR-6: default checks perform no physical BLE interaction | PROJ-003, PROJ-016, PROJ-018, PROJ-020, PROJ-024 | Physical-peripheral discovery isolation must be proven, not assumed. |
| FR-7: hardware checks opt-in and approval-gated | PROJ-003, PROJ-021, PROJ-024 | Ticket closes without adding a check if none is shipped. |
| FR-8: unsupported behavior fails clearly | PROJ-007, PROJ-010, PROJ-014, PROJ-015 | Exact unsupported cases depend on the evidenced format/boundary. |
| Generated fixture privacy and truthful labeling | PROJ-002, PROJ-008, PROJ-024 | No fixture may exist on the zero-operation path. |
| Minimal native macOS `CBPeripheralManager` test double | PROJ-011–PROJ-013 | It must not be called controller-level Bluetooth emulation. |
| Smallest viable .NET/native boundary | PROJ-012, PROJ-014 | In-process versus process boundary is an unresolved evidence gate. |
| Hardware-free automated check | PROJ-016 or PROJ-018, PROJ-020 | Supported macOS/.NET versions and local toolchain availability are not yet established. |
| Contributor setup, example, checks, and limitations | PROJ-017, PROJ-019–PROJ-023 | Example is positive-path only; no deployment/package task is required because distribution is a non-goal. |
| ADR 0001 accepted or superseded | PROJ-011, PROJ-012, PROJ-022 | Zero-operation resolution conflicts with unavailable positive-path native evidence and must be recorded honestly. |
| Quality, code review, documentation alignment, and PM acceptance | PROJ-020, PROJ-023–PROJ-025 | Hardware verification may remain unavailable; it cannot be reported as passed. |
| Safety and authorization | PROJ-002–PROJ-006, PROJ-021, PROJ-024, PROJ-025 | No ticket authorizes pairing or BLE transmission. Separate explicit approval is still required. |
| Non-goals and focused-v1 boundary | PROJ-007, PROJ-009, PROJ-024, PROJ-025 | Full protocol, inspector UI, cloud/database, multi-platform support, controller emulation, Rust/C++, package publication, and production claims are intentionally absent. |
| Success measures: traceability, reproducibility, zero unsupported claims | PROJ-020, PROJ-023–PROJ-025 | Validation follows the selected gate outcome. |

Every stated focused-v1 goal maps to at least one ticket. Open questions are represented as blocked research/evidence gates rather than fabricated implementation details.

## Recommended Execution Order

Work sequentially as a solo developer. Each item starts only after its dependencies and preceding required ticket PRs are human-approved and merged into `master`; `github` then creates the exact branch in the Branch and Merge Plan. Do not begin the next ticket on an unmerged predecessor branch.

1. PROJ-001 — evidence ledger and layout
2. PROJ-002 — sanitization/provenance rules
3. PROJ-003 — safe capture procedure
4. PROJ-004 — authorized advertisement observations
5. PROJ-005 — authorized GATT inventory
6. PROJ-006 — candidate experiment and reproduction/negative result
7. PROJ-007 — freeze the one-operation or zero-operation outcome
8. If one operation passes: PROJ-008 → PROJ-009 → PROJ-010 → PROJ-011 → PROJ-012 → PROJ-013 → PROJ-014 → PROJ-015 → PROJ-016 → PROJ-017
9. If zero operations pass: PROJ-018 → PROJ-019
10. PROJ-020 — shared default validation entry point
11. PROJ-021 — isolate any retained hardware check, or document that none ships
12. PROJ-022 — resolve ADR 0001
13. PROJ-023 — contributor documentation
14. PROJ-024 — final traceability/privacy/scope audit
15. PROJ-025 — code review and project-manager acceptance

Do not begin the conditional implementation path before PROJ-007, and do not create branches for the unselected path. Hardware-dependent work remains blocked until explicit approval for the actual action is granted. Any pre-authorized closely coupled exception is one branch and one PR; otherwise every ticket uses its own branch and merge gate.

## Definition of Complete

The focused v1 is complete only when all of the following are true:

- The evidence ledger, sanitized observations, interpretations, and any generated fixtures are separated, versioned, linked, and free of prohibited data.
- Approved discovery work produced either one safely reproduced operation or a reproducible negative/inconclusive result with open risks and a next falsifiable experiment.
- The project manager recorded one evidence-gate outcome and no artifact from the unselected path was introduced.
- On the one-operation path, exactly one public asynchronous C# operation is evidence-backed, deterministic, explicit about failures, and verified end to end against the macOS GATT peripheral test double without physical hardware.
- On the zero-operation path, no command fixture, codec, device-operation API, synthetic GATT shape, or supported-operation example exists, and the evidence-only validation check passes.
- The default validation command performs no physical-device BLE interaction. Any hardware check is separate, opt-in, side-effect-documented, and approval-gated; unavailable hardware checks are reported unavailable.
- Public usage or zero-operation status, errors, evidence links, setup, checks, and limitations match the artifacts. Test-double results are never presented as real-device results.
- ADR 0001 is accepted or superseded based on recorded evidence.
- All applicable PRD acceptance criteria pass; links and terminology are valid; focused-v1 scope remains distinct from `END_GOAL.md`.
- The code reviewer has no unresolved correctness, safety, protocol-evidence, or focused-test findings, and the project manager accepts the complete handoff.

Commit, push, and pull-request creation may follow the repository orchestration workflow after acceptance. Pull-request merge, release, package publication, and hardware interaction remain separate human-approved actions and are not part of focused-v1 completion.
