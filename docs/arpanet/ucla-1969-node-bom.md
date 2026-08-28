# UCLA, September 1969: reconstructing the first ARPANET node as installed infrastructure

> Status: active excavation. This file deliberately separates **confirmed**, **probable**, and **still unresolved** components. It is not enough to say that “the first ARPANET node was at UCLA.” The archaeological question is: **what equipment was actually in the room, how was it interconnected, what software ran on each machine, which organizations owned each layer, and what changed between delivery, local host/IMP operation, and the first UCLA–SRI traffic?**

## 1. Why this node deserves a bill of materials

Popular histories compress the event into one sentence:

> UCLA connected an SDS Sigma 7 to an Interface Message Processor in 1969.

That is historically true but technically impoverished. The September–October 1969 UCLA installation was a stack assembled across organizational boundaries:

```text
UCLA user / measurement software
        ↓
SDS Sigma 7 host
        ↓
UCLA-built Host–IMP hardware interface
        ↓
1822-style bit-serial Host–IMP boundary
        ↓
BBN IMP No. 1
  modified Honeywell DDP-516
        ↓
BBN synchronous line interface
        ↓
Bell 303-class wideband data set / modem path  [model/date needs primary confirmation]
        ↓
AT&T Long Lines / local telco facilities
        ↓
50 kbit/s inter-IMP circuit to SRI
        ↓
SRI IMP
        ↓
SRI host interface
        ↓
SDS 940 host
```

Every box and arrow in that drawing has its own engineering history.

## 2. Timeline: delivery is not the same event as networking

### 30 August 1969 — IMP delivery

Steve Crocker later recalled that the first IMP, expected around Labor Day, was air-shipped by BBN and reached UCLA's loading dock on Saturday, **30 August 1969**. The machine was based on a Honeywell 516. BBN personnel then installed and shook down the packet switch.

Leonard Kleinrock's retrospective gives the same weekend chronology and identifies a much broader installation scene: UCLA, BBN, Honeywell, Scientific Data Systems, AT&T Long Lines, GTE, ARPA, campus personnel, and graduate students were all implicated in making the system work.

### 2 September 1969 — local bits and messages between Sigma 7 and IMP

Kleinrock's account places the successful local Host–IMP bring-up on the Tuesday after Labor Day. Bits moved between the UCLA host and the IMP; by the following day messages were moving between the two local machines.

This is a distinct milestone from host-to-host networking. At this point the UCLA machine had acquired a functioning boundary to its packet switch, but the famous UCLA–SRI login had not yet occurred.

### early October 1969 — second IMP at SRI

The second IMP was installed at SRI. The two switching nodes were linked by a high-speed leased circuit.

### 29 October 1969 — first UCLA–SRI host-to-host login attempt

At 22:30 UCLA time, Charley Kline at the UCLA Sigma 7 attempted a remote login to Bill Duvall at the SRI SDS 940. `L` and `O` arrived before the remote system failed; a complete login followed roughly an hour later.

The original UCLA IMP log survives and should be treated as a primary operational artifact, not just a story repeated by later histories.

## 3. Host computer: SDS Sigma 7

### Confirmed role

The UCLA node's host was a **Scientific Data Systems Sigma 7**, used by Leonard Kleinrock's Network Measurement Center. RFC and later Internet timelines identify the UCLA system as the first ARPANET host. Later summaries commonly associate the machine with the `SEX` operating environment; the exact UCLA operating-system configuration and its changes during 1969 should be reconstructed from UCLA/SDS records rather than accepted from timeline shorthand.

### What still needs to be captured

A proper Sigma 7 artifact record should include:

- CPU configuration and installed memory;
- I/O channel architecture used by the network interface;
- exact UCLA OS build/revision in August–October 1969;
- device addresses / channel assignment for the Host–IMP interface;
- whether network input/output used DMA, channel programs, interrupts, or a mixture;
- console and mass-storage devices present in 3420 Boelter Hall;
- exact physical cabinet layout if photographs or floor plans survive.

## 4. The most historically important custom hardware: Mike Wingfield's interface

The IMP did **not** plug directly into a standard port on the Sigma 7.

Steve Crocker's retrospective says SDS wanted many months and substantial money to build the required interface. UCLA graduate student **Mike Wingfield** instead undertook the work and produced a fully instrumented interface in roughly five and a half weeks.

This device deserves to be treated as an independent hardware artifact.

### Why it matters

The ARPANET's first four hosts were architecturally different computers. BBN standardized the IMP-side host boundary, but each site still had to bridge that boundary into its own host's native I/O system. At UCLA the result was custom hardware that translated between:

```text
Sigma 7 I/O/channel semantics
        ↕
Wingfield interface logic
        ↕
BBN Host–IMP bit-serial handshake
```

That is a different historical object from the IMP itself.

### Required excavation targets

We still need to recover, preferably from UCLA engineering drawings or surviving hardware:

- logic diagrams;
- board count and board technology;
- connector type and cable pinout;
- voltage levels;
- register map exposed to the Sigma 7;
- interrupt/channel behavior;
- instrumentation/test points;
- buffering strategy;
- treatment of `Last Bit`, ready, and error indications;
- photographs of the interface in situ;
- surviving parts or replicas and their provenance.

Steve Crocker has explicitly identified Wingfield as builder of the first UCLA host interface in later Internet-history correspondence.

## 5. The Host–IMP software at UCLA

RFC 7, Gerard Deloche's May 1969 *Host-IMP Interface*, is unusually valuable because it is a software design document written before the node became operational. It says the UCLA organization was divided into two major programs:

- a **Handler program**, driving the channel hardware;
- a **Network program**, processing users' transmission requests.

The two exchanged payload data through a pool of buffers and logical state through an interface table. Full duplex communication implied corresponding input and output paths.

RFC 1 also shows that the host protocol was still deliberately provisional. This matters: the first ARPANET node was not a finished standardized Internet stack. It was a moving target in which host groups were inventing the software boundary while BBN was finishing the IMP.

### Program archaeology still needed

- actual UCLA source listings;
- assembler/compiler and build process;
- buffer sizes and allocation strategy;
- channel handler interrupt paths;
- message queue structures;
- diagnostics used on 2 September;
- changes between September and the 29 October login;
- measurement hooks added for the Network Measurement Center.

## 6. IMP No. 1: modified Honeywell DDP-516

BBN's retrospective account identifies the original IMP hardware as a **modified Honeywell 516**. The 1969 IMP software was written by Bernie Cosell, Will Crowther, and Dave Walden; hardware modifications were led by Ben Barker and Severo Ornstein, with Frank Heart leading the project and Bob Kahn heavily involved in the overall design.

The retrospective describes the 516 as having roughly **32,000 bytes of memory** and a **1 µs memory cycle**. Older historical timelines often phrase the same configuration as **12K 16-bit words**. These values should not be collapsed carelessly: `12K words` and `24 KB`, `16K words` and `32 KB`, or configured-vs-addressable memory are different claims. The initial UCLA unit's exact installed core-memory capacity requires confirmation from the 1969 manufacturing/configuration documentation.

### BBN-specific hardware functions

The restored IMP project documents multiple custom interfaces/functions on the 516/316 family:

- synchronous modem interface with DMA-like memory transfer, framing, CRC and DLE handling;
- synchronous serial host interface;
- real-time clock;
- watchdog timer;
- network-specific communications status and interface logic.

The IMP was therefore not “just a Honeywell minicomputer running routing software.” It was a **Honeywell platform materially altered into a communications appliance**.

## 7. IMP software development chain

The software development environment is itself an artifact chain.

BBN's retrospective says IMP source was edited on BBN's **PDP-1d** using TECO. A modified **MIDAS** assembler understood Honeywell 516 opcodes, word size, and page boundaries. The resulting octal program could be emitted to **paper tape** for loading into an IMP through its paper-tape reader.

So an early IMP software release path looked approximately like:

```text
BBN engineer
   ↓ TECO
PDP-1d source
   ↓ modified MIDAS
Honeywell-516 machine image
   ↓ paper tape
paper-tape reader on IMP
   ↓
IMP core memory
```

This deserves preservation alongside the network protocol itself because it explains how packet-switch software was physically deployed before network-based remote updating became available.

## 8. Inter-IMP line: 50 kbit/s, not ordinary dial-up modem service

Early ARPANET histories repeatedly describe the UCLA–SRI link as **50 kbit/s**. Later ARPANET infrastructure moved toward standardized 56 kbit/s digital service, which is why retrospective RFCs may describe the ARPANET more generally as a 56-kbit/s network.

The 1969 link should therefore be recorded specifically as an **early 50-kbit/s generation**, not silently normalized to later 56-kbit/s terminology.

### Bell 303 question

Engineering recollections and later technical descriptions associate the first-generation IMP synchronous wideband interface with **Bell 303** data sets. This is highly plausible and is consistent with BBN's later IMP hardware documentation, but the exact UCLA and SRI modem/data-set model numbers, suffixes, circuit type, and installation records still require primary Bell/AT&T/BBN confirmation.

The research target is not merely “modem: Bell 303.” It is:

- exact model/revision at UCLA;
- exact model/revision at SRI;
- analog wideband or other carrier-service classification;
- four-wire/two-wire arrangement;
- leased-circuit tariff/service name;
- timing/clock source;
- line equalization/conditioning;
- local-loop ownership (GTE at UCLA) vs long-haul responsibility (AT&T Long Lines);
- BBN line-interface board connected to the data set;
- connector and pinout;
- commissioning/test procedures.

## 9. Organizations in the room

The node is best understood as a supply chain rather than a single invention.

| Layer | Organization(s) | Function |
|---|---|---|
| Research / measurement | UCLA | Network Measurement Center, host software, local experimentation |
| Host | Scientific Data Systems | Sigma 7 platform |
| Host interface | UCLA / Mike Wingfield | custom Sigma 7 ↔ IMP hardware |
| Packet switch | BBN | IMP hardware modifications, switching software, installation |
| Base minicomputer | Honeywell | DDP-516 platform |
| Long-haul telecom | AT&T Long Lines | intersite carrier facilities |
| Local telephone facilities | GTE (UCLA context) | local telco participation |
| Funding / program direction | ARPA/IPTO | network program and contracts |

This table is important because it shows why “who invented the Internet?” is usually the wrong granularity of question.

## 10. What an operator would have seen

A future revision should reconstruct the actual operational view:

- Sigma 7 console state;
- Wingfield interface indicators/test points;
- IMP front-panel lamps;
- communications channel indicators;
- Bell data-set alarms/indicators;
- paper logs;
- voice telephone coordination between UCLA and SRI during first login;
- BBN diagnostic procedures;
- test messages used before host-to-host service.

This is the difference between protocol history and infrastructure archaeology.

## 11. Surviving artifacts

UCLA's Connection Lab / Internet Museum states that **IMP No. 1 survives in 3420 Boelter Hall**. That surviving machine should eventually have a provenance record including:

- serial number;
- cabinet photographs;
- internal board photographs;
- present vs 1969 configuration;
- restoration/replacement history;
- whether the installed interface boards are original;
- whether the original UCLA Host–IMP interface survives nearby;
- conservation status.

Do not infer that every component currently attached to the surviving IMP is necessarily the exact September 1969 configuration without provenance evidence.

## 12. Current reconstruction confidence

### Confirmed / strong evidence

- UCLA was the first IMP delivery site.
- The host was an SDS Sigma 7.
- BBN's IMP was based on a modified Honeywell 516.
- Mike Wingfield built the UCLA Host–IMP interface.
- UCLA had local host/IMP communication at the beginning of September 1969.
- the first UCLA–SRI host-to-host login attempt occurred on 29 October 1969.
- the initial UCLA–SRI backbone generation operated at 50 kbit/s.

### Probable but not yet sufficiently nailed down

- exact Bell 303 model/suffix used on both ends of the first UCLA–SRI line;
- exact installed core-memory size of UCLA IMP No. 1 at delivery;
- exact cabinet/board population of Wingfield's interface;
- exact UCLA Sigma 7 operating-system revision at each milestone.

## 13. Open excavation checklist

1. Obtain BBN Reports 1763, 1783, 1837 and 1890 as image+OCR and mine component/configuration claims page by page.
2. Obtain a clean, date-specific Report 1822 revision closest to September 1969, not only the 1975/76 revision.
3. Locate Mike Wingfield drawings, thesis/report material, photographs or oral history.
4. Locate UCLA purchase/configuration records for the Sigma 7.
5. Locate AT&T/GTE service orders or Bell data-set installation records for the UCLA–SRI circuit.
6. Determine Bell 303 exact suffix/revision and electrical interface.
7. Photograph and inventory surviving IMP No. 1 board-by-board.
8. Determine whether the original Host–IMP interface hardware survives.
9. Recover UCLA 1969 network software listings and compare them to RFC 7's planned architecture.
10. Reconstruct the exact diagnostic sequence used on 2 September and 29 October.

## Sources

Primary/near-primary and participant sources used in this excavation:

- Steve Crocker recollection reproduced in RFC 1000, including Wingfield's interface and the 30 August delivery: https://www.rfc-editor.org/info/rfc1000/
- Gerard Deloche, RFC 7, *Host-IMP Interface* (May 1969): https://datatracker.ietf.org/doc/html/rfc7
- Steve Crocker, RFC 1, *Host Software* (7 April 1969): https://www.rfc-editor.org/info/rfc1/
- Leonard Kleinrock, *The Day the Infant Internet Uttered its First Words*: https://www.lk.cs.ucla.edu/internet_first_words.html
- Leonard Kleinrock personal history of the installation weekend: https://www.lk.cs.ucla.edu/personal_history.html
- UCLA Connection Lab / Internet Museum: https://uclaconnectionlab.org/internet-museum/
- *The ARPANET IMP Program: Retrospective and Resurrection* (IMP Software Guys, 2013): https://www.bitsavers.org/pdf/bbn/imp/The_ARPANET_IMP_Program_-_Retrospective_and_Resurrection_201312.pdf
- BBN IMP technical-report index, including Reports 1763 and 1822: https://www.bitsavers.org/pdf/bbn/imp/
- Internet-history discussion on original ARPANET line speed and Bell 303 evidence: https://elists.isoc.org/pipermail/internet-history/2017-January/004171.html

Secondary/context sources are useful as discovery aids but should not override the original installation records when those are recovered.
