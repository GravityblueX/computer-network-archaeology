# Ledger synchronization queue

This is the compact live queue for flat-ledger synchronization. Detailed older pending inventories are preserved under `data/batches/` and the archived queue.

## Current structured frontier

The `records/` tree is intentionally ahead of the flat CSV ledgers.

### Artifacts

Recent structured ranges now include:

- `ART-0175..0194` — number registries, Unix service/protocol databases, kernel constants, BPF/libpcap/tcpdump;
- `ART-0195..0207` — `/etc/networks`, `/etc/ethers`, `/etc/rpc`, NSS, `/etc/hosts`, resolver/getaddrinfo, route/routed/PF_ROUTE/rtnetlink/iproute2/GateD;
- `ART-0208` — glibc NSS;
- `ART-0209` — Linux net-tools;
- `ART-0210` — GNU Zebra;
- `ART-0211` — Quagga;
- `ART-0212` — FRRouting;
- `ART-0213` — Zebra/Quagga/FRR internal Zebra protocol lineage.

**Next unreserved artifact ID: `ART-0214`**, subject to merge-time verification.

### Sources

Recent structured ranges now include:

- `SRC-0166..0194` — registries, Unix database/implementation and packet-observability sources;
- `SRC-0195..0212` — Unix local databases, NSS, resolver, route/routed, PF_ROUTE/rtnetlink/iproute2 and GateD sources;
- `SRC-0213` — glibc NSS manual;
- `SRC-0214` — Linux Foundation net-tools;
- `SRC-0215` — Linux Foundation iproute2;
- `SRC-0216` — Linux kernel IP-aliasing compatibility documentation;
- `SRC-0217` — GNU Zebra historical page;
- `SRC-0218` — Quagga manual;
- `SRC-0219` — Quagga governance/fork documentation;
- `SRC-0220` — FRRouting documentation;
- `SRC-0221` — FRRouting Zebra protocol version history.

**Next unreserved source ID: `SRC-0222`**, subject to merge-time verification.

### Lineages

Recent structured ranges now include:

- `LIN-0125..0140` — registries, Unix local database/UAPI/capture lineages;
- `LIN-0141..0152` — Unix network databases, NSS, resolver, route/routed/PF_ROUTE/rtnetlink/iproute2/GateD;
- `LIN-0153` — Solaris NSS method → glibc NSS influence, explicitly no shared code;
- `LIN-0154` — BSD nsdispatch ↔ glibc NSS parallel families;
- `LIN-0155` — net-tools role migration → iproute2;
- `LIN-0156` — GNU Zebra → Quagga fork;
- `LIN-0157` — Quagga → FRRouting fork;
- `LIN-0158` — GateD → GNU Zebra role genealogy without code-ancestry claim;
- `LIN-0159` — GNU Zebra internal protocol → Quagga carry-over;
- `LIN-0160` — Quagga Zebra protocol v3 → FRR v4 revision boundary.

**Next unreserved lineage ID: `LIN-0161`**, subject to merge-time verification.

## Recent batch manifests

- `data/batches/2026-08-29-root-hunting.md`
- `data/batches/2026-08-29-root-hunting-2.md`
- `data/batches/2026-08-29-unix-implementation-layer.md`
- `data/batches/2026-08-29-unix-resolver-routing-gated.md`
- `data/batches/2026-08-29-nss-routing-forks.md`

## Current narrative frontier

- `docs/software/resolver-getaddrinfo-modern-unix.md`
- `docs/routing/route-routed-pfroute-netlink-iproute2.md`
- `docs/routing/routed-to-gated-multiprotocol-daemon.md`
- `docs/software/glibc-nss-vs-bsd-nsdispatch.md`
- `docs/software/net-tools-to-iproute2.md`
- `docs/routing/gated-zebra-quagga-frr.md`

## Next root-hunting targets

- first glibc NSS release/commit and exact Solaris comparison;
- glibc `getaddrinfo`/NSS module call graph and DNS/files/NIS behavior by release;
- earliest Linux rtnetlink/netlink design sources and first iproute releases;
- distro migration from net-tools to iproute2;
- GNU Zebra first release/CVS snapshot and Zserv v0 format;
- exact Quagga and FRR fork points;
- Zebra protocol source diffs across v0-v6+;
- GateD vs Zebra RIB/policy/kernel-interface architecture from primary source;
- modern packet/control traces pairing historical command/API language with current systems.

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
