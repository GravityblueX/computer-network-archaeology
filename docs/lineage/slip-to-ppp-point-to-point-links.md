# SLIP → PPP: when “put IP on a serial line” became a negotiated link protocol

> **Lineage question:** how did a tiny framing convention for IP over serial lines turn into a general, negotiated, multi-protocol point-to-point link architecture?

This is another case where the modern descendant solves a much larger problem than the older mechanism.

---

## 1. SLIP solves the smallest possible problem

RFC 1055, June 1988, is unusually candid even in its title:

> *A Nonstandard for Transmission of IP Datagrams over Serial Lines: SLIP*

Primary source:

- RFC 1055 — https://www.rfc-editor.org/rfc/rfc1055.html

The problem is simple:

```text
IP datagram
    ↓
serial byte stream
```

A serial line does not inherently tell the receiver where one IP packet ends and the next begins.

SLIP therefore supplies framing around IP datagrams.

Its historical attraction is precisely its minimalism.

---

## 2. The minimalism is also the limitation

SLIP does **not** attempt to become a complete negotiated link layer.

The historical design leaves many things outside the protocol:

- no protocol type for carrying arbitrary network protocols;
- no built-in link configuration negotiation;
- no authentication framework;
- no automatic negotiation of network-layer parameters;
- limited error-detection responsibility at the framing layer;
- no standard mechanism for negotiating addresses or compression.

This made SLIP easy to implement, especially in Unix and personal-computer networking environments, but difficult to generalize into a universal point-to-point data-link standard.

The correct historical lesson is not “SLIP was primitive.”

It was deliberately small.

---

## 3. PPP is proposed as a broader architecture

RFC 1134, November 1989, is titled:

> *Point-to-Point Protocol: A Proposal for Multi-Protocol Transmission of Datagrams Over Point-to-Point Links*

Primary source:

- RFC 1134 — https://www.rfc-editor.org/rfc/rfc1134.html

Already in the title, PPP expands the problem:

```text
not only IP
      ↓
multiple network-layer protocols
      ↓
one generic point-to-point link framework
```

PPP is therefore better understood as a **generalization of the point-to-point link problem**, not merely “SLIP version 2”.

---

## 4. PPP separates link establishment from network-layer configuration

A key architectural move is modular negotiation.

The canonical PPP model becomes:

```text
physical / serial / point-to-point link
          ↓
framing
          ↓
LCP — Link Control Protocol
          ↓
optional authentication / link features
          ↓
NCP — Network Control Protocols
          ↓
IP or other network-layer protocol
```

This is much more structured than SLIP's “frame IP datagrams on a byte stream.”

### LCP

LCP negotiates and manages the data-link connection.

### NCPs

Different network-layer protocols can have their own configuration protocols.

For IP, IPCP later configures IP-specific parameters.

This architecture means the link can negotiate **how it works** before a particular network-layer protocol becomes operational.

---

## 5. The PPP revision chain is long and should remain revision-specific

The core standards genealogy is unusually well documented:

```text
RFC 1134 (1989)
    ↓ obsoleted by
RFC 1171 (1990)
    ↓ obsoleted by
RFC 1331 (1992)
    ↓ obsoleted by
RFC 1548 (1993)
    ↓ obsoleted by
RFC 1661 (1994)
```

Primary sources:

- RFC 1134 — https://www.rfc-editor.org/rfc/rfc1134.html
- RFC 1171 — https://www.rfc-editor.org/rfc/rfc1171.html
- RFC 1331 — https://www.rfc-editor.org/rfc/rfc1331.html
- RFC 1548 — https://www.rfc-editor.org/rfc/rfc1548.html
- RFC 1661 — https://www.rfc-editor.org/rfc/rfc1661.html

Do not treat all of these as interchangeable copies of “PPP”.

Version-level protocol archaeology belongs in the archive.

---

## 6. PPP framing has its own revision lineage

The PPP core and PPP framing specifications are not the same document family.

For HDLC-like framing:

```text
RFC 1549 (1993)
    ↓ obsoleted by
RFC 1662 (1994)
```

Primary sources:

- RFC 1549 — https://www.rfc-editor.org/rfc/rfc1549.html
- RFC 1662 — https://www.rfc-editor.org/rfc/rfc1662.html

RFC 1549 explicitly covers synchronous and asynchronous point-to-point links, including octet-oriented serial links, and uses HDLC as a basis.

This is important because “PPP” is really a family of cooperating specifications:

```text
PPP architecture / LCP
PPP framing
network-control protocols
authentication protocols
compression / multilink / later extensions
```

---

## 7. SLIP → PPP is not a formal revision edge

RFC 1134 does not obsolete RFC 1055 as a direct formal revision.

The relationship should therefore be modeled carefully.

Better:

```text
SLIP point-to-point IP framing role
        ↓ broader successor role
PPP negotiated multi-protocol point-to-point framework
```

Not:

```text
SLIP
  ↓ revision-of
PPP
```

This distinction is exactly why the repository has a lineage vocabulary.

---

## 8. PPP adds negotiation as a first-class network behavior

SLIP assumes external configuration.

PPP makes negotiation part of the link.

This changes operations substantially.

Instead of an administrator or dialer simply assuming both ends agree, PPP can establish a conversation about link parameters.

That design pattern survives widely in networking:

> before carrying normal traffic, peers negotiate capabilities and configuration state.

The archive should not claim PPP invented negotiation as a general idea, but it is a strong example of negotiated link configuration becoming normal in Internet access.

---

## 9. Authentication becomes part of the point-to-point access layer

PPP provides hooks for authentication protocols such as PAP and CHAP.

This matters historically because the serial point-to-point link is no longer merely a wire between two machines.

In dial-up service it becomes a **subscriber access boundary**.

The stack can now look like:

```text
telephone call / modem link
       ↓
serial connection
       ↓
PPP framing + LCP
       ↓
PAP or CHAP
       ↓
IPCP
       ↓
subscriber IP traffic
```

That path connects directly to the terminal-server / PortMaster / RADIUS excavations elsewhere in the repository.

---

## 10. The user endpoint becomes a real IP host

This is one of the biggest historical shifts in the remote-access lineage.

Older terminal access:

```text
terminal
  ↓ character stream
TIP / PAD / terminal server
  ↓
remote host performs computing/network protocol work
```

Dial-up IP with SLIP/PPP:

```text
PC / workstation runs TCP/IP itself
        ↓
SLIP or PPP point-to-point link
        ↓
access server / router
        ↓
Internet
```

The edge device changes from “terminal session adapter” toward “network-layer access concentrator”.

PPP helps make this transition operationally manageable.

---

## 11. Why PPP outlived dial-up modems

PPP should not be reduced to “the dial-up Internet protocol.”

Its architecture was reused across many point-to-point contexts.

The broader lineage includes later environments such as:

- synchronous serial WAN links;
- ISDN-related access;
- PPP over Ethernet (PPPoE);
- PPP over ATM and broadband access architectures;
- cellular modem/data contexts using PPP in some generations.

Those later branches require their own evidence records.

The important inherited abstraction is:

```text
point-to-point bearer
      ↓
framing + link negotiation
      ↓
authentication / configuration
      ↓
network-layer protocol
```

---

## 12. What survives and what dies

### SLIP properties that survive conceptually

- serial point-to-point IP access;
- simple framing around network-layer packets;
- use in dial-up and directly connected serial environments.

### SLIP mechanisms that do not become the PPP core

- SLIP's specific framing convention;
- IP-only assumption;
- external/manual configuration assumptions.

### PPP additions that become durable

- explicit protocol multiplexing;
- LCP negotiation;
- per-network-protocol configuration;
- authentication integration;
- modular extension architecture.

---

## 13. Sources

Primary sources:

- RFC 1055 — SLIP — https://www.rfc-editor.org/rfc/rfc1055.html
- RFC 1134 — early PPP proposal — https://www.rfc-editor.org/rfc/rfc1134.html
- RFC 1171 — PPP revision — https://www.rfc-editor.org/rfc/rfc1171.html
- RFC 1331 — PPP revision — https://www.rfc-editor.org/rfc/rfc1331.html
- RFC 1548 — PPP revision — https://www.rfc-editor.org/rfc/rfc1548.html
- RFC 1661 — PPP Internet Standard — https://www.rfc-editor.org/rfc/rfc1661.html
- RFC 1549 — PPP in HDLC framing — https://www.rfc-editor.org/rfc/rfc1549.html
- RFC 1662 — PPP in HDLC-like framing — https://www.rfc-editor.org/rfc/rfc1662.html

---

## 14. Next excavation layer

1. SLIP implementation archaeology in BSD/Sun/KA9Q/PC stacks;
2. CSLIP / Van Jacobson TCP header-compression branch;
3. PPP RFC 1134 → 1171 → 1331 → 1548 → 1661 clause/state-machine diff;
4. PAP and CHAP genealogy;
5. IPCP history and IP-address negotiation;
6. Multilink PPP;
7. modem → PPP dialer scripts and chat programs;
8. PortMaster/Ascend/Cisco PPP implementation behavior;
9. PPPoE and broadband access as a later branch;
10. surviving packet captures/configuration manuals from 1990s ISP POPs.

---

## Conclusion

SLIP answered:

> **How do I delimit IP datagrams on a serial line?**

PPP answered a larger question:

> **How do two endpoints create, negotiate, authenticate, configure, and operate a general network link over a point-to-point bearer?**

That expansion of responsibility is the real lineage.