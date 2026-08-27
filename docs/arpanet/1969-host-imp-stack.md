# ARPANET 1969: Reconstructing the Host–IMP Boundary

This is the first deliberately **deep** excavation in the repository. The goal is to show what “connect a host to ARPANET” meant before networking interfaces became standardized commodity hardware.

The central lesson is simple:

> An ARPANET node was not “a computer plugged into a router.” It was a negotiated boundary between a host operating system, site-specific interface hardware, BBN's IMP design, and leased communications infrastructure.

## 1. The archaeological stack

A useful reconstruction begins with separate objects:

```text
user program / terminal-facing subsystem
              ↓
       host operating system
              ↓
       network program
              ↓
        handler program
              ↓
site-specific Host–IMP channel hardware
              ↓
       Interface Message Processor
              ↓
        line interface / data set
              ↓
      leased communications circuit
              ↓
        remote IMP and host
```

The words in this diagram come from different administrative and engineering layers. Treating all of them as one generic “network stack” destroys evidence.

## 2. RFC 1 captures the design while it is still unstable

Steve Crocker's RFC 1, dated **7 April 1969**, explicitly describes the host-software agreements as tentative. It says BBN had responsibility for IMP software while individual host groups still needed to agree on host software. It also names the initial-site working group and separately notes Gerard DeLoche's work on the Host–IMP interface.

Primary source: https://www.rfc-editor.org/rfc/rfc1.txt

That means the documentary strata should be read this way:

```text
BBN IMP specification
        +
site Host–IMP hardware design
        +
site operating-system handler
        +
Network Working Group host protocol
        =
usable ARPANET host
```

No single document necessarily defines the whole thing.

## 3. Message is not packet

RFC 1 uses two distinct units:

- a **host-to-host message** supplied to an IMP;
- one or more **packets** used between IMPs.

The April 1969 description allows a message data stream up to **8080 bits**, plus a 16-bit host header. The destination IMP divides that material into packets of at most **1010 bits** for IMP-to-IMP transport and reassembles them before delivery.

Primary source: https://www.rfc-editor.org/rfc/rfc1.txt

This distinction matters historically because a modern reader may instinctively call everything a packet. Contemporary terminology exposes where segmentation/reassembly responsibility lived.

## 4. The 16-bit host header

RFC 1's described header contains:

| Field | Width | Historical function |
|---|---:|---|
| destination | 5 bits | numerical destination host code |
| link | 8 bits | logical link identifier |
| trace | 1 bit | request measurement/status tracing |
| spare | 2 bits | unused in this description |

The trace facility could cause IMPs to collect status information for the Network Measurement Center at UCLA.

This tiny header should eventually be compared against later IMP-host formats; do not assume it remained unchanged.

## 5. Thirty-two logical links and RFNM

The April design describes **32 logical full-duplex links between a pair of hosts**. An IMP would not accept another successive message on the same link until a special **RFNM — Request for Next Message** returned from the destination side.

That mechanism is an early, very concrete example of flow/congestion control at the host/IMP service boundary.

Important nuance: RFC 1 itself points out that the mechanism cannot magically prevent every overload case. It assumes host cooperation.

## 6. Error checking exists at more than one boundary

RFC 1 describes a **24-bit cyclic checksum** generated and checked by IMP transmission hardware for IMP-to-IMP packets.

The host-software discussion nevertheless asks for additional host-to-host checking, specifically because the Host–IMP path and software interfaces remain outside that link checksum's guarantee.

This is a useful general rule for the whole repository:

> “The network checks errors” is meaningless unless we specify **which segment, which unit, and which layer**.

## 7. RFC 7 exposes the UCLA host-side implementation problem

RFC 7, *Host-IMP Interface*, dated **May 1969**, is especially valuable because the surviving text is a reconstruction from a partially illegible handwritten original. The RFC Editor explicitly records this textual history.

Primary source: https://www.rfc-editor.org/rfc/rfc7.txt

The preliminary UCLA software organization separates two major host-side components:

- a **Network program**, which multiplexes user requests and prepares/receives network messages;
- a **Handler program**, which directly drives the channel hardware and responds to I/O interrupts.

They communicate through a pool of buffers and an interface table.

Already, before the first famous ARPANET login, there is a recognizably complex device-driver/OS/network boundary.

## 8. The Sigma 7 implementation is machine-specific

RFC 7 is not an abstract universal host adapter specification. It is rooted in UCLA's **Sigma 7** environment.

The document discusses:

- privileged handler code integrated with the I/O supervisor;
- a special channel hardware unit;
- interrupts;
- buffers;
- MIOP/SIOP attachment questions;
- user-to-network program interfaces.

This is exactly why the first four ARPANET hosts must be excavated separately. The IBM 360/75 at UCSB and PDP-10 at Utah did not magically share UCLA's Sigma 7 I/O architecture.

## 9. A useful host-side data path

RFC 7 suggests a workflow that can be reconstructed abstractly as:

```text
user process wants to transmit
        ↓
Network program receives text location / length / destination
        ↓
Network program prepares host heading and message buffers
        ↓
interface table identifies buffer and length
        ↓
Handler program drives special channel hardware
        ↓
Host–IMP electrical transfer
        ↓
IMP receives host message
```

The receive direction mirrors this structure.

This is not yet a Berkeley socket API. Application-to-network access is being designed simultaneously with the packet network itself.

## 10. Character encoding was not a solved background detail

RFC 7's preliminary design even discusses converting **EBCDIC characters to ASCII** in outgoing material.

That one detail points to a whole archaeological field:

- different hosts may use different native encodings;
- terminal conventions differ;
- byte size assumptions are not universal;
- “send text” may require conversion at a site boundary;
- later protocol design increasingly tries to define canonical network representations.

Encoding history belongs inside network history.

## 11. Buffer sizes are architecture

RFC 7 derives a host-side buffer large enough to contain the then-maximum host message plus heading/marking and proposes a **1024-byte / 256-word** buffer size for the Sigma 7-side implementation.

That is not trivia. Buffer size affects:

- memory pressure;
- how many links can remain active;
- I/O scheduling;
- interrupt frequency;
- maximum transmission units;
- throughput under contention.

A future site reconstruction should therefore include host memory allocation and channel behavior, not only packet fields.

## 12. The unresolved questions are as valuable as the answers

RFC 7 leaves basic questions open about:

- error behavior on the Host–IMP transfer;
- where the special channel hardware should attach;
- how end-of-message is signaled;
- how incoming message length is known;
- operating-system mechanisms needed by the network program.

The unfinished state is historically important. It prevents us from projecting the eventual implementation backward into spring 1969.

## 13. Terminal history is embedded inside host protocol design

RFC 1 imagines an initial simple service in which a remote host can behave roughly as though a teletype user had dialed it directly. It reserves one logical link for operating-system coordination and uses other links for TTY-like or file-oriented connections in the tentative design.

This shows continuity with the pre-network world:

```text
1950s/60s remote terminal logic
           ↓
ARPANET TTY-like remote use
           ↓
Telnet / network virtual terminal abstractions
           ↓
terminal servers / remote login
```

The Internet does not erase terminal history; it absorbs it.

## 14. RFC 1 also contains an unrealized distributed-front-end idea

One of the document's most revealing sections is its concern that remote interactive graphics would feel terrible if every trivial keystroke/echo required a roughly long network round trip. The proposed direction, called **DEL**, would let some terminal-control behavior execute locally while significant work remained remote.

Whether or not DEL became the path ultimately taken, the design problem survives today in many forms:

- local echo;
- terminal emulation;
- client-side input handling;
- remote desktop prediction;
- edge computation.

Dead proposals are therefore worth preserving because they reveal which performance problems engineers already understood.

## 15. What still has to be found before this is a true 1969 reconstruction

This article is **not complete** until the following are located and linked:

### BBN side
- BBN Report 763 referenced by RFC 7;
- exact IMP Host interface electrical specification;
- DDP-516 I/O modifications;
- IMP memory configuration in the first delivered UCLA unit;
- line-interface/data-set model;
- IMP bootstrap and diagnostic procedures;
- software revision installed in September 1969.

### UCLA side
- special Sigma 7 Host–IMP interface schematics;
- MIOP/SIOP attachment documentation;
- Gerard DeLoche's additional notes;
- UCLA Network Measurement Center tooling;
- Sigma 7 OS/network program source or listings;
- installation photographs with identifiable cabling/cards.

### Telephone/carrier side
- exact 50 kbit/s circuit service description;
- carrier/provider;
- modem/data-set models;
- clocking/interface standard;
- demarcation and maintenance procedures.

### Operational side
- first IMP installation log;
- first host/IMP loopback or connectivity tests;
- exact sequence from IMP arrival to host-ready state;
- fault reports before the October UCLA–SRI experiment.

## 16. Why this level of detail matters

If all of those layers are recovered, the famous 1969 diagram stops looking like four circles joined by lines. It becomes a physical system:

```text
human / terminal
      ↓
Sigma 7 software
      ↓
site-built interface hardware
      ↓
DDP-516 IMP
      ↓
telecommunications termination equipment
      ↓
50 kbit/s leased circuit
      ↓
remote IMP
      ↓
remote host adapter + OS
```

That is the level at which “the first Internet history” becomes **infrastructure archaeology**.

## Primary sources used

- Steve Crocker, RFC 1, *Host Software*, 7 April 1969: https://www.rfc-editor.org/rfc/rfc1.txt
- Gerard DeLoche, RFC 7, *Host-IMP Interface*, May 1969: https://www.rfc-editor.org/rfc/rfc7.txt

## Research status

**Started / primary-source grounded, but hardware/carrier layer still incomplete.**

Next excavation target: **BBN Report 763 and the exact UCLA Sigma 7 ↔ IMP electrical interface.**