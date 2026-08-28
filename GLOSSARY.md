# Historical Networking Glossary

Networking vocabulary is archaeological evidence. The same word can change meaning across decades, and different communities often used different words for nearly the same function.

This glossary is therefore **historical**, not merely definitional. It records how terms were used and warns against silently replacing period language with modern language.

## acoustic coupler

A modem arrangement in which the telephone handset is physically placed into cups containing acoustic transducers. It avoids a direct electrical connection to the telephone network. Common in portable and early dial-up computing, especially when telephone-company rules or practical access made direct connection difficult.

Do not use *acoustic coupler* as a synonym for every early modem.

## AUI — Attachment Unit Interface

The cable/interface between Ethernet station equipment and a separate Medium Attachment Unit (MAU/transceiver) in classic 10 Mbit/s Ethernet. Particularly visible in 10BASE5 installations, where the transceiver could be mounted on the thick coax and connected to a host/NIC through an AUI cable.

## backbone

A higher-capacity or structurally central network carrying traffic among other networks. The meaning is organizational as much as physical: ARPANET, NSFNET and commercial provider backbones represent very different architectures and institutions.

## bang path

A source-route-like UUCP addressing notation using exclamation marks between host names, e.g. `siteA!siteB!user`. The path could reflect scheduled dial-up relationships and telephone economics, not continuously available packet links.

## baud

Symbol changes per second, not automatically bits per second. For simple one-bit-per-symbol modulation they may be numerically equal; for higher-order modulation they are not. Historical sources often use *baud* colloquially where modern writers might say bit/s, so preserve the source wording and explain it.

## BBS — Bulletin Board System

A host users commonly reached by dialing a modem directly. BBS systems could be standalone or participate in store-and-forward networks such as FidoNet. Do not equate a BBS with an Internet host merely because later BBS systems gained Internet gateways.

## bridge

A device forwarding frames between link-layer segments, typically learning MAC addresses in Ethernet contexts. A bridge normally does not create an IP routing boundary. In the 1980s, bridges and routers solved different scaling/administrative problems and often coexisted.

## carrier

Ambiguous. It may mean a telecommunications operator, a modulated carrier signal, or the physical indication that a modem has detected carrier. Always infer meaning from context.

## circuit switching

A communications model in which an end-to-end circuit/path is established for a session, historically exemplified by telephone service. Packet switching was developed partly to avoid dedicating network capacity in the same way, but real packet networks often still ran over leased or switched telecommunications circuits underneath.

## collision domain

A region of shared Ethernet in which simultaneous transmissions can collide. Repeater hubs extend a collision domain; switches/bridges separate them. The term becomes especially useful when explaining why 10BASE-T star wiring with hubs was still logically a shared-medium Ethernet.

## CSU — Channel Service Unit

Customer-side equipment associated with terminating and conditioning a digital carrier circuit, especially DDS/T1-era services in North America. Often combined with a DSU in one box and colloquially called a CSU/DSU.

## data set

Bell System and telecommunications-era term for equipment interfacing data-terminal equipment to a communications circuit. Many devices later called modems appeared in Bell documentation as **Data Sets**. Preserve the period name, model suffix and service context.

## datagram

A self-contained packet forwarded independently without requiring a pre-established end-to-end virtual circuit. CYCLADES made datagram service a central architectural choice; IP later made it foundational to the Internet layer.

The word does not imply guaranteed delivery, order or duplicate suppression.

## DCE — Data Circuit-terminating Equipment / Data Communications Equipment

The network/communications-side equipment at a standardized DTE/DCE boundary. Exact expansion varies by standard and period. In X.25, the network-facing side of the subscriber interface is DCE.

## DDP-516 / Honeywell 516

A 16-bit minicomputer family member historically important because machines in the Honeywell Series 16 lineage were used as packet-switch platforms in early networking, including BBN IMPs and NPL work. Do not infer identical hardware configurations merely from the processor family.

## DSU — Data Service Unit

Equipment adapting customer digital data equipment to a digital telecommunications service. Commonly paired with a CSU. Exact functions differ by service and vendor generation.

## DTE — Data Terminal Equipment

User/customer-side equipment at a communications interface: a terminal, host or other end system depending on context. In X.25, DTE is the subscriber equipment using the packet service.

## Ethernet

A family whose meaning changes by date. At minimum distinguish:

- Metcalfe's 1973 Ethernet concept;
- Xerox PARC experimental ~2.94 Mbit/s Ethernet;
- 10 Mbit/s DIX Ethernet;
- IEEE 802.3 families such as 10BASE5/2/T;
- later switched/full-duplex Ethernet.

Writing “Ethernet” without a revision/physical layer can hide major engineering differences.

## FEP — Front-End Processor

A computer or communications processor placed between a host and communications lines/terminals to offload protocol, polling, buffering or line handling. IBM and other vendors used front-end processors extensively before small routers/terminal servers became ubiquitous.

## frame

A link-layer transmission unit. Historical sources may use *block*, *message*, *packet* or other terms for units that later writers would classify differently. Do not overwrite the source vocabulary without an explicit mapping.

## Fuzzball

David L. Mills' compact networking software environment for PDP-11/LSI-11-class machines. Fuzzballs were used in Internet research and the original 56 kbit/s NSFNET backbone. It is more accurate to think of Fuzzball as a network-oriented operating/software system that could make a minicomputer serve as a router, not merely as a router model name.

## gateway

One of the most dangerous historical terms.

In early Internet documents, **gateway** commonly means what later terminology calls an **IP router**: a machine forwarding Internet datagrams between networks. By the 1990s, *router* became the normal forwarding term while *gateway* increasingly implied translation or an application/protocol boundary.

Always preserve the period term and annotate its functional equivalent.

## host

An end-system computer attached to a network. ARPANET literature distinguishes Hosts from IMPs. Internet architecture later formalized end systems versus routers. In older vendor literature, *host* can also mean a centralized mainframe accessed by terminals; context matters.

## hub

Usually a multiport repeater in classic 10BASE-T Ethernet. A hub creates a convenient physical star while retaining one shared logical collision domain. Later consumer terminology sometimes called switching devices hubs, so identify the internal function.

## IMP — Interface Message Processor

The BBN packet switch used in ARPANET. Early IMPs were based on Honeywell DDP-516 hardware with custom interfaces and BBN software. The IMP separated packet-network operation from heterogeneous host computers.

Calling an IMP simply “a router” is useful only as a rough analogy; it hides ARPANET's host/IMP protocol, internal network semantics and historical terminology.

## internetwork / internet

Historically, an **internetwork** is a network of networks. Lowercase *internet* was used generically before *the Internet* became the proper name for the global TCP/IP system. Preserve capitalization from documents when historically meaningful.

## leased line / private line

A communications circuit provided for continuous or contracted use between customer points instead of being established as an ordinary dial call each time. Early packet networks frequently used leased telephone-company circuits underneath packet switching.

“Packet switched” therefore does not imply that the physical carrier path itself was packet switched.

## link

A connection between neighboring network entities. The physical realization could be a local cable, leased telephone circuit, radio hop, satellite channel or something else. ARPANET's *link* terminology can also refer to logical host-to-host mechanisms, so use period-specific definitions.

## MAU — Medium Attachment Unit

Classic Ethernet transceiver attached to the medium, especially visible in 10BASE5. Not to be confused with IBM Token Ring's **Multistation Access Unit**, which uses the same acronym but is an entirely different device/function.

## message switching

Store-and-forward communication where complete messages are forwarded between intermediate nodes. Packet switching divides communications into smaller units and was partly motivated by delay, buffering and utilization concerns in message-switching designs.

## modem

Modulator/demodulator: equipment translating digital data into signals appropriate to a communications channel and back again. Historical modem categories differ greatly: private-line vs dial-up, FSK vs phase/amplitude modulation, synchronous vs asynchronous, acoustic vs direct-connect.

Never write a modem speed without attaching it to a standard/model and distinguishing baud from bit/s when relevant.

## NCP — Network Control Program

In ARPANET history, NCP refers to the pre-TCP host-to-host protocol/software environment. The acronym is dangerously overloaded: IBM and Novell also used NCP for unrelated networking concepts. Always qualify it.

## network operating system

May mean a dedicated OS for shared network services (e.g. NetWare), an OS running in network equipment, or more broadly an operating system with networking support. Historical vendor usage varies; avoid treating it as one universal category.

## NIC — Network Interface Card / Controller

Host adapter connecting a computer bus/system to a network. Older literature may say interface controller, adapter, Ethernet controller, network adapter, etc. Exact bus, chipset, transceiver arrangement, drivers, IRQ/DMA/I/O configuration can be essential archaeological details.

## node

Generic and potentially ambiguous. A node may be a packet switch, host, router, terminal concentrator or site depending on the network. Avoid converting every historic “node” into “router.”

## PAD — Packet Assembler/Disassembler

Device/function connecting asynchronous character terminals to an X.25 packet-mode environment. The classic CCITT Triple-X family is:

- X.3 — PAD parameters/functions;
- X.28 — terminal ↔ PAD interaction;
- X.29 — PAD ↔ packet-mode DTE/PAD control.

The PAD is a key lost box of public packet-network history.

## packet

A bounded unit carried by a packet-switched network. Packet format, maximum size and whether the packet is visible to hosts vary by network.

ARPANET's IMP packets, NPL packets, CYCLADES datagrams, X.25 packets and IP datagrams are **not interchangeable historical objects** merely because modern writers call all of them packets.

## packet switch

A node whose core function is receiving, buffering and forwarding packets within a packet network. IMPs, CIGALE nodes and many X.25 network switches fit this broad archaeological category, although their architectures differ substantially.

## packet switching

A family of communication techniques dividing data into bounded units that share network resources and are forwarded among nodes. It is not one protocol and has never implied one uniform architecture: datagram and virtual-circuit networks are both packet switched.

## protocol

Rules governing communication among peers. Networking history shows the term itself becoming more common during the 1960s. Earlier documents may say *procedure*, *convention* or *discipline* for essentially protocol-like rules.

## PTT

Postal, Telegraph and Telephone administration or analogous national telecommunications authority. In much of twentieth-century Europe, PTT institutions shaped standards, tariffs, modem attachment, leased circuits and public data networks. They are part of the technical history, not background scenery.

## repeater

Physical-layer device regenerating/repeating signals to extend a segment. Ethernet repeaters do not learn MAC addresses and do not isolate collision domains.

## RFNM — Request for Next Message

ARPANET IMP-to-host flow-control signal indicating that the network was ready for another message on a logical link after processing the prior message. This is specific to ARPANET's early host/IMP architecture and should not be casually mapped onto TCP acknowledgments.

## router

Network-layer forwarding device selecting a next hop for packets/datagrams between networks. The word gradually replaced early Internet use of *gateway* for this function.

A router is not automatically a dedicated appliance: PDP-11 Fuzzballs, UNIX hosts and other general-purpose computers have historically routed packets.

## RS-232 / EIA-232

A family of serial interface standards defining electrical and control-signal conventions between DTE and DCE. Historical revisions matter. Equipment may implement only subsets or use nonstandard connectors even while claiming compatibility.

Do not reduce RS-232 to “the DB-25 connector.” Connector shape and electrical/procedural standard are separate issues.

## store-and-forward

An intermediary receives and stores data before forwarding it. The storage may be milliseconds in packet-switch memory or hours on disk in a UUCP spool. The phrase spans radically different delay and persistence regimes.

## switch

Historically overloaded. Telephone switch, packet switch, LAN switch and switching system are different objects. Ethernet *switch* became common for multiport bridging devices in the 1990s, but earlier equivalent functions might be sold as bridges.

## T1

North American digital carrier hierarchy service at **1.544 Mbit/s**, commonly divided into DS0 channels. T1 is a carrier/transmission service and framing family, not itself an Internet protocol. NSFNET's 1988 T1 backbone rode IP routing infrastructure over carrier circuits supplied in part by MCI.

## terminal

Human-facing input/output device connected to a computer directly or through communications facilities. Important types include teletypes, Selectric-derived terminals, CRT “glass terminals” and later PC terminal emulators.

Terminal line speed, character encoding, current loop vs RS-232, local echo and flow control are often crucial to understanding early networks.

## terminal server

Device connecting multiple serial terminals/modems to hosts or packet/IP networks. Terminal servers can look superficially like routers because they connect many ports to a network, but their primary archaeological role is session/terminal access.

## TIP — Terminal Interface Processor

ARPANET device derived from the IMP concept that provided direct terminal access to the network without requiring each terminal to attach through a conventional host. Preserve exact TIP hardware and port-interface revisions.

## transceiver

Transmitter/receiver unit at a physical medium boundary. In Ethernet history this often refers to a separate MAU attached to coax. In radio history it may mean an RF unit. Specify medium and interface.

## virtual circuit

A logical connection established across a packet network so packets can be associated with persistent per-connection state. X.25 virtual calls and permanent virtual circuits are classic examples.

A virtual circuit is **not** the same thing as a physically dedicated circuit.

## vampire tap

Informal name for the 10BASE5 attachment mechanism that penetrates the outer insulation/shield of thick coax to contact the conductor without cutting the entire cable. Usually associated with a separate Ethernet transceiver and AUI cable.

## V.24 / V.28 / V.35

CCITT interface recommendations frequently encountered in historical data communications. V.24 concerns interchange circuits/functions; electrical characteristics can be specified separately (e.g. V.28). V.35 belongs to a different high-speed interface tradition. Historical equipment documentation must be read carefully rather than translating all of them into “serial port.”

## X.25

CCITT recommendation family defining the DTE/DCE interface for packet-mode operation on public data networks. The first major edition dates to 1976, with later revisions changing details.

X.25 is not synonymous with every internal protocol used by every packet-switched public data network.

## 1822 interface

Host/IMP and IMP-related interface lineage associated with ARPANET, named after BBN Report 1822. It includes electrical/logical conventions for attaching hosts and later equipment to IMPs. Exact editions and hardware interfaces must be dated.

---

## Editorial rule for future glossary additions

A glossary entry should answer at least one of these:

1. Did the word mean something different in the period?
2. Is the modern simplification likely to mislead?
3. Does the acronym collide with another historical networking term?
4. Does understanding the term reveal a physical box, interface, service or operational practice that modern diagrams tend to erase?

If yes, it belongs here.