# 1960s: From Remote Terminals to Packet Switching

The 1960s are the decade in which computer communication stops being merely “a terminal reaches a central machine” and begins to become “computers share a network”. The transition is gradual and messy: time-sharing, leased lines, modem access, message switching, packet-switching theory, heterogeneous hosts and interface processors coexist.

## 1. Time-sharing changes the social meaning of a computer

A batch computer is used indirectly: prepare a job, submit it, wait. Time-sharing turns the computer into an interactive service. That immediately makes communications engineering important.

A simplified access path becomes:

```text
user
  ↓
terminal / teletype
  ↓ modem or leased line
communications controller / terminal multiplexer
  ↓
time-sharing host
```

The historical importance is not just convenience. Once many remote people depend on one computer, designers must care about:

- interactive latency;
- echo behavior;
- terminal character handling;
- connection setup/teardown;
- multiplexing many sessions;
- authentication/accounting;
- line cost;
- fault isolation;
- host front-end load.

## 2. CTSS, Project MAC and the network-computing imagination

MIT's Compatible Time-Sharing System and Project MAC made interactive shared computing a major research environment. J. C. R. Licklider's ARPA work is important not because one memo “invented the Internet”, but because he helped frame computers as interactive communication partners and resources that might be accessed across distance.

Future excavation should distinguish:

- Licklider's written concepts;
- ARPA program administration;
- actual terminal/host technology available at the time;
- later recollections that retrospectively sound more Internet-like than contemporary implementation permitted.

## 3. The line-utilization problem

Computer traffic is bursty. A human types, pauses, thinks, then sends more characters. A program may send a large block and then wait.

Traditional circuit switching allocates an end-to-end channel whether or not useful bits are flowing. That makes sense for continuous voice conversations; it can be wasteful for bursty data.

The packet-switching question can therefore be stated economically as well as technically:

> Can many conversations statistically share the same expensive transmission capacity?

This is one reason packet switching became attractive.

## 4. Paul Baran and distributed communications

RAND's Paul Baran studied survivable distributed communications and proposed dividing traffic into standardized message blocks that could travel through a distributed network.

The historical relationship to later packet switching must be narrated carefully:

- Baran's work emerged from survivable military-communications research;
- Donald Davies later coined and developed the “packet” concept independently in the UK;
- ARPANET design drew from a broader environment of ideas, engineering needs and people;
- “ARPANET was built to survive nuclear war” is an oversimplification that should not be repeated as a substitute for project history.

Primary target: RAND's original *On Distributed Communications* report series.

## 5. Donald Davies and NPL

NPL's institutional timeline dates Donald Davies and team's development of packet switching to **1965**.

Source: https://www.npl.co.uk/about-us/history/timeline

The core move is to split a message into small packets that can share links with other traffic and be recombined at the destination.

Important excavation questions:

- when “packet” first appears in surviving NPL documentation;
- exact packet size/format in successive NPL designs;
- switching-node hardware;
- line speeds;
- routing;
- buffering;
- host interface;
- measurement results;
- influence on ARPANET designers;
- differences between proposed and deployed NPL systems.

NPL's timeline places the NPL Data Communications Network operational milestone at **1970**, so its design belongs in the 1960s even though its mature operation crosses into the next decade.

## 6. Why packet switching is not just “breaking data into packets”

The deeper architecture includes at least these questions:

1. Who chooses the route?
2. Does every packet choose independently?
3. Does the network preserve order?
4. How much buffering exists inside switching nodes?
5. What happens on congestion?
6. Who retransmits after an error or loss?
7. Does the network promise reliability?
8. How does a host identify a destination?
9. How large is a packet?
10. How are hosts protected from one another's traffic?

Different networks answered differently. That diversity later produces the datagram/virtual-circuit and end-system/network-intelligence debates.

## 7. ARPA decides to network heterogeneous research computers

ARPA's challenge was not to build another centrally controlled terminal system. It wanted expensive research computers at multiple sites to communicate and share resources.

The hosts were heterogeneous:

- different manufacturers;
- different word sizes;
- different operating systems;
- different terminal conventions;
- different local applications.

This made a separate packet-switching node attractive: the host could connect to a standard-ish interface processor instead of every host team reinventing the entire WAN.

## 8. BBN and the Interface Message Processor

Bolt Beranek and Newman won the contract to build the ARPANET Interface Message Processors (IMPs). RFC 2555's retrospective on the RFC series describes IMPs as forerunners of modern routers, refrigerator-sized and roughly $100,000 devices in 1969.

Source: https://www.rfc-editor.org/rfc/rfc2555.html

The modern “router” analogy is useful but incomplete. The IMP was a particular packet switch with ARPANET-specific host interfaces, message handling, routing, monitoring and flow-control behavior.

### Original hardware line

The early IMP used the Honeywell DDP-516, ruggedized for network-node service. Later variants and Honeywell 316/Pluribus generations need separate records.

### Why the IMP is a historical boundary object

It sits between:

```text
host architecture
    ↕ Host–IMP interface
IMP packet-switch software/hardware
    ↕ line interface / modem
leased telecom circuit
```

Each boundary has its own documents.

## 9. RFC 1 shows the network before it is finished

RFC 1, *Host Software*, dated **7 April 1969**, is valuable precisely because it is tentative. Steve Crocker explicitly says that little is firm and reactions are expected.

Source: https://www.rfc-editor.org/info/rfc1/

RFC 1 already documents:

- messages up to 8080 bits plus a header;
- IMP partitioning of messages into packets;
- packets no more than 1010 bits in the described design;
- 24-bit cyclic checksum at IMP transmission hardware;
- logical links between hosts;
- RFNM-style flow-control assumptions;
- host software primitives for establishing TTY-like and file-like connections.

This is not a polished retrospective. It is the excavation layer where designers are still negotiating behavior.

## 10. The Host–IMP interface deserves its own history

A packet network is useless if host machines cannot electrically/logically connect to the packet switch.

RFC 7 is explicitly titled *Host-IMP interface*.

RFC index: https://www.rfc-editor.org/rfc-index/

Future work must recover:

- electrical interface specification;
- parallel/serial nature by host;
- word/bit ordering;
- ready/busy signaling;
- interrupt behavior;
- DMA/channel interfaces;
- host-specific interface hardware;
- differences among Sigma 7, SDS 940, IBM 360/75 and PDP-10 installations.

The four hosts were not plug-and-play Ethernet machines.

## 11. The first four ARPANET sites were four different integration projects

The famous four-node diagram hides a great deal of engineering:

- UCLA — SDS Sigma 7
- SRI — SDS 940
- UCSB — IBM 360/75
- University of Utah — DEC PDP-10

Each site had to make its own host system cooperate with the IMP and emerging host protocols.

A future article should reconstruct each node as a bill of materials + software stack + people + installation chronology.

## 12. The “LO” story is only one event in bring-up

The October 1969 UCLA–SRI login attempt, in which the system failed after `L` and `O`, is a memorable anecdote. It should be preserved, but not allowed to replace the engineering history.

The more useful archaeology asks:

- when each IMP became reachable;
- when host interfaces worked;
- when host software could exchange useful messages;
- when login protocols stabilized;
- what failed during the first tests;
- which logs survive.

## 13. Early RFCs as engineering strata

The first RFCs should eventually be annotated one by one because their titles alone show how unfinished the system was:

- RFC 1 — Host Software
- RFC 2 — Host software
- RFC 3 — Documentation conventions
- RFC 4 — Network timetable
- RFC 5 — Decode Encode Language (DEL)
- RFC 6 — Conversation with Bob Kahn
- RFC 7 — Host-IMP interface
- RFC 8 — ARPA Network Functional Specifications
- RFC 9 — Host Software
- RFC 10 — Documentation conventions

Source: https://www.rfc-editor.org/rfc-index/

The RFC series is therefore itself an archaeological artifact: a public-ish sequence of evolving technical conversation rather than a conventional standards bureaucracy.

## 14. What the 1960s hand to the 1970s

By the end of 1969:

- remote interactive computing is normal enough to shape expectations;
- modems and leased lines provide practical data paths;
- packet switching has independent intellectual roots in multiple places;
- NPL work exists;
- ARPANET's first nodes are operating;
- interface processors separate host systems from WAN switching;
- host protocols are still unsettled;
- packet networking has not converged on one architecture.

The 1970s will therefore not be “the Internet expands”. It will be a decade in which **many incompatible packet networks and protocol philosophies compete**.

## Primary-source targets

- RAND *On Distributed Communications* series
- NPL packet-switching reports
- ARPA planning memos
- BBN IMP proposal/specifications
- Honeywell DDP-516 documentation
- Host–IMP interface drawings
- UCLA/SRI/UCSB/Utah installation reports
- RFC 1 onward
- early Network Working Group notes
- oral histories with Frank Heart, Steve Crocker, Larry Roberts, Donald Davies colleagues and first-site engineers

## Current anchors

- RFC 1: https://www.rfc-editor.org/info/rfc1/
- RFC index: https://www.rfc-editor.org/rfc-index/
- RFC 2555 retrospective: https://www.rfc-editor.org/rfc/rfc2555.html
- NPL timeline: https://www.npl.co.uk/about-us/history/timeline
- BBN Report 4799 archive: https://commons.wikimedia.org/wiki/File:A_History_of_the_ARPANET,_The_First_Decade,_BBN_Report_4799,_April_1981.pdf
- ARPANET completion report archive: https://commons.wikimedia.org/wiki/File:Arpanet_Completion_Report.pdf

## Status

**Started.** Highest-priority next task: reconstruct one complete 1969 ARPANET site from host CPU to leased line with exact hardware and software references.