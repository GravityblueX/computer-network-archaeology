# Standards and Architecture Genealogy: How the Modern Network Grew Out of Older Boundaries

Networking history becomes much easier to misunderstand when standards are treated as isolated inventions.

A modern diagram often begins with Ethernet, IP, TCP, DNS, BGP and HTTP, as if each protocol appeared into an empty world. The archaeological record shows something different. New networking standards repeatedly inherited older assumptions from telegraphy, telephony, time-sharing, carrier services, operating systems, packet-switch networks and equipment interfaces.

This chapter introduces a **genealogical reading** of the archive.

The question is not merely:

> When was standard X published?

It is also:

> Which older boundary did X formalize? Which responsibility moved? Which mechanism was retained? Which physical constraint disappeared while its logical convention survived?

The machine-readable relationship queue is [`../../data/lineage-ledger.csv`](../../data/lineage-ledger.csv). The evidence model is described in [`../../lineage/README.md`](../../lineage/README.md).

---

## 1. The first long-lived inheritance: terminal ↔ communication equipment

Before packet switching, a recurring engineering problem was already visible:

```text
human / business machine / computer
              |
          terminal side
              |
      electrical/control boundary
              |
       data set / modem side
              |
        telephone facility
```

Bell System documentation uses the period term **data set**. Later standards and textbooks commonly frame the boundary as **DTE ↔ DCE**:

- DTE: Data Terminal Equipment;
- DCE: Data Communication Equipment / Data Circuit-terminating Equipment, depending on standards family and period.

The important historical point is not the acronym itself. It is the durable idea that equipment from one manufacturer should be able to present data and control signals to communication equipment from another manufacturer through a defined interchange boundary.

That boundary became one of the most persistent fossils in networking.

### EIA RS-232 revision spine

A U.S. National Bureau of Standards survey records the standardization sequence:

- RS-232 — May 1960;
- RS-232-A — October 1963;
- RS-232-B — October 1965;
- RS-232-C — August 1969.

The same survey describes RS-232-C as a widely adopted data-terminal-to-modem interface and notes later replacement pressure from EIA-422/423-class electrical interfaces.

The historical TIA listing for RS-232-A describes it explicitly as an interface between **data processing terminal equipment** and **data communication equipment**, exchanging binary serial data and control signals. It also identifies the 1960 RS-232 as the preceding historical version.

This is an unusually clean standards genealogy because the revisions are formal and dated.

### Product adoption proves the boundary was not merely theoretical

A Bell System 202C/202D interface specification from May 1964 states that the bipolar interface signals exchanged between business machines and the data sets conform to **EIA RS-232-A of October 1963**.

This creates a concrete chain:

```text
terminal / business-machine interoperability problem
              ↓
       EIA RS-232 (1960)
              ↓ revision
       EIA RS-232-A (1963)
              ↓ deployed product interface
       Bell 202C / 202D data sets
```

The standard therefore belongs in the physical archaeology of modem/data-set equipment, not in a detached “standards history” appendix.

### CCITT V.24 is related, but do not write `V.24 = RS-232`

ITU's V.24 recommendation defines interchange circuits between DTE and DCE for binary data, control and timing signals. Modern reference material often uses “RS-232/V.24” as shorthand, but historically the specifications divide responsibility differently.

A useful decomposition is:

```text
functions / interchange-circuit meanings   → CCITT V.24
some electrical characteristics            → CCITT V.28 and relatives
connector/pin allocation                    → other ISO/national standards
US integrated interface specification       → EIA RS-232 family
```

The archive should therefore store **parallel and interworking standards families**, not flatten them into synonyms.

See [`bell-data-set-rs232-v24.md`](bell-data-set-rs232-v24.md).

---

## 2. Shared-medium genealogy: ALOHA → experimental Ethernet

The relationship between ALOHAnet and Ethernet is one of the strongest examples of a documented conceptual inheritance.

ALOHAnet confronted a fundamental shared-medium problem in radio:

- multiple stations transmit into a common medium;
- transmissions can overlap;
- collisions destroy useful reception;
- endpoints need a strategy for retransmission.

At Xerox PARC, Ethernet reworked the shared-medium problem for coaxial cable. Metcalfe and Boggs' 1976 paper explicitly places Ethernet in this intellectual context.

But the lineage must not be simplified to:

```text
ALOHA = Ethernet before cable
```

Ethernet added or changed crucial mechanisms:

- carrier sensing;
- collision detection during transmission;
- a different physical medium;
- transceiver/interface hardware;
- packet framing and CRC choices;
- an implementation tightly integrated with Alto microcode and interface hardware.

A better lineage statement is:

```text
ALOHA shared-medium contention problem
              ↓ documented influence
Xerox experimental Ethernet access architecture
              ↓
coax + transceiver + collision detection + backoff + frame logic
```

The inherited object is partly a **problem formulation**, not a copied protocol.

See:

- [`../alohanet/radio-to-ethernet.md`](../alohanet/radio-to-ethernet.md)
- [`../ethernet/xerox-alto-2-94mbps-pup-stack.md`](../ethernet/xerox-alto-2-94mbps-pup-stack.md)
- [`../ethernet/experimental-ethernet-physical-layer.md`](../ethernet/experimental-ethernet-physical-layer.md)

---

## 3. Ethernet itself is several genealogies braided together

“Ethernet” is not one uninterrupted object.

At minimum the archive should distinguish:

1. the 1973 concept/memos;
2. the roughly 3 Mbit/s Xerox experimental Ethernet;
3. the 10 Mbit/s DIX specification lineage;
4. IEEE 802.3 standardization;
5. 10BASE5 shared coax;
6. 10BASE2 thin coax;
7. twisted-pair repeater/hub Ethernet;
8. transparent bridging and switching;
9. full-duplex switched Ethernet.

Different properties have different descendants.

### Medium attachment lineage

```text
experimental coax transceiver
        ↓
10 Mbit/s coax MAU/transceiver practice
        ↓
AUI-era external attachment
        ↓
NIC-integrated PHY/transceiver functions
```

### Access-control lineage

```text
shared coax CSMA/CD
        ↓
shared repeater/hub collision domain
        ↓
bridged/switch-separated collision domains
        ↓
full-duplex point-to-point Ethernet
```

The frame/addressing family survived much longer than the ordinary experience of collision detection.

So it is misleading to say simply:

> Ethernet still uses CSMA/CD.

A genealogical statement is more precise:

> CSMA/CD is central to the shared-medium ancestry of Ethernet, while modern switched full-duplex Ethernet preserves other parts of the family and normally eliminates collisions from ordinary link operation.

This is exactly why the archive needs property-level lineage edges.

---

## 4. Host protocol replacement: NCP → IP/TCP was an operational migration

The ARPANET transition from NCP to IP/TCP is often compressed into one date: **1 January 1983**.

RFC 801, *NCP/TCP Transition Plan* (November 1981), preserves the migration as an operational process instead.

It called for:

- host implementations of IP/TCP;
- TCP versions of Telnet, FTP and mail;
- dual-protocol hosts;
- relay hosts connecting NCP-only and TCP-only environments;
- staged service milestones;
- removal of NCP from service in January 1983.

The lineage therefore contains both **replacement** and **service continuity**:

```text
ARPANET NCP host environment
         ↓ replaced operationally
IP/TCP host environment
```

while simultaneously:

```text
Telnet user service ───────────────→ TCP Telnet
FTP user service    ───────────────→ TCP FTP
network mail        ───────────────→ SMTP-based mail environment
```

The applications are not identical across the boundary, but the migration deliberately preserves important user-facing roles.

This distinction matters because standards transitions are often migration engineering problems, not merely protocol-design problems.

Primary source: RFC 801, RFC Editor.

---

## 5. Packet switch → gateway → router: roles evolve before terminology stabilizes

The word **router** can obscure earlier equipment if it is projected backward.

ARPANET's IMPs switched packets **inside one packet-switched network**. Later DARPA Internet gateways forwarded Internet datagrams **between unlike networks**. By the late 1980s and 1990s, the term router became normal for much of this network-layer forwarding role.

A useful role genealogy is:

```text
packet-switching node inside a network
          IMP / CIGALE / other packet switch

                    ≠

network interconnection machine
          DARPA Internet gateway
                    ↓ terminology/role evolution
                 IP router
```

The unequal sign is important. IMP → router is not a clean product genealogy.

A better archive records several dimensions separately:

- switching inside one network;
- inter-network forwarding;
- routing-control computation;
- physical interface inventory;
- operational monitoring;
- terminology used by contemporary documents.

The 1982 BBN Internet Gateway described in RFC 823 is a particularly good fossil because it already looks functionally familiar to a modern router engineer while retaining the older **gateway** term.

See [`../internetworking/bbn-gateway-to-router.md`](../internetworking/bbn-gateway-to-router.md).

---

## 6. Virtual-circuit and datagram histories are braided, not winner/loser branches

A popular retrospective story says:

```text
X.25 / virtual circuit loses
TCP/IP / datagram wins
```

The operational record is messier.

RFC 877 specifies **IP datagrams over public data networks**, including X.25 environments. CSNET and other networks used combinations of TCP/IP and carrier/public-data-network services.

So the archive must be able to express:

```text
IP
 ↓ encapsulated/carried over
X.25 virtual circuits
```

at the same historical moment when datagram and virtual-circuit architectures were also competing conceptually and institutionally.

Technologies can simultaneously:

- compete;
- interoperate;
- encapsulate one another;
- occupy different layers;
- share physical infrastructure.

Genealogy must therefore be a graph, not a tournament bracket.

---

## 7. Store-and-forward did not die when dial-up UUCP faded

UUCP networking demonstrates another kind of inheritance.

The physical form was historically specific:

```text
Unix host
  ↓ spool queue
serial interface
  ↓
modem
  ↓
telephone circuit
  ↓
remote modem
  ↓
remote UUCP spool
```

The exact UUCP protocols and bang-path addressing faded from mainstream Internet use, but several architectural practices remain common:

- persistent queues;
- deferred transmission;
- retry after failure;
- asynchronous delivery;
- tolerance of intermittent connectivity;
- separation between enqueue time and delivery time.

It is tempting to draw a direct line from UUCP to every modern message queue. That would usually be too strong.

The safe historical statement is:

> the engineering pattern survives widely, while direct code/protocol descent must be demonstrated separately.

See [`../uucp/usenet-store-and-forward-world.md`](../uucp/usenet-store-and-forward-world.md) and the Duke/UNC physical-path excavation.

---

## 8. Backbone router genealogy: Fuzzball → IBM RT NSS → T3 generation

NSFNET shows how a role can survive while the implementation changes radically.

### Phase I

The original 56 kbit/s backbone used Fuzzball systems on PDP-11/LSI-11-family hardware.

### T1 phase

The 1988 T1 backbone replaced that platform with IBM RT-based Nodal Switching Subsystems. One NSS was not simply “a faster router”; it was a multi-computer routing/switching subsystem with separate packet switching, route control, internal Token Rings, management machines, and carrier-side infrastructure.

### T3 phase

The next generation again changed processors, transmission systems and backbone architecture.

The stable historical property is not the chassis.

It is the **national IP-backbone forwarding and routing role**.

This is a textbook `role-descends-into` lineage rather than a simple hardware `revision-of` relation.

See:

- [`../nsfnet/fuzzball-node-internals.md`](../nsfnet/fuzzball-node-internals.md)
- [`../nsfnet/ibm-rt-nss-node-internals.md`](../nsfnet/ibm-rt-nss-node-internals.md)

---

## 9. Standards have multiple kinds of ancestry

Every standards genealogy should distinguish at least five relationships.

### 9.1 Formal revision ancestry

Example:

```text
RS-232 → RS-232-A → RS-232-B → RS-232-C
```

This is the easiest kind because standards bodies explicitly publish revisions.

### 9.2 Practice → standard

A standards committee may formalize an already-existing industry boundary or convention.

This relationship requires committee history, drafts, vendor practice or contemporary discussion. Do not infer it merely because an older product looks similar.

### 9.3 Standard → deployed product

Example:

```text
RS-232-A
    ↓ adopted by
Bell 202C / 202D interface
```

Vendor manuals are excellent evidence for this edge.

### 9.4 Parallel standards

Example:

```text
EIA RS-232 family  ↔  CCITT V.24/V.28 family
```

Neither side should automatically be labeled a copy of the other.

### 9.5 Standard survives after original use case changes

A modem interface can become a terminal interface, console port, embedded equipment interface, or compatibility layer long after the original carrier service disappears.

This is one of the most important forms of technological afterlife.

---

## 10. The archaeology question for every modern standard

For each modern mechanism, the archive should eventually be able to answer:

1. What problem existed before the standard?
2. Which pre-standard equipment solved it incompatibly?
3. Which committee/document formalized the boundary?
4. Which vendor products first implemented it?
5. Which revisions changed electrical, framing or semantic behavior?
6. Which parts became de facto practice beyond the original scope?
7. Which parts were later replaced?
8. Which names survived even when the mechanism changed?
9. Which physical constraints disappeared?
10. Which modern systems still contain a recognizable fossil?

That turns a standards list into a history of engineering inheritance.

---

## Sources used in this first lineage pass

- U.S. National Bureau of Standards, historical standards survey recording RS-232 (May 1960), RS-232-A (October 1963), RS-232-B (October 1965), and RS-232-C (August 1969): https://www.govinfo.gov/content/pkg/GOVPUB-C13-4d7b52427051ca9e169ba2337917df2f/pdf/GOVPUB-C13-4d7b52427051ca9e169ba2337917df2f.pdf
- TIA historical listing for RS-232-A (October 1963), including its relationship to the May 1960 RS-232: https://store.accuristech.com/standards/tia-rs-232-a?product_id=2593188
- Bell System 202C/202D interface specification (May 1964), archived by Bitsavers, explicitly citing EIA RS-232-A: https://bitsavers.org/communications/westernElectric/modems/202C_and_202D_Interface_Specification_May64.pdf
- ITU-T V.24 recommendation database and edition history: https://www.itu.int/ITU-T/recommendations/rec.aspx?lang=en&rec=4938
- Metcalfe and Boggs, *Ethernet: Distributed Packet Switching for Local Computer Networks* (1976), preserved transcription: https://www.cs.cornell.edu/courses/cs414/2002sp/papers/ethernet/ethernet.htm
- Jon Postel, RFC 801, *NCP/TCP Transition Plan* (November 1981): https://www.rfc-editor.org/rfc/rfc801.html
- RFC 877, IP over public data networks/X.25: https://www.rfc-editor.org/rfc/rfc877.html

## Status

This file is a map of high-value lineages, not a claim that the genealogies are complete.

The next stage should promote each important arrow into a source-located `LIN-*` record and split broad relationships into property-specific edges: connector, voltage, control circuit, frame field, addressing rule, routing role, API, or operational practice.