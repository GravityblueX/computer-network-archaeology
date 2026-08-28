# NSFNET T1 Nodal Switching Subsystem: nine IBM RTs, dual Token Rings, packet processors, routing control, and production operations

> Status: active excavation. This chapter reconstructs the 1988 NSFNET **Nodal Switching Subsystem (NSS)** as a multi-machine routing/switching installation. An NSS was not simply “an IBM RT router.” It was a redundant distributed node assembled from multiple IBM RT systems, internal Token Ring networks, management computers, wide-area line equipment, Ethernet attachment, routing software, and a production operations system.

## 1. The misleading one-box diagram

A network map usually draws each NSFNET backbone site as a single circle. RFC 1074 even says that, **for routing purposes**, each NSS is considered one entity.

Physically, however, Merit's NSFNET history states that each of the thirteen T1-era NSSs contained **nine IBM RT systems processors** running Berkeley UNIX and interconnected by **two Token Ring networks**. The node then attached outward to T1 facilities and to a regional/supercomputer network, typically by Ethernet.

The archaeological stack is therefore closer to:

```text
                     NSFNET logical routing node
    ┌─────────────────────────────────────────────────────┐
    │              Nodal Switching Subsystem             │
    │                                                     │
T1──┤ PSP ─┐                                             │
T1──┤ PSP ─┤                                             │
T1──┤ PSP ─┼── dual IBM Token Ring internal networks ─┐ │
T1──┤ PSP ─┘                                          │ │
    │                                                  │ │
    │              Routing Control Processor ──────────┤ │
    │              External Packet Switching Processor│─┼──Ethernet──regional/supercomputer network
    │                                                  │ │
    │              + three backup IBM RTs             │ │
    │                                                  │ │
    │  PS/2 Model 80 Bridge Manager ───────────────────┤ │
    │  PS/2 Model 80 NetView PC LAN Manager ──────────┘ │
    └─────────────────────────────────────────────────────┘
            ↑
       DSU/CSU + WACS
            ↑
      T1 carrier plant
```

This is a **distributed router implemented as a small network of computers**.

## 2. Thirteen sites, T1 links, richer logical topology

RFC 1074 (October 1988) gives a contemporary protocol-level description of the new backbone:

- thirteen sites in the continental United States;
- permanent point-to-point **T1 links at 1.544 Mbit/s**;
- a T1 could contain multiple **logical links** running at sub-T1 rates up through full T1;
- this produced a hybrid circuit/packet-switching system whose logical connectivity could be richer than its underlying physical T1 topology;
- every site contained an NSS;
- each NSS attached to regional networks through LANs, usually Ethernet.

The T1 network therefore had at least three different topology layers:

```text
physical carrier topology
    actual T1 circuits

        ↓ mapped by WACS / logical channels

logical backbone-link topology
    multiple logical links can share T1 facilities

        ↓ packet routing

IP / routing topology
    NSSs treated as routing entities
```

A conventional Internet map usually preserves only the third layer.

## 3. The nine IBM RT systems

Merit's Figure 14 and accompanying text provide the clearest surviving high-level decomposition.

The visible diagram shows:

### Four Packet Switching Processors (PSPs)

Four IBM RT systems are explicitly labeled **Packet Switching Processor**. Each is shown on the wide-area side of the dual Token Rings.

Their role was packet movement associated with backbone links. Later descriptions of the NSS architecture commonly speak of a PSP per T1/backbone interface; exact mapping by site and date should be verified from contemporary configuration documents rather than inferred from the generic figure.

### One Routing Control Processor (RCP)

An IBM RT system labeled **Routing Control Processor** handled routing-control functions.

RFC 1093 later refers explicitly to the **RCP/PSP routing architecture**, saying much of it was implemented by Rick Boivie and colleagues at IBM TCS in Milford, Connecticut.

The architectural significance is separation of:

```text
packet forwarding processors
        ↕
shared internal interconnect
        ↕
routing-control processor
```

This resembles later control-plane/data-plane separation, but it should be described in its own 1988 vocabulary rather than forced into a modern router chassis metaphor.

### One External Packet Switching Processor

The diagram contains one IBM RT labeled **External Packet Switching Processor** on the Ethernet/client-network side.

Later presentations sometimes call this a `PSP-G` or gateway packet-switching processor. The exact term by software release needs documentary reconciliation.

Its apparent role is to bridge the internal NSS forwarding system to the regional/supercomputer network side.

### Three backup IBM RTs

Figure 14's caption explicitly states that **three IBM RTs serving as backup are not shown**.

This closes the arithmetic:

```text
4 Packet Switching Processors
1 Routing Control Processor
1 External Packet Switching Processor
3 backup IBM RTs
-----------------------------------
9 IBM RT systems
```

The backup arrangement is itself an excavation target: were spares cold, warm, or hot? Which processor roles could each spare assume? What configuration/state had to be restored? How quickly did failover occur? Which failures were automatic versus NOC-directed?

## 4. Two IBM Token Ring networks formed the internal fabric

The IBM RT systems were linked by **two Token Ring networks**.

Merit's narrative says redundancy was a fundamental design objective: if a component or entire system failed, another RT could take over. The dual rings therefore should not be described merely as “LANs inside the router”; they formed a redundant internal communications fabric joining the distributed node's processors and management systems.

We still need to recover:

- exact IBM Token Ring adapter models;
- 4 or 16 Mbit/s operating speed;
- cabling system and MAU models;
- addresses of each processor on both rings;
- failover/ring-selection behavior;
- frame formats/protocols used internally;
- whether both rings carried normal traffic simultaneously or one was preferential/backup;
- ring monitoring and fault isolation procedures.

Until those values are recovered, “dual Token Ring” should be treated as strong architecture evidence but not a complete physical record.

## 5. PS/2 Model 80 management computers were additional machines

Figure 14 depicts **two IBM PS/2 Model 80** systems in addition to the nine RT processors:

- **Bridge Manager**;
- **NetView PC LAN Manager**.

These should not be counted among the nine IBM RTs.

Their presence reveals a second plane of machine activity around the routing node: network management, internal LAN/bridge supervision, diagnostics, and administrative control.

Research targets include:

- exact PS/2 Model 80 subtype/configuration;
- operating system (e.g. OS/2/DOS variant — do not assume without source);
- NetView release;
- Bridge Manager software identity;
- Token Ring/Ethernet adapters;
- console/monitor hardware;
- communications with the Ann Arbor NOC;
- retained logs/configuration media.

## 6. Berkeley UNIX was modified into router infrastructure

Merit's history calls the systems Berkeley UNIX machines. RFC 1074 is more precise: the IBM RT/PC processors ran a **modified version of a 4.3BSD kernel**.

This is an important implementation boundary.

The NSS was not simply using user-space routing daemons on stock UNIX. The archive needs to identify:

- kernel networking changes;
- forwarding fast path;
- driver changes for Token Ring, T1/WACS-facing hardware and Ethernet;
- interprocessor protocols;
- route-installation mechanisms;
- process layout on PSP vs RCP vs external PSP;
- build/release identifiers;
- IBM/Merit local patches versus upstream 4.3BSD.

A future source-code concordance should map each functional block in Figure 14 to actual kernel/daemon modules.

## 7. Routing: an ANSI IS-IS adaptation inside the backbone

RFC 1074 documents a striking protocol choice: the NSFNET backbone's interior routing protocol was an **adaptation of ANSI IS-IS / ISO ES-IS** to the IP environment.

This means the second-phase NSFNET core did not simply adopt RIP, HELLO, or OSPF.

The implementation:

- supported Level 2 routing rather than the complete ANSI hierarchy;
- treated permanent point-to-point links as the relevant subnetwork type;
- carried IS-IS/ES-IS-related PDUs **inside IP**, using IP protocol number 85;
- encoded IP information into NSAP-like structures for the adapted algorithm;
- ran Shortest Path First over flooded topology information;
- used 10-second IS-ES Hello intervals and 40-second hold times in the documented implementation.

This is a wonderful counterexample to a simplified standards-war narrative in which “Internet” and “OSI technology” never mixed. The production NSFNET backbone borrowed an ISO/ANSI routing design and adapted it directly into an IP network.

## 8. Exterior routing: EGP and a policy database

The boundary between NSFNET and attached mid-level networks used **EGP**.

RFC 1074 and RFC 1093 describe filtering/policy logic around these exchanges. Routing information learned through regional peers was injected into the backbone's internal routing with policy controls; reachability learned through the backbone was in turn filtered before advertisement outward.

The node therefore had at least these routing knowledge domains:

```text
regional / peer network routing
        ↕ EGP + filters
Policy Based Routing Database
        ↕
NSS routing control
        ↕ adapted IS-IS/SPF
backbone internal reachability
```

The repository should preserve the actual policy-database formats and operational edit/deployment process, because they are ancestors of the policy-heavy interdomain routing culture that later matured around BGP.

## 9. Packet switching and routing control were physically separated roles

Merit's report summarizes three NSS functions:

- packet switching;
- routing control;
- statistics gathering.

The multi-RT architecture gives those roles physical boundaries. A packet did not necessarily pass through the same processor that computed the topology.

The deep reconstruction target is:

```text
T1 packet arrives
        ↓
line/WACS/DSU-CSU boundary
        ↓
Packet Switching Processor
        ↓
internal Token Ring(s)
        ↓
possibly another PSP or External PSP
        ↓
output interface
```

while separately:

```text
routing updates / topology state
        ↓
Routing Control Processor
        ↓ SPF / policy / route computation
        ↓
forwarding state distributed to PSPs
```

Exact packet path and table-distribution semantics still require IBM/Merit engineering documents or source code.

## 10. WACS: the wide-area communications subsystem

Merit's Figure 14 draws the backbone's T1 lines emerging from a cloud called the **Wide-Area Communications Subsystem (WACS)**, passing through **DSU/CSU** blocks before entering the NSS.

This means the packet router node and the carrier/circuit system were deliberately separated.

The WACS is essential because RFC 1074 says multiple logical links could share T1 facilities. Circuit capacity therefore had to be subdivided, mapped and managed before packets reached individual switching processors.

Later institutional descriptions associate the WACS with IBM IDNX equipment. The archive must still obtain a contemporary engineering source identifying exact IDNX models, software, channelization and circuit-switching behavior at each site.

Do not replace WACS with a generic “T1 multiplexer” until model-level evidence is obtained.

## 11. DSU/CSU boxes were first-class infrastructure

Figure 14 visibly places **DSU/CSU** units between T1 lines and the NSS.

That physical boundary should become its own device genealogy:

- carrier-side electrical interface;
- customer-side interface;
- framing mode;
- line coding;
- clock source;
- loopbacks;
- alarms;
- performance counters;
- connector/cabling;
- vendor/model;
- who owned the box (MCI, site, IBM, Merit);
- who could initiate tests.

A backbone link did not run directly from an IBM RT serial port into “the telephone network.”

## 12. Ethernet was the client-facing edge

RFC 1074 says attached regional networks normally connected through local-area interfaces, typically **Ethernet**. Merit's Figure 14 shows a single Ethernet path from the External Packet Switching Processor to a mid-level and/or supercomputer network.

The exact Ethernet generation and adapter models need site-by-site research.

Questions:

- 10BASE5 or other physical variant at July 1988 deployment?
- IBM RT Ethernet adapter manufacturer/model?
- transceiver/AUI details?
- client-side bridge/router between NSS and regional backbone?
- ARP behavior and subnet/address plan?
- EGP peer process location?

This external Ethernet is different from the two internal Token Rings and should never be flattened into a generic “LAN attachment.”

## 13. Assembly was industrialized in Ann Arbor

Merit's history preserves an unusually concrete deployment practice.

The third floor of the University of Michigan Computer Center was turned into an **assembly line/depot**. IBM RT systems were delivered there, tested, loaded with software and assembled into NSS configurations. Staff from regional networks came to Ann Arbor and participated in building their own router nodes.

The project therefore had something resembling a router manufacturing/integration line before shipment to each site.

This deserves preservation as process archaeology:

```text
IBM hardware delivery
        ↓
Ann Arbor assembly depot
        ↓ hardware test
        ↓ software installation
        ↓ NSS configuration/integration
        ↓ regional staff participation
        ↓ rack/crate shipment
        ↓ site installation by IBM personnel
        ↓ remote Merit/MCI support
```

The report says the project ultimately configured roughly **150 systems integrating thousands of parts**.

## 14. “Seven RTs and three racks”: preserve the inconsistency

The same Merit report tells an anecdote about shipping a node to Rice University for SESQUINET: **seven RTs and three racks** were in the shipment.

That apparently conflicts with the generic statement that each NSS had nine IBM RT systems.

The correct archaeological response is **not** to choose whichever number looks cleaner.

Possible explanations include:

- only seven active/non-spare RTs shipped in that particular load;
- backup units were shipped separately;
- SESQUINET had a site-specific configuration;
- the anecdote simplified the count;
- the architecture changed by date.

Until shipping records/inventory lists are found, both claims should remain in the record with different scope:

- **generic architecture:** nine RTs per NSS;
- **specific SESQUINET shipment anecdote:** seven RTs, three racks.

This is exactly the kind of conflict that disappears in conventional histories.

## 15. The NOC was part of the router system

The new Merit Network Operations Center occupied the same third floor in Ann Arbor.

Merit's report describes:

- a hexagonal central room;
- large monitors showing status of each NSS, MichNet and NSFNET links;
- an Ann Arbor NSS visible through a window into the machine room;
- **two IBM 4831 mainframes** used for network management/statistics and information services;
- documentation and performance data;
- round-the-clock staffing.

Soon after opening, staffing increased from **four to eighteen people**, providing **24 hours/day, seven days/week** coverage.

The NSS therefore had an operational extension hundreds or thousands of kilometres away:

```text
remote NSS sensors/state
        ↓
network management / reporting path
        ↓
Ann Arbor NOC
        ↓
operators + large displays + IBM systems
        ↓
trouble ticket / escalation
        ↓
Merit / IBM / MCI / regional site action
```

## 16. Commercial operations discipline entered academic Internet infrastructure

Merit's retrospective explicitly emphasizes procedures adopted or adapted from IBM and MCI:

- documentation;
- trouble tickets;
- escalation procedures;
- follow-through;
- statistical reporting;
- 24×7 coverage.

A line problem could move through an aggressive MCI escalation ladder. A routing-daemon failure could result in the software author being called at home and issuing a fix within hours.

This is historically important because the late-1980s Internet was becoming not only faster but **operationally professionalized**.

The archive needs the actual `NSFNET Site Manual`, trouble-ticket forms, escalation matrices, call lists and NOC runbooks.

## 17. Cross-domain debugging exposed new failure boundaries

Merit records an example in which MCI's transmission measurements suggested a circuit was operating acceptably while Merit observed roughly 50% packet loss.

The precise incident should be recovered from contemporary ticket/log records, but the story illustrates a new operational problem:

```text
carrier sees physical/T1 circuit metrics
        ≠
IP operator sees packet-delivery behavior
```

A backbone could therefore be “up” in the telephone-company sense while unusable in the packet-network sense.

This boundary between telecom operations and IP operations deserves its own history.

## 18. Routing software itself failed in production

Merit's history records a weekend during which routing daemons throughout the nodes crashed. Hans-Werner Braun contacted Yakov/Jacob Rekhter and a fix was produced within roughly two hours.

This is valuable implementation evidence:

- routing control was software under active development;
- the backbone could encounter correlated/systemic software failure;
- expert developers were part of production escalation;
- patch turnaround was operationally critical.

Future archaeology should locate the actual bug report, source diff, release identifier and deployment log.

## 19. Retirement created a provenance trail

A December 1992 NANOG archive message states that after traffic migrated from the T1 NSFNET to the T3 infrastructure, the T1 NSS network had been dismantled. Regional sites were offered donated IBM RT workstations from their former NSS equipment.

The message says approximately **4–6 RT workstations were available at each T1 NSS site**, and notes that most lacked monitor or keyboard because they had served as routers.

This is an extraordinary provenance lead.

A museum search should therefore not look only for an object labeled “NSFNET router.” Some surviving NSFNET RTs may have spent decades afterward as ordinary donated workstations at universities or in private collections.

Needed follow-up:

- recipient lists;
- IBM serial numbers;
- asset tags;
- disposal records;
- photographs of racks before dismantling;
- surviving RTs with NSFNET labels/config disks/adapters.

## 20. Current known machine inventory of a generic NSS

### Strongly supported by Merit Figure 14

| Count | Machine / role |
|---:|---|
| 4 | IBM RT System — Packet Switching Processor |
| 1 | IBM RT System — Routing Control Processor |
| 1 | IBM RT System — External Packet Switching Processor |
| 3 | IBM RT System — backup units, not shown in figure |
| 1 | IBM PS/2 Model 80 — Bridge Manager |
| 1 | IBM PS/2 Model 80 — NetView PC LAN Manager |
| 2 | IBM Token Ring internal networks |
| multiple | DSU/CSU units associated with T1 links |
| 1 logical subsystem | WACS / wide-area communications system |
| 1+ | Ethernet attachment to client network |

### Not yet known at adequate confidence

- exact IBM RT model/submodel;
- CPU card and clock rate;
- RAM in each RT role;
- disk size/model;
- tape/floppy/boot media;
- exact Token Ring adapter and MAU;
- Ethernet adapter/transceiver;
- T1/WACS interface boards;
- DSU/CSU vendor/model;
- IDNX model and configuration;
- PS/2 Model 80 submodel, RAM/storage/adapter configuration;
- rack manufacturer and rack-unit layout;
- UPS/power distribution;
- console cabling;
- spare parts inventory.

The next milestone for this chapter is to replace the second list with a site-specific BOM.

## 21. Software inventory still to recover

The node's software archaeology should eventually separate:

### common/base
- modified 4.3BSD kernel;
- IBM RT boot environment;
- device drivers;
- internal Token Ring protocols.

### PSP
- packet forwarding;
- T1/logical-link interface;
- packet queues;
- counters;
- route-table lookup.

### RCP
- adapted IS-IS/ES-IS;
- SPF computation;
- EGP;
- policy database;
- route distribution to PSPs;
- management agent(s).

### external PSP
- Ethernet attachment;
- regional peer forwarding;
- EGP/data-plane interaction.

### management
- Bridge Manager;
- NetView PC LAN Manager;
- NOC telemetry;
- statistics collection;
- configuration/update mechanisms.

Every binary/source release should be tied to a date and site if possible.

## 22. NSFNET proves “router” was becoming a system-of-systems

The Fuzzball generation could plausibly be imagined as one PDP-11-class machine with several interfaces. The T1 NSS makes that mental model fail.

A routing node now comprised:

- many general-purpose computers;
- redundant internal LANs;
- separate control and forwarding roles;
- separate management computers;
- packet switching plus circuit/channel management;
- carrier termination equipment;
- remote NOC infrastructure;
- formal operational processes.

In other words, a single circle on an NSFNET map hid a **small distributed computing system**.

## 23. Open excavation checklist

1. Recover the original Merit/IBM NSS hardware engineering specification.
2. Identify exact IBM RT models for every role and every site.
3. Recover per-role RAM/disk/adapter configurations.
4. Identify internal Token Ring adapters, MAUs, speed and cabling.
5. Reconstruct PSP↔RCP internal protocol and route-table distribution.
6. Locate modified 4.3BSD kernel/source tree and build system.
7. Recover RCP/PSP software release history and source control artifacts.
8. Recover the Policy Based Routing Database format and deployment workflow.
9. Identify WACS hardware, exact IBM IDNX model(s), channelization and control software.
10. Identify DSU/CSU models and T1 framing/line-code settings.
11. Recover physical rack layout and power/console wiring.
12. Build a per-site circuit/BOM table for all thirteen July 1988 NSS sites.
13. Resolve nine-RT generic design versus seven-RT SESQUINET shipment anecdote.
14. Recover the NSFNET Site Manual, trouble-ticket forms and escalation procedures.
15. Recover Ann Arbor NOC software/screens/statistics architecture.
16. Identify the two IBM 4831 systems' exact roles/configurations.
17. Recover 1988 routing-daemon crash incident and patch.
18. Trace 1992–93 dismantling/donation by RT serial number and recipient.
19. Locate surviving NSS-derived IBM RTs and preserve provenance.
20. Compare the T1 NSS architecture to the later T3 C-NSS/E-NSS architecture without projecting the later design backward.

## Primary / high-value sources

- Yakov/Jacob Rekhter, RFC 1074, *The NSFNET Backbone SPF Based Interior Gateway Protocol* (October 1988): https://www.rfc-editor.org/rfc/rfc1074.html
- Hans-Werner Braun, RFC 1093, *The NSFNET Routing Architecture* (February 1989): https://www.rfc-editor.org/rfc/rfc1093.html
- Yakov/Jacob Rekhter, RFC 1092, *EGP and Policy Based Routing in the New NSFNET Backbone* (February 1989): https://www.rfc-editor.org/rfc/rfc1092.html
- Merit Network, *NSFNET: A Partnership for High-Speed Networking* — especially Figure 14 and the NOC/deployment discussion: https://www.merit.edu/wp-content/uploads/2024/10/Merit-Network_NSFNET-A-Partnership-for-High-Speed-Networking.pdf
- NANOG archive, Bob Farzami, `T1 NSFNet NSS Dismantling - January 1993` (24 December 1992): https://lists.nanog.org/archives/list/nanog@lists.nanog.org/1992/12/
- Hans-Werner Braun & Yakov/Jacob Rekhter, RFC 1222, *Advancing the NSFNET Routing Architecture* (May 1991): https://www.rfc-editor.org/rfc/rfc1222.html

### Evidence cautions

- The Merit final report is a participant/institutional retrospective, though its machine-role diagram and deployment narrative are exceptionally concrete. Whenever possible, recover contemporary IBM/Merit hardware inventories beneath it.
- RFC 1074 is contemporary primary protocol/architecture evidence, but it treats an NSS as one logical routing entity and therefore does not describe every physical machine.
- The `seven RTs and three racks` SESQUINET anecdote is preserved as a scoped observation rather than used to overwrite the generic nine-RT architecture.
