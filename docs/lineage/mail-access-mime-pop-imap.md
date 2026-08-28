# Mail representation and access: RFC 822, MIME, POP and IMAP are different lineages

## Why this lineage matters

Modern users call all of this "email":

- message headers/body format;
- attachments and non-ASCII content;
- message transfer between servers;
- mailbox storage;
- client retrieval;
- remote mailbox manipulation.

Historically these responsibilities were standardized by different protocol families.

A useful decomposition is:

```text
message representation      RFC 822 -> MIME
server-to-server transfer   SMTP/ESMTP
mail routing                DNS/MX
mailbox retrieval           POP
remote mailbox access       IMAP
```

The lineages interact, but they should not be merged.

---

# Part I — message representation and MIME

## 1. RFC 822 assumes a mostly ASCII message world

RFC 822 defines Internet text-message syntax with structured headers and a message body.

MIME later explicitly describes RFC 822 as providing detailed US-ASCII header structure while leaving the body essentially flat US-ASCII text.

That limitation becomes the design pressure for MIME.

The historical question is not "how were attachments invented?" but:

> How can the existing mail transport/message infrastructure carry richer content without replacing the whole mail system?

---

## 2. MIME is an extension architecture, not a new mail transport

The MIME family extends message representation to support:

- non-US-ASCII textual bodies;
- non-text content types;
- multipart bodies;
- encoded transfer representations;
- non-ASCII header information through companion specifications.

Primary source:

- RFC 2045 — https://www.rfc-editor.org/rfc/rfc2045.html

The lineage is roughly:

```text
RFC 822 text-message representation
      ↓ extension pressure
RFC 934 and other experiments
      ↓
RFC 1341 MIME
      ↓
RFC 1521/1522 generation
      ↓
RFC 2045-2049 MIME family
```

This must be reconstructed document by document.

---

## 3. Content-Type creates an extensible type system inside mail

MIME introduces a typed content model rather than assuming one undifferentiated text body.

Conceptually:

```text
Content-Type: text/plain
Content-Type: image/...
Content-Type: application/...
Content-Type: multipart/...
```

The important inheritance pattern is:

> keep the RFC 822-style message envelope/header framework while adding a typed body representation.

This is `survives-as` plus extension, not wholesale replacement.

---

## 4. Content-Transfer-Encoding reflects old transport constraints

MIME had to coexist with mail transport paths that historically assumed restricted text-safe formats.

Hence encodings such as quoted-printable and base64 are not arbitrary cosmetic inventions. They are adaptation layers between richer content and transport constraints.

The archaeology should therefore connect:

```text
rich binary/non-ASCII object
      ↓ MIME encoding
mail-safe textual representation
      ↓ SMTP/mail infrastructure
remote MIME decoder
      ↓
original content semantics
```

Do not treat base64 as "an email attachment format". It is a reusable encoding used here as one part of a larger compatibility strategy.

---

# Part II — POP: bring mail from an always-up server to a workstation

## 5. POP appears when workstations do not make good always-on mailboxes

RFC 918 (October 1984) proposes the Post Office Protocol so a workstation can dynamically access mail stored on a mailbox server.

Primary source:

- RFC 918 — https://www.rfc-editor.org/rfc/rfc918.html

This is a change in computing topology:

```text
traditional multiuser host
    user reads mailbox on same always-on machine

workstation era
    personal machine may be off
    mailbox stays on server
    client fetches mail later
```

The protocol exists because personal computers/workstations changed availability and storage assumptions.

---

## 6. POP2 makes the client/server division explicit

RFC 937 (February 1985) is POP Version 2 and explicitly says it revises RFC 918.

It expects:

- a user's workstation as an Internet host;
- mailbox storage on an "always up" server;
- SMTP for posting/sending mail;
- POP for mailbox access.

Primary source:

- RFC 937 — https://www.rfc-editor.org/rfc/rfc937.html

This is a clean division of labor:

```text
SMTP -> put/send mail through transfer system
POP  -> retrieve stored mail from mailbox server
```

POP does not replace SMTP.

---

## 7. POP3 is not simply POP2 with one more command

RFC 1081 (November 1988) defines POP3 and says it is based on the earlier POP work while also reflecting additional project experience.

Later POP3 standardization leads to RFC 1939.

Primary sources:

- RFC 1081 — https://www.rfc-editor.org/rfc/rfc1081.html
- RFC 1939 — https://www.rfc-editor.org/rfc/rfc1939.html

The exact POP2→POP3 state-machine/command changes should be captured as a revision genealogy, not summarized as "POP got version 3."

---

# Part III — IMAP: keep the mailbox remote and manipulate it there

## 8. IMAP solves a broader problem than simple retrieval

IMAP's central idea is different from the simplest POP workflow.

RFC 1176 describes IMAP2 as allowing workstations and personal computers to access a mailbox repository and says it can be thought of as a **functional superset** of POP2/POP3 for many operations, while explicitly noting that the protocols differ in important ways.

Primary source:

- RFC 1176 — https://www.rfc-editor.org/rfc/rfc1176.html

The key shift is:

```text
POP-like mental model
server mailbox -> retrieve messages to client

IMAP mental model
mailbox remains a remote structured repository
client queries/manipulates messages and mailboxes on server
```

---

## 9. IMAP2 cites POP as a model, which is real documented influence

RFC 1176 states that RFC 937 was used as a model because POP addresses a similar problem with a less comprehensive solution.

This supports a real `influenced` edge:

```text
POP2 protocol/problem model
      ↓ documented model/influence
IMAP2 design
```

But it does **not** justify:

```text
POP2 -> IMAP2 formal revision
```

They become competing/coexisting mailbox-access families.

This is a perfect example of why the lineage database needs multiple relation types.

---

## 10. Tagged commands are an IMAP architectural signature

RFC 1064/1176 describes tagged commands and responses. A command carries an identifier and the matching server completion response uses the same tag, while unsolicited data can arrive independently.

That is a very different interaction model from a simple strictly lock-step retrieval protocol.

It enables richer asynchronous/remote-repository behavior.

Future archaeology should compare:

- IMAP2 tags/state;
- IMAP4 revisions;
- unsolicited responses;
- mailbox selection/state;
- message flags;
- partial fetch/search;
- concurrent client expectations.

---

## 11. IMAP version genealogy

A simplified document spine:

```text
RFC 1064 IMAP2 (1988)
      ↓
RFC 1176 IMAP2 (1990)
      ↓ broader revision work
RFC 1730 IMAP4 (1994)
      ↓
RFC 2060 IMAP4rev1 (1996)
      ↓
RFC 3501 IMAP4rev1 (2003)
```

Primary sources:

- RFC 1064 — https://www.rfc-editor.org/rfc/rfc1064.html
- RFC 1176 — https://www.rfc-editor.org/rfc/rfc1176.html
- RFC 1730 — https://www.rfc-editor.org/rfc/rfc1730.html
- RFC 3501 — https://www.rfc-editor.org/rfc/rfc3501.html

Later revisions beyond the core period should be retained as descendant endpoints.

---

## 12. POP and IMAP coexist because they embody different client/server assumptions

Do not encode:

```text
POP -> IMAP = upgrade
```

Better:

```text
mailbox-on-server problem
      /                  \
 simple retrieval          remote repository manipulation
      |                           |
     POP                         IMAP
```

Implementations and users may choose either depending on client capability, connectivity, storage and synchronization expectations.

---

## 13. SMTP, POP and IMAP form a composed service, not one protocol stack

A workstation-era message path may look like:

```text
sender client
   ↓ submission/SMTP-like path
mail transfer system
   ↓ DNS/MX routing
recipient mailbox server
   ↓
POP or IMAP
   ↓
recipient client
```

Message representation is separately governed by RFC 822/MIME.

This decomposition is the key to understanding why changing one part of mail did not require replacing every other part.

---

## 14. Implementation archaeology targets

### MIME

- first MIME-capable mailers/readers;
- metamail and early MIME tools;
- Sendmail interaction;
- content-type registry history;
- real early multipart messages;
- gateways that damaged 8-bit/binary content.

### POP

- POP server/client source;
- workstation mail clients;
- mailbox-locking behavior;
- leave-on-server evolution;
- authentication mechanisms.

### IMAP

- Mark Crispin's implementations;
- UW IMAP source;
- server mailbox formats;
- synchronization/client caches;
- early Pine/other client integration;
- extension negotiation.

---

## 15. Lineage rules

Safe:

```text
RFC 822 text-message framework
    -> extended by MIME body/type/encoding architecture

RFC 918 -> RFC 937
    = explicit POP revision

POP2
    -> documented design model for IMAP2
    = influence, not formal revision

IMAP2 -> IMAP4 -> IMAP4rev1
    = protocol-family revision genealogy
```

Unsafe:

```text
MIME -> SMTP                       WRONG RESPONSIBILITY
POP -> IMAP formal upgrade         WRONG
IMAP sends mail                    WRONG CORE ROLE; mail transfer handled separately
base64 = attachment protocol       TOO NARROW
RFC 822 = SMTP message format      MIXES REPRESENTATION/TRANSFER
```

---

## 16. Sources

Primary:

- RFC 918, *Post Office Protocol*, October 1984 — https://www.rfc-editor.org/rfc/rfc918.html
- RFC 937, *Post Office Protocol — Version 2*, February 1985 — https://www.rfc-editor.org/rfc/rfc937.html
- RFC 1081, *Post Office Protocol — Version 3*, November 1988 — https://www.rfc-editor.org/rfc/rfc1081.html
- RFC 1939, *Post Office Protocol — Version 3*, May 1996 — https://www.rfc-editor.org/rfc/rfc1939.html
- RFC 1064, *Interactive Mail Access Protocol — Version 2*, July 1988 — https://www.rfc-editor.org/rfc/rfc1064.html
- RFC 1176, *Interactive Mail Access Protocol — Version 2*, August 1990 — https://www.rfc-editor.org/rfc/rfc1176.html
- RFC 1730, *Internet Message Access Protocol — Version 4*, December 1994 — https://www.rfc-editor.org/rfc/rfc1730.html
- RFC 3501, *Internet Message Access Protocol — Version 4rev1*, March 2003 — https://www.rfc-editor.org/rfc/rfc3501.html
- RFC 2045, *MIME Part One*, November 1996 — https://www.rfc-editor.org/rfc/rfc2045.html

MIME's earlier RFC 934/1341/1521/1522 documents require separate mining.

---

## Open excavation questions

1. Build RFC 822 → RFC 934 → 1341 → 1521/1522 → 2045-2049 representation genealogy.
2. Recover first interoperable MIME implementation and sample messages.
3. Build POP 918→937→1081→1939 command/state diff.
4. Build IMAP 1064→1176→1730→2060→3501 command/state diff.
5. Recover early workstation mail clients and mailbox-server products.
6. Trace SMTP submission versus POP/IMAP retrieval as separate operational workflows.
7. Trace attachment handling, character sets and 8BITMIME as intersecting but distinct lineages.

Modern email is not one protocol. It is a **federation of historical compromises whose boundaries became stable enough that each part could evolve without replacing the whole.**
