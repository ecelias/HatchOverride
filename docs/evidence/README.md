# Restore 2 evidence

This directory keeps evidence classes separate so protocol claims remain traceable:

- [`ledger.md`](ledger.md) records claim status, interpretation, confidence, experiments, and artifact links.
- [`ADMISSION.md`](ADMISSION.md) defines the sanitization and provenance review required before an artifact is committed.
- [`capture-procedure.md`](capture-procedure.md) separates physical-device observation stages, approvals, side effects, sanitization, and abort records.
- [`observations/`](observations/README.md) contains sanitized source observations or references.
- [`interpretations/`](interpretations/README.md) contains analysis derived from observations.
- [`generated-fixtures/`](generated-fixtures/README.md) contains synthetic test data derived from reproduced evidence.

The only claim statuses are `observed`, `inferred`, `disproved`, and `unknown`. When applicable, maturity is recorded separately as `reproduced`, `fixture-backed`, `supported`, or `hardware-validated`.

An `observed` or `disproved` claim requires a sanitized source reference and its capture method, timestamp, conditions, result, direction, timing, repetition, and errors when applicable. Device model and relevant firmware/app versions are recorded when available; absence is explicit. Generated fixtures are never device captures.

Do not add private identifiers, credentials, proprietary captures, or unrelated personal data. Apply the [evidence admission rules](ADMISSION.md) before committing an artifact. The repository contains two sanitized Stage 1 observation summaries, one sanitized Stage 2 GATT inventory summary, one sanitized Stage 4 read summary, and no raw captures; Restore 2 attribution remains inferred.
