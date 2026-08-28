# Technology Lineage Catalog

This catalog is the human-readable index of technical genealogies tracked by the archive.

A timeline asks **when**. A stack reconstruction asks **how the pieces were connected at one moment**. A lineage asks:

> Which exact property, role, interface convention, protocol responsibility, operational practice, or institutional boundary moved from one historical object into another?

Machine-readable discovery edges live in [`../data/lineage-ledger.csv`](../data/lineage-ledger.csv). Mature edges live in `../records/lineages/`.

## Status vocabulary

- **seed** — plausible lineage saved; evidence incomplete.
- **priority** — important relationship selected for excavation.
- **started** — at least one strong/direct source supports the edge.
- **substantial** — multiple property-level edges and revision records exist.
- **mature** — formal revisions, implementation/deployment evidence, exclusions, and open questions are all developed.

A plausible-looking arrow is not evidence. Similarity alone does not establish ancestry.

---

# 1. Terminal / modem / serial-interface lineage

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

### Current state: **substantial**

Deep excavation:

- [`../docs/lineage/bell-data-set-rs232-v24.md`](../docs/lineage/bell-data-set-rs232-v24.md)
- [`../docs/lineage/bell-modems-to-itu-v-series.md`](../docs/lineage/bell-modems-to-itu-v-series.md)

Already documented:

- formal RS-232 revision dates;
- RS-232-A → Bell 202C/202D implementation edge;
- Bell 101/103 source conflict;
- 103A contemporary existence by 1962;
- V.24 kept separate from RS-232 identity claims;
- V.21/V.22/V.22bis/V.32/V.32bis/V.34/V.90 as distinct modem-standard generations;
- V.34 1994 (28.8k) versus 1996 (33.6k) edition distinction;
- V.90 as an architectural change exploiting the digital PSTN, not merely "faster V.34".

### Next work

- recover original RS-232/A/B/C standards and build field diffs;
- EIA committee history;
- original V.21/V.22/V.22bis edition dates and texts;
- Bell 103 versus V.21 signal-frequency/compatibility comparison;
- Bell 202 versus V.23 relationship;
- V.32/V.32bis training and signal-processing diff;
- V.34 1994 → 1996 clause-level diff;
- V.90/V.92;
- MNP → V.42/V.42bis;
- Hayes AT command lineage;
- router/terminal-server console-port afterlife.

---

# 2. Shared-medium Ethernet → switched full-duplex Ethernet

```text
ALOHA shared radio channel
          ↓ documented influence
Xerox experimental Ethernet (~2.94 Mb/s)
          ↓
DIX Ethernet 1.0 (1980)
          ↓
DIX Ethernet 2.0 (1982)
          ↘ related / coexisting standardization
            IEEE 802.3
               ↓
        shared coax Ethernet
               ↓
          10BASE-T hubs
               ↓
        bridges / switches
               ↓
     full-duplex switched Ethernet
```

### Current state: **substantial**

Deep excavations:

- [`../docs/alohanet/radio-to-ethernet.md`](../docs/alohanet/radio-to-ethernet.md)
- [`../docs/ethernet/xerox-alto-2-94mbps-pup-stack.md`](../docs/ethernet/xerox-alto-2-94mbps-pup-stack.md)
- [`../docs/ethernet/experimental-ethernet-physical-layer.md`](../docs/ethernet/experimental-ethernet-physical-layer.md)
- [`../docs/lineage/ethernet-shared-medium-to-switched.md`](../docs/lineage/ethernet-shared-medium-to-switched.md)

Already documented:

- ALOHA → Ethernet design influence;
- experimental 2.94 Mb/s system as a separate artifact;
- transceiver/coax/interface/microcode division;
- DIX 1.0 and DIX 2.0 as separate specification generations;
- IEEE 802.3 as related but not byte-identical to DIX framing semantics;
- IEEE 802.3i-1990 10BASE-T;
- physical star with a hub still being one shared collision domain;
- bridge → switch role genealogy;
- IEEE 802.3x-1997 full duplex and the disappearance of collision arbitration from normal point-to-point operation.

This lineage demonstrates a central archival principle: **the name Ethernet survived more continuously than the physical/access mechanism**.

### Next work

- DIX 1.0 → 2.0 clause diff;
- DIX Ethernet II ↔ IEEE 802.3/LLC frame interpretation;
- AUI/MAU/transceiver revisions;
- 10BASE5 → 10BASE2 → 10BASE-T installation economics;
- early commercial bridges;
- Kalpana EtherSwitch model/ASIC/forwarding history;
- store-and-forward versus cut-through switching;
- autonegotiation;
- 802.3x implementation and driver controls;
- Fast/Gigabit Ethernet branches;
- surviving hardware provenance.

---

# 3. Internetwork protocol layering lineage

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
                  deployed TCP/IP
```

### Current state: **started / substantial**

Deep excavation:

[`../docs/lineage/tcp-ip-split-and-standardization.md`](../docs/lineage/tcp-ip-split-and-standardization.md)

Already recorded:

- RFC 675 integrated Transmission Control Program;
- RFC 760 IP IEN replacement list;
- RFC 761 TCP IEN replacement list;
- RFC 791/793 successor relationships;
- responsibility split between best-effort IP and reliable TCP;
- NCP → dual-protocol → TCP/IP operational migration.

### Next work

- acquire every cited IEN;
- header/state-machine diffs;
- early implementation source;
- UDP/ICMP branching;
- sockets/API lineage;
- congestion-control branch without back-projecting it into early TCP.

---

# 4. ARPANET host/network boundary lineage

```text
site-specific host channel
        ↓
Host–IMP / 1822 boundary
        ↓
Local / Distant / Very Distant Host variants
        ↓
network-specific gateway interfaces
        ↓
later generalized router link interfaces
```

### Current state: **started**

Deep excavations:

- [`../docs/arpanet/1969-host-imp-stack.md`](../docs/arpanet/1969-host-imp-stack.md)
- [`../docs/arpanet/ucla-1969-node-bom.md`](../docs/arpanet/ucla-1969-node-bom.md)
- [`../docs/arpanet/bbn-1822-physical-interface.md`](../docs/arpanet/bbn-1822-physical-interface.md)
- Bell 303 / VDH physical excavations.

### Next work

- Report 1822 revision diff;
- Wingfield interface schematics;
- SRI/UCSB/Utah host interfaces;
- later 1822 boards;
- identify what disappeared with ARPANET-specific hardware and what survives as generalized host/router interface practice.

---

# 5. Packet switch / gateway / router role lineage

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

Important rule: **do not make IMP → router a simple ancestry edge.**

The archive distinguishes packet switching, host/network boundary, internetwork forwarding, route computation, interfaces, operations, and contemporary terminology.

---

# 6. GGP → autonomous systems → EGP → BGP

```text
common smart/core-gateway routing
          ↓ scaling + operational rigidity
   autonomous-system partitioning
          ↓
 interior routing / exterior routing split
          ↓
      EGP (RFC 827/888/904)
          ↓ experience / topology limits
      BGP-1 → BGP-2 → BGP-3 → BGP-4
                               ↘
                                CIDR prefix/aggregation architecture
```

### Current state: **substantial**

Deep excavations:

- [`../docs/lineage/ggp-egp-bgp-routing-domains.md`](../docs/lineage/ggp-egp-bgp-routing-domains.md)
- [`../docs/lineage/bgp-1-to-bgp-4.md`](../docs/lineage/bgp-1-to-bgp-4.md)

Already documented:

- RFC 827's explicit explanation of why one common gateway-routing regime stopped scaling;
- autonomous systems as an administrative/technical decomposition;
- RFC 890 deployment plan from smart/dumb gateways to AS membership and EGP;
- RFC 904 formal EGP;
- EGP → BGP as documented design/operational ancestry, not formal revision;
- BGP-1/2/3/4 formal version chain;
- BGP TCP/179 continuity;
- CIDR ↔ BGP-4 intersection;
- RFC 4271 replacing the BGP-4 core specification while retaining the name BGP-4.

### Next work

- GGP packet/source-code archaeology;
- RFC 827 → 888 → 904 field/state-machine diff;
- AS-number allocation history;
- real August 1984 EGP deployment state;
- Cisco/NSFNET BGP-1 software;
- `gated` source lineage;
- BGP attribute diffs;
- route-reflector/confederation/community branches;
- operational incident lineage.

---

# 7. Virtual-circuit / datagram interworking lineage

```text
X.25 virtual-circuit public networks
        ↕ interworked / carried
IP datagrams
```

while at the architectural level:

```text
CYCLADES / IP datagram ideas  ↔  virtual-circuit architectures
```

### Current state: **started**

Deep excavation:

[`../docs/x25/pad-public-data-network-stack.md`](../docs/x25/pad-public-data-network-stack.md)

Next work: named IP-over-X.25 deployments, X.75, Frame Relay relationship, ATM relationship, carrier-service migration.

Do not assume Frame Relay or ATM are simple descendants until documentary/standards relationships are established.

---

# 8. Store-and-forward lineage

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

Deep excavations:

- [`../docs/uucp/usenet-store-and-forward-world.md`](../docs/uucp/usenet-store-and-forward-world.md)
- earliest Duke/UNC physical-path excavation.

Direct descent into modern queue systems remains mostly unproven. Treat analogies as hypotheses until documentary links exist.

---

# 9. NSFNET backbone platform lineage

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

The inherited property is the backbone routing/forwarding role, not chassis architecture.

---

# 10. Naming/directory lineage

```text
manual host naming
      ↓
HOSTS.TXT / NIC distribution
      ↓ scaling/administrative pressure
hierarchical domain naming
      ↓
DNS RFC 882/883
      ↓
DNS RFC 1034/1035
      ↓
modern delegated DNS
```

### Current state: **started**

Deep excavation:

[`../docs/lineage/hosts-txt-to-dns.md`](../docs/lineage/hosts-txt-to-dns.md)

Already recorded:

- central table/distribution versus delegated authority;
- RFC 819 influence on early DNS design;
- RFC 882/883 → RFC 1034/1035 formal successor relationships;
- local hosts-file mechanism surviving beside DNS.

Next work: BIND/Jeeves source code, resolver APIs, root/TLD operations, caching evolution, DNSSEC as later branch.

---

# 11. Future high-value lineage branches

## LAN switching

```text
repeater ≠ bridge
bridge → transparent bridge/STP → multiport bridge/switch → VLAN/full duplex/high-speed switching
```

## Error control / compression

```text
vendor MNP families ↔ V.42 / V.42bis
```

## Remote access

```text
terminal concentrator / PAD / terminal server / dial access server
```

The relationships here are likely to be networks rather than clean trees.

## Routing inside an AS

HELLO, RIP, OSPF, IS-IS and proprietary IGPs need separate mechanism genealogies rather than one false sequence.

## Network management

ARPANET/NOC measurement → vendor management → SNMP/CMIP branches should be reconstructed from operator practice and protocol documents.

---

## Completion criterion for a lineage

A lineage is not mature because a diagram looks plausible.

For each important arrow, preserve:

```text
source object
   ↓
specific inherited / revised / rejected property
   ↓
target object
   ↓
source document + locator
   ↓
certainty + directness
   ↓
negative claim: what this arrow does NOT establish
```

A good lineage can say not only **what survived**, but also **what died while the name survived**.

That is the difference between technical genealogy and mythology.
