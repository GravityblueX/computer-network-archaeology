# From `route(8)` and `routed` to PF_ROUTE, rtnetlink and `ip route`

## One word — “routing” — hides several different layers

A Unix system can contain all of the following:

```text
route(8)
routed(8)
kernel routing table
routing socket / PF_ROUTE
rtnetlink / NETLINK_ROUTE
ip route
```

They do not form one simple program-version ladder.

They represent different responsibilities:

```text
operator command
    ↓
user-space control interface
    ↓
kernel routing state
    ↑
dynamic routing daemon
```

The archaeological task is to identify which responsibility survives across systems and which interface was redesigned.

---

## 1. `route(8)`: the operator edits kernel state

The classic `route` utility appeared in 4.2BSD.

Its basic role is direct administrative manipulation of the host's routing table:

```text
route add
route delete
route change
route get
```

That is different from running a routing protocol.

Conceptually:

```text
administrator
    ↓
route(8)
    ↓
kernel route entry
```

The command became such a durable administrative convention that descendants still exist across BSDs and traditional Linux networking tools.

But the **kernel interface used to implement the command changed** over time.

---

## 2. `routed`: a daemon computes routes instead of merely entering them

`routed` also belongs to the early BSD TCP/IP world, but its role is different.

Historical documentation describes it as a network routing daemon that manages kernel routing tables and exchanges routing information using a variant of the Xerox NS Routing Information Protocol.

The control loop is therefore:

```text
neighbor routing advertisements
        ↓
      routed
        ↓
distance-vector computation
        ↓
kernel routing table
```

A local administrator might seed special information through files such as `/etc/gateways`, but the daemon's defining role is dynamic maintenance rather than one-off manual edits.

---

## 3. Implementation became de-facto protocol before the RFC caught up

RFC 1058 (1988) provides unusually valuable evidence about this transition.

It says the RIP specification is **loosely based on** the `routed` program distributed with 4.3BSD. It also notes that multiple supposedly compatible implementations already disagreed in details, so the RFC combined behavior from several implementations while trying to preserve interoperability.

This gives a documented lineage:

```text
Xerox NS routing ideas
        ↓
Berkeley routed implementation
        ↓
commercial / third-party RIP-like implementations
        ↓
implementation disagreement
        ↓
RFC 1058 standardization
```

The standard therefore did not simply precede the code.

In this case, **deployment and implementation created the protocol family that the RFC later regularized**.

---

## 4. Early kernel route state could change outside the daemon

Classic `routed` documentation preserves a revealing operational problem: the kernel's routing table could change because of ICMP Redirect processing in ways that did not necessarily match `routed`'s internal database.

This illustrates a general architecture problem:

```text
user-space daemon state
      ≠
kernel forwarding state
```

if there is no sufficiently rich notification/control interface between them.

It would be historically unsafe to claim that this specific bug *caused* PF_ROUTE without design records proving that connection.

But it clearly demonstrates the class of problem that later explicit kernel/user routing-message interfaces address.

---

## 5. PF_ROUTE: routing state becomes a socket message interface

BSD routing sockets made route control and notification a first-class socket protocol family.

The `route(4)` documentation states that **PF_ROUTE first appeared in 4.3BSD-Reno**.

Instead of treating route-table modification as an opaque private kernel operation, user space can exchange structured messages such as route add/delete/get and address/interface notifications.

Conceptually:

```text
route utility / routing daemon
           ↕
      PF_ROUTE socket
           ↕
       kernel routing
```

This makes the routing table a visible control-plane object rather than simply an internal kernel data structure.

---

## 6. The BSD `route` command itself adapted to PF_ROUTE

Later BSD `route(8)` manuals describe the command as capable of issuing requests through the programmatic interface documented by `route(4)`.

So the user-facing role survives:

```text
route add default ...
```

while the underlying control path changes:

```text
early route-table manipulation
        ↓
PF_ROUTE structured messages
```

This is a classic root-hunting distinction:

> **command-language continuity does not imply kernel-API continuity.**

---

## 7. Linux did not simply inherit PF_ROUTE

Linux developed a different kernel/user messaging architecture: **netlink**.

The routing family is exposed through:

```c
socket(AF_NETLINK, ..., NETLINK_ROUTE)
```

and commonly called **rtnetlink**.

Current Linux documentation says rtnetlink allows routing tables to be read and altered, but its scope is broader than routes alone. It also carries information and operations for:

- addresses;
- links;
- neighbors;
- queueing disciplines;
- route tables;
- related network configuration objects.

Messages include families such as:

```text
RTM_NEWROUTE
RTM_DELROUTE
RTM_GETROUTE
```

This is functionally analogous to some PF_ROUTE responsibilities, but **direct ancestry must not be asserted without design evidence**.

The safe model is:

```text
BSD PF_ROUTE      Linux rtnetlink
      \             /
       \           /
        same broad role:
 kernel ↔ user routing/control messages
```

parallel designs rather than a proven revision chain.

---

## 8. `iproute2` turns rtnetlink into an operator language

Modern Linux commonly exposes routing configuration through `iproute2`, especially:

```text
ip route
ip address
ip link
ip neigh
ip rule
```

The maintained `iproute2` source describes itself as a set of Linux networking utilities, and `ip/iproute.c` explicitly identifies itself as the implementation of **`ip route`**, historically associated with Alexey Kuznetsov.

The relationship is:

```text
kernel rtnetlink objects/messages
        ↓
iproute2 libraries/parsers
        ↓
`ip route` operator command
```

The command surface is richer than classic `route(8)` because Linux exposes policy-routing tables, route protocol tags, scopes, metrics, multiple nexthops and many other attributes through netlink.

---

## 9. `route -n` and `ip route` represent different eras of observability

Traditional `route`/`netstat` tools often present routes as a table of destination, gateway, flags, metric and interface.

`ip route` reflects a newer data model where the routing object can include:

```text
prefix
routing table
scope
route type
protocol origin
metric
nexthop(s)
MTU / RTT-related attributes
policy-routing context
```

This is not merely prettier output.

It reflects a richer kernel routing API.

---

## 10. The historical line is role continuity plus interface replacement

A misleading family tree would be:

```text
route → routed → PF_ROUTE → netlink → iproute2
```

That mixes tools, daemons and APIs.

A better decomposition is:

```text
MANUAL ROUTE ADMINISTRATION
4.2BSD route(8)
      ↓ role survives
BSD route(8) / Linux route
      ↓ role survives with richer model
Linux `ip route`

DYNAMIC ROUTE COMPUTATION
XNS-inspired routing
      ↓
BSD routed
      ↓ de-facto dialect
RIP / RFC 1058

KERNEL ↔ USER ROUTING CONTROL
private/older interfaces
      ↓
BSD PF_ROUTE

parallel Linux branch:
netlink / rtnetlink
      ↓
iproute2
```

This preserves the distinction between **what the software does** and **how it talks to the kernel**.

---

## 11. What survived into current systems

Still recognizable today:

- a kernel forwarding/routing table;
- explicit route add/delete/get operations;
- named route origins/protocols;
- dynamic routing daemons separate from the forwarding kernel;
- user-space tools that translate symbolic names and prefixes into kernel route objects;
- message interfaces that allow the kernel to notify user space of network-state changes.

What changed dramatically:

- data structures;
- address-family assumptions;
- policy routing;
- multipath support;
- route metrics and attributes;
- notification APIs;
- user-space tool suites.

---

## 12. Root-hunting targets

For a particular Unix release, preserve:

- `route(8)` source and manual;
- kernel route-table structures;
- routing socket/netlink headers;
- `routed`, `gated`, or later daemon source;
- `/etc/gateways` and related configuration;
- route protocol/service assignments;
- sample route-table dumps;
- packet captures of routing updates;
- user-space/kernel message traces where possible.

Then the archive can answer:

> **“When I type `ip route`, which parts descend from old Unix routing practice, and which parts belong to a completely different Linux control interface?”**

---

## Primary anchors

- historical BSD `route(8)` and `routed(8)` manuals;
- RFC 1058, *Routing Information Protocol*;
- BSD `route(4)` documentation identifying PF_ROUTE's 4.3BSD-Reno origin;
- Linux `rtnetlink(7)`;
- maintained `iproute2` source, especially `ip/iproute.c`.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
