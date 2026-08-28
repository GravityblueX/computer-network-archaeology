# Bridge → Spanning Tree → Ethernet Switch → VLAN

> A technical genealogy of Layer-2 forwarding, loop control, multiport switching, and virtual bridged LANs.

This excavation follows one of the most important but easily flattened lineages in LAN history:

```text
shared LAN segments
      ↓
transparent bridge
      ↓
loop problem
      ↓
spanning-tree bridge topology
      ↓
multiport bridge / Ethernet switch
      ↓
virtual bridged LANs / VLANs
```

The tempting modern shorthand is:

> bridge → switch → VLAN.

That is too simple.

The important inheritance is not a product name. It is a set of responsibilities:

- learning which source MAC addresses are reachable through which port;
- selectively forwarding or filtering frames;
- flooding when the destination is unknown;
- preventing forwarding loops in a topology that may contain redundant links;
- maintaining a logical topology that can differ from physical cabling;
- eventually allowing several logical broadcast domains to coexist over shared switching infrastructure.

This is the path by which a box originally used to join two LAN segments grows into the conceptual ancestor of the modern Ethernet switch.

---

## 1. Why a bridge exists at all

An early LAN such as Ethernet is a shared local communication medium. A single LAN has practical limits in geography, load, station count, and fault domain.

One answer is routing at a higher layer. Another is to interconnect LAN segments while preserving the illusion of a larger link-layer environment.

A **transparent bridge** does that below the network layer.

The basic forwarding problem is:

```text
LAN A ──[ bridge ]── LAN B
```

A bridge observes source MAC addresses arriving on each port and builds a forwarding database. A frame whose destination is known can be sent only toward the appropriate segment. A frame whose destination is unknown may have to be flooded.

This is already the conceptual center of later Ethernet switching.

RFC 1493, *Definitions of Managed Objects for Bridges* (1993), describes bridges as devices connecting LAN segments below the network layer and maps its Bridge MIB directly onto IEEE 802.1D-1990 bridge objects:

- bridge address;
- port table;
- forwarding database;
- spanning-tree state;
- root identifier;
- root cost;
- root port;
- topology-change counters;
- static filtering entries.

Primary/near-primary references:

- RFC 1493: https://www.rfc-editor.org/rfc/rfc1493.html
- IEEE 802.1D historical standards corpus: https://standards.ieee.org/

---

## 2. The loop problem is not optional

Two bridges between the same LANs appear to give redundancy:

```text
        ┌── bridge 1 ──┐
LAN A ──┤              ├── LAN B
        └── bridge 2 ──┘
```

But ordinary Ethernet frames do not contain a hop count like an IP packet.

A flooded broadcast/unknown-destination frame can therefore circulate repeatedly through a bridged loop. Copies multiply. Forwarding tables become unstable because the same source address appears to arrive from different directions.

So a bridged LAN needs a way to retain physical redundancy while selecting a **loop-free active forwarding topology**.

That requirement is what makes the spanning-tree problem central to bridge history.

---

## 3. Radia Perlman and distributed spanning tree

Radia Perlman's 1985 SIGCOMM paper, *An Algorithm for Distributed Computation of a Spanning Tree in an Extended LAN*, describes bridges computing an acyclic spanning subset of an arbitrary extended-LAN topology in a distributed manner.

The mechanism chooses a root and computes least-cost paths toward it. Some physical links/ports are therefore prevented from forwarding ordinary traffic, leaving one logical tree spanning all LANs.

The essential transformation is:

```text
physical mesh
     ↓ distributed computation
logical loop-free tree
```

The paper emphasizes that the algorithm requires little memory per bridge and little protocol traffic independent of the total number of bridges or links.

Bibliographic record:

- Radia J. Perlman, SIGCOMM 1985, pp. 44–53, DOI 10.1145/318951.319004.
- Author-hosted copy: https://people.eecs.berkeley.edu/~sylvia/papers/spanning-tree.pdf

This is a direct documented lineage, not merely a resemblance between modern STP and an older idea.

---

## 4. DEC LANbridge 100 is a historical warning

RFC 1493 exposes a useful archaeological detail in its managed object `dot1dStpProtocolSpecification`.

It distinguishes values for:

- `decLb100(2)` — DEC LANbridge 100 Spanning Tree protocol;
- `ieee8021d(3)` — IEEE 802.1D implementation.

This means the archive must not write a single timeless object called “STP” and assume every bridge used exactly the same wire protocol/state machine.

The correct structure is closer to:

```text
DEC bridge/STP implementation lineage
           ↓ standardization / revision work
IEEE 802.1D spanning-tree generation
```

The exact relationship between DEC product revisions, Perlman's design, and each IEEE edition needs revision-level documentation, but RFC 1493 independently proves that operators still had to distinguish DEC LANbridge-100 STP from IEEE 802.1D STP in the early 1990s.

That distinction deserves separate artifacts and protocol records.

---

## 5. Bridge state becomes operational state

By 1993 the Bridge MIB treated spanning-tree information as ordinary manageable network state.

Examples include:

```text
dot1dStpPriority
dot1dStpDesignatedRoot
dot1dStpRootCost
dot1dStpRootPort
dot1dStpTimeSinceTopologyChange
dot1dStpTopChanges
```

This is historically important because it links two other repository genealogies:

```text
bridge/STP lineage
        +
SNMP/MIB management lineage
        ↓
managed switched LAN infrastructure
```

Modern switch management did not appear independently of forwarding history. The control/monitoring objects grew around real bridge state machines and forwarding tables.

---

## 6. Why an Ethernet switch is a bridge descendant

Later industry documents often describe an Ethernet switch as, functionally, a **multiport bridge**.

This is a useful statement if interpreted carefully.

A classic two-port bridge:

```text
LAN A ──[ bridge ]── LAN B
```

A multiport bridge/switch:

```text
          port 1 ── station/segment
             \
port 2 ── [ switching fabric ] ── port 3
             /
          port 4
```

The inherited link-layer roles remain recognizable:

- source-address learning;
- forwarding database lookup;
- selective forwarding/filtering;
- unknown/broadcast flooding;
- loop-control participation;
- MAC-layer transparency to higher protocols.

But **switch = bridge** must not erase hardware history.

Commercial switches changed implementation economics through:

- more ports;
- simultaneous forwarding between multiple port pairs;
- dedicated packet processors/ASICs;
- cut-through versus store-and-forward designs;
- per-port collision domains;
- higher internal fabric bandwidth;
- management and VLAN functions.

A later patent description of switching history states that Ethernet switches appeared commercially with Kalpana's early EtherSwitch generation and explicitly characterizes switches, from an Ethernet perspective, as multiport bridges. That is useful secondary/industry evidence, but exact “first Ethernet switch” claims still need Kalpana product announcements, patents, manuals, and shipping records.

Relevant leads:

- Kalpana switching history in patent literature: https://patents.google.com/patent/WO2001001637A1/en
- CHM collection entry for a surviving Kalpana EtherSwitch EPS-1500: https://computerhistory.org/wp-content/uploads/2019/08/core-2006.pdf

---

## 7. Segmentation changes Ethernet before VLAN exists

A hub/repeater extends one collision domain.

A bridge/switch separates forwarding segments.

Thus the topology changes from:

```text
one shared medium
     ↓
repeated shared medium
```

into:

```text
multiple link segments
     ↓ bridge/switch forwarding
one larger logical LAN
```

This matters because switched Ethernet can preserve a common Layer-2 broadcast domain while eliminating the requirement that all attached stations contend on one physical collision medium.

When full-duplex point-to-point links later become normal, CSMA/CD itself can cease to be operationally relevant on those links even though the system remains Ethernet.

That transformation is documented separately in:

[`ethernet-shared-medium-to-switched.md`](ethernet-shared-medium-to-switched.md)

---

## 8. VLAN: the logical LAN detaches from physical port geography

Once bridges/switches already maintain a logical forwarding topology, another step becomes possible:

> one physical switching infrastructure can represent multiple logical LANs.

IEEE 802.1Q-1998 is explicitly titled *Virtual Bridged Local Area Networks*.

IEEE describes it as defining:

- an architecture for Virtual Bridged LANs;
- services provided by Virtual Bridged LANs;
- protocols and algorithms used to provide those services.

Board approval: **8 December 1998**.  
Published: **8 March 1999**.

IEEE catalog page:

https://standards.ieee.org/ieee/802.1Q/1039/

The critical lineage is therefore not:

```text
Ethernet → magic VLAN tag
```

It is:

```text
LAN
 ↓
bridged LAN
 ↓
loop-controlled bridged LAN
 ↓
managed multiport bridging/switching
 ↓
virtual bridged LAN
```

The tagged frame format is only one part of this larger architecture.

---

## 9. VLAN changes what “a LAN” means

In a shared coax network, physical attachment strongly constrains LAN membership.

With virtual bridging, membership can be an administrative property.

Conceptually:

```text
physical topology
      ≠
logical broadcast topology
```

A switch can therefore carry several logical Layer-2 domains across common hardware/trunks.

This is a profound architectural inheritance from bridge history: the forwarding device already maintained a logical model distinct from raw physical connectivity; VLANs extend that separation.

---

## 10. What survived into modern switching

A modern Ethernet switch still contains recognizable bridge ancestry:

- MAC address learning;
- forwarding/filtering database;
- flooding of unknown/broadcast traffic;
- bridge identifiers and loop-control concepts;
- topology-change handling;
- per-port state;
- management objects reflecting bridge state;
- VLAN-aware forwarding and logical segmentation.

But other ancestral mechanisms are conditional or transformed:

- shared-medium collision handling may be irrelevant on full-duplex links;
- classic STP may be replaced by later variants or alternative control designs;
- forwarding may be implemented in ASIC tables rather than a general-purpose bridge CPU;
- “port” may represent a physical interface, LAG, virtual port, tunnel attachment, or other abstraction.

Thus a modern switch is not simply “an old bridge made faster.”

It is a platform in which bridge semantics survived while implementation and topology changed radically.

---

## 11. Lineage edges to preserve

High-confidence edges:

```text
transparent bridge forwarding role
    └─ survives-as → Ethernet switch Layer-2 forwarding

Radia Perlman 1985 distributed spanning-tree design
    └─ influenced/standardized-into → IEEE bridge spanning-tree lineage

IEEE 802.1D bridge/STP model
    └─ managed-by → Bridge MIB / SNMP objects

bridged LAN architecture
    └─ extended-by → IEEE 802.1Q Virtual Bridged LAN architecture
```

Edges requiring caution:

```text
DEC LANbridge 100 STP → IEEE 802.1D
```

This requires precise DEC/IEEE committee and protocol revision evidence.

Likewise:

```text
Kalpana EtherSwitch = first Ethernet switch
```

should remain a product-history claim requiring original product/shipping evidence, not an unquestioned slogan.

---

## 12. Next excavation targets

- DEC LANbridge 100 manuals and exact spanning-tree PDU/state machine;
- Radia Perlman/DEC implementation chronology versus IEEE 802.1D editions;
- IEEE 802.1D-1990 primary text and revision history;
- Kalpana EtherSwitch EPS-700/EPS-1500 model chronology;
- Kalpana patents and forwarding-fabric details;
- first product manuals explicitly using `switch` rather than `bridge`;
- store-and-forward versus cut-through implementation genealogy;
- switch ASIC/CAM forwarding-table history;
- IEEE 802.1Q-1998 tag/frame and VLAN membership details;
- VLAN trunking predecessors and vendor-specific alternatives;
- later STP branches: RSTP/MSTP;
- bridge/switch management object evolution from RFC 1286/1493 onward.

---

## Archaeological conclusion

The Ethernet switch did not begin as an unrelated box that replaced the bridge.

Its central Layer-2 behavior grows from bridge semantics:

> learn → filter → forward → flood → prevent loops.

Then the physical LAN and logical LAN gradually separate:

> segment → bridge → spanning tree → multiport switching → virtual bridging.

That is why a modern switch still carries concepts created for a world of much smaller LANs, even though its hardware, bandwidth, and topology would be unrecognizable to an early bridge designer.
