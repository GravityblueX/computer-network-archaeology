# Interdomain Routing Lineage: GGP → EGP → BGP

Modern BGP makes little sense if it is introduced as "the Internet routing protocol" without recovering the architecture it replaced.

The key historical transition is not simply one routing algorithm replacing another. It is the Internet changing from a relatively small collection of gateways expected to participate in a common routing regime into a federation of independently administered **autonomous systems**.

This file connects three important generations:

```text
GGP / common core-gateway routing
          ↓ architectural scaling problem
EGP / autonomous-system boundary routing
          ↓ policy and topology limitations
BGP / path-vector interdomain routing
```

The arrows are not all the same kind. GGP did not "revise into" EGP, and EGP did not simply become BGP. The administrative model of the network changed along the way.

## 1. The earlier Internet gateway model

Early DARPA Internet gateways were heterogeneous packet-forwarding computers connecting networks such as ARPANET, packet-radio networks, satellite networks and local networks.

RFC 823 (1982) documents one concrete BBN gateway generation and its network interfaces.

Within the early gateway system, Gateway-to-Gateway Protocol (GGP) was used among the "smart" core gateways to exchange routing information.

RFC 890 later describes the situation explicitly: smart gateways dynamically exchanged routing information among themselves using GGP, while "dumb" gateways required manual routing-table entries in the smart gateways.

This is important because GGP belongs to a relatively centralized architectural moment.

## 2. Why one common routing system stopped scaling

RFC 827 (October 1982) is unusually explicit about the problem.

As the Internet grew, adding radically different gateway implementations directly into one common routing algorithm became difficult because:

- routing overhead increased;
- heterogeneous gateway implementations made maintenance and fault isolation harder;
- changes to the common routing algorithm required coordination across too many gateways and organizations;
- one integrated gateway system became operationally rigid.

The proposed answer was institutional as much as algorithmic.

The Internet would evolve into separate **domains or autonomous systems**, each with its own internal routing procedures.

That change is the key ancestor of today's interdomain-routing architecture.

## 3. EGP creates an explicit autonomous-system boundary

The Exterior Gateway Protocol was designed to exchange reachability information across autonomous-system boundaries.

RFC 827 is the 1982 draft. RFC 888 (January 1984) describes the working Stub EGP. RFC 904 (April 1984) is the formal EGP specification for the DARPA community.

RFC 890 provides the operational transition schedule and describes the intended architecture:

```text
Autonomous System A
  internal routing
       ↓
 border gateway
       ↕ EGP
 core / other autonomous system
       ↕ EGP
 border gateway
       ↓
Autonomous System B
  internal routing
```

The central architectural separation is:

- **interior routing** can differ between autonomous systems;
- **exterior routing** provides controlled exchange between administrations.

This is one of the most important institutional abstractions in Internet history.

## 4. "Autonomous system" is not just a field in a packet

In modern textbooks, an AS number can look like merely another protocol field.

Historically, the autonomous-system concept solved a coordination problem.

It made it possible for organizations to:

- operate different internal routing algorithms;
- deploy different gateway software;
- change internal architecture without modifying every gateway in the Internet;
- exchange only the information needed at administrative boundaries.

The architecture therefore decomposed a technical problem according to organizational ownership.

That pattern survives throughout the modern Internet.

## 5. The 1984 GGP → EGP transition was operational policy

RFC 890 is especially useful because it records not merely a specification but a planned deployment transition.

It describes:

1. replacing "dumb" gateways with at least Stub EGP capability;
2. factoring the existing smart-gateway environment into autonomous systems;
3. retaining a large core autonomous system during transition;
4. moving toward richer connectivity among autonomous systems.

The memo states that after 1 August 1984 there should be no dumb gateways in the Internet and that gateways should belong to autonomous systems.

This should be recorded as a deployment/operations event, not merely a protocol publication date.

## 6. EGP's architecture was still constrained

EGP established the autonomous-system boundary but was not a modern general path-vector protocol.

Its reachability model was closely tied to the Internet topology and operational assumptions of its period.

As the Internet became less core-centric and policy relationships between autonomous systems became more complicated, a richer protocol was needed.

This is where BGP enters.

## 7. BGP-1 inherited the AS boundary but changed route information

RFC 1105 (1989) defines BGP-1.

Its historical significance includes:

- routing between autonomous systems;
- use of TCP (port 179) rather than building transport reliability into the routing protocol itself;
- explicit path information associated with reachable networks;
- real implementations noted in Cisco routers and the NSFNET Nodal Switching System.

BGP therefore belongs to the autonomous-system architecture introduced during the EGP era, but provides a different route-information and policy mechanism.

This relationship is best encoded as:

```text
EGP experience / AS architecture
           ↓ documented influence / replacement pressure
BGP-1
```

not as `revision-of`.

## 8. BGP versions become a formal protocol lineage

Unlike GGP→EGP or EGP→BGP, the BGP version chain itself is explicit:

```text
BGP-1  RFC 1105 (1989)
  ↓
BGP-2  RFC 1163 (1990)
  ↓
BGP-3  RFC 1267 (1991)
  ↓
BGP-4  RFC 1771 (1995)
```

RFC 1771 itself refers to RFCs 1105, 1163, 1267 and 1771 as BGP versions 1 through 4.

This makes the BGP series a good example of a strong formal lineage.

## 9. BGP-4 intersects with CIDR

BGP-4's most important change cannot be understood entirely inside the BGP specification.

The early 1990s Internet faced two related scaling problems:

- exhaustion/inefficiency of classful IPv4 address allocation;
- explosive growth in global routing-table entries.

CIDR changed route representation from implicit class A/B/C network sizes to arbitrary address prefixes and masks.

RFC 1519 describes the need for interdomain routing to carry network+mask information and support aggregation.

BGP-4 then carried classless prefixes and route aggregation.

So the genealogy is a cross-standard intersection:

```text
classful Internet routing
        ↓ scaling pressure
CIDR address/prefix architecture
        ↘
         BGP-4 classless route advertisement
        ↗
BGP version lineage
```

This is precisely the kind of relationship that a simple chronological timeline obscures.

## 10. What survived from the GGP/EGP era

### Autonomous systems

The explicit administrative-routing domain is one of the strongest surviving ideas.

### Interior versus exterior routing

The division remains fundamental:

- IGPs manage routing within an AS;
- BGP manages routing relationships across AS boundaries.

### Operational autonomy

Different networks can change internal topology and routing implementation while preserving an external routing contract.

### Gateway/router operations as an administrative system

Routing has always involved more than shortest-path computation. Fault isolation, policy, configuration ownership and inter-organizational coordination were already visible in the transition away from one common core-gateway routing regime.

## 11. What changed dramatically

- GGP's common core routing world largely disappeared.
- EGP's core-centric reachability assumptions did not scale into the commercial Internet.
- BGP evolved from network-reachability exchange into the policy-bearing global routing system.
- classful route assumptions disappeared under CIDR.
- the number of independently administered networks increased by orders of magnitude.
- routing policy became an explicit business and security surface.

## 12. A genealogy of abstractions

```text
common gateway routing system
      ↓ scaling + operational heterogeneity
separate autonomous systems
      ↓
interior routing / exterior routing split
      ↓ EGP
AS-boundary reachability exchange
      ↓ topology + policy scaling
BGP path-vector family
      ↓ BGP-4 + CIDR
classless policy-rich interdomain routing
```

The important ancestor is not merely an old packet format. It is the decision to align routing architecture with administrative domains.

## 13. Artifacts that need separate records

The repository should avoid one generic `EGP` or `BGP` object swallowing the whole story.

High-value separate artifacts include:

- GGP as implemented in BBN/core gateways;
- RFC 827 draft EGP;
- RFC 888 Stub EGP;
- RFC 904 formal EGP;
- the August 1984 EGP operational transition;
- autonomous-system number administration;
- BGP-1, BGP-2, BGP-3, BGP-4;
- Cisco BGP-1 implementation;
- NSFNET NSS BGP-1 implementation;
- gated BGP implementations;
- route servers;
- early Internet exchange-point BGP deployments;
- CIDR deployment events;
- BGP-4 RFC 1771 implementation generation;
- RFC 4271 specification generation while retaining the protocol name BGP-4.

## 14. Source-code archaeology targets

Specifications tell only part of the routing story.

The following implementation evidence would materially improve the archive:

- BBN GGP gateway source;
- NSFNET NSS routing-control source and policy databases;
- early Cisco BGP code/documentation where legally preservable;
- `gated` releases implementing EGP/BGP;
- early BGP-4 test suites and interoperability reports;
- MRT routing table dumps and route-server archives;
- operator configuration examples and incident reports.

## 15. Operations are part of the lineage

For each generation, the archive should ask:

- Who assigned identifiers?
- Who could change routing policy?
- How were neighbor relationships configured?
- What monitoring tools existed?
- How were bad routes withdrawn?
- What happened when an autonomous system became unreachable?
- How were software upgrades coordinated?
- What failures produced the next protocol change?

Routing protocols evolve because networks fail and organizations change, not only because protocol designers prefer new packet formats.

## 16. Evidence anchors

- RFC 823 (1982): concrete DARPA gateway implementation and GGP context.
- RFC 827 (1982): why a common gateway-routing system became operationally difficult and why autonomous systems were proposed.
- RFC 888 (1984): Stub EGP.
- RFC 890 (1984): official EGP implementation schedule and transition from smart/dumb gateway environment to autonomous systems.
- RFC 904 (1984): formal EGP specification.
- RFC 1105 (1989): BGP-1.
- RFC 1163 (1990): BGP-2.
- RFC 1267 (1991): BGP-3.
- RFC 1771 (1995): BGP-4.
- RFC 1519 (1993): CIDR architecture and interdomain route aggregation requirements.
- RFC 4271 (2006): later core BGP-4 specification that obsoletes RFC 1771 without changing the protocol's major-version name.

## 17. Next digs

1. Recover GGP packet format and BBN routing-table structures from RFC 823 and source code.
2. Build RFC 827 → 888 → 904 EGP field/state-machine diff.
3. Track autonomous-system-number format and allocation history.
4. Recover the actual August 1984 EGP deployment state from gateway tables/logs.
5. Reconstruct BGP-1 on one Cisco router and one NSFNET NSS node.
6. Build BGP-1/2/3/4 attribute/message diffs.
7. Connect BGP-4 to concrete early CIDR deployment prefixes and routing-table size changes.
8. Recover early `gated` source releases supporting EGP/BGP.
9. Follow BGP into route reflectors, confederations, communities and multiprotocol extensions as later lineage branches.
10. Preserve operational incidents that changed BGP practice even when the base protocol version did not change.

Modern BGP is therefore not merely the fourth version of one protocol. It sits on top of a much older decision: **the Internet should be a network of independently administered routing domains rather than one centrally coordinated gateway system.**
