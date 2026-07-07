# ADR 0001: Evidence-first, C# API with a native macOS test double

Status: proposed

## Context

The 2017 Hatch Baby Rest library is a compact C# BLE client. The Restore 2 is a different product generation with no protocol evidence yet. VirtualBT demonstrates Windows GATT/HID server patterns but is tied to Windows APIs and does not provide a macOS BLE controller emulator.

## Decision

Begin with protocol evidence, then build the public API in modern C#. Spike a minimal CoreBluetooth `CBPeripheralManager` GATT peripheral test double on macOS. Keep Rust and C++ out until a measured requirement appears.

## Consequences

- The first milestone produces evidence and a test boundary, not a broad application.
- A CoreBluetooth peripheral test double may cover API tests but cannot be described as full controller-level Bluetooth emulation.
- Protocol and transport seams are introduced only where tests or a second implementation require them.

## Evidence needed to accept

- Restore 2 service and characteristic observations.
- Confirmation that macOS can advertise the required synthetic GATT shape.
- A minimal .NET-to-native integration experiment or a documented process boundary.
