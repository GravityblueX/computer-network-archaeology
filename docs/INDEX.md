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

Questions opened by this excavation include exact BBN 1822 electrical details, site-specific interface hardware, first-node bills of materials and the leased-line/modem layer behind the IMP cloud.

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

## ALOHAnet → experimental Ethernet

- [`alohanet/radio-to-ethernet.md`](alohanet/radio-to-ethernet.md)  
  Starts from the actual Hawaiian radio system: UHF channel pair, Terminal Control Unit, RS-232 terminal boundary, packet/retransmission behavior, Pure/Slotted ALOHA and later microprocessor packet-control units, then follows the shared-medium idea into Xerox PARC Ethernet.

It explicitly keeps **ALOHAnet**, **1973 Ethernet concept**, **2.94 Mbit/s experimental Ethernet** and **10 Mbit/s DIX/IEEE Ethernet** as distinct historical objects.

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

The next target is a per-site router/interface/circuit inventory for each backbone generation.

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

The project should grow both **horizontally**, **vertically**, and now **structurally**.

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

Several previously listed targets now have first-pass deep excavations. The next layer should concentrate on **revision-level and site-level specificity**:

1. September–October 1969 UCLA ARPANET node bill of materials;
2. BBN Report 1822 and exact Host–IMP electrical interface revisions;
3. Bell 101A/B/C and 103A/F revision tree from Bell primary documents;
4. NPL Mark I switch: Honeywell 516 I/O boards, packet header, link hardware and operator console;
5. CIGALE per-site Mitra 15 configurations, packet format and routing table;
6. 1973–1976 Xerox experimental 2.94 Mbit/s Ethernet: Alto interface, transceiver, coax and PUP stack;
7. one real 1970s X.25 terminal → modem → PAD → public data network → host path with vendor models and tariff;
8. one UUCP overnight feed reconstructed from modem model, call schedule, spool files, wire protocol and phone cost;
9. one 1982 BBN Internet Gateway site with exact PDP-11, interface boards, memory map and INOC monitoring path;
10. one 1986 NSFNET Fuzzball site and one 1988 IBM RT NSS site with complete hardware/circuit inventory;
11. one 1994 dial-up ISP POP from analog subscriber loop through modem bank/access server to upstream BGP router;
12. an archive/museum provenance map showing where surviving routers, IMPs, modems, terminals, NICs and manuals physically reside.

# The completion criterion

This archive should never declare a subject “done” merely because a readable narrative exists.

A mature excavation ideally connects:

**idea → specification → hardware → software → deployment → operation → failure → replacement → surviving artifact → primary source.**

And every important arrow should eventually carry:

**source → locator → date precision → certainty → rights/provenance.**

That graph, not article count, is the real measure of completeness.