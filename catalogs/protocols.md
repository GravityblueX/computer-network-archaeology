# Protocol and Standards Inventory

This is a discovery catalog, not a claim that all listed protocols were interoperable, equally important, or simultaneously deployed. The purpose is to prevent the history from collapsing into “Ethernet + IP + TCP + HTTP”.

A protocol family should eventually have one record **per significant revision**, with the defining documents, implementation evidence and deployment history separated.

Runnable reconstructions belong primarily in [tmzncty/protocol-zoo](https://github.com/tmzncty/protocol-zoo).

## Telegraph/terminal/data-link ancestry

- Baudot / ITA2 teleprinter coding
- ASCII and early ASCII revisions
- EBCDIC in data communications
- synchronous vs asynchronous serial framing
- start/stop telegraphy
- half-duplex line-control conventions
- IBM Bisync / BSC
- IBM SDLC
- HDLC
- ADCCP
- LAP / LAPB
- DDCMP
- character-oriented line disciplines
- block-mode terminal protocols

## Physical/serial interface standards and conventions

These are not packet protocols, but they determine what could physically interoperate.

- EIA RS-232 revisions
- RS-232-C
- V.24 / V.28 interface recommendations
- RS-422
- RS-423
- RS-449
- X.21
- V.35
- current-loop teletype interfaces
- modem control signals: DTR, DSR, RTS, CTS, DCD, RI and related conventions

## Modem/data-transmission standards

Track Bell System data-set practices separately from CCITT/ITU-T V-series standards.

### Bell System / North American modem lineages
- Bell 101 family — exact chronology requires primary-source resolution
- Bell 103
- Bell 113
- Bell 201
- Bell 202
- Bell 208
- Bell 212A
- Bell 209 / leased-line families
- Bell 434 and other data-set families to verify

### CCITT/ITU-T V-series research leads
- V.21
- V.22
- V.22bis
- V.23
- V.26 / V.26bis / V.26ter
- V.27 / V.27bis / V.27ter
- V.29
- V.32
- V.32bis
- V.32terbo (industry extension; not an ITU recommendation)
- V.34
- V.90
- V.92
- V.42 error correction
- V.42bis compression
- MNP classes/protocols

For each modem standard eventually record symbol rate, bit rate, duplex assumptions, modulation, fallback, negotiation and line requirements.

## ARPANET host/IMP and early host protocols

- Host–IMP interface
- IMP leader/message formats
- RFNM flow control
- Host-to-Host protocol proposals
- NCP / Network Control Program
- Initial Connection Protocol (ICP)
- Telnet early forms
- FTP early forms
- Mail protocols before SMTP
- Network Graphics Protocol
- Remote Job Entry protocols
- NETRJS
- DEL / Decode Encode Language proposal
- ARPANET measurement/trace conventions

### Early RFC documentary sequence

At minimum, annotate RFC 1 onward in chronological context. Examples:

- RFC 1 — *Host Software* (1969)
- RFC 2 — *Host software*
- RFC 3 — *Documentation conventions*
- RFC 4 — *Network timetable*
- RFC 5 — *Decode Encode Language (DEL)*
- RFC 6 — *Conversation with Bob Kahn*
- RFC 7 — *Host-IMP interface*
- RFC 8 — *ARPA Network Functional Specifications*

Canonical index: https://www.rfc-editor.org/rfc-index/

## Packet-switching and internetworking research protocols

- NPL packet formats/protocols
- CYCLADES datagram protocols
- CIGALE/Mitranet internal protocols
- STST transport protocol
- INWG internetworking proposals
- International Packet Network Working Group proposals
- Internet Experiment Notes (IEN) corpus
- Cerf/Kahn early Transmission Control Program
- pre-split TCP versions
- TCP after TCP/IP split
- Internet Protocol experimental versions
- IP version-number history

## ALOHA / random-access / packet radio

- Pure ALOHA
- Slotted ALOHA
- ALOHAnet terminal/channel protocols
- packet-radio MAC research
- PRNET protocols
- amateur packet-radio AX.25
- KISS TNC framing (later amateur packet-radio ecosystem)

## Ethernet and LAN standards/protocols

### Xerox/PARC lineage
- experimental Ethernet (2.94 Mbit/s)
- PUP / PARC Universal Packet
- PUP internetwork routing/transport/application protocols
- XNS Internet Datagram Protocol
- XNS SPP
- XNS RIP lineage
- XNS Courier/RPC-related protocols

### Ethernet standardization
- DIX Ethernet Version 1
- DIX Ethernet Version 2 / Ethernet II
- IEEE 802
- IEEE 802.3
- LLC / IEEE 802.2
- SNAP
- CSMA/CD
- 10BASE5
- 10BASE2
- 10BASE-T
- Fast Ethernet / 100BASE-* families
- autonegotiation
- full-duplex Ethernet

### Bridging/switching
- transparent bridging
- Spanning Tree Protocol / IEEE 802.1D
- source-route bridging
- VLAN / IEEE 802.1Q
- link aggregation lineage

### Other LANs
- ARCNET
- Token Ring / IEEE 802.5
- Token Bus / IEEE 802.4
- FDDI
- Cambridge Ring protocols
- Chaosnet protocols
- LocalTalk link protocol

## X.25 and public data-network protocol families

- X.25, edition by edition
- X.3 PAD parameters
- X.28 terminal-to-PAD procedures
- X.29 PAD-to-host procedures
- X.75 inter-network signaling
- LAPB
- virtual-call setup/clear procedures
- permanent virtual circuits
- packet-layer numbering/windowing revisions

CCITT adopted X.25 in 1976; later colored-book editions must be treated as revisions rather than one static protocol.

## OSI protocol suite

- OSI Basic Reference Model / ISO 7498
- CLNP / ISO 8473
- ES-IS
- IS-IS
- TP0
- TP1
- TP2
- TP3
- TP4
- Session layer protocols
- Presentation layer protocols
- FTAM
- X.400 messaging
- X.500 directory
- ROSE
- CMIP
- ASN.1 / BER as infrastructure for many OSI and telecom protocols
- GOSIP profiles
- MAP/TOP profiles

## IBM networking

- SNA architecture
- SDLC
- PU/LU concepts
- LU 6.2 / APPC
- VTAM-related protocols/interfaces
- APPN
- HPR
- RSCS
- NJE

## DEC networking

Track by DECnet phase rather than using “DECnet” as one timeless protocol.

- DECnet Phase I
- Phase II
- Phase III
- Phase IV
- Phase IV+ extensions
- Phase V / DECnet-Plus / OSI transition
- DDCMP
- NSP
- Routing protocols
- MOP
- LAT
- DNA architecture

## Apple networking

- AppleTalk Phase 1
- AppleTalk Phase 2
- LocalTalk Link Access Protocol (LLAP)
- DDP
- RTMP
- NBP
- ATP
- PAP
- AFP
- EtherTalk
- TokenTalk

## Novell networking

- IPX
- SPX
- RIP (Novell variant)
- SAP
- NCP (NetWare Core Protocol — distinguish from ARPANET NCP)
- NetBIOS over IPX/SPX variants

## Banyan / PC LAN / enterprise protocols

- Banyan VINES VIP
- StreetTalk protocols
- NetBIOS
- NetBEUI
- SMB early dialects
- LAN Manager transport conventions
- IBM PC Network protocols
- 3Com/3+ networking

## Unix networking and distributed systems

- UUCP protocols (`g`, `f`, and other variants)
- uux / UUCP job transfer conventions
- Usenet A News propagation
- B News
- C News
- NNTP
- Sun RPC / ONC RPC
- XDR
- NFS versions
- Yellow Pages / NIS
- R protocols (`rlogin`, `rsh`, `rexec`)

## Core Internet Protocol suite — historical revisions matter

### Internet layer
- IPv4 / RFC 791 and predecessor documents
- ICMP / RFC 792 and revisions
- IGMP versions
- ARP
- RARP
- BOOTP
- DHCP lineage
- fragmentation/reassembly rules
- source routing options
- IP options no longer commonly used

### Transport
- TCP historical revisions
- UDP
- RDP
- NETBLT
- VMTP
- XTP research lineage

### Routing
- Gateway-to-Gateway Protocol (GGP)
- HELLO
- EGP
- RIP
- IGRP
- EIGRP
- OSPFv1/v2
- IS-IS in IP networks
- BGP-1
- BGP-2
- BGP-3
- BGP-4
- CIDR
- route aggregation

### Naming/directory/configuration
- HOSTS.TXT distribution
- IEN-era naming proposals
- DNS RFC 882/883
- DNS RFC 1034/1035
- domain-registration procedures
- WHOIS
- NICNAME
- BOOTP
- DHCP

### Remote login / file transfer / mail
- Telnet
- FTP
- TFTP
- SMTP
- Mail Transfer Protocol predecessors
- POP1/POP2/POP3
- IMAP versions
- MIME
- finger
- talk

### Network management/time
- ICMP control/error mechanisms
- SNMPv1
- SNMPv2 lineage
- CMOT (CMIP over TCP/IP) historical competition
- NTP versions
- daytime/time protocols
- syslog evolution

## Pre-Web and early Internet information systems

- Archie
- Gopher
- Gopher+
- WAIS
- Veronica
- Jughead
- WHOIS/NIC services
- anonymous FTP conventions
- NNTP
- IRC protocol

## Web-era protocols included where they explain network transformation

- HTTP/0.9
- HTTP/1.0
- HTTP/1.1
- early proxy conventions
- SOCKS
- SSL versions
- TLS lineage

The repository is not primarily a Web-history archive; preserve enough to explain traffic, access and infrastructure change.

## Dial-up Internet access

- SLIP
- CSLIP
- PPP
- PAP
- CHAP
- IPCP
- LCP
- Multilink PPP
- PPP over ISDN links
- RADIUS
- TACACS/TACACS+

## Carrier/WAN protocols that shaped enterprise Internet access

- Frame Relay
- LAPF/Q.922
- ATM
- AAL5
- SMDS
- PPP/HDLC on leased serial links
- Cisco HDLC
- ISDN Q.921/Q.931
- SONET/SDH framing context

## Network-management and operations protocols worth preserving

- ARPANET NMC measurement protocols
- CMIP/CMIS
- SNMP
- RMON
- TFTP-based boot/config transfer
- BOOTP-based diskless boot
- Cisco Discovery Protocol (later period)
- vendor proprietary management protocols

## Protocol-document archives to index deeply

- RFC series
- Internet Experiment Notes (IEN)
- ARPANET Network Working Group notes
- BBN reports
- NPL reports
- CYCLADES/INWG papers and notes
- CCITT Yellow/Red/Blue Book X-series recommendations
- ISO/IEC OSI standards
- IEEE 802 standards and drafts
- DEC Digital Network Architecture documentation
- IBM SNA manuals
- Xerox PUP/XNS documentation
- AppleTalk protocol documentation
- Novell NetWare protocol documentation

## Naming collisions that require explicit disambiguation

- **NCP** — ARPANET Network Control Program vs Novell NetWare Core Protocol
- **RIP** — Internet Routing Information Protocol vs similarly named vendor variants
- **ICP** — Initial Connection Protocol and unrelated later uses
- **IP** — Internet Protocol vs generic “internetwork protocol” language in old documents
- **Ethernet** — experimental PARC Ethernet vs DIX Ethernet vs IEEE 802.3 families

## Archaeological rule

Every protocol entry should eventually answer:

1. Which exact document defined this version?
2. What problem was it designed to solve?
3. What lower-layer service did it assume?
4. What state did endpoints/network nodes keep?
5. What were the header fields and limits?
6. How were errors, loss, duplication and reordering treated?
7. Was interoperability ever demonstrated?
8. Which implementations shipped?
9. Where was it deployed?
10. What replaced it, and what survived conceptually?

A protocol that “lost” is often more historically informative than a protocol that became invisible through success.