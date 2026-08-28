# From the Internet Transmission Control Program to IP + TCP

Modern readers normally encounter **IP** and **TCP** as separate layers.

That separation is itself a historical result.

The early internetworking design did not begin with the exact modern division of responsibility. The surviving specifications show a multi-year process in which internetwork delivery functions and reliable host-to-host transport were progressively separated, revised and standardized.

This chapter treats that split as a technical genealogy rather than jumping directly from the 1974 Cerf/Kahn work to RFC 791/793.

---

## 1. December 1974: one Internet Transmission Control Program

RFC 675, by Vinton Cerf, Yogen Dalal and Carl Sunshine, is titled:

> **Specification of Internet Transmission Control Program**

and is explicitly the **December 1974 version**.

Canonical source:

https://www.rfc-editor.org/rfc/rfc675.html

The document describes an internetwork **Transmission Control Program (TCP)** and its interface to applications/users.

The terminology is historically important:

```text
application / user process
          ↓
Internet Transmission Control Program
          ↓
underlying packet networks + gateways
```

Do not project the later IP/TCP split into this document as if it already existed in its final form.

The artifact here is a **combined internetwork transmission-control architecture** whose responsibilities were still being reorganized.

---

## 2. The later TCP specification remembers its own revision tree

RFC 761, *DoD Standard Transmission Control Protocol* (January 1980), is unusually valuable because the title page preserves its ancestry.

It identifies itself as:

- RFC 761;
- IEN 129;
- replacing IENs **124, 112, 81, 55, 44, 40, 27, 21, 5**.

Canonical source:

https://www.rfc-editor.org/rfc/rfc761.html

Its preface says that there had been **eight earlier editions of the ARPA TCP specification** on which the standard was based.

That gives the repository a formal revision spine even before every IEN has been individually mined.

```text
IEN 5
  ↓
IEN 21
  ↓
IEN 27
  ↓
IEN 40
  ↓
IEN 44
  ↓
IEN 55
  ↓
IEN 81
  ↓
IEN 112
  ↓
IEN 124
  ↓
IEN 129 / RFC 761 (Jan 1980)
```

The next excavation should recover each IEN and produce a responsibility/field diff rather than merely preserving the numbers.

---

## 3. By 1980, TCP explicitly sits above a separate Internet Protocol

RFC 761 states that TCP fits into a layered protocol architecture **just above a basic Internet Protocol**.

It describes IP as the mechanism that provides Internet datagram envelopes, addressing across networks, and fragmentation/reassembly needed to cross different networks and gateways.

This is the genealogy pivot:

```text
1974 integrated Internet Transmission Control Program
                  ↓ repeated redesign
          internetwork delivery functions
                  ↓ separated into
             Internet Protocol
                  +
       reliable host-to-host TCP
```

The separation is not cosmetic.

It moves responsibilities into distinct modules:

### Internet Protocol side

- source/destination Internet addressing;
- datagram delivery across interconnected networks;
- fragmentation/reassembly;
- routing through gateways at the internetwork layer;
- protocol demultiplexing field;
- best-effort service.

### TCP side

- reliable host-to-host byte-stream service;
- sequencing;
- acknowledgements;
- retransmission;
- flow control;
- connection state;
- application-facing transport service.

That division became one of the deepest architectural fossils of the modern Internet.

---

## 4. RFC 760: IP has its own independent revision lineage

RFC 760, *DoD Standard Internet Protocol* (January 1980), also preserves an explicit ancestry.

Canonical source:

https://www.rfc-editor.org/rfc/rfc760.html

It identifies itself as:

- RFC 760;
- IEN 128;
- replacing IENs **123, 111, 80, 54, 44, 41, 28, 26**.

Its preface says it is based on **five earlier editions of the ARPA Internet Protocol Specification**.

This gives IP a parallel revision tree:

```text
IEN 26 / 28 / 41 / 44 / 54 / 80 / 111 / 123
                       ↓
              IEN 128 / RFC 760
                       ↓
                   RFC 791
```

Note that IEN 44 appears in both the TCP and IP ancestry lists. That is exactly the kind of detail that deserves excavation: it may preserve a stage in which responsibilities or document organization were still being split/recast.

Do not infer the exact meaning from the number alone; recover IEN 44 itself.

---

## 5. The 1980 IP specification is explicitly best effort

RFC 760 gives a very clear statement of IP's scope.

It says the Internet Protocol does **not** provide a reliable communication facility:

- no end-to-end acknowledgements;
- no hop-by-hop acknowledgements as an IP service;
- no retransmissions;
- no flow control;
- data errors are not repaired by IP;
- header integrity is checked separately.

That is a major lineage fact.

Reliability has been moved upward rather than embedded in internetwork forwarding.

A useful property-level edge is therefore:

```text
integrated early TCP responsibilities
           ↓ split / responsibility migration
IP: best-effort datagram delivery
TCP: end-to-end reliability and flow control
```

This is more precise than saying merely “TCP/IP was invented.”

---

## 6. September 1981: RFC 791 and RFC 793 stabilize the familiar pair

### RFC 791 — Internet Protocol

Canonical source:

https://www.rfc-editor.org/rfc/rfc791.html

The preface says the document is based on **six earlier editions of the ARPA Internet Protocol Specification** and revises addressing, error handling, option codes and security/precedence-related details.

It replaces RFC 760.

### RFC 793 — Transmission Control Protocol

Canonical source:

https://www.rfc-editor.org/rfc/rfc793.html

The preface says there had been **nine earlier editions of the ARPA TCP specification**.

It replaces RFC 761 / IEN 129 and lists the earlier IEN lineage.

So the standards genealogy becomes:

```text
1974 RFC 675 / integrated TCP concept
        |
        | repeated IEN development
        |
        +---------------------------+
        |                           |
 Internet Protocol line       Transmission Control line
        |                           |
 IEN 128 / RFC 760          IEN 129 / RFC 761
        |                           |
    RFC 791                     RFC 793
        |                           |
        +------------+--------------+
                     |
              operational TCP/IP
```

The tree should eventually be replaced by a braid of exact version-level edges.

---

## 7. The split is also a software-architecture change

Protocol text is only one layer.

A host implementation now needs distinguishable modules/interfaces:

```text
application
    ↓
TCP module
    ↓
IP module
    ↓
local-network module
    ↓
Ethernet / ARPANET / packet radio / satellite / other network
```

RFC 760 illustrates this modularity directly: an Internet module can pass a datagram to a local-network interface, which then wraps it in the appropriate local-network header. For ARPANET, the local-network module can add an 1822 leader and deliver it to the IMP.

This is a crucial internetworking principle:

> the Internet datagram is not the same thing as the local network packet/message that carries it.

That separation is one reason IP could cross heterogeneous networks.

---

## 8. TCP/IP standardization did not immediately mean universal deployment

The existence of RFC 791/793 in September 1981 did not instantly replace NCP on every ARPANET host.

RFC 801, *NCP/TCP Transition Plan* (November 1981), shows the deployment/migration layer:

https://www.rfc-editor.org/rfc/rfc801.html

It required:

- implementation work at each host organization;
- TCP-based Telnet/FTP/mail services;
- dual-protocol hosts;
- relay services between old and new environments;
- progressive conversion through 1982;
- NCP removal and full Internet service in January 1983.

The complete genealogy is therefore:

```text
design lineage
RFC 675 → IEN revisions → IP/TCP split → RFC 760/761 → RFC 791/793

                         ↓ deployment

operational lineage
NCP hosts → dual-protocol period → TCP/IP hosts → NCP removed
```

Specification genealogy and deployment genealogy are related but different objects.

---

## 9. Application protocols also cross the boundary

RFC 801 explains that the principal services had to be available on the new IP/TCP base.

### Telnet

The user-visible role continues, but protocol details change. RFC 801 specifically notes that the old Initial Connection Protocol mechanism disappears and NCP Interrupt is replaced with TCP Urgent mechanisms.

### FTP

The service continues, but protocol details are revised for the TCP environment.

### Mail

Mail changes more dramatically: it is separated from the old FTP/NCP mail procedure and moves toward a distinct mail server/protocol environment.

Therefore the transition contains multiple lineage types:

- `replaced-by` at the host-protocol base;
- `role-descends-into` at the application-service layer;
- `revision-of` for protocol documents;
- `coexisted-with` during the dual-protocol migration window.

A single arrow cannot capture all of it.

---

## 10. What survived into the modern Internet?

### IP fossils that remain recognizable

- best-effort datagram delivery;
- source/destination addressing;
- protocol demultiplexing;
- TTL/hop-limiting ancestry;
- fragmentation/reassembly history;
- local-network independence;
- gateways/routers forwarding between networks.

### TCP fossils that remain recognizable

- reliable ordered delivery;
- sequence numbers;
- acknowledgements;
- retransmission;
- flow-control windows;
- connection state;
- ports/socket-oriented application multiplexing lineage.

### What changed substantially later

- congestion control;
- routing architecture;
- addressing/classful assumptions;
- options use;
- security mechanisms;
- implementation APIs;
- hardware offload;
- scale of routing and host populations.

The 1981 specifications are ancestors, not frozen descriptions of today's implementations.

---

## 11. Open excavation targets

### Recover the Internet Experiment Notes

The strongest next move is to register and mine every cited IEN:

#### TCP line

- IEN 5
- IEN 21
- IEN 27
- IEN 40
- IEN 44
- IEN 55
- IEN 81
- IEN 112
- IEN 124
- IEN 129 / RFC 761

#### IP line

- IEN 26
- IEN 28
- IEN 41
- IEN 44
- IEN 54
- IEN 80
- IEN 111
- IEN 123
- IEN 128 / RFC 760

For each version record:

- header format changes;
- addressing changes;
- fragmentation responsibilities;
- connection-state changes;
- acknowledgement behavior;
- port/socket semantics;
- gateway behavior;
- checksums;
- retransmission timers;
- flow control;
- security/precedence fields;
- implementation compatibility.

### Recover source code by version

Protocol genealogy becomes much stronger when paired with implementations.

Targets include:

- Stanford TCP implementations;
- BBN TCP implementations;
- TENEX/TOPS-20 stacks;
- Unix/BSD early TCP/IP trees;
- Fuzzball TCP/IP;
- gateway code;
- packet-radio and SATNET implementations.

### Connect the split to APIs

A later genealogy should trace:

```text
protocol module interfaces
       ↓
BSD networking implementation
       ↓
sockets API
       ↓
portable application expectations
```

That is a different lineage from packet-format revision and deserves separate edges.

---

## Primary sources

- RFC 675, *Specification of Internet Transmission Control Program* (December 1974): https://www.rfc-editor.org/rfc/rfc675.html
- RFC 760 / IEN 128, *DoD Standard Internet Protocol* (January 1980): https://www.rfc-editor.org/rfc/rfc760.html
- RFC 761 / IEN 129, *DoD Standard Transmission Control Protocol* (January 1980): https://www.rfc-editor.org/rfc/rfc761.html
- RFC 791, *Internet Protocol* (September 1981): https://www.rfc-editor.org/rfc/rfc791.html
- RFC 793, *Transmission Control Protocol* (September 1981): https://www.rfc-editor.org/rfc/rfc793.html
- RFC 801, *NCP/TCP Transition Plan* (November 1981): https://www.rfc-editor.org/rfc/rfc801.html

## Current conclusion

The modern phrase **TCP/IP** hides an important historical transformation.

The Internet architecture did not begin with a perfectly separated IP layer and TCP layer. The surviving RFC/IEN genealogy records a period of repeated redesign in which internetwork datagram delivery was separated from reliable host-to-host transport, both lines accumulated their own revisions, and the resulting standards were then deployed through a staged operational migration.

In other words:

> **layering itself has a history.**

That history belongs in the archive just as much as the packet formats.