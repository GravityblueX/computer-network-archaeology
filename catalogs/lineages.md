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

Deep excavations:

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

- original RS-232/A/B/C standards and field diffs;
- EIA committee history;
- original V.21/V.22/V.22bis editions;
- Bell 103 versus V.21 signal-frequency/compatibility comparison;
- Bell 202 versus V.23;
- V.32/V.32bis training diff;
- V.34 1994 → 1996 clause diff;
- V.90/V.92;
- console-port afterlife.

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
- DIX 1.0 and 2.0 as separate generations;
- IEEE 802.3 as related but not byte-identical to DIX frame semantics;
- IEEE 802.3i-1990 10BASE-T;
- physical star with a hub still being one shared collision domain;
- bridge → switch role genealogy;
- IEEE 802.3x-1997 full duplex and disappearance of collision arbitration from normal point-to-point operation.

This lineage demonstrates a central archival principle: **the name Ethernet survived more continuously than the physical/access mechanism**.

### Next work

- DIX 1.0 → 2.0 clause diff;
- DIX Ethernet II ↔ IEEE 802.3/LLC frame interpretation;
- AUI/MAU revisions;
- 10BASE5 → 10BASE2 → 10BASE-T installation economics;
- early commercial bridges and switches;
- autonegotiation;
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

Deep excavation: [`../docs/lineage/tcp-ip-split-and-standardization.md`](../docs/lineage/tcp-ip-split-and-standardization.md)

Already recorded: RFC 675 integrated TCP, IP/TCP IEN replacement lists, RFC 791/793 successor relationships, responsibility split, and NCP → TCP/IP operational migration.

Next: every cited IEN, source-code implementations, UDP/ICMP, sockets/API, and later congestion-control lineage.

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

Next: Report 1822 diffs, Wingfield interface, other first-four-host interfaces, later 1822 boards, and what survived as generalized host/router interface practice.

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

Deep excavation: [`../docs/internetworking/bbn-gateway-to-router.md`](../docs/internetworking/bbn-gateway-to-router.md)

Important rule: **do not make IMP → router a simple ancestry edge.** Packet switching, internetwork forwarding, route computation, interfaces, operations, and terminology have separate genealogies.

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

Already documented: autonomous-system decomposition, RFC 890 deployment plan, formal EGP, EGP→BGP influence rather than revision, BGP-1/2/3/4 chain, TCP/179 continuity, CIDR intersection, and RFC 4271 replacing RFC 1771 while the family remains BGP-4.

Next: GGP code, EGP deployment artifacts, AS-number allocation history, Cisco/NSFNET BGP-1, `gated`, attribute diffs, and later policy branches.

---

# 7. Virtual-circuit / datagram interworking lineage

```text
X.25 virtual-circuit public networks
        ↕ interworked / carried
IP datagrams
```

### Current state: **started**

Deep excavation: [`../docs/x25/pad-public-data-network-stack.md`](../docs/x25/pad-public-data-network-stack.md)

Next: named IP-over-X.25 deployments, X.75, Frame Relay and ATM relationships, carrier-service migration. Do not assume simple descendants.

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

Deep excavations include UUCP/Usenet and the earliest Duke/UNC physical-path reconstruction. Direct descent into modern queue systems remains mostly unproven.

---

# 9. NSFNET backbone platform lineage

```text
56 kbit/s PDP-11/LSI-11 Fuzzballs
            ↓ replaced operationally
1.544 Mbit/s IBM RT Nodal Switching Subsystems
            ↓
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

Deep excavation: [`../docs/lineage/hosts-txt-to-dns.md`](../docs/lineage/hosts-txt-to-dns.md)

Next: Jeeves/BIND source code, resolver APIs, root/TLD operations, caching evolution, DNSSEC as a later branch.

---

# 11. Bridge → spanning tree → switch → VLAN

```text
shared LAN segments
      ↓
transparent bridge
      ↓ redundant loops become a problem
spanning-tree computation
      ↓
IEEE 802.1D bridge/STP lineage
      ↓
multiport bridge / Ethernet switch
      ↓
IEEE 802.1Q virtual bridged LANs
```

### Current state: **started / substantial**

Deep excavation: [`../docs/lineage/bridge-stp-switch-vlan.md`](../docs/lineage/bridge-stp-switch-vlan.md)

Structured artifacts/edges now include IEEE 802.1D-1990 (`ART-0103`) and `LIN-0062` for Perlman-design influence.

Already documented:

- bridge learning/filtering/flooding responsibilities;
- the loop problem in redundant bridged LANs;
- Perlman's 1985 distributed spanning-tree algorithm;
- RFC 1493's explicit distinction between DEC LANbridge 100 STP and IEEE 802.1D STP;
- bridge/STP state exposed through SNMP Bridge MIB;
- switch role as multiport bridge descendant, while hardware/ASIC history remains separate;
- IEEE 802.1Q-1998 as Virtual Bridged LAN architecture.

### Next work

- DEC LANbridge 100 manuals and exact STP dialect;
- IEEE 802.1D editions and clause/PDU/timer diff;
- Kalpana EPS-700/EPS-1500 chronology and forwarding hardware;
- store-and-forward vs cut-through;
- CAM/ASIC history;
- 802.1Q tag/member semantics and vendor VLAN predecessors;
- RSTP/MSTP branches.

---

# 12. MNP → V.42 / V.42bis modem reliability lineage

```text
vendor modem error-control protocols
          ↓
MNP installed base
          ↕ compatibility/interworking
V.42 LAPM standardized error control
          +
V.42bis standardized compression
```

### Current state: **started**

Deep excavation: [`../docs/lineage/mnp-v42-v42bis.md`](../docs/lineage/mnp-v42-v42bis.md)

Structured artifact: `ART-0107` V.42 (11/1988). Structured compatibility edge: `LIN-0068`.

Already documented:

- first V.42 edition in November 1988;
- formal V.42 revision line 1988 → 1993 → 1996 → 2002;
- LAPM as the standardized V.42 error-control path;
- deployed V.42 modem products retaining MNP Classes 2-4 fallback/interworking;
- MNP5 and V.42bis as distinct compression families;
- V.42bis approval 31 January 1990;
- separation among modulation speed, DTE serial rate, error correction, and compressed effective throughput.

### Next work

- original Microcom MNP specifications/patents/licensing;
- exact MNP class genealogy;
- V.42 1988 normative text and LAPM state machine;
- real LAPM/MNP negotiation captures;
- MNP5 vs V.42bis algorithm comparison;
- modem-buffer and RTS/CTS/XON-XOFF interaction;
- later V.44/V.92 branch.

---

# 13. Hayes Smartmodem → AT command ecosystem

```text
manual/separate modem call control
          ↓
software-controllable Smartmodem
          ↓
Hayes AT command + command/data state model
          ↓
communications software depends on it
          ↓
third-party Hayes-compatible modems
          ↓
large vendor-specific AT supersets
```

### Current state: **started**

Deep excavation: [`../docs/lineage/hayes-at-command-set.md`](../docs/lineage/hayes-at-command-set.md)

Structured artifact: `ART-0110`. Structured de-facto-interface edge: `LIN-0075`.

Already documented:

- `AT` command/control grammar in Hayes technical references;
- command/data mode distinction;
- S-register configuration model;
- machine-readable result codes;
- `+++` online escape behavior in deployed software documentation;
- independent software embedding Hayes command strings;
- multiple third-party products explicitly marketed/listed as Hayes-compatible.

### Next work

- earliest Smartmodem manual and exact introduction chronology;
- first command grammar versus 1200/2400 generations;
- original guard-time semantics;
- model-by-model S-register diff;
- UUCP dialer source, BBS drivers, SLIP/PPP chat scripts;
- vendor extension namespaces;
- ETSI/3GPP AT-command branch, but only after explicit documentary ancestry is found.

---

# 14. Network management lineage

```text
early gateway/host monitoring
      ↓
HMP / INOC-era mechanisms
      ↓
SGMP
      ↓ architecture survives despite wire incompatibility
SNMP
      ↓
SNMPv2 / SNMPv3 frameworks
```

### Current state: **started**

Deep excavation: [`../docs/lineage/hmp-sgmp-snmp-management.md`](../docs/lineage/hmp-sgmp-snmp-management.md)

Next: HMP source/implementations, SGMP source, first SNMP agents, SMI/MIB object genealogy, CMIP coexistence, vendor management platforms, and configuration/telemetry descendants with cautious influence claims.

---

# 15. Future high-value lineage branches

## Remote access

```text
terminal concentrator ↔ PAD ↔ terminal server ↔ dial access server
```

This will probably be a network of role/interworking edges rather than a clean tree.

## Routing inside an AS

HELLO, RIP, OSPF, IS-IS and proprietary IGPs need separate mechanism genealogies rather than one false sequence.

## Application protocols

NCP-era Telnet/FTP/mail → TCP-era revisions → later standards; preserve service continuity separately from transport/protocol continuity.

## Network configuration and telemetry

CLI/config files, SNMP management, NETCONF/YANG, streaming telemetry and controller APIs should be connected only where design/implementation evidence proves ancestry.

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

It can also say when an old protocol survived only as a compatibility path, when a product interface became a de-facto standard, and when two technologies merely coexisted without one descending from the other.

That is the difference between technical genealogy and mythology.
