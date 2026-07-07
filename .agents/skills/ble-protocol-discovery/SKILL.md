---
name: ble-protocol-discovery
description: Discover and document Hatch Restore 2 BLE behavior without turning guesses into code.
---

# BLE protocol discovery

1. Define the single behavior under study and the safe experiment.
2. Record device/firmware/app versions without private identifiers.
3. Capture advertised services, GATT services, characteristics, properties, descriptors, reads, writes, notifications, timing, and errors.
4. Store sanitized raw evidence separately from interpretations.
5. Add ledger rows labeled `observed`, `inferred`, `disproved`, or `unknown`.
6. Reproduce an observation before proposing an encoder/decoder fixture.
7. Never transmit or pair without explicit human approval.
