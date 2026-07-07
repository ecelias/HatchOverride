# Project charter

## Objective

Create an open, well-tested API for controlling a personally owned Hatch Restore 2, informed by the small shape of `m4rcus.HatchBaby.Rest` but not by assuming its protocol applies to a different device generation.

## Why this is technically interesting

The project joins reverse-engineering discipline, asynchronous BLE transport, deterministic protocol serialization, multi-agent evidence governance, and a browser-visible inspection surface. The impressive part is not agent count; it is whether the agents preserve provenance from captured bytes to API behavior.

## First deliverable

A protocol-discovery spike with:

- a sanitized service/characteristic inventory;
- a versioned evidence ledger;
- one reproduced command/notification pair, if safely observable;
- a minimal macOS GATT peripheral test-double decision;
- an architecture decision choosing the smallest viable implementation stack.

## Constraints

- Restore 2 behavior is unknown until measured.
- Work only with owned/authorized devices and accounts.
- Do not bypass authentication, encryption, firmware protections, or safety controls.
- No patient or production healthcare data belongs in this repository.
- No claim of a full macOS Bluetooth emulator until controller-level behavior is demonstrated. CoreBluetooth may be sufficient for a GATT peripheral test double.
- Working branches and pull requests may be published through the repository's orchestrated Git workflow. Pull-request merges, releases, and package publication require explicit human approval.

## Initial stack hypothesis

- Public API and protocol library: modern .NET/C#.
- macOS peripheral test double: the thinnest native CoreBluetooth component needed to advertise synthetic GATT services.
- Rust/C++: deferred until profiling, portability, or native integration creates a concrete requirement.
- Inspector UI: deferred until recorded protocol artifacts need human review.

## Success criteria

1. Every implemented command traces to sanitized evidence and a deterministic test fixture.
2. The API can run against a test double without physical hardware.
3. Hardware tests are opt-in, clearly labeled, and safe by default.
4. Documentation lets a new contributor reproduce the supported path.
5. Multi-agent handoffs leave an auditable record of decisions, evidence, and checks.
