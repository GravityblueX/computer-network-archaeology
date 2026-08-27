# 1980s: Protocol Wars, LANs, Dial-Up Worlds, and the Growth of Internetworking

The 1980s are not a simple victory march for TCP/IP. They are a decade of **multiplication**: academic networks, public X.25 services, vendor architectures, Ethernet LANs, Token Ring, BITNET, CSNET, Usenet, BBS networks, OSI standards, DECnet, SNA, XNS, AppleTalk, NetWare and an increasingly important TCP/IP Internet all coexist.

The decade is best understood as overlapping networking worlds that gradually become more interconnected.

## 1. 1983: the ARPANET NCP-to-TCP/IP transition

1 January 1983 is the famous coordinated cutover from NCP to TCP/IP on ARPANET-related hosts.

This is historically important, but it should not be described as “the day the Internet was invented.” It was a deployment migration inside an already mature networking ecosystem.

The archaeology should recover:

- migration planning documents;
- dual-stack/transition software;
- host readiness lists;
- systems that missed the deadline;
- operations messages;
- NCP shutdown procedures;
- TCP/IP implementation differences by host OS.

## 2. BSD makes TCP/IP reproducible outside one project

The Berkeley Unix networking releases helped place a usable TCP/IP implementation and socket API in the hands of universities and vendors.

Critical strata include:

- 4.1aBSD
- 4.1bBSD
- 4.1cBSD
- 4.2BSD
- 4.3BSD
- Tahoe/Reno networking changes

A mature article should distinguish:

- DARPA-funded TCP work;
- BBN implementation contributions;
- Berkeley integration;
- the socket API;
- kernel protocol code;
- applications such as `telnet`, `ftp`, `rlogin` and `sendmail`;
- vendor ports.

## 3. The socket API becomes invisible infrastructure

Today many programmers experience networking through a small set of calls:

```text
socket()
bind()
listen()
accept()
connect()
send()/recv()
```

That interface is historically important because it helps separate application software from protocol implementation details. The repository should track when these calls stabilize and how other operating systems imitate or reinterpret them.

## 4. HOSTS.TXT stops scaling

Early ARPANET/Internet naming relied on centrally distributed host tables. As hosts and networks multiplied, the process became operationally painful.

The Domain Name System responded by distributing authority and lookup.

Key documentary sequence:

- RFC 882 / RFC 883 era DNS design;
- later RFC 1034 / RFC 1035 consolidation;
- resolver libraries;
- root/name-server deployment;
- NIC registration procedures.

Internet Society's participant history explicitly frames DNS as a response to the failure of a single centrally maintained table to scale.

Source: https://www.internetsociety.org/internet/history-internet/brief-history-internet/

## 5. Routing becomes a separate scaling problem

Small internets can rely on simple gateway knowledge. Large internets need routing protocols and administrative boundaries.

Research sequence:

- GGP
- HELLO
- EGP
- RIP
- IGRP
- OSPF development
- autonomous-system concept
- later BGP transition

Do not treat routing protocols as mere algorithm names. Preserve:

- topology assumptions;
- metric definitions;
- update frequency;
- convergence problems;
- operational incidents;
- code implementations;
- router memory/CPU constraints.

## 6. BITNET: a different academic network philosophy

Internet Society dates BITNET's beginning to **1980–81** and describes its use of IBM RSCS protocol lineage over direct leased lines.

Source: https://www.internetsociety.org/internet/history-internet/brief-history-internet-related-networks/

BITNET demonstrates that universities did not need IP routing to form a successful international network.

Important components:

- IBM mainframes;
- RSCS;
- NJE;
- leased point-to-point links;
- store-and-forward files/messages;
- LISTSERV;
- EARN and regional extensions;
- gateways to Internet mail.

## 7. CSNET: connect institutions that ARPANET did not reach

Internet Society's related-network history notes that CSNET used:

- **PhoneNet/MMDF** for telephone-based mail relaying;
- TCP/IP;
- the first use of TCP/IP over X.25 commercial public data networks;
- a name-server/white-pages service.

Source: https://www.internetsociety.org/internet/history-internet/brief-history-internet-related-networks/

This hybrid design is important. A site could participate without having the same expensive always-on packet infrastructure as an ARPANET site.

## 8. JANET shows another academic protocol path

The UK JANET network began in 1984 and initially used the UK Colored Book protocol suite extensively rather than simply adopting TCP/IP from day one.

Future work:

- X.25 lower-layer services;
- Yellow Book Transport Service;
- Grey Book Mail;
- Blue Book file transfer;
- name/address conventions;
- gateways to Internet services;
- transition to TCP/IP.

JANET is a warning against writing “global academic networking” as a US protocol export story only.

## 9. NORDUnet and international TCP/IP

Nordic research networking became an important bridge for international TCP/IP connectivity. This history should be reconstructed from NORDUnet archives, national research networks, satellite/cable circuits and early routing policy.

## 10. NSFNET begins as 56 kbit/s Fuzzballs

The first NSFNET backbone, operational in 1986, used **Fuzzball routers** running on DEC PDP-11 systems and 56 kbit/s circuits.

Source: https://nsf.net/projects/backbone

This is a wonderful piece of hardware/software archaeology because the later Internet backbone begins with minicomputers acting as routers, not mysterious “Internet cloud” symbols.

Reconstruction target:

```text
regional/supercomputer center LAN
  ↓ interface
PDP-11 Fuzzball
  ↓ 56 kbps serial/carrier circuit
PDP-11 Fuzzball
  ↓
next attached network
```

Document CPU model, interfaces, OS/software, routing code, line equipment and management.

## 11. 1987–1988: Merit + IBM + MCI rebuild NSFNET

NSF awarded the expanded backbone work to Merit Network with IBM and MCI in 1987. The T1 backbone entered service in July 1988.

Sources:
- https://nsf.net/timeline
- https://www.merit.edu/research/projects/the-nsfnet-backbone-service/

The T1 system is not “one router per city” in the modern sense. The NSFNET historical project describes T1 nodes built from multiple IBM RT systems cooperating as a Nodal Switching Subsystem.

Source: https://nsf.net/projects/backbone

That architecture deserves model-level recovery.

## 12. Ethernet escapes the laboratory

By the 1980s Ethernet becomes a commercial LAN technology, but multiple physical generations coexist.

### 10BASE5 / thick Ethernet

A station may require:

```text
NIC
  ↓ AUI cable
external MAU/transceiver
  ↓ vampire tap
shared thick coax
```

This is far more physical machinery than today's integrated RJ-45 port.

### 10BASE2 / thin Ethernet

BNC T-connectors and terminators move the transceiver closer to the NIC but keep a shared coax bus.

### 10BASE-T and hubs

Twisted-pair star wiring changes installation and fault isolation. Logically, hub-based Ethernet is still a shared collision domain even though the cabling looks like a star.

That distinction is crucial to explaining why “switch” later changes Ethernet behavior.

## 13. Token Ring was not stupid

IBM Token Ring and IEEE 802.5 provided deterministic token-passing access instead of Ethernet's contention model.

In an era of shared media, limited buffering and concern about predictable access, that was a rational engineering tradeoff.

Preserve:

- IBM cabling system;
- MSAU hardware;
- ring-in-star physical topology;
- token protocol;
- source-route bridging;
- 4/16 Mbit/s generations;
- PC adapter cards;
- enterprise deployment.

## 14. Bridges make LANs larger

Transparent bridges learn which MAC addresses appear behind which ports and selectively forward frames. Spanning Tree prevents loops in bridged topologies.

This is the architectural ancestor of the Ethernet switch.

A history of Ethernet that jumps directly from coax to switch misses the bridge era entirely.

## 15. FDDI, Token Bus, ARCNET and the LAN zoo

Ethernet's eventual dominance should not erase competing technologies:

- ARCNET in office/industrial environments;
- Token Bus and MAP ambitions;
- FDDI for high-speed fiber backbones;
- LocalTalk for Macintosh networks;
- proprietary workstation LANs.

Each had its own cabling, adapters, management and economic niche.

## 16. Novell NetWare creates a PC LAN world

For many PC users in the 1980s/early 1990s, networking meant:

```text
DOS workstation
  ↓ NIC + driver
IPX/SPX / NetWare client
  ↓ Ethernet/Token Ring/ARCNET
NetWare file server
```

Internet Protocol might not be present at all.

The archive should preserve:

- NE1000/NE2000 hardware;
- ODI driver model;
- IPX/SPX;
- SAP/RIP;
- bindery/NDS era differences;
- client shells;
- NetWare server versions.

## 17. AppleTalk makes networking nearly appliance-like

Apple's LocalTalk/AppleTalk stack made small-office networking comparatively easy. Low-speed serial physical networking could support naming, routing, printing and file services without an administrator assigning IP addresses.

Research:

- LocalTalk cabling/adapters;
- PhoneNET third-party wiring;
- LLAP;
- DDP;
- NBP;
- RTMP;
- EtherTalk transition;
- AppleShare.

## 18. SNA and DECnet remain major worlds

Enterprise/minicomputer networking does not vanish because TCP/IP exists.

### SNA
IBM shops depend on communications controllers, VTAM, SDLC and SNA concepts.

### DECnet
DEC shops operate multiple DECnet phases over Ethernet and WAN links.

Routers/bridges in the late 1980s often become **multiprotocol** because customers need IP, DECnet, AppleTalk, IPX, XNS and others simultaneously.

## 19. OSI is not merely a failed seven-layer diagram

OSI represents a huge international standardization effort and a serious alternative architecture.

Preserve the actual suite:

- CLNP
- ES-IS
- IS-IS
- TP0–TP4
- FTAM
- X.400
- X.500
- CMIP
- ASN.1
- government OSI profiles

The “protocol wars” are about engineering, procurement policy, international standardization, vendor power, installed bases and institutional legitimacy—not just packet-header elegance.

## 20. X.25 remains normal networking

Public X.25 networks are widely deployed through this period. Corporate users connect hosts and terminals through PADs and leased/dial access.

A person could spend the whole decade “online” without touching TCP/IP.

Important hardware:

- PADs;
- X.25 interface cards;
- carrier packet switches;
- synchronous modems/DSUs;
- terminal concentrators.

## 21. Usenet and UUCP scale a delay-tolerant social network

UUCP networks use scheduled phone calls to exchange queued data. Usenet software evolves from A News to B News to C News, with topology and traffic engineering of its own.

Preserve:

- dial schedules;
- long-distance telephone costs;
- bang paths;
- UUCP maps;
- backbone sites;
- `uucico` protocols;
- transition to NNTP.

This is networking as logistics.

## 22. BBS and FidoNet create another parallel civilization

FidoNet, beginning in 1984, automates message/file exchange between bulletin boards, often through overnight modem calls optimized around telephone tariffs.

This ecosystem has its own:

- node addressing;
- nodelists;
- echomail;
- mailers;
- BBS software;
- modem negotiation;
- routing conventions;
- gateways to Internet email/news.

It deserves equal documentary seriousness.

## 23. Hayes Smartmodem changes user-level networking hardware

The Hayes command-set model allows software to control dialing through an in-band command language. `AT` commands become a de facto compatibility expectation across many modem vendors.

The modem becomes programmable infrastructure:

```text
PC serial port
  ↓ AT commands
modem
  ↓ dialing / carrier negotiation
PSTN
```

Preserve command-set revisions, S-registers, result codes, flow control and compatibility quirks.

## 24. Modem speed becomes an arms race

300 → 1200 → 2400 → 9600 and beyond are not just numbers. Higher rates depend on increasingly complex modulation, echo cancellation, adaptive equalization, error correction and compression.

Standards and proprietary systems coexist:

- Bell standards;
- CCITT V-series;
- MNP;
- Telebit proprietary high-speed modes;
- vendor fallbacks.

## 25. TCP congestion collapse forces the Internet to learn restraint

By the late 1980s, rapid network growth exposes congestion pathologies. Van Jacobson's congestion-control work becomes essential to keeping TCP networks stable.

A mature article should recover:

- observed collapse incidents;
- code patches;
- slow start;
- congestion avoidance;
- fast retransmit ancestry;
- deployment timeline in BSD-derived stacks.

This is a reminder: the Internet architecture was not finished in 1983.

## 26. The late-1980s machine room is multiprotocol

A realistic university/company might contain:

```text
VAX running DECnet + TCP/IP
Sun workstations running TCP/IP + NFS
DOS PCs using IPX/NetWare
Macintoshes using AppleTalk
IBM mainframe using SNA
X.25 gateway/PAD for public data service
Ethernet + Token Ring segments
router supporting several protocol families
modem pool for dial-in
```

This is the environment that “TCP/IP won” must actually explain.

## What the 1980s hand to the 1990s

- TCP/IP has a broad implementation base;
- DNS and routing infrastructure are maturing;
- NSFNET is becoming a national/international backbone;
- Ethernet is spreading but not yet the only LAN;
- proprietary protocols remain normal;
- dial-up networks and online services are enormous;
- commercial Internet providers are emerging;
- network traffic growth is forcing new router and congestion-control engineering;
- OSI and X.25 are still institutionally significant.

The 1990s will be the decade when many of these worlds collapse into or connect through a commercial IP Internet—and when a large amount of visible network machinery disappears behind standard interfaces.

## Current sources

- Internet Society, related networks: https://www.internetsociety.org/internet/history-internet/brief-history-internet-related-networks/
- Internet Society, brief history: https://www.internetsociety.org/internet/history-internet/brief-history-internet/
- NSFNET timeline: https://nsf.net/timeline
- NSFNET backbone: https://nsf.net/projects/backbone
- Merit NSFNET history: https://www.merit.edu/research/projects/the-nsfnet-backbone-service/
- RFC index: https://www.rfc-editor.org/rfc-index/

## Status

**Started.** Priority follow-ups: NCP→TCP migration evidence, BSD network-stack genealogy, exact Fuzzball hardware, T1 NSFNET node architecture, JANET Colored Books, and a comparative “1988 university machine room” reconstruction.