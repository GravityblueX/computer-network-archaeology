# Lineage Excavations

This directory asks a different question from the main timeline:

> **What did this technology inherit, revise, reject, split, standardize, or carry forward?**

The archive treats lineage as evidence-bearing relationships, not as a decorative family tree. A plausible resemblance is not enough to claim ancestry.

Machine-readable edges live in [`../../data/lineage-ledger.csv`](../../data/lineage-ledger.csv), with mature claim-level records in [`../../records/lineages/`](../../records/lineages/).

## Current deep excavations

### Foundations

- [`standards-genealogy.md`](standards-genealogy.md) — why networking history should be reconstructed as overlapping genealogies rather than one progress timeline.

### Serial interfaces and modems

- [`bell-data-set-rs232-v24.md`](bell-data-set-rs232-v24.md) — Bell data sets, DTE/DCE, RS-232 and V.24/V.28 boundaries.
- [`bell-modems-to-itu-v-series.md`](bell-modems-to-itu-v-series.md) — Bell-era modem practice, V.21/V.22/V.32/V.34/V.90 generations, and why a modem speed ladder is not enough.
- [`mnp-v42-v42bis.md`](mnp-v42-v42bis.md) — MNP error-control/compression families, V.42 LAPM, compatibility fallback, V.42bis compression, and the modem becoming a protocol engine.
- [`hayes-at-command-set.md`](hayes-at-command-set.md) — Smartmodem command/data modes, `AT` commands, S-registers, result codes, escape sequences, and de-facto Hayes compatibility.

### Ethernet, bridging and virtual LANs

- [`ethernet-shared-medium-to-switched.md`](ethernet-shared-medium-to-switched.md) — 2.94 Mb/s PARC Ethernet → DIX → IEEE 802.3 → 10BASE-T → bridge/switch → full-duplex Ethernet.
- [`bridge-stp-switch-vlan.md`](bridge-stp-switch-vlan.md) — transparent bridges → distributed spanning tree → IEEE 802.1D → multiport switching → IEEE 802.1Q virtual bridged LANs.

### Internet protocol layering

- [`tcp-ip-split-and-standardization.md`](tcp-ip-split-and-standardization.md) — the integrated early Transmission Control Program splitting into IP and TCP responsibilities.

### Naming

- [`hosts-txt-to-dns.md`](hosts-txt-to-dns.md) — central HOSTS.TXT maintenance → hierarchical naming → delegated DNS.

### Interdomain routing

- [`ggp-egp-bgp-routing-domains.md`](ggp-egp-bgp-routing-domains.md) — common smart-gateway routing → autonomous systems → EGP → BGP.
- [`bgp-1-to-bgp-4.md`](bgp-1-to-bgp-4.md) — the formal BGP-1/2/3/4 revision chain and CIDR intersection.

### Network management

- [`hmp-sgmp-snmp-management.md`](hmp-sgmp-snmp-management.md) — early gateway/host monitoring → SGMP → SNMP → SNMPv2/v3 management frameworks.

## How to read an arrow

An arrow must name the property that crosses the historical boundary.

For example:

```text
SGMP ──survives-as──> SNMP
```

is too vague by itself.

The actual claim is:

```text
SGMP simple-agent / remote-manager architecture
    └── survives-as ──> SNMP management architecture
```

while separately:

```text
SGMP wire syntax
    └── NOT backward-compatible with SNMP
```

Likewise:

```text
Ethernet shared-medium frame/MAC lineage
    └── survives-as ──> switched full-duplex Ethernet
```

but:

```text
CSMA/CD collision arbitration
    └── no longer normally operates on full-duplex point-to-point links
```

And modem history needs yet another relation:

```text
MNP installed base
    └── interworked-with ──> V.42-era modem implementations
```

This is **not** a formal `revision-of` edge. LAPM is the standardized V.42 procedure while MNP compatibility survives because deployed equipment and software already exist.

A good lineage records both survival and death, and it records the *kind* of survival.

## Relationship strengths

The preferred evidence ladder is:

1. **formal revision/supersession** — a standard or RFC explicitly replaces another;
2. **documented design ancestry** — designers/specifications explicitly cite prior work;
3. **documented operational transition/interworking** — deployment records show replacement or coexistence;
4. **de-facto interface inheritance** — compatible products/software demonstrably depend on an earlier product interface;
5. **participant testimony** — later recollection by engineers/operators;
6. **scholarly reconstruction** — strong historical analysis connecting sources;
7. **hypothesis** — saved lead, not yet a fact.

The repository deliberately keeps `possibly-influenced`, `coexisted-with`, `interworked-with`, and disputed edges rather than making a clean but false tree.

## Lineages already showing important historical patterns

### Same role, different machinery

```text
Fuzzball router
   ↓ replaced operationally
IBM RT Nodal Switching Subsystem
   ↓
T3/RS-6000 backbone
```

The backbone role persists while implementation architecture changes radically.

### Same name, mechanism disappears

```text
shared-medium Ethernet
    ↓
hub Ethernet
    ↓
switched full-duplex Ethernet
```

The name and frame lineage persist while collision arbitration largely disappears.

### Wire incompatibility, architecture survives

```text
SGMP
   ↓ incompatible syntax
SNMP
```

but the management philosophy and manager/agent architecture are explicitly carried forward.

### One responsibility splits into layers

```text
early integrated Transmission Control Program
            ↓
          IP + TCP
```

Layering itself has a history.

### Standardization preserves compatibility rather than erasing the old protocol

```text
MNP error-control installed base
          ↕ compatibility
V.42 LAPM-era modem ecosystem
```

A formal standard can arrive while the previous de-facto protocol remains operationally necessary.

### A product interface becomes an ecosystem convention

```text
Hayes Smartmodem command interpreter
          ↓
Hayes AT command family
          ↓ software dependency + compatible competitors
Hayes-compatible modem ecosystem
```

This is de-facto standardization, not standards-body revision.

### Logical topology separates from physical topology

```text
physical redundant LAN
      ↓ bridge/STP
logical loop-free topology
      ↓ multiport switching
virtual bridged LAN / VLAN
```

A modern switch inherits bridge semantics while the physical implementation changes completely.

### Technology changes because the infrastructure below it changed

```text
analogue voiceband modem assumptions
          ↓ PSTN digitization
V.90 digital-provider / analogue-subscriber modem pair
```

The device standard changes because the carrier network underneath it changed.

### Technical architecture follows institutional boundaries

```text
one common gateway-routing regime
          ↓ scaling / operations problem
autonomous systems
          ↓
IGP inside / EGP outside
          ↓
BGP interdomain policy routing
```

An administrative abstraction becomes part of protocol architecture.

## Current structured examples

The lineage system is not only prose. Representative claim-level edges now include:

- `LIN-0034` — BGP-3 → BGP-4 formal revision intersecting CIDR;
- `LIN-0057` — SGMP → SNMP architectural continuity despite incompatible wire syntax;
- `LIN-0062` — Perlman distributed spanning-tree design → IEEE bridge/STP lineage;
- `LIN-0068` — MNP installed base ↔ V.42 compatibility/interworking;
- `LIN-0075` — Hayes AT command convention → third-party Hayes-compatible modem interfaces.

Representative structured artifacts now include IEEE 802.1D-1990, V.42-1988, and the Hayes AT command-set family.

## Next lineage excavations

The next layer should move below the current summaries:

- **bridge/STP:** DEC LANbridge 100 manuals, exact PDU/timer/state-machine differences, IEEE 802.1D edition diffs, RSTP/MSTP;
- **switching/VLAN:** Kalpana EtherSwitch model/BOM/ASIC history, store-and-forward vs cut-through, 802.1Q tag and membership details, vendor VLAN predecessors;
- **MNP/V.42:** original Microcom MNP specs, LAPM state machine, real negotiation traces, MNP5 vs V.42bis algorithm comparison;
- **Hayes:** first Smartmodem manuals, early command grammar, S-register diffs, UUCP dialers, BBS modem drivers, SLIP/PPP chat scripts, formal ETSI/3GPP AT-command ancestry;
- **Ethernet:** autonegotiation and high-speed PHY lineage;
- **SNMP:** HMP implementation → SGMP source → first SNMP agents; SMI/MIB revision genealogy;
- **routing:** GGP source → EGP deployment → BGP-1 source; HELLO/RIP/OSPF/IS-IS as separate IGP families;
- **applications:** NCP Telnet/FTP/mail → TCP-era application protocol revisions;
- **DNS:** ARPANET host tables → DNS server implementations (Jeeves/BIND);
- **remote access:** terminal concentrator → PAD → terminal server → dial access server;
- **management/configuration:** bridge/router management → SNMP → later configuration/telemetry systems, with direct influence claims treated cautiously.

## Completion criterion

A lineage becomes useful when it can answer:

- What exact property moved?
- What exact property did **not** move?
- Was this a formal revision, operational replacement, influence, coexistence, compatibility layer, or only analogy?
- Which source proves the relationship?
- At what date/revision did the change occur?
- Which implementation first demonstrated it?
- Which part survives in modern systems?
- Which part is now extinct?

The goal is not to prove that everything has one ancestor.

The goal is to make visible the dense network of **inheritance, competition, coexistence, redesign and forgetting** underneath modern networking.
