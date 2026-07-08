# Restore 2 Stage 1 advertisement observation — 2026-07-08

- **Ledger claim:** [`R2-EVID-001`](../ledger.md#r2-evid-001--does-an-authorized-restore-2-advertise-ble-services-under-reproducible-conditions)
- **Outcome:** Inconclusive. Three scans completed, but no advertisement could be attributed to the authorized Restore 2 without retaining a private peripheral identifier or guessing from unrelated nearby-device traffic.
- **Authorization:** The human owner approved Stage 1 advertisement scanning on 2026-07-08 and acknowledged possible controller scan-request transmission. The project manager approved the same bounded stage. No later stage was authorized or attempted for this ticket.
- **Device model:** Hatch Restore 2 (owner-confirmed); no private identifier recorded.
- **Firmware version:** Unavailable.
- **App version:** Unavailable; the app was not used by the capture tool.
- **Host:** arm64 Mac, macOS 26.5.1 (build 25F80); private host identifiers omitted.
- **Capture method:** Temporary native CoreBluetooth command-line scanner built with Apple clang 17.0.0. Source SHA-256 `2d1ef0007d452de65e9002407230fee21fac51b4d4779975ae63fbf992f5c296`; binary SHA-256 `6bcab2804ea79c9a7aa8b3b8971b61fc50c25516211e8b97442ae9183c366bc5`. The tool requested an unfiltered scan with duplicate advertisements enabled and contained no connection or GATT operation.
- **Conditions:** Bluetooth reported `powered_on`. Three independent 60-second scans were planned with approximately 60-second spacing. Scan-start events lacked timestamps, so exact spacing is unavailable. Device power state, proximity, app state, and nearby-radio conditions were not recorded, which prevents a negative conclusion.
- **Predeclared result rule:** Positive only if the same sanitized candidate signature appeared in at least two independent runs; negative if no candidate appeared in all completed runs, without proving non-support; inconclusive for errors, incomplete runs, ambiguous attribution, or inconsistent observations.
- **Direction:** Nearby peripherals to scanner advertisements; macOS or the controller may also have transmitted scan requests.
- **Timing and repetition:** Three scan processes completed with one `scan_start` and one `scan_end` event each. Advertisement windows were 2026-07-08 15:37:06Z–15:38:09Z, 15:39:46Z–15:40:49Z, and 15:41:47Z–15:42:49Z.
- **Sanitized advertisement fields:** No target-attributable local name, service UUID, manufacturer data, service data, connectability value, or signal value was admitted. A case-insensitive search for `Hatch` or `Restore` in local-name fields found zero candidates across all runs. Unrelated advertisements and private peripheral identifiers were discarded from this artifact.
- **Errors:** CoreBluetooth reported `powered_on`; all runs emitted normal start/end records; error logs were empty. Ambiguous attribution is the limiting condition.
- **Result:** Inconclusive. The positive threshold was not met. The result is not labeled negative because the target conditions and a privacy-safe attribution method were not established before execution.
- **Next falsifiable experiment:** After separate approval, repeat Stage 1 with the Restore 2 power state, app state, fixed proximity, nearby-radio conditions, and a privacy-safe out-of-band attribution method recorded before scanning. Predeclare the same run count, timing, and classification rule.
- **Original output:** Retained outside the repository under `/private/tmp/hatchoverride-proj004-20260708` for this local handoff only; it must not be committed. Final raw SHA-256 values: run 1 `b7b292e4c8dbb753683da021fb971b10b98b9f085407d647d2882fa74d119ea7`, run 2 `b890468fe4fe09bf08fdde1c9da061540d94d144f1ad4b29d4c550ede28907c6`, run 3 `045efcdcc98b10be21e8cc8c57940a6255b8fa57b0dcb1ccc85a51b79ad88083`.

## Stage handoff

- **Stage:** Stage 1 — passive advertisement observation
- **Completed:** Yes; later stages were not attempted.
- **Expected side effects:** Scan requests could be transmitted; unrelated nearby advertisements could be received.
- **Abort or cleanup:** No abort trigger or cleanup action was required. Each process stopped its scan before exit.
- **Admission decision:** Admit this minimum transformed summary only. Raw output, peripheral identifiers, nearby-device names, and unrelated advertisement fields remain outside the repository.

## Evidence admission review

- **Artifacts reviewed:** This sanitized observation summary.
- **Ledger claims:** `R2-EVID-001`.
- **Source authorization recorded:** Yes; owned device and Stage 1 approval are recorded above without an identifier.
- **Manual review:** Pass — project manager, 2026-07-08.
- **Transformation method:** Reduced raw output to aggregate run completion and attribution findings; removed peripheral identifiers, nearby-device names, and all unrelated advertisement fields.
- **Heuristic repository search:** Pass — the command from [`ADMISSION.md`](../ADMISSION.md) returned policy/context terms only; no prohibited value was found.
- **Synthetic fixture labeling/linkage:** Not applicable; no fixture exists.
- **Decision:** Admitted.
