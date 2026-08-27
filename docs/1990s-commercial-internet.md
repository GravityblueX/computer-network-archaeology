# 1990s: From a Network of Networks to Commercial Infrastructure

The 1990s are when many separate networking worlds become increasingly reachable through IP, when commercial providers replace a government-funded backbone model, when Ethernet changes from shared media to switching, and when dial-up users begin encountering the Internet directly.

The Web matters enormously, but it is not the beginning of the story. In this archive the Web is treated as a new application/traffic regime riding on decades of earlier network engineering.

## 1. ARPANET disappears without taking the Internet with it

ARPANET was decommissioned in 1990. By then, the Internet was already larger than the research network that had helped incubate it.

That single fact is conceptually useful:

> the Internet is not ARPANET with a new name.

It is an internetwork architecture and an expanding set of independently operated networks using compatible protocols.

## 2. NSFNET becomes the visible backbone of US academic Internet growth

The NSFNET historical project describes the sequence:

- 56 kbit/s backbone in 1986;
- T1 expansion in 1988;
- T3/45 Mbit/s era by 1991;
- retirement of the backbone service on 30 April 1995.

Sources:
- https://nsf.net/timeline
- https://nsf.net/projects/backbone
- https://www.merit.edu/research/projects/the-nsfnet-backbone-service/

The technical archaeology must recover all three hardware generations, not just speeds.

## 3. NSFNET's T1 node was a machine cluster, not a black router icon

The NSFNET historical project says the T1 Nodal Switching Subsystem used multiple IBM RT systems working together. The later T3 architecture used IBM RS/6000 hardware.

Source: https://nsf.net/projects/backbone

A mature reconstruction should identify:

- exact RT models;
- number and role of processors;
- interface adapters;
- operating system/software;
- routing implementation;
- MCI carrier equipment;
- network-management links;
- power/rack arrangement;
- failure modes and field replacement procedures.

## 4. Growth is visible in packet counts

NSFNET archival project milestones include:

- more than 500 connected networks by 1989;
- roughly 10 billion packets/month by 1990;
- 60.6 billion packets in June 1994.

Source: https://nsf.net/achievements

These numbers matter because they explain why router performance, addressing and routing-table scale become urgent engineering problems.

## 5. Internationalization is not merely “foreign sites join America”

By the early 1990s, research networks in Europe, Asia-Pacific and elsewhere have their own histories, protocol transitions and infrastructure. NSFNET links are one component of a broader global graph.

The repository should reconstruct:

- NORDUnet;
- JANET;
- SURFnet;
- DFN;
- RENATER;
- AARNet;
- WIDE;
- EARN;
- national PTT/public data networks;
- transatlantic/transpacific circuits;
- routing policy and exchange points.

National networking history should not be reduced to “date of first Internet connection”.

## 6. BGP evolves because EGP's model no longer fits

An Internet made of many autonomous organizations needs policy-aware interdomain routing.

Track by version:

- BGP-1
- BGP-2
- BGP-3
- BGP-4

Important changes include path-vector behavior, classless routing integration and policy expression.

The hardware context matters: router RAM, CPU, forwarding implementation and route-table growth constrain what protocols can practically do.

## 7. CIDR is an operational rescue, not a cosmetic address notation change

Classful A/B/C allocation wasted address space and inflated routing tables. Classless Inter-Domain Routing permits variable-length prefixes and aggregation.

Archaeological tasks:

- pre-CIDR allocation records;
- route-table growth graphs;
- RFC 1518/1519 era;
- router software support;
- provider aggregation practice;
- transition pain.

## 8. The commercial Internet transition is institutional engineering

The NSFNET backbone did not simply switch off and “the free market took over”. A new interconnection architecture had to exist.

Research topics:

- NSF Acceptable Use Policy;
- ANS and ANS CO+RE;
- Commercial Internet eXchange (CIX);
- FIX-East/FIX-West;
- Network Access Points;
- commercial backbone providers;
- routing-policy coordination;
- address/ASN registry changes;
- NSFNET phase-out contracts.

The NSFNET archive explicitly records contemporary controversy over commercial traffic and ANS arrangements.

Source: https://nsf.net/about

## 9. Providers become historical networks in their own right

The project should reconstruct provider backbones rather than merely list company names:

- UUNET / AlterNet
- PSINet
- CERFnet
- SprintLink
- MCI Internet
- BBN Planet
- Netcom
- ANSNet
- regional ISP backbones

For each:

- POP locations;
- router models;
- leased circuits;
- exchange-point presence;
- routing policies;
- modem/access infrastructure;
- acquisitions/renamings;
- topology maps.

## 10. Dial-up IP reaches ordinary users

The access path of a 1990s user can be reconstructed physically:

```text
PC
  ↓ serial port
external/internal modem
  ↓ analog local loop
telephone switch network
  ↓
ISP modem bank / digital access server
  ↓ terminal/access server
PPP or SLIP
  ↓
ISP IP network
  ↓
Internet backbone
```

This stack deserves the same detail as ARPANET.

## 11. SLIP and PPP

### SLIP
Serial Line Internet Protocol provides a minimal way to carry IP datagrams over serial links but offers limited negotiation/control.

### PPP
Point-to-Point Protocol adds link negotiation, authentication options and network-control protocols.

Preserve:

- LCP;
- IPCP;
- PAP;
- CHAP;
- async framing;
- compression options;
- terminal-server implementation differences;
- Windows/Mac/Unix dialer behavior.

## 12. The modem's last great technical generations

1990s dial-up speed progression includes:

- 9600/14.4 kbit/s V.32/V.32bis-era systems;
- V.34 / 28.8–33.6 kbit/s generations;
- 56k technologies and the eventual V.90 standard;
- V.92 refinements.

The nominal speed hides a remarkable amount of signal processing:

- adaptive equalization;
- echo cancellation;
- trellis-coded modulation;
- retraining;
- fallback;
- V.42 error correction;
- V.42bis compression;
- proprietary pre-standard 56k incompatibility.

## 13. Modem banks turn into access servers

An ISP may have hundreds of incoming analog calls. That requires:

- PRI/T1/E1 trunks;
- digital modem shelves;
- terminal/access servers;
- RADIUS/TACACS-style AAA;
- address pools;
- PPP negotiation;
- accounting;
- load management.

Hardware leads:

- USRobotics Total Control
- Ascend MAX family
- Livingston PortMaster
- Cisco access-server families
- vendor integrated modem/PRI chassis

This is a major missing material culture of the consumer Internet.

## 14. Ethernet physically changes its meaning

### Shared coax era
Everyone sees the same medium; collisions are expected.

### Hub era
Cabling becomes a star, but the hub repeats bits; one collision domain remains.

### Bridge era
Traffic is filtered by learned MAC location.

### Switch era
A multiport bridge gives each station/segment a separate collision domain; eventually full duplex removes CSMA/CD from normal point-to-point use.

This means the word **Ethernet** survives while its physical/operational reality changes drastically.

## 15. Fast Ethernet and autonegotiation

The shift to 100 Mbit/s creates new PHYs, switches and negotiation issues. Research should preserve:

- 100BASE-TX/T4/FX;
- 802.3u;
- autonegotiation ancestry;
- half/full duplex mismatch failures;
- Category cabling assumptions;
- repeater class restrictions.

## 16. VLANs make one physical switch behave like multiple logical LANs

IEEE 802.1Q and vendor predecessors change campus-network design by decoupling broadcast domains from simple physical wiring.

Track early proprietary VLAN/trunking schemes as well as standardization.

## 17. Frame Relay: WANs between X.25 and IP/MPLS worlds

Frame Relay strips much of X.25's hop-by-hop reliability from carrier packet networks under the assumption that digital lines are cleaner.

Important material:

- DLCIs;
- PVCs;
- LMI variants;
- FRADs;
- router serial interfaces;
- CIR/traffic contracts;
- provider cloud design.

Frame Relay is essential for understanding 1990s enterprise WANs.

## 18. ATM: the future that became infrastructure but not the universal endpoint LAN

ATM promised one cell-based architecture for voice, video and data. It became important in carrier backbones and some campus networks, but Ethernet/IP remained dominant at endpoints.

Preserve:

- 53-byte cell rationale;
- UNI/NNI;
- AAL5;
- PVC/SVC;
- ATM switches;
- LAN Emulation;
- Classical IP over ATM;
- MPOA;
- DSL/backhaul afterlife.

“ATM failed” is far too simple.

## 19. ISDN as both endpoint access and digital telecom archaeology

ISDN BRI/PRI exposes telephone-network digital channels to customers. It intersects:

- dial-up Internet;
- routers;
- terminal adapters;
- digital modem banks;
- videoconferencing;
- business WAN access.

Its D/B channel separation and Q.921/Q.931 signaling deserve preservation.

## 20. The Web changes network demand

NCSA Mosaic (1993) and later browsers make Internet resources much easier to navigate. This changes:

- traffic composition;
- public interest;
- commercial demand;
- server deployment;
- ISP growth;
- cache/proxy use;
- backbone capacity planning.

But Web packets still traverse routers, leased lines, Ethernet, modems and TCP/IP built from earlier layers.

## 21. Gopher, WAIS and FTP do not vanish instantly

Early 1990s information retrieval is plural:

- Gopher menus;
- WAIS search;
- anonymous FTP archives;
- Archie indexes;
- Usenet;
- IRC;
- Web.

The Web wins gradually. Preserve the overlap period.

## 22. Multiprotocol networks persist into the decade

A 1993 enterprise/campus might still carry:

- IPv4;
- IPX/SPX;
- AppleTalk;
- DECnet;
- SNA encapsulation;
- XNS;
- OSI/CLNP;
- bridging protocols.

Cisco and other routers market multiprotocol capability because customers actually need it.

The Internet does not conquer an empty landscape.

## 23. NAT and private addressing emerge from scaling pressure

As IPv4 address scarcity and security/administrative practices change, private addressing and Network Address Translation become increasingly common.

Track:

- RFC 1597/1918 lineage;
- NAT terminology;
- router/firewall implementations;
- impact on end-to-end connectivity;
- home/SOHO broadband adoption later in the decade/2000s.

## 24. Linux becomes network infrastructure

Linux in the 1990s rapidly gains networking stacks, routing/firewall features, driver support and server software. It becomes practical to build routers, dial-in servers and Internet servers from commodity PCs.

Preserve:

- early TCP/IP stack history;
- `ifconfig`/`route`/net-tools;
- IP forwarding;
- IP firewall code generations;
- PPP daemon;
- SLIP;
- routing daemons;
- NIC driver support.

## 25. 30 April 1995: NSFNET backbone service ends

The NSFNET historical project and Merit identify **30 April 1995** as the end of the NSFNET Backbone Service.

Sources:
- https://nsf.net/timeline
- https://www.merit.edu/research/projects/the-nsfnet-backbone-service/

The importance is not that a cable was unplugged and the Internet suddenly became commercial. The importance is that enough private backbones, exchange mechanisms, regional networks and routing arrangements existed for the research backbone to stop serving as the central transit infrastructure.

## 26. The cloud symbol begins to hide physical history

Network diagrams increasingly draw carrier/Internet infrastructure as a cloud:

```text
LAN ─ router ─ ☁ ─ router ─ LAN
```

The archaeological mission is to open that cloud:

- which provider?
- what POP?
- which router?
- what circuit?
- what line speed?
- what exchange point?
- which routing policy?
- what modem/access server?
- what failure mode?

The 1990s are when hiding infrastructure behind an abstraction becomes operationally useful—and historically dangerous.

## Primary-source targets

- Merit NSFNET final reports
- NSF solicitations and policy documents
- ANS/CIX/NAP records
- early ISP topology maps
- Route Views/early routing-table archives
- BGP RFC/version documents
- router vendor manuals/configuration guides
- modem manuals and CCITT/ITU V-series standards
- Livingston/Ascend/USR access-server manuals
- Frame Relay Forum documents
- ATM Forum specifications
- early Ethernet switch manuals
- ISP advertisements/pricing
- dial-up software packages and screenshots

## Current anchors

- NSFNET timeline: https://nsf.net/timeline
- NSFNET backbone: https://nsf.net/projects/backbone
- NSFNET achievements: https://nsf.net/achievements
- NSFNET overview/commercialization: https://nsf.net/about
- Merit NSFNET history: https://www.merit.edu/research/projects/the-nsfnet-backbone-service/
- Internet Society history: https://www.internetsociety.org/internet/history-internet/brief-history-internet/

## Status

**Started.** High-priority next work: commercial ISP topology/hardware, BGP-1→4 genealogy, dial-up ISP access-stack reconstruction, and shared-Ethernet→switch timeline with actual products.