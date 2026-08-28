# Ledger synchronization queue

This is the compact live queue for flat-ledger synchronization.

A detailed snapshot of all pending records before the field-level root-hunting batch is preserved at:

- [`ledger-sync-queue-archive-2026-08-29-pre-root-hunting.md`](ledger-sync-queue-archive-2026-08-29-pre-root-hunting.md)

The new field-level batch is described at:

- [`batches/2026-08-29-root-hunting.md`](batches/2026-08-29-root-hunting.md)

## Why this file is compact

The claim-level `records/` tree can advance faster than the flat CSV ledgers. Rewriting a large CSV after every excavation burst is riskier than preserving a verified batch manifest and merging periodically.

The archived queue preserves the exact pre-batch ID inventory. This live queue preserves only the current merge frontier and next safe IDs.

## Pending flat-ledger frontier

### Artifacts

Earlier pending structured records (see archive):

- `ART-0114` through `ART-0158`, with the reserved intermediate gaps documented in the archived queue.

Field-level root-hunting batch:

- `ART-0159` — IPv4 TOS → DS field semantic lineage
- `ART-0160` — IPv4 Identification field semantic lineage
- `ART-0161` — ICMP Source Quench branch
- `ART-0162` — DNS Resource Record typed extension framework
- `ART-0163` — SMTP command/reply transactional core
- `ART-0164` — Internet media-type system descended from MIME
- `ART-0165` — DNS SVCB / HTTPS Resource Record family

**Next unreserved artifact ID: `ART-0166`**, subject to merge-time verification.

### Sources

Earlier pending structured records (see archive):

- `SRC-0097` through `SRC-0147`, including reserved gaps documented in the archived queue.

Field-level root-hunting batch:

- `SRC-0148` — RFC 2474 DS field
- `SRC-0149` — RFC 6864 updated IPv4 ID
- `SRC-0150` — RFC 2782 DNS SRV
- `SRC-0151` — RFC 3596 DNS AAAA / IPv6 support
- `SRC-0152` — RFC 8659 DNS CAA
- `SRC-0153` — RFC 9460 DNS SVCB / HTTPS
- `SRC-0154` — RFC 2046 MIME media types
- `SRC-0155` — RFC 9110 HTTP media-type reuse

**Next unreserved source ID: `SRC-0156`**, subject to merge-time verification.

### Lineages

Earlier pending structured records (see archive):

- `LIN-0085` through `LIN-0111`.

Field-level root-hunting batch:

- `LIN-0112` — IPv4 TOS octet → DS field semantic replacement/continuity
- `LIN-0113` — IPv4 Identification semantics RFC 791 → RFC 6864
- `LIN-0114` — DNS RR framework → AAAA extension
- `LIN-0115` — DNS RR framework → SVCB/HTTPS extension
- `LIN-0116` — MIME media types → HTTP representation media types
- `LIN-0117` — RFC 821 SMTP command core → modern SMTP command/reply core

**Next unreserved lineage ID: `LIN-0118`**, subject to merge-time verification.

## New narrative/methodology files in this batch

- `docs/methodology/root-hunting.md`
- `docs/lineage/ipv4-header-field-survivorship.md`
- `docs/lineage/icmp-type-code-survivorship.md`
- `docs/lineage/dns-rr-type-genealogy.md`
- `docs/lineage/smtp-command-reply-survivorship.md`
- `docs/lineage/mime-content-type-to-http-media-types.md`

## Batch merge checklist

Before changing the flat CSV ledgers:

1. fetch the complete latest CSV blobs;
2. verify the actual highest IDs and concurrent additions;
3. validate every queued record file against its JSON schema;
4. preserve reserved gaps rather than silently reusing them;
5. append/promote rows without changing existing rows;
6. validate CSV quoting and column counts;
7. confirm every structured `ART/SRC/LIN` ID is discoverable in the flat ledgers;
8. synchronize `docs/INDEX.md`, `catalogs/lineages.md`, and relevant human-readable indexes;
9. archive the completed queue state before clearing it.

This queue is archival hygiene, not a second research database.
