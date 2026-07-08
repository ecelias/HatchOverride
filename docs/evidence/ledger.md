# Restore 2 evidence ledger

The [evidence directory](README.md) defines the artifact boundaries and allowed status and maturity vocabulary. The seed records below preserve every [open evidence question](../PRD_FOCUSED_V1.md#open-questions-and-evidence-gates) as `unknown` without asserting protocol facts.

## Record template

Copy this template for a new claim. Maturity is optional and, when applicable, must be one of `reproduced`, `fixture-backed`, `supported`, or `hardware-validated`.

```markdown
### R2-EVID-NNN — Question or claim

- **Status:** observed | inferred | disproved | unknown
- **Maturity (optional):** reproduced | fixture-backed | supported | hardware-validated
- **Interpretation:**
- **Confidence:**
- **Confirming or falsifying experiment:**
- **Sanitized source reference:**
- **Capture method:**
- **Timestamp:**
- **Conditions:**
- **Result:**
- **Direction:**
- **Timing:**
- **Repetition:**
- **Errors:**
- **Device model:**
- **Firmware version:**
- **App version:**
- **Derived fixtures:** none | repository-relative links
- **Supported code:** none | repository-relative links
```

For `observed` and `disproved` records, every capture field is required; use an explicit `not applicable` only when the field does not apply. For other statuses, omit capture fields that have no evidence rather than implying an observation. Record unavailable device or version data explicitly.

## Open questions

### R2-EVID-001 — Does an authorized Restore 2 advertise BLE services under reproducible conditions?

- **Status:** `inferred`
- **Interpretation:** A discovery-mode Stage 1 experiment observed the same sanitized `Restore`-labeled candidate signature in all three runs. Attribution to the owned Restore 2 is inferred from the owner-confirmed discovery-mode timing and redacted local-name token; it was not independently established. An earlier experiment without recorded device conditions was inconclusive.
- **Confidence:** Moderate. The repeated candidate observation is direct; target attribution lacks a matched discovery-mode-off comparison.
- **Confirming or falsifying experiment:** After separate approval, compare matched Stage 1 scans with discovery mode deliberately off and on, using the same privacy-safe signature and predeclared classification rule.
- **Sanitized source reference:** [`observations/2026-07-08-discovery-mode-advertisement-scan.md`](observations/2026-07-08-discovery-mode-advertisement-scan.md); earlier inconclusive [`observations/2026-07-08-advertisement-scan.md`](observations/2026-07-08-advertisement-scan.md)
- **Capture method:** Temporary native macOS CoreBluetooth scanner; source and binary hashes are recorded in the source reference.
- **Timestamp:** 2026-07-08 15:54:24Z–15:59:08Z discovery-mode advertisement windows.
- **Conditions:** Owner-confirmed discovery mode before run 1; persistence through later runs unknown. Bluetooth `powered_on`; three planned 60-second scans with approximately 60-second spacing. Exact scan-start spacing is unavailable.
- **Result:** Positive candidate observation under the predeclared repetition rule; attribution to the Restore 2 remains inferred.
- **Direction:** Nearby peripheral advertisements to scanner; controller scan-request transmission may also have occurred.
- **Timing:** Per-run advertisement windows and raw-output hashes are recorded in the discovery-mode source reference.
- **Repetition:** Three completed scan processes.
- **Errors:** Empty process error logs; lack of a matched discovery-mode-off comparison limits attribution.
- **Device model:** Hatch Restore 2 (owner-confirmed); no private identifier recorded.
- **Firmware version:** Unavailable.
- **App version:** Unavailable; the app was not used by the capture tool.
- **Derived fixtures:** none
- **Supported code:** none

### R2-EVID-002 — Which services, characteristics, properties, and descriptors are observable?

- **Status:** `observed`
- **Maturity:** `reproduced`
- **Interpretation:** A discovery-mode Stage 2 experiment observed the same sanitized GATT service, characteristic, property, and descriptor inventory in three completed runs. Attribution to the owned Restore 2 remains inferred from the owner-confirmed discovery-mode timing and prior sanitized advertisement signature; it was not independently established by a retained private identifier. The observation does not establish command semantics, readable values, notification payloads, write behavior, authentication requirements, or implementation eligibility.
- **Confidence:** Moderate. The normalized inventory reproduced across three completed runs; target attribution remains inferred and runs 2 and 3 overlapped in wall-clock time.
- **Confirming or falsifying experiment:** After separate approval, repeat the inventory with discovery mode deliberately off and on, or use a privacy-preserving pairing between the advertisement candidate and GATT target that does not admit a private identifier.
- **Sanitized source reference:** [`observations/2026-07-08-gatt-inventory.md`](observations/2026-07-08-gatt-inventory.md)
- **Capture method:** Temporary native macOS CoreBluetooth central; source and binary hashes are recorded in the source reference.
- **Timestamp:** 2026-07-08 20:44:47Z–20:45:14Z inventory run set.
- **Conditions:** Owner-confirmed discovery mode before the run set. Bluetooth `powered_on`. The tool matched the PROJ-004 sanitized candidate signature, required one matching candidate, connected, discovered services, characteristics, and descriptors, then disconnected. Runs 2 and 3 overlapped and are not spaced environmental trials.
- **Result:** Reproduced sanitized inventory: primary services `180F`, `180A`, and `02340000-5EFD-47EB-9C1A-DE53F7A2B232`; ten characteristics with observed properties and three `2902` descriptors as listed in the source reference.
- **Direction:** Host central scan, connection initiation, GATT service discovery, characteristic discovery, descriptor discovery, and disconnect; peripheral discovery responses to host.
- **Timing:** Run 1 completed in about 4 seconds; runs 2 and 3 completed in about 3 seconds each. Exact per-event timestamps are recorded in the source reference.
- **Repetition:** Three completed inventory processes reported the same normalized inventory.
- **Errors:** No connect failure, discovery failure, authentication prompt, encryption prompt, or unexpected disconnect recorded.
- **Device model:** Hatch Restore 2 (owner-confirmed); no private identifier recorded.
- **Firmware version:** Unavailable.
- **App version:** Unavailable; the app was not used by the capture tool.
- **Derived fixtures:** none
- **Supported code:** none

### R2-EVID-003 — What authentication, encryption, sequencing, timing, or firmware constraints exist?

- **Status:** `unknown`
- **Interpretation:** The Stage 2 inventory recorded no authentication prompt, encryption prompt, or discovery failure during connection plus GATT discovery only. The Stage 4 Battery Level read recorded no authentication prompt, encryption prompt, pairing prompt, or read failure for `180F/2A19` under the recorded discovery-mode conditions. These facts do not answer requirements for other reads, notification subscriptions, writes, sequencing, command timing, firmware-specific behavior, or non-discovery conditions.
- **Confidence:** Low for constraints beyond the exact observed discovery and Battery Level read paths. The observed constraint fact is absence of prompts or errors during those approved procedures only.
- **Confirming or falsifying experiment:** Define and obtain approval for one safe candidate-operation experiment that isolates a single read, subscription, or write behavior and records prompts, failures, sequencing, timing, and firmware/app context.
- **Sanitized source reference:** [`observations/2026-07-08-gatt-inventory.md`](observations/2026-07-08-gatt-inventory.md); [`observations/2026-07-08-battery-level-read.md`](observations/2026-07-08-battery-level-read.md)
- **Device model:** Hatch Restore 2 (owner-confirmed); no private identifier recorded.
- **Firmware version:** Unavailable.
- **App version:** Unavailable; the app was not used by the capture tool.
- **Derived fixtures:** none
- **Supported code:** none

### R2-EVID-004 — Can one operation and its response be observed safely and reproduced?

- **Status:** `observed`
- **Maturity:** `reproduced`
- **Interpretation:** A discovery-mode Stage 4 experiment reproduced one safe read operation: service `180F`, characteristic `2A19`, returned value length `1` and unsigned one-byte value `0` in three completed attempts. This is evidence for a bounded Battery Level read only. It does not establish Restore 2 vendor command semantics, command/notification pairing, notification behavior, write behavior, implementation eligibility, or a public API operation.
- **Confidence:** Moderate for this exact read under the recorded conditions. The response reproduced three times, but the runs overlapped in wall-clock time, target attribution remains inferred from earlier evidence, and firmware/app versions are unavailable.
- **Confirming or falsifying experiment:** For this exact read, repeat under spaced conditions or with discovery mode deliberately off and on. For the PRD command/notification question, define a separate subscription or vendor-operation experiment only after explicit approval for the exact transmitted action and abort criteria.
- **Sanitized source reference:** [`observations/2026-07-08-battery-level-read.md`](observations/2026-07-08-battery-level-read.md)
- **Capture method:** Temporary native macOS CoreBluetooth central; source and binary hashes are recorded in the source reference.
- **Timestamp:** 2026-07-08 21:07:32Z–21:07:36Z read run set.
- **Conditions:** Owner-confirmed discovery mode before execution. Bluetooth `powered_on`. The tool matched the PROJ-004 sanitized candidate signature, required one matching candidate, connected, discovered service `180F` and characteristic `2A19`, issued one read request per attempt, then disconnected. Runs overlapped and are not spaced environmental trials.
- **Result:** Reproduced read response: `180F/2A19` returned value length `1` and unsigned one-byte value `0` in all three attempts.
- **Direction:** Host central scan, connection initiation, GATT service discovery, characteristic discovery, one read request to `180F/2A19`, read response from peripheral, and disconnect.
- **Timing:** Three attempts completed within about 3–4 seconds each; exact per-event timestamps are recorded in the source reference.
- **Repetition:** Three completed read processes returned the same sanitized value.
- **Errors:** No connect failure, discovery failure, read failure, authentication prompt, encryption prompt, pairing prompt, or unexpected disconnect recorded.
- **Device model:** Hatch Restore 2 (owner-confirmed); no private identifier recorded.
- **Firmware version:** Unavailable.
- **App version:** Unavailable; the app was not used by the capture tool.
- **Derived fixtures:** none
- **Supported code:** none

### R2-EVID-005 — Can CoreBluetooth advertise the required synthetic GATT shape accurately enough for the v1 API boundary?

- **Status:** `unknown`
- **Interpretation:** No required GATT shape or CoreBluetooth reproduction evidence is established.
- **Confidence:** No conclusion.
- **Confirming or falsifying experiment:** After an evidence-backed GATT shape exists, run a bounded CoreBluetooth peripheral test and record its observable limitations.
- **Device model:** Not applicable; this question concerns a future synthetic test boundary.
- **Firmware version:** Not applicable; this question concerns a future synthetic test boundary.
- **App version:** Not recorded; no test observation exists.
- **Derived fixtures:** none
- **Supported code:** none

### R2-EVID-006 — Is an in-process native bridge smaller and more reliable than a process boundary?

- **Status:** `unknown`
- **Interpretation:** Current repository evidence does not compare the boundaries.
- **Confidence:** No conclusion.
- **Confirming or falsifying experiment:** Compare the smallest runnable boundary spikes against documented reliability and complexity criteria.
- **Device model:** Not applicable; this question concerns software architecture.
- **Firmware version:** Not applicable; this question concerns software architecture.
- **App version:** Not applicable; this question concerns software architecture.
- **Derived fixtures:** none
- **Supported code:** none
