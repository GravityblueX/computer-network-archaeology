# Documentation Index

This is the human-readable entrance to the excavation. The repository is designed to support three reading modes:

1. **chronological reading** — follow how computer communication changed over decades;
2. **artifact-first research** — start from one device/protocol/network/document and follow cross-links outward;
3. **stack reconstruction** — choose one historical path and recover every layer from terminal/host software down to interfaces, carrier circuits, switching nodes and operations.

## Chronological spine

Start here if you want the broad transformation:

1. [`1950s-data-communications.md`](1950s-data-communications.md)  
   SAGE, radar data, modems/data sets, leased telephone infrastructure, remote terminals, SABRE, and why the decade before packet switching matters.

2. [`1960s-time-sharing-packet-switching.md`](1960s-time-sharing-packet-switching.md)  
   Time-sharing, Baran, Davies/NPL, ARPA, BBN, IMPs, the first four ARPANET hosts, and the still-unfinished host protocol problem.

3. [`1970s-many-networks.md`](1970s-many-networks.md)  
   ARPANET/NCP, ALOHAnet, CYCLADES, Ethernet/PUP, X.25, Tymnet/Telenet, packet radio, satellite, vendor architectures and the emergence of internetworking.

4. [`1980s-protocol-wars.md`](1980s-protocol-wars.md)  
   TCP/IP transition, BSD sockets, DNS/routing, BITNET, CSNET, JANET, NSFNET, Ethernet/Token Ring, NetWare, AppleTalk, OSI, X.25, UUCP/Usenet/BBS/FidoNet and the multiprotocol machine room.

5. [`1990s-commercial-internet.md`](1990s-commercial-internet.md)  
   NSFNET T1/T3, BGP/CIDR, commercial providers, dial-up IP, modem banks, PPP, switching Ethernet, Frame Relay, ATM, ISDN, Web-driven growth and the 1995 backbone transition.

The shorter date-oriented reference is [`../timeline/master-timeline.md`](../timeline/master-timeline.md).

---

# Deep excavations

These files demonstrate the intended final granularity. A subject is **not** considered complete merely because it has one deep excavation; each file should expose the next layer of missing evidence.

## ARPANET: Host ↔ IMP

- [`arpanet/1969-host-imp-stack.md`](arpanet/1969-host-imp-stack.md)  
  Reconstructs the early host/IMP boundary from RFC 1 and RFC 7: messages vs packets, logical links, RFNM, error checking, UCLA Sigma 7 host software organization, buffer design and unresolved hardware/carrier questions.

- [`arpanet/ucla-1969-node-bom.md`](arpanet/ucla-1969-node-bom.md)  
  Treats the first UCLA ARPANET node as installed infrastructure rather than a milestone slogan: Sigma 7 host, Mike Wingfield's custom Host–IMP interface, BBN IMP No. 1, modified Honeywell DDP-516, IMP software build/deployment path, 50 kbit/s carrier layer, probable Bell 303-class data sets, telco responsibilities, first-login chronology and surviving IMP provenance.

- [`arpanet/bbn-1822-physical-interface.md`](arpanet/bbn-1822-physical-interface.md)  
  Excavates 1822 as physical machinery: bit-serial asynchronous handshaking, ready lines, Local/Distant/Very Distant Host variants, liveness/watchdog behavior, leader revision drift, RFC 642 implementation cleanup, JANUS lineage and the need for revision-specific electrical/pinout records.

The next ARPANET layer is no longer “what was the IMP?” It is now board-, cable- and revision-level: Wingfield interface drawings, exact 1969 Report 1822 values, Bell 303 service orders, IMP No. 1 board population, and per-site host-interface implementations.

## Bell data sets: source conflict as an artifact

- [`modems/bell-101-103-source-conflict.md`](modems/bell-101-103-source-conflict.md)  
  A worked example of source criticism. Modern histories and surviving Bell-document metadata do not yet produce a clean Bell 101/103 model/revision chronology, so the conflict is preserved rather than silently flattened.

This is the model for all disputed “firsts,” product dates and model-family claims.

## NPL Mark I / Mark II

- [`npl/mark-i-mark-ii-stack.md`](npl/mark-i-mark-ii-stack.md)  
  Reconstructs NPL packet switching below the slogan: BS 4421 and earlier parallel interfaces, host-interface speed constraints, Honeywell 516 switching hardware, Bartlett's alternating-bit work, software/protocol redesign in Mark II, project staffing and surviving-document problems.

Particularly important leads now exposed: exact Honeywell I/O configuration, the 768 kbit/s local-link claim, Mark I/Mark II packet formats, operator facilities and surviving NPL memoranda.

## CYCLADES / CIGALE

- [`cyclades/cigale-datagram-stack.md`](cyclades/cigale-datagram-stack.md)  
  Reconstructs the French datagram network as equipment: CII Mitra 15 packet switches, 16K-word configurations, PTT leased circuits, V.24/V.35-style host attachment, queue/process organization, remote reload, datagram/end-system responsibility, heterogeneous hosts and the 1974 NPL–CYCLADES link.

The next layer is a per-site CIGALE bill of materials plus packet-header/routing reconstruction.

## ALOHAnet

- [`alohanet/radio-to-ethernet.md`](alohanet/radio-to-ethernet.md)  
  Starts from the actual Hawaiian radio system: UHF channel pair, Terminal Control Unit, RS-232 terminal boundary, packet/retransmission behavior, Pure/Slotted ALOHA and later microprocessor packet-control units, then follows the shared-medium idea into Xerox PARC Ethernet.

It explicitly keeps **ALOHAnet**, **1973 Ethernet concept**, **2.94 Mbit/s experimental Ethernet** and **10 Mbit/s DIX/IEEE Ethernet** as distinct historical objects.

## Xerox PARC experimental Ethernet + PUP

- [`ethernet/xerox-alto-2-94mbps-pup-stack.md`](ethernet/xerox-alto-2-94mbps-pup-stack.md)  
  Reconstructs the Alto-era 2.94 Mbit/s system instead of projecting 10BASE5 backward: coax Ether, transceiver, FIFO/phase-encoding/clock-recovery/CRC interface logic, Ethernet microcode, backplane-wired host address, software-visible collision/backoff state, early packet conventions, and the PUP internetwork stack carried across Ethernet, ARPANET and synchronous links.

The next layer is physical and source-level: transceiver electrical characteristics, coax/tap/terminator models, interface schematics, Ethernet microcode source, 1973/1974 document genealogy, PUP gateway machines and surviving PARC hardware provenance.

## X.25 + Triple-X PAD

- [`x25/pad-public-data-network-stack.md`](x25/pad-public-data-network-stack.md)  
  Reconstructs what “using an X.25 network” looked like from an asynchronous terminal: DTE/DCE boundary, link and packet levels, logical channels, switched/permanent virtual circuits, X.3 PAD parameters, X.28 terminal procedures and X.29 packet-side control.

It also documents IP-over-X.25 as a deployed architectural overlap rather than repeating a simplistic “TCP/IP versus X.25” story.

## UUCP + Usenet

- [`uucp/usenet-store-and-forward-world.md`](uucp/usenet-store-and-forward-world.md)  
  Treats the telephone bill, modem, serial port, disk spool and call schedule as parts of the network. Covers UUCP's queued transfer model, bang paths, economic topology, early Usenet origins, A News/B News/C News and the journey of an article across intermittently connected sites.

The next excavation should split the UUCP wire protocols and news release trees into version-level records.

## Internet gateway → router

- [`internetworking/bbn-gateway-to-router.md`](internetworking/bbn-gateway-to-router.md)  
  Uses RFC 823's 1982 BBN Internet Gateway to reconstruct an early IP router before *router* became the standard term: PDP-11/LSI-11 platform, MACRO-11 implementation, 1822/Proteon Ring/HDLC/Ethernet/Fibernet interfaces, packet queues, GGP, monitoring and INOC operations.

This file is also the canonical warning that contemporary **gateway** terminology must not be silently modernized.

## NSFNET: Fuzzball → T1 NSS → T3

- [`nsfnet/fuzzball-to-t1-nss.md`](nsfnet/fuzzball-to-t1-nss.md)  
  Tracks national Internet backbone growth as hardware: 56 kbit/s PDP-11/LSI-11 Fuzzballs, HELLO routing and overload; the 1988 1.544 Mbit/s T1 backbone with multi-IBM-RT Nodal Switching Subsystems; then the T3/RS-6000 transition and 1995 retirement.

- [`nsfnet/fuzzball-node-internals.md`](nsfnet/fuzzball-node-internals.md)  
  Opens the Fuzzball itself: PDP-11/LSI-11 operating system and RT-11 virtual-machine environment, scheduler/IPC, three-layer network drivers, paired input/output processes, zero-copy packet path, TCP/IP applications, HELLO/Hellospeak, 1000 Hz logical clock, surviving source archive and the unresolved per-site Phase-I hardware inventory.

The next NSFNET layer is site-specific: exact processor, RAM, bus, disk, Ethernet adapter, serial/WAN controller, carrier termination, clock hardware, software image and circuit ID for each of the six production Fuzzball sites, followed by the same treatment for one IBM RT NSS node.

---

# Catalog entrances

The narrative is intentionally not the master database. Use these discovery catalogs when researching one object:

- [`../catalogs/networks.md`](../catalogs/networks.md) — named networks, services and network ecosystems;
- [`../catalogs/hardware.md`](../catalogs/hardware.md) — terminals, modems, switches, interfaces, NICs, routers, carrier gear and diagnostics;
- [`../catalogs/software.md`](../catalogs/software.md) — switching-node software, host stacks, network operating systems, utilities and user-facing programs;
- [`../catalogs/protocols.md`](../catalogs/protocols.md) — protocol/standard families and revisions;
- [`../catalogs/document-corpora.md`](../catalogs/document-corpora.md) — where the original protocol texts and technical record survive.

# Evidence entrances

- [`../sources/primary-sources.md`](../sources/primary-sources.md) — RFC/IEN/BBN/NPL/RAND/CYCLADES/ALOHAnet/PARC/vendor/manual/source-code corpora;
- [`../sources/secondary-sources.md`](../sources/secondary-sources.md) — scholarship and participant histories;
- [`../SOURCING.md`](../SOURCING.md) — evidence hierarchy, dating, copyright/preservation and conflict rules.

# Machine-readable research queues

- [`../data/artifact-ledger.csv`](../data/artifact-ledger.csv) — concrete devices, interfaces, protocols, software, services and networks awaiting deeper records;
- [`../data/source-ledger.csv`](../data/source-ledger.csv) — sources discovered/acquired/mined or still sought;
- [`../data/README.md`](../data/README.md) — ledger field semantics and workflow.

A name can enter a ledger before it gets an article. This prevents obscure discoveries from disappearing simply because there was not enough time to investigate them immediately.

# Machine-readable archival model

The archive is moving from flat CSV discovery queues toward claim-level records.

- [`../schema/artifact-record.schema.json`](../schema/artifact-record.schema.json) — artifact schema: chronology with precision/certainty, physical interfaces, hardware, software, protocols, addressing, routing, operations, economics, survival, open questions and source locators;
- [`../schema/source-record.schema.json`](../schema/source-record.schema.json) — source schema: identity, provenance, edition, access, fixity/checksum, rights, evidence grade, claims and conflicts;
- [`../vocab/controlled-vocabulary.md`](../vocab/controlled-vocabulary.md) — controlled artifact types, evidence grades, certainty states, relationship verbs and naming rules;
- [`../GLOSSARY.md`](../GLOSSARY.md) — historical terminology warnings and definitions.

The schemas are intentionally stricter than narrative Markdown. Their purpose is to make a future graph/database possible without discarding uncertainty.

# Record templates

The older prose-oriented templates remain useful for human-readable excavation:

- [`../templates/hardware-record.md`](../templates/hardware-record.md)
- [`../templates/protocol-record.md`](../templates/protocol-record.md)
- [`../templates/network-record.md`](../templates/network-record.md)
- [`../templates/source-record.md`](../templates/source-record.md)

The templates intentionally ask for details that popular histories omit: connector pins, line service, clocking, buffer sizes, software revisions, operator diagnostics, pricing, source conflicts, surviving specimens and rights status.

---

# Recommended excavation order

The project should grow both **horizontally**, **vertically**, and **structurally**.

## Horizontal: prevent loss

Keep expanding discovery coverage:

- network names;
- device/product families;
- software packages;
- standards/protocols;
- companies;
- national networks;
- carrier services;
- archives and document series;
- diagnostic/test equipment;
- operator practices.

A thin catalog/ledger row is enough to save a lead.

## Vertical: prove what a system really was

Choose individual systems and reconstruct them end-to-end:

```text
user / application
      ↓
host software
      ↓
interface hardware
      ↓
switch/router/PAD/modem
      ↓
actual carrier or local medium
      ↓
remote equipment
      ↓
remote software / user
```

## Structural: turn prose into an evidence graph

When a deep excavation stabilizes enough, promote its claims into schema-conformant records:

```text
artifact
  ├── date claim ── source + locator + certainty
  ├── interface ── related artifact
  ├── software ── related artifact
  ├── protocol ── exact revision
  ├── physical service ── carrier artifact
  ├── operator practice ── source + locator
  └── surviving specimen ── museum + provenance
```

This will eventually let the repository answer questions that prose cannot answer reliably at scale.

---

# Next high-value vertical digs

Several former targets now have first-pass deep excavations. The queue should therefore move downward rather than repeat the same subjects at summary level:

1. **UCLA 1969 node, board level:** Mike Wingfield interface schematics/logic, connector/pinout, Sigma 7 channel mapping, IMP No. 1 serial/board inventory, exact installed core memory and present-vs-1969 provenance.
2. **1822 revision archaeology:** earliest 1969 specification plus 1973/1974/1975/1976 diffs; Local/Distant Host signal lists, electrical values, cable limits, grounding and complete state machines; VDH kept separate.
3. **Bell data-set genealogy:** Bell 101A/B/C, 103A/F and Bell 303-family revision tree from Bell System Practices, tariffs, announcements and surviving hardware.
4. **NPL Mark I at board level:** Honeywell 516 I/O cards, memory/configuration, host-interface hardware, packet header, line framing, switch software and operator console.
5. **CIGALE at site level:** Mitra 15 configurations, modem/line equipment, packet header, routing-table representation, process queues and remote reload path.
6. **Xerox experimental Ethernet at electrical/source level:** 1973/1974 memos, transceiver schematic/specification, coax/taps/terminators, Alto interface boards, Ethernet microcode revisions, PUP gateway software and surviving hardware.
7. **One real 1970s X.25 session:** named terminal → serial modem → named PAD → named public data network → named host, including tariff, X.3 profile and operator/user commands.
8. **One real UUCP overnight feed:** named machines and modems, phone route, call schedule, Devices/Systems files, spool filenames, wire protocol, news software and telephone cost.
9. **One concrete 1982 BBN gateway site:** exact PDP-11/LSI-11, memory map, interface-board population, GGP tables, MOS/source image and INOC alarm/monitoring path.
10. **NSFNET site BOMs:** all six production Fuzzball sites, then one complete IBM RT NSS node including carrier-side T1 equipment and software build identifiers.
11. **One 1994 dial-up ISP POP:** analog subscriber loop → modem → modem rack/digital trunk → access server → Ethernet/FDDI → upstream router/BGP, with actual vendor models and configuration artifacts.
12. **Physical provenance map:** museum/archive/collection records for surviving IMPs, modems, PADs, packet switches, routers, terminals, Ethernet transceivers, NICs, cables, manuals and operator documents.
13. **Source-code archaeology:** Fuzzball, PUP, early BSD TCP/IP, UUCP/News, IMP resurrection sources — manifests, checksums, build tools and code-to-spec concordances.
14. **Operations archaeology:** network maps are not enough; preserve NOC consoles, alarms, logs, maintenance manuals, test sets, escalation procedures, circuit IDs and human operator workflows.

# The completion criterion

This archive should never declare a subject “done” merely because a readable narrative exists.

A mature excavation ideally connects:

**idea → specification → hardware → software → deployment → operation → failure → replacement → surviving artifact → primary source.**

And every important arrow should eventually carry:

**source → locator → date precision → certainty → rights/provenance.**

That graph, not article count, is the real measure of completeness.