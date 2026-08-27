# Primary Source Excavation Guide

This repository should ultimately be navigable not only by technology but by **surviving evidence**. This file records high-value primary-source corpora and the questions they can answer.

The goal is not merely to link famous documents. It is to recover enough documentary strata to reconstruct actual installations, software revisions, protocol changes and operational practice.

## 1. RFC Series

Canonical home: https://www.rfc-editor.org/

Master index: https://www.rfc-editor.org/rfc-index/

The RFC series begins in 1969 and is one of the richest continuous primary-source corpora in networking history.

### Archaeological value

Early RFCs preserve work-in-progress rather than polished standards. They reveal:

- unstable terminology;
- rejected ideas;
- host-interface assumptions;
- protocol version changes;
- operational problems;
- authorship and institutional networks;
- dates at which concepts were merely proposed vs implemented.

### Priority excavation bands

#### RFC 1–100
Focus on:
- Host–IMP interface;
- host-to-host protocol;
- NCP;
- Telnet;
- FTP;
- early mail;
- socket/connection terminology;
- documentation culture.

#### RFC 101–500
Focus on:
- mature ARPANET services;
- network measurement;
- mail and FTP evolution;
- internetworking experiments;
- protocol-number registries.

#### RFC 500–1000
Focus on:
- TCP version evolution;
- IP split;
- UDP;
- ICMP;
- TCP/IP transition;
- DNS;
- routing;
- SMTP;
- 1980s operational lessons.

### Preservation fields

For each RFC eventually record:
- RFC number;
- title;
- author(s);
- date;
- status at publication;
- later status/obsoletes/updates relationships;
- protocol family;
- implementation evidence;
- historical notes;
- canonical text URL;
- plain-text checksum if mirrored lawfully.

## 2. Internet Experiment Notes (IEN)

IENs document the experimental internetworking period before many ideas stabilized as RFCs.

Research goals:
- complete index;
- surviving scans/text;
- author/date metadata;
- mapping IEN concepts into later RFCs;
- version lineage of TCP/IP;
- gateway experiments;
- addressing/fragmentation changes.

Do not let the RFC corpus erase the IEN layer.

## 3. ARPANET Network Working Group notes and host documents

Early networking work produced notes outside the formal RFC sequence.

Targets:
- Host–IMP interface specifications;
- site installation documents;
- host-specific interface drawings;
- NCP implementation notes;
- network schedules;
- network maps;
- Network Information Center documents;
- host tables;
- operations bulletins;
- outage/measurement reports.

## 4. BBN ARPANET reports

### *A History of the ARPANET: The First Decade*
BBN Report 4799, April 1981.

Archive copy:
https://commons.wikimedia.org/wiki/File:A_History_of_the_ARPANET,_The_First_Decade,_BBN_Report_4799,_April_1981.pdf

Use it to recover:
- procurement history;
- IMP hardware evolution;
- routing and flow-control changes;
- line interfaces;
- operations;
- traffic growth;
- management organization;
- lessons learned.

### *Completion Report: ARPA Network Development*
Frank Heart, Alex McKenzie, John McQuillan, Dave Walden, 1978.

Archive copy:
https://commons.wikimedia.org/wiki/File:Arpanet_Completion_Report.pdf

Use it for engineering detail, not merely general chronology.

### Additional BBN targets

- IMP specifications;
- IMP source listings;
- Pluribus design reports;
- TIP documentation;
- Network Control Center manuals;
- annual/quarterly progress reports;
- proposals and contract documents;
- BBN technical memoranda.

## 5. NPL packet-switching archive

Institutional history:
https://www.npl.co.uk/about-us/history/timeline

Priority materials:
- Donald Davies' 1965–1966 papers/memos;
- NPL Data Communications Network reports;
- packet-switch node documentation;
- packet formats;
- routing algorithms;
- host-interface documents;
- performance measurements;
- photographs and topology maps;
- papers by Roger Scantlebury and colleagues.

Key research requirement: distinguish proposal dates from actual NPL network deployment around 1970.

## 6. RAND / Paul Baran reports

Primary target corpus: **On Distributed Communications** report series.

Preserve:
- report number;
- volume/title;
- publication date;
- diagrams;
- terminology used for message blocks;
- survivability assumptions;
- switching/routing proposals;
- later citations by ARPANET designers.

Do not convert Baran's military problem statement into the myth that ARPANET itself was simply designed as a nuclear-war-survival network.

## 7. CYCLADES / CIGALE / IRIA–Inria archive

Institutional starting points:
- https://www.inria.fr/en/louis-pouzin-et-internet
- https://www.inria.fr/en/arpanet-internet-france-some-milestones

Primary targets:
- CYCLADES architecture papers;
- CIGALE switch documentation;
- Mitra 15 documentation;
- STST transport protocol;
- host software;
- network maps;
- project reports;
- INWG documents;
- Louis Pouzin papers and correspondence;
- international demonstration records.

## 8. ALOHAnet archive

Institutional starting point:
https://www.eng.hawaii.edu/about/history/alohanet/

Primary targets:
- Norman Abramson papers;
- ALOHA protocol papers;
- original radio-terminal design;
- UHF channel details;
- terminal packet formats;
- central-station design;
- Pure ALOHA vs Slotted ALOHA documentation;
- photographs/schematics;
- operational logs if preserved.

## 9. Xerox PARC Ethernet / PUP / XNS materials

Priority targets:
- Robert Metcalfe's 1973 Ethernet memo;
- Alto Ethernet hardware documentation;
- experimental Ethernet specifications;
- PUP architecture papers;
- PUP source code;
- EFTP/network boot/printing protocols;
- DIX Ethernet specifications;
- XNS architecture manuals;
- Xerox workstation networking manuals.

Track separately:
1. experimental 2.94 Mbit/s PARC Ethernet;
2. DIX Ethernet;
3. IEEE 802.3.

## 10. IEEE 802 historical corpus

Important families:
- 802 overview and committee history;
- 802.2 LLC;
- 802.3 Ethernet;
- 802.4 Token Bus;
- 802.5 Token Ring;
- 802.1 bridging/spanning tree;
- later 802.1Q VLAN;
- 100BASE-* standardization.

Copyright caution: preserve bibliographic metadata and lawful access locations; do not mirror copyrighted standards indiscriminately.

## 11. CCITT / ITU-T standards archive

High-value recommendations:

### X-series
- X.21
- X.25 by edition;
- X.3;
- X.28;
- X.29;
- X.75;
- X.400;
- X.500.

### V-series modem/data communications
- V.21;
- V.22/V.22bis;
- V.23;
- V.26 family;
- V.27 family;
- V.29;
- V.32/V.32bis;
- V.34;
- V.42/V.42bis;
- V.90/V.92.

Record recommendation edition/year because later revisions may substantially change behavior.

## 12. Bell System / AT&T data-communications documentation

This corpus is essential for resolving modem chronology.

Targets:
- Bell System Data Set 101 manuals;
- Data Set 103 manuals;
- Data Set 201/202/208/209/212A families;
- Bell System Technical Journal papers;
- AT&T product announcements;
- tariff documents;
- private-line service descriptions;
- modem interface specifications;
- line-conditioning requirements;
- T-carrier technical papers.

Priority unresolved question:
**Bell 101 vs Bell 103 dating, product status and “first commercial modem” claims.**

## 13. SAGE / US military technical documentation

Targets:
- AN/FSQ-7 manuals;
- SAGE communications-system manuals;
- AFCRC reports;
- radar-data modem papers;
- Cape Cod System reports;
- site diagrams;
- line-speed and encoding documentation;
- operator-console manuals;
- maintenance manuals;
- contractor histories.

Possible repositories:
- US government technical archives;
- MIT Lincoln Laboratory archives;
- Computer History Museum;
- Smithsonian;
- university special collections.

## 14. IBM communications/network architecture manuals

Priority corpora:
- Bisync/BSC;
- SDLC;
- SNA architecture;
- VTAM;
- 270x/3704/3705/3725/3745 controllers;
- RSCS;
- NJE;
- APPN/APPC;
- Token Ring;
- IBM cabling system;
- SABRE-related IBM documentation.

IBM publications often have document/order numbers. Preserve those identifiers because titles are frequently reused across editions.

## 15. DEC networking manuals

Track DECnet by phase:
- Phase I;
- Phase II;
- Phase III;
- Phase IV;
- Phase IV+;
- Phase V / DECnet-Plus.

Also recover:
- DDCMP;
- NSP;
- routing;
- LAT;
- MOP;
- Ethernet interfaces;
- DECserver terminal servers;
- LANbridge products;
- VMS/RSX/TOPS networking manuals.

## 16. Novell / PC networking manuals

Targets:
- NetWare 2.x/3.x/4.x;
- IPX/SPX documentation;
- NetWare Core Protocol;
- SAP/RIP;
- NE1000/NE2000 hardware manuals;
- ODI driver documentation;
- client shells/VLMs;
- server installation manuals;
- LANalyzer/protocol-analysis tools.

## 17. AppleTalk / Macintosh networking documentation

Targets:
- *Inside AppleTalk* editions;
- LocalTalk interface/cabling manuals;
- AppleTalk Phase 1/2;
- EtherTalk;
- TokenTalk;
- AppleShare;
- Apple Internet Router;
- MacTCP;
- Open Transport.

## 18. BSD / Unix source trees

Networking source code is a primary source.

Priority versions:
- 4.1aBSD;
- 4.1bBSD;
- 4.1cBSD;
- 4.2BSD;
- 4.3BSD;
- 4.3BSD Tahoe;
- 4.3BSD Reno;
- later BSD descendants when historically necessary.

Trace:
- socket API;
- TCP state machine;
- IP forwarding;
- ARP;
- routing sockets/tables;
- congestion-control patches;
- network utilities.

## 19. UUCP / Usenet primary corpus

Targets:
- Version 7 UUCP source;
- HoneyDanBer UUCP;
- UUCP protocol documentation;
- A News;
- B News;
- C News;
- Usenet maps;
- backbone-site lists;
- old `comp.*`, `news.*` discussions about operations;
- bang-path maps;
- telephone-cost discussions;
- NNTP transition records.

## 20. FidoNet / BBS documents

Targets:
- FidoNet Technical Standards (FTS) documents;
- nodelists;
- echomail specifications;
- Fidonet Policy documents;
- BBS software manuals;
- mailer manuals;
- modem configuration guides;
- QWK packet specifications;
- preserved message bases where legally/ethically suitable.

## 21. NSFNET primary corpus

Starting points:
- https://nsf.net/
- https://www.merit.edu/research/projects/the-nsfnet-backbone-service/

Recover:
- NSF solicitations;
- Merit proposals;
- backbone technical reports;
- 56 kbit/s Fuzzball documentation;
- IBM RT Nodal Switching Subsystem reports;
- T3 RS/6000 architecture;
- network maps;
- traffic statistics;
- routing policy;
- Acceptable Use Policy;
- ANS/ANS CO+RE documents;
- NAP transition material;
- shutdown reports.

## 22. Router vendor manuals and software

### Cisco
- AGS/MGS/IGS/CGS;
- 2500/3000/4000;
- 7000/7500;
- IOS version documentation;
- interface processor manuals;
- routing-protocol implementation notes;
- product catalogs.

### Proteon
- router hardware manuals;
- routing software;
- Token Ring/Ethernet interfaces.

### Wellfleet / Bay Networks
- router architecture;
- multiprotocol software;
- WAN interface hardware.

### Others
- ACC;
- 3Com;
- BBN;
- Net/One;
- Retix;
- Xylogics;
- Cabletron;
- Livingston.

## 23. Modem / access-server primary documentation

Targets:
- Hayes manuals and command references;
- USRobotics Courier/Total Control;
- Telebit TrailBlazer;
- Racal-Vadic;
- Codex;
- Microcom;
- Multi-Tech;
- Ascend MAX;
- Livingston PortMaster;
- Cisco access servers.

Preserve:
- AT command sets;
- S-registers;
- modulation support;
- fallback;
- flow control;
- error correction/compression;
- rack/modem-pool architecture;
- PRI/T1 integration.

## 24. Advertisements, catalogs and price lists

Technical history without price history is incomplete.

Advertisements/catalogs can establish:
- announcement windows;
- product positioning;
- list price;
- claimed speed;
- supported standards;
- connector options;
- intended customer;
- contemporaneous terminology.

Marketing claims must be cross-checked, but they are valuable evidence about how products were sold.

## 25. Network maps

Maps are not illustrations only; they are topology evidence.

For each map record:
- network;
- date;
- issuing organization;
- node names;
- link speeds if shown;
- line types;
- gateways;
- legend;
- whether map depicts planned or operational topology.

Priority map series:
- ARPANET;
- NPL;
- CYCLADES;
- NSFNET;
- BITNET;
- JANET;
- NORDUnet;
- regional NSFNET networks;
- commercial ISP backbones;
- Usenet/U UCP maps.

## 26. Oral histories

Oral history can recover what specifications omit:
- why a design choice was made;
- what failed in the field;
- organizational conflict;
- undocumented hacks;
- actual operator workflow;
- product naming/version changes.

But memory is not a clock. Use oral history for context and leads, and verify exact dates/model numbers where possible.

Important oral-history repositories include:
- Computer History Museum;
- IEEE History Center / Engineering and Technology History Wiki;
- Charles Babbage Institute;
- institutional university archives;
- James Pelkey interview collection.

## 27. Source-loss prevention workflow

When a fragile source is found:

1. record title/author/date immediately;
2. record canonical URL;
3. record archive/mirror URL if lawful;
4. record report/catalog/document number;
5. record rights status;
6. if a lawful copy is held, calculate SHA-256;
7. add it to `data/source-ledger.csv`;
8. cite exact page/section in any article that uses it;
9. note if the online copy is incomplete, OCR-corrupted or missing plates.

The repository's real long-term value will be measured partly by how many historical trails remain followable after their original websites disappear.