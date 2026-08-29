# Ledger synchronization queue

This is the compact live queue for flat-ledger synchronization.

Detailed older pending inventories are preserved at:

- `ledger-sync-queue-archive-2026-08-29-pre-root-hunting.md`
- `batches/2026-08-29-root-hunting.md`
- `batches/2026-08-29-root-hunting-2.md`

## Pending flat-ledger frontier

Structured records currently run ahead of the flat CSV ledgers.

### Artifacts

Latest structured frontier after the number-space/identity batch:

- `ART-0175..0178` — EtherType, IP Protocol Number, Service/Port and Assigned Numbers publication/registry systems;
- `ART-0179` — Autonomous System Number namespace and special-use subspaces;
- `ART-0180` — four-octet ASN transition;
- `ART-0181` — IEEE EUI-48 / MA-L / MA-M / MA-S assignment system;
- `ART-0182` — IPv4 Special-Purpose Address registry framework;
- `ART-0183` — RFC 1918 private IPv4 space;
- `ART-0184` — TEST-NET documentation address family;
- `ART-0185` — 100.64.0.0/10 Shared Address Space.

**Next unreserved artifact ID: `ART-0186`**, subject to merge-time verification.

### Sources

Latest structured frontier:

- `SRC-0166..0172` — IEEE/IANA number registries and Assigned Numbers publication lineage;
- `SRC-0173` — RFC 1930;
- `SRC-0174` — RFC 6793;
- `SRC-0175` — RFC 6996;
- `SRC-0176` — RFC 5398;
- `SRC-0177` — RFC 5396;
- `SRC-0178` — IEEE Registration Authority FAQ;
- `SRC-0179` — IEEE Registration Authority registry page;
- `SRC-0180` — RFC 1918;
- `SRC-0181` — RFC 5737;
- `SRC-0182` — RFC 6598;
- `SRC-0183` — IANA IPv4 Special-Purpose Address Space registry;
- `SRC-0184` — IANA Autonomous System Numbers registry.

**Next unreserved source ID: `SRC-0185`**, subject to verification.

### Lineages

Latest structured frontier:

- `LIN-0125..0128` — EtherType/protocol/port/Assigned-Numbers registry lineages;
- `LIN-0129` — two-octet ASN regime → four-octet ASN transition;
- `LIN-0130` — original private ASN reservation → expanded private-use ranges;
- `LIN-0131` — OUI-era allocation → MA-L/MA-M/MA-S family;
- `LIN-0132` — RFC1918 private space ↔ RFC6598 Shared Address Space as distinct coexisting scopes;
- `LIN-0133` — TEST-NET-1 → three-prefix documentation family.

**Next unreserved lineage ID: `LIN-0134`**, subject to verification.

## Current narrative frontier

Recent root-hunting narratives include:

- `docs/lineage/ethertype-registry-genealogy.md`
- `docs/lineage/ip-protocol-number-registry-genealogy.md`
- `docs/lineage/port-number-service-registry-genealogy.md`
- `docs/lineage/as-number-genealogy-16-to-32-bit.md`
- `docs/lineage/oui-eui48-mac-address-block-genealogy.md`
- `docs/lineage/ipv4-special-purpose-address-space-genealogy.md`

## Next implementation-layer targets

- `/etc/services` and `/etc/protocols` from 4.2BSD onward;
- `getservbyname`, `getservbyport`, `getprotobyname`, `getprotobynumber` libc interfaces;
- `/etc/inetd.conf` service/protocol resolution and process launch;
- BSD/Linux `ETHERTYPE_*`, `ETH_P_*`, `IPPROTO_*` constants;
- tcpdump/BPF/libpcap dissector genealogy;
- `/etc/networks`, `/etc/ethers`, protocol/service databases through NIS/NSS and modern resolver stacks.

## Batch merge checklist

Before changing flat CSV ledgers:

1. fetch complete latest CSV blobs;
2. verify actual highest IDs and concurrent additions;
3. validate all queued JSON records against schemas;
4. preserve reserved gaps;
5. append/promote without altering existing rows;
6. validate CSV quoting/column counts;
7. verify every structured ID is discoverable from flat ledgers;
8. synchronize human-readable indexes;
9. archive completed queue state before clearing it.

This queue is archival hygiene, not a second research database.
