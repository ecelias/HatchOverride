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

- **Status:** `unknown`
- **Interpretation:** Current repository evidence does not answer this question.
- **Confidence:** No conclusion.
- **Confirming or falsifying experiment:** Perform an authorized, documented, repeatable observation under the approved capture procedure.
- **Device model:** Not recorded; no source observation exists.
- **Firmware version:** Not recorded; no source observation exists.
- **App version:** Not recorded; no source observation exists.
- **Derived fixtures:** none
- **Supported code:** none

### R2-EVID-002 — Which services, characteristics, properties, and descriptors are observable?

- **Status:** `unknown`
- **Interpretation:** Current repository evidence does not answer this question.
- **Confidence:** No conclusion.
- **Confirming or falsifying experiment:** Perform an authorized inventory using the approved capture procedure and record sanitized results.
- **Device model:** Not recorded; no source observation exists.
- **Firmware version:** Not recorded; no source observation exists.
- **App version:** Not recorded; no source observation exists.
- **Derived fixtures:** none
- **Supported code:** none

### R2-EVID-003 — What authentication, encryption, sequencing, timing, or firmware constraints exist?

- **Status:** `unknown`
- **Interpretation:** Current repository evidence does not answer this question.
- **Confidence:** No conclusion.
- **Confirming or falsifying experiment:** Define and obtain approval for a safe experiment that isolates one constraint before collecting evidence.
- **Device model:** Not recorded; no source observation exists.
- **Firmware version:** Not recorded; no source observation exists.
- **App version:** Not recorded; no source observation exists.
- **Derived fixtures:** none
- **Supported code:** none

### R2-EVID-004 — Can one operation and its response be observed safely and reproduced?

- **Status:** `unknown`
- **Interpretation:** Current repository evidence does not answer this question.
- **Confidence:** No conclusion.
- **Confirming or falsifying experiment:** After explicit human approval, document one bounded operation/response experiment and attempt reproduction under the same conditions.
- **Device model:** Not recorded; no source observation exists.
- **Firmware version:** Not recorded; no source observation exists.
- **App version:** Not recorded; no source observation exists.
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
