# Interior routing is not one upgrade chain: HELLO, RIP, OSPF, and IS-IS

> **Lineage question:** how did routers inside an administrative routing domain learn paths, and why is the history a branching family tree rather than `RIP → OSPF → IS-IS`?

This is a place where simplified networking history is especially misleading.

The modern phrase **IGP — Interior Gateway Protocol** describes a role. It does not identify one ancestry.

Several fundamentally different routing traditions occupied that role.

---

## 1. First separate the role from the algorithm

After the Internet moved toward autonomous systems, a routing domain could choose its own internal routing mechanism while using a different protocol externally.

So this:

```text
inside an AS
    ↓
IGP
```

is a **role category**.

Inside that role we can have:

```text
distance-vector / Bellman-Ford family
        RIP

link-state / SPF family
        OSPF
        IS-IS

historical Internet-specific family
        HELLO

vendor/proprietary branches
        IGRP, etc.
```

Do not turn those branches into a fake linear version sequence.

---

## 2. RIP documents an existing distance-vector tradition

RFC 1058, June 1988, describes the Routing Information Protocol.

Primary source:

- RFC 1058 — https://www.rfc-editor.org/rfc/rfc1058.html

The document says it is describing an **existing protocol**.

RIP belongs to the Bellman-Ford / distance-vector tradition.

The conceptual model is:

```text
router knows a distance/metric to destinations
        ↓
shares route information with neighbors
        ↓
neighbors update their own tables
```

The famous RIP hop-count metric and finite “infinity” are implementation/design choices within this family.

The critical archaeological point is that RIP is not the beginning of routing and not the generic definition of an IGP.

---

## 3. HELLO is another Internet-era interior-routing branch

The repository already tracks the HELLO routing protocol in the Fuzzball/NSFNET context.

HELLO used delay-related metrics and was deeply associated with David Mills' Internet/NSFNET work.

Its role overlaps with what we would call an IGP, but its protocol ancestry is not simply RIP.

So:

```text
HELLO
RIP
```

should normally be modeled as **coexisting IGP approaches**, not revision ancestors.

The NSFNET excavations show how HELLO was tied to a specific router/software ecosystem and backbone generation.

This is a useful reminder:

> routing-protocol history is often inseparable from router implementation and operations history.

---

## 4. OSPF explicitly changes algorithmic family

RFC 1583's introduction states that OSPF is based on **link-state or SPF technology** and that this is a departure from the Bellman-Ford base used by traditional TCP/IP routing protocols.

Primary sources:

- RFC 1131 (1989), original OSPF specification — https://www.rfc-editor.org/rfc/rfc1131.html
- RFC 1247 (1991), OSPF Version 2 — https://www.rfc-editor.org/rfc/rfc1247.html
- RFC 1583 (1994), OSPF Version 2 revision — https://www.rfc-editor.org/rfc/rfc1583.html
- RFC 2178 (1997) — https://www.rfc-editor.org/rfc/rfc2178.html
- RFC 2328 (1998), later OSPFv2 standard — https://www.rfc-editor.org/rfc/rfc2328.html

The architectural change is therefore real:

```text
distance-vector tradition
        ≠
link-state database + SPF computation
```

But the correct edge is not necessarily:

```text
RIP → OSPF
```

OSPF is a new IGP design in a different algorithmic family, developed for the TCP/IP Internet environment.

---

## 5. Link-state routing changes what every router knows

A simplified distance-vector mental model:

```text
neighbor tells me:
"destination X is N units away"
```

A simplified link-state model:

```text
routers distribute descriptions of topology links
        ↓
each router builds a topology database
        ↓
each router computes shortest paths locally
```

That means the inherited routing **role** is similar — choose next hops inside a domain — but the state representation, information distribution, convergence behavior, and computation architecture differ sharply.

This is a classic `role-descends-into` versus `revision-of` distinction.

---

## 6. OSPF itself has a formal revision genealogy

Within OSPF, unlike between RIP and OSPF, formal version edges are appropriate.

```text
RFC 1131 OSPF
     ↓ obsoleted by
RFC 1247 OSPF Version 2
     ↓ obsoleted by
RFC 1583 OSPF Version 2
     ↓
RFC 2178
     ↓
RFC 2328
```

This is a true standards revision line.

The archive should eventually diff:

- packet formats;
- LSA types;
- area behavior;
- external route handling;
- virtual links;
- authentication;
- CIDR support;
- flooding rules;
- routing table computation.

---

## 7. IS-IS comes from a different standards universe

IS-IS is the clearest warning against writing Internet routing history as if every useful protocol originated inside TCP/IP.

RFC 1195, December 1990, specifies the use of **OSI IS-IS** for routing in TCP/IP and dual IP/OSI environments.

Primary sources:

- RFC 1142 — OSI IS-IS Intra-domain Routing Protocol — https://www.rfc-editor.org/rfc/rfc1142.html
- RFC 1195 — Use of OSI IS-IS for routing in TCP/IP and dual environments — https://www.rfc-editor.org/rfc/rfc1195.html

RFC 1195 says explicitly that the integrated protocol is based on the OSI Intra-domain IS-IS routing protocol with IP-specific functions added.

So this edge **is** documentary:

```text
OSI IS-IS
    ↓ extended for
Integrated IS-IS supporting IP
```

This is not an OSPF revision and not a RIP descendant.

---

## 8. OSPF and IS-IS are parallel link-state families

Both use SPF/Dijkstra-style link-state approaches, but similarity does not establish ancestry.

They come from different specification histories:

```text
IETF / TCP-IP OSPF branch

ISO/OSI IS-IS branch
       ↓
RFC 1195 integrated IP support
```

They later coexist as major IGP choices.

This should be encoded as:

- shared algorithmic family / comparable role;
- coexistence;
- documented cross-references where present;

not as a simple `OSPF → IS-IS` or `IS-IS → OSPF` edge without evidence.

---

## 9. IS-IS brings OSI architecture into IP routing

RFC 1195 describes integrated IS-IS as one protocol capable of supporting:

- pure IP environments;
- pure OSI environments;
- dual environments.

It also preserves IS-IS concepts such as:

- routing domains;
- two-level hierarchy;
- areas;
- Level 1 and Level 2 routing;
- link-state packets;
- pseudonodes on broadcast LANs;
- designated-router-like LAN behavior.

This is a strong example of a protocol family crossing institutional ecosystems rather than being “replaced” by the winning Internet suite.

---

## 10. The ‘Ships in the Night’ alternative is itself historical evidence

RFC 1195 explicitly discusses an alternative called **Ships in the Night**:

```text
one protocol routes IP
another protocol routes OSI
both operate independently on the same routers/network
```

Integrated IS-IS instead attempts to use one routing protocol to support both.

This matters because protocol coexistence was not accidental clutter.

It was an explicit design choice administrators and standards engineers had to make.

---

## 11. Modern IGP choice preserves these old branches

A modern operator can encounter:

```text
OSPF
IS-IS
RIP (legacy/small systems)
```

Those names are not just modern configuration options.

They represent different historical answers to:

> What information should routers exchange inside one routing domain, and what should each router compute locally?

This is why a router configuration syntax can itself be read archaeologically.

---

## 12. A better lineage graph

Instead of:

```text
RIP → OSPF → IS-IS
```

use something more like:

```text
                 interior-routing role
                  /      |       \
                 /       |        \
   distance-vector     HELLO    link-state/SPF
         |                         /       \
        RIP                      OSPF     OSI IS-IS
                                           |
                                           ↓
                                 Integrated IS-IS for IP
```

And separately:

```text
OSPF RFC 1131
     ↓
RFC 1247
     ↓
RFC 1583
     ↓
RFC 2178
     ↓
RFC 2328
```

That distinguishes **family relationship** from **formal standard revision**.

---

## 13. Sources

Primary/reference sources:

- RFC 1058, *Routing Information Protocol* — https://www.rfc-editor.org/rfc/rfc1058.html
- RFC 1131, *OSPF specification* — https://www.rfc-editor.org/rfc/rfc1131.html
- RFC 1247, *OSPF Version 2* — https://www.rfc-editor.org/rfc/rfc1247.html
- RFC 1583, *OSPF Version 2* — https://www.rfc-editor.org/rfc/rfc1583.html
- RFC 2178, *OSPF Version 2* — https://www.rfc-editor.org/rfc/rfc2178.html
- RFC 2328, *OSPF Version 2* — https://www.rfc-editor.org/rfc/rfc2328.html
- RFC 1142, *OSI IS-IS Intra-domain Routing Protocol* — https://www.rfc-editor.org/rfc/rfc1142.html
- RFC 1195, *Use of OSI IS-IS for routing in TCP/IP and dual environments* — https://www.rfc-editor.org/rfc/rfc1195.html
- existing repository sources on HELLO/Fuzzball/NSFNET.

---

## 14. Next excavation layer

1. RIP ancestry before RFC 1058 — Xerox PUP/XNS/Unix `routed` connections and what can actually be documented;
2. RIP-1 → RIP-2 RFC 1388/1723 revision diff;
3. HELLO packet/source-code archaeology in Fuzzball;
4. OSPF Working Group design notes and earliest implementations;
5. RFC 1131 → 1247 → 1583 → 2178 → 2328 structured diff;
6. Proteon/Cisco/Gated OSPF implementation history;
7. ISO 10589 edition history for IS-IS;
8. RFC 1142 provenance and relationship to ISO text;
9. RFC 1195 integrated IS-IS implementation history;
10. early IS-IS-for-IP vendor deployments;
11. OSPF versus IS-IS operational comparisons from contemporary operator sources;
12. later extensions such as OSPFv3 and wide-metric/multi-topology IS-IS as separate branches.

---

## Conclusion

The history of interior routing is not a ladder where every new protocol replaces the previous rung.

It is a branching ecosystem:

> **same operational role, different algorithmic families, different standards institutions, different implementation histories.**

That distinction is exactly what a technical genealogy should preserve.