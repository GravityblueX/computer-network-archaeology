# GateD, GNU Zebra, Quagga and FRRouting: Role Continuity vs Real Fork Lineage

## Why this lineage needs two different kinds of arrows

Modern open-source routing suites can look like obvious descendants of GateD because they share familiar roles:

```text
multiple routing protocols
policy/filtering
shared routing state
kernel/FIB programming
Unix host as router control plane
```

But source-code history is not the same as architectural resemblance.

The evidence supports two different stories:

```text
GateD ── role/architecture comparison ──> Zebra

GNU Zebra ── fork ──> Quagga ── fork ──> FRRouting
```

The second is a real code/project fork lineage. The first must be treated more cautiously.

---

## 1. GateD: many protocols in one multiprotocol routing program

GateD emerged to replace `routed` in environments where a Unix gateway needed to speak several routing languages such as RIP, EGP and HELLO.

Its historical importance lies in:

- multiprotocol routing;
- policy-controlled import/export;
- one Unix host acting as routing control plane;
- coupling protocol-derived routes into kernel forwarding state.

GateD is therefore an architectural predecessor in the broad **multiprotocol routing-suite role**.

But that does not establish direct code ancestry to later projects.

---

## 2. GNU Zebra changes the process architecture

GNU Zebra describes itself as **multi-server routing software** capable of turning a Unix machine into a router and supporting protocols such as RIP, OSPF and BGP.

The important architectural change is process decomposition.

Instead of one monolithic multiprotocol program, Zebra-family software separates a central kernel/routing-information service from protocol daemons.

Conceptually:

```text
            bgpd
             |
ripd ---- zebra ---- ospfd
             |
           kernel
```

The `zebra` daemon abstracts kernel routing interaction and exposes an internal protocol/API to routing daemons.

This is a different implementation architecture from the classic “one GateD process contains all protocol functionality” model.

---

## 3. Similar role does not prove GateD → Zebra source ancestry

Both systems solve:

```text
many protocols
    ↓
shared route selection/policy
    ↓
kernel forwarding state
```

But the safe relationship is:

```text
GateD multiprotocol routing role
       ↓ role/architecture evolves in the ecosystem
Zebra distributed multi-daemon routing role
```

not:

```text
GateD source code → Zebra source code
```

unless explicit source provenance is found.

This is exactly why this repository distinguishes `role-descends-into`, `influenced`, `carried-over` and direct revision/fork ancestry.

---

## 4. GNU Zebra → Quagga is a real fork

GNU's historical Zebra page now points users toward Quagga and describes Quagga as having been forked from Zebra.

Quagga's own manual is even more explicit:

> Quagga is a fork of GNU Zebra.

Quagga retained the basic distributed architecture:

```text
zebra   — kernel interface / static routes / internal service
ripd    — RIP
ripngd  — RIPng
ospfd   — OSPFv2
ospf6d  — OSPFv3
bgpd    — BGP
isisd   — IS-IS
```

and used the **Zserv** interface between protocol clients and the zebra daemon.

This is direct project/source lineage, not merely analogy.

---

## 5. Quagga governance records the fork itself

Quagga's project/governance documentation records that Quagga was forked from GNU Zebra by Paul Jakma, after which governance moved to a collective maintainer group.

That is useful because it adds a project-governance layer to the code lineage:

```text
GNU Zebra
    ↓ fork
Quagga
    ↓ community-maintainer governance
```

Technical history should preserve both source ancestry and institutional/project stewardship.

---

## 6. Quagga → FRRouting is another explicit fork

FRRouting's own documentation states plainly:

```text
FRR is a fork of the Quagga project.
```

So the direct code/project genealogy is:

```text
GNU Zebra
    ↓ fork
Quagga
    ↓ fork
FRRouting
```

This is one of the cleanest modern open-source routing software lineages available for archival reconstruction.

---

## 7. The internal Zebra protocol itself has a version genealogy

FRRouting development documentation preserves an unusually useful artifact: version history for the internal **Zebra protocol** used between routing daemons and the zebra core.

It records generations including:

```text
Version 0 — GNU Zebra and early Quagga
Version 1 — later Quagga
Version 2 — Quagga
Version 3 — late Quagga / pre-FRR fork
Version 4 — early FRR, marker changed to prevent binary mixing
Version 5 — larger VRF identifier
Version 6 — later FRR command restructuring
```

This means the fork history survives not only in repository history but in an **internal daemon-to-daemon protocol**.

The protocol version even carries compatibility boundaries between Quagga and FRR binaries.

This is a perfect example of a software-internal wire format becoming an archaeological object.

---

## 8. The zebra daemon is an abstraction boundary

Quagga documentation describes zebra as an abstraction layer over the underlying Unix kernel and as the server for Zserv clients.

That creates a reusable pattern:

```text
protocol daemon
      ↓ route candidate / nexthop
zebra core
      ↓ kernel-specific adaptation
kernel route/FIB interface
```

On different operating systems the kernel interface may be:

- Linux netlink/rtnetlink;
- BSD routing sockets;
- other platform-specific mechanisms.

The routing protocol daemon can therefore avoid embedding every kernel API directly.

This is a different kind of portability from GateD's earlier multiprotocol integration.

---

## 9. FRR preserves the architecture while greatly expanding it

Modern FRRouting describes itself as a full-featured routing suite supporting BGP, RIP, OSPF, IS-IS and many additional protocols/extensions across Linux and BSD systems.

The core lineage remains recognizable:

```text
protocol daemons
       ↓
Zebra / routing infrastructure
       ↓
platform kernel interface
```

while newer generations add:

- VRFs;
- EVPN;
- BFD;
- MPLS/LDP;
- PIM;
- policy-based routing;
- management daemon/northbound APIs;
- richer nexthop handling;
- modern Linux integration.

The organism grew dramatically while keeping a recognizable architectural skeleton.

---

## 10. GateD and Zebra represent two different answers to the same scaling problem

A useful comparison is:

```text
GateD
┌─────────────────────────────┐
│ RIP EGP HELLO ...           │
│ policy / routing database   │
│ kernel interface            │
└─────────────────────────────┘
        one multiprotocol program
```

versus:

```text
Zebra / Quagga / FRR

ripd ─┐
ospfd ├── internal protocol ── zebra ── kernel
bgpd ─┤
isisd ┘
```

Both centralize route coordination, but process boundaries differ.

This difference should be treated as a major architectural branch, not hidden by the generic phrase “routing daemon.”

---

## 11. What survived from the old Unix-router idea

Across GateD, Zebra, Quagga and FRR, the durable operational architecture is:

```text
routing intelligence in user space
        ↓
policy / route selection
        ↓
program kernel forwarding state
```

That pattern also connects backward to:

- BSD `routed`;
- Fuzzball routing systems;
- NSFNET routing hosts;

and forward to modern software routers and routing stacks.

But source-code ancestry should only be asserted where documentation or repository history proves it.

---

## 12. Root-hunting targets

The archive should preserve:

### GateD
- first source tarballs;
- configuration grammar;
- internal RIB structures;
- kernel interface modules;
- protocol modules;
- Cornell/Merit release transitions.

### GNU Zebra
- earliest source/CVS snapshots;
- first `zebra` daemon/Zserv protocol;
- vty CLI design;
- kernel interface code per OS.

### Quagga
- fork point from Zebra;
- first release;
- Zserv version changes;
- protocol daemon splits;
- governance and project assets.

### FRRouting
- exact Quagga fork point;
- Zebra protocol v3→v4 incompatibility boundary;
- FRR 2.x→current architecture changes;
- modern kernel/netlink modules;
- configuration migration tools.

The ideal exhibit is a source-level genealogy:

```text
file / function / protocol version
GNU Zebra revision
      ↓
Quagga revision
      ↓
FRR revision
```

beside a separate architectural comparison to GateD.

---

## Primary anchors

- GNU Zebra historical project page.
- Quagga manual and project documentation.
- FRRouting project/user/developer documentation.
- FRR Zebra protocol version-history documentation.
- GateD sources already recorded in the repository (RFC 1118, RFC 1387, Merit history).

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
