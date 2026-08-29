# Ledger synchronization queue

This compact live queue tracks the structured-record frontier. Older inventories live in `data/batches/` and the archived queue.

## Current structured frontier

### Artifacts

Recent ranges include:

- `ART-0175..0213` — registries, Unix/Linux implementation layers, resolver/routing suites, NSS/net-tools and GNU Zebra→Quagga→FRRouting;
- `ART-0214` — ifconfig / ioctl control model;
- `ART-0215` — rtnetlink link/address control model;
- `ART-0216` — `ip addr` / `ip link`;
- `ART-0217` — `/proc/net/tcp{,6}` tables;
- `ART-0218` — tcp/inet/sock diag family;
- `ART-0219` — `ss` / TCP_INFO observability;
- `ART-0220` — Linux generic neighbour subsystem;
- `ART-0221` — `ip neigh`;
- `ART-0222` — IPv6 ND/NUD;
- `ART-0223` — Linux RPDB;
- `ART-0224` — `ip rule` / multiple-FIB administration.

**Next unreserved artifact ID: `ART-0225`**, subject to merge-time verification.

### Sources

- `SRC-0166..0221` — prior registry/Unix/Linux/routing-suite evidence;
- `SRC-0222..0235` — ifconfig/iproute2/rtnetlink, proc socket tables, ss/TCP_INFO, RFC 5681/6298/4861, neighbour and RPDB documentation, and FRR ZAPI version history.

**Next unreserved source ID: `SRC-0236`**, subject to verification.

### Lineages

- `LIN-0125..0160` — prior registry, Unix/Linux implementation, resolver/routing-suite and real-fork lineages;
- `LIN-0161..0162` — ioctl/ifconfig role → rtnetlink → ip addr/link;
- `LIN-0163..0166` — proc socket tables → sock_diag → ss and TCP timing/congestion-state observability;
- `LIN-0167..0170` — ARP + IPv6 ND/NUD → Linux neighbour object → ip neigh, with ARP-vs-ND negative-lineage guard;
- `LIN-0171..0172` — classic destination routing → RPDB → ip rule/multiple FIB tables;
- `LIN-0173..0175` — ZAPI v0→v1→v2→v3;
- `LIN-0160` — existing Quagga v3 → FRR v4 fork/revision boundary;
- `LIN-0176..0177` — ZAPI v4→v5→v6.

**Next unreserved lineage ID: `LIN-0178`**, subject to verification.

## Persistent task authority

Use `docs/methodology/root-hunting-master-worklist.md` as the human-readable execution list. New work must be added there when discovered; chat reminders are not the task database.

## Latest batch

- `data/batches/2026-08-29-linux-operations-roots.md`

## Flat-ledger merge checklist

Before changing the three flat CSV ledgers:

1. fetch complete latest CSV blobs;
2. verify actual highest IDs and concurrent additions;
3. validate queued JSON records against schemas;
4. preserve reserved gaps;
5. append/promote without altering existing rows;
6. validate CSV quoting and column counts;
7. verify every structured ID is discoverable from flat ledgers;
8. synchronize human-readable indexes;
9. archive completed queue state before clearing it.

This queue is archival hygiene, not a second master database.
