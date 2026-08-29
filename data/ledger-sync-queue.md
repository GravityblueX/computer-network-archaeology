# Ledger synchronization queue

This compact live queue tracks the structured-record frontier. Older inventories live in `data/batches/` and the archived queue.

## Current structured frontier

### Artifacts

Recent ranges include:

- `ART-0175..0213` — registries, Unix/Linux implementation layers, resolver/routing suites, NSS/net-tools and GNU Zebra→Quagga→FRRouting;
- `ART-0214..0224` — ifconfig/rtnetlink, proc/socket diagnostics, ss/TCP observability, Linux neighbour/ND and RPDB/ip rule;
- `ART-0225` — legacy Linux network-device ioctl control family;
- `ART-0226` — Linux 2.1.15 Netlink character-device/message hybrid;
- `ART-0227` — Linux 2.1.68 rtnetlink object model;
- `ART-0228` — early ip/iproute/iproute2 userspace suite;
- `ART-0229` — rtmon;
- `ART-0230` — ip monitor;
- `ART-0231` — Linux network namespace;
- `ART-0232` — Linux VRF/l3mdev routing-domain model;
- `ART-0233` — generic l3mdev FIB rule.

**Next unreserved artifact ID: `ART-0234`**, subject to merge-time verification.

### Sources

- `SRC-0166..0235` — prior registry/Unix/Linux/routing/operations evidence;
- `SRC-0236..0247` — network-device ioctl ABI, Linux 2.1.15/2.1.68 Netlink/rtnetlink source, FIB compatibility conversion, RFC 3549, ip/iproute archive/history, rtmon/ip monitor, network namespaces and VRF/l3mdev.

**Next unreserved source ID: `SRC-0248`**, subject to verification.

### Lineages

- `LIN-0125..0177` — prior registry, Unix/Linux implementation, routing-suite, operations, neighbour/RPDB and ZAPI lineages;
- `LIN-0178..0187` — ioctl→rtnetlink migration, Netlink transport/message/object transition, rtnetlink→iproute, event-monitoring, RPDB→VRF integration, l3mdev transition and netns/VRF negative lineage.

**Next unreserved lineage ID: `LIN-0188`**, subject to verification.

## Persistent task authority

Use `docs/methodology/root-hunting-master-worklist.md`. New work must be added there when discovered; chat reminders are not the task database.

## Latest batch manifests

- `data/batches/2026-08-29-linux-operations-roots.md`
- `data/batches/2026-08-29-netlink-iproute-netns-vrf.md`

## Current narrative frontier

Latest additions:

- `docs/software/linux-ifconfig-ioctl-rtnetlink-transition.md`
- `docs/software/netlink-rtnetlink-origins.md`
- `docs/software/iproute2-early-release-command-evolution.md`
- `docs/operations/rtmon-ip-monitor-rtnetlink-events.md`
- `docs/routing/network-namespaces-vrf-l3mdev-rpdb.md`

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
