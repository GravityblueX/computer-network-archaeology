# Ledger synchronization queue

This is the compact live queue for flat-ledger synchronization.

Detailed older pending inventories are preserved in the archived queue and batch manifests under `data/batches/`.

## Pending flat-ledger frontier

Structured records currently run ahead of the flat CSV ledgers.

### Artifacts

Current structured frontier includes:

- `ART-0175..0178` — EtherType, IP Protocol Number, Service/Port and Assigned Numbers registry/publication systems;
- `ART-0179..0185` — ASN namespace/four-octet transition, IEEE MAC address blocks, and IPv4 special-purpose/private/documentation/shared spaces;
- `ART-0186` — Unix `/etc/services` database;
- `ART-0187` — Unix `/etc/protocols` database;
- `ART-0188` — BSD netdb service/protocol lookup API family;
- `ART-0189` — inetd service activation model;
- `ART-0190` — Linux `ETH_P_*` UAPI constants;
- `ART-0191` — Linux `IPPROTO_*` UAPI constants;
- `ART-0192` — BSD Packet Filter packet-capture architecture;
- `ART-0193` — libpcap portable packet-capture interface;
- `ART-0194` — tcpdump analyzer/dissector lineage.

**Next unreserved artifact ID: `ART-0195`**, subject to merge-time verification.

### Sources

Current structured frontier includes:

- `SRC-0166..0184` — number registries, Assigned Numbers, ASN, IEEE RA and IPv4 special-purpose sources;
- `SRC-0185` — BSD `services(5)`;
- `SRC-0186` — BSD `protocols(5)`;
- `SRC-0187` — 4.2BSD `tftpd.c`;
- `SRC-0188` — 4.4BSD IPC/netdb documentation;
- `SRC-0189` — FreeBSD inetd documentation;
- `SRC-0190` — Linux UAPI `if_ether.h`;
- `SRC-0191` — Linux UAPI `in.h`;
- `SRC-0192` — 1993 BSD Packet Filter paper;
- `SRC-0193` — libpcap source/README;
- `SRC-0194` — tcpdump source repository.

**Next unreserved source ID: `SRC-0195`**, subject to verification.

### Lineages

Current structured frontier includes:

- `LIN-0125..0133` — Internet number-registry, ASN/MAC/special-address lineages;
- `LIN-0134` — Assigned Numbers → Unix local service/protocol databases;
- `LIN-0135` — `/etc/services` → netdb service API;
- `LIN-0136` — `/etc/protocols` → netdb protocol API;
- `LIN-0137` — service database → inetd runtime activation;
- `LIN-0138` — registry identities → Linux compile-time/UAPI constants;
- `LIN-0139` — BPF → libpcap capture/filter abstraction;
- `LIN-0140` — libpcap → tcpdump analyzer/dissector interface.

**Next unreserved lineage ID: `LIN-0141`**, subject to verification.

## Recent batch manifests

- `data/batches/2026-08-29-root-hunting.md`
- `data/batches/2026-08-29-root-hunting-2.md`
- `data/batches/2026-08-29-unix-implementation-layer.md`

## Current implementation-layer narratives

- `docs/software/bsd-services-protocols-databases.md`
- `docs/software/inetd-service-name-to-socket.md`
- `docs/software/kernel-protocol-constants.md`
- `docs/operations/tcpdump-bpf-libpcap-observability.md`

## Next root-hunting targets

- exact 4.2BSD `/etc/services` and `/etc/protocols` snapshots and Assigned Numbers diffs;
- `/etc/networks`, `/etc/ethers`, `/etc/rpc` genealogy;
- NIS/NSS backend evolution and compiled service databases;
- earliest inetd source/manual and configuration grammar;
- BSD/Linux historical `ETHERTYPE_*`, `ETH_P_*`, `IPPROTO_*` diffs;
- oldest tcpdump/libpcap distributions and pre-BPF packet capture;
- BPF filter compiler path from service/protocol names to packet offsets/constants;
- packet captures pairing historical RFC diagrams, contemporary implementation output and modern dissectors.

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
