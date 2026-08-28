# NPL Mark I / Mark II: reconstructing the packet network, not just the idea

The National Physical Laboratory (NPL) story is frequently compressed into one sentence: **Donald Davies invented packet switching in Britain**. That sentence is historically important, but it hides the engineering archaeology.

This note reconstructs the NPL Data Communications Network as a working system: interfaces, packet-switch hardware, local links, protocols, people, and the transition from Mark I to Mark II.

## Why NPL matters

Donald Davies proposed packet switching in a data-communications context in 1965. A team led in day-to-day technical work by Roger Scantlebury, with Keith Bartlett leading hardware and Peter Wilkinson leading software, then turned the idea into a real local network at NPL.

Martin Campbell-Kelly's archival study is unusually valuable because it was built from surviving project memoranda and interviews. It records a problem that this repository exists to resist: many central administrative records had already been destroyed as obsolete, while much of the surviving technical record existed only because individual engineers retained copies.

That means the history of networking is already partly a history of **accidental survival**.

## The physical/logical stack

A simplified Mark I path was approximately:

```text
host or terminal-side equipment
        ↓
NPL-defined computer/network interface
        ↓
packet-switching computer
        ↓
local high-speed data link
        ↓
packet-switching computer / network service
        ↓
remote host or terminal service
```

The important point is that packet switching did not replace interfaces and transmission engineering. It sat on top of them.

## Interfaces before networking had settled terminology

NPL already had experience with an **8-bit parallel interface** developed in Derek Barber's group. A draft specification circulated in 1965; interaction with ICT/ICL helped produce a revised specification that became **British Standard BS 4421** in April 1969.

When the packet-network group was defining its host interface in 1967, CCITT V.24 existed but compatible equipment was not yet common enough at NPL to make it an obvious choice. The project therefore reused the local ecosystem around BS 4421.

Campbell-Kelly records a revealing detail: an April 1967 memorandum by Scantlebury and Bartlett, *A Protocol for Use in the NPL Data Communications Network*, appears to contain an early use of the word **protocol** in a data-communications context. The team had previously used language such as *procedure*.

This is a useful reminder that even the vocabulary of networking was still being invented.

## Why a byte-at-a-time interface was not enough

The designers recognized that byte-by-byte handshaking would constrain effective transmission speed to roughly **50 kbit/s**, too slow for the computer-to-computer transfers they wanted. They explored a 16-byte-segment interface, eight segments per packet, although this particular arrangement was later abandoned.

The archaeological lesson is more important than the abandoned format: packet switching was not merely an algorithm. The host interface could become a bottleneck, so packet-network design immediately reached down into electrical and transfer-unit engineering.

## Hardware: the Plessey setback and Honeywell 516

The original project expected to use the Plessey XL12. Plessey cancelled that computer in 1968, forcing a redesign around available hardware.

The eventual Mark I packet switch was built around a **Honeywell 516** minicomputer. This creates one of the most striking cross-links in early networking history: the NPL project and BBN's ARPANET IMP project independently converged on machines in the Honeywell Series 16 family during the same period.

Do not turn this into a simplistic claim that the NPL node and ARPANET IMP were the same machine or the same architecture. They were different networks with different designs. The useful fact is that the small rugged minicomputer had become practical infrastructure for packet switching.

## Mark I

The Mark I network was built in the late 1960s and became operational around 1969–1970 depending on which milestone is being counted. Campbell-Kelly describes the network as first operational in 1970; later institutional histories distinguish partial operation in 1969 from full operation in January 1970.

**Dating rule:** preserve both milestones until contemporary commissioning records are located.

A later Computer Conservation Society reconstruction describes Mark I as using a single Honeywell DDP-516 packet switch and **768 kbit/s local channels** across the NPL site. This figure should be traced back to project documentation before being promoted to a canonical machine-readable fact.

## Link control and the alternating-bit idea

Keith Bartlett's 1968 work on *Transmission Control in a Local Network* described link hardware using what became known as an **alternating-bit protocol**. The basic problem was already modern: how can a sender and receiver detect loss/duplication and coordinate retransmission across an unreliable link without confusing a retransmitted block with a new one?

This work belongs in the same archaeological layer as later data-link ARQ schemes. It also shows that packet switching immediately forced explicit separation between:

1. physical transmission;
2. link-level reliable transfer;
3. packet/network functions.

Campbell-Kelly notes that Bartlett explicitly argued for levels with defined interfaces so that improvements in one level would not force redesign of the others. This pre-dates the later formal dominance of layered network models.

## Mark II: software and protocol architecture mature

The Mark II redesign began around 1970–1971 and was primarily a redesign of **software and protocols** rather than a wholesale replacement of the hardware.

That transition matters because it captures a recurring pattern in network history:

> first make packets move; then discover that architecture, layering, operations and extensibility matter as much as raw forwarding.

Mark II became operational in the early 1970s and continued in service for many years. It also became part of Britain's broader packet-network research environment and international interconnection experiments.

## NPL was not just a packet switch

A full excavation must recover the surrounding system:

- host interfaces and adapters;
- terminal access;
- switching-node software;
- local link hardware;
- packet formats;
- retransmission/link procedures;
- address assignment;
- routing;
- measurement and simulation tools;
- control/operations facilities;
- file-store/network services;
- interconnection with external experimental networks.

The project also performed queueing and simulation studies, especially around congestion and network failure. That work should be treated as operational engineering history, not merely theory.

## People who should not disappear behind one famous name

The minimum recurring cast should include:

- **Donald W. Davies** — overall intellectual and institutional leadership;
- **Derek Barber** — deputy and early data-communications leadership;
- **Roger Scantlebury** — day-to-day technical leadership;
- **Keith Bartlett** — hardware design;
- **Peter T. Wilkinson** — software/protocol design;
- John Laws;
- Carol Walsh;
- Keith Wilkinson;
- Rex Haymes;
- Les Pink;
- Patrick Woodroffe;
- Brian Aldous;
- Peter Carter;
- Peter Neale;
- later simulation, operations and Post Office collaborators.

One purpose of this archive is to keep the technicians and implementation teams visible, not only the people attached to famous concepts.

## The NPL → ARPANET relationship needs careful wording

NPL's work influenced the packet-switching conversation in which ARPANET was designed. Roger Scantlebury presented NPL work at the 1967 Gatlinburg symposium attended by ARPA researchers. NPL's packet-switching ideas and estimated line speeds became part of the international engineering discussion.

However, historical influence is not the same as a single linear invention chain. Paul Baran's RAND work, Davies' NPL work, ARPA's networking goals, BBN's implementation, and later CYCLADES all solve overlapping problems from different institutional contexts.

This repository should preserve those parallel lines instead of inventing a single heroic origin story.

## Primary/source trail

High-value sources:

1. Martin Campbell-Kelly, **“Data Communications at the National Physical Laboratory (1965–1975)”**, *Annals of the History of Computing* 9, no. 3/4 (1987/1988 scanning varies by catalog): 221–247. Surviving scan: <https://archive.org/details/DataCommunicationsAtTheNationalPhysicalLaboratory>
2. NPL, **Donald Davies** institutional biography: <https://www.npl.co.uk/about-us/history/famous/donald-davies>
3. NPL, **Packet Switching: The first steps on the road to the information society**: <https://www.npl.co.uk/getattachment/de2d9db5-999d-4a75-99ce-6730b8c204a6/UK-role-in-Packet-Switching-%281%29.pdf>
4. Computer History Museum, early networking timeline and NPL switch artifacts: <https://www.computerhistory.org/revolution/story/407>
5. Computer Conservation Society, retrospective discussion of the NPL packet network: <https://www.computerconservationsociety.org/resurrection/res95.htm>

## Unresolved excavation tasks

- locate scans of the April 1967 Scantlebury/Bartlett protocol memorandum;
- identify surviving BS 4421 editions and connector/electrical details;
- recover exact Mark I packet format and header fields;
- recover Honeywell 516 memory configuration and NPL-specific I/O modifications;
- identify the exact 768 kbit/s line hardware and signalling method;
- reconstruct packet-switch process scheduling and queue structures;
- document Mark II packet and address changes;
- locate NPL operator/control-center manuals;
- locate network maps by date;
- determine which physical switch boxes and interface hardware survive in museums;
- cross-reference surviving NPL → EPSS → PSS and NPL → CYCLADES interconnection records.

## Why this is a model excavation

The NPL network demonstrates the repository's intended method:

```text
idea
  ↓
memorandum
  ↓
interface standard
  ↓
minicomputer + custom I/O
  ↓
link protocol
  ↓
packet-switch software
  ↓
operational local network
  ↓
Mark II redesign
  ↓
public-network and international influence
```

The historical object is the whole stack, not the phrase “packet switching.”