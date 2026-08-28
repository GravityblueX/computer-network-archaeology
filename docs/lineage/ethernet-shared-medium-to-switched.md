# Ethernet Lineage: from shared coax to switched full-duplex links

Ethernet did not become the modern Ethernet we know by merely increasing its bit rate. The more important genealogy is architectural: a shared-medium random-access system became a family of standardized physical layers, then a star-wired shared collision domain, then a bridged/switched network, and finally a predominantly point-to-point full-duplex technology in which the original collision-detection machinery normally no longer participates.

This file keeps those historical layers separate.

## 1. Experimental Ethernet was a shared-medium system

The Xerox PARC experimental Ethernet of the 1970s inherited the central shared-medium problem that had already been explored in ALOHAnet: many independently operating stations contend for one communication medium.

The Ethernet solution was not simply ALOHA over coax. It combined:

- carrier sensing before transmission;
- collision detection during transmission;
- retransmission after collision;
- randomized backoff;
- a passive shared coaxial medium;
- station transceivers attached to that medium;
- framing and CRC logic distributed between interface hardware, microcode and software.

The experimental PARC system operated at approximately 2.94 Mbit/s. It should remain a separate artifact from later 10 Mbit/s Ethernet.

See:

- `../ethernet/xerox-alto-2-94mbps-pup-stack.md`
- `../ethernet/experimental-ethernet-physical-layer.md`

## 2. DIX Ethernet was not merely a renamed PARC prototype

Digital Equipment Corporation, Intel and Xerox jointly published *The Ethernet: A Local Area Network — Data Link Layer and Physical Layer Specifications*.

Version 1.0 is dated 30 September 1980. The IEEE Milestones archive identifies it as the DEC/Intel/Xerox Ethernet "Blue Book" specification.

This generation standardized a 10 Mbit/s Ethernet suitable for multivendor implementation. It is therefore better modeled as a successor generation to the Xerox experimental Ethernet rather than as the same object with a different date.

Important excavation tasks include:

- Version 1.0 versus Version 2.0 field-by-field comparison;
- physical-layer differences from the 2.94 Mbit/s PARC system;
- transceiver and Attachment Unit Interface evolution;
- address assignment practice;
- packet/frame type conventions;
- relationship between the DIX `EtherType` interpretation and IEEE 802.3 length/LLC conventions.

A surviving Version 1.0 copy is indexed by the IEEE Milestones history collection.

## 3. DIX Version 2.0

DIX Ethernet Version 2.0 appeared in November 1982.

For historical work, Version 2.0 needs its own record. Modern software documentation often loosely calls Ethernet-II framing "DIX" or "Ethernet II", but this archive should distinguish:

```text
Xerox experimental Ethernet
        ↓
DIX Ethernet Version 1.0 (1980)
        ↓
DIX Ethernet Version 2.0 (1982)
```

This is a specification lineage. It is not yet the whole IEEE standardization lineage.

## 4. IEEE 802.3 standardized CSMA/CD as a broader standard family

IEEE records show the original IEEE 802.3 standard approved by the Standards Board on 23 June 1983 and published as IEEE 802.3-1985.

The critical historical point is that IEEE 802.3 should not be described as a byte-for-byte renaming of DIX Ethernet.

DIX Ethernet and IEEE 802.3 were closely related and interoperable in important ways, but the standards lineage includes distinctions in framing interpretation and the relationship to IEEE 802 LLC.

The repository should therefore model the relationship as:

```text
DIX Ethernet 2.0
     ↘
      closely related / coexisted with
                               IEEE 802.3
```

rather than simply:

```text
DIX → renamed IEEE 802.3
```

## 5. 10BASE5: the classic shared coax world

Early standardized 10 Mbit/s Ethernet retained the shared-medium model.

A historically complete 10BASE5 installation includes more than "coax cable":

- thick 50-ohm coax;
- terminators;
- taps;
- Medium Attachment Units / transceivers;
- AUI cables;
- station interfaces;
- repeaters where used;
- segment-length and repeater-count constraints;
- collision domains;
- physical diagnostic practices such as TDR testing.

In that world, CSMA/CD was not an abstract diagram in a networking textbook. It was a direct consequence of multiple stations physically sharing one collision medium.

## 6. The star arrives without eliminating the shared medium

IEEE 802.3i-1990 standardized 10BASE-T. IEEE describes it as a 10 Mb/s twisted-pair MAU and baseband medium for a CSMA/CD LAN, with guidance for repeatered multisegment networks.

This creates one of the most important historical traps in Ethernet archaeology.

The physical topology could now look like a star:

```text
PC ─┐
PC ─┼─ hub
PC ─┘
```

but a repeater hub still created a shared collision domain.

So the transformation was:

```text
shared coax bus
      ↓
star-wired repeater network
```

not yet:

```text
shared medium
      ↓
independent point-to-point links
```

This distinction explains why early 10BASE-T networks could look physically modern while still behaving like classic CSMA/CD Ethernet.

## 7. Bridges and switches change the meaning of the LAN

Transparent bridges introduced a different boundary. Instead of repeating every bit into one shared collision domain, a bridge could learn MAC locations and selectively forward frames between segments.

The commercial Ethernet switch can be understood as a multiport bridging architecture, though product implementation histories must be documented separately.

Kalpana is an important excavation target because early EtherSwitch products helped make multiport Ethernet switching a commercial reality.

The key lineage is functional:

```text
repeater
  └── repeats physical symbols / bits

bridge
  └── forwards selected frames between collision domains

multiport bridge / Ethernet switch
  └── many independently forwarded ports
```

Do not describe a switch merely as "a faster hub". They inhabit different forwarding layers and changed the structure of contention.

## 8. Full duplex makes collision detection optional

IEEE 802.3x-1997 added full-duplex operation on a speed-independent basis for relevant Ethernet physical layers and also introduced pause-based flow control.

This marks a profound conceptual mutation.

On a dedicated point-to-point full-duplex link:

- each direction has its own communication path;
- simultaneous transmit and receive is allowed;
- there is no shared collision medium between the two endpoints;
- CSMA/CD collision handling is therefore not part of normal full-duplex operation.

The Ethernet frame lineage survives, while a defining mechanism of original Ethernet — shared-medium collision arbitration — can disappear from everyday operation.

This is exactly why lineage must track **properties**, not only product names.

## 9. What survived and what died

### Strongly surviving concepts

- MAC addressing;
- Ethernet framing lineage;
- frame check sequence / CRC error detection;
- Ethernet as a LAN link technology;
- a large portion of software-visible link semantics;
- the general family identity called "Ethernet".

### Mechanisms that became historically conditional

- shared coax as the normal medium;
- vampire taps;
- long AUI transceiver cables;
- repeater hubs;
- one large collision domain;
- CSMA/CD as a mechanism ordinary endpoints actually exercise.

### Concepts that changed meaning

"Ethernet" once implied a shared contention medium. Modern Ethernet commonly means switched point-to-point links in which contention/collisions are structurally absent.

The name survived more continuously than the physical topology.

## 10. A property-level lineage

The archive should ultimately support a table like this:

| Generation | Approx. medium/topology | Rate | Collision domain | CSMA/CD operationally relevant? | Forwarding element |
|---|---|---:|---|---|---|
| PARC experimental | shared coax | 2.94 Mb/s | shared | yes | none / shared Ether |
| DIX/10BASE5 | thick shared coax | 10 Mb/s | shared | yes | repeater optional |
| 10BASE2 | thin shared coax | 10 Mb/s | shared | yes | repeater optional |
| hub-based 10BASE-T | twisted pair star | 10 Mb/s | shared through hub | yes | repeater hub |
| bridged Ethernet | multiple media | 10+ Mb/s | one per bridge segment | locally | bridge |
| switched half-duplex | twisted pair | 10/100 Mb/s | often one per switch port | possible | switch |
| switched full-duplex | point-to-point | 10 Mb/s and above | none between endpoints | no | switch |

This table should eventually be generated from artifact/lineage records rather than maintained manually.

## 11. Evidence discipline

Primary/high-authority anchors for this lineage currently include:

- Metcalfe & Boggs, *Ethernet: Distributed Packet Switching for Local Computer Networks* (1976), for experimental Ethernet;
- DIX Ethernet Version 1.0 (30 September 1980), preserved in the IEEE Milestones archive;
- DIX Ethernet Version 2.0 (November 1982), surviving in archival copies;
- IEEE 802.3 history and base-standard records, with original approval in June 1983;
- IEEE 802.3i-1990, explicitly standardizing 10BASE-T MAU/baseband operation;
- IEEE 802.3x-1997, explicitly adding full-duplex operation and PAUSE flow control.

Copyrighted standards should be indexed and linked, not bulk-copied.

## 12. Open questions

- Exact DIX 1.0 → 2.0 clause/field diff.
- Exact frame-format differences among experimental Ethernet, DIX Ethernet II and IEEE 802.3/LLC usage.
- Earliest commercial 10BASE-T adapters and hubs by vendor/model.
- Early bridge product chronology before "Ethernet switch" became the dominant product term.
- Kalpana EtherSwitch model/revision chronology and implementation architecture.
- First documented deployed full-duplex Ethernet installations.
- Which early NICs could disable collision-detection/backoff behavior for full-duplex operation, and by what driver/API controls.
- Surviving examples of DIX-era transceivers, taps, hubs, early bridges and switches with deployment provenance.

## Lineage summary

```text
ALOHA shared-medium research
          ↓ documented influence
Xerox PARC experimental Ethernet (~2.94 Mb/s)
          ↓ successor generation
DIX Ethernet 1.0 (1980)
          ↓ revision
DIX Ethernet 2.0 (1982)
          ↘ related / coexisting standardization
           IEEE 802.3 (1983/1985)
                 ↓ physical-layer amendments
             10BASE5 / 10BASE2
                 ↓
             10BASE-T (802.3i, 1990)
                 ↓
          bridges / switches
                 ↓
       full-duplex Ethernet (802.3x, 1997)
```

The remarkable thing is not that Ethernet survived. It is that the word **Ethernet** survived while so much of the original physical and access mechanism changed underneath it.
