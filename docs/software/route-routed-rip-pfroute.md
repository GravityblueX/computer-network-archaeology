# Static Routes, `route(8)`, `routed`, RIP, and PF_ROUTE: How Unix Learned Where to Send the Packet

## Routing is both kernel state and distributed knowledge

A modern Unix routing table often looks like a simple set of prefix/next-hop/interface entries.

Historically, however, several distinct mechanisms converged on that table:

```text
administrator
   ↓ route(8)
static kernel route

/etc/gateways
   ↓ routed configuration
routed / RIP-style dynamic exchange
   ↓
kernel routing table

ICMP Redirect
   ↓ host-route adjustment
kernel routing table

later routing daemons
   ↓ routing socket / kernel API
kernel forwarding information
```

The important root-hunting distinction is:

> **the route table is state; the mechanisms that create or change that state have separate genealogies.**

---

## 1. `route(8)`: direct administrative mutation of kernel routing state

Historical BSD manuals state that the `route` utility appeared in **4.2BSD**.

Its fundamental role is straightforward:

```text
operator command
      ↓
add / delete / change route
      ↓
kernel route table
```

A route command may specify concepts such as:

```text
destination
network or host
gateway
interface
metric / flags / later attributes
```

The command is not a routing protocol.

It does not discover the Internet.

It is an administrative control interface for routing state.

This distinction matters because modern documentation often places static and dynamic routing under one broad heading, making it easy to forget they are different mechanisms.

---

## 2. The kernel table is the forwarding substrate

Ultimately the IP forwarding path needs an answer to:

```text
for this destination,
which next hop / interface should I use?
```

The routing table stores enough information to make that decision.

Historically the table included host/network distinctions and gateway/interface flags shaped by classful addressing.

Later systems added:

- subnet masks;
- CIDR prefixes;
- cloning/neighbor-related routes;
- metrics;
- multiple tables;
- labels;
- policy-routing metadata;
- multipath/ECMP;
- per-route MTU and expiry state.

So the phrase “routing table” hides a data-structure genealogy of its own.

A future source-code excavation should diff `struct rtentry` and descendant FIB structures release by release.

---

## 3. `routed`: a user-space daemon that learns and publishes routes

BSD manuals state that `routed` also appeared in **4.2BSD**.

Its role is fundamentally different from `route(8)`:

```text
neighbor routing updates
        ↓
routed routing algorithm/database
        ↓
selected routes
        ↓
kernel route table
```

The daemon uses UDP for routing updates and historically implements the family of distance-vector behavior later standardized as RIP.

The 4BSD implementation also used routing traffic to monitor point-to-point links.

This means one process combined:

- route discovery;
- metric calculation;
- periodic advertisements;
- failure inference;
- kernel route installation.

---

## 4. `/etc/gateways`: static knowledge feeding a dynamic daemon

Historical `routed(8)` manuals list:

```text
/etc/gateways
```

for distant gateways.

That file is an excellent hybrid artifact.

It shows that “dynamic routing daemon” never necessarily meant “all route knowledge learned dynamically.”

A daemon can combine:

```text
connected interface knowledge
        +
manual gateway configuration
        +
learned neighbor advertisements
        +
ICMP/other kernel information
        ↓
route selection
```

This mixed-source reality is much closer to actual operations than a clean static-vs-dynamic binary.

---

## 5. Berkeley `routed` helped create the thing later standardized as RIP

RFC 1058 is unusually explicit about ancestry.

It says the Routing Information Protocol described there is **loosely based on the program `routed`, distributed with 4.3BSD**.

But it also says several implementations existed that were supposedly the same protocol yet disagreed in details.

The RFC therefore combines behavior from multiple implementations and makes some choices differently while trying to retain interoperability.

That produces a non-obvious standards genealogy:

```text
PUP Gateway Information Protocol
        ↓
XNS Routing Information Protocol
        ↓ adapted into
Berkeley routed behavior for IP
        ↓ widely copied / diverging implementations
        ↓
RFC 1058 RIP specification
```

The standard is not simply the ancestor of the implementation.

In this case, **implementation practice is part of the ancestor of the standard**.

That deserves an explicit lineage relation distinct from ordinary `standardizes`.

---

## 6. RFC 1009 caught RIP before it was cleanly standardized

RFC 1009 (1987) describes RIP-like protocols as widely available because they were incorporated in Berkeley BSD gateway code and says they came close to being an open IGP.

But it also complains that there was not yet a good standard document for RIP.

One year later RFC 1058 provides exactly that sort of specification.

This snapshot is historically valuable:

```text
1987:
widely deployed behavior
but no single clean specification

1988:
RFC 1058 attempts to codify interoperable RIP
```

Standards can arrive after deployment has already produced a family of de-facto dialects.

---

## 7. ICMP Redirect: another producer of routing state

RFC 792 defines ICMP Redirect so a gateway can tell a host that a better next-hop gateway exists on the same connected network.

The packet can therefore cause a host to alter its routing behavior without a routing daemon.

Conceptually:

```text
host sends through G1
        ↓
G1 sees better gateway G2 on same network
        ↓ ICMP Redirect
host installs/uses better route toward G2
```

RFC 1009 later discusses redirect-created routing-table entries and warns about gateway behavior.

This is another reason “route table = routing protocol output” is wrong.

The route table can be modified by:

- administrator commands;
- routing daemons;
- redirects;
- interface configuration;
- kernel events;
- later routing-socket clients.

---

## 8. A historical bug: user-space daemon state and kernel state can diverge

Old `routed(8)` BUGS sections are unusually revealing.

They warn that:

> the kernel's routing tables may not correspond to those of routed when redirects change or add routes.

This is architecture exposed through a bug report.

There are at least two routing databases:

```text
routed's own routing knowledge
        ↓ tries to program
kernel routing table

but independently:
ICMP Redirect / kernel events
        ↓ change
kernel routing table
```

If the daemon cannot observe every kernel change, the two views diverge.

The fix to this class of problem is not merely a better routing algorithm.

It requires a better **kernel ↔ user-space routing-state interface**.

---

## 9. PF_ROUTE: routing state becomes a socket protocol

BSD descendants document that the **PF_ROUTE routing socket family first appeared in 4.3BSD-Reno**.

This is a major interface transition.

Instead of special-purpose mechanisms for every user-space routing utility, the kernel exposes routing changes and requests through messages containing fields such as:

```text
RTM_ADD
RTM_DELETE
RTM_CHANGE
RTM_GET

RTA_DST
RTA_GATEWAY
RTA_NETMASK
RTA_IFP
RTA_IFA
RTA_AUTHOR
...
```

The route database becomes message-oriented.

Conceptually:

```text
routing daemon / route utility
        ↕ PF_ROUTE messages
kernel routing subsystem
```

This supports both control and observation.

The architectural benefit is directly related to the old `routed` divergence problem: user space gains a mechanism for hearing about routing changes rather than assuming its own database is the sole source of truth.

---

## 10. `route(8)` itself evolves to use the routing socket world

The BSD `route` utility predates PF_ROUTE.

So its own implementation has a lineage:

```text
4.2BSD route command
     ↓ old kernel-routing control interface
4.3BSD-Reno PF_ROUTE appears
     ↓
route utility adapted to routing messages
     ↓
modern route tooling
```

The command name survives while its kernel interface changes underneath.

This is another classic repository pattern:

> user-visible command survives; implementation boundary is replaced.

---

## 11. The routing daemon eventually stops being “the routing architecture”

`routed` was important enough that RFC 1058 used it as a major protocol reference point.

But Internet routing later diversified:

```text
RIP
OSPF
IS-IS
BGP
gated
vendor routing suites
Quagga / FRR descendants
```

The kernel route table becomes a common substrate consumed by many control-plane protocols.

Therefore:

```text
routed
```

should not be drawn as the direct ancestor of all later routing daemons.

The safer genealogy is:

```text
shared user-space routing-daemon role
        ↓ expands into multiple protocol implementations
        ↓
common kernel route/FIB programming interfaces
```

while individual software ancestry such as `gated → Zebra/Quagga/FRR` must be researched separately.

---

## 12. Route table versus FIB versus RIB

Modern terminology often distinguishes:

- RIB — routing information base, protocol/control-plane candidates and selected routes;
- FIB — forwarding information base, data-plane lookup state;
- kernel routing table — OS-specific representation which may correspond more closely to a FIB or selected-route store.

These distinctions should **not** be projected backward carelessly onto early BSD documentation.

Early sources talk about routing tables in their own implementation vocabulary.

A root-hunting record should preserve contemporary terms first, then map them to later concepts separately.

---

## 13. Root-hunting chain

A modern static route command may hide this ancestry:

```text
4.2BSD route(8)
      ↓ user command survives
PF_ROUTE / later routing APIs
      ↓
kernel FIB/routing state
```

A modern dynamic route may hide another:

```text
PUP/XNS distance-vector ideas
      ↓
Berkeley routed
      ↓
de-facto IP RIP variants
      ↓
RFC 1058
      ↓
later RIP implementations
      ↓
kernel route programming API
```

The two paths meet in forwarding state, not in a single protocol ancestry.

---

## 14. Sources

Primary/period anchors:

- RFC 1058 — RIP ancestry and relationship to 4.3BSD `routed`:
  - https://www.rfc-editor.org/info/rfc1058/
- RFC 1009 — 1987 gateway requirements and pre-standardized RIP deployment commentary:
  - https://www.rfc-editor.org/info/rfc1009/
- BSD `route(8)` history:
  - https://man.freebsd.org/cgi/man.cgi?query=route&sektion=8
- historical BSD `routed(8)`:
  - https://man.freebsd.org/cgi/man.cgi?manpath=4.3BSD+NET%2F2&query=routed&sektion=8
- BSD routing socket `route(4)`:
  - https://man.freebsd.org/cgi/man.cgi?query=route&sektion=4
- RFC 792 ICMP Redirect:
  - https://www.rfc-editor.org/info/rfc792/

High-value source-code targets:

- 4.2BSD `route` and `routed` source;
- `/etc/gateways` actual historical files;
- 4.3BSD-Reno PF_ROUTE introduction commit/source;
- `struct rtentry` / `radix` routing-table implementation;
- `gated` early distributions;
- contemporary kernel route dumps and `netstat -r` output.

## 15. Next excavation

- exact `route(8)` kernel interface before PF_ROUTE;
- first PF_ROUTE source and message layout;
- `/etc/gateways` syntax/revision history;
- `routed` source → RFC 1058 field-by-field comparison;
- radix-tree route lookup and CIDR transition;
- `gated` as multi-protocol control-plane software;
- Linux rtnetlink as a parallel descendant interface, without assuming it descends from PF_ROUTE unless sourced;
- kernel FIB structures and modern hardware forwarding split.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
