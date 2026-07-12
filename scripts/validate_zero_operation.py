#!/usr/bin/env python3
"""Validate the focused-v1 zero-operation artifact set.

This is intentionally boring: standard library only, no BLE access, no build
system, no protocol implementation. It checks the documents and files that
exist on the zero-operation path.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STATUS_VALUES = {"observed", "inferred", "disproved", "unknown"}
MATURITY_VALUES = {"reproduced", "fixture-backed", "supported", "hardware-validated"}
REQUIRED_OBSERVED_FIELDS = [
    "Sanitized source reference",
    "Capture method",
    "Timestamp",
    "Conditions",
    "Result",
    "Direction",
    "Timing",
    "Repetition",
    "Errors",
    "Device model",
    "Firmware version",
    "App version",
    "Derived fixtures",
    "Supported code",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read(path: str) -> str:
    target = ROOT / path
    if not target.is_file():
        fail(f"missing required file: {path}")
    return target.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        fail(f"{label} missing: {needle}")


def ledger_records(ledger: str) -> dict[str, str]:
    matches = list(re.finditer(r"^### (R2-EVID-\d{3}) .*$", ledger, re.MULTILINE))
    if not matches:
        fail("ledger contains no R2-EVID records")
    records: dict[str, str] = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(ledger)
        records[match.group(1)] = ledger[match.start() : end]
    return records


def validate_ledger() -> None:
    ledger = read("docs/evidence/ledger.md")
    records = ledger_records(ledger)

    for required in [f"R2-EVID-{i:03d}" for i in range(1, 7)]:
        if required not in records:
            fail(f"missing ledger record: {required}")

    for record_id, body in records.items():
        status_match = re.search(r"- \*\*Status:\*\* `([^`]+)`", body)
        if not status_match:
            fail(f"{record_id} missing status")
        status = status_match.group(1)
        if status not in STATUS_VALUES:
            fail(f"{record_id} uses invalid status: {status}")

        maturity_match = re.search(r"- \*\*Maturity:\*\* `([^`]+)`", body)
        if maturity_match and maturity_match.group(1) not in MATURITY_VALUES:
            fail(f"{record_id} uses invalid maturity: {maturity_match.group(1)}")

        for field in ["Interpretation", "Confidence", "Confirming or falsifying experiment"]:
            require(body, f"- **{field}:**", f"{record_id}")

        if status in {"observed", "disproved"}:
            for field in REQUIRED_OBSERVED_FIELDS:
                require(body, f"- **{field}:**", f"{record_id}")


def validate_links() -> None:
    evidence_files = list((ROOT / "docs/evidence").rglob("*.md"))
    for path in evidence_files:
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            if not file_part:
                continue
            resolved = (path.parent / file_part).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"{path.relative_to(ROOT)} links outside repository: {target}")
            if not resolved.exists():
                fail(f"{path.relative_to(ROOT)} has broken link: {target}")


def validate_zero_operation_decision() -> None:
    decision = read("docs/evidence/interpretations/2026-07-09-focused-v1-evidence-gate.md")
    require(decision, "Focused v1 follows the **zero-operation path**.", "gate decision")
    for text in [
        "PROJ-018 — zero-operation validation check",
        "PROJ-019 — zero-operation handoff documentation",
        "PROJ-008 — generated fixture",
        "command fixture",
        "protocol codec",
        "public device-operation API",
        "synthetic GATT shape for a selected operation",
        "supported-operation example",
    ]:
        require(decision, text, "gate decision")


def validate_generated_vs_observed_labeling() -> None:
    observations = read("docs/evidence/observations/README.md")
    fixtures = read("docs/evidence/generated-fixtures/README.md")
    require(observations, "sanitized source observations", "observations README")
    require(fixtures, "synthetic test data", "generated-fixtures README")
    require(fixtures, "not device captures", "generated-fixtures README")
    require(fixtures, "contains no generated fixtures yet", "generated-fixtures README")


def validate_absent_prohibited_artifacts() -> None:
    forbidden_paths = [
        ROOT / "src",
        ROOT / "tests",
        ROOT / "examples",
        ROOT / "docs/evidence/generated-fixtures",
    ]

    generated_fixture_files = [
        p
        for p in (ROOT / "docs/evidence/generated-fixtures").rglob("*")
        if p.is_file() and p.name != "README.md"
    ]
    if generated_fixture_files:
        fail("generated fixture files exist on zero-operation path")

    for directory in forbidden_paths[:3]:
        if directory.exists():
            fail(f"prohibited implementation/example directory exists: {directory.relative_to(ROOT)}")

    prohibited_suffixes = {".cs", ".csproj", ".sln"}
    prohibited_name_parts = [
        "codec",
        "fixture",
        "test-double",
        "testdouble",
        "device-operation",
        "supported-operation",
    ]
    allowed = {
        Path("docs/evidence/generated-fixtures/README.md"),
        Path("docs/evidence/interpretations/2026-07-09-focused-v1-evidence-gate.md"),
        Path("scripts/validate_zero_operation.py"),
    }
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        relative = path.relative_to(ROOT)
        if relative in allowed:
            continue
        lowered = relative.as_posix().lower()
        if path.suffix.lower() in prohibited_suffixes:
            fail(f"prohibited .NET/API artifact exists: {relative}")
        if any(part in lowered for part in prohibited_name_parts):
            fail(f"prohibited zero-operation artifact name exists: {relative}")


def main() -> int:
    validate_ledger()
    validate_links()
    validate_zero_operation_decision()
    validate_generated_vs_observed_labeling()
    validate_absent_prohibited_artifacts()

    print("PASS: zero-operation evidence validation")
    print("supported_operations=0")
    print("hardware_validation=unavailable/not run")
    print("ble_actions=not run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
