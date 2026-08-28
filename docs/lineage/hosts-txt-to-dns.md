# From HOSTS.TXT to DNS: When a Central Naming File Stopped Scaling

The Domain Name System did not appear because someone merely wanted prettier host names.

It grew out of a concrete operational problem: an expanding Internet was relying on centrally maintained/distributed host information while internetworking was simultaneously making naming, administration and address interpretation more complex.

This chapter reconstructs the genealogy from the host-table world into distributed hierarchical naming.

---

## 1. The host table was real infrastructure

RFC 810, *DoD Internet Host Table Specification* (March 1982), documents the format of the Internet host table.

Canonical source:

https://www.rfc-editor.org/rfc/rfc810.html

The file could contain entries such as:

- `NET`;
- `GATEWAY`;
- `HOST`;
- host aliases;
- network addresses;
- operating-system identifiers;
- protocol/service information.

This was not merely a local `/etc/hosts` convenience file in the modern sense.

It was part of an Internet-wide naming/distribution regime associated with the Network Information Center.

A simplified operational model is:

```text
NIC / central host information
          ↓ maintained table
     HOSTS.TXT-style database
          ↓ distributed/copied
       individual hosts
          ↓
applications resolve known host names
```

The important archaeological object is both the **file format** and the **institutional distribution process**.

---

## 2. Central distribution creates scaling and administration pressure

As the network grows, several costs increase:

- number of entries;
- update frequency;
- distribution traffic;
- stale local copies;
- name conflicts;
- coordination burden;
- coupling between one authority/database and many independently administered networks.

Internetworking adds another problem: a flat host namespace is no longer a natural administrative model for a network of networks.

The naming system therefore has to solve not just lookup but **delegation of authority**.

---

## 3. RFC 819: the naming hierarchy appears before the final DNS protocol

RFC 819, *The Domain Naming Convention for Internet User Applications* (August 1982), explicitly says that the familiar `<user>@<host>` convention needs to be generalized with the advent of network interconnection.

Canonical source:

https://www.rfc-editor.org/rfc/rfc819.html

It proposes replacing the simple host field with a composite **domain** name.

The key shift is administrative hierarchy:

```text
flat/simple host name
        ↓
composite domain name
        ↓
hierarchical naming authority
        ↓
distributed name-service responsibility
```

RFC 819 describes the domain hierarchy as an administrative structure rather than a direct reflection of network topology.

That principle survives strongly in modern DNS.

### A naming fossil still visible today

RFC 819 already states that the components run from specific to general, with the root on the right in textual names.

The fundamental idea:

```text
host.subdomain.domain
```

is recognizable in the modern DNS namespace.

---

## 4. RFC 819 also shows what the designers wanted to escape

The document contrasts absolute hierarchical naming with locally interpreted/relative naming environments.

It even discusses UUCP-style source-route names such as:

```text
alpha!beta!gamma!john
```

and identifies problems with locally interpreted names and route-dependent naming.

This is a valuable genealogy point:

> DNS ancestry is not only HOSTS.TXT → DNS; it also belongs to a broader historical struggle between flat, local, route-dependent and globally interpretable naming systems.

The archive should therefore track several naming lineages in parallel:

- ARPANET host tables;
- UUCP bang paths;
- mail naming;
- X.400/X.500 directories;
- DECnet/SNA/proprietary naming;
- DNS.

---

## 5. RFC 882 and RFC 883: DNS becomes a distributed database/protocol system

In November 1983, Paul Mockapetris published:

- RFC 882 — *Domain Names: Concepts and Facilities*;
- RFC 883 — *Domain Names: Implementation and Specification*.

Sources:

https://www.rfc-editor.org/rfc/rfc882.html

https://www.rfc-editor.org/rfc/rfc883.html

RFC 882's references explicitly include:

- RFC 810 host-table specification;
- RFC 819 domain naming convention;
- RFC 830 distributed Internet name service;
- RFC 811 Hostnames Server;
- IEN 116 Internet Name Server.

The protocol did not appear from nowhere; the reference list itself preserves a design genealogy.

### Architectural shift

RFC 883 describes a distributed database divided among name servers.

The user/application interacts with a **resolver**.

The resolver queries name servers, and data may be cached.

```text
application
    ↓
resolver
    ↓ query
name server
    ↓ delegation / remote information
other name servers
```

This is a very different scaling model from distributing one central table to every host.

---

## 6. Delegation is as important as lookup

The crucial historical innovation is not only:

> convert name to address.

The domain structure creates zones/administrative responsibility so independent organizations can control different parts of the namespace.

The system therefore distributes two things:

1. **data**;
2. **authority**.

This is why DNS scales organizationally as well as technically.

A lineage edge should therefore preserve:

```text
central naming authority
        ↓ transformed into
hierarchical delegated naming authority
```

rather than describing DNS as merely a faster host-table lookup service.

---

## 7. Caching creates another line of descent

RFC 883 explicitly discusses cached data acquired by resolvers and eventually discarded by timeout.

This produces a durable mechanism:

```text
query remote authoritative information
        ↓
cache local answer
        ↓
reuse without repeating full lookup
        ↓
expire according to time policy
```

Modern DNS cache behavior is far more developed, but the basic architecture is already recognizable.

The lineage needs to track:

- cache location;
- TTL semantics;
- negative caching (later development);
- recursive vs iterative behavior;
- resolver/server co-location;
- cache poisoning/security consequences (much later descendants).

---

## 8. RFC 883 is explicitly preliminary — standards evolve after deployment experience

An especially useful historical warning appears in RFC 883: parts of the format are described as preliminary and not final implementation guidance.

This prevents a common mistake:

> RFC published = design frozen.

Early DNS went through implementation experience and revision.

That is why later RFCs matter as a separate genealogy stage.

---

## 9. RFC 1034 / RFC 1035 replace the early DNS pair

In November 1987, DNS was re-specified in:

- RFC 1034 — *Domain Names - Concepts and Facilities*;
- RFC 1035 — *Domain Names - Implementation and Specification*.

Sources:

https://www.rfc-editor.org/rfc/rfc1034.html

https://www.rfc-editor.org/rfc/rfc1035.html

RFC 883 is marked obsolete by RFC 1034 and RFC 1035.

The formal revision chain is therefore:

```text
RFC 819            naming convention / early design
     ↓
RFC 882 + RFC 883  early DNS architecture/specification
     ↓ revision / operational experience
RFC 1034 + 1035    mature core DNS specification pair
```

But RFC 1034 contains a useful warning: it describes RFC 819 as **early thoughts** and notes that the current implementation is quite different.

So the correct lineage relation is not simply `revision-of` from 819 to 1034.

It is closer to:

- 819 influenced/defined early naming concepts;
- 882/883 implemented a first DNS architecture;
- 1034/1035 formally superseded the 1983 specification pair.

---

## 10. HOSTS.TXT did not vanish instantly

As with NCP→TCP/IP, naming migration is not an atomic event.

A mature excavation should recover:

- when each operating system gained resolver libraries;
- when local host-table fallbacks remained;
- when applications became domain-aware;
- when mail systems began relying on MX records;
- how bootstrapping worked before DNS was universally available;
- how host-table distribution continued during transition.

The genealogy therefore includes a coexistence interval:

```text
host table only
     ↓
host table + experimental DNS
     ↓
DNS primary + local host-table fallback
```

That pattern still exists on modern machines.

`/etc/hosts` is a particularly literal living fossil.

---

## 11. The modern DNS still carries several early design fossils

### Hierarchical administrative namespace

Still central.

### Resolver / server separation

Still recognizable.

### Distributed authority

Still fundamental.

### Caching

Still fundamental.

### Resource records

Still the central data abstraction, though the set of types expanded enormously.

### Datagram queries plus reliable transport when needed

The transport details evolved, especially with DNS-over-TCP and later encrypted transports, but the dual transport history begins early.

### Local host file fallback

Still present in mainstream operating systems.

The result is a striking lineage:

```text
central text file distribution
        ↓
distributed hierarchical database
        ↓
planet-scale naming infrastructure
```

while the old local file survives beside it.

---

## 12. Open excavation targets

### Pre-DNS host-table operations

- recover HOSTS.TXT distribution schedule;
- file sizes by year;
- host counts by revision;
- update workflow at the NIC;
- transfer protocol used to fetch updates;
- stale-table incidents;
- name-conflict handling;
- staff/operator workload.

### Intermediate name-service experiments

Mine:

- IEN 116 Internet Name Server;
- RFC 811 Hostnames Server;
- RFC 812 NICNAME/WHOIS relationship;
- RFC 830 distributed name-service proposal;
- CSNET name server;
- mail meeting/design records.

### DNS implementation archaeology

Recover early software:

- first Mockapetris/ISI DNS server/resolver implementations;
- BIND ancestry;
- TOPS-20/TENEX/Unix resolver adoption;
- root server software/configuration;
- zone file examples;
- cache algorithms;
- operator logs.

### Root and top-level-domain operations

Track:

- initial root server list;
- `.ARPA` transition;
- early top-level domains;
- delegation procedures;
- zone-transfer mechanisms;
- administrative organizations.

### Application lineage

Trace DNS effects on:

- SMTP/MX;
- Telnet/FTP host naming;
- HTTP virtual hosting (later descendant);
- reverse DNS;
- service discovery records.

---

## Primary sources

- RFC 810, *DoD Internet Host Table Specification* (March 1982): https://www.rfc-editor.org/rfc/rfc810.html
- RFC 819, *The Domain Naming Convention for Internet User Applications* (August 1982): https://www.rfc-editor.org/rfc/rfc819.html
- RFC 882, *Domain Names: Concepts and Facilities* (November 1983): https://www.rfc-editor.org/rfc/rfc882.html
- RFC 883, *Domain Names: Implementation and Specification* (November 1983): https://www.rfc-editor.org/rfc/rfc883.html
- RFC 1034, *Domain Names - Concepts and Facilities* (November 1987): https://www.rfc-editor.org/rfc/rfc1034.html
- RFC 1035, *Domain Names - Implementation and Specification* (November 1987): https://www.rfc-editor.org/rfc/rfc1035.html

## Current conclusion

DNS is not merely a protocol that maps names to IP addresses.

Its genealogy records a deeper infrastructure transition:

> **central file maintenance and distribution became hierarchical delegation, distributed authority, resolver/server separation and caching.**

And one of the best archaeological jokes is that the ancestor never completely disappeared:

> the global Internet uses DNS, but your machine can still consult a little local hosts file.