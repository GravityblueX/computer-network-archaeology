# From `routed` to GateD: One Unix Host Learns to Speak Several Routing Languages

## Why GateD matters

Early Unix routing often appears simple in retrospect:

```text
host/router
   ↓
routed
   ↓
RIP-like interior routing
```

But the late-1980s Internet was not one routing-protocol world.

A campus or regional gateway might need to understand:

```text
RIP
HELLO
EGP
later OSPF / BGP families
```

and translate policy/reachability between them.

GateD is therefore important not merely as “another routing daemon,” but as a transition from **one daemon tightly associated with one routing family** to a **configurable multiprotocol routing control plane on a general-purpose Unix host**.

---

## 1. The problem: several routing worlds on the same Ethernet

RFC 1118 (1989) gives an unusually vivid contemporary explanation.

It describes regional and campus networks using RIP while the DDN/NSFNET world used EGP and notes the practical problem: how do these routing systems interoperate?

The text says Mark Fedor, then at Cornell, attempted to solve the problem with a replacement for `routed` called **gated**.

GateD could speak:

```text
RIP ↔ RIP speakers
EGP ↔ EGP speakers
HELLO ↔ HELLO speakers
```

while configuration controlled which routes were accepted, translated or announced.

That is a major architectural shift:

```text
one routing daemon / one main dialect
            ↓
multiprotocol routing daemon
            ↓
policy-controlled redistribution
```

---

## 2. Static routing fails differently from dynamic routing

RFC 1118 frames GateD against a real operational problem with static routing.

If reachability is configured statically, the rest of the network may continue believing a destination is reachable after the actual path fails. Packets can then follow a stale route until applications time out.

A dynamic routing system can withdraw or change reachability.

GateD's role was therefore not just “support more protocols.” It was also to keep **routing state from different administrative/protocol domains synchronized enough to avoid persistent false reachability**.

---

## 3. Protocol translation is not literal packet translation

“GateD talks RIP, EGP and HELLO” should not be interpreted as converting one routing packet byte-for-byte into another.

The actual conceptual model is closer to:

```text
protocol-specific input
       ↓
common routing information base / internal state
       ↓
policy filters
       ↓
protocol-specific export
```

This is an ancestor of a design pattern that later became normal in routing software:

> multiple protocol processes feed a common routing decision framework, with policy controlling import and export.

The exact GateD internal data structures and version-by-version architecture remain high-priority source-code archaeology targets.

---

## 4. GateD is not simply `routed` version 2

A false lineage would be:

```text
routed → gated → modern router daemon
```

That collapses too much.

The historically supportable relationship is narrower:

- GateD was explicitly described as a **replacement for routed** in an environment where one host needed to interoperate among RIP, EGP and HELLO;
- GateD added multiprotocol and configuration/policy roles that `routed` did not represent;
- RIP itself continued separately as a standardized protocol family;
- many vendor routers implemented the same protocols without using GateD source.

So the lineage is partly **role expansion**, not a universal code ancestry.

---

## 5. GateD became a routing-protocol implementation laboratory

By the early 1990s GateD was not only operational glue; it was also a platform for trying new protocol versions.

RFC 1387 (1993), analyzing RIP Version 2, records a nearly complete RIP-2 implementation in GateD by Jeffrey Honig at Cornell and even gives the contemporary anonymous-FTP distribution path.

The listed implementation included features such as:

- multicasting;
- subnet masks;
- limited authentication;
- next-hop support;
- limited routing-domain support.

This is valuable archaeological evidence because it connects:

```text
protocol draft/specification
        ↓
real source implementation
        ↓
interoperability testing
```

before the feature set became ordinary router behavior.

---

## 6. Institutional lineage: Cornell → Merit

Merit Network's institutional history records that in 1995 Merit acquired the GateD Consortium from Cornell University and continued development of GateD as modular routing software used to interconnect packet-switched networks.

This means GateD has both a technical and organizational genealogy:

```text
Cornell GateD work
      ↓
GateD Consortium
      ↓ 1995 transfer
Merit Network
```

The archive should distinguish:

- source-code revision history;
- protocol-feature history;
- consortium/governance history;
- deployment history.

A project can survive institutionally even while individual routing protocols inside it change.

---

## 7. GateD shows why routing policy becomes first-class

Once a daemon speaks several routing protocols, “redistribute everything” is unsafe.

Different routing systems have different:

- metric meanings;
- administrative scopes;
- trust assumptions;
- topology visibility;
- loop-prevention rules;
- route-selection semantics.

Therefore GateD's configuration/filtering role is historically important.

The multiprotocol router is not merely:

```text
RIP + EGP + HELLO
```

It needs:

```text
RIP input ─┐
EGP input ─┼→ policy / preference / route selection → exports
HELLO in ──┘
```

That pattern later becomes central to BGP-era routing policy and modern routing suites, even when there is no direct source-code lineage.

---

## 8. A general-purpose Unix host becomes a serious router control plane

GateD also belongs to the history of the Unix host as routing platform.

Before routing control was universally associated with dedicated commercial routers, Unix machines could run routing software that:

- exchanged interior and exterior routes;
- installed kernel forwarding entries;
- filtered announcements;
- translated between protocol domains;
- logged and diagnosed routing state.

This connects directly to other excavations in the repository:

```text
Fuzzball
BSD routed
GateD
commercial Unix/router software
modern routing suites
```

These are not necessarily one code family, but they share the recurring architecture of **user-space routing intelligence programming a separate forwarding state**.

---

## 9. GateD and modern routing suites: do not overclaim ancestry

Modern systems such as FRRouting, BIRD and vendor routing stacks occupy a familiar role:

```text
multiple protocols
policy
RIB
kernel/FIB programming
```

That resemblance makes GateD an obvious ancestor in a broad role-genealogy sense.

But the repository should not claim:

```text
GateD source → FRRouting source
```

or any other direct code descent without explicit evidence.

A safer relation is:

```text
GateD multiprotocol routing-daemon role
      ↓ operational-practice/architecture survives in
later multiprotocol routing suites
```

with implementation ancestry investigated separately.

---

## 10. What to excavate next

High-value GateD artifacts include:

- earliest Mark Fedor source releases;
- Cornell distribution tapes/tarballs;
- versioned configuration grammar;
- RIP/HELLO/EGP protocol modules;
- OSPF/BGP additions by release;
- route preference and redistribution code;
- kernel routing-table interface on each supported Unix;
- GateD Consortium documents;
- Merit-era releases;
- build instructions and supported hardware/OS lists;
- surviving operator configuration files.

The archive should ideally reconstruct one real site:

```text
interfaces
routing protocols
GateD version
configuration
kernel routes
peer routers
policy filters
failure behavior
```

rather than treating GateD only as a software title.

---

## 11. Root-hunting conclusion

GateD demonstrates another form of technical inheritance:

> **the surviving thing is not always a packet format or API; sometimes it is an operational architecture.**

The architecture is:

```text
many routing languages
        ↓
one policy-controlled routing process/framework
        ↓
one kernel forwarding system
```

That pattern is now so normal that it is easy to forget there was a time when putting RIP, EGP and HELLO into one configurable Unix routing daemon was itself a major integration step.

---

## Primary anchors

- RFC 1118, *The Hitchhikers Guide to the Internet* — contemporary description of GateD as Mark Fedor's replacement for `routed`, speaking RIP/EGP/HELLO.
- RFC 1387, *RIP Version 2 Protocol Analysis* — contemporary GateD RIP-2 implementation evidence.
- Merit Network institutional history — 1995 acquisition of the GateD Consortium from Cornell.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
