# Staged safe BLE capture procedure

Use this procedure only with a personally owned or explicitly authorized device and account. It documents evidence collection; it does not establish any Restore 2 protocol fact or authorize hardware interaction.

Before every physical-device stage, record the named action, device authorization, operator, date/time, intended tool, expected side effects, stop conditions, and explicit human approval. Approval for one stage does not authorize another. Pairing, any BLE transmission, and device writes always require explicit approval for that action. Never bypass authentication, encryption, firmware protection, or safety controls.

Default build and test commands must not run any stage below. Physical-device work is manual and opt-in.

## Common prerequisites and records

Before starting:

- Confirm device/account ownership or explicit authorization without recording private identifiers.
- Define one bounded question linked to an `unknown` claim in [`ledger.md`](ledger.md).
- Choose the minimum stage capable of answering it; do not proceed to later stages automatically.
- Prepare an external, non-repository location for original output and a timer or timestamp source.
- Review [`ADMISSION.md`](ADMISSION.md). Only a sanitized, minimum transformed excerpt may enter [`observations/`](observations/README.md).
- Record available device model and firmware/app versions; explicitly record unavailable values.

For every attempted stage, record capture method, timestamp, conditions, result, direction, timing, repetition, errors, approval reference, and whether the stage completed or aborted. On error or abort, stop interaction, preserve the error outside the repository until sanitized, and record what occurred and what was not attempted. Never treat absence, failure, or an aborted stage as evidence of unsupported behavior without a reproducible experiment.

## Stage 1 — Passive advertisement observation

- **Approval:** Obtain explicit project-manager and human approval before scanning. This conservative gate remains until passive-scan approval semantics are resolved.
- **Prerequisites:** Common prerequisites; Bluetooth enabled; no connection, pairing, read, subscription, or write action configured.
- **Expected side effects:** The application requests a scan and receives nearby advertisements; it requests no connection or GATT operation. Do not treat this as guaranteed RF-passive behavior: macOS or the Bluetooth controller may transmit scan requests. Other nearby devices may be visible in original output.
- **Collect:** Tool/version, scan interval, timestamps, conditions, repetitions, sanitized advertisement fields relevant to the question, and errors. Do not retain private device identifiers.
- **Output:** Original output remains outside the repository. Candidate sanitized excerpts go in `docs/evidence/observations/`; interpretation belongs in `docs/evidence/interpretations/`; update `ledger.md` only after admission review.
- **Sanitize:** Remove nearby-device data, private identifiers, and unrelated fields; apply `ADMISSION.md`.
- **Abort:** Stop if authorization is uncertain, the tool initiates a connection, prohibited data cannot be separated safely, or unexpected device behavior occurs. Record the trigger and that no later stage was attempted.

## Stage 2 — Connection

- **Approval:** Obtain explicit human approval for the connection action and bounded disconnect cleanup. Stage 1 approval is insufficient.
- **Prerequisites:** Stage 1 results justify connection; target selection can be made without committing a private identifier; no automatic pairing, discovery, read, subscription, or write is enabled.
- **Expected side effects:** The host initiates BLE connection traffic; the device may change connection state, indicator behavior, availability, or power use.
- **Collect:** Connection attempt/result, timestamps, duration, disconnect reason, timing, repetitions, conditions, direction, and errors.
- **Output and sanitization:** Follow the common output paths and `ADMISSION.md`; remove addressing and private identifiers.
- **Abort:** Use the preapproved disconnect if pairing is requested unexpectedly, authorization/authentication is unclear, the device changes state unexpectedly, or the tool begins an unapproved operation. If disconnect is not approved or safe, issue no further BLE action, document the state, and obtain approval before cleanup. Record the error and unattempted stages.

## Stage 3 — Pairing

- **Approval:** Stop and obtain explicit human approval specifically for pairing and any planned bond cleanup. Never reuse connection approval; unpairing or bond deletion requires separate approval unless named in this approval.
- **Prerequisites:** Pairing is necessary for the bounded question; account/device authorization is confirmed; expected OS/device prompts and a safe unpairing plan are documented.
- **Expected side effects:** The host and device exchange pairing traffic and may store bonds or keys; prompts, account effects, or persistent trust state may result.
- **Collect:** Prompt/result, timestamps, conditions, persistence observed, direction, timing, repetitions, and errors. Never record keys, credentials, or private identifiers.
- **Output and sanitization:** Follow the common output paths and `ADMISSION.md`; retain no secrets or raw pairing material.
- **Abort:** Stop on unexpected credential requests, protection-bypass requirements, unclear prompts, or unexpected persistent/device effects. Do not attempt bypasses. Perform only preapproved cleanup; otherwise issue no further BLE action, document the state, and obtain approval before cleanup. Record the result and whether cleanup was safely performed.

## Stage 4 — Reads

- **Approval:** Obtain explicit human approval for the exact read request; a read is BLE transmission even if it is expected not to modify application state.
- **Prerequisites:** The target attribute and reason are established by admitted evidence; connection/pairing prerequisites are satisfied; the tool cannot issue automatic writes or subscriptions.
- **Expected side effects:** The host transmits a read request; the device responds or errors and may update transport/session state.
- **Collect:** Sanitized attribute reference, request/response direction, timestamps, bytes only when admissible and necessary, timing, repetitions, conditions, and errors.
- **Output and sanitization:** Follow the common output paths and `ADMISSION.md`; do not commit raw vendor output or values containing prohibited data.
- **Abort:** Stop on authentication/encryption errors, unexpected state changes, responses containing data that cannot be safely sanitized, or any unapproved follow-on request.

## Stage 5 — Notification subscription

- **Approval:** Obtain explicit human approval for the exact subscription, bounded observation, and unsubscribe/disconnect cleanup. Subscription commonly requires a transmitted configuration write; treat it as transmission and a device write.
- **Prerequisites:** The characteristic and bounded observation window are supported by admitted evidence; connection/pairing requirements are satisfied; automatic unrelated subscriptions are disabled.
- **Expected side effects:** The host may write subscription configuration; the device may emit notifications and change session or power behavior until unsubscribe/disconnect.
- **Collect:** Sanitized attribute reference, subscribe/unsubscribe results, notification direction, timestamps, payload excerpts only when admissible, timing, count/repetition, conditions, and errors.
- **Output and sanitization:** Follow the common output paths and `ADMISSION.md`; minimize payloads and remove prohibited content.
- **Abort:** Use the preapproved unsubscribe or disconnect on unexpected traffic volume, device behavior, sensitive content, authentication errors, or inability to bound the observation. If cleanup is not approved or safe, issue no further BLE action, document the state, and obtain approval before cleanup. Record cleanup and errors.

## Stage 6 — Writes

- **Approval:** Stop and obtain explicit human approval for the exact bytes/action and expected device effect immediately before writing. No earlier approval authorizes a write.
- **Prerequisites:** The write and expected response are justified by reproduced, admitted evidence; safe initial state, rollback/recovery, timeout, and repetition limit are documented; safety controls remain active.
- **Expected side effects:** The host transmits data that may change device state, stored settings, behavior, indicators, sound/light output, session state, or account-visible state.
- **Collect:** Evidence-linked operation name, sanitized transmitted/received excerpts, direction, timestamps, timing, bounded repetition, before/after state, expected/actual result, and errors.
- **Output and sanitization:** Follow the common output paths and `ADMISSION.md`. A later generated fixture must be labeled synthetic and linked to reproduced claims; it is not a capture.
- **Abort:** Do not write if bytes, target, state, effect, recovery, or authorization is uncertain. Stop on any unexpected effect, timeout, error, or mismatch; execute only the preapproved safe recovery and record the outcome.

## Stage handoff record

Record this in the ticket handoff for each attempted stage:

```text
BLE capture stage record
- Question / ledger claim:
- Stage:
- Device/account authorization confirmed: yes/no (no private identifiers)
- Explicit human approval: approver, action, date/time
- Method / tool version:
- Conditions and expected side effects:
- Start/end time and repetition:
- Direction and result:
- Errors / abort trigger / cleanup:
- Original output retained outside repository: yes/no
- Candidate sanitized artifact and output path: path/none
- Admission review: pass/fail/not performed
- Later stages not attempted:
```

## Manual no-hardware dry run

This review exercises the procedure only. Do not start a scanner or Bluetooth tool, pair, connect, read, subscribe, write, or transmit.

1. Read the common prerequisites and all six stages in order.
2. Confirm each stage has a distinct approval, prerequisites, side effects, collected fields, output path, sanitization, and abort/error record.
3. Confirm pairing, every transmission, and every write require action-specific explicit approval.
4. Confirm default build/test commands are excluded and authorization/security controls are preserved.
5. Confirm the handoff record can represent an aborted stage without implying later stages ran.

```text
PROJ-003 manual no-hardware dry run
- Reviewer: documentation_agent
- Date: 2026-07-07
- Result: pass
- Stages reviewed: passive observation, connection, pairing, reads, notification subscription, writes
- Hardware actions performed: none; no scanning, pairing, connecting, reading, subscribing, writing, or BLE transmission
- Findings: every required field and gate is present; later stages require separate approval
- Limitations: documentation review only; no tool, radio, OS, or device behavior was validated
```
