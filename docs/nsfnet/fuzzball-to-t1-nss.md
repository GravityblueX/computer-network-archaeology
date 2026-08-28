# NSFNET: from Fuzzball routers to the IBM RT Nodal Switching Subsystem

NSFNET is often summarized as “the backbone that replaced ARPANET.” That hides one of the most useful hardware transitions in network history: a small 56 kbit/s research backbone built from David Mills' **Fuzzball** routers was rapidly replaced by a 1.544 Mbit/s T1 system whose nodes were themselves clusters of IBM RT computers.

The change shows the Internet outgrowing research hardware in real time.

## Phase 1: the 56 kbit/s backbone

The first NSFNET backbone became operational in 1986 to connect NSF supercomputer centers and surrounding academic networks.

The backbone used **56 kbit/s leased circuits** and routers running David L. Mills' Fuzzball software on DEC PDP-11/LSI-11-class machines.

A simplified site looked like:

```text
campus / supercomputer-center Ethernet
              ↓
        Fuzzball router
              ↓
       56 kbit/s serial circuit
              ↓
        Fuzzball router
              ↓
remote center / regional network
```

This was Internet technology deployed as a national research backbone, but on hardware modest enough that overload quickly became a defining operational fact.

## The Fuzzball was an operating system as much as a router

“Fuzzball” refers to Mills' compact networking software environment for PDP-11/LSI-11 systems. It was not merely one routing daemon.

The surviving Fuzzball material includes networking, routing, monitoring and timing work accumulated through years of experiments. Mills' own archive describes source and binaries surviving into the present.

This makes Fuzzball unusually attractive for archaeological reconstruction because the software corpus may be recoverable well enough to run in emulation later in `protocol-zoo`.

## Backbone routing

The original NSFNET Fuzzballs used the **HELLO** routing protocol within the backbone environment.

This creates an important historical cross-link with routing protocol evolution:

```text
GGP / early core routing
       ↓
HELLO / EGP-era Internet
       ↓
NSFNET scaling pressure
       ↓
BGP-era interdomain routing
```

The 56 kbit/s NSFNET was already exposing the limitations of a growing Internet organized around a relatively small set of coordinated routing systems.

## Congestion became the experiment

Mills later described the original NSFNET as “gloriously overloaded.”

That is more than a colorful phrase. The backbone became a laboratory for queue management and congestion behavior because supercomputer transfers could behave like enormous flows among smaller interactive traffic.

The Fuzzball papers discuss queueing, preemption and source-quench-related control mechanisms used to keep overload from simply destroying service.

This belongs in the same history as the wider 1980s TCP congestion-collapse crisis and Van Jacobson's later transport-layer congestion-control work.

## Why 56 kbit/s stopped being enough

Regional academic networks attached rapidly. Traffic growth outpaced the original backbone.

NSF therefore funded a major upgrade through **Merit Network**, **IBM**, and **MCI**.

The T1 backbone entered service in 1988 with circuits at **1.544 Mbit/s**, an enormous step over the 56 kbit/s system.

But the new architecture was not simply “replace PDP-11 with one faster router.”

## Nodal Switching Subsystem (NSS)

The T1 backbone's node was called a **Nodal Switching Subsystem**.

Merit's historical report describes an NSS as a coordinated group of IBM RT systems connected internally, with redundancy and specialized roles.

A typical node used multiple **IBM RT PC** machines — often described as roughly nine systems acting together — rather than one monolithic router.

Conceptually:

```text
regional / campus network interfaces
             ↓
   [ IBM RT ][ IBM RT ][ IBM RT ]
        \       |       /
         internal LAN / coordination
        /       |       \
   [ IBM RT ][ IBM RT ][ IBM RT ]
             ↓
         T1 backbone links
```

The exact node composition changed, and backup systems could be present in addition to the primary set.

## Why use multiple computers inside one backbone node?

The architecture separated functions and provided redundancy while allowing a system to be assembled from available commercial computers.

The node therefore sits between two eras:

- earlier research routers built from one small general-purpose computer;
- later carrier routers with specialized backplanes and forwarding hardware.

The IBM RT NSS was effectively a packet-switching system built out of a small local network of computers.

## The T1 backbone as a hierarchy

NSFNET's importance was also organizational.

Rather than connect every university directly to one national network, the system encouraged a hierarchy:

```text
campus network
     ↓
regional / midlevel network
     ↓
NSFNET backbone
     ↓
other regions / external Internet
```

This architecture distributed both cost and administration.

Examples of midlevel/regional networks included SURAnet, NYSERNet, BARRNet, MIDnet, Westnet and others.

The Internet was becoming a federation of administratively distinct networks rather than one centrally operated packet network.

## Merit + IBM + MCI = protocol history is also procurement history

The backbone existed because three different competencies were combined:

- **Merit** — network operations, routing, coordination and academic-network experience;
- **IBM** — computing hardware and engineering support;
- **MCI** — long-haul telecommunications circuits and carrier infrastructure.

That institutional stack matters as much as TCP/IP.

When reconstructing a backbone, always ask:

- who owned the routers?
- who maintained the computers?
- who supplied the circuits?
- who staffed the NOC?
- who paid for regional attachment?
- what happened when responsibility crossed organizational boundaries?

## From T1 to T3

Traffic growth continued. A **T3 / 45 Mbit/s** backbone followed in the early 1990s.

The hardware changed again: RS/6000-class systems and a redesigned architecture replaced the large multi-RT T1 node configuration.

This gives NSFNET a remarkably compact speed/hardware ladder:

```text
1986: 56 kbit/s
      PDP-11/LSI-11 Fuzzball routers

1988: 1.544 Mbit/s T1
      multi-IBM-RT Nodal Switching Systems

1991: 45 Mbit/s T3
      RS/6000-era backbone nodes
```

Each transition deserves a separate bill of materials.

## Why the backbone ended

NSFNET was not intended to remain the permanent commercial core of the Internet.

During the early 1990s, private backbone providers, exchange points and the NAP model expanded. The NSFNET backbone service was retired on **30 April 1995**.

The physical shutdown is a better historical marker than saying vaguely that “the Internet became commercial.”

## Sources

1. NSFNET historical project, **Internet Backbone**: <https://nsf.net/projects/backbone>
2. NSFNET historical timeline: <https://nsf.net/timeline>
3. David L. Mills, **The Fuzzball** archive/history: <https://www.eecis.udel.edu/~mills/gallery/gallery10.html>
4. D. L. Mills and H.-W. Braun, **The NSFNET Backbone Network** (SIGCOMM 1987), surviving copies referenced from the Fuzzball archive.
5. Merit Network, **NSFNET: A Partnership for High-Speed Networking**: <https://www.merit.edu/wp-content/uploads/2024/10/Merit-Network_NSFNET-A-Partnership-for-High-Speed-Networking.pdf>
6. Internet Society interview/history of Hans-Werner Braun and NSFNET: <https://news.internetsociety.org/increasing-growth-speed-coverage-and-reliability-hans-werner-braun-and-the-development-of-the-nsfnet/>

## Unresolved excavation tasks

### Fuzzball phase

- identify exact PDP-11/LSI-11 model at every backbone site;
- identify Ethernet controllers and serial-line interfaces;
- document DDCMP use on 56 kbit/s trunks;
- recover site configuration files and routing tables;
- recover HELLO protocol parameters;
- reconstruct monitoring displays and statistics collection;
- preserve Fuzzball source and build instructions with checksums;
- document surviving physical Fuzzball machines.

### T1 NSS phase

- produce a per-site bill of materials;
- recover exact count and role of IBM RT systems in each NSS revision;
- document the internal Token Ring or other node interconnect precisely;
- identify T1 interfaces/channel equipment and MCI circuit termination;
- document redundancy/failover behavior;
- recover routing software and management software;
- reconstruct NOC consoles and operational escalation;
- archive topology maps month by month.

### T3 phase

- identify RS/6000 models and interfaces;
- document 45 Mbit/s carrier technology and node architecture;
- trace ANS/ANS CO+RE operational boundaries;
- document FIX-E/FIX-W and NAP transition.

NSFNET's hardware history is the story of Internet growth becoming visible as metal: **one PDP-11 router stopped being enough, then a roomful of RTs stopped being enough, and the backbone had to change again.**