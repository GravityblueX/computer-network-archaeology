# Protocol Record Template

> Create separate records for materially different protocol versions. A protocol family is not one timeless object.

## Identity

- **Contemporary name:**
- **Common later name:**
- **Version / edition:**
- **Date proposed:**
- **Date documented:**
- **Date first implemented:**
- **Date deployed:**
- **Date standardized:**
- **Date retired / made historic:**
- **Author(s) / body:**
- **Defining document(s):**
- **Predecessor:**
- **Successor:**

## Problem statement

What concrete contemporary problem was this protocol designed to solve?

## Assumed environment

- endpoint type:
- network type:
- lower-layer service:
- reliability assumption:
- ordering assumption:
- MTU / message-size assumptions:
- connection-oriented or connectionless:
- centralized or distributed state:

## Architecture

Explain where protocol state lives and which entity is responsible for reliability, routing, naming, congestion, retransmission and recovery.

```text
application / user
  ↓
...
  ↓
physical network
```

## Addressing / identifiers

- endpoint identifiers:
- network identifiers:
- connection/socket/port identifiers:
- broadcast/multicast concepts:
- allocation authority:

## Packet / frame / message format

Preserve fields in contemporary order and units.

| Field | Width | Meaning | Notes |
|---|---:|---|---|
| | | | |

Do not silently translate unusual historical units/word sizes into modern byte assumptions.

## State machine

- connection setup:
- normal transfer:
- acknowledgement:
- timeout:
- retransmission:
- close/reset:
- error states:

## Flow and congestion control

- sender window/credit:
- receiver flow control:
- network feedback:
- congestion mechanism:
- fairness assumptions:

## Error handling

- checksum/FCS:
- corruption:
- packet loss:
- duplication:
- reordering:
- fragmentation/reassembly:
- reset/recovery:

## Routing / forwarding interaction

If applicable:
- route computation:
- metric:
- update mechanism:
- loops:
- convergence:
- policy:

## Timing

- timers:
- retransmission values:
- keepalive:
- clock assumptions:

## Security / trust model

Describe what the original protocol assumed, even if the answer is effectively “trusted network/users”. Avoid judging it only by modern threat models.

## Specification genealogy

| Date | Document | Change | Status |
|---|---|---|---|
| | | | |

## Implementations

| Implementation | Platform/OS | Date | Evidence | Notes |
|---|---|---:|---|---|
| | | | | |

Implementation source code belongs historically here as evidence; runnable reconstruction belongs primarily in `protocol-zoo`.

## Interoperability evidence

- demonstrations:
- plugfests/tests:
- cross-vendor deployment:
- known incompatibilities:

## Deployment

- networks using it:
- organizations:
- scale:
- peak period:
- coexistence with competing protocols:

## Operational problems

Preserve real incidents, performance failures, unexpected traffic patterns and administrator workarounds.

## Why it made sense then

Explain contemporary line cost, CPU/RAM limits, carrier assumptions, institutional constraints and installed base.

## Why it changed / declined

Avoid “better protocol won” shorthand. Separate:
- technical limitations;
- implementation availability;
- vendor support;
- regulation/procurement;
- installed base;
- economics;
- standardization politics;
- migration costs.

## Descendants / concepts that survived

Even dead protocols may leave lasting ideas, field formats, terminology, APIs or architecture.

## Primary sources

- specifications:
- implementation source:
- test reports:
- operator manuals:
- mailing lists/meeting notes:

## Secondary sources

- scholarship:
- oral histories:

## Source conflicts / unresolved questions

## Research status

`seed | started | substantially documented | needs primary verification | blocked`

## Last reviewed

- date:
- reviewer/agent:
