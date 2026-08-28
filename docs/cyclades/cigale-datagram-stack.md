# CYCLADES / CIGALE: datagrams, Mitra 15s, leased lines, and host responsibility

CYCLADES is often reduced to the claim that it “influenced TCP/IP.” That is true but insufficient. The engineering object was a real French heterogeneous-computer network whose packet-switching subnetwork, **CIGALE**, deliberately behaved differently from ARPANET in several important respects.

This note reconstructs the stack as closely as surviving published descriptions currently allow.

## Project frame

The French IRIA launched CYCLADES in 1972 under Louis Pouzin. The goal was not simply to build another packet network; it was to provide an experimental heterogeneous network linking university, research and data-processing computers while keeping operating-system modification manageable.

The architecture separated:

```text
host-to-host protocols and applications
              ↓
       CYCLADES host layer
              ↓
     CIGALE packet service
              ↓
      leased data circuits
              ↓
     CIGALE packet service
              ↓
       remote CYCLADES host
```

The CIGALE subnetwork was intentionally a comparatively transparent packet carrier. End-to-end correctness belonged primarily above it.

## CIGALE node hardware

Louis Pouzin's 1974 CIGALE description gives unusually concrete hardware details:

- packet nodes were **CII Mitra 15** minicomputers;
- a node had **16 K words of 16-bit memory** in the described configuration;
- beyond a teletype, the switch did not require a conventional mass-storage peripheral set for basic packet-switch operation;
- the same Mitra 15 family was also used for terminal concentrator functions.

The choice matters historically. France's national computing policy, CII hardware, PTT participation, and network architecture were physically intertwined. CYCLADES was not a placeless protocol experiment.

## Lines and interfaces

Pouzin's CIGALE paper describes point-to-point PTT leased lines between packet nodes at approximately **4.8 to 48 kbit/s**.

Hosts were generally connected to a CIGALE node over telephone/data circuits. Published descriptions mention:

- **CCITT V.24** electrical interfaces up to roughly 19.2 kbit/s;
- **V.35** at higher rates in later survey material;
- commonly about **19.2 kbit/s baseband modulation** over voice-grade circuits in the 1974 CIGALE description;
- transparent binary-synchronous transmission procedures supplied by host vendors.

This produced an important practical compromise: CYCLADES could attach heterogeneous vendor systems without requiring every machine to replace its existing low-level communications machinery.

## Host population

The 1973 design paper listed a deliberately heterogeneous collection, including systems from CII, IBM, CDC and Philips. A contemporary list included:

- CII 10070;
- CII IRIS 80;
- CII IRIS 50;
- IBM System/360-class equipment;
- CDC 6600;
- Philips systems;
- Mitra 15 communications computers.

Exact inventories changed as the project evolved, so inventories should always be dated.

## Datagram as an architectural decision

The word **datagram** is central here.

CIGALE treated packets independently. Pouzin compared their handling to letters in the mail. The packet subnetwork did not promise that messages would arrive in sequence, and the design avoided embedding end-to-end transport semantics in the packet switches.

This creates a clean division:

### CIGALE should do

- packet forwarding;
- routing;
- queueing;
- local transmission/error handling;
- congestion-related control;
- measurements, tracing and operational support.

### Hosts / higher layers should do

- end-to-end reliability where required;
- ordering where required;
- flow control between communicating processes;
- application semantics;
- recovery from packet loss/duplication/reordering.

That is one of CYCLADES' most important conceptual contributions to later internetworking.

## Addressing was not supposed to mirror topology forever

Pouzin's CIGALE description distinguishes host address space from physical topology. It also describes larger concepts such as regions and network names for inter-network traffic.

This is historically significant because a network that expects other networks to exist must avoid confusing:

> “where a host is physically plugged in”

with

> “what object the packet is intended for.”

The later Internet would wrestle with the same distinction repeatedly through network numbers, subnetting, CIDR, mobility and multihoming.

## Multihoming was not an afterthought

CIGALE allowed hosts to attach through multiple lines. Packets could travel independently, making multiple paths conceptually natural rather than anomalous.

That feature connects directly to the end-to-end argument implicit in the architecture: if the network may choose different paths, the host cannot rely on the network delivering an ordered byte stream merely because packets entered in order.

## Software organization inside a packet switch

Pouzin described switching as asynchronous processes communicating through queues.

The node software also included operational functions beyond forwarding:

- echo/testing;
- statistics collection;
- debugging facilities;
- node configuration;
- artificial traffic generation;
- clock/time functions;
- optional per-packet priority;
- tracing;
- routing controls.

A central control facility received reports and helped locate failing components. Nodes could be **remotely reloaded** by sending their program through the network in packets.

That last detail is worth preserving because it makes the CIGALE node look recognizably like later remotely administered network infrastructure rather than a one-off laboratory switch.

## Development chronology

A 1975 project-status paper gives a useful operational sequence:

- **1972:** general design, planning, staffing and participation work;
- **1973:** a small demonstration network with three homogeneous hosts and one packet switch, offering operator communication, file transfer and remote job entry;
- **February 1974:** demonstration with four hosts and three packet nodes;
- during 1974: CIGALE became routinely operational for test periods while heterogeneous host software was brought up;
- by 1974–1975: the network supported remote login/time-sharing, remote batch and file transfer, with continuing expansion and interconnection experiments.

The project should therefore not be assigned one magical “birth date.” Design, first packet node, public demonstration, regular service and heterogeneous-network operation are different milestones.

## NPL ↔ CYCLADES interconnection

One particularly valuable archaeological seam is the direct NPL–CYCLADES link.

A 1974 *Computer Weekly* report preserved by The National Museum of Computing describes a test link between an NPL CTL Modular One and a CYCLADES Mitra 15 using **Codex modems** and a **9,600-baud line**. At the lowest level, IBM binary synchronous line control was being used, with packet formats carried above it.

This is exactly the sort of detail that disappears from architectural histories.

An “internetwork” was not an abstract cloud. It was:

```text
NPL host
  ↓
interface / local NPL network
  ↓
Codex modem
  ↓
9,600-baud telephone circuit
  ↓
Codex modem
  ↓
Mitra 15 / CIGALE
  ↓
CYCLADES host protocols
```

This interconnection deserves its own future article.

## CYCLADES and the 1974 TCP paper

Vint Cerf and Bob Kahn's internetworking work developed in an international conversation that included ARPANET, NPL and CYCLADES. Early Internet documents explicitly cited Pouzin's 1973 CYCLADES paper.

The careful claim is not “CYCLADES invented TCP/IP.” The stronger and more historically useful claim is:

- CYCLADES made a deliberately connectionless packet subnetwork concrete;
- it emphasized end-system responsibility;
- it explored naming/addressing for heterogeneous and interconnected networks;
- its designers participated directly in INWG discussions;
- these ideas were visible to and cited by the people designing early TCP.

## CIGALE vs X.25 as an architectural fork

Later public packet networks commonly exposed virtual-circuit services associated with X.25. CYCLADES instead treated independent datagrams as a fundamental design tool.

That contrast should not be turned into “good Internet design vs bad telecom design.” The systems optimized for different institutional and operational requirements.

A future comparison should ask:

- who was expected to provide reliability?
- who controlled addressing?
- who paid while a virtual circuit remained open?
- how did failure affect existing conversations?
- how much per-flow state lived in the network?
- how were terminals, not just computers, supported?
- what operational guarantees did a public PTT need to sell?

## Sources

1. Louis Pouzin, **“Presentation and Major Design Aspects of the CYCLADES Computer Network”** (1973). Surviving scan: <https://walden-family.com/am254/vol1-9e-pouzin-cyclades.pdf>
2. Louis Pouzin, **“CIGALE, The Packet Switching Machine of the CYCLADES Computer Network”** (IFIP 1974), transcribed copy: <https://rogerdmoore.info/PS/CIGALE/CIGALE.html>
3. Louis Pouzin, **“The CYCLADES Network — Present State and Development Trends”** (1975), transcribed copy: <https://www.rogerdmoore.info/PS/CIGALE/CYCL2.html>
4. Inria, **From the Arpanet to Internet in France: some milestones**: <https://www.inria.fr/en/arpanet-internet-france-some-milestones>
5. Inria, **Between Stanford and Cyclades, a transatlantic perspective on the creation of Internet**: <https://www.inria.fr/en/between-stanford-and-cyclades-transatlantic-vision-creation-internet>
6. The National Museum of Computing, 1974 *Computer Weekly* excerpt on the NPL–IRIA link: <https://www.tnmoc.org/notes-from-the-museum/2023/10/04/fifty-years-ago-from-the-pages-of-computer-weekly-c72lb-xdn8p-fdjlr-ahz981-lw8bw-8x5kr-l5eja-6kpe7-7tt86-9yej8-csrke-9e4zz>
7. RFC 635, which cites the 1973 CYCLADES paper: <https://www.rfc-editor.org/rfc/rfc635.html>
8. RFC 675, early Internet TCP specification and bibliography: <https://www.rfc-editor.org/rfc/rfc675.html>

## Unresolved excavation tasks

- obtain an original scan and page images of the 1974 CIGALE paper from a stable archive;
- recover exact Mitra 15 hardware revision(s), memory cycle, interface boards and line controllers used in each CIGALE node;
- identify modem models used on ordinary CIGALE leased links;
- reconstruct packet header bit layout;
- reconstruct routing table format and routing-update algorithm;
- recover queue limits and congestion-control mechanisms;
- recover node boot/reload packet protocol;
- recover operations-center console procedures;
- inventory all hosts by date and host-interface type;
- reconstruct terminal concentrator hardware/software;
- document STST and other CYCLADES transport/host protocols separately;
- reconstruct the NPL–CYCLADES interconnection from both sides;
- locate surviving Mitra 15 hardware and determine whether any unit can be tied to CYCLADES provenance.

CYCLADES should ultimately be documented not as an influence arrow pointing at TCP/IP, but as a working stack made of French computers, PTT lines, modems, queues, packets, host software and operational compromises.