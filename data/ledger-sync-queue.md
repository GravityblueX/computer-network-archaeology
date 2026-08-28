# Ledger synchronization queue

This is the compact live queue for flat-ledger synchronization.

A detailed snapshot of all pending records before the field-level root-hunting batch is preserved at:

- [`ledger-sync-queue-archive-2026-08-29-pre-root-hunting.md`](ledger-sync-queue-archive-2026-08-29-pre-root-hunting.md)

The first field-level batch is described at:

- [`batches/2026-08-29-root-hunting.md`](batches/2026-08-29-root-hunting.md)

## Why this file is compact

The claim-level `records/` tree can advance faster than the flat CSV ledgers. Rewriting a large CSV after every excavation burst is riskier than preserving verified batch manifests and merging periodically.

## Pending flat-ledger frontier

### Artifacts

Earlier pending structured records:

- `ART-0114` through `ART-0165`, with reserved intermediate gaps documented in the archived queue and root-hunting batch manifest.

No new structured artifact IDs were assigned in the second root-hunting narrative-only burst yet.

**Next unreserved artifact ID: `ART-0166`**, subject to merge-time verification.

### Sources

Earlier pending structured records:

- `SRC-0097` through `SRC-0155`, including reserved gaps documented in archived/batch manifests.

No new structured source IDs were assigned in the second root-hunting narrative-only burst yet.

**Next unreserved source ID: `SRC-0156`**, subject to verification.

### Lineages

Earlier pending structured records:

- `LIN-0085` through `LIN-0117`.

No new structured lineage IDs were assigned in the second root-hunting narrative-only burst yet.

**Next unreserved lineage ID: `LIN-0118`**, subject to verification.

## New narrative files since the first root-hunting batch

Second root-hunting expansion:

- `docs/lineage/ipv4-options-cemetery-pmtud.md`
- `docs/lineage/dscp-ecn-shared-octet.md`
- `docs/lineage/icmp-type-code-full-survivorship.md`
- `docs/lineage/tcp-options-genealogy.md`
- `docs/lineage/dns-extension-forest-dnssec-naptr-sshfp-tlsa.md`
- `docs/lineage/smtp-ehlo-capability-genealogy.md`
- `docs/lineage/mime-multipart-to-form-data.md`

High-value structured promotions from this burst should cover:

- IPv4 option families / PMTUD;
- DSCP and ECN bit semantics;
- ICMP message-branch survivorship;
- TCP MSS/WS/SACK/TS option families;
- DNSSEC/NAPTR/SSHFP/TLSA extension branches;
- SMTP EHLO extension registry branches;
- multipart/form-data and media-type registration lineage.

## Batch merge checklist

Before changing the flat CSV ledgers:

1. fetch the complete latest CSV blobs;
2. verify actual highest IDs and concurrent additions;
3. validate every queued record file against its JSON schema;
4. preserve reserved gaps rather than silently reusing them;
5. append/promote rows without changing existing rows;
6. validate CSV quoting and column counts;
7. confirm every structured `ART/SRC/LIN` ID is discoverable in flat ledgers;
8. synchronize `docs/INDEX.md`, `catalogs/lineages.md`, and relevant human-readable indexes;
9. archive completed queue state before clearing it.

This queue is archival hygiene, not a second research database.
