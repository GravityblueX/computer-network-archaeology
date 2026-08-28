# Fuzzball router internals: PDP-11, RT-11 virtual machines, zero-copy forwarding, HELLO, and NSFNET

> Status: active excavation. This chapter treats the Fuzzball as a **complete network system**, not a synonym for “old router.” David Mills' 1988 paper is unusually explicit about process structure, driver layering, routing, buffers, clocks and applications, while his surviving source archive makes implementation archaeology possible.

## 1. Fuzzball was an operating system and applications library

David Mills' 1988 description defines the Fuzzball as an **operating system and applications library for the PDP-11 family**. It usually ran on an LSI-11-class workstation and could act as:

- packet switch;
- Internet gateway/router;
- protocol-development platform;
- service host;
- terminal concentrator;
- monitoring/control node.

This is already enough to reject a modern oversimplification such as:

> “Fuzzball was routing software running under RT-11.”

The relation to RT-11 was more interesting: the Fuzzball provided a multi-user virtual-machine environment in which many RT-11 programs could run, while its own supervisor and network processes controlled the system beneath them.

## 2. Genealogy before NSFNET

Mills traces the system backward through several stages:

```text
1971 Edinburgh small-system work
        ↓
1975 University of Maryland DCN virtual-machine network
        ↓
1977 leaner rebuild + TCP/IP work + redesigned routing
        ↓
Fuzzball as Internet research platform
        ↓
SATNET / gateway experiments / campus use
        ↓
1986–1988 NSFNET Phase-I backbone routers
```

The name therefore refers to a long-lived evolving software family, not one immutable binary image.

## 3. Process model

The operating system contained:

- a **supervisor**;
- **supervisor processes**;
- **user processes**.

Supervisor processes handled device and network functions. User processes provided an RT-11-like virtual environment and hosted application programs.

Mills describes process address space in four segments:

- instruction segment;
- data segment;
- descriptor segment;
- parameter segment.

Descriptor and parameter areas carried scheduling state, memory descriptors, device parameters, counters and operator-visible status.

This matters because routing was embedded in a general-purpose experimental system with explicit operator control and measurement, not a sealed black-box appliance.

## 4. Scheduler and interprocess communication

The scheduler used multiple priority levels with preemptive round-robin service inside a priority level.

Processes communicated with **small 16-byte messages**, while exceptional conditions could be delivered as asynchronous interrupts useful for logging and alarms.

Synchronization used semaphore queues.

These details should eventually be mapped directly onto the source archive so that each design claim can be tied to assembler modules and data structures.

## 5. The network driver stack had three layers

One of the most valuable passages in Mills' paper is the network-software description.

Each network interface had a pair of supervisor driver processes:

- one input process;
- one output process.

The driver itself was conceptually layered:

```text
Internet-common layer
  routing / fragmentation / Internet errors
        ↓
local-network layer
  Ethernet / serial-line / other subnet behavior
        ↓
device-specific interrupt routines
  actual controller registers and interrupts
```

This is exactly the kind of boundary the archive should preserve for every router generation.

## 6. Zero-copy packet forwarding

Mills states that packets could enter directly into a buffer and leave from **the same buffer without copying**.

That detail is historically important. Resource limits on a PDP-11 made unnecessary memory copying expensive, and Fuzzball architecture deliberately separated protocol modules while sharing packet storage.

The forwarding path can therefore be conceptualized as:

```text
network-interface input DMA/driver
        ↓
packet buffer
        ↓
Internet processing / routing
        ↓
same packet buffer
        ↓
output driver
        ↓
network-interface transmission
```

Future work should determine when header rewriting or fragmentation forced additional buffer operations.

## 7. Internet, TCP, UDP and applications were all present

The Fuzzball was not a forwarding-only box.

Mills describes support for:

- IP;
- routing and fragmentation;
- TCP;
- UDP;
- TELNET;
- FTP;
- SMTP/mail services;
- EGP;
- DNS/name-resolution tools;
- time services;
- ICMP-based diagnostics including PING;
- experimental multimedia services.

A Fuzzball could therefore be configured as a router, host, experiment platform, or several of those simultaneously.

## 8. Hellospeak / HELLO routing

The DCN routing protocol was redesigned into what Mills calls **Hellospeak**. Later Internet documentation describes HELLO as a routing protocol used by the early NSFNET backbone.

Its notable metric was **delay in milliseconds**, rather than a simple hop count.

That choice tightly coupled routing and time measurement. If routers compare one-way or path delay, they need useful time information; the Fuzzball's routing experiments therefore helped drive sophisticated clock synchronization.

## 9. Timekeeping was an operating-system primitive

The Fuzzball included a logical clock incrementing at **1000 Hz**, with frequency and phase adjustment mechanisms.

This clock supported synchronization through routing/time protocols and later work related to NTP.

Thus the same system that forwarded packets also served as an experimental platform for one of the Internet's most important invisible infrastructures: synchronized time.

## 10. The NSFNET Phase-I node

Mills and Hans-Werner Braun's 1987 NSFNET paper describes the original backbone as a set of switching nodes at the six supercomputer sites:

- San Diego Supercomputer Center (SDSC);
- NCSA at Illinois;
- Cornell National Supercomputer Facility;
- Pittsburgh Supercomputer Center;
- John von Neumann Center;
- National Center for Atmospheric Research (NCAR).

The nodes were interconnected by **56 kbit/s internode trunks**. Additional development/test nodes brought the overall Fuzzball population involved with the project higher.

Each backbone node attached to an onsite **Ethernet**, which in turn connected supercomputers, campus hosts, and other gateways.

So a Phase-I path was approximately:

```text
regional/campus network
        ↓
site Ethernet
        ↓
Fuzzball PDP-11 router
        ↓
56 kbit/s serial backbone trunk
        ↓
remote Fuzzball
        ↓
remote Ethernet
        ↓
remote site / regional network
```

## 11. Hardware was not one universal PDP-11 configuration

Mills describes Fuzzballs as PDP-11/LSI-11 systems, but surviving configuration material shows multiple processors, memories, disk controllers, serial interfaces and Ethernet adapters across deployments.

A mature artifact catalog must therefore split:

- software family (`Fuzzball`);
- individual router instance;
- processor model;
- memory size;
- storage;
- line interface;
- Ethernet interface;
- clock hardware;
- installed software image/date.

The phrase “a Fuzzball router” is analogous to “a Unix router”: useful, but not a bill of materials.

## 12. Source code survives

This is one of the most important preservation facts in the whole network-archaeology project.

Mills' archive page provides a Fuzzball source archive described as roughly **16 MB** of source and binaries, with source in PDP-11 assembler and a last update in 1992.

The archive is organized into multiple directories and can be built with RT-11, directly or under simulation.

That means this subject can eventually be researched at three levels simultaneously:

1. published architecture paper;
2. actual source code/configuration;
3. reconstructed/emulated execution.

The third belongs primarily in the companion `protocol-zoo`/implementation work, while this repository should preserve versioned source provenance and implementation findings.

## 13. Why the first NSFNET overloaded

Mills' retrospective calls the original backbone dramatically overloaded. The 56-kbit/s links were carrying traffic associated with national supercomputer use and growing regional-network interconnection.

This congestion pressure made the network a real-world laboratory for:

- queue management;
- overload protection;
- routing based on measured conditions;
- packet-drop policy;
- traffic measurement.

The point is historically important: Internet congestion control did not emerge from abstract concern alone. Operational backbones produced pathological traffic that forced algorithmic adaptation.

## 14. Fuzzball as protocol laboratory

Mills credits Fuzzball deployments with experimental or prototype work involving Internet applications and protocols. The platform appeared in:

- packet-radio experiments;
- packet-satellite experiments;
- SATNET;
- INTELPOST;
- campus networking;
- NSFNET;
- gateway experiments;
- timing experiments.

This mobility is why a system originally intended as a “research pipewrench” became infrastructurally important.

## 15. Operator view: still to reconstruct

The architecture paper shows that parameter segments exposed counters and operational values, and that the system supported logging, alarms and remote services.

A future pass needs to reconstruct an actual operator session:

- boot sequence;
- RT-11/Fuzzball transition;
- console prompt;
- interface configuration;
- IP address configuration;
- route inspection;
- HELLO neighbor state;
- EGP peer state;
- packet/error counters;
- clock state;
- log and alarm messages;
- remote debugging;
- software update procedure.

Without this, we understand the protocol but not the machine room.

## 16. Build/deployment archaeology

The source archive raises additional questions:

- which RT-11 release was used to assemble each NSFNET image?
- which MACRO-11 toolchain revision?
- were images cross-built elsewhere and copied to removable media?
- which modules were enabled at each backbone site?
- how were configuration tables generated?
- how were emergency patches distributed?
- did sites keep local branches?
- how were crash dumps collected?

These are exactly the kinds of details that disappear when histories only record “NSFNET used Fuzzballs.”

## 17. Exact Phase-I hardware: unresolved

The archive currently has strong evidence for PDP-11/LSI-11 Fuzzball hardware and 56-kbit/s circuits, but **the precise per-site bill of materials still needs reconstruction**.

For every one of the six production nodes we want:

- processor model (`11/23`, `11/73`, or other);
- installed RAM;
- Q-bus/Unibus details;
- disk/floppy model;
- Ethernet adapter model;
- serial/WAN controller model;
- timing/clock board;
- CSU/DSU or telco termination equipment;
- rack/chassis;
- console terminal;
- software build identifier;
- IP addresses and interface names;
- circuit IDs if preserved.

Do not copy configuration examples from unrelated Fuzzballs onto NSFNET nodes without site-specific evidence.

## 18. From Fuzzball to the T1 NSS

The overloaded 56-kbit/s Fuzzball backbone was replaced by the Merit/IBM/MCI T1 architecture.

That replacement should be treated as an architectural transition, not merely a speed upgrade:

```text
Phase I
PDP-11 / Fuzzball
56 kbit/s trunks
site-local router node
        ↓
Phase II
IBM RT-based Nodal Switching Subsystem
T1 wide-area communications subsystem
centralized/distributed management architecture
```

The companion chapter `fuzzball-to-t1-nss.md` covers the backbone transition; this chapter supplies the missing internals of the Fuzzball side.

## 19. Open excavation checklist

1. Download and checksum the surviving Fuzzball source archive.
2. Produce a release/version chronology from source timestamps and comments.
3. Identify all network-interface drivers and supported controller models.
4. Map the three driver layers to actual assembler modules.
5. Reconstruct packet-buffer structures and zero-copy path.
6. Reconstruct HELLO/Hellospeak route tables, timers and update format.
7. Map EGP implementation modules and operational configuration.
8. Recover per-site NSFNET hardware inventories.
9. Recover per-site 56-kbit/s carrier equipment and circuit information.
10. Recover screenshots/photos/operator logs from production nodes.
11. Identify surviving physical Fuzzball machines and provenance.
12. Build a source-to-paper concordance: each architecture claim → assembler routine/data structure.
13. Preserve Mills' source archive metadata even if executable reconstruction lives elsewhere.

## Primary sources

- David L. Mills, *The Fuzzball* (SIGCOMM 1988): https://www.eecis.udel.edu/~mills/database/papers/fuzz.pdf
- David L. Mills, Fuzzball history/gallery: https://www.eecis.udel.edu/~mills/gallery/gallery10.html
- David L. Mills, collaboration resources / surviving Fuzzball source archive: https://www.eecis.udel.edu/~mills/resource.html
- David L. Mills and Hans-Werner Braun, *The NSFNET Backbone Network* (SIGCOMM 1987): https://www.ntp.org/reflib/papers/bone.pdf
- David L. Mills, RFC 891, *DCN Local-Network Protocols* (1983): https://www.rfc-editor.org/rfc/rfc891.html

Context/discovery:

- NSFNET History Project, Backbone: https://nsf.net/projects/backbone

### Preservation note

The source archive is historically exceptional because executable implementation evidence survives. Preserve checksums, timestamps, directory structure, toolchain assumptions and provenance before attempting modernization or cleanup.
