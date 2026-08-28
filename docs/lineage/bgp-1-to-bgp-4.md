# BGP-1 → BGP-4: How Interdomain Routing Became Classless Policy Routing

The Border Gateway Protocol is often introduced to modern readers as if **BGP-4** were simply “BGP.”

Historically, the protocol went through several explicit public versions in only six years:

```text
BGP-1  RFC 1105   June 1989
   ↓
BGP-2  RFC 1163   June 1990
   ↓
BGP-3  RFC 1267   October 1991
   ↓
BGP-4  RFC 1771   March 1995
```

RFC 1771 itself states that RFC 1105 is commonly called BGP-1, RFC 1163 BGP-2, RFC 1267 BGP-3, and RFC 1771 BGP-4.

This is therefore a particularly strong protocol genealogy: the revision boundaries are explicit in the contemporary standards corpus.

---

## 1. Before BGP: EGP and the early Autonomous-System Internet

RFC 904, *Exterior Gateway Protocol Formal Specification* (April 1984), specifies EGP for exchanging reachability information between Internet gateways belonging to autonomous systems.

Canonical source:

https://www.rfc-editor.org/rfc/rfc904.html

EGP belongs to an earlier Internet routing environment. By the late 1980s the Internet needed richer inter-AS routing behavior, especially as NSFNET and other autonomous networks enlarged the operational graph.

RFC 1771 later says explicitly that BGP was built on experience gained with:

- EGP as defined in RFC 904;
- EGP usage in the NSFNET Backbone as described in RFC 1092 and RFC 1093.

So the evidence supports a real design lineage:

```text
EGP protocol experience
        +
NSFNET operational EGP/policy experience
        ↓
BGP inter-AS routing design
```

This should be recorded as **documented influence/design ancestry**, not a simple `revision-of`: BGP is not merely EGP version 2.

---

## 2. BGP-1: RFC 1105, June 1989

RFC 1105, by Kirk Lougheed and Yakov Rekhter, is titled *A Border Gateway Protocol (BGP)*.

Canonical source:

https://www.rfc-editor.org/rfc/rfc1105.html

Its purpose is exchange of network-reachability information between Autonomous Systems.

### It was not purely theoretical

The RFC says that, at the time of writing, BGP implementations existed for:

- **cisco routers**;
- the **NSFNET Nodal Switching Systems**;
- and a public-domain `gated` implementation was being developed.

That is a valuable deployment anchor.

BGP-1 therefore belongs simultaneously to:

- protocol-standard history;
- Cisco software/product archaeology;
- NSFNET IBM RT NSS archaeology;
- Unix routing-daemon history.

### TCP as the transport

RFC 1105 says BGP uses a transport-protocol connection and clarifies that this means TCP; it uses **TCP port 179**.

The operational model is already recognizable:

```text
BGP system
   ↓ TCP connection (port 179)
BGP peer
   ↓
initial routing-table transfer
   + incremental updates
   + keepalives
   + notifications
```

The RFC states that the hosts running BGP need not themselves be routers, an important warning against equating “BGP speaker” with one particular forwarding chassis.

### AS paths and loop prevention

BGP-1 carries Autonomous-System path information and uses AS-path inspection to avoid routing loops while allowing local policy restrictions to affect propagation.

This is one of the durable conceptual fossils of BGP.

---

## 3. BGP-2: RFC 1163, June 1990

RFC 1163 explicitly says:

> Obsoletes: RFC 1105

Canonical source:

https://www.rfc-editor.org/rfc/rfc1163.html

It defines BGP together with companion RFC 1164, *Application of the Border Gateway Protocol in the Internet*, as a proposed standard for inter-autonomous-system routing.

The OPEN message identifies the protocol version as **2**.

### What changed from BGP-1?

Later BGP documentation preserves a concise change history.

RFC 1773 explains that BGP-2:

- removed the BGP-1 concepts of **up**, **down**, and **horizontal** relationships between Autonomous Systems;
- introduced the more general concept of **path attributes**;
- clarified parts of BGP-1 that were under-specified.

Source:

https://www.rfc-editor.org/rfc/rfc1773.html

This is a major architectural change.

The lineage is not just “same protocol, bug fixes.”

A more general attribute model begins replacing fixed assumptions about AS relationships.

```text
BGP-1 fixed relationship concepts
          ↓ removed/generalized
BGP-2 path-attribute architecture
```

That generalization becomes important for later policy growth.

---

## 4. BGP-3: RFC 1267, October 1991

RFC 1267, *Border Gateway Protocol 3 (BGP-3)*, explicitly obsoletes RFC 1163.

Canonical source:

https://www.rfc-editor.org/rfc/rfc1267.html

The RFC itself says:

- RFC 1105 is often called BGP-1;
- RFC 1163 is BGP-2;
- this document is BGP-3.

### Changes from BGP-2

The later protocol-history summary in RFC 1773 records that BGP-3:

- lifted some restrictions on the use of the `NEXT_HOP` path attribute;
- added a **BGP Identifier** field to the OPEN message;
- clarified distribution of BGP routes among speakers within one AS.

These changes show another historical trend:

> interdomain routing increasingly needed explicit mechanisms for deployment inside complex autonomous systems, not merely AS-to-AS message exchange at one simple boundary.

---

## 5. BGP-4: RFC 1771, March 1995

RFC 1771, *A Border Gateway Protocol 4 (BGP-4)*, makes the most consequential revision in this early lineage.

Canonical source:

https://www.rfc-editor.org/rfc/rfc1771.html

The document explicitly roots BGP in EGP and NSFNET operational experience, then states that **BGP-4 provides mechanisms for classless interdomain routing**.

### The classful assumption disappears from BGP

BGP-4 adds support for advertising an **IP prefix** and removes the concept of network “class” from BGP's routing model.

This matters because the Internet's address/routing system was under scaling pressure.

The routing object is no longer naturally:

```text
Class A / B / C network number
```

but:

```text
address prefix + prefix length
```

That is a profound fossil still visible in every modern BGP table.

### Route aggregation

RFC 1771 also introduces mechanisms for:

- aggregating routes;
- aggregating AS paths;
- expressing multiple reachable destinations through prefixes.

Aggregation reduces the amount of routing information that BGP speakers need to store and exchange.

The genealogy therefore contains a property-level transformation:

```text
BGP-1/2/3 classful network reachability
                 ↓
BGP-4 prefix reachability + route aggregation
```

This is one of the points where routing-protocol genealogy and address-allocation/CIDR genealogy intersect.

### Policy machinery also expands

BGP-4 introduces/renames important path attributes, including:

- `LOCAL_PREF`;
- `MULTI_EXIT_DISC` (renamed from an earlier metric attribute);
- `ATOMIC_AGGREGATE`;
- changed `AS_PATH` semantics to support aggregation/classless routing.

The protocol is becoming not only a reachability mechanism but an increasingly expressive **policy-routing language between autonomous systems**.

---

## 6. BGP's ancestry is operational as well as textual

RFC 1105 tells us BGP was already implemented on Cisco routers and NSFNET NSS systems.

That means the version genealogy should eventually be joined to implementation records:

```text
RFC 1105 BGP-1
   ├── Cisco router implementation
   ├── NSFNET NSS implementation
   └── gated implementation lineage

RFC 1163 BGP-2
   └── implementation upgrades

RFC 1267 BGP-3
   └── implementation upgrades

RFC 1771 BGP-4
   ├── CIDR/prefix support
   ├── aggregation
   └── commercial Internet deployment
```

The real history is not complete until we know:

- which Cisco software release first shipped each version;
- which NSS software build spoke which version;
- when `gated` added each version;
- what upgrade/coexistence mechanisms were used;
- how speakers negotiated protocol versions;
- which networks continued old versions after a successor RFC existed.

---

## 7. A standards RFC is not the same as operational convergence

The publication sequence is neat:

```text
1989 → 1990 → 1991 → 1995
```

Deployment was less neat.

Each new version had to exist in a live Internet containing old software, multiple vendors, policy constraints, and changing routing tables.

So a mature BGP archaeology needs at least four timelines:

1. **RFC publication**;
2. **first implementation**;
3. **first production deployment**;
4. **retirement of prior versions**.

Those dates will not necessarily match.

---

## 8. BGP grows out of the Autonomous-System concept

BGP's basic unit is not a physical link or one router.

It exchanges reachability between **Autonomous Systems**.

The RFCs treat an AS as presenting a coherent routing view to other ASes even though its interior routing may be complex.

This creates a durable architectural boundary:

```text
inside an AS
  IGP / internal routing / local topology
            ↓ border policy
between ASes
  BGP / AS path / policy
```

The archive should separately excavate the ancestry of:

- Autonomous System numbers;
- IGP/EGP separation;
- internal vs external BGP;
- route reflectors (later);
- confederations (later);
- policy language/configuration.

Do not force all of these into the BGP-1→4 protocol-version tree.

---

## 9. What survived from BGP-1 into BGP-4?

Several core ideas are recognizable across the early lineage:

- inter-AS reachability exchange;
- AS path information;
- loop avoidance using path information;
- TCP transport;
- incremental updates after initial exchange;
- keepalive/liveness mechanisms;
- notification/error messages;
- policy-controlled advertisement.

These are strong candidates for `survives-as` property edges.

But the encoding and policy model changed substantially.

---

## 10. What BGP-4 changed that still defines modern routing

The most important BGP-4 fossils include:

- classless prefixes;
- route aggregation;
- richer path attributes;
- explicit local preference;
- prefix-oriented NLRI;
- AS-path-based policy/loop information.

Modern BGP has many later extensions, larger AS-number support, multiprotocol NLRI, communities, route reflection, security work and operational practices not present in RFC 1771.

RFC 1771 is therefore an ancestor, not today's complete BGP.

It was itself later obsoleted by RFC 4271.

---

## 11. The BGP genealogy after 1995

The next formal core step is:

```text
RFC 1771 BGP-4 (1995)
        ↓ revised core specification
RFC 4271 BGP-4 (2006)
```

But by then the real BGP family had become a web of extensions.

Future branches should include:

- route reflection;
- communities;
- multiprotocol BGP;
- 4-octet AS numbers;
- graceful restart;
- add-path;
- route refresh;
- RPKI/origin validation interaction;
- large communities;
- modern policy/configuration mechanisms.

Those descendants extend beyond this repository's core 1950s–1990s excavation window, but they are necessary endpoints for understanding which old design properties survive today.

---

## 12. Open excavation targets

### BGP-1 deployment

- exact Cisco router models and software releases;
- NSFNET NSS BGP process/source code;
- `gated` first BGP implementation/release;
- real BGP-1 configuration files;
- first inter-AS production sessions;
- packet captures/logs if any survive.

### BGP-2 and BGP-3 migration

- version-negotiation behavior;
- interoperability matrices;
- deployment announcements;
- implementation bug reports;
- routing incidents tied to version changes.

### BGP-4 / CIDR

- connect RFC 1771 to RFC 1518/1519 CIDR lineage;
- recover early classless routing tables;
- measure table-size effects of aggregation;
- trace first production prefix aggregation;
- recover policy configurations from early commercial ISPs;
- identify first BGP-4 implementations by vendor/release.

### Hardware lineage

Connect BGP versions to actual forwarding platforms:

- Cisco AGS/IGS/MGS/CGS-era systems;
- NSFNET IBM RT NSS;
- Proteon;
- gated Unix hosts;
- early commercial backbone routers.

### Operations

Recover:

- NOC route-policy documents;
- neighbor configuration syntax;
- route filters;
- AS-path policies;
- troubleshooting commands;
- route dumps;
- early looking-glass equivalents;
- incidents caused by bad advertisements.

---

## Primary sources

- RFC 904, *Exterior Gateway Protocol Formal Specification* (April 1984): https://www.rfc-editor.org/rfc/rfc904.html
- RFC 1105, *A Border Gateway Protocol (BGP)* (June 1989): https://www.rfc-editor.org/rfc/rfc1105.html
- RFC 1163, *A Border Gateway Protocol (BGP)* (June 1990): https://www.rfc-editor.org/rfc/rfc1163.html
- RFC 1267, *Border Gateway Protocol 3 (BGP-3)* (October 1991): https://www.rfc-editor.org/rfc/rfc1267.html
- RFC 1771, *A Border Gateway Protocol 4 (BGP-4)* (March 1995): https://www.rfc-editor.org/rfc/rfc1771.html
- RFC 1773, *Experience with the BGP-4 Protocol* / BGP-version history context: https://www.rfc-editor.org/rfc/rfc1773.html
- RFC 1092 / RFC 1093 for NSFNET policy/routing architecture context.

## Current conclusion

BGP's early genealogy is unusually visible because the RFC series names its own generations.

The important transformation is not merely:

> BGP got four versions.

It is:

> **an inter-AS reachability protocol born from EGP/NSFNET operational experience progressively generalized its policy machinery and then, in BGP-4, absorbed the classless-prefix and aggregation requirements of a rapidly scaling Internet.**

That is why a modern BGP route still looks like an archaeological bundle of decisions made across several distinct Internet eras.