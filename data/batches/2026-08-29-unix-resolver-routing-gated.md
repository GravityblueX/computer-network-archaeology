# 2026-08-29 Unix Resolver, Routing-Control and GateD Root-Hunting Batch

Theme: trace present-day Unix name resolution and routing administration back through local databases, resolver APIs, routing daemons and kernel/user control interfaces.

## Narrative outputs

- `docs/software/resolver-getaddrinfo-modern-unix.md`
- `docs/routing/route-routed-pfroute-netlink-iproute2.md`
- `docs/routing/routed-to-gated-multiprotocol-daemon.md`

## Structured source outputs

- `SRC-0203` — RFC 2553 getaddrinfo design/provenance
- `SRC-0204` — RFC 3493 socket API generation
- `SRC-0205` — BSD route(4) / PF_ROUTE
- `SRC-0206` — 4.3BSD NET/2 routed(8)
- `SRC-0207` — Linux rtnetlink(7)
- `SRC-0208` — iproute2 source
- `SRC-0209` — RFC 1118 GateD description
- `SRC-0210` — RFC 1387 GateD RIP-2 implementation
- `SRC-0211` — Merit GateD institutional history
- `SRC-0212` — BSD route(8) 4.2BSD history anchor

Earlier attached sources used in this batch include `SRC-0195..0202` for `/etc/networks`, `/etc/ethers`, `/etc/rpc`, NSS, `/etc/hosts`, BSD resolver and `resolv.conf`, plus `SRC-0110` for RFC 1058 RIP.

## Structured artifact outputs

- `ART-0195` — `/etc/networks`
- `ART-0196` — `/etc/ethers`
- `ART-0197` — `/etc/rpc`
- `ART-0198` — NSS/nsdispatch
- `ART-0199` — `/etc/hosts`
- `ART-0200` — BSD resolver/resolv.conf lineage
- `ART-0201` — getaddrinfo/getnameinfo
- `ART-0202` — route(8)
- `ART-0203` — routed
- `ART-0204` — PF_ROUTE
- `ART-0205` — Linux rtnetlink
- `ART-0206` — iproute2 ip route
- `ART-0207` — GateD

## Structured lineage outputs

- `LIN-0141` — official/NIC network database practice → `/etc/networks`
- `LIN-0142` — SunOS ethers convention → BSD `/etc/ethers`
- `LIN-0143` — Sun RPC program-number namespace → `/etc/rpc`
- `LIN-0144` — ULTRIX/Solaris dispatch ideas → NetBSD NSS
- `LIN-0145` — NetBSD NSS → FreeBSD NSS
- `LIN-0146` — BSD/POSIX lookup tradition → getaddrinfo/getnameinfo
- `LIN-0147` — 4.3BSD routed → RFC 1058 RIP influence/standardization context
- `LIN-0148` — classic route(8) role → Linux `ip route` role
- `LIN-0149` — PF_ROUTE ↔ rtnetlink as parallel kernel/user control families
- `LIN-0150` — rtnetlink → iproute2 operator interface
- `LIN-0151` — routed role → GateD multiprotocol replacement/expansion
- `LIN-0152` — Cornell GateD stewardship → Merit GateD stewardship

## Principal findings

1. `getaddrinfo()` combines several older namespaces: host naming, service/port naming, address families, socket types and protocol numbers.
2. A lookup API does not prove its backend once NSS/name-service dispatch exists.
3. `route(8)`, `routed`, PF_ROUTE, rtnetlink and `ip route` occupy different layers; they must not be flattened into one version chain.
4. RFC 1058 documents a case where deployed implementations around BSD `routed` existed before the formal RIP specification consolidated behavior.
5. PF_ROUTE and Linux rtnetlink solve broadly similar kernel/user control problems but no direct ancestry is asserted.
6. GateD marks the shift from a routed-centric routing daemon to a configurable multiprotocol/policy routing framework on Unix.
7. GateD also has an institutional lineage: Cornell → GateD Consortium → Merit in 1995.

## Next IDs

Subject to merge-time verification after this batch is committed:

- next artifact: `ART-0208`
- next source: `SRC-0213`
- next lineage: `LIN-0153`

## Next excavation targets

- glibc NSS/resolver source genealogy versus BSD nsdispatch (do not assume common code ancestry);
- first getaddrinfo prototype and earliest OS deployments;
- early Linux netlink/rtnetlink design discussions and first iproute releases;
- net-tools `route`/`ifconfig` → iproute2 operational migration;
- kernel FIB structures and policy-routing evolution;
- earliest GateD source tarballs, config grammar and protocol-module history;
- GateD → OSPF/BGP implementation milestones;
- modern FRRouting/BIRD role genealogy with code ancestry kept separate.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
