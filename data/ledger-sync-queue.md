# Ledger synchronization queue

This is the compact live queue for flat-ledger synchronization.

Detailed older pending inventories are preserved at:

- [`ledger-sync-queue-archive-2026-08-29-pre-root-hunting.md`](ledger-sync-queue-archive-2026-08-29-pre-root-hunting.md)
- [`batches/2026-08-29-root-hunting.md`](batches/2026-08-29-root-hunting.md)
- [`batches/2026-08-29-root-hunting-2.md`](batches/2026-08-29-root-hunting-2.md)

## Why this file is compact

The claim-level `records/` tree can advance faster than the flat CSV ledgers. Rewriting a large CSV after every excavation burst is riskier than preserving verified batch manifests and merging periodically.

## Pending flat-ledger frontier

### Artifacts

Pending structured range now extends through:

- `ART-0174` — multipart/form-data Web form-upload media type.

The detailed composition of earlier ranges and reserved gaps lives in the archive/batch manifests above.

Latest batch (`ART-0166..0174`):

- IPv4 Options cemetery;
- Path MTU Discovery;
- DSCP/ECN semantic lineage;
- ICMP Type/Code survivorship;
- TCP Window Scale/Timestamps;
- TCP SACK;
- DNSSEC;
- SMTP EHLO extension framework;
- multipart/form-data.

**Next unreserved artifact ID: `ART-0175`**, subject to merge-time verification.

### Sources

Pending structured range now extends through:

- `SRC-0165` — IANA ICMP Parameters registry.

Latest batch (`SRC-0156..0165`) includes RFC 1191, RFC 7126, RFC 3168, RFC 7323, RFC 2018, RFC 4033, IANA SMTP extensions, RFC 7578, RFC 6838 and the IANA ICMP registry.

**Next unreserved source ID: `SRC-0166`**, subject to verification.

### Lineages

Pending structured range now extends through:

- `LIN-0124` — MIME multipart model → multipart/form-data.

Latest batch (`LIN-0118..0124`) covers PMTUD derivation, DS/ECN semantic carry-over, TCP option growth, DNS→DNSSEC, SMTP→EHLO capability growth, and MIME multipart→Web form upload.

**Next unreserved lineage ID: `LIN-0125`**, subject to verification.

## Current narrative frontier

Second root-hunting expansion:

- `docs/lineage/ipv4-options-cemetery-pmtud.md`
- `docs/lineage/dscp-ecn-shared-octet.md`
- `docs/lineage/icmp-type-code-full-survivorship.md`
- `docs/lineage/tcp-options-genealogy.md`
- `docs/lineage/dns-extension-forest-dnssec-naptr-sshfp-tlsa.md`
- `docs/lineage/smtp-ehlo-capability-genealogy.md`
- `docs/lineage/mime-multipart-to-form-data.md`

## Next high-value structured targets

- complete IPv4 Option-number table plus Router Alert/source-route branches;
- classic PMTUD → PLPMTUD / IPv6 Packet Too Big;
- DiffServ PHBs and ECN/AccECN;
- TCP option Kind registry, MSS and option-space exhaustion;
- DNS NAPTR/SSHFP/TLSA and DNSSEC predecessor generations;
- individual SMTP EHLO extension artifacts such as SIZE/8BITMIME/PIPELINING/STARTTLS/AUTH/DSN;
- RFC 1867 → RFC 2388 → RFC 7578 form-upload revisions;
- raw packet/capture records pairing present traffic with historical diagrams.

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
