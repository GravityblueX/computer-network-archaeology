# DNS RFC 1034/1035: A 1987 Core That Learned to Grow Extensions

DNS is one of the clearest examples of a standard designed to survive by **not trying to freeze every future use**.

RFC 1034 and RFC 1035 were published in November 1987. They remain foundational to contemporary DNS architecture and wire behavior, even though the system has accumulated decades of new resource-record types, security mechanisms, transport practices, resolver behavior, and operational techniques.

Primary records:

- RFC 1034: https://www.rfc-editor.org/info/rfc1034/
- RFC 1035: https://www.rfc-editor.org/info/rfc1035/

---

## 1. DNS did not survive by staying small

A simplistic story would say:

```text
1987 DNS
  ↓
modern DNS
```

But modern DNS includes mechanisms that the original authors did not need to solve in 1987:

- DNSSEC;
- EDNS;
- much larger responses;
- IPv6 address records;
- new service-discovery record types;
- new privacy transports;
- anycasted authoritative infrastructure;
- validating recursive resolvers;
- aggressive negative caching;
- internationalized-name processing at adjacent layers;
- modern operational attack defenses.

Yet the core architecture is still recognizable.

That is the historical point.

---

## 2. The durable skeleton

RFC 1034/1035 established or consolidated a model containing:

- hierarchical domain names;
- zones and delegation;
- authoritative data;
- name servers;
- recursive/iterative resolution concepts;
- resolvers;
- caching;
- resource records;
- query/response messages;
- classes and RR types;
- distributed administration;
- TTL-based cache lifetime;
- zone-transfer mechanisms.

A modern DNS operator would recognize this vocabulary immediately.

---

## 3. RFC 1034 practically predicted its own survival strategy

RFC 1034 explicitly describes DNS as intentionally extensible.

It distinguishes a core official protocol from experimental/new data types and behavior, and says that the official parts are expected to remain essentially stable in production while extensions continue to appear.

That is an unusually revealing design choice.

The genealogy is therefore not:

```text
DNS v1 → DNS v2 → DNS v3
```

It is more like:

```text
             RFC 1034/1035 core
                 /   |   |   \
              new   new security transport
              RR    behavior   branches
```

A branching ecosystem grows around a stable semantic center.

---

## 4. Distributed administration was part of the protocol architecture

DNS is not merely a compact lookup packet format.

Its history is inseparable from a scaling problem:

```text
one centrally maintained host table
          ↓ does not scale
hierarchical namespace
          ↓
delegated administrative authority
          ↓
distributed authoritative servers
          ↓
caching resolvers
```

This is why the repository treats DNS lineage as simultaneously:

- application protocol history;
- database/distribution history;
- administrative-institution history;
- caching history;
- operational infrastructure history.

The system's hierarchy is social as well as technical.

---

## 5. The packet still looks old

The RFC 1035 message structure remains historically recognizable:

```text
Header
Question
Answer
Authority
Additional
```

The famous header includes fields such as:

- ID;
- QR;
- OPCODE;
- AA;
- TC;
- RD;
- RA;
- response code;
- section counts.

Later work extended the system rather than throwing this format away.

This makes a current packet capture a direct archaeological object.

---

## 6. Resource records: extensibility encoded into the data model

One of DNS's great survival mechanisms is the generic RR model.

A resource record can be thought of as:

```text
NAME
TYPE
CLASS
TTL
RDLENGTH
RDATA
```

The ability to introduce new TYPE semantics meant that the name system could learn new data without redesigning the whole protocol.

Historic/newer record families include, among many others:

- A;
- NS;
- CNAME;
- SOA;
- MX;
- PTR;
- TXT;
- AAAA;
- SRV;
- DNSSEC records;
- CAA;
- SVCB/HTTPS.

The archive should treat each significant RR type as a branch from the resource-record extensibility mechanism, not as "new DNS versions."

---

## 7. MX shows how one subsystem migrated into DNS

Earlier mail-routing experiments used DNS MD/MF records. RFC 974 then established MX processing and mail-exchanger preference behavior.

This is already excavated in:

- `dns-mail-routing-md-mf-mx.md`

It is a useful example because DNS became a platform on which other Internet services could publish routing/service information.

The name system did not merely replace HOSTS.TXT. It became infrastructure for other protocols.

---

## 8. BIND: standards become daemon behavior

The DNS standard genealogy is only half the story.

The Berkeley Internet Name Domain implementation turned the RFC architecture into Unix software and operational practice.

Related excavation:

- `bind-dns-implementation-history.md`

The implementation layer creates another genealogy:

```text
DNS standard
   ↓
name-server daemon
resolver library
zone-file syntax
cache implementation
operational tooling
```

These are not automatically specified by the wire protocol.

---

## 9. DNSSEC is an extension, not a replacement DNS

Security did not arrive by replacing DNS with a new naming architecture.

Instead, security records, signatures, delegation-of-trust mechanisms, validation behavior, and operational key management were layered onto the existing system.

That makes DNSSEC a particularly strong example of **living-core-with-extension-forest** survival.

The core names/delegation/query model remains; new semantics are attached to it.

---

## 10. Transport changed around a stable message model

Classic DNS is strongly associated with UDP and TCP on port 53.

Modern systems can also carry DNS messages through newer protected transports.

This distinction must be preserved:

```text
DNS data/query model
          ≠
transport used to carry a DNS exchange
```

Changing the transport does not necessarily mean replacing the DNS protocol model.

This same distinction appears elsewhere in Internet history: application semantics can persist while lower layers change.

---

## 11. Caching is an old idea that became even more important

RFC 1034 treats caching as a central scaling mechanism.

Modern recursive resolution still depends on caching, but decades of deployment added much richer behavior:

- negative caching;
- validation-state caching;
- serve-stale approaches;
- aggressive denial-of-existence use;
- resolver prefetching and policy;
- cache-poisoning defenses.

The original cache architecture survives while the operational rules branch.

---

## 12. What did *not* survive unchanged

A living core should not be confused with frozen practice.

Areas of major change include:

- security assumptions;
- typical response size;
- resolver hardening;
- authoritative deployment scale;
- root/TLD operations;
- transport privacy;
- IPv6 integration;
- DNSSEC;
- abuse/attack environment;
- load balancing/anycast practice;
- application use of DNS metadata.

So the archive should record:

```text
core mechanism survives
while
operational environment transforms
```

---

## 13. DNS as a reference survival pattern

Repository category:

### `living-core-with-extension-forest`

Definition:

> a foundational standard remains the recognizable architectural and wire-format core while later standards add independent data types, security, transports, operational practices, and application uses around it.

DNS RFC 1034/1035 is the reference example.

---

## Primary sources

- RFC 1034 — Domain Names — Concepts and Facilities: https://www.rfc-editor.org/info/rfc1034/
- RFC 1035 — Domain Names — Implementation and Specification: https://www.rfc-editor.org/info/rfc1035/
- RFC 974 — Mail Routing and the Domain System: https://www.rfc-editor.org/info/rfc974/

## Related archive excavations

- `hosts-txt-to-dns.md`
- `dns-mail-routing-md-mf-mx.md`
- `bind-dns-implementation-history.md`
- `living-standards-still-on-wire.md`

## Next excavation tasks

- build RFC 882/883 → 1034/1035 field/function diff;
- map DNS header bits and section semantics that remain byte-for-byte recognizable;
- create a RR-type genealogy dataset;
- document RFC 1035 zone-transfer behavior → modern AXFR/IXFR practice;
- trace negative caching;
- trace EDNS;
- trace DNSSEC documents and deployment milestones;
- trace BIND 4 → 8 → 9 code/config genealogy;
- preserve early zone files and root-zone snapshots where legally available;
- trace resolver-library API behavior in BSD/Unix/Linux;
- separate DNS-over-TCP historical use from modern encrypted transport branches.