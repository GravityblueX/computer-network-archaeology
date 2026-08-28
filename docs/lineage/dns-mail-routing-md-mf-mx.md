# DNS mail routing: from host-oriented mail delivery to MD/MF and MX

## Why this lineage matters

SMTP answers how one mail transfer agent talks to another. It does not, by itself, answer a different question:

> Given an address like `user@example`, which host should the sending mailer contact?

Before DNS, mail routing was entangled with host tables, source routes, relay conventions and explicit host names. The Domain Name System created a new place to store routing intent for mail.

This lineage is not simply:

```text
DNS -> MX
```

It is:

```text
host-oriented addressing/routing
        ↓
early domain mail bindings: MD / MF
        ↓ operational/design problems
single MX RR type + preference
        ↓
mailer lookup, ranking, fallback, loop avoidance
```

---

## 1. RFC 883: DNS mail support began with more than one RR type

RFC 883 (November 1983) includes explicit "DOMAIN SUPPORT FOR MAIL" and defines early mail-related resource records.

Primary source:

- RFC 883 — https://www.rfc-editor.org/rfc/rfc883.html

The early scheme distinguishes:

- **MD** — mail destination;
- **MF** — mail forwarder.

Conceptually:

```text
domain
  |
  +-- MD -> host expected to deliver locally
  |
  +-- MF -> host willing to forward toward destination
```

This is historically important because modern MX collapses both functions into a single record type with preference ordering.

---

## 2. Agent binding versus mailbox binding

RFC 883's mail discussion is broader than an MX prototype. It explores how domains should bind mail destinations to agents/mailboxes while existing mail systems continue operating.

The global part of an address (`X@Y`) becomes a domain-system lookup key.

That creates a new architectural separation:

```text
mailbox local-part
       |
       | interpreted by receiving mail system
       v
user/account

mail global-part/domain
       |
       | interpreted by DNS/mail routing
       v
mail transfer host(s)
```

This boundary is one of the deep ancestors of modern Internet mail addressing.

---

## 3. Why MD/MF was redesigned

RFC 1035 later explains one practical problem with the original two-type design: if a cache contains one RR type, that does not prove it contains the complete information from the other type.

Primary source:

- RFC 1035 — https://www.rfc-editor.org/rfc/rfc1035.html

The redesign uses a **single MX type** carrying:

- a preference value;
- the exchange host name.

That makes a complete ordered set easier to cache and interpret.

The standard later marks MD and MF obsolete and directs systems toward MX.

This is a very clean example of a data-model redesign caused partly by distributed cache semantics.

---

## 4. RFC 974: MX becomes operational mail-routing policy

RFC 974 (January 1986) explains how mailers are expected to route messages using MX records.

Primary source:

- RFC 974 — https://www.rfc-editor.org/rfc/rfc974.html

An MX contains:

```text
owner domain
preference (16-bit unsigned integer)
mail exchanger host name
```

Lower preference values are tried first.

Multiple MX records can represent:

- primary exchange;
- fallback exchanges;
- equal-preference exchanges.

This moves part of mail-routing policy into DNS data.

---

## 5. MX is not just "the mail server record"

A simplistic modern explanation says:

> MX tells you the mail server for a domain.

Historically, MX is more interesting. It gives mailers an **ordered set of candidate exchangers** with specific loop-avoidance and fallback rules.

```text
A.EXAMPLE  MX 10 primary
A.EXAMPLE  MX 20 secondary
A.EXAMPLE  MX 30 tertiary
```

A mailer must interpret preferences and its own position carefully.

RFC 974 discusses avoiding loops when the local host is itself one of the listed exchangers.

---

## 6. DNS caching affects mail routing

Once mail routing depends on distributed DNS data, cache lifetime becomes operationally visible.

RFC 974 explicitly discusses stale/incomplete routing information and the fact that eliminating resolver caching would be impractical.

So mail delivery now depends on a chain like:

```text
mailer
  ↓ resolver
cached DNS data OR authoritative query
  ↓
MX set
  ↓
ordered connection attempts
  ↓
SMTP delivery
```

This is why DNS history and SMTP history cannot be fully separated.

---

## 7. No-MX fallback is itself historical behavior

RFC 974 describes behavior for names that return no MX records: treat the destination as though it had an implicit MX pointing to itself.

That behavior later becomes part of operational mail expectations.

It also shows why "MX is mandatory for mail" is an inaccurate historical simplification.

Track separately:

- no-MX fallback rules;
- A/AAAA lookup behavior by era;
- later SMTP standards changes;
- null MX and explicit no-mail signaling as a later branch.

---

## 8. MD/MF -> MX is a real standard lineage

Safe relation:

```text
RFC 883 MD/MF mail-routing data model
          ↓ redesigned/superseded
MX preference-based data model
          ↓
RFC 974 operational mailer behavior
          ↓
RFC 1035 marks MD/MF obsolete, use MX
```

This is stronger than a vague `influenced` edge because the later specifications explicitly describe the replacement.

But do not claim all historical mail-routing behavior came from DNS. Source routing, gateways and non-Internet mail systems continued to coexist.

---

## 9. Mail routing and SMTP are separate responsibilities

The clean conceptual split is:

```text
DNS / MX
    answers: where should I try to deliver?

SMTP
    answers: how do I transfer the message to that peer?
```

And another layer remains separate:

```text
RFC 822 / MIME
    answers: how is the message represented?
```

And another:

```text
POP / IMAP
    answers: how does a user/client access stored mailbox content?
```

Modern "email" is therefore not one protocol but a composition of independent historical lineages.

---

## 10. Implementation archaeology

Recover:

- first DNS mail-aware resolver/mailer implementations;
- Sendmail versions gaining domain/MX support;
- BIND resolver interactions;
- HOSTS.TXT/source-route coexistence;
- mailer queue behavior when MX hosts fail;
- cache-related incidents;
- secondary MX operational practice;
- UUCP/Internet mail gateway interactions.

Real configuration files are especially valuable:

```text
sendmail.cf
zone files
resolver configuration
mail queue/log samples
```

---

## 11. Surviving fossils

Modern DNS still uses MX preference values in a recognizably similar form.

But many surrounding assumptions changed:

- SMTP standards evolved;
- anti-spam policy became central;
- IPv6 added AAAA routing implications;
- DNSSEC changed authenticity possibilities;
- cloud mail hosting changed operational topology;
- secondary/fallback MX practice changed.

A mature lineage should preserve the stable MX core without projecting modern mail-service architecture backward.

---

## 12. Lineage rules

Safe:

```text
RFC 883 MD/MF
    -> redesigned into MX model

MX records
    -> used by RFC 974 mailer routing behavior

DNS routing decision
    + SMTP transport
    = composed mail-delivery path
```

Unsafe:

```text
DNS invented email routing                  TOO BROAD
MX = SMTP                                   WRONG LAYER
MD -> MF -> MX linear version ladder        WRONG; MD/MF coexist as roles
MX always required                          HISTORICALLY FALSE
modern hosted-mail topology existed in 1986 PRESENTIST
```

---

## 13. Sources

Primary:

- Paul Mockapetris, RFC 883, *Domain Names — Implementation and Specification*, November 1983 — https://www.rfc-editor.org/rfc/rfc883.html
- Craig Partridge, RFC 974, *Mail Routing and the Domain System*, January 1986 — https://www.rfc-editor.org/rfc/rfc974.html
- Paul Mockapetris, RFC 1035, *Domain Names — Implementation and Specification*, November 1987 — https://www.rfc-editor.org/rfc/rfc1035.html

Related:

- RFC 882 / RFC 1034 DNS concepts;
- RFC 821 SMTP;
- later SMTP core standards for changed fallback/routing rules.

---

## Open excavation questions

1. Recover the exact RFC/document where MX first replaces MD/MF and map the intermediate update path around RFC 973/974.
2. Reconstruct the first deployed MX-aware mailers.
3. Trace Sendmail/BIND implementation commits/releases.
4. Recover early zone files containing MD, MF and MX records.
5. Reconstruct real secondary-MX arrangements from university/network archives.
6. Trace DNS mail routing coexistence with UUCP bang paths and mail gateways.
7. Track later null-MX and mail-policy records only as descendant branches.

The MX record is a small surviving fossil of a much larger transformation: **mail delivery stopped being only a property of host names and became policy stored in a distributed naming system.**
