# Xerox PARC, 1973–1978: the 2.94 Mbit/s Alto Ethernet and PUP stack

> Status: active excavation. This chapter is intentionally about **the experimental Xerox Ethernet**, not later DIX Ethernet or IEEE 802.3. The goal is to reconstruct the actual Alto-era stack: coax, transceiver, interface logic, microcode, packet conventions, PUP internetworking, gateway hosts, and higher-level protocols.

## 1. Do not project 10BASE5 backward into 1973

The word **Ethernet** changed underneath its own success.

A modern summary often jumps from Bob Metcalfe's 1973 memo directly to 10 Mb/s Ethernet. That erases the system that actually ran at Xerox PARC during the Alto era.

The Alto Hardware Manual describes an Ethernet with these characteristics:

- **2.94 Mbit/s** channel;
- broadcast, multi-drop, bit-serial packet network;
- up to **256 nodes**;
- roughly **1 km** extent;
- passive shared medium;
- distributed access control;
- best-effort delivery rather than guaranteed delivery.

This is the network this chapter means by *experimental Ethernet*.

## 2. The 1973 memo begins as “Alto Aloha Network”

Bob Metcalfe's 22 May 1973 internal memo is famous partly because it shows the design before its vocabulary stabilized. The memo was addressed to **ALTO ALOHA DISTRIBUTION** and discussed the “Alto Aloha Network.”

That title is not trivia. It preserves the intellectual path from packet radio and random-access ALOHA ideas into a wired local broadcast medium.

The repository should preserve the name sequence rather than rewriting every early document as though “Ethernet” had always been the settled term.

## 3. Physical stack: Ether → transceiver → Alto interface → microcode

The 1979 Alto Hardware Manual explicitly says an Alto Ethernet comes in **three pieces**:

1. the **transceiver**;
2. the **interface**;
3. the **microcode**.

Conceptually:

```text
shared coaxial Ether
        ↕
transceiver attached to the passing medium
        ↕
Alto Ethernet interface electronics
  FIFO / shift registers / CRC / clock recovery
        ↕
Ethernet microcode task
        ↕
Alto main memory buffers
        ↕
software packet protocols
```

This decomposition is crucial. “Ethernet card” is an anachronistic compression of multiple separately understandable mechanisms.

## 4. The transceiver was deliberately generic

The Alto manual says the transceiver tapped the passing Ether, inserted and extracted bits, and was intended to disturb the medium as little as possible. The same transceiver design could be used by different kinds of Ethernet interfaces, not only Altos.

This hints at an early separation between:

- medium attachment;
- station-specific interface/controller;
- software protocol.

A complete artifact record still needs the exact transceiver electrical specification, connector/tap construction, coax type, signal levels, collision-detection circuitry, cable-spacing constraints, terminators, and surviving specimen photographs.

## 5. Alto interface hardware

Section 7.2 of the Alto Hardware Manual identifies the hardware blocks:

- FIFO buffer;
- output shift register;
- phase encoder;
- clock-recovery circuit;
- input shift register;
- CRC register;
- an Ethernet microcode task.

Packets were **phase encoded** and transmitter-synchronous. The receiver had to determine packet start, recover the clock, and deserialize the bit stream.

The FIFO was not decorative. The manual explains that the Ethernet task had relatively low microprocessor priority and could experience worst-case wake-up latency on the order of tens of microseconds; buffering bridged the line-rate hardware and the shared Alto microprocessor.

## 6. A packet begins with a sync bit

The Alto hardware prefixed a single sync bit to each transmission. Receiver logic used transitions to detect the packet envelope and establish clock phase.

This is another reason not to paste a modern Ethernet frame diagram over the early system. The physical and framing conventions evolved.

## 7. CRC lived in the bit-serial hardware

The interface included CRC generation/checking. The Alto status byte exposed a CRC-bad condition to software.

This distinction later becomes especially clear when PUP is layered above Ethernet:

- Ethernet CRC protects a frame while it traverses an Ethernet;
- the PUP checksum is an end-to-end internetwork checksum carried across different underlying networks.

They are not redundant copies of the same mechanism.

## 8. The Alto's Ethernet controller was partly microcode

Programs did not manipulate every signal directly. They communicated with the Ethernet interface/microcode through the Alto `SIO` instruction plus reserved memory locations.

The manual records locations for:

- completion/status;
- interrupt mask;
- end count;
- retransmission load/backoff state;
- input buffer count;
- input buffer pointer;
- output buffer count;
- output buffer pointer;
- host address.

This provides unusually concrete evidence for how network I/O was exposed to software.

## 9. Hardware host address, set by backplane wiring

The Alto's Ethernet host address was returned by `SIO` and was physically set by wires on the backplane. Software normally copied that value into the receive-filter location.

The packet's first word conventionally contained:

- destination in the left byte;
- source in the right byte.

Special addresses included:

- destination `0`: broadcast;
- a reserved Ethernet boot destination;
- a reserved diagnostic destination.

The manual also describes a mode in which address filtering could be disabled so the machine received packets regardless of destination — recognizably what later networking calls **promiscuous mode**.

## 10. Collision handling was visible to software and microcode

The controller detected collisions. The microcode used a growing mask/state value to generate randomized retransmission intervals.

The manual exposes collision behavior in status fields and records a failure condition after **16 consecutive collisions** for a transmit attempt.

This means the classic Ethernet story — listen, transmit, detect conflict, back off randomly — was not only a mathematical idea. It existed as:

- collision-detection circuitry;
- microcode state;
- memory-resident control values;
- software-visible status.

That whole chain belongs in the archaeological record.

## 11. Receive and transmit contend for one interface

The Alto controller did not behave like a modern full-duplex NIC. The manual describes software/microcode coordination between receiver and transmitter, including cases where an incoming packet could abort a pending transmission attempt while the machine was in a random backoff interval.

That operational detail is more revealing than a generic “CSMA/CD” label because it tells us what an actual station had to do.

## 12. Ethernet packet conventions were smaller and simpler than modern frames

The Alto manual gives software conventions layered on the bare frame:

- first word: destination byte + source byte;
- second word: **type word**;
- payload follows;
- physical interface handles CRC.

The type word was a software convention; the hardware did not interpret it.

For PUP, the type word value was assigned to identify the payload as a PUP packet.

Again, do not substitute later EtherType field widths/assignments without version labels.

## 13. PUP: Ethernet was local; PUP was internetworking

The **PARC Universal Packet (PUP)** suite is the key to understanding why Xerox's networking history is larger than Ethernet.

A PUP specification memo states that PUP was intended to allow processes on Xerox's interconnected computers to exchange packets through **multiple interconnected packet-switching networks**. Gateway hosts forwarded PUPs between those networks.

The core architecture is strikingly explicit:

1. use a standard internetwork packet (the PUP);
2. make packet communication end-to-end;
3. require the internetwork only to make a best effort to move independently addressed packets;
4. put whatever reliability applications need into higher-level end protocols.

This is not merely a LAN protocol. It is an internetwork architecture.

## 14. PUP packet format

The 1978 PUP specification shows a **20-byte header**, followed by up to 532 content bytes and a checksum.

Major fields include:

- Pup Length;
- Transport Control;
- Pup Type;
- 32-bit Pup Identifier;
- Destination Network;
- Destination Host;
- Destination Socket;
- Source Network;
- Source Host;
- Source Socket;
- contents;
- optional pad/garbage byte for 16-bit alignment;
- Pup Checksum.

A PUP port therefore identifies not just a host but a process endpoint using **network + host + socket**.

## 15. PUP hop count and gateway behavior

The Transport Control field included a gateway-count mechanism. The specification says a packet reaching its 16th gateway would be discarded.

At a gateway, a PUP was conceptually:

1. decapsulated from the incoming network;
2. routed toward another network;
3. re-encapsulated for the outgoing network.

That is a clean example of network-independent internetwork packet handling.

## 16. One PUP, several transporting networks

The PUP specification explicitly describes encapsulation over multiple underlying systems.

### Ethernet

An immediate Ethernet destination and source surround the PUP, with a type identifying PUP and an Ethernet CRC protecting the local traversal.

### ARPANET

PUP could also be carried through ARPANET messages. The specification records an ARPANET link value reserved to identify PUP traffic.

### Low-speed synchronous links

The document also describes encapsulation over lower-speed synchronous lines using a subset of BiSync-style framing plus network-specific line control.

This is the conceptual picture:

```text
          Ethernet A
             │
             │ PUP
             ▼
          Gateway
         /       \
 PUP over ARPANET  PUP over sync line
       │                 │
       ▼                 ▼
 remote network      remote network
```

The internetwork packet survives while link framing changes.

## 17. Reliability: Ethernet and PUP both admit loss

The Alto Hardware Manual states plainly that Ethernet is **not error-free** and packets are delivered only with high probability.

The PUP specification makes the same architectural assumption at internetwork level: PUPs may be lost, reordered, or discarded because of checksum failure or resource shortage. End processes are responsible for protocols providing the reliability they need.

That layering should be preserved precisely:

```text
Ethernet: best-effort local packet delivery
        ↓
PUP: best-effort internetwork datagram
        ↓
PUP Byte Stream / other higher protocols:
reliability, flow control, application semantics
```

## 18. PUP checksum vs Ethernet CRC

The PUP checksum is a 16-bit one's-complement add-and-cycle checksum intended as an **end-to-end check** across intermediate hardware and software.

The PUP document explicitly distinguishes it from a transporting network's own error mechanism. On Ethernet, therefore:

```text
Ethernet CRC
  protects local Ethernet frame traversal

PUP checksum
  travels with the internetwork packet end-to-end
```

This is a beautiful early example of layered error detection.

## 19. Echo, rendezvous, byte streams

The PUP specification does not stop at the network packet.

It also records higher-level protocols including:

- Echo for diagnostics;
- Rendezvous/Termination for establishing and closing logical connections;
- Byte Stream for reliable, flow-controlled byte transport.

The Byte Stream layer has acknowledgments and allocation information governing how much data the receiver is prepared to accept.

A future protocol-zoo implementation can recreate these; this repository's role is to preserve the specification genealogy, actual implementations, services, and surviving source code.

## 20. Alto networking was already an internet, not just an Ethernet

By the late 1970s, the Alto Hardware Manual says most Ethernets were interconnected by gateways and leased lines to form a nationwide **internet** inside the Xerox research environment.

The manual also lists optional Alto communications controllers for:

- BBN-1822;
- SDLC;
- BiSync;
- Async.

Larry Stewart is credited with the Alto BBN-1822 interface.

This means an Alto could participate in a much richer communications ecosystem than “one coax cable in PARC.”

## 21. Physical/electrical archaeology still needed

The next pass must recover the actual 1973–76 hardware documents:

### medium
- coax type and impedance;
- segment length;
- topology/branching rules;
- terminators;
- tap construction and spacing;
- grounding;
- cable routing through PARC buildings.

### transceiver
- schematic;
- transmitter drive level;
- collision detection;
- receive threshold;
- isolation;
- cable between transceiver and station interface.

### Alto interface
- logic schematics;
- IC families;
- FIFO depth;
- CRC polynomial and implementation;
- phase encoder/decoder details;
- exact clock frequency relation to 2.94 Mb/s;
- backplane connector/pinout;
- host-address wiring.

### microcode
- Ethernet task source;
- random-backoff algorithm;
- buffer-copy loop;
- receive filtering;
- error/status posting;
- changes across Alto microcode releases.

## 22. Version genealogy to preserve

Do not merge these into one generic Ethernet record:

1. May 1973 Alto Aloha / Ethernet concept memo;
2. June 1974 Alto Ethernet Interface memo;
3. operating 2.94 Mb/s PARC Ethernet generation;
4. 1976 Metcalfe/Boggs published system description;
5. PUP internetwork deployment over experimental Ethernet;
6. DIX 10 Mb/s Ethernet specification (1980);
7. IEEE 802.3 lineage;
8. 10BASE5 commercial hardware;
9. later bridges, twisted pair, switching and full duplex.

The winning name survived while most physical details changed.

## 23. Surviving-source ecosystem

The Xerox Alto archive maintained by the Computer History Museum is extraordinarily valuable because it preserves not only prose histories but hardware manuals, PUP specifications, software trees, and protocol memoranda.

This repository should eventually inventory:

- each Ethernet hardware memo;
- transceiver drawings;
- microcode source;
- Alto OS network drivers;
- PUP gateway implementations;
- PUP services;
- Ethernet diagnostics and boot protocols;
- photographs and surviving physical transceivers/taps;
- source snapshots by date.

## 24. Open excavation checklist

1. Recover the complete 22 May 1973 `Ether Acquisition` memo with page-level provenance.
2. Recover the June 1974 Alto Ethernet Interface memo from a primary archive.
3. Mine `Ethernet_Transceiver_Electrical_Characteristics.pdf` and record every physical parameter.
4. Identify coax, connectors, tap hardware, and terminators by vendor/model where possible.
5. Recover Ethernet interface schematics and PCB photographs.
6. Extract Ethernet microcode from Alto source trees and map it against the 1979 manual.
7. Build a revision table for host-address conventions and packet type assignments.
8. Record PUP gateway host models and physical interfaces.
9. Recover early PUP specification editions before the 1978 update.
10. Catalog PUP services and source implementations.
11. Trace PUP/XNS genealogy without treating them as identical.
12. Record surviving original PARC Ethernet hardware with museum provenance.

## Primary sources

- Xerox PARC, *Alto Hardware Manual* (1979), especially Section 7, Ethernet: https://xeroxalto.computerhistory.org/_cd8_/altodocs/.altohardware.press%212.pdf
- Ed Taft and Bob Metcalfe, *Pup Specifications* (30 June 1978, updating the 20 October 1975 version): https://xeroxalto.computerhistory.org/_cd8_/pup/.pupspec.press%211.pdf
- Bob Metcalfe, 22 May 1973 Ethernet concept sketch/memo context, preserved by DigiBarn with PARC provenance: https://www.digibarn.com/collections/diagrams/ethernet-original/
- Robert Metcalfe and David Boggs, *Ethernet: Distributed Packet Switching for Local Computer Networks* (1976), text mirror: https://www.cs.cornell.edu/courses/cs414/2002sp/papers/ethernet/ethernet.htm
- Bitsavers Xerox Alto Ethernet document index: https://bitsavers.trailing-edge.com/pdf/xerox/alto/ethernet/

### Rights note

Many Xerox/PARC and ACM documents remain copyrighted. This repository should index and describe them, link to lawful archival access, and mirror only when rights permit.
