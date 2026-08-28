# Living Standards Still on the Wire

> A standard can be old in three different senses: old text, old mechanism, or old deployment. Those are not the same thing.

This excavation tracks a class of artifacts that are unusually easy to misunderstand: networking standards whose roots are decades old but whose descendants are still used in production systems today.

The goal is **not** to say that the Internet has not changed. It has changed continuously. The goal is to distinguish several historically different forms of continuity.

---

## 1. Three kinds of survival

### 1.1 The original RFC is still an Internet Standard

Examples include:

- IPv4 — RFC 791, September 1981, still listed by the RFC Editor as **STD 5 / Internet Standard**, with later updates.
- UDP — RFC 768, August 1980, still **STD 6 / Internet Standard**, with later updates.
- ICMP for IPv4 — RFC 792, September 1981, still **STD 5 / Internet Standard**, with later updates.

This is stronger than saying that later systems are merely "compatible with the old idea". In these cases, the old standard remains part of the contemporary standards corpus.

Primary records:

- RFC 791: https://www.rfc-editor.org/info/rfc791/
- RFC 768: https://www.rfc-editor.org/info/rfc768/
- RFC 792: https://www.rfc-editor.org/info/rfc792/

But even here, **still a standard does not mean frozen**. RFC 791 has been updated by later RFCs; host requirements were supplemented by RFC 1122; deployed interpretations accumulated around fragmentation, precedence/DS fields, router behavior, MTU discovery, security, and operational practice.

The right genealogy is therefore:

```text
old core standard
    + later normative updates
    + implementation practice
    + operational constraints
    = current deployed protocol behavior
```

not:

```text
1981 text == every 2026 implementation detail
```

---

### 1.2 The old RFC is formally obsolete, but the protocol identity survives

TCP is the clearest example.

RFC 793 (1981) defined the famous TCP functional specification. In August 2022, RFC 9293 formally **obsoleted RFC 793** and collected decades of normative changes into a consolidated specification.

RFC 9293 explicitly says that TCP has continuously evolved over decades and that the new document combines the RFC 793 specification with later changes. Its main body was adapted from RFC 793 Section 3 with formatting and layout intentionally kept close where possible.

Primary record:

- RFC 9293: https://www.rfc-editor.org/info/rfc9293/

This gives us a different kind of historical continuity:

```text
TCP RFC 793
   ↓ updates / corrections / security changes / errata
TCP RFC 9293
```

The old *document* is obsolete.

The old *protocol lineage* is not.

This distinction matters throughout the archive. "Obsoleted" is a relationship between standards documents. It does **not** mean that the protocol disappeared from the network.

---

### 1.3 The old architecture remains the production skeleton while extensions keep growing

DNS is a classic example.

RFC 1034 and RFC 1035 were published in November 1987. They define the concepts, namespace, server/resolver model, caching, queries/responses, and wire/data structures of the Domain Name System.

The DNS ecosystem has since accumulated enormous additions:

- new resource-record types;
- EDNS;
- DNSSEC;
- internationalized names at other layers;
- new transport practices;
- resolver privacy mechanisms;
- operational root/TLD changes;
- anycast deployments;
- aggressive caching and validation behavior.

Yet the RFC 1034/1035 architecture is still immediately recognizable in contemporary DNS.

Primary records:

- RFC 1034: https://www.rfc-editor.org/info/rfc1034/
- RFC 1035: https://www.rfc-editor.org/info/rfc1035/

RFC 1034 itself says that the official protocol components were expected to remain essentially unchanged and operate as a production service, while extensions could continue to appear.

That is almost a description of what actually happened.

---

## 2. A modern packet is full of historical strata

Consider an ordinary IPv4 Ethernet packet carrying a DNS query over UDP.

A simplified view looks like:

```text
Ethernet frame
  ↓
ARP-derived neighbor resolution context
  ↓
IPv4 header
  ↓
UDP header
  ↓
DNS header/question
```

The historical core dates are roughly:

```text
Ethernet family        1970s–1980s
UDP RFC 768            1980
IPv4 RFC 791           1981
ICMP RFC 792           1981
ARP RFC 826            1982
DNS RFC 1034/1035      1987
```

This is not a museum reconstruction.

It is an ordinary production pattern still encountered on real networks.

The important observation is not merely that "old things survived". It is that **different layers survived in different ways**:

- frame formats survive while physical media changed;
- IPv4 survives while address allocation and routing changed;
- UDP survives while applications around it changed dramatically;
- ARP survives on IPv4 LANs even while IPv6 uses a different neighbor-discovery architecture;
- DNS survives by deliberately providing an extensible data model;
- application semantics are repeatedly revised while retaining recognizable command and header conventions.

---

## 3. IPv4: still STD 5

RFC 791 remains an Internet Standard.

Its core model is startlingly familiar:

- datagrams;
- fixed-length source/destination addresses;
- independent packet handling;
- no virtual circuit;
- routing toward destination;
- fragmentation/reassembly model;
- TTL;
- header checksum;
- protocol-number demultiplexing.

RFC 791 explicitly limits IP's responsibility: it does not provide end-to-end reliability, acknowledgments, retransmission, sequencing, or flow control. Those responsibilities belong elsewhere.

That separation remains one of the most durable architectural fossils in networking.

But not every 1981 field has the same modern meaning. Type of Service evolved; router requirements accumulated; fragmentation practice changed; security expectations changed; NAT became common; CIDR replaced classful address assumptions.

So this archive must track **field survival**, not only protocol-name survival.

---

## 4. UDP: minimalism that survived

RFC 768 is one of the shortest and longest-lived core Internet standards.

Its durable design is exactly its lack of ambition:

- source port;
- destination port;
- length;
- checksum;
- application datagrams;
- no reliability machinery;
- no ordering machinery;
- no connection state.

Modern applications may build sophisticated behavior above UDP, but the underlying abstraction remains recognizable.

This is an important historical lesson:

> durability does not always come from adding features; sometimes it comes from refusing responsibility.

---

## 5. ICMP: control/error semantics as an IP companion

RFC 792 describes ICMP as part of the Internet protocol machinery for reporting problems and control information.

Many mechanisms familiar to operators depend on this old control plane:

- Echo Request / Echo Reply → the primitive used by `ping`;
- Time Exceeded → exploited by traceroute-style path discovery;
- Destination Unreachable;
- Redirect, historically important but operationally controversial;
- later extensions and deprecations layered onto the original framework.

Again, the old RFC is still an Internet Standard while later documents update specific behavior.

---

## 6. ARP: an old local-network boundary that IPv4 still uses

ARP dates to RFC 826 (1982).

Its job is conceptually simple:

```text
protocol-layer address
        ↓ resolution
local hardware/link-layer address
```

For Ethernet/IPv4, this commonly means:

```text
IPv4 address → Ethernet MAC address
```

ARP survived because the problem survived: an IP implementation on a broadcast LAN still needs to know which link-layer destination to use for a local next hop.

But this is not a universal Internet-layer law. IPv6 did **not** simply adopt ARP unchanged; it uses Neighbor Discovery over ICMPv6.

That makes ARP especially useful as a historical boundary marker:

> some mechanisms survived for decades without becoming universal across successor protocols.

---

## 7. TCP: the protocol survives by being revised

TCP demonstrates a different survival strategy from UDP.

The 1981 protocol identity persisted, but TCP accumulated:

- retransmission-timer improvements;
- congestion control;
- sequence-number security changes;
- reset-handling hardening;
- ECN-related control bits;
- clarified host requirements;
- decades of errata and interoperability lessons.

RFC 9293 is therefore historically significant not because it invents a new TCP, but because it makes explicit that **the living standard is a sedimentary object**.

A protocol can be continuous while its normative text is periodically recompiled from decades of amendments.

---

## 8. DNS: extensibility as a survival mechanism

RFC 1034/1035 built extensibility into the system from the beginning.

The durable skeleton includes:

- hierarchical names;
- delegation;
- authoritative servers;
- resolvers;
- caching;
- resource records;
- queries and responses;
- distributed administration.

Later mechanisms did not need to replace the entire naming system. They could add data types, security, transport options, and operational practices.

This is why DNS history should be modeled as a **core plus branching extensions**, not as a clean sequence of replacements.

---

## 9. Mail: the transport changes while message archaeology remains visible

Modern Internet mail still exposes deep historical layers.

SMTP's modern core specification is RFC 5321 (2008), which consolidates and updates earlier SMTP standards. Message syntax is separately defined by RFC 5322, which explicitly descends from RFC 2822 and RFC 822.

MIME RFC 2045 and its companion documents extend message representation for non-ASCII text, media types, multipart bodies, and transfer encodings.

So one contemporary message may simultaneously embody genealogies from:

```text
ARPANET mail headers
      ↓
RFC 822 message syntax
      ↓
RFC 2822
      ↓
RFC 5322

plus

MIME RFC 2045 family

plus

SMTP RFC 821
      ↓
ESMTP extensions
      ↓
RFC 2821
      ↓
RFC 5321
```

Mail is not one protocol. It is a stack of old interfaces that learned to coexist.

---

## 10. Survival vocabulary for this repository

Future records should distinguish at least these statuses:

### `still-current-original-standard`

The old standards document itself remains a current Internet Standard or equivalent normative anchor.

Examples:

- RFC 791 IPv4;
- RFC 768 UDP;
- RFC 792 ICMP.

### `obsoleted-document-living-protocol`

The old RFC is formally obsolete but the protocol lineage survives through a replacement specification.

Example:

- RFC 793 TCP → RFC 9293.

### `living-core-with-extension-forest`

The old architecture remains the core while many later standards extend it.

Example:

- DNS RFC 1034/1035.

### `interface-convention-survives`

The exact original standard may be superseded or vendor-specific, but software and hardware still inherit the interaction model.

Examples elsewhere in this archive:

- Hayes-style AT commands;
- RS-232-derived console practice;
- bridge/switch MAC learning roles.

### `mechanism-dead-name-survives`

The family name remains while a once-central mechanism becomes irrelevant in ordinary deployment.

Example:

- full-duplex switched Ethernet retaining the Ethernet identity while normal CSMA/CD operation disappears.

---

## 11. Why this matters

Networking history is often narrated as replacement:

```text
old → new → newer → modern
```

But the production Internet is more accurately described as layering:

```text
old core
 + revisions
 + compatibility
 + extensions
 + operational workarounds
 + new transports
 + new security expectations
```

The result is why a packet capture made today can still contain structures whose basic format was standardized before many current engineers were born.

This is not technical stagnation.

It is **compatibility as historical force**.

---

## Primary sources

- RFC 791 — Internet Protocol: https://www.rfc-editor.org/info/rfc791/
- RFC 768 — User Datagram Protocol: https://www.rfc-editor.org/info/rfc768/
- RFC 792 — Internet Control Message Protocol: https://www.rfc-editor.org/info/rfc792/
- RFC 826 — Address Resolution Protocol: https://www.rfc-editor.org/info/rfc826/
- RFC 1122 — Requirements for Internet Hosts — Communication Layers: https://www.rfc-editor.org/info/rfc1122/
- RFC 1034 — Domain Names — Concepts and Facilities: https://www.rfc-editor.org/info/rfc1034/
- RFC 1035 — Domain Names — Implementation and Specification: https://www.rfc-editor.org/info/rfc1035/
- RFC 9293 — Transmission Control Protocol (TCP): https://www.rfc-editor.org/info/rfc9293/
- RFC 5321 — Simple Mail Transfer Protocol: https://www.rfc-editor.org/info/rfc5321/
- RFC 5322 — Internet Message Format: https://www.rfc-editor.org/info/rfc5322/
- RFC 2045 — MIME Part One: https://www.rfc-editor.org/info/rfc2045/
- RFC 8200 — IPv6 Specification: https://www.rfc-editor.org/info/rfc8200/

## Open excavation tasks

- field-by-field IPv4 RFC 791 → later updates matrix;
- UDP RFC 768 → RFC 9868 checksum update genealogy;
- ICMP RFC 792 message-type afterlife/deprecation matrix;
- ARP implementation source history across BSD, SunOS, Linux and embedded stacks;
- TCP RFC 793 → 9293 normative diff;
- DNS 1034/1035 extension graph;
- SMTP 821 → 2821 → 5321 command/reply diff;
- RFC 822 → 2822 → 5322 syntax diff;
- MIME 1341/1521/2045 family revision genealogy;
- identify which 1980s packet fields are still byte-for-byte recognizable in captures today.