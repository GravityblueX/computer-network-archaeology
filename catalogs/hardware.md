# Hardware Inventory

Networking history disappears fastest when it is told only as software and protocol history. This catalog treats the physical boxes, cables, interfaces and line equipment as first-class evidence.

The list below is deliberately broad. Many entries are families/classes that must later split into model- and revision-level records.

## 1. Teleprinters and terminals

### Teleprinters / hardcopy terminals
- Teletype Model 28 family
- Teletype Model 33 ASR
- Teletype Model 33 KSR
- Teletype Model 35
- IBM 2741
- GE TermiNet families
- Data General / DEC hardcopy terminal families
- printing terminals used by early time-sharing services

### CRT / “glass TTY” terminals
- DEC VT05
- DEC VT50
- DEC VT52
- DEC VT100 and descendants
- Lear Siegler ADM-3 / ADM-3A
- Hazeltine terminals
- Tektronix storage terminals
- IBM 3270 terminals/controllers
- IBM 2260 display system
- Data General terminals
- HP terminals
- Beehive terminals
- Wyse terminal families

For every terminal: keyboard encoding, line speed, duplex mode, escape/control sequences, connector/interface, local echo behavior, and modem assumptions matter.

## 2. Modems and “data sets”

### Early Bell System data sets
- SAGE-era modem/data-set equipment
- Bell 101 family — primary-source chronology needed
- Bell 103 family
- Bell 113
- Bell 201
- Bell 202
- Bell 208
- Bell 209 families
- Bell 212A

### Acoustic couplers
- early 110/300 baud acoustic couplers
- Livermore/Data Communications acoustic devices
- Anderson-Jacobson acoustic couplers
- Novation CAT
- portable acoustic couplers used with early microcomputers

### Smart/dial-up modem generations
- Hayes Smartmodem 300
- Hayes Smartmodem 1200
- Hayes 2400 and successors
- USRobotics Courier families
- Telebit TrailBlazer families
- Microcom modem families
- Racal-Vadic modems
- Codex modem families
- Milgo modem families
- Multi-Tech modem families
- Practical Peripherals
- Supra
- Zoom

### High-speed modem-bank era
- rackmount modem shelves
- ISP modem banks
- digital modem/PRI access equipment
- USRobotics Total Control
- Ascend access-server/modem products
- Livingston/PortMaster-connected modem banks

Record: modulation, symbol/bit rate, originate/answer frequency plans, duplex, leased/dial operation, error correction, compression, command language, fallback and line-quality assumptions.

## 3. Line and carrier equipment

- channel banks
- CSU/DSU devices
- DDS service units
- T1 DSUs
- E1 termination equipment
- multiplexers
- statistical multiplexers
- time-division multiplexers
- line conditioners
- echo suppressors/cancellers where relevant
- repeaters for carrier circuits
- microwave/satellite earth-station interface equipment relevant to packet links

## 4. SAGE and pre-packet communication hardware

- AN/FSQ-7 system communication peripherals
- SAGE operator consoles
- remote radar input equipment
- data transmission terminal equipment
- early digital modem hardware developed for radar-data transmission
- communications-control equipment bridging radar sites and direction centers

This category must remain careful about the difference between the overall SAGE system and a packet-switched computer network.

## 5. ARPANET switching hardware

### IMP family
- Honeywell DDP-516-based IMP
- ruggedized IMP packaging
- Honeywell 316-based IMP variants
- later IMP revisions
- Pluribus IMP
- multiprocessor IMP designs

### TIP and related access equipment
- Terminal Interface Processor (TIP)
- TIP terminal ports/interfaces
- mini-host / access variants

### Host interface hardware
- Host–IMP interface adapters for SDS Sigma systems
- PDP-10 interfaces
- IBM mainframe interfaces
- UCSB host interfaces
- Utah graphics-host interfaces
- later host front-end adapters

### Line-side hardware
- 50 kbit/s leased-line modem/data sets used between IMPs
- line interfaces for higher-speed ARPANET links
- satellite/packet-radio gateways

For each IMP generation eventually document CPU, memory, interface count, cabinet, line speeds, software image, bootstrap mechanism, diagnostic console, power and physical installation.

## 6. NPL/CYCLADES/European packet-switch hardware

- NPL packet-switching nodes — identify exact computer models/revisions
- CYCLADES CIGALE packet switches
- CII Mitra 15 used in CIGALE
- EPSS packet switches
- RCP/TRANSPAC packet-switching equipment
- Euronet packet switches
- public-data-network PADs

## 7. Commercial packet-network hardware

- Tymnet switching nodes
- Telenet packet switches
- X.25 packet switches
- PAD appliances
- concentrators
- front-end processors
- Datapac equipment
- TRANSPAC equipment
- PSS equipment
- carrier-specific network-management consoles

Vendor/model-level excavation is a major future task.

## 8. Packet radio and satellite hardware

- ALOHAnet UHF terminals
- ALOHAnet central station equipment
- PRNET packet-radio units
- Packet Radio Terminal / experimental DARPA terminals
- SATNET interface equipment
- satellite modems and earth-station interfaces
- amateur packet-radio TNCs
- TAPR TNC families

## 9. Ethernet transceivers and media

### Experimental/PARC
- experimental Ethernet interfaces for Alto systems
- Xerox PARC coax transceivers

### 10BASE5 / thick Ethernet
- thick coaxial cable
- vampire taps
- external transceivers/MAUs
- AUI cables
- N-series/BNC-type physical fittings where historically applicable
- cable markers and installation tools
- terminators

### 10BASE2 / thin Ethernet
- RG-58 coax
- BNC T-connectors
- BNC terminators
- NIC-mounted transceivers

### Twisted-pair Ethernet
- early StarLAN-related equipment
- 10BASE-T hubs
- twisted-pair MAUs
- RJ-45 structured cabling components
- Fast Ethernet hubs/switches
- autonegotiating PHYs

### Fiber Ethernet
- FOIRL
- 10BASE-F variants
- 100BASE-FX and related families

## 10. Repeaters, bridges, hubs and switches

- Ethernet repeaters
- multiport repeaters/hubs
- DEC LANbridge products
- Transparent-learning bridges
- source-route bridges
- IBM Token Ring bridges
- Kalpana EtherSwitch lineage
- early Cisco Ethernet switches
- 3Com switches
- Cabletron hubs/switches
- SynOptics hubs
- Bay Networks switching products

A future catalog should record the historical transition:

`shared coax → repeater hub → bridge → multiport bridge/switch → switched full-duplex Ethernet`.

## 11. Token Ring / Token Bus / FDDI hardware

### Token Ring
- IBM Token Ring NICs
- Multistation Access Units (MAUs/MSAUs)
- IBM Type 1 cabling components
- source-route bridge hardware
- Token Ring concentrators

### Token Bus
- industrial IEEE 802.4 hardware
- MAP-related interfaces

### FDDI
- FDDI NICs
- dual-attachment stations
- concentrators
- optical bypass hardware
- Cisco/DEC/IBM FDDI products

## 12. ARCNET and other LAN hardware

- Datapoint ARCNET controllers
- ARCNET active/passive hubs
- ARCNET coax/twisted-pair interfaces
- Cambridge Ring interfaces
- Chaosnet interfaces
- LocalTalk/PhoneNET adapters

## 13. Network interface cards

The NIC catalog should eventually be searchable by bus, chipset, media and protocol stack.

### Early workstation/minicomputer interfaces
- Xerox Alto Ethernet boards
- DEC Ethernet interfaces
- Sun Ethernet interfaces
- VAX UNIBUS/Q-bus Ethernet controllers

### PC-era NIC families
- 3Com EtherLink families
- Novell NE1000
- Novell NE2000
- Western Digital/SMC EtherCard families
- Intel EtherExpress
- AMD LANCE-based boards
- DEC Tulip-based boards
- Racal/Interlan cards
- Token Ring ISA/MCA adapters
- ARCNET ISA cards

Fields to preserve: ISA/MCA/EISA/PCI/bus type, I/O address, IRQ, DMA, boot ROM, transceiver options, connector type, chipset, driver/packet-driver support.

## 14. Front-end processors and communications controllers

Historically these were often as important as routers.

- IBM 270x communications controllers
- IBM 3704
- IBM 3705
- IBM 3725/3745 lineage
- DEC communications processors
- Univac communications front ends
- Burroughs communications processors
- Honeywell front ends
- terminal concentrators
- remote-job-entry controllers

## 15. Routers/gateways

“Router” should not be projected backward indiscriminately. This section includes devices called gateways or routers in their own eras.

### Experimental/academic gateways
- ARPANET internetwork gateways
- Fuzzball routers (DEC PDP-11 family running David Mills' software)
- Stanford/Cisco gateway ancestry
- MIT gateways
- Proteon routers

### Cisco families to excavate
- AGS / AGS+
- MGS
- IGS
- CGS
- 2500 series
- 3000/4000 families
- 7000/7500 families
- early Catalyst lineage where switching overlaps routing

### Other vendors
- Proteon
- Wellfleet
- Bay Networks
- 3Com
- ACC
- BBN routers/gateways
- IBM routers
- DEC routers
- Net/One
- Retix
- Xylogics

For every router: CPU, interfaces, supported protocols, software release, routing protocols, forwarding architecture, configuration method and management interface.

## 16. NSFNET hardware

### 56 kbit/s backbone
- DEC PDP-11 systems running Fuzzball router software
- leased 56 kbit/s circuits

### T1 backbone
- IBM RT systems used in Nodal Switching Subsystem architecture
- T1 communication subsystem equipment
- Network Operations Center systems

### T3 backbone
- IBM RS/6000-based nodes
- T3 circuits and associated carrier equipment

Sources: https://nsf.net/projects/backbone and Merit reports.

## 17. Terminal servers / access servers / PADs

- DECserver families
- Xylogics Annex
- Cisco terminal-server products
- Livingston PortMaster
- Chase Research terminal servers
- X.25 PAD appliances
- modem-pool terminal servers
- dial-in access concentrators

These devices bridge the era from “terminal to host” to “dial-up user to IP network”.

## 18. ISDN / Frame Relay / ATM era hardware

- ISDN terminal adapters
- BRI routers
- PRI access servers
- Frame Relay access devices (FRADs)
- Frame Relay-capable routers
- ATM edge switches
- ATM campus/backbone switches
- LAN Emulation hardware

## 19. Cabling, connectors and physical miscellany

This category is easy to erase from history but essential to reconstructing a real installation.

- 20 mA current-loop interfaces
- DB-25 serial cabling
- null-modem cables
- RS-232 breakout boxes
- patch panels
- punch blocks
- leased-line demarcation equipment
- AUI DB-15 connectors
- BNC Ethernet fittings
- N-style thick-Ethernet fittings where used
- RJ-45 modular cabling
- IBM Token Ring hermaphroditic connectors
- fiber ST/SC connectors in early LANs
- transceiver power arrangements
- terminators
- loopback plugs
- line-test sets

## 20. Diagnostic and network-analysis hardware

- breakout boxes
- serial-line analyzers
- protocol analyzers
- LAN analyzers
- Time Domain Reflectometers for Ethernet cable faults
- network-management terminals
- packet-monitoring interfaces
- hardware loopback devices

## 21. Surviving-hardware questions

Every major artifact should eventually include:

- museum collections known to hold it;
- private collections with public documentation;
- restoration projects;
- high-resolution photographs;
- scans of labels/serial plates;
- ROM/firmware dumps where lawful;
- schematics/manuals;
- whether an operational example survives.

## Sources anchoring early hardware work

- Computer History Museum, networking timeline: https://www.computerhistory.org/timeline/networking-the-web/
- Computer History Museum, computer timeline (SAGE/SABRE/terminals): https://www.computerhistory.org/timeline/computers/
- RFC 1, *Host Software*: https://www.rfc-editor.org/info/rfc1/
- BBN, *A History of the ARPANET: The First Decade*, Report 4799 (1981)
- *Completion Report: ARPA Network Development* (1978)
- NPL history: https://www.npl.co.uk/about-us/history/timeline
- Inria CYCLADES histories: https://www.inria.fr/en/louis-pouzin-et-internet
- NSFNET backbone project: https://nsf.net/projects/backbone
- James Pelkey, *History of Computer Communications*: https://historyofcomputercommunications.info/

## Rule for future additions

A box does not become historically unimportant merely because its function later moved onto a motherboard, ASIC, operating system, or cloud service. If an old network needed a separate physical object to make something happen, preserve that object in the history.