# Xerox experimental Ethernet physical layer: coax, taps, transceivers, watchdogs, and collision sensing

> Status: active excavation. This chapter stays inside the **2.94/3 Mbit/s Xerox experimental Ethernet**. It must not be silently mixed with DIX 10 Mb/s Ethernet, 10BASE5 MAUs, AUI, IEEE 802.3 collision/jam timing, or later “vampire tap” installation rules unless a specific genealogy is demonstrated.

## 1. Four pieces, not “an Ethernet card”

Metcalfe and Boggs' 1976 implementation description divides experimental Ethernet into four major parts:

1. the **Ether** — the passive shared medium;
2. **transceivers** attached directly to that medium;
3. station-specific **interfaces** that serialize, deserialize, checksum and buffer packets;
4. station-specific **controllers** — firmware/software that schedule transmission and retransmission.

For an Alto this becomes:

```text
Alto memory / software
        ↕
Ethernet microcode controller
        ↕
Alto Ethernet interface
  FIFO / serializer / phase encoder
  clock recovery / deserializer / CRC
        ↕
interface cable
  transmit / receive / interference + power
        ↕
external Ethernet transceiver
        ↕
CATV-style tap
        ↕
shared coaxial Ether
```

The physical medium and the station electronics are separate artifacts.

## 2. The Ether was deliberately passive

The design philosophy was to keep the shared communication facility passive so an active-component failure would normally damage only one station rather than the entire network.

The 1976 paper describes the topology as an **unrooted tree** with only one physical path between any pair of stations. Multiple paths would produce delayed copies of the same transmission and self-interference.

A station could join by tapping the nearest convenient point on the Ether.

This is not identical to the later textbook image of one straight 10BASE5 bus. The experimental design explicitly contemplated branching so long as the topology remained loop-free and signal integrity remained acceptable.

## 3. Off-the-shelf CATV hardware was part of the experiment

For the experimental medium Xerox used:

- low-loss coaxial cable;
- off-the-shelf **CATV taps and connectors**;
- smaller-diameter coax within station clusters;
- larger-diameter, lower-loss coax for longer runs between clusters.

This is important because Ethernet did not begin with a complete purpose-built cabling ecosystem. It appropriated available broadband/CATV physical hardware and then wrapped new packet electronics around it.

The artifact catalog still needs the actual manufacturer/model numbers of those early taps, connectors and cable types.

## 4. The shared medium ran through the building, not through a hub

Metcalfe and Boggs describe the Ether as passing through ceilings or under floors. A station's transceiver attached directly to that passing cable.

So the building itself became part of the network machine:

```text
ceiling / underfloor coax
      ├── tap → transceiver → Alto A
      ├── tap → transceiver → printer
      ├── tap → transceiver → server
      └── long run → another cluster
```

Installation archaeology should therefore seek floor plans, cable routes, closet photographs and PARC facilities records in addition to electronic schematics.

## 5. One kilometer and hundreds of taps were engineering targets

The experimental implementation was designed around approximately:

- **1 km** of Ether;
- up to **256 stations**;
- roughly **3 Mbit/s** line rate (the Alto documentation gives the more precise 2.94 Mbit/s figure).

Metcalfe and Boggs stress that these were implementation choices, not conceptual limits of Ethernet.

The physical design challenge was to maintain usable signal levels and collision visibility across that large passive network despite many taps, cable attenuation and propagation delay.

## 6. The transceiver was external and generic

The Alto Hardware Manual calls the transceiver a small external device that taps into the passing Ether and says the same transceiver could serve different station interface types.

That genericity matters. Xerox was separating:

- medium attachment;
- station controller electronics;
- host architecture.

This is conceptually similar to later separation between a medium attachment unit and a host network controller, but the terminology and electrical details should remain period-specific.

## 7. The transceiver/interface cable carried signals *and power*

The 1976 paper says the external transceiver was powered and controlled through **five twisted pairs** in its interface cable.

Those pairs carried the functions needed for:

- transmit data;
- receive data;
- interference/collision indication;
- power-supply voltages.

The Alto Hardware Manual later summarizes the functional signals as transmit, receive and collision plus supplied power/ground.

This cable is a separate historical object from both the coax Ether and the later 15-pin AUI cable standardized for 10 Mb/s Ethernet.

## 8. Failure containment was designed into the transceiver

The designers were intensely concerned that one broken station could jam a shared passive medium for everyone.

The 1976 paper makes two particularly strong design requirements visible:

- when unpowered, a transceiver should electrically disconnect itself from the Ether;
- a **watchdog timer** should shut down a suspicious transmitting output stage before it pollutes the network indefinitely.

This is one of the deepest continuities in shared-medium networking: the physical layer must defend the commons against a station that fails while transmitting.

## 9. The transceiver had to survive abuse

The paper says experimental transceivers were designed to survive conditions including:

- sustained direct shorting;
- improper Ether termination;
- simultaneous drive by many stations.

They also had to operate in the presence of:

- ground-potential differences across widely separated stations;
- ordinary electrical noise from office equipment such as typewriters and drills.

That environmental requirement is easy to miss when Ethernet history is told only through collision algorithms.

## 10. Collision detection happened at the transceiver

The transceiver compared what the station was attempting to transmit with what it observed on the Ether.

If the received value differed from the transmitted value, it asserted an **interference** indication back toward the station interface/controller.

This created a physical chain:

```text
station emits bit
      ↓
transceiver drives Ether
      ↓
transceiver simultaneously observes Ether
      ↓
observed bit != intended bit
      ↓
INTERFERENCE signal
      ↓
interface/controller aborts packet
      ↓
random retransmission scheduling
```

Collision detection was therefore not an abstract MAC-layer oracle. It depended on analog/digital comparison at the cable attachment point.

## 11. Carrier detection was derived from phase-encoded transitions

Packets were phase encoded, guaranteeing transitions during each bit time. A receiving transceiver/interface could therefore determine that another station was active by observing transitions — what the paper calls the presence of **carrier**.

Carrier sense allowed a station to defer before starting a transmission.

The crucial race remained propagation delay: two distant stations could both see an idle Ether and begin before the other's signal reached them. Those are the collisions Ethernet had to detect and resolve.

## 12. Collision consensus: all contenders must know

Metcalfe and Boggs describe a mechanism they call **collision consensus enforcement**.

When a station discovered interference, it briefly continued/jammed in a way intended to ensure every participant in the collision also recognized the event and aborted.

This should not be copied uncritically into later IEEE “jam sequence” terminology. The idea is genealogically related, but exact bit patterns/timing belong to each implementation generation.

## 13. The interface did the CRC, not the transceiver

The station-specific Ethernet interface serialized/deserialized data and implemented a **16-bit CRC**.

On transmit it:

1. fetched parallel words from memory;
2. serialized and phase encoded them;
3. prefixed synchronization;
4. accumulated CRC;
5. appended CRC after packet data.

On receive it:

1. detected carrier/start;
2. recovered phase/clock;
3. deserialized into memory words;
4. recomputed CRC;
5. rejected/flagged bad packets.

The external transceiver's job was medium coupling, signal observation and collision-related behavior — not full frame processing.

## 14. Hardware filtered obvious garbage before software saw it

Experimental Ethernet tried to avoid wasting host CPU time on hopeless packets.

Mechanisms discussed in the 1976 paper include:

- packet error detection;
- truncated-packet filtering;
- address filtering in the station interface;
- collision detection before a long damaged packet could consume a whole packet time.

This is already recognizably a theme that persists in modern NIC offload: push cheap repetitive validation down toward the hardware boundary.

## 15. Small and large coax were mixed

One unusually easy-to-forget statement in the 1976 paper is that Xerox used **different coax diameters on the same experimental Ethernet**:

- smaller coax for convenient local cluster wiring;
- larger, lower-loss coax for longer inter-cluster runs.

This means any attempt to identify “the original Ethernet cable” with a single later standardized 10BASE5 cable specification is historically unsafe.

A physical reconstruction must discover the exact cable stock used in each PARC deployment date.

## 16. The 1970s electrical-characteristics sheet survives

A Xerox document titled **`Ethernet Transceiver Electrical Characteristics`** survives in the Bitsavers Xerox Alto Ethernet collection.

Searchable archival metadata/text exposes a detailed station-side and Ether-side electrical specification, including TTL-compatible station signals, transceiver drive/load behavior, frequency/duty-cycle constraints, power requirements and physical dimensions.

However, the current research pass could not reliably render the primary scan page through the web PDF viewer. Therefore this repository should treat those numerical values as **discovered but not yet page-image-verified evidence**.

Do not promote exact volts/ohms/mA/dimensions into canonical structured artifact fields until the scan itself is locally acquired, checksummed and visually verified.

This is precisely why the archive separates `discovered` from `mined` and `verified`.

## 17. The June 1974 Alto Ethernet Interface memo also survives

A 22 June 1974 Xerox inter-office memorandum titled **`Alto Ethernet Interface`** survives in multiple archival/manual mirrors.

Its searchable text describes reserved Alto memory locations used by the Ethernet microcode for:

- retransmission/collision mask state;
- input buffer count and pointer;
- output buffer count and pointer;
- station serial/address filtering;
- completion/status.

This is a particularly valuable bridge between the 1973 design concept and the later 1976/1979 mature descriptions.

A clean primary-archive copy should receive its own source record and a line-by-line revision comparison with the 1979 Hardware Manual.

## 18. Experimental Ethernet ≠ 10BASE5

The archive must enforce the following distinction:

```text
1973 concept / Alto Aloha Network
        ↓
1974 experimental Ethernet hardware
  ~2.94 Mb/s
  CATV taps/connectors
  Xerox transceiver/interface cable
        ↓
1976 published experimental system
        ↓
DIX Ethernet 10 Mb/s
        ↓
IEEE 802.3 / 10BASE5
  standardized MAU + AUI + cable rules
```

There is genealogy, but not identity.

Terms such as **AUI**, **MAU**, **10BASE5**, standardized vampire taps, IEEE collision-domain timing and standardized frame rules should not appear in a 1974 artifact record unless explicitly marked as later descendants/comparisons.

## 19. Why a transceiver failure was existential

On a point-to-point link, one bad transmitter usually damages one link. On a passive shared Ether, a transmitter stuck active could damage communications for the whole collision domain.

This explains several design choices that otherwise look oddly defensive:

- watchdog transmitter cutoff;
- fail-disconnected behavior when power is absent;
- robust short/termination tolerance;
- collision/interference monitoring at the attachment point;
- passive shared plant with distributed intelligence at stations.

The physical-layer engineering and the distributed-systems philosophy reinforce each other.

## 20. Required physical artifact fields

For every surviving Xerox experimental transceiver we eventually want:

- Xerox part/assembly number;
- revision;
- serial number;
- PCB photographs both sides;
- IC/transistor inventory;
- station-interface connector;
- Ether-side tap/connector;
- input/output electrical values;
- power rails and consumption;
- dimensions and enclosure;
- watchdog circuit;
- collision detector;
- receive/carrier detector;
- transmitter output stage;
- installation cable type;
- provenance: Alto site, printer, gateway, etc.;
- date removed from service;
- museum/collection location.

For the cable plant:

- coax manufacturer/model;
- impedance;
- diameter;
- attenuation vs frequency;
- terminator values;
- CATV tap model/loss;
- connector model;
- branch topology;
- maximum tap count;
- actual PARC route drawings.

## 21. Modern reconstruction projects are useful — but secondary evidence

Modern Xerox Alto restoration projects have built interfaces to the original 3 Mb/s Ethernet and confirm the practical separation between:

- station TTL-side signals;
- external transceiver/cable behavior;
- PUP/IFS software.

These projects are valuable for locating surviving hardware and testing interpretations, but the repository should keep reconstruction evidence separate from contemporary Xerox specifications.

A successful modern reproduction does not by itself prove that a specific circuit value or cable model was present in a 1974 PARC installation.

## 22. Open excavation checklist

1. Acquire and checksum `Ethernet_Transceiver_Electrical_Characteristics.pdf` locally.
2. Visually verify every numerical electrical parameter and record page/field locators.
3. Locate date, authorship, Xerox filing number and revision history for that sheet.
4. Acquire primary-copy `Alto Ethernet Interface`, 22 June 1974.
5. Diff June 1974 interface semantics against August 1976 and May 1979 Alto manuals.
6. Locate transceiver schematic and PCB assembly drawings.
7. Identify exact CATV tap/connector vendor/model used at PARC.
8. Identify small- and large-diameter coax vendor/model and impedance.
9. Recover PARC building cable-route/topology drawings.
10. Find surviving experimental transceiver specimens and record provenance.
11. Recover Ethernet microcode source by release and map every hardware register/state field.
12. Separate experimental collision-consensus behavior from later IEEE jam-sequence rules.
13. Trace which experimental physical ideas survived into DIX/10BASE5 and which were discarded.
14. Record repeater/filter/gateway hardware used to extend Xerox's internal Ethernets.

## Primary sources and archival targets

- Robert M. Metcalfe and David R. Boggs, *Ethernet: Distributed Packet Switching for Local Computer Networks* (1976), accessible text mirror: https://teaching.csse.uwa.edu.au/units/CITS3002/resources/metcalfe/
- Xerox PARC, *Alto Hardware Manual*, Ethernet chapter, later mature implementation description: https://www.bitsavers.org/pdf/xerox/alto/Alto_Hardware_Manual_Aug76.pdf and Computer History Museum Alto archive copies
- Xerox, `Ethernet_Transceiver_Electrical_Characteristics.pdf`, archival index: https://www.bitsavers.org/pdf/xerox/alto/ethernet/
- Xerox inter-office memorandum, *Alto Ethernet Interface*, 22 June 1974, surviving in Alto memo archives; primary-archive identity still to be pinned down
- Bitsavers Xerox Alto collection: https://www.bitsavers.org/pdf/xerox/alto/

### Evidence rule

The 1976 Metcalfe/Boggs paper is strong contemporary evidence for the operating experimental network. The Alto manuals are strong implementation evidence for documented Alto revisions. The surviving transceiver electrical sheet should become the authority for exact analog/electrical parameters **only after its scan is visually verified and revision metadata established**.
