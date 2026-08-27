# Research Roadmap

This roadmap is intentionally oversized. The project goal is not to choose a few famous milestones; it is to build an ever-denser map of surviving evidence.

Checkboxes mean **coverage status**, not historical importance.

## Phase 0 — archival infrastructure

- [x] repository mission and scope
- [x] AI authorship disclosure
- [x] source/evidence policy
- [x] contributor/agent rules
- [ ] controlled vocabulary for artifact types
- [ ] YAML/JSON schema for artifact records
- [ ] source checksum workflow
- [ ] dead-link/archival-link checker
- [ ] citation linter
- [ ] chronology consistency checks
- [ ] rights/license field for every mirrored document
- [ ] index of museums/archives holding surviving hardware

## 1940s–1950s — prehistory of computer networking

### Communication infrastructure
- [ ] telegraph store-and-forward practice
- [ ] teletypewriter networks
- [ ] private wire / leased-line services
- [ ] telephone switching assumptions inherited by data communications
- [ ] early carrier systems and multiplexing
- [ ] T-carrier development and T1
- [ ] conditioned vs unconditioned voice-grade circuits
- [ ] Bell System data services and tariffs

### Radar, command-and-control and remote data
- [ ] Whirlwind
- [ ] Cape Cod System
- [ ] SAGE architecture
- [ ] SAGE data terminals
- [ ] SAGE communications links
- [ ] SAGE modems/data sets
- [ ] AN/FSQ-7 and communication peripherals
- [ ] light-gun/operator-console networking implications
- [ ] Air Force Cambridge Research Center modem work

### Early modems/data sets
- [ ] resolve Bell 101 / Bell 103 dating and naming from primary AT&T documents
- [ ] Data Set 101 family
- [ ] Data Set 103 family
- [ ] FSK signaling details
- [ ] originate/answer frequency plans
- [ ] 110 bps vs 300 bps services
- [ ] private-line vs dial-up modem engineering
- [ ] early modem competitors and compatibility problems

### Transaction and reservation systems
- [ ] American Airlines/IBM SABRE ancestry from SAGE
- [ ] IBM reservation terminal hardware
- [ ] ERMA / banking data communications context
- [ ] railway reservation systems
- [ ] point-of-sale/transaction-network precursors

## 1960s — remote access, time-sharing and packet switching

### Terminals and access
- [ ] Teletype Model 33 ASR/KSR
- [ ] Teletype Model 35
- [ ] IBM 2741
- [ ] Selectric-based terminals
- [ ] acoustic couplers
- [ ] terminal multiplexers
- [ ] serial interfaces before RS-232 standardization
- [ ] EIA RS-232 revisions
- [ ] character encodings used by terminals

### Time-sharing
- [ ] CTSS remote access
- [ ] Project MAC
- [ ] DTSS
- [ ] MULTICS networking precursors
- [ ] remote-job-entry systems
- [ ] terminal concentrators/front-end processors

### Packet-switching ideas
- [ ] Paul Baran RAND distributed communications reports
- [ ] Donald Davies NPL packet-switching work
- [ ] NPL Data Communications Network hardware/software
- [ ] Leonard Kleinrock queueing work and its actual role
- [ ] message switching vs packet switching terminology
- [ ] store-and-forward ancestry
- [ ] datagram vs virtual-circuit ancestry

### ARPANET design/build
- [ ] ARPA/IPTO institutional history
- [ ] Licklider
- [ ] Ivan Sutherland
- [ ] Bob Taylor
- [ ] Larry Roberts
- [ ] BBN proposal and contract
- [ ] Frank Heart team
- [ ] Honeywell DDP-516 IMP
- [ ] ruggedization and packaging
- [ ] IMP software architecture
- [ ] Host–IMP interface electrical/logical details
- [ ] 50 kbit/s leased circuits
- [ ] modems/data sets used on early ARPANET lines
- [ ] RFNM flow control
- [ ] IMP packet/message sizes
- [ ] routing algorithm revisions
- [ ] Network Measurement Center
- [ ] UCLA, SRI, UCSB, Utah first-node host hardware
- [ ] SDS Sigma 7 host integration
- [ ] SDS 940 at SRI
- [ ] IBM 360/75 at UCSB
- [ ] DEC PDP-10 at Utah
- [ ] 1969 first-message chronology and logs

### Early RFC corpus
- [ ] RFC 1–10 annotated guide
- [ ] Host Software proposals
- [ ] DEL
- [ ] Host–IMP interface notes
- [ ] documentation conventions
- [ ] NCP evolution

## 1970s — many networks, many architectural bets

### ARPANET expansion
- [ ] IMP revisions
- [ ] TIP terminal access
- [ ] Pluribus IMP
- [ ] network maps by year
- [ ] line-rate upgrades
- [ ] satellite links
- [ ] ARPANET operational procedures
- [ ] Network Control Program
- [ ] Telnet evolution
- [ ] FTP evolution
- [ ] electronic mail protocol evolution
- [ ] host tables and NIC services

### Packet radio / satellite
- [ ] ALOHAnet hardware and radio channels
- [ ] Pure ALOHA / Slotted ALOHA
- [ ] PRNET
- [ ] SATNET
- [ ] Atlantic Packet Satellite Network
- [ ] packet-radio terminals
- [ ] internetworking experiments across ARPANET/PRNET/SATNET

### Europe and alternative packet networks
- [ ] NPL operational network
- [ ] CYCLADES/Cigale
- [ ] Mitra 15 packet switches
- [ ] STST transport protocol
- [ ] datagram architecture
- [ ] INWG
- [ ] EIN / European Informatics Network
- [ ] EPSS
- [ ] RCP
- [ ] TRANSPAC
- [ ] DATAPAC
- [ ] EIN/Euronet
- [ ] RETD

### Commercial packet switching
- [ ] Tymnet
- [ ] Telenet
- [ ] packet assemblers/disassemblers (PADs)
- [ ] virtual circuits
- [ ] X.25 1976 edition and later revisions
- [ ] X.3 / X.28 / X.29
- [ ] public data network tariffs and access methods
- [ ] statistical multiplexers

### Internetworking
- [ ] Cerf/Kahn 1974 paper
- [ ] early TCP versions
- [ ] TCP split into TCP + IP
- [ ] Internet Experiment Notes
- [ ] gateway concepts
- [ ] end-to-end principle precursors
- [ ] internetwork packet formats
- [ ] addressing evolution

### LANs
- [ ] Xerox PARC experimental Ethernet
- [ ] Alto Aloha Network / Ethernet naming
- [ ] 2.94 Mbit/s Ethernet
- [ ] PARC Universal Packet (PUP)
- [ ] DEC/Intel/Xerox Ethernet (DIX)
- [ ] thick coax physical topology
- [ ] transceivers and taps
- [ ] contention/collision detection engineering
- [ ] ARCNET
- [ ] Cambridge Ring
- [ ] Chaosnet

### Vendor architectures
- [ ] IBM SNA
- [ ] DECnet phases
- [ ] Xerox XNS ancestry
- [ ] Burroughs networking
- [ ] Honeywell networks
- [ ] proprietary terminal networks

## 1980s — protocol wars and network multiplication

### TCP/IP transition
- [ ] January 1, 1983 ARPANET flag day
- [ ] NCP retirement
- [ ] BSD TCP/IP distribution history
- [ ] sockets API
- [ ] 4.1cBSD / 4.2BSD networking
- [ ] TCP congestion collapse episodes
- [ ] Van Jacobson congestion control

### Naming/routing
- [ ] HOSTS.TXT scaling problem
- [ ] DNS design
- [ ] RFC 882/883 → 1034/1035
- [ ] root server history
- [ ] EGP
- [ ] RIP
- [ ] HELLO
- [ ] IGRP
- [ ] OSPF origins
- [ ] autonomous-system numbering

### Academic networks
- [ ] CSNET
- [ ] PhoneNet/MMDF
- [ ] TCP/IP over X.25
- [ ] BITNET
- [ ] RSCS/NJE
- [ ] EARN
- [ ] JANET
- [ ] NORDUnet
- [ ] HEPNET
- [ ] MFENET
- [ ] SPAN
- [ ] regional research networks

### UUCP/Usenet
- [ ] UUCP protocol and software history
- [ ] dial-up store-and-forward topology
- [ ] bang paths
- [ ] Usenet A/B/C News
- [ ] maps and backbone sites
- [ ] news transport protocols

### LAN technologies
- [ ] IEEE 802 process
- [ ] IEEE 802.3 Ethernet
- [ ] 10BASE5
- [ ] vampire taps
- [ ] AUI
- [ ] 10BASE2
- [ ] repeaters
- [ ] bridges
- [ ] Spanning Tree Protocol
- [ ] Token Ring
- [ ] IBM cabling system
- [ ] Token Bus
- [ ] FDDI
- [ ] LocalTalk/AppleTalk
- [ ] EtherTalk

### Personal-computer networking
- [ ] Novell NetWare
- [ ] IPX/SPX
- [ ] Microsoft LAN Manager
- [ ] IBM PC Network
- [ ] Banyan VINES
- [ ] TOPS
- [ ] PC-NFS
- [ ] network interface cards and drivers

### Online services / dial-up worlds
- [ ] bulletin board systems
- [ ] FidoNet
- [ ] CompuServe
- [ ] The Source
- [ ] GEnie
- [ ] Minitel
- [ ] Prestel
- [ ] videotex modems/terminals
- [ ] modem speed ladder: 300/1200/2400/9600 etc.
- [ ] Hayes Smartmodem and AT command set
- [ ] error correction and compression standards

### OSI and standards wars
- [ ] OSI reference model history
- [ ] ISO 7498
- [ ] CLNP
- [ ] TP0–TP4
- [ ] FTAM
- [ ] X.400
- [ ] X.500
- [ ] GOSIP
- [ ] MAP/TOP industrial networking
- [ ] coexistence and multiprotocol routers

## NSFNET and the late 1980s–1990s Internet

- [ ] NSF supercomputer-center network plan
- [ ] original 56 kbit/s Fuzzball backbone
- [ ] David Mills' Fuzzball routers
- [ ] Merit/IBM/MCI partnership
- [ ] IBM RT-based T1 nodes
- [ ] T1 backbone architecture
- [ ] RS/6000-based T3 nodes
- [ ] Network Operations Center
- [ ] regional network attachment
- [ ] acceptable-use policy
- [ ] ANS and ANS CO+RE
- [ ] commercialization disputes
- [ ] FIX-E/FIX-W
- [ ] NAP transition
- [ ] NSFNET shutdown, 30 April 1995

## 1990s — commercial Internet and physical transformation

### Routing
- [ ] BGP-1
- [ ] BGP-2
- [ ] BGP-3
- [ ] BGP-4
- [ ] CIDR
- [ ] route-server history
- [ ] early commercial exchange points

### Access
- [ ] SLIP
- [ ] PPP
- [ ] terminal servers
- [ ] dial-up IP
- [ ] 14.4/28.8/33.6/56k modem generations
- [ ] V.32/V.32bis/V.34/V.90/V.92 chronology
- [ ] ISDN BRI/PRI access
- [ ] CSU/DSU
- [ ] T1/E1 leased Internet access
- [ ] frame relay
- [ ] ATM

### Ethernet physical evolution
- [ ] 10BASE-T
- [ ] hubs
- [ ] twisted-pair transceivers
- [ ] switching Ethernet
- [ ] Fast Ethernet
- [ ] autonegotiation
- [ ] VLANs / 802.1Q
- [ ] full-duplex Ethernet

### Internet applications as network drivers
- [ ] Gopher
- [ ] WAIS
- [ ] IRC
- [ ] early web deployment
- [ ] HTTP protocol revisions
- [ ] Mosaic/Netscape traffic effects
- [ ] SMTP operational history
- [ ] POP/IMAP
- [ ] FTP decline/continuity

### Service-provider hardware
- [ ] Cisco router families
- [ ] Proteon
- [ ] Wellfleet/Bay Networks
- [ ] 3Com
- [ ] Ascend terminal servers
- [ ] Livingston PortMaster
- [ ] modem banks
- [ ] access concentrators
- [ ] early carrier-class routers

## Cross-cutting catalogs

### Hardware families
- [ ] modem/data-set catalog
- [ ] acoustic-coupler catalog
- [ ] terminal catalog
- [ ] front-end processor catalog
- [ ] packet-switch catalog
- [ ] IMP/TIP catalog
- [ ] router catalog
- [ ] repeater/bridge/hub/switch catalog
- [ ] NIC/transceiver catalog
- [ ] CSU/DSU catalog
- [ ] terminal-server/PAD catalog
- [ ] multiplexers/channel banks

### Protocol/document families
- [ ] ARPANET RFC/NCP corpus
- [ ] Internet Experiment Notes
- [ ] TCP/IP RFC evolution
- [ ] Ethernet/DIX/IEEE 802.3 documents
- [ ] X.25 editions
- [ ] OSI suite
- [ ] SNA documentation
- [ ] DECnet documentation
- [ ] XNS/PUP documentation
- [ ] AppleTalk documentation
- [ ] IPX/SPX documentation
- [ ] modem V-series recommendations

### Organizations
- [ ] ARPA/DARPA/IPTO
- [ ] BBN
- [ ] NPL
- [ ] IRIA/Inria
- [ ] CCITT/ITU-T
- [ ] ISO
- [ ] IEEE 802
- [ ] IETF/IAB ancestry
- [ ] Network Working Group
- [ ] ICCC/INWG
- [ ] NSF
- [ ] Merit Network
- [ ] major PTTs/telcos
- [ ] major networking vendors

### Human history
- [ ] oral-history index by person
- [ ] engineer/administrator/operator biographies
- [ ] lesser-known contributors
- [ ] women in networking history
- [ ] technicians and operations staff
- [ ] regional histories outside the United States

## Ultimate archival questions

For every historically important network we should eventually be able to answer:

- What machines were connected?
- Through what interface?
- To what box?
- Over what physical medium/service?
- At what speed?
- With what framing and error control?
- Who paid for the circuit?
- Which organization operated each layer?
- What software ran on hosts and switching nodes?
- Which protocols were actually deployed at each date?
- How were addresses assigned?
- How did routing work?
- How did names/directories work?
- How was the network monitored?
- What happened when a link/node failed?
- What did operators see?
- What did users see?
- What documents survive?
- What hardware survives?
- What source code survives?
- What is still uncertain?

When the repository can answer those questions repeatedly across decades, it will have become more than a timeline: it will be an archaeological reconstruction of networking as infrastructure.