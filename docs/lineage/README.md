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

### Terminal, remote-access and AAA edges

- [`terminal-access-tip-pad-terminal-server-portmaster.md`](terminal-access-tip-pad-terminal-server-portmaster.md) — BBN TIP, X.25 PAD, DECserver/LAT, Cisco communications servers and Livingston PortMaster as a recurring edge-access role rather than a false single product ancestry.
- [`portmaster-radius-aaa.md`](portmaster-radius-aaa.md) — PortMaster modem-pool/access-server administration → Livingston RADIUS → RFC 2058/2138/2865, with Accounting as a sibling branch and later AAA uses kept separate from the original dial-access problem.
- [`slip-to-ppp-point-to-point-links.md`](slip-to-ppp-point-to-point-links.md) — minimal IP-over-serial SLIP beside a growing PPP architecture with framing, LCP, NCPs, authentication and negotiated point-to-point links; direct causal ancestry is deliberately not asserted without evidence.

### Host bootstrap and configuration

- [`rarp-bootp-dhcp-host-configuration.md`](rarp-bootp-dhcp-host-configuration.md) — hardware-address bootstrap with RARP → routed BOOTP client/server bootstrap → DHCP reusable address leases and host-configuration state.

### Internet protocol layering

- [`tcp-ip-split-and-standardization.md`](tcp-ip-split-and-standardization.md) — the integrated early Transmission Control Program splitting into IP and TCP responsibilities.

### Naming

- [`hosts-txt-to-dns.md`](hosts-txt-to-dns.md) — central HOSTS.TXT maintenance → hierarchical naming → delegated DNS.

### Interior routing families

- [`igp-families-rip-hello-ospf-isis.md`](igp-families-rip-hello-ospf-isis.md) — HELLO, RIP, OSPF and IS-IS as parallel IGP families: distance-vector, Internet-specific and link-state branches, including OSI IS-IS entering IP through RFC 1195 rather than a false `RIP → OSPF → IS-IS` ladder.

### Interdomain routing

- [`ggp-egp-bgp-routing-domains.md`](ggp-egp-bgp-routing-domains.md) — common smart-gateway routing → autonomous systems → EGP → BGP.
- [`bgp-1-to-bgp-4.md`](bgp-1-to-bgp-4.md) — the formal BGP-1/2/3/4 revision chain and CIDR intersection.

### Network management

- [`hmp-sgmp-snmp-management.md`](hmp-sgmp-snmp-management.md) — early gateway/host monitoring → SGMP → SNMP → SNMPv2/v3 management frameworks.

## How to read an arrow

An arrow must name the property that crosses the historical boundary.

For example:

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

Modem history needs another relation:

```text
MNP installed base
    └── interworked-with ──> V.42-era modem implementations
```

Terminal-access history adds another warning:

```text
TIP  ↔  PAD  ↔  terminal server
```

may describe a recurring role, but without documentary design links it must **not** be rewritten as:

```text
TIP → PAD → terminal server
```

The new IGP excavation makes the same point:

```text
RIP   OSPF   IS-IS
```

are protocols that can occupy the same interior-routing role, but shared role is not a revision chain.

And DHCP provides the opposite case — a genuinely documented derivation:

```text
BOOTP
  └── explicitly extended by ──> DHCP
```

RFC 1531 says DHCP is based on BOOTP, preserves BOOTP relay behavior and adds reusable address allocation/configuration.

A good lineage records both survival and death, and it records the *kind* of survival.

## Relationship strengths

The preferred evidence ladder is:

1. **formal revision/supersession** — a standard or RFC explicitly replaces another;
2. **documented derivation/design ancestry** — the descendant specification explicitly says it is based on or extends prior work;
3. **documented operational transition/interworking** — deployment records show replacement or coexistence;
4. **de-facto interface inheritance** — compatible products/software demonstrably depend on an earlier product interface;
5. **role genealogy** — the same infrastructure responsibility expands or migrates across product categories, with direct product ancestry explicitly excluded when unknown;
6. **participant testimony** — later recollection by engineers/operators;
7. **scholarly reconstruction** — strong historical analysis connecting sources;
8. **hypothesis** — saved lead, not yet a fact.

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

### Same name, mechanism disappears

```text
shared-medium Ethernet
    ↓
hub Ethernet
    ↓
switched full-duplex Ethernet
```

### Wire incompatibility, architecture survives

```text
SGMP
   ↓ incompatible syntax
SNMP
```

### One responsibility splits into layers

```text
early integrated Transmission Control Program
            ↓
          IP + TCP
```

### A narrow bootstrap role grows into configuration-state management

```text
RARP: hardware address → protocol address
             ↓ broader bootstrap
BOOTP: routed client/server boot configuration
             ↓ explicit derivation + lease model
DHCP: reusable address + complete host configuration
```

### Same remote-access environment, different protocol ambition

```text
SLIP: delimit IP packets on serial bytes
PPP: negotiate a multi-protocol point-to-point link
```

The archive currently records operational coexistence and role expansion, not an unsupported formal `SLIP → PPP` revision claim.

### Parallel routing families under one IGP role

```text
             IGP role
        /       |        \
      RIP     HELLO    link-state/SPF
                        /       \
                     OSPF     OSI IS-IS
                                  ↓ documented derivation
                         Integrated IS-IS for IP
```

### Standardization preserves compatibility rather than erasing the old protocol

```text
MNP error-control installed base
          ↕ compatibility
V.42 LAPM-era modem ecosystem
```

### A product interface becomes an ecosystem convention

```text
Hayes Smartmodem command interpreter
          ↓
Hayes AT command family
          ↓ software dependency + compatible competitors
Hayes-compatible modem ecosystem
```

### Logical topology separates from physical topology

```text
physical redundant LAN
      ↓ bridge/STP
logical loop-free topology
      ↓ multiport switching
virtual bridged LAN / VLAN
```

### Edge role survives while endpoint intelligence moves

```text
dumb terminal → TIP/PAD/terminal server → remote host service
```

becomes, in another branch:

```text
PC with IP stack → PPP → access server → routed Internet
```

### A product deployment problem creates a protocol

```text
PortMaster / modem-pool administration
          ↓ documented origin
RADIUS centralized NAS authentication/configuration
          ↓ formal RFC revisions
RADIUS core + Accounting sibling branch
```

### Technology changes because infrastructure below it changed

```text
analogue voiceband modem assumptions
          ↓ PSTN digitization
V.90 digital-provider / analogue-subscriber modem pair
```

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

## Current structured examples

Representative claim-level edges now include:

- `LIN-0034` — BGP-3 → BGP-4 formal revision intersecting CIDR;
- `LIN-0057` — SGMP → SNMP architectural continuity despite incompatible wire syntax;
- `LIN-0062` — Perlman distributed spanning-tree design → IEEE bridge/STP lineage;
- `LIN-0068` — MNP installed base ↔ V.42 compatibility/interworking;
- `LIN-0075` — Hayes AT command convention → third-party Hayes-compatible modem interfaces;
- `LIN-0079` — terminal-server edge role → authenticated dial-IP access-server role without claiming vendor/source-code ancestry;
- `LIN-0081` — Livingston PortMaster environment → RADIUS documented product/protocol origin;
- `LIN-0085` — RARP → BOOTP bootstrap-role generalization with formal obsolescence explicitly excluded;
- `LIN-0086` — BOOTP → DHCP documented derivation;
- `LIN-0087` — SLIP ↔ PPP deployed coexistence without invented direct ancestry;
- `LIN-0088` — OSI IS-IS → Integrated IS-IS direct derivation;
- `LIN-0089` / `LIN-0090` — negative-lineage records preventing RIP/OSPF/IS-IS from being flattened into a fake upgrade chain.

Structured artifacts now also include RARP, BOOTP, DHCP/RFC2131, SLIP, PPP/RFC1661, RIP/RFC1058, OSPFv2/RFC1583, OSI IS-IS and Integrated IS-IS.

## Next lineage excavations

The next layer should move below the current summaries:

- **DHCP:** RFC 951→1542 BOOTP relay changes, RFC 1531→1541→2131 state-machine diff, options, early server/client source, lease-file formats;
- **PPP:** RFC 1134→1171→1331→1548→1661 diff, RFC 1549→1662 framing branch, PAP/CHAP/IPCP, CSLIP, Multilink and early access-server implementations;
- **IGPs:** RIP prehistory/RIP-2, HELLO source, OSPF RFC revision chain and first implementations, ISO 10589/IS-IS edition history and early Integrated IS-IS deployments;
- **RADIUS:** pre-RFC Livingston implementation, ComOS client/server behavior, UDP 1645/1646→1812/1813, Accounting RFC 2059→2139→2866, then later 802.1X/EAP uses only with direct evidence;
- **TIP:** processor/terminal scanner boards, port buffers, modem lines, user command software, named deployed sites;
- **PAD:** actual Tymnet/Telenet/Transpac/DATAPAC PAD products and user command sets;
- **DECserver/LAT:** DECserver 100 BOM/firmware/downline loading, LAT service advertisements/session setup/load balancing;
- **access servers:** Cisco STS/MSM/ASM/500-CS and Livingston PortMaster/ComOS hardware/software genealogy;
- **bridge/STP:** DEC LANbridge 100 PDU/timer/state machine, IEEE 802.1D diffs, RSTP/MSTP;
- **switching/VLAN:** Kalpana EtherSwitch BOM/ASIC history, 802.1Q tag/membership details, vendor VLAN predecessors;
- **MNP/V.42:** original Microcom specs, LAPM state machine, negotiation traces, MNP5 vs V.42bis;
- **Hayes:** first Smartmodem manuals, S-register diffs, UUCP/BBS/SLIP/PPP modem drivers, formal ETSI/3GPP AT ancestry;
- **Ethernet:** autonegotiation and high-speed PHY lineage;
- **SNMP:** HMP implementation → SGMP source → first SNMP agents; SMI/MIB genealogy;
- **applications:** NCP Telnet/FTP/mail → TCP-era application protocol revisions;
- **DNS:** host tables → Jeeves/BIND server implementations.

## Completion criterion

A lineage becomes useful when it can answer:

- What exact property moved?
- What exact property did **not** move?
- Was this a formal revision, documented derivation, operational replacement, influence, coexistence, compatibility layer, role migration, or only analogy?
- Which source proves the relationship?
- At what date/revision did the change occur?
- Which implementation first demonstrated it?
- Which part survives in modern systems?
- Which part is now extinct?

The goal is not to prove that everything has one ancestor.

The goal is to make visible the dense network of **inheritance, competition, coexistence, redesign and forgetting** underneath modern networking.
