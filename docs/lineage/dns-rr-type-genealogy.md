# DNS Resource-Record Genealogy — One 1987 Container, Decades of New Meanings

DNS is a textbook example of a **living core with an extension forest**. RFC 1035's Resource Record structure remains recognizable, while new TYPE values have allowed DNS to absorb new addressing, service-discovery, security and application-binding roles for decades.

## 1. The ancient container still works

RFC 1035 defines the Resource Record shape around fields such as:

```text
NAME
TYPE
CLASS
TTL
RDLENGTH
RDATA
```

The power of the design is that `TYPE` selects the interpretation of `RDATA`.

That means the core database/wire machinery can survive while the set of meanings grows.

## 2. 1987 baseline

RFC 1035 already lists core RR types including:

- `A` — host address;
- `NS` — authoritative name server;
- `CNAME` — alias/canonical-name relationship;
- `SOA` — start of zone authority;
- `PTR` — pointer/reverse-style mapping;
- `MX` — mail exchange;
- `TXT` — text strings;
- others, including historical types.

It also marks `MD` and `MF` obsolete in favor of `MX`, showing that even the first mature DNS core already contained fossils.

## 3. DNS type space is an archaeological registry

A DNS zone can contain records from very different eras under one structural model.

For example:

```text
A      → IPv4 addressing
MX     → mail routing
TXT    → generic text / later many application conventions
AAAA   → IPv6 addressing
SRV    → service location
CAA    → certificate-authority authorization
SVCB   → generic service binding
HTTPS  → HTTP-oriented SVCB form
```

The RR container is older than many of the services it now describes.

## 4. Experimental branches reveal roads not taken

RFC 1183 (1990) defined experimental DNS records for:

- AFS database location;
- responsible person (`RP`);
- X.25 address (`X25`);
- ISDN address (`ISDN`);
- route-through (`RT`).

This is particularly valuable for network archaeology because DNS did not expand only toward today's winning technologies.

The type registry also preserves attempts to make DNS carry information about technologies that later declined.

So the DNS RR space is not merely an extensibility mechanism; it is a **historical sediment register**.

## 5. AAAA — the old DNS container absorbs a new network layer

RFC 3596 defines `AAAA` for IPv6 addresses and describes the extension as compatible with existing DNS applications and implementations.

The architecture is strikingly conservative:

```text
RFC 1035 RR machinery
        ↓ new TYPE/RDATA interpretation
AAAA = 128-bit IPv6 address
```

IPv6 did not require inventing a new naming database.

The 1987 DNS container simply learned a new address family.

## 6. SRV — DNS begins describing services, not only hosts

RFC 2782 defines `SRV` records to specify the location of services.

This broadens DNS from:

> “What address belongs to this name?”

toward:

> “Which host/port provides this named service, and with what priority/weight?”

Again the extension is not a DNS replacement. It is another semantic branch growing from the same RR substrate.

## 7. LOC — DNS briefly becomes a geographic database

RFC 1876 defines the experimental `LOC` RR and explicitly frames it as another use of DNS's extensible record machinery.

This is a useful reminder that not every extension becomes ubiquitous.

`LOC` belongs in the archive as a living-or-niche branch whose existence reveals how broad DNS's ambitions became.

## 8. CAA — DNS becomes part of certificate issuance policy

RFC 8659 defines `CAA` so a domain owner can specify which Certification Authorities are authorized to issue certificates.

This is a remarkable expansion of DNS responsibility:

```text
naming database
    ↓
address/service routing metadata
    ↓
security-policy publication for PKI issuance
```

The protocol core still looks like DNS.

The application semantics are now far outside the 1980s host-table replacement problem.

## 9. SVCB / HTTPS — the 1987 RR model reaches modern service bootstrap

RFC 9460 defines `SVCB` and `HTTPS` records to publish service-binding information, alternative endpoints and connection parameters.

The specification explicitly describes uses including choosing service endpoints and informing modern HTTP connection setup.

This creates a striking lineage:

```text
RFC 1035 RR: TYPE + CLASS + TTL + RDATA
              ↓ decades of extensions
RFC 9460 SVCB / HTTPS
```

A 2020s mechanism for HTTP/3-oriented service bootstrap fits inside a database/wire abstraction designed in the 1980s.

## 10. The right genealogy is a tree, not a sequence

Do not write:

```text
A → MX → AAAA → SRV → CAA → HTTPS
```

They are not revisions of one another.

A better model is:

```text
                       RFC 1035 RR framework
            ┌──────────────┼───────────────┐
            ↓              ↓               ↓
       addressing      service/routing     metadata
       /       \         /      \          /   \
      A       AAAA      MX      SRV       TXT  LOC
                                      \
                                       security/application
                                         /          \
                                       CAA       SVCB/HTTPS
```

The inherited property is **the extensible typed-record container**, not the semantics of any earlier RR.

## 11. What survives today

The most durable DNS inheritance is not any single RR type. It is the model:

```text
owner name
+ typed data
+ class
+ TTL
+ authoritative/cached distribution
```

That model has proven able to absorb addressing changes, mail routing, service discovery, security policy and modern application bootstrap.

## Primary source spine

- RFC 1034 / 1035 — DNS core;
- RFC 1183 — experimental RR branches;
- RFC 1876 — LOC;
- RFC 2782 — SRV;
- RFC 3596 — AAAA;
- RFC 8659 — CAA;
- RFC 9460 — SVCB and HTTPS.

## Next excavation

- build machine-readable RR genealogy by TYPE code and mnemonic;
- preserve obsolete/experimental status separately from allocation status;
- trace TXT's many later application conventions without pretending TXT itself standardized them;
- trace DNSSEC RR families;
- trace NAPTR, TLSA, SSHFP, URI and other service/security branches;
- recover BIND source changes required for new RR types;
- create real-zone examples showing 1987 and 2020s record forms coexisting.

---

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
