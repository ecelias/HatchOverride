# Restore 2 Stage 1 discovery-mode advertisement observation — 2026-07-08

- **Ledger claim:** [`R2-EVID-001`](../ledger.md#r2-evid-001--does-an-authorized-restore-2-advertise-ble-services-under-reproducible-conditions)
- **Outcome:** Positive candidate observation under the predeclared repetition rule. Target attribution remains inferred rather than directly established.
- **Authorization:** The human owner approved a second Stage 1 advertisement scan on 2026-07-08 after placing the owned Restore 2 into discovery mode. Possible controller scan-request transmission was acknowledged. No connection or GATT action was authorized or attempted.
- **Device model:** Hatch Restore 2 (owner-confirmed); no private identifier recorded.
- **Firmware version:** Unavailable.
- **App version:** Unavailable.
- **Host and tool:** The same arm64 macOS 26.5.1 host and temporary native CoreBluetooth scanner recorded in the [first observation](2026-07-08-advertisement-scan.md).
- **Conditions:** The owner confirmed discovery mode before run 1. Whether discovery mode persisted through runs 2 and 3 was not observed and remains unknown. Bluetooth reported `powered_on`. Three independent 60-second scans were planned with approximately 60-second spacing; exact scan-start spacing is unavailable.
- **Predeclared result rule:** Positive only if the same sanitized candidate signature appeared in at least two independent runs; negative if no candidate appeared in all completed runs, without proving non-support; inconclusive for errors, incomplete runs, ambiguous attribution, or inconsistent observations.
- **Direction:** Nearby peripheral advertisements to scanner; macOS or the controller may also have transmitted scan requests.
- **Timing and repetition:** Three scan processes completed with one `scan_start` and one `scan_end` event each. Advertisement windows were 2026-07-08 15:54:24Z–15:55:26Z, 15:56:14Z–15:57:16Z, and 15:58:05Z–15:59:08Z.
- **Sanitized candidate signature:** The local-name field contained `Restore`; the remaining name was removed. The candidate reported connectable `true`, service UUID `180A`, a service-data field keyed by `180F` with a one-byte value, and a 10-byte manufacturer-data field. Service-data and manufacturer-data values were removed rather than admitted. The same full candidate signature appeared in all three runs. A second form without manufacturer data appeared only in run 1 and did not meet the threshold.
- **Errors:** CoreBluetooth reported `powered_on`; all runs emitted normal start/end records; error logs were empty.
- **Result:** Positive under the predeclared candidate threshold. Attribution to the owned Restore 2 is inferred from the owner-confirmed discovery-mode timing and the redacted `Restore` local-name token; it was not independently established. This observation does not establish GATT availability, characteristic behavior, commands, payload meaning, or implementation eligibility.
- **Next falsifiable experiment:** After separate approval, compare otherwise matched Stage 1 scans with discovery mode deliberately off and on. Predeclare conditions and confirm whether the sanitized candidate appears only in the on condition without retaining a private identifier.
- **Original output:** Retained outside the repository under `/private/tmp/hatchoverride-proj004-discovery-20260708` for this local handoff only; it must not be committed. Final raw SHA-256 values: run 1 `3c73c835a298b9586adc820bbc5eb274e3a454ca9f1dd7412df5cc5391adc0cd`, run 2 `90495a833e6bf5729960dbb6abcf08afd35312c61b4828e5e623b864e089bcd5`, run 3 `5dd2eeb43b8a4368c28d545f64020be9aad67644f0951b20e87c0d85e9ebdcb0`.

## Stage handoff

- **Stage:** Stage 1 — passive advertisement observation.
- **Completed:** Yes; later stages were not attempted.
- **Expected side effects:** Scan requests could be transmitted; unrelated nearby advertisements could be received.
- **Abort or cleanup:** No abort trigger or cleanup action was required. Each process stopped its scan before exit.
- **Admission decision:** Admit this minimum transformed summary only. Exact local name, peripheral identifiers, payload values, signal values, nearby-device names, and unrelated advertisement fields remain outside the repository.

## Evidence admission review

- **Artifacts reviewed:** This sanitized observation summary.
- **Ledger claims:** `R2-EVID-001`.
- **Source authorization recorded:** Yes; owned device and Stage 1 approval are recorded above without an identifier.
- **Manual review:** Pass — project manager, 2026-07-08.
- **Transformation method:** Reduced raw output to run completion and the repeated candidate shape; removed the exact local name, peripheral identifiers, payload values, signal values, nearby-device names, and unrelated fields.
- **Heuristic repository search:** Pass — the command from [`ADMISSION.md`](../ADMISSION.md) returned policy/context terms only; no prohibited value was found.
- **Synthetic fixture labeling/linkage:** Not applicable; no fixture exists.
- **Decision:** Admitted.

