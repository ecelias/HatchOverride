# Restore 2 discovery-mode GATT inventory — 2026-07-08

- **Ledger claim:** [`R2-EVID-002`](../ledger.md#r2-evid-002--which-services-characteristics-properties-and-descriptors-are-observable)
- **Outcome:** Reproduced sanitized GATT inventory for the discovery-mode candidate. Attribution to the owned Restore 2 remains inferred from the preceding advertisement evidence and owner-confirmed discovery-mode timing; no private identifier was retained.
- **Authorization:** The human owner confirmed the device was in discovery mode and approved connection, pairing, GATT discovery, read, notification subscription, and write actions as needed for project requirements. This ticket used only connection plus service, characteristic, and descriptor discovery. No pairing prompt appeared, and no characteristic value read, write, or notification subscription was attempted.
- **Device model:** Hatch Restore 2 (owner-confirmed); no private identifier recorded.
- **Firmware version:** Unavailable.
- **App version:** Unavailable; the app was not used by the capture tool.
- **Host and tool:** arm64 macOS 26.5.1 host. Temporary native CoreBluetooth command-line central built with Apple clang 17.0.0. Source SHA-256 `c4859790f74b884c9346533d286c6ff5ff79881a7a48f96d4e003363d7ccd439`; binary SHA-256 `848d7c59dfe1eacd34a30779b73b25fb56c22256de39d458eb3f605d0816423b`.
- **Tool behavior:** The tool requested an unfiltered scan, matched the PROJ-004 sanitized candidate signature, required exactly one matching candidate during a two-second confirmation window, connected to that candidate, discovered all services, discovered all characteristics for each service, discovered descriptors for each characteristic, disconnected, and exited. Forbidden-call review found no value read, write, notification subscription, pairing, or connected-peripheral retrieval call in the tool source.
- **Conditions:** Owner-confirmed discovery mode before the run set. Bluetooth reported `powered_on`. Runs were launched from the same host in the same session. Runs 2 and 3 overlapped in wall-clock time, so the repetition supports inventory stability but should not be treated as spaced independent environmental trials.
- **Predeclared result rule:** Reproducible inventory if at least two completed runs reported the same normalized service, characteristic, property, and descriptor set; inconclusive for connection/discovery errors, ambiguous candidates, or inconsistent inventories.
- **Direction:** Host central scanned, initiated a connection, requested service discovery, requested characteristic discovery, requested descriptor discovery, and disconnected. The candidate peripheral returned discovery metadata. macOS or the controller may also have transmitted scan requests and connection-management traffic.
- **Timing and repetition:** Three processes completed with `inventory_complete`: run 1 from 2026-07-08 20:44:47Z to 20:44:51Z, run 2 from 20:45:11Z to 20:45:14Z, and run 3 from 20:45:11Z to 20:45:14Z.
- **Errors:** CoreBluetooth reported `powered_on`; no connect failure, discovery failure, authentication prompt, encryption prompt, or unexpected disconnect was recorded.
- **Original output:** Retained outside the repository under `/private/tmp/hatchoverride-proj005` for this local handoff only; it must not be committed. Raw JSONL SHA-256 values: run 1 `76670db3a8ff6d4dd7a266a2cd7f50bdd145c48291eb8e27c98e9438d361b8d9`, run 2 `f382d0ec5ffd3ee58669f12eae766c675497c32699b36a8f0176969e64839f5d`, run 3 `7676249836f8ec812b384a89b0a0a703f8e40c8760a1e82e61a49fb770bbb432`.

## Observed inventory

The following UUIDs, primary flags, characteristic properties, and descriptor UUIDs are admitted as observed facts only. They do not establish command semantics, value formats, authentication requirements, firmware behavior, or implementation eligibility.

| Service UUID | Primary | Characteristic UUID | Observed properties | Observed descriptors |
|---|---:|---|---|---|
| `180F` | yes | `2A19` | `read`, `notify` | `2902` |
| `180A` | yes | `2A24` | `read` | none observed |
| `180A` | yes | `2A25` | `read` | none observed |
| `180A` | yes | `2A26` | `read` | none observed |
| `180A` | yes | `2A27` | `read` | none observed |
| `180A` | yes | `2A29` | `read` | none observed |
| `02340000-5EFD-47EB-9C1A-DE53F7A2B232` | yes | `02340001-5EFD-47EB-9C1A-DE53F7A2B232` | `write_without_response`, `write` | none observed |
| `02340000-5EFD-47EB-9C1A-DE53F7A2B232` | yes | `02340002-5EFD-47EB-9C1A-DE53F7A2B232` | `notify` | `2902` |
| `02340000-5EFD-47EB-9C1A-DE53F7A2B232` | yes | `02340003-5EFD-47EB-9C1A-DE53F7A2B232` | `write_without_response`, `write` | none observed |
| `02340000-5EFD-47EB-9C1A-DE53F7A2B232` | yes | `02340004-5EFD-47EB-9C1A-DE53F7A2B232` | `notify` | `2902` |

## Interpretation boundaries

- The services `180A` and `180F`, characteristics `2A19`, `2A24`, `2A25`, `2A26`, `2A27`, `2A29`, and descriptor `2902` are Bluetooth SIG-assigned UUIDs, but this observation did not read their values.
- The `02340000-5EFD-47EB-9C1A-DE53F7A2B232` service family is observed as a UUID shape only. Its vendor, purpose, command direction, payload format, authentication behavior, and sequencing remain unknown.
- The presence of `read`, `write`, `write_without_response`, or `notify` properties records advertised GATT properties only. It is not evidence that reads, writes, or notifications are safe, authenticated, accepted, meaningful, or sufficient for any supported API operation.
- No pairing or encryption prompt appeared during this discovery-only procedure. That does not disprove authentication or encryption requirements for value reads, notification subscriptions, writes, or later command experiments.

## Stage handoff

- **Stage:** Stage 2 — connection and GATT discovery inventory.
- **Completed:** Yes; service, characteristic, and descriptor discovery completed in three runs.
- **Expected side effects:** Scan requests, connection-management traffic, and GATT discovery requests may have been transmitted. No value read, notification subscription, or write was attempted.
- **Abort or cleanup:** No abort trigger was reached. Each process stopped scanning, disconnected if connected, and exited.
- **Admission decision:** Admit this minimum transformed summary only. Peripheral identifiers, exact local name suffixes, advertisement payload values, RSSI/signal values, and raw event streams remain outside the repository.

## Evidence admission review

- **Artifacts reviewed:** This sanitized GATT inventory summary.
- **Ledger claims:** `R2-EVID-002`; related limitation note for `R2-EVID-003`.
- **Source authorization recorded:** Yes; owned device and action approval are recorded above without an identifier.
- **Manual review:** Pass — project manager, 2026-07-08.
- **Transformation method:** Reduced raw JSONL to event timing, tool provenance, normalized UUID/property/descriptor facts, and error status; removed private peripheral identifiers by tool design and omitted raw event streams.
- **Heuristic repository search:** Pass — the command from [`ADMISSION.md`](../ADMISSION.md) returned policy/context terms only; no prohibited value was found.
- **Synthetic fixture labeling/linkage:** Not applicable; no fixture exists.
- **Decision:** Admitted.
