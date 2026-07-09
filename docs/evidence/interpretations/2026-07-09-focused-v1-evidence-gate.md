# Focused v1 evidence-gate decision — 2026-07-09

- **Decision owner:** `project_manager`
- **Ticket:** PROJ-007 — Decide and freeze the focused-v1 evidence-gate outcome
- **Decision:** Focused v1 follows the **zero-operation path**.
- **Decision status:** Accepted for focused v1 planning.
- **Hardware interaction required for this decision:** None.
- **Test-double evidence used:** None. No CoreBluetooth test-double behavior is treated as hardware evidence.

## Decision summary

The repository has reproduced evidence for advertisement shape, GATT inventory, and one safe Battery Level read. It does not have reproduced evidence for a Restore 2 vendor command, command response, notification pair, request framing, write behavior, or all bytes and fields needed for deterministic protocol behavior.

Therefore focused v1 must not create a command fixture, codec, device-operation API, synthetic GATT shape, GATT peripheral test double for a selected operation, or supported-operation example.

## Evidence assessed

| Evidence area | Ledger / source | Gate assessment |
|---|---|---|
| Discovery-mode advertisement candidate | [`R2-EVID-001`](../ledger.md#r2-evid-001--does-an-authorized-restore-2-advertise-ble-services-under-reproducible-conditions), [`2026-07-08-discovery-mode-advertisement-scan.md`](../observations/2026-07-08-discovery-mode-advertisement-scan.md) | Useful for target discovery under recorded conditions. Attribution remains inferred and does not establish commands. |
| GATT services, characteristics, properties, descriptors | [`R2-EVID-002`](../ledger.md#r2-evid-002--which-services-characteristics-properties-and-descriptors-are-observable), [`2026-07-08-gatt-inventory.md`](../observations/2026-07-08-gatt-inventory.md) | Reproduced inventory exists. UUIDs/properties are observed facts only and do not establish value formats, command direction, notification payloads, writes, or implementation eligibility. |
| Auth/encryption/sequencing/timing constraints | [`R2-EVID-003`](../ledger.md#r2-evid-003--what-authentication-encryption-sequencing-timing-or-firmware-constraints-exist) | Still `unknown` beyond the exact discovery and Battery Level read paths. No evidence supports vendor command sequencing or notification behavior. |
| One operation and response | [`R2-EVID-004`](../ledger.md#r2-evid-004--can-one-operation-and-its-response-be-observed-safely-and-reproduced), [`2026-07-08-battery-level-read.md`](../observations/2026-07-08-battery-level-read.md) | Reproduced Battery Level read exists. It is not a Restore 2 vendor command/notification pair and does not justify a public Restore control operation. |
| Synthetic GATT shape for API boundary | [`R2-EVID-005`](../ledger.md#r2-evid-005--can-corebluetooth-advertise-the-required-synthetic-gatt-shape-accurately-enough-for-the-v1-api-boundary) | Remains `unknown`; no selected operation exists, so no required synthetic GATT shape is defined. |
| Native bridge/process boundary | [`R2-EVID-006`](../ledger.md#r2-evid-006--is-an-in-process-native-bridge-smaller-and-more-reliable-than-a-process-boundary) | Remains `unknown`; no implementation boundary is needed on the zero-operation path before the evidence-only validation work. |

## Eligibility assessment

| PROJ-007 criterion | Assessment |
|---|---|
| Observed and reproduced evidence | Advertisement, inventory, and Battery Level read evidence exist. Only the Battery Level read is a reproduced operation response. |
| Sanitization | Admitted artifacts record provenance and keep raw output outside the repository. No private identifiers, raw captures, fixtures, or proprietary payload dumps are committed. |
| Documented conditions | Conditions are recorded, including discovery mode, host/tool hashes, timing, repetition, unavailable firmware/app versions, and limitations around overlapping runs. |
| Byte/field completeness | Complete only for the one-byte `180F/2A19` Battery Level read response. Incomplete for any Restore 2 vendor command, notification, write, or selected operation fixture. |
| Safety constraints | No writes, notification subscriptions, pairing, authentication bypass, firmware modification, or safety-control bypass are evidenced or authorized for implementation. |
| Fixture feasibility | A deterministic fixture could be made for the Battery Level read, but that would not satisfy the focused-v1 Restore control-operation intent. No command fixture is allowed on the selected zero-operation path. |
| Remaining unknowns | Vendor command semantics, request framing, response/notification fields, write safety, notification behavior, auth/encryption beyond the exact read path, firmware constraints, synthetic GATT shape, and native boundary remain unknown. |

## Frozen focused-v1 path

Focused v1 is now frozen to the zero-operation path until a later ticket or future scope explicitly reopens evidence discovery.

Activated conditional tickets:

- PROJ-018 — zero-operation validation check.
- PROJ-019 — zero-operation handoff documentation.
- PROJ-020 and later common tickets remain sequenced after the zero-operation path prerequisites described in `JIRA.md`.

Not applicable for this focused-v1 gate:

- PROJ-008 — generated fixture.
- PROJ-009 — .NET solution for a selected operation.
- PROJ-010 — operation codec.
- PROJ-011 — CoreBluetooth synthetic GATT shape spike for a selected operation.
- PROJ-012 — native boundary for selected operation.
- PROJ-013 — GATT peripheral test double for selected operation.
- PROJ-014 — transport seam for selected operation.
- PROJ-015 — public operation API.
- PROJ-016 — one-operation hardware-free check.
- PROJ-017 — supported-operation example.

## Prohibited by this decision

Do not introduce any of the following for focused v1:

- command fixture;
- protocol codec;
- public device-operation API;
- synthetic GATT shape for a selected operation;
- GATT peripheral test double for a selected operation;
- supported-operation example;
- claim that the Battery Level read proves Restore 2 control semantics.

## Next falsifiable experiment

Future discovery, outside this frozen focused-v1 path, should choose exactly one vendor-operation question and obtain explicit approval for the exact transmitted action. The next useful experiment would be a bounded notification or vendor-characteristic experiment that predeclares target characteristic, side effects, abort criteria, cleanup, expected direction, timing, and sanitization before any subscription or write.

## Project-manager acceptance

The project manager accepts the zero-operation decision for PROJ-007 because the evidence is sufficient to show that approved discovery work was completed, but insufficient to justify a deterministic Restore 2 command fixture, codec, public API operation, or test-double shape without speculation.
