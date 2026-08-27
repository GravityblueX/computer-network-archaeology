# Networking Software Inventory

Networking did not become real when a protocol was written down; it became real when someone made an operating system, switch, gateway, terminal or application implement it. This catalog tracks that implementation layer.

Executable reconstruction belongs mainly in [tmzncty/protocol-zoo](https://github.com/tmzncty/protocol-zoo); this repository records historical implementations, releases, source trees and deployment evidence.

## ARPANET switching-node software

- original BBN IMP software for Honeywell DDP-516
- Honeywell 316 IMP software revisions
- IMP routing software revisions
- IMP diagnostic/monitoring code
- Pluribus IMP software
- TIP software
- Network Measurement Center tools
- Network Control Center operations software

Research questions:

- language/assembler used;
- memory footprint;
- routing-update mechanism;
- boot/loading method;
- configuration tables;
- diagnostics;
- version chronology;
- surviving source listings or dumps.

## Early ARPANET host software

The first hosts did not share one operating system, so “ARPANET software” means multiple independently developed host implementations.

Research leads:

- UCLA SDS Sigma 7 Host–IMP software
- SRI SDS 940 network software
- UCSB IBM 360/75 network software
- University of Utah PDP-10 networking
- BBN TENEX network software
- Multics networking
- MIT ITS networking
- TOPS-10/TOPS-20 networking
- Network Control Program implementations by host OS
- Initial Connection Protocol implementations
- early Telnet clients/servers
- early FTP implementations
- early mail programs

## NPL / CYCLADES / European packet networking software

- NPL packet-switch software
- NPL host protocols
- CYCLADES/CIGALE switch software on Mitra 15
- STST implementations
- CYCLADES host software
- EPSS software
- RCP/TRANSPAC switching software
- public X.25 switch software
- PAD software

## Packet radio / satellite implementations

- ALOHAnet central-station software
- ALOHAnet terminal software
- PRNET packet-radio software
- SATNET gateway software
- internetwork gateway software used in multi-network TCP experiments

## Ethernet / PARC software

- Alto Ethernet drivers
- PUP implementations
- PUP routing/gateway software
- EFTP and other PUP applications
- XNS software
- Xerox workstation/printer networking
- early Ethernet diagnostics and boot protocols

## BSD and Unix TCP/IP lineage

This area must be versioned carefully.

- early TCP implementations at BBN and Stanford
- BBN TCP/IP implementations for multiple systems
- Berkeley networking before 4.2BSD
- 4.1a/4.1b/4.1cBSD networking research releases
- 4.2BSD TCP/IP stack
- 4.3BSD networking
- 4.3BSD Tahoe
- 4.3BSD Reno
- socket API evolution
- `ifconfig`
- `route`
- `netstat`
- `arp`
- `rlogin`, `rsh`, `rcp`, `rexec`
- `ftp`, `telnet`
- `sendmail`
- `named`
- `routed`
- `gated`
- `inetd`

## TCP/IP implementations outside BSD

- TOPS-20 TCP/IP
- VMS TCP/IP packages
- DEC TCP/IP products
- IBM mainframe TCP/IP
- VM/CMS TCP/IP
- MVS TCP/IP
- Multics TCP/IP
- NOS/CDC implementations
- UNIX System V networking packages
- SunOS networking
- HP-UX networking
- AIX networking
- Ultrix networking
- IRIX networking
- Apollo Domain networking
- early Macintosh TCP/IP stacks (e.g. MacTCP)
- DOS TCP/IP stacks
- Windows TCP/IP add-ons and later built-in stacks

## PC TCP/IP stacks and drivers

- FTP Software PC/TCP
- Sun PC-NFS
- NCSA Telnet
- KA9Q NOS
- Trumpet Winsock
- Microsoft TCP/IP stacks
- Novell LAN Workplace
- Wollongong TCP/IP products
- Beame & Whiteside stacks
- packet driver specification ecosystem
- ODI drivers
- NDIS drivers

## Network interface driver history

Record the driver model separately from individual NICs:

- vendor-specific DOS drivers
- Clarkson packet drivers
- Novell ODI
- Microsoft/3Com NDIS
- BSD network-device drivers
- STREAMS networking drivers
- Linux early NIC drivers
- boot ROM/PXE predecessors

## Unix-to-Unix networking

- UUCP
- `uucico`
- `uux`
- `uuxqt`
- HDB UUCP
- UUCP protocol variants
- sendmail over UUCP
- UUCP map-processing tools

## Usenet software

- A News
- B News
- C News
- `rnews`
- `inews`
- early newsreaders
- `rn`
- `trn`
- `nn`
- NNTP server implementations
- INN

Track the shift from UUCP propagation to NNTP/IP separately.

## BITNET / NJE software

- IBM RSCS
- VM/CMS networking components
- NJE implementations for non-IBM hosts
- LISTSERV
- BITNET gateways
- EARN software

## CSNET software

- PhoneNet software
- MMDF
- CSNET name server / directory software
- TCP/IP-over-X.25 implementations
- mail-relay software

## DNS implementation history

- early name-server prototypes
- BIND ancestry
- BIND 4
- BIND 4.8/4.9 lineage
- resolver libraries
- host-table conversion tools
- NIC host-table distribution software

## Routing software

- IMP routing software
- gateway algorithms in early Internet experiments
- Fuzzball router software by David Mills
- `routed`
- `gated`
- Cornell/NSFNET routing software
- Cisco IOS ancestors and releases
- Proteon routing software
- Wellfleet router software
- BGP implementations
- OSPF implementations
- EGP implementations

## NSFNET software

- Fuzzball routing software on PDP-11
- IBM RT Nodal Switching Subsystem software
- RS/6000 T3 node software
- NSFNET management/monitoring software
- routing-policy tools
- statistics/traffic-measurement tools

## IBM networking software

- VTAM
- NCP (IBM Network Control Program — distinguish from ARPANET NCP)
- ACF/NCP
- RSCS
- APPN software
- SNA gateways
- Communications Server products

## DEC networking software

- DECnet implementations by phase
- RSX DECnet
- VMS DECnet
- TOPS DECnet
- Ultrix DECnet
- LAT software
- MOP tools
- DECnet routing software

## Xerox networking software

- PUP stack
- XNS stack
- Xerox Network Systems services
- Clearinghouse
- Courier
- network boot/software-distribution components

## Novell NetWare software

- early NetWare releases
- NetWare 2.x
- NetWare 3.x
- NetWare 4.x
- IPX/SPX stack
- NetWare Core Protocol implementations
- SAP/RIP services
- client shells
- VLM client software
- ODI driver stack
- IPX gateways

## Apple networking software

- AppleTalk Phase 1/2 stacks
- AppleShare
- LocalTalk drivers
- EtherTalk
- MacTCP
- Open Transport
- Apple Internet Router

## Banyan / LAN Manager / peer LAN software

- Banyan VINES OS/network services
- StreetTalk
- Microsoft LAN Manager
- IBM LAN Server
- 3Com 3+Share
- TOPS networking software
- early SMB clients/servers
- NetBIOS implementations

## Online-service client software

- CompuServe terminal/client programs
- The Source terminal software
- GEnie access clients
- AOL/Quantum Link clients
- Prodigy client software
- Minitel terminal firmware/software
- Prestel clients

Client software belongs because proprietary networks often exposed their architecture only through these programs.

## BBS software

- CBBS
- RBBS-PC
- WWIV
- Fido BBS
- Opus
- BinkleyTerm
- FrontDoor
- Maximus
- PCBoard
- Wildcat!
- MajorBBS
- Synchronet
- QWK mail readers

## FidoNet software and formats

- Fido
- mailers
- nodelist-processing tools
- FTS specification implementations
- echomail processors
- tossers/scanners

## Terminal emulation / communications software

- Kermit implementations
- XMODEM/YMODEM/ZMODEM programs
- Crosstalk
- ProComm
- Telix
- Qmodem
- Minicom (later Unix lineage)
- terminal software bundled with modem vendors

## File-transfer protocols/software outside FTP

- Kermit
- XMODEM
- YMODEM
- ZMODEM
- UUCP file transfer
- MODEM7 and predecessors
- proprietary online-service file-transfer protocols

## Network operating systems and management

- Cisco IOS lineage
- Wellfleet/Bay Networks software
- 3Com networking software
- Cabletron management software
- HP OpenView
- SunNet Manager
- IBM NetView
- DECnet management tools
- SNMP managers/agents
- CMIP managers

## Early Internet information-service software

- Archie server/client
- Gopher server/client
- WAIS
- Veronica
- Jughead
- IRC daemons/clients
- anonymous FTP servers
- WAIS gateways
- early HTTP servers
- CERN httpd
- NCSA HTTPd
- Mosaic

## Network security software/history leads

Only include where it intersects historical networking architecture:

- password/authentication handling in remote login
- Kerberos
- TCP wrappers
- firewall/router ACL software
- packet filters
- TIS Firewall Toolkit
- SOCKS
- early VPN/tunneling software
- SSL/TLS implementations

## Source preservation goals

For every software family, seek:

- release tapes/images;
- source trees;
- binaries;
- build instructions;
- manuals;
- release notes;
- bug reports;
- protocol conformance notes;
- mailing-list archives;
- screenshots/console transcripts;
- known emulation projects;
- checksums;
- licensing status.

## Important naming collisions

- ARPANET **NCP** and IBM **NCP** are unrelated major historical systems.
- NetWare **NCP** is another unrelated use.
- `routed` and “router daemon” should not be confused with a general router operating system.
- “TCP/IP stack” may refer to kernel code, a user-space package, or an integrated vendor product; record which.

## Archaeological rule

A paper specification tells us what designers intended. Source code and binaries tell us what machines could actually do. Deployment records and operator reports tell us what users really experienced. Preserve all three layers.