# Technology Lineage

Computer networking history is not only a timeline and not only a stack.

This directory records a fourth dimension:

> **What did a technology inherit, revise, reject, standardize, replace, or leave behind in later systems?**

A timeline can tell us that RS-232-A followed RS-232. A stack reconstruction can tell us that a terminal connected to a modem through a DTE/DCE boundary. A lineage record should additionally tell us which conventions survived into later serial interfaces, which electrical choices disappeared, and which later standards formalized or redistributed the same responsibilities.

The goal is not to draw attractive family trees. It is to build an **evidence-bearing graph of technical descent and transformation**.

## Why lineage belongs in an archaeology repository

Modern networking is full of living fossils:

- DTE/DCE terminology outlived the modem environment that made it ordinary;
- asynchronous serial control circuits survived in terminal, modem, console and router practice;
- ALOHA's shared-medium contention work sits in the ancestry of experimental Ethernet;
- experimental Ethernet was revised into 10 Mbit/s Ethernet, then standardized and later transformed by bridges and switches;
- the ARPANET IMP, Internet gateway and later router occupy related but non-identical engineering roles;
- packet switching did not erase telephone infrastructure — it repeatedly reused leased lines, modems, carrier multiplexers and operations practice;
- store-and-forward systems such as UUCP disappeared from ordinary Internet transport while queueing, retry and asynchronous delivery remain everywhere.

A useful archive should therefore answer not only **what existed?** but also:

- what was inherited;
- what was discarded;
- what changed layer;
- what became a formal standard;
- what survived under a different name;
- what coexisted rather than replaced one another;
- which alleged influences are actually documented.

## Relationship classes

Lineage edges use a deliberately constrained vocabulary.

### Strong documentary relations

These normally require a specification, revision notice, standards record, implementation documentation, or other direct evidence.

- `revision-of` — a formally identifiable revision of the same standard/protocol/product.
- `successor-of` — the later object was explicitly positioned as a successor.
- `replaced-by` — documentation or operational evidence shows an actual replacement.
- `standardizes` — a standard formalizes a pre-existing technique/interface/practice.
- `derived-from` — the later design explicitly derives implementation or design material from the earlier one.
- `splits-into` — one protocol/system is deliberately divided into separately identifiable successors.
- `merges-into` — multiple objects are deliberately consolidated.

### Architectural survival relations

These require evidence that a mechanism or responsibility survived, not merely that the later object looks similar.

- `survives-as` — a concrete mechanism/convention remains recognizable in the later system.
- `role-descends-into` — an operational role evolves into a later equipment/software role even when implementation is replaced.
- `interface-convention-inherited-by` — signal naming, boundary conventions, connector roles, or other interface concepts are carried forward.
- `operational-practice-inherited-by` — monitoring, maintenance, queueing, provisioning or troubleshooting practice persists into a later environment.

### Influence relations

These are the most dangerous edges.

- `influenced` — use only when documentary evidence, citation, participant testimony, or design records support influence.
- `possibly-influenced` — a plausible relationship worth investigating, but not sufficiently established.

**Similarity is not influence. Chronological priority is not influence.**

When possible, record the stronger evidence form instead:

> paper B cites report A

is better than

> A influenced B.

## Coexistence matters

Technical history is not a single elimination tournament.

Useful relations also include:

- `coexisted-with`
- `carried-over`
- `encapsulated-over`
- `gatewayed-to`
- `interworked-with`

For example, TCP/IP and X.25 cannot be represented honestly by a simple winner/loser arrow because IP was actually carried over X.25 in deployed networks.

## Edge evidence

Every mature lineage edge should contain:

1. source object and target object;
2. relationship type;
3. date or date range when the relationship matters;
4. scope — physical, interface, link, routing, transport, application, operations, institutional, etc.;
5. the **specific inherited/rejected property**;
6. source identifier;
7. page/section/figure/paragraph locator;
8. certainty;
9. notes explaining what the edge does **not** claim.

The machine-readable schema lives at [`../schema/lineage-edge.schema.json`](../schema/lineage-edge.schema.json).

The discovery queue lives at [`../data/lineage-ledger.csv`](../data/lineage-ledger.csv).

## A lineage is usually a braid, not a tree

Do not force histories into one parent → one child chains.

A useful diagram may look like:

```text
telegraph / teleprinter practice
       \          /
        \        /
      early data sets
            |
       DTE/DCE boundary
        /         \
   EIA RS-232    CCITT V.24/V.28 family
        \         /
         \       /
      terminals + modems
             |
       serial host access
             |
      terminal servers / router consoles
```

Likewise Ethernet has multiple simultaneous genealogies:

- shared-medium access;
- frame format;
- transceiver/medium attachment;
- addressing;
- bridging/switching;
- standards governance.

They should not be flattened into one arrow.

## Extinction and survival

Lineage records should explicitly ask two questions.

### What died?

Examples:

- a voltage convention;
- a physical connector;
- collision domains in ordinary switched Ethernet;
- a routing protocol;
- a carrier tariff/service;
- a product-specific host interface.

### What survived?

Examples:

- terminology;
- address semantics;
- end-system responsibility;
- framing ideas;
- operational procedures;
- queueing behavior;
- software APIs;
- cultural expectations about interoperability.

This makes it possible to describe modern networking as a **running archaeological site** rather than merely the endpoint of a chronology.

## Research rule

For every major artifact, future excavation should eventually include a **lineage section** answering:

- What did this object inherit?
- What did it deliberately reject?
- What replaced it physically?
- What replaced it logically?
- Which pieces survived under another name?
- Which later systems explicitly cite or derive from it?
- Which alleged descendants are only retrospective analogy?

The archive is mature when those answers can be queried across thousands of artifacts instead of reconstructed manually from prose.