# Restore 2 discovery-mode Battery Level read — 2026-07-08

- **Ledger claim:** [`R2-EVID-004`](../ledger.md#r2-evid-004--can-one-operation-and-its-response-be-observed-safely-and-reproduced)
- **Source claims:** [`R2-EVID-001`](../ledger.md#r2-evid-001--does-an-authorized-restore-2-advertise-ble-services-under-reproducible-conditions), [`R2-EVID-002`](../ledger.md#r2-evid-002--which-services-characteristics-properties-and-descriptors-are-observable), and [`R2-EVID-003`](../ledger.md#r2-evid-003--what-authentication-encryption-sequencing-timing-or-firmware-constraints-exist)
- **Outcome:** Reproduced read response for Battery Service `180F`, Battery Level characteristic `2A19`, on the discovery-mode candidate. Attribution to the owned Restore 2 remains inferred from the preceding advertisement and GATT-inventory evidence plus owner-confirmed discovery-mode timing; no private identifier was retained.
- **Authorization:** The human owner confirmed discovery mode and explicitly approved up to three bounded attempts to scan, connect, discover `180F/2A19`, issue one read request to `2A19` per attempt, record the response or error, and disconnect. No writes, notification subscriptions, pairing, or other characteristic reads were approved or attempted.
- **Candidate selected:** Battery Level read from service `180F`, characteristic `2A19`. This was selected as the smallest observed, read-capable, non-vendor-specific candidate operation. It does not establish Hatch Restore 2 vendor command semantics.
- **Device model:** Hatch Restore 2 (owner-confirmed); no private identifier recorded.
- **Firmware version:** Unavailable.
- **App version:** Unavailable; the app was not used by the capture tool.
- **Host and tool:** arm64 macOS 26.5.1 host. Temporary native CoreBluetooth command-line central built with Apple clang 17.0.0. Source SHA-256 `17d99b5ff58d09d56badfced2abb13bb433dfc1404a3786b5b4aa06c429c34a2`; binary SHA-256 `5bc50b2884d66f6cc9914726c866af4d5d4d2ccf4b2f4db92d01386c995ed0e6`.
- **Tool behavior:** The tool requested an unfiltered scan, matched the PROJ-004 sanitized candidate signature, required exactly one matching candidate during a two-second confirmation window, connected to that candidate, discovered service `180F`, discovered characteristic `2A19`, issued one `readValueForCharacteristic:` call for `2A19`, recorded value length and unsigned one-byte value when present, disconnected, and exited. Forbidden-call review found no write, notification subscription, descriptor discovery, pairing, or connected-peripheral retrieval call in the tool source.
- **Conditions:** Owner-confirmed discovery mode before execution. Bluetooth reported `powered_on`. Runs were launched from the same host in the same session. The three runs overlapped in wall-clock time, so the repetition supports response stability in this bounded session but should not be treated as spaced independent environmental trials.
- **Predeclared result rule:** Reproduced read result if at least two successful attempts returned the same admissible one-byte value under the same bounded conditions; inconclusive for ambiguous candidates, connection/discovery/read errors, auth/encryption prompts, unsafe device behavior, or inconsistent values.
- **Direction:** Host central scanned, initiated a connection, requested service and characteristic discovery, transmitted one read request for `180F/2A19`, received a read response, and disconnected. macOS or the controller may also have transmitted scan requests and connection-management traffic.
- **Timing and repetition:** Three processes completed with `read_complete`: run 1 from 2026-07-08 21:07:32Z to 21:07:36Z, run 2 from 21:07:33Z to 21:07:36Z, and run 3 from 21:07:33Z to 21:07:36Z.
- **Sanitized read result:** Each of the three runs returned value length `1` and unsigned one-byte value `0` for service `180F`, characteristic `2A19`.
- **Errors:** CoreBluetooth reported `powered_on`; no connect failure, discovery failure, read failure, authentication prompt, encryption prompt, pairing prompt, or unexpected disconnect was recorded.
- **Original output:** Retained outside the repository under `/private/tmp/hatchoverride-proj006` for this local handoff only; it must not be committed. Raw JSONL SHA-256 values: run 1 `3cbeb7370159445642e386ad6ea3d27a0c462d07034392ab26eec0e09941c5d7`, run 2 `66fd6ea8e5f0c81f95739f21f727403ac391477ea1be8258ac21ed2c958dc39e`, run 3 `af86ba1e5a483365ba3632eb0149fd291e101159963c4580756ef4fd29ed7149`.

## Interpretation boundaries

- This observation establishes one reproduced read response for `180F/2A19` under the recorded conditions only.
- The one-byte value is admitted because it is the minimum response needed to support the read claim. It is not evidence of vendor command framing, command direction, notification behavior, write behavior, or a supported public API operation.
- The absence of auth/encryption/pairing prompts applies only to this read path under this session's conditions. It does not disprove auth/encryption requirements for other reads, notifications, writes, firmware versions, app states, or non-discovery conditions.
- The result is probably insufficient by itself for the v1 one-operation path because the PRD asks for a command/notification pair if safely observable. It is still useful evidence for the zero-operation vs one-operation gate because it records the safest reproduced operation attempted before any vendor write or subscription.

## Stage handoff

- **Stage:** Stage 4 — exact read request.
- **Completed:** Yes; three bounded attempts completed.
- **Expected side effects:** Scan requests, connection-management traffic, GATT discovery requests, one read request per attempt, read responses, and disconnect cleanup may have been transmitted or observed. No pairing, notification subscription, or write was attempted.
- **Abort or cleanup:** No abort trigger was reached. Each process disconnected if connected and exited.
- **Admission decision:** Admit this minimum transformed summary only. Peripheral identifiers, exact local name suffixes, advertisement payload values, RSSI/signal values, and raw event streams remain outside the repository.

## Evidence admission review

- **Artifacts reviewed:** This sanitized Battery Level read summary.
- **Ledger claims:** `R2-EVID-004`; related limitation note for `R2-EVID-003`.
- **Source authorization recorded:** Yes; owned device and exact read approval are recorded above without an identifier.
- **Manual review:** Pass — project manager, 2026-07-08.
- **Transformation method:** Reduced raw JSONL to event timing, tool provenance, selected UUIDs, value length, one-byte unsigned value, and error status; removed private peripheral identifiers by tool design and omitted raw event streams.
- **Heuristic repository search:** Pass — the command from [`ADMISSION.md`](../ADMISSION.md) returned policy/context terms only; no prohibited value was found.
- **Synthetic fixture labeling/linkage:** Not applicable; no fixture exists.
- **Decision:** Admitted.
