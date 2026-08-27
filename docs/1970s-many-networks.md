# 1970s: There Was No Single Inevitable Network

The 1970s are easiest to misunderstand if we read them backward from today's Internet. The decade did not contain one obvious winner waiting to mature. It contained many incompatible answers to the question “how should computers communicate?”

ARPANET expanded. NPL operated a packet network. CYCLADES explored datagrams. ALOHAnet used packet radio. Public carriers built X.25 services. Xerox PARC invented Ethernet and PUP. IBM promoted SNA. DEC built DECnet. Commercial packet networks such as Tymnet and Telenet sold access. DARPA tried to interconnect packet radio, satellite and terrestrial packet networks.

The correct mental picture is a **network archipelago**.

## 1. ARPANET grows from experiment into infrastructure

After the initial 1969 nodes, ARPANET accumulated sites, line changes, IMP revisions, host implementations and user applications. The network became useful enough that operational concerns mattered as much as conceptual design.

Future excavation must track by year:

- nodes and host computers;
- IMP/TIP hardware generation;
- leased-line speeds;
- routing software revision;
- host protocol implementation;
- Network Control Center procedures;
- traffic volume;
- major outages;
- network maps.

A single “ARPANET map” is historically misleading because topology changed constantly.

## 2. NCP: the Internet did not begin with TCP

Early ARPANET hosts communicated using the Network Control Program/Protocol system generally called **NCP**. This deserves full treatment because later histories often jump directly from IMPs to TCP/IP.

Questions to preserve:

- exact NCP document genealogy;
- Initial Connection Protocol role;
- sockets/connection naming in NCP-era software;
- host-to-host flow control;
- differences among host implementations;
- migration pain when TCP/IP replaced it.

Do not confuse ARPANET NCP with IBM's Network Control Program or NetWare Core Protocol.

## 3. Telnet, FTP and mail are part of protocol archaeology

User-visible network services forced abstract packet infrastructure into real workflows.

### Telnet
Remote login required a way to cope with incompatible terminals and host conventions. The idea of a network virtual terminal is historically tied to the earlier world of teletypes and remote terminals.

### FTP
File transfer quickly exposed differences in host file systems, character sets, record formats and byte sizes. Early FTP revisions should be read as evidence of a heterogeneous computing world, not merely as obsolete syntax.

### Email
Network mail became one of ARPANET's most important applications. The path from local mail programs to network mail, address conventions and later SMTP is a technical and social history of its own.

## 4. TIPs: terminal access without a full host

The Terminal Interface Processor (TIP) extended IMP technology to direct terminal access. It reveals how the old terminal world and packet-network world overlapped.

A TIP article should eventually document:

- processor/platform;
- terminal port hardware;
- modem/serial support;
- command interface;
- protocol support;
- remote login workflow;
- installation sites;
- later replacements by terminal servers.

## 5. ALOHAnet proves shared media can work

The University of Hawaiʻi states that ALOHAnet began providing inter-island packet-radio access in **June 1971** and demonstrated large-scale shared-channel random access.

Source: https://www.eng.hawaii.edu/about/history/alohanet/

The important conceptual chain is:

```text
shared radio channel
  ↓
transmit without reserving an end-to-end circuit
  ↓
collisions / missing acknowledgements
  ↓
randomized retransmission
```

This idea directly influenced Ethernet.

Future hardware excavation:

- UHF frequencies;
- terminal radio equipment;
- central station;
- data rates;
- packet format;
- acknowledgements;
- Pure vs Slotted ALOHA chronology.

## 6. CYCLADES makes the network less responsible

Inria describes Louis Pouzin's CYCLADES project as launched in **1972**, with an official demonstration in **1973**. Its CIGALE packet-switching subnet used CII Mitra 15 minicomputers.

Sources:
- https://www.inria.fr/en/arpanet-internet-france-some-milestones
- https://www.inria.fr/en/louis-pouzin-et-internet

The architectural importance is the datagram approach: packets are treated more independently, while reliable end-to-end communication is achieved above an unreliable packet service.

This stands in contrast to carrier-oriented virtual-circuit approaches that make the network maintain more connection state.

### Hardware matters here too

The CYCLADES history should not become only “Louis Pouzin influenced TCP/IP”. Preserve:

- CIGALE switches;
- Mitra 15 hardware;
- host interfaces;
- telephone links;
- STST transport software;
- deployment geography;
- international links;
- source code and manuals if surviving.

## 7. 1973 Ethernet: packet radio ideas meet coax

IEEE Communications Society dates Robert Metcalfe's Ethernet work at Xerox PARC to **1973** and explicitly links it to ALOHAnet.

Source: https://www.comsoc.org/node/19561

Ethernet's first world is physically alien to modern twisted-pair switched Ethernet:

```text
Alto workstation
  ↓ interface/transceiver
shared coaxial cable
  ↓
other stations share same medium
  ↓
carrier sense + collision detection + backoff
```

The first experimental PARC Ethernet ran at approximately 2.94 Mbit/s, not 10 Mbit/s.

The historical sequence must distinguish:

- experimental PARC Ethernet;
- PUP protocols above it;
- DIX Ethernet;
- IEEE 802.3;
- 10BASE5 deployment;
- 10BASE2;
- twisted-pair hubs;
- bridges and switches.

## 8. PUP/XNS: a nearly forgotten Internet lineage

Xerox PARC did not merely invent a LAN link layer. PUP (PARC Universal Packet) provided an internetworking architecture connecting multiple Ethernets and other networks. XNS later commercialized/extended this lineage.

This matters because:

- internetworking ideas existed outside TCP/IP;
- routing and datagram services were used in practical workstation environments;
- later systems borrowed from XNS;
- protocol success is not equivalent to conceptual originality.

Full excavation targets:

- PUP packet format;
- addresses;
- gateways;
- routing;
- EFTP;
- network boot;
- printing;
- XNS IDP/SPP;
- Xerox workstation products;
- surviving source code.

## 9. Public packet networks choose virtual circuits

CCITT adopted X.25 in **1976**. IEEE Communications Society describes X.25 as a virtual-circuit protocol that became foundational to national packet networks such as Datapac and Transpac.

Source: https://www.comsoc.org/node/19621

X.25 deserves to be understood on its own terms.

Telephone administrations already operated networks where the network itself supplied a managed connection service. It was natural to extend that model into packet communications:

```text
terminal/host
  ↓
DTE/DCE interface
  ↓
X.25 virtual call
  ↓
packet-switched carrier network
  ↓
remote DTE
```

The network keeps connection state and is expected to supply ordered/reliable packet service characteristics.

### The forgotten PAD world

Many users did not run X.25 on their terminal. A Packet Assembler/Disassembler (PAD) converted asynchronous terminal traffic into X.25 packets.

Important standards:

- X.3 — PAD parameters
- X.28 — terminal-to-PAD interface
- X.29 — PAD-to-host control

This makes the PAD one of the great missing boxes of simplified networking history.

## 10. Tymnet and Telenet: networking becomes a commercial service

Commercial packet networks demonstrate that a packet-switched infrastructure can sell terminal/host connectivity across cities and countries.

They require research into:

- switching-node hardware;
- access concentrators;
- modem pools;
- host interface products;
- pricing;
- carrier regulation;
- international gateways;
- X.25 migration/compatibility;
- corporate applications.

James Pelkey's *History of Computer Communications* is particularly valuable for entrepreneurial/vendor history:

https://historyofcomputercommunications.info/

## 11. Internetting: the problem changes from “build a packet network” to “connect different packet networks”

Internet Society's participant history says DARPA initiated an Internetting research program in **1973** to develop technology for interlinking packet networks of different kinds.

Source: https://www.internetsociety.org/internet/history-internet/brief-history-internet-related-networks/

This is the conceptual shift that makes “Internet” distinct from “ARPANET”.

The problem now includes:

- independently administered networks;
- different packet sizes;
- different reliability assumptions;
- radio vs satellite vs terrestrial links;
- gateways between networks;
- end-to-end transport across those boundaries.

## 12. Cerf/Kahn and the Transmission Control Program

The 1974 paper *A Protocol for Packet Network Intercommunication* proposed a common internetworking architecture. But “TCP” in 1974 is not yet the later TCP + IP pair familiar today.

The repository should trace:

1. 1974 architecture;
2. successive TCP versions;
3. Internet Experiment Notes;
4. experimentation across ARPANET/PRNET/SATNET;
5. separation of Internet Protocol from Transmission Control Protocol;
6. later RFC standardization;
7. implementation on actual hosts.

Never cite one modern TCP RFC as if it describes the whole 1970s design history.

## 13. Packet radio and satellite links force architecture to generalize

A terrestrial leased-line packet network can assume relatively stable point-to-point links. Packet radio and satellite networks behave differently.

That diversity tests whether internetworking abstractions really work.

Research topics:

- PRNET radios;
- mobile/variable connectivity;
- SATNET channel access;
- packet satellite equipment;
- gateways;
- retransmission responsibility;
- fragmentation;
- path MTU differences;
- early multi-network TCP demonstrations.

## 14. Vendor network architectures proliferate

### IBM SNA
Systems Network Architecture reflects IBM's mainframe/terminal/control-unit world. It should not be caricatured as “wrong because TCP/IP won”. Its hierarchy matched large enterprise installations and IBM's installed base.

### DECnet
DECnet evolves through multiple phases alongside DEC's minicomputer/VAX ecosystem.

### Xerox PUP/XNS
A workstation-oriented packet/internetwork architecture.

### Chaosnet
MIT's local network/protocol environment.

These systems make the 1970s/1980s a multiprotocol world.

## 15. Standards become strategic

Networking increasingly depends on interfaces that cross vendor and national boundaries. Standards bodies become part of engineering history:

- CCITT
- ISO
- IEEE
- ARPANET Network Working Group
- INWG
- vendor consortia

The question “who gets to define the interface?” becomes economic and political as well as technical.

## 16. 1978 ARPANET completion report as primary evidence

The *Completion Report: ARPA Network Development* (Heart, McKenzie, McQuillan, Walden; 1978) is a crucial primary report on ARPANET engineering.

Archive: https://commons.wikimedia.org/wiki/File:Arpanet_Completion_Report.pdf

BBN's later 1981 Report 4799 provides a broader first-decade history:

https://commons.wikimedia.org/wiki/File:A_History_of_the_ARPANET,_The_First_Decade,_BBN_Report_4799,_April_1981.pdf

These should be mined page-by-page for hardware/software/topology details, not merely cited as general background.

## 17. 1979 Usenet: a network can be intermittent

Usenet reminds us that “networked” does not require a permanently connected packet path.

Original propagation relied on UUCP and dial-up/store-and-forward exchanges. A rough model:

```text
site A queues news
  ↓ scheduled phone call
modems connect
  ↓ UUCP transfers batch
site B stores news
  ↓ later call
site C
```

Messages may take hours to propagate, yet a distributed social information system emerges.

That is a radically different architecture from always-on packet routing, but historically it is still a network society.

## 18. The central conflict of the decade

The deepest 1970s question can be reduced to:

> How much intelligence, reliability and state should live inside the network, and how much should live at the endpoints?

Different answers lead toward:

- X.25 virtual circuits;
- datagram networks;
- CYCLADES;
- TCP/IP;
- vendor-specific architectures;
- later OSI debates.

The answer was not obvious at the time.

## What the 1970s hand to the 1980s

By 1980:

- packet switching is proven in multiple environments;
- ARPANET is mature infrastructure;
- commercial packet networks exist;
- public X.25 networks are spreading;
- Ethernet exists but has not yet become universal LAN infrastructure;
- PUP/XNS, SNA, DECnet and other architectures are viable;
- TCP/IP has evolved through experiments but is not yet the universal Internet suite;
- UUCP/Usenet demonstrate store-and-forward community networking;
- the world is heading into protocol and standards competition, not convergence by default.

## Primary-source targets

- yearly ARPANET maps
- IMP/TIP manuals and source listings
- NCP specification evolution
- early Telnet/FTP/mail RFCs
- ALOHAnet papers and hardware diagrams
- Xerox Ethernet memo and Alto Ethernet hardware docs
- PUP papers/source code
- CYCLADES/STST/INWG papers
- X.25 1976 recommendation and PAD standards
- Tymnet/Telenet technical manuals
- PRNET/SATNET reports
- Internet Experiment Notes
- Cerf/Kahn 1974 paper
- IBM SNA and DECnet contemporary architecture manuals
- early UUCP/Usenet source and correspondence

## Status

**Started.** The next major improvement should be a matrix comparing ARPANET, NPL, CYCLADES, X.25, PUP and ALOHAnet across addressing, routing, reliability, packet format, switch hardware and host interface.