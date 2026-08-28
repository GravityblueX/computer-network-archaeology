# Technology Lineage Catalog

This catalog is the human-readable index of technical genealogies tracked by the archive.

It is intentionally different from the chronological timeline.

A lineage asks:

> Which exact property, role, interface convention, protocol responsibility, or operational practice moved from one historical object into another?

Machine-readable discovery edges live in [`../data/lineage-ledger.csv`](../data/lineage-ledger.csv). Mature edges live in `../records/lineages/`.

---

## Status vocabulary

- **seed** — plausible lineage saved; evidence chain incomplete.
- **priority** — important relationship selected for excavation.
- **started** — at least one direct/strong source supports the edge.
- **substantial** — multiple property-level edges and revision records exist.
- **mature** — formal revisions, implementation/deployment evidence, exclusions and open questions are all developed.

---

# 1. Terminal / modem / serial-interface lineage

## Core chain

```text
teleprinter / business-machine communication practice
                ↓
Bell data sets / modem boundaries
                ↓
DTE ↔ communication-equipment interoperability problem
                ↓
EIA RS-232 (1960)
                ↓
RS-232-A (1963)
                ↓
RS-232-B (1965)
                ↓
RS-232-C (1969)
                ↓
serial terminals / modems / computer ports / console ports
```

Parallel/related international family:

```text
CCITT V.24 / V.28 / connector standards
```

### Current state: **started**

Already documented:

- formal RS-232 revision dates;
- RS-232-A → Bell 202C/202D explicit implementation edge;
- Bell 101/103 source conflict;
- 103A contemporary existence by 1962;
- 103A BSP date conflict;
- V.24 kept separate from RS-232 identity claims.

Deep excavation:

[`../docs/lineage/bell-data-set-rs232-v24.md`](../docs/lineage/bell-data-set-rs232-v24.md)

### Next work

- recover original RS-232, A, B, C standards;
- field-by-field revision diff;
- recover EIA committee/working-group history;
- recover earliest V.24/V.28 revisions;
- build 101A/B/C, 103A1/A2/F/etc. product tree;
- trace DB-25 and circuit/pin standardization separately;
- trace router/terminal-server console-port afterlife.

---

# 2. Shared-medium access lineage

## Core chain

```text
ALOHA shared radio channel
          ↓ documented influence
Xerox experimental Ethernet
          ↓
10 Mbit/s Ethernet families
          ↓
shared coax / repeaters / hubs
          ↓
bridges / switches
          ↓
full-duplex switched Ethernet
```

### Current state: **started**

Already documented:

- ALOHAnet radio/TCU path;
- Pure/Slotted ALOHA as distinct objects;
- 2.94 Mbit/s Xerox experimental Ethernet;
- experimental transceiver/coax/interface/microcode division;
- Metcalfe/Boggs documentary influence edge.

Deep excavations:

- [`../docs/alohanet/radio-to-ethernet.md`](../docs/alohanet/radio-to-ethernet.md)
- [`../docs/ethernet/xerox-alto-2-94mbps-pup-stack.md`](../docs/ethernet/xerox-alto-2-94mbps-pup-stack.md)
- [`../docs/ethernet/experimental-ethernet-physical-layer.md`](../docs/ethernet/experimental-ethernet-physical-layer.md)

### Next work

Split Ethernet into independent property lineages:

- medium attachment;
- transceiver/MAU;
- frame format;
- type/length semantics;
- addressing;
- collision access;
- CRC;
- DIX ↔ 802.3 standardization differences;
- bridging;
- spanning tree;
- switch architecture;
- half-duplex → full-duplex transition;
- autonegotiation.

---

# 3. Internetwork protocol layering lineage

## Core chain

```text
1974 Internet Transmission Control Program (RFC 675)
                   ↓ repeated IEN redesign
             responsibilities separate
                /                 \
        Internet Protocol       TCP transport
             ↓                     ↓
       RFC 760 / IEN 128      RFC 761 / IEN 129
             ↓                     ↓
          RFC 791                RFC 793
                \                 /
                 \               /
                  deployed TCP/IP
```

### Current state: **started**

Deep excavation:

[`../docs/lineage/tcp-ip-split-and-standardization.md`](../docs/lineage/tcp-ip-split-and-standardization.md)

Already recorded:

- RFC 675 integrated Transmission Control Program;
- RFC 760 IP IEN replacement list;
- RFC 761 TCP IEN replacement list;
- RFC 791/793 successor relationship;
- best-effort responsibility on IP side;
- reliable host-to-host responsibility on TCP side;
- NCP → dual-protocol → TCP/IP operational migration.

### Next work

- acquire every cited IEN;
- version-level header diff;
- recover early TCP/IP source implementations;
- map source-code compatibility to document versions;
- trace UDP/ICMP branching;
- trace sockets/API lineage separately from wire protocols;
- add congestion-control lineage as a later branch rather than back-projecting it into early TCP.

---

# 4. ARPANET host/network boundary lineage

## Core chain

```text
site-specific host channel
        ↓
Host–IMP / 1822 boundary
        ↓
Local / Distant / Very Distant Host variants
        ↓
network-specific gateway interfaces
        ↓
later standardized router link interfaces
```

### Current state: **started**

Deep excavations:

- [`../docs/arpanet/1969-host-imp-stack.md`](../docs/arpanet/1969-host-imp-stack.md)
- [`../docs/arpanet/ucla-1969-node-bom.md`](../docs/arpanet/ucla-1969-node-bom.md)
- [`../docs/arpanet/bbn-1822-physical-interface.md`](../docs/arpanet/bbn-1822-physical-interface.md)
- Bell 303 / VDH physical excavations.

### Next work

- Report 1822 revision diff;
- Mike Wingfield UCLA interface schematics;
- SRI/UCSB/Utah host-interface implementations;
- 1822 interface boards in later BBN gateways;
- map what disappeared with ARPANET-specific hardware and what survived as the generalized host/router link-interface concept.

---

# 5. Packet switch / gateway / router role lineage

## Core role map

```text
packet switch inside one network
  IMP / CIGALE / commercial packet switch

                ≠

internetwork gateway
  heterogeneous-network IP forwarding
                ↓ role/terminology evolution
              router
```

### Current state: **started**

Deep excavation:

[`../docs/internetworking/bbn-gateway-to-router.md`](../docs/internetworking/bbn-gateway-to-router.md)

Important rule:

**Do not make IMP → router a simple direct ancestry edge.**

The archive must distinguish:

- packet switching within one network;
- host/network boundary;
- internetwork forwarding;
- route computation;
- link interfaces;
- operations/NOC role;
- contemporary terminology.

### Next work

- gateway source-code lineages;
- GGP → EGP → interdomain-routing transitions;
- Proteon/Fuzzball/BBN/Cisco product and software genealogies;
- control-plane vs forwarding-plane separation history;
- route cache/FIB hardware evolution.

---

# 6. Virtual circuit / datagram interworking lineage

## Non-tree relationship

```text
X.25 virtual-circuit public networks
        ↕ interworked / carried
IP datagrams
```

while at the architecture level:

```text
CYCLADES / IP datagram ideas  ↔  virtual-circuit architectures
```

### Current state: **started**

Deep excavation:

[`../docs/x25/pad-public-data-network-stack.md`](../docs/x25/pad-public-data-network-stack.md)

Important evidence:

- X.3/X.28/X.29 PAD world;
- RFC 877 IP over public data networks/X.25;
- CSNET and other operational overlaps.

### Next work

- named IP-over-X.25 deployments;
- X.75 inter-network gateways;
- Frame Relay relationship (do not assume simple successor);
- ATM relationship (again, document rather than infer);
- carrier service/tariff migration.

---

# 7. Store-and-forward lineage

## Core mechanism

```text
queued telegraph/message practice
        ↓
dial-up UUCP
        ↓
Usenet/news propagation
        ↓
modern queue/retry/asynchronous-delivery patterns
```

### Current state: **seed / started mix**

The UUCP mechanisms are documented. Direct descent into particular modern systems is usually **not** yet documented.

Deep excavations:

- [`../docs/uucp/usenet-store-and-forward-world.md`](../docs/uucp/usenet-store-and-forward-world.md)
- earliest Duke/UNC physical-path excavation.

### Next work

- telegraph store-and-forward ancestry;
- UUCP g/f/t/e protocol versions;
- A/B/C News release lineage;
- NNTP transition;
- prove or reject direct influence claims on later mail/message-queue systems.

---

# 8. NSFNET backbone platform lineage

```text
56 kbit/s PDP-11/LSI-11 Fuzzballs
            ↓ replaced operationally
1.544 Mbit/s IBM RT Nodal Switching Subsystems
            ↓ replaced operationally
T3 / RS/6000-generation backbone
            ↓
commercial backbone/NAP era
```

### Current state: **started**

Deep excavations:

- [`../docs/nsfnet/fuzzball-node-internals.md`](../docs/nsfnet/fuzzball-node-internals.md)
- [`../docs/nsfnet/ibm-rt-nss-node-internals.md`](../docs/nsfnet/ibm-rt-nss-node-internals.md)

The important inherited property is the **backbone routing/forwarding role**, not a stable chassis architecture.

### Next work

- per-site Fuzzball BOM;
- per-site NSS BOM;
- software release/build genealogy;
- HELLO/SPF/EGP policy evolution;
- T3 node architecture;
- migration to commercial routing platforms.

---

# 9. Naming and directory lineage — not yet excavated

Priority chain:

```text
manual host naming
      ↓
HOSTS.TXT / NIC distribution
      ↓ scaling failure
DNS RFC 882/883
      ↓ revision
DNS RFC 1034/1035
      ↓
root/TLD operational system
```

Need to separate:

- namespace structure;
- file/distribution mechanisms;
- resolver API;
- server protocol;
- root operations;
- caching;
- administrative delegation.

Status: **priority**.

---

# 10. Routing protocol lineage — not yet excavated systematically

Candidate branches:

```text
ARPANET IMP routing algorithms
GGP
HELLO
EGP
RIP
OSPF
IS-IS
BGP-1 → BGP-2 → BGP-3 → BGP-4
```

This must not become a single chain. Interior routing, exterior routing, link-state/distance-vector mechanisms and administrative-policy routing have different genealogies.

Status: **priority**.

---

# 11. Modem speed / error-control lineage — priority

Candidate family map:

```text
Bell 101/103/202/201 families
      ↓
Bell 212 / compatible modems
      ↓
1200 / 2400 / 9600 / 14.4 / 28.8 / 33.6 / 56k generations
      ↓
V-series standardization branches

MNP error control/compression
      ↔
V.42 / V.42bis
```

Track separately:

- modulation;
- symbol rate vs bit rate;
- duplexing;
- negotiation;
- error correction;
- compression;
- automatic calling/answering;
- interface standards;
- carrier-network constraints.

Status: **priority**.

---

# 12. LAN switching lineage — priority

Candidate map:

```text
repeater
  ≠
bridge
  ↓
transparent bridge + spanning tree
  ↓
multiport bridge / Ethernet switch
  ↓
VLAN / full duplex / high-speed switching
```

Need specific product archaeology:

- DEC bridges;
- Bridge Communications;
- Kalpana EtherSwitch;
- Cisco/3Com/Bay/other early switching;
- ASIC vs CPU forwarding;
- learning tables;
- store-and-forward vs cut-through.

Status: **priority**.

---

## Completion criterion for a lineage

A lineage is not mature because a diagram looks plausible.

For each important arrow, the archive should eventually preserve:

```text
source object
   ↓
specific inherited/revised property
   ↓
target object
   ↓
source document + locator
   ↓
certainty + directness
   ↓
negative claim: what this arrow does NOT establish
```

That is the difference between a genealogy and a myth.