# ALOHAnet: the radio network inside the Ethernet origin story

ALOHAnet is often mentioned only as “the thing that inspired Ethernet.” That hides an unusually concrete packet-radio system: UHF channels, terminal control units, RS-232 terminals, a central computer, retransmission rules, repeaters, concentrators and later gateways to other networks.

## Project purpose

The University of Hawaiʻi began the ALOHA project in the late 1960s under Norman Abramson and Franklin Kuo with a practical geographic problem: university users were scattered across islands, while the main computing resources were centralized in Honolulu.

Building dedicated terrestrial circuits to every site was expensive. Radio made the transmission medium shared by design.

That forced the team to solve a problem that wired point-to-point networking could often postpone:

> what happens when several independent users transmit into the same medium without a central scheduler?

## Original radio architecture

Abramson's retrospective engineering account records two 100 kHz UHF channels assigned at approximately:

- **407.350 MHz**;
- **413.475 MHz**.

The system separated traffic direction: remote terminals transmitted toward the central station on one channel, while the central station broadcast outward on the other.

A simplified terminal path was:

```text
terminal
  ↓ RS-232
Terminal Control Unit (TCU)
  ↓ packet framing / retransmission logic
UHF radio transmitter
  ↓ shared inbound radio channel
central ALOHA station / host-side system
  ↓
central computer services
```

Return traffic followed the broadcast channel back to remote users.

## Terminal Control Unit (TCU)

The TCU is one of the most important physical artifacts in ALOHAnet and should not be reduced to a diagram box.

Abramson credits Alan Okinaka and David Wax with design work on the special-purpose TCU. The unit handled:

- packet formatting;
- retransmission behavior;
- the terminal/radio boundary;
- connection of a conventional terminal through **RS-232**;
- access at approximately **9600 bit/s** within radio range.

The original design deliberately carried extensive debugging facilities because this was experimental hardware and protocol logic, not a mature communications appliance.

## Packet format

A later NIST/NBS historical review gives a compact description of an ALOHA packet consisting of:

- a 32-bit header;
- a 16-bit header check word;
- up to 80 bytes of data;
- a 16-bit data check word.

This should be checked against the specific network revision being documented. ALOHAnet evolved, and packet formats should be versioned rather than treated as timeless.

## Pure ALOHA: failure is part of the protocol

The original ALOHA random-access idea was strikingly simple:

1. a remote station transmits when it has a packet;
2. if two stations overlap, their transmissions may collide;
3. the sender infers failure from the lack of successful acknowledgment/response;
4. it waits a random interval;
5. it retransmits.

In other words, the protocol does not prevent every collision. It makes collision **recoverable**.

That trade changes the entire design space. Instead of central reservation, the shared medium can remain simple and decentralized at the edge.

## Slotted ALOHA

Slotted ALOHA restricts transmission starts to synchronized time slots. That lowers the vulnerable collision interval and improves theoretical maximum throughput compared with unslotted Pure ALOHA.

The conceptual lineage matters more than the famous throughput numbers:

```text
shared broadcast medium
        ↓
random access
        ↓
collision as an expected event
        ↓
randomized retransmission
        ↓
slotted refinement
        ↓
carrier sensing / collision detection in Ethernet
```

## Range and island geography

Abramson's 1985 account describes useful radio range on the order of **100 km** for the original system. The physical geography therefore belongs in the protocol story: mountains, islands, antenna placement, repeaters and line-of-sight conditions affected what “network topology” meant.

Future work should map every known TCU/repeater site by year.

## The Menehune and central resources

Later ALOHAnet diagrams show a central station called the **Menehune**, along with terminal units, concentrators, repeaters and gateways to external networks.

The name should be attached to exact hardware/software revisions in future work rather than used generically for every stage of the project.

## Microprocessors changed the edge

Later ALOHA packet-control units could use early microprocessors instead of purely special-purpose logic. Historical diagrams show packet-control units based on Intel 8008/8080-era technology as the system evolved.

This is an important transition:

> packet networking moved from bespoke communications electronics toward programmable edge devices.

That same shift later transformed modems, NICs, bridges, routers and terminal servers.

## ALOHAnet ↔ ARPANET

ALOHAnet was eventually connected into the ARPA networking world. The exact chronology and transmission path should be documented separately, because contemporary and retrospective sources sometimes compress satellite experiments, packet-radio work and ordinary ARPANET attachment into one sentence.

The important architectural consequence is clear: radio packet networks became one of the heterogeneous subnetworks that motivated **internetworking**, not merely host networking.

## From ALOHA to Ethernet

Bob Metcalfe studied the ALOHA work before developing Ethernet at Xerox PARC. Ethernet inherited the notion that many stations could share one broadcast medium without a central polling controller.

But Ethernet did not simply copy ALOHA.

Its early coaxial medium allowed a station to sense activity and detect collisions while transmitting. That produced **carrier-sense multiple access with collision detection (CSMA/CD)**.

A useful comparison is:

| Feature | ALOHAnet | Experimental Ethernet |
|---|---|---|
| medium | UHF radio | shared coaxial cable |
| topology | central broadcast/radio coverage | cable segment |
| access | random transmit/retry | carrier sense + transmit + collision detection |
| collision knowledge | inferred from failed exchange | detected on cable during transmission |
| edge unit | TCU/packet unit | Ethernet interface/transceiver |
| major constraint | scarce shared radio channel | shared cable capacity and propagation delay |

## Ethernet archaeology begins before 10BASE5

The first PARC Ethernet was not 10 Mbit/s IEEE Ethernet. Metcalfe's 1973 memo described the concept, and the experimental Alto network that followed ran at roughly **2.94 Mbit/s**.

Only later did DEC, Intel and Xerox publish the 10 Mbit/s DIX Ethernet specification, followed by IEEE 802.3 standardization.

Therefore this repository must preserve at least four distinct objects:

1. ALOHA packet radio;
2. 1973 PARC Ethernet concept;
3. experimental 2.94 Mbit/s Xerox Ethernet;
4. 10 Mbit/s DIX / IEEE 802.3 Ethernet families.

Treating all of these as one “Ethernet” erases the engineering evolution.

## Sources

1. University of Hawaiʻi College of Engineering, **ALOHAnet history and paper archive**: <https://www.eng.hawaii.edu/about/history/alohanet/>
2. Norman Abramson, **“Development of the ALOHANET”** (1985), hosted by University of Hawaiʻi: <https://www.eng.hawaii.edu/wp-content/uploads/2020/06/abramson1985-Development-of-the-ALOHANET.pdf>
3. Computer History Museum oral history of Norman Abramson: <https://archive.computerhistory.org/resources/access/text/2020/12/102746750-05-01-acc.pdf>
4. NIST/NBS retrospective packet-network survey with ALOHAnet resource diagrams: <https://nvlpubs.nist.gov/nistpubs/jres/086/6/jresv86n6.pdf>
5. Computer History Museum, **Happy 40th Birthday, Ethernet!**: <https://computerhistory.org/blog/happy-40th-birthday-ethernet/>
6. Ethernet 1973 PARC memo metadata/preserved copy: <https://ieeemilestones.ethw.org/File:Ref1_PARC_Ethernet_Memo_1973.pdf>
7. IEEE/ETHW Ethernet milestone history: <https://ethw.org/Milestones:Ethernet_Local_Area_Network_(LAN),_1973-1985>

## Unresolved excavation tasks

- recover the 1970 AFIPS ALOHA paper in a stable primary archive;
- identify exact radio models, transmit power, antennas and modems used by each site;
- document TCU schematics and logic families;
- reconstruct the packet header field-by-field for each revision;
- document acknowledgment and retransmission timing constants;
- map every terminal/repeater site and date;
- recover Menehune hardware and software revisions;
- trace Intel 8008/8080 packet-control units;
- document the exact ALOHAnet–ARPANET gateway path;
- reconstruct Metcalfe's ALOHA simulation work and what changed in Ethernet;
- write a separate 2.94 Mbit/s Ethernet hardware excavation covering Alto interfaces, coax, transceivers and packet formats.

The historical bridge from ALOHA to Ethernet is not “wireless became wired.” It is the migration of a deeper idea: **a shared medium can be useful even when collisions are normal, provided the protocol makes contention survivable.**