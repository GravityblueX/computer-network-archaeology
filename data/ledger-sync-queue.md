# Ledger synchronization queue

This is the compact live queue for flat-ledger synchronization.

Detailed older pending inventories are preserved in the archived queue and batch manifests under `data/batches/`.

## Pending flat-ledger frontier

Structured records currently run ahead of the flat CSV ledgers.

### Artifacts

Current structured frontier includes:

- `ART-0175..0178` — EtherType, IP Protocol Number, Service/Port and Assigned Numbers registry/publication systems;
- `ART-0179..0185` — ASN namespace/four-octet transition, IEEE MAC address blocks, and IPv4 special-purpose/private/documentation/shared spaces;
- `ART-0186..0194` — Unix services/protocol databases, netdb API, inetd, Linux UAPI constants, BPF/libpcap/tcpdump;
- `ART-0195` — Unix `/etc/networks`;
- `ART-0196` — Unix `/etc/ethers`;
- `ART-0197` — Unix `/etc/rpc`;
- `ART-0198` — NSS/nsdispatch backend-selection architecture;
- `ART-0199` — Unix `/etc/hosts`;
- `ART-0200` — BSD resolver / `resolv.conf` lineage;
- `ART-0201` — `getaddrinfo()` / `getnameinfo()`;
- `ART-0202` — BSD `route(8)` manual route administration;
- `ART-0203` — BSD `routed`;
- `ART-0204` — BSD PF_ROUTE routing socket;
- `ART-0205` — Linux rtnetlink / NETLINK_ROUTE;
- `ART-0206` — iproute2 `ip route`;
- `ART-0207` — GateD multiprotocol routing daemon lineage.

**Next unreserved artifact ID: `ART-0208`**, subject to merge-time verification.

### Sources

Current structured frontier includes:

- `SRC-0166..0194` — number registries, Unix service/protocol databases, kernel constants and packet-observability sources;
- `SRC-0195` — BSD `networks(5)`;
- `SRC-0196` — BSD `ethers(5)` / SunOS lineage;
- `SRC-0197` — BSD `rpc(5)` / Sun RPC program numbers;
- `SRC-0198` — NetBSD 1.4 `nsswitch.conf`;
- `SRC-0199` — FreeBSD NSS import/provenance;
- `SRC-0200` — BSD `hosts(5)`;
- `SRC-0201` — BSD `resolver(3)`;
- `SRC-0202` — BSD `resolv.conf(5)`;
- `SRC-0203` — RFC 2553 `getaddrinfo()` design/provenance;
- `SRC-0204` — RFC 3493 socket API generation;
- `SRC-0205` — BSD `route(4)` / PF_ROUTE;
- `SRC-0206` — 4.3BSD NET/2 `routed(8)`;
- `SRC-0207` — Linux `rtnetlink(7)`;
- `SRC-0208` — iproute2 source;
- `SRC-0209` — RFC 1118 GateD description;
- `SRC-0210` — RFC 1387 GateD RIP-2 implementation;
- `SRC-0211` — Merit GateD institutional history;
- `SRC-0212` — BSD `route(8)` 4.2BSD history anchor.

**Next unreserved source ID: `SRC-0213`**, subject to verification.

### Lineages

Current structured frontier includes:

- `LIN-0125..0140` — Internet-number registries, Unix local databases, UAPI constants and packet-observability lineages;
- `LIN-0141` — official/NIC network database practice → `/etc/networks`;
- `LIN-0142` — SunOS ethers convention → BSD `/etc/ethers`;
- `LIN-0143` — Sun RPC program-number namespace → `/etc/rpc`;
- `LIN-0144` — ULTRIX/Solaris dispatch ideas → NetBSD NSS;
- `LIN-0145` — NetBSD NSS → FreeBSD NSS;
- `LIN-0146` — BSD/POSIX lookup tradition → `getaddrinfo()`/`getnameinfo()`;
- `LIN-0147` — 4.3BSD `routed` → RFC 1058 RIP influence/standardization context;
- `LIN-0148` — classic `route(8)` operator role → Linux `ip route` role;
- `LIN-0149` — PF_ROUTE ↔ rtnetlink as parallel kernel/user control families;
- `LIN-0150` — rtnetlink → iproute2 operator interface;
- `LIN-0151` — `routed` role → GateD multiprotocol successor/expansion;
- `LIN-0152` — Cornell GateD stewardship → Merit GateD stewardship.

**Next unreserved lineage ID: `LIN-0153`**, subject to verification.

## Recent batch manifests

- `data/batches/2026-08-29-root-hunting.md`
- `data/batches/2026-08-29-root-hunting-2.md`
- `data/batches/2026-08-29-unix-implementation-layer.md`
- `data/batches/2026-08-29-unix-resolver-routing-gated.md`

## Current implementation-layer narratives

- `docs/software/bsd-services-protocols-databases.md`
- `docs/software/inetd-service-name-to-socket.md`
- `docs/software/kernel-protocol-constants.md`
- `docs/operations/tcpdump-bpf-libpcap-observability.md`
- `docs/software/unix-network-databases-beyond-services.md`
- `docs/software/nis-nss-name-service-switch.md`
- `docs/software/hosts-resolver-getaddrinfo.md`
- `docs/software/resolver-getaddrinfo-modern-unix.md`
- `docs/software/route-routed-rip-pfroute.md`
- `docs/routing/route-routed-pfroute-netlink-iproute2.md`
- `docs/routing/routed-to-gated-multiprotocol-daemon.md`

## Next root-hunting targets

- glibc NSS/resolver genealogy versus BSD nsdispatch; do not assume source ancestry;
- first `getaddrinfo` prototype and earliest OS deployments;
- exact 4.2BSD `/etc/networks`, `/etc/services`, `/etc/protocols` snapshots and NIC/Assigned-Numbers diffs;
- original SunOS `/etc/ethers` and Sun RPC `/etc/rpc` source distributions;
- early Linux netlink/rtnetlink design discussions and first iproute releases;
- net-tools `route`/`ifconfig` → iproute2 migration;
- kernel FIB/rules/multipath evolution;
- earliest GateD source tarballs, config grammar, RIP/EGP/HELLO/OSPF/BGP modules and Merit-era release history;
- direct packet/control traces pairing historical APIs with modern systems.

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
