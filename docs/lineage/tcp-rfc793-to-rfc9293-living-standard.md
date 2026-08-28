# TCP RFC 793 → RFC 9293: How a 1981 Protocol Stayed Alive

TCP is a useful warning against equating **protocol age** with **document age**.

The protocol standardized in RFC 793 in September 1981 is still recognizably TCP today: sequence numbers, acknowledgments, ports, a stateful connection model, retransmission, flow control, SYN/FIN/RST semantics, and a byte-stream abstraction remain central.

But RFC 793 itself is no longer the current normative TCP specification.

In August 2022, RFC 9293 formally obsoleted RFC 793 and several later RFCs, consolidating decades of corrections and updates into a new Internet Standard text.

Primary record:

- RFC 9293: https://www.rfc-editor.org/info/rfc9293/

---

## 1. The wrong story

A misleading timeline would be:

```text
1981 TCP
  ↓
modern TCP
```

as though nothing happened in between.

Another misleading timeline would be:

```text
RFC 793
  ↓ obsolete
TCP disappeared
```

The actual history is closer to:

```text
RFC 793 functional specification
      ↓
implementation experience
      ↓
congestion collapse and congestion control
      ↓
RTO/RFC requirement corrections
      ↓
security hardening
      ↓
ECN and control-bit evolution
      ↓
errata + host requirements + interoperability practice
      ↓
RFC 9293 consolidated TCP specification
```

The protocol identity survives by repeated repair.

---

## 2. What RFC 9293 says about its own ancestry

RFC 9293 explicitly describes TCP as a protocol that has **continuously evolved over decades of use and Internet growth**.

It says that changes to RFC 793 had accumulated piecemeal and that RFC 9293 brings those changes together with the original protocol specification.

Most strikingly, the document states that its main body was adapted from Section 3 of RFC 793 — the functional specification — while attempting to keep formatting and layout close to the original.

That is unusually strong documentary evidence for a living technical lineage.

This is not merely:

> modern TCP was inspired by RFC 793.

It is closer to:

> the current TCP standard is a revised compilation of the RFC 793 protocol lineage.

---

## 3. What survived from the early TCP identity

The following architectural properties remain immediately recognizable:

- connection-oriented byte stream;
- ordered sequence space;
- acknowledgments;
- retransmission after loss;
- port-number multiplexing;
- connection establishment using SYN;
- orderly close using FIN;
- reset semantics using RST;
- sender/receiver window-based flow control;
- pseudo-header checksum relationship to IP addresses/protocol identity;
- TCP state machine;
- Maximum Segment Size negotiation lineage.

These are not incidental naming similarities. They are the skeleton of the same protocol family.

---

## 4. What could not remain frozen

### Congestion control

RFC 793 did not contain the congestion-control algorithms now associated with production TCP.

The 1980s congestion-collapse experience showed that end-to-end reliability alone was not enough. Hosts could be individually correct while collectively destabilizing the network.

This archive tracks that separately in:

- `docs/lineage/tcp-congestion-collapse-jacobson.md`

The important genealogical rule is:

```text
TCP reliability machinery
          ≠
TCP congestion-control machinery
```

Congestion control is a later major branch that became essential to the living TCP implementation contract.

---

### Retransmission timers

RTO behavior was repeatedly refined because real networks exposed weaknesses in simplistic timing models.

This is another example where the packet/header identity survives while the operational algorithm changes dramatically.

---

### Security hardening

Sequence-number generation, reset handling, and other edge cases became security problems once TCP moved from a research network to a hostile global environment.

Later RFCs hardened behavior without creating a new transport protocol name.

---

### ECN and control bits

RFC 9293 notes that TCP control bits have been updated based on later specifications such as RFC 3168.

The header therefore remains historically continuous without being byte-for-byte semantically frozen in 1981.

---

## 5. Document genealogy is not protocol genealogy

RFC 9293 obsoletes:

- RFC 793;
- RFC 879;
- RFC 2873;
- RFC 6093;
- RFC 6429;
- RFC 6528;
- RFC 6691.

It also updates portions of other host-requirement/security documents.

This demonstrates why the archive must preserve two graphs:

```text
RFC document graph
```

and

```text
protocol mechanism graph
```

They overlap, but they are not identical.

A document can be obsoleted because its normative material was incorporated into a successor.

The mechanism can remain alive.

---

## 6. TCP as a sedimentary standard

A useful model is:

```text
1981 core
 + host requirements
 + operational failure lessons
 + congestion algorithms
 + security fixes
 + new control semantics
 + errata
 + interoperability clarifications
 = current TCP specification
```

This is closer to geology than replacement engineering.

A later engineer does not encounter one moment called "TCP". They encounter compressed historical layers.

---

## 7. What stayed outside the RFC 9293 consolidation

RFC 9293 deliberately does not absorb every informational story or every later TCP extension into one monolith.

That matters historically.

The archive should separately preserve:

- congestion-control algorithm families;
- SACK;
- timestamps;
- window scaling;
- ECN;
- TCP-AO / earlier MD5 protection;
- Fast Open;
- MPTCP as a related but separate extension architecture;
- implementation-specific algorithms (Tahoe, Reno, NewReno, CUBIC, BBR, etc.);
- socket API behavior, which is an implementation/interface genealogy rather than the wire protocol itself.

---

## 8. The 2022 standard still carries 1981 language in its bones

The historical importance of RFC 9293 is precisely that it does not pretend TCP was reinvented.

It documents continuity.

This gives the repository a strong category:

### `obsoleted-document-living-protocol`

Definition:

> the original standards document is formally superseded, but the protocol identity and major mechanisms survive through a successor specification that directly incorporates/revises the older normative material.

TCP RFC 793 → RFC 9293 is the reference example.

---

## 9. Contrast with UDP

UDP demonstrates a different form of durability.

RFC 768 itself remains an Internet Standard.

So:

```text
UDP:
old document + old protocol both remain normative anchors
```

while:

```text
TCP:
old document superseded
old protocol lineage continues through consolidated successor
```

Both are "old protocols still in use," but historically they survived differently.

---

## 10. Contrast with Ethernet

Ethernet gives yet another pattern:

```text
family name survives
frame/MAC lineage survives
physical medium changes
collision-domain model changes
full duplex eliminates normal CSMA/CD operation
```

So protocol/technology survival is multi-dimensional.

The repository should never reduce it to a binary `alive/dead` field.

---

## Primary sources

- RFC 793 — Transmission Control Protocol: https://www.rfc-editor.org/info/rfc793/
- RFC 9293 — Transmission Control Protocol (TCP): https://www.rfc-editor.org/info/rfc9293/
- RFC 1122 — Requirements for Internet Hosts — Communication Layers: https://www.rfc-editor.org/info/rfc1122/
- RFC 3168 — Explicit Congestion Notification: https://www.rfc-editor.org/info/rfc3168/

## Related archive excavations

- `tcp-ip-split-and-standardization.md`
- `tcp-congestion-collapse-jacobson.md`
- `udp-icmp-ip-companion-protocols.md`
- `living-standards-still-on-wire.md`

## Next excavation tasks

- create a clause/requirement diff RFC 793 → RFC 9293;
- map every RFC 9293 incorporated document to exact mechanism;
- map every held/accepted RFC 793 erratum incorporated into 9293;
- reconstruct TCP state-machine changes by revision;
- trace sequence-number security lineage;
- trace RTO lineage;
- trace window scaling/timestamps/SACK as branches;
- correlate BSD/Linux TCP source revisions with standards revisions;
- preserve packet captures demonstrating how much of the 1981 header remains directly recognizable.