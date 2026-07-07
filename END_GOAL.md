# End goal

## North star

Create a safe, documented, testable ecosystem for controlling a personally owned Hatch Restore 2, with every supported behavior traceable from sanitized observation through deterministic fixtures to public API behavior.

The current delivery contract is the [focused v1 PRD](docs/PRD_FOCUSED_V1.md). This file describes the longer-term product vision, not a committed backlog or permission to bypass evidence gates.

## Intended experience

### API consumers

Developers can discover a device, inspect its supported capabilities, control evidenced features, observe state changes, handle failures explicitly, and test their integrations without routine physical-hardware access.

### Contributors

Contributors can reproduce protocol observations, understand confidence and provenance, add support through a documented evidence-to-implementation workflow, and run focused checks before requesting review.

### Protocol investigators

Investigators can compare sanitized captures, fixtures, firmware contexts, timing, and competing hypotheses without confusing inference or generated data with observed device behavior.

## Full product capabilities

Capabilities may enter the product only when evidence and user need justify them:

- A mature C# API for evidenced Restore 2 lighting, sound, routine, alarm, control, and state behaviors.
- A coherent notification and state model with explicit synchronization and failure semantics.
- Reliable BLE discovery, connection lifecycle, cancellation, retry, timeout, and diagnostics.
- Version-aware protocol behavior when firmware differences are observed.
- Deterministic codecs and sanitized fixtures for every supported behavior.
- Hardware-free test doubles that cover documented API and GATT boundaries without overstating controller fidelity.
- Opt-in authorized hardware validation with reproducible evidence records.
- An inspection surface for reviewing recorded artifacts, decoded messages, evidence links, and validation results.
- Packaging and examples that make supported capabilities straightforward to consume.
- Additional platform support only where demand and measured platform constraints justify it.

## Quality attributes

- **Provenance:** every supported behavior traces to reproducible, sanitized evidence.
- **Safety:** physical-device actions are explicit, authorized, bounded, and separated from default checks.
- **Determinism:** serialization, fixtures, and test outcomes are stable and reviewable.
- **Clarity:** unsupported operations and uncertainty fail visibly rather than guess.
- **Observability:** failures expose enough context to distinguish transport, protocol, device, and test-double problems.
- **Maintainability:** standard-library and native-platform capabilities precede dependencies and custom abstractions.
- **Portability:** new languages or platforms follow measured requirements, not aspiration.
- **Privacy:** fixtures and documentation contain no credentials, private identifiers, proprietary captures, or unrelated personal data.

## Evidence maturity model

Claims carry one status: `unknown`, `inferred`, `observed`, or `disproved`. An inference records confidence, competing explanations, and a falsifying experiment; it is not a prerequisite for observation.

Observed behavior may then advance through these maturity stages:

1. **Reproduced:** the observation repeats under documented conditions.
2. **Fixture-backed:** a clearly labeled generated fixture represents the reproduced behavior deterministically.
3. **Supported:** code, tests, usage documentation, limitations, and evidence links agree.
4. **Hardware-validated:** an opt-in authorized check confirms applicable behavior on documented device and firmware conditions.

Promotion between maturity stages requires evidence. A test double cannot promote a claim about real hardware.

## Possible future surfaces

- A local browser-based protocol and fixture inspector.
- Diagnostic capture and comparison tools with automatic sanitization checks.
- Published .NET packages and versioned compatibility documentation.
- Broader desktop, mobile, or home-automation integration.
- Higher-fidelity peripheral simulation when CoreBluetooth limitations are measured.
- Rust or C++ components when portability, performance, controller access, or FFI measurements justify them.

These are options, not promises. They remain outside focused v1 until separately scoped and approved.

## Permanent boundaries

- Do not claim protocol facts from another Hatch model or from generated fixtures.
- Do not bypass authentication, encryption, firmware protection, account controls, or safety mechanisms.
- Do not describe a GATT peripheral test double as controller-level Bluetooth emulation without evidence.
- Do not make hardware interaction, Git publication, releases, or package publication implicit.
- Do not add platforms, dependencies, services, or abstraction layers without a demonstrated need.
- Do not store credentials, private identifiers, patient data, proprietary captures, or unrelated personal data.

## Product completion

The product vision is realized when the useful, safely observable Restore 2 capabilities selected for support are:

- documented with explicit compatibility and limitations;
- traceable to sanitized, reproducible evidence;
- represented by deterministic fixtures;
- exposed through a stable, understandable API;
- covered by hardware-free automated checks and appropriate opt-in hardware validation;
- diagnosable by contributors without requiring unsupported assumptions;
- maintainable under the repository's evidence, review, and approval gates.

“Complete” does not require guessing unknown behavior or implementing every possible feature. It requires that every claimed capability is true, reproducible, and usable.
