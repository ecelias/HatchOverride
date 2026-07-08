# Evidence admission rules

Use this checklist before committing any observation, interpretation, or generated fixture under this directory. Originals stay outside the repository. Admit only the smallest transformed excerpt needed to support a ledger claim and the provenance metadata needed to reproduce or challenge it.

These rules are a repository contribution boundary, not legal advice. Here, **proprietary capture** means raw vendor-tool output or third-party material for which explicit redistribution permission has not been established. Do not commit it. A transformed excerpt may be admitted only when it contains no prohibited material, is necessary to support a claim, and does not reproduce the source artifact.

## Admission checklist

- [ ] The contributor is authorized to use the source and records that authorization without adding account or device identifiers.
- [ ] The original and unsanitized source remain outside the repository.
- [ ] The artifact contains no private device identifiers, credentials, keys, tokens, unrelated personal data, proprietary capture, or unsanitized source material.
- [ ] The artifact is the minimum transformed excerpt needed to support its linked ledger claim.
- [ ] The linked ledger record preserves capture method, timestamp, conditions, result, direction, timing, repetition, and errors when applicable.
- [ ] Device model and relevant firmware/app versions are recorded when available; missing values are explicit.
- [ ] An observation links to its claim in [`ledger.md`](ledger.md). An interpretation also links to its source observation.
- [ ] A generated fixture is labeled **synthetic**, links to reproduced ledger claims and its sanitized source observations, and is never called a capture.
- [ ] Manual review and the heuristic repository search below are recorded. Search results have been examined; a clean search is not treated as proof that sanitization is complete.

Reject the artifact if any item fails. Remove prohibited material from the candidate artifact rather than masking it in repository history.

## Transform an observation for admission

1. Work on a copy of the original outside the repository.
2. Remove private identifiers, credentials, unrelated personal data, and source content not needed for the claim. Replace a removed value with a descriptive marker such as `[device identifier removed]` only when its presence matters to the observation.
3. Reduce the copy to the minimum excerpt that supports the claim. Do not copy raw vendor-tool output or unlicensed third-party material into the repository.
4. Preserve the required capture metadata in the linked ledger record: method, timestamp, conditions, result, direction, timing, repetition, errors, and available device/version context.
5. In the review record, describe the transformation method, including what categories were removed, replaced, or reduced. Do not record the removed values.
6. Review the transformed artifact against the checklist before moving it into `docs/evidence/`.

## Review record

Add this record to the ticket handoff or pull-request description:

```text
Evidence admission review
- Artifacts reviewed:
- Ledger claims:
- Source authorization recorded: yes/no
- Manual review: pass/fail — reviewer and date
- Transformation method: removed/replaced/reduced categories, without removed values
- Heuristic repository search: pass/fail — command and findings
- Synthetic fixture labeling/linkage: pass/fail/not applicable
- Decision: admitted/rejected
- Notes:
```

Run a heuristic search from the repository root and review every match. Extend the terms when the source suggests another identifier or secret format.

```sh
rg -n -i '(password|passwd|secret|api[_-]?key|access[_-]?token|refresh[_-]?token|private[_-]?key|serial[_ -]?number|device[_ -]?id|mac[_ -]?address|email|phone)' docs/evidence
```

The command identifies suspicious text; it does not validate privacy, ownership, or redistribution rights.

## Historical hardware-free empty-layout dry run

PROJ-002 used this dry run before evidence artifacts existed. It is retained as the historical validation record, not as a current instruction that the layout must remain empty. It validated the admission boundary without scanning, pairing, connecting, reading, writing, or contacting a device:

1. Confirm that, at the time of the dry run, `docs/evidence/observations/` and `docs/evidence/generated-fixtures/` contained only their README files.
2. Apply the checklist to those files and record `not applicable` for artifact-specific provenance and fixture linkage.
3. Run the heuristic search and manually review its expected policy/template matches.
4. Record the result using the review record above.

```text
Evidence admission review — PROJ-002 empty-layout dry run
- Artifacts reviewed: docs/evidence/observations/README.md; docs/evidence/generated-fixtures/README.md
- Ledger claims: not applicable; no evidence artifact was admitted
- Source authorization recorded: not applicable; no source artifact was used
- Manual review: pass — project_manager, 2026-07-07
- Transformation method: not applicable; no source artifact was transformed
- Heuristic repository search: pass — `rg -n -i '(password|passwd|secret|api[_-]?key|access[_-]?token|refresh[_-]?token|private[_-]?key|serial[_ -]?number|device[_ -]?id|mac[_ -]?address|email|phone)' docs/evidence`; expected findings were policy and template terms only
- Synthetic fixture labeling/linkage: not applicable; no fixture exists
- Decision: admitted; empty layout and policy README files only
- Notes: No scanning, pairing, connection, read, write, transmission, or other hardware interaction occurred.
```
