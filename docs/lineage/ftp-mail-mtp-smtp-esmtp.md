# FTP mail feature → MTP → SMTP → ESMTP: when electronic mail grew its own transport protocol

> **Lineage question:** how did ARPANET electronic mail move from being partly embedded in existing file-transfer practice to a dedicated mail-transfer protocol, and then gain an explicit extension framework without abandoning SMTP's core relay model?

This lineage is valuable because the primary documents themselves describe the split.

---

## 1. Early network mail was not born with SMTP

ARPANET mail existed years before RFC 821.

The early network had several overlapping pieces:

- host-to-host/NCP transport;
- file-transfer mechanisms;
- mailbox/printing conventions;
- evolving message-header formats;
- site-specific mail programs and forwarding practices.

RFC 196, July 1971, *A Mail Box Protocol*, describes a standard mechanism for receiving sequential files for immediate or deferred printing or other use.

Primary source:

- RFC 196 — https://www.rfc-editor.org/rfc/rfc196.html

The design still visibly belongs to the early ARPANET world: NCP, Initial Connection Protocol, Data Transfer Protocol, ASCII files, printers, and mailbox numbers.

This is not yet the modern SMTP model.

---

## 2. Mail and file transfer were historically entangled

RFC 772, September 1980, is unusually explicit.

Its introduction says the new Mail Transfer Protocol has strong similarities to portions of FTP because:

> the original ARPA Network implementation of computer mail was a feature of FTP.

Primary source:

- RFC 772 — https://www.rfc-editor.org/rfc/rfc772.html

That sentence gives us a strong lineage relation.

The historical picture is not:

```text
email appears
   ↓
SMTP
```

but more like:

```text
ARPANET host/file-transfer infrastructure
          ↓
mail delivery as an FTP-related feature
          ↓ pressure to separate the responsibility
Mail Transfer Protocol (MTP)
          ↓
SMTP
```

---

## 3. Why split mail transfer out of FTP?

File transfer and mail transfer overlap in one obvious sense: both move data from one host to another.

But their operational semantics differ.

Mail needs concepts such as:

- envelope sender;
- recipient mailboxes;
- acceptance/rejection per recipient;
- forwarding/relaying;
- delivery failure handling;
- queued store-and-forward operation;
- message headers/content semantics separate from transfer commands.

A dedicated mail-transfer protocol makes those responsibilities first-class instead of treating mail as a special case inside a broader file-transfer protocol.

This is another example of **responsibility specialization** in protocol history.

---

## 4. MTP is a transitional branch, not just a forgotten name

RFC 772 defines a first draft of Mail Transfer Protocol (MTP) whose objective is to transfer mail reliably and efficiently.

The document depends on the surrounding ARPA Internet Protocol Handbook environment and explicitly notes its FTP ancestry.

That makes MTP archaeologically useful even though SMTP soon superseded it.

The archive should preserve:

```text
FTP-related mail mechanisms
        ↓
MTP RFC 772
        ↓ revisions
RFC 780
        ↓
SMTP RFC 788
```

RFC 788 (November 1981) explicitly says it replaces RFC 780 and RFC 772.

Primary source:

- RFC 788 — https://www.rfc-editor.org/rfc/rfc788.html

This is a formal revision/supersession line.

---

## 5. SMTP becomes independent of one transport substrate

RFC 788 and later RFC 821 define SMTP around a powerful abstraction:

> mail transfer requires a reliable ordered data stream, but is not tied to one particular transmission subsystem.

Primary source:

- RFC 821 — https://www.rfc-editor.org/rfc/rfc821.html

That matters enormously in the NCP → TCP/IP transition.

Instead of defining mail as something that belongs to one network's file-transfer service, SMTP is designed as an application protocol that can operate across different transport environments.

The responsibility becomes:

```text
reliable ordered interprocess channel
        ↓
SMTP conversation
        ↓
mail envelope + content
```

The underlying network/transport can change while the mail-transfer semantics persist.

---

## 6. Relaying is part of the architecture

RFC 821 emphasizes SMTP's ability to relay mail across transport service environments.

So SMTP is not merely:

```text
user A → server B
```

It supports an intermediate message-transfer architecture:

```text
originating MTA
      ↓
relay MTA
      ↓
possibly another relay
      ↓
destination MTA / mailbox environment
```

The later operational complexity of Internet mail grows on top of this relay concept.

This is why SMTP history should be connected to:

- host naming/DNS;
- mail routing;
- MX records;
- queue management;
- message format standards;
- mail transfer agents such as Sendmail and predecessors.

---

## 7. Message format is a separate lineage from mail transport

Another archival trap is treating “SMTP” as the whole email standard.

Transport and message syntax are separate genealogies.

For example:

```text
mail transfer protocol lineage
    MTP → SMTP → ESMTP

message format lineage
    early ARPANET formats
        → RFC 561 / RFC 680 / RFC 733
        → RFC 822
        → later Internet Message Format / MIME ecosystem
```

RFC 680, April 1975, extends message-field definitions and points to the evolving ARPANET message-format standards.

Primary source:

- RFC 680 — https://www.rfc-editor.org/rfc/rfc680.html

RFC 822 later becomes a major message-format anchor.

Do not collapse message format, transfer protocol, mailbox access, and user-agent behavior into one “email protocol” object.

---

## 8. RFC 788 → RFC 821 is a formal SMTP revision

RFC 788 is an early SMTP specification.

RFC 821, August 1982, becomes the classic SMTP specification.

The repository should preserve both rather than starting the story at RFC 821.

```text
RFC 772 MTP
   ↓
RFC 780
   ↓
RFC 788 SMTP
   ↓
RFC 821 SMTP
```

The exact 780/788/821 field/command changes belong in a future structured diff.

---

## 9. DNS later becomes part of mail routing infrastructure

SMTP did not originally depend on today's DNS/MX world because DNS itself was still emerging.

Mail routing later intersects the naming lineage.

RFC 974 (1986), *Mail Routing and the Domain System*, is a key bridge between these histories.

Primary source:

- RFC 974 — https://www.rfc-editor.org/rfc/rfc974.html

So another branch appears:

```text
SMTP relay architecture
       +
DNS/domain naming architecture
       ↓
DNS-based mail exchanger routing
```

This is not SMTP turning into DNS. It is two previously distinct protocol lineages becoming operationally coupled.

---

## 10. ESMTP preserves SMTP while adding a negotiation framework

By the early 1990s, SMTP had been deployed for roughly a decade and needed extensions.

RFC 1425 (1993), later RFC 1651 (1994), introduces an explicit SMTP service-extension framework.

Primary sources:

- RFC 1425 — https://www.rfc-editor.org/rfc/rfc1425.html
- RFC 1651 — https://www.rfc-editor.org/rfc/rfc1651.html

The critical move is **capability discovery**.

Instead of every extension silently assuming support, an extended SMTP server can advertise what it supports.

The new `EHLO` path turns extension negotiation into a protocol mechanism.

Conceptually:

```text
classic SMTP
    ↓ retains basic mail-transfer model
ESMTP
    ↓ adds capability advertisement / negotiated extensions
extended SMTP ecosystem
```

---

## 11. This is continuity, not replacement of the whole protocol

ESMTP is a good example of an old protocol surviving by gaining an extension framework.

The core concepts remain recognizable:

- SMTP client/server roles;
- envelope sender;
- recipients;
- DATA/message content;
- relay behavior;
- reliable ordered transport assumption.

What changes is extensibility.

This resembles other networking lineages where a stable core survives while negotiation becomes explicit.

---

## 12. The protocol command line itself is a living fossil

Modern SMTP still looks surprisingly textual to anyone accustomed to binary network protocols.

A session can still expose commands descended from this early command/reply culture:

```text
EHLO
MAIL FROM
RCPT TO
DATA
QUIT
```

That textual interaction is not accidental decoration.

It belongs to a long ARPANET/Internet tradition of human-readable command/reply application protocols, including FTP and Telnet-era practice.

Direct command-by-command ancestry should be established from protocol diffs rather than assumed, but the family resemblance is historically meaningful.

---

## 13. A better email genealogy

Avoid:

```text
email → SMTP → Gmail
```

Use multiple intersecting lineages:

```text
TRANSFER
FTP-related mail handling
      ↓
MTP
      ↓
SMTP RFC 788/821
      ↓
ESMTP extension framework

FORMAT
early ARPANET message formats
      ↓
RFC 733 / RFC 822
      ↓
MIME / later message format

ROUTING
host tables
      ↓
DNS
      ↓
MX-based mail routing

ACCESS
terminal/mailbox/user programs
      ↓
POP / IMAP / webmail branches
```

Only by keeping these separate can the archive explain which part of modern email came from which ancestor.

---

## 14. Sources

Primary sources used or registered for this excavation:

- RFC 196, *A Mail Box Protocol* — https://www.rfc-editor.org/rfc/rfc196.html
- RFC 680, *Message Transmission Protocol* — https://www.rfc-editor.org/rfc/rfc680.html
- RFC 772, *Mail Transfer Protocol* — https://www.rfc-editor.org/rfc/rfc772.html
- RFC 788, *Simple Mail Transfer Protocol* — https://www.rfc-editor.org/rfc/rfc788.html
- RFC 821, *Simple Mail Transfer Protocol* — https://www.rfc-editor.org/rfc/rfc821.html
- RFC 822, message format — https://www.rfc-editor.org/rfc/rfc822.html
- RFC 974, *Mail Routing and the Domain System* — https://www.rfc-editor.org/rfc/rfc974.html
- RFC 1425, *SMTP Service Extensions* — https://www.rfc-editor.org/rfc/rfc1425.html
- RFC 1651, *SMTP Service Extensions* — https://www.rfc-editor.org/rfc/rfc1651.html

---

## 15. Next excavation layer

1. recover the exact FTP mail commands and their revision history;
2. RFC 772 → 780 → 788 → 821 command/state-machine diff;
3. trace NCP-era mail implementations into TCP/IP-era MTAs;
4. ARPANET mail queue/spool formats and operator practice;
5. RFC 561 → 680 → 733 → 822 message-format genealogy;
6. DNS MX implementation and RFC 974 operational history;
7. Sendmail/Delivermail and other MTA source-code genealogy;
8. RFC 821 → ESMTP RFC 1425/1651/1869 extension genealogy;
9. MIME as a separate content-format branch;
10. POP/IMAP as mailbox-access branches, explicitly separate from SMTP transport;
11. UUCP mail interworking with SMTP;
12. surviving mail logs/configuration files from early Internet sites.

---

## Conclusion

The history of SMTP is not simply “someone designed an email protocol.”

It is a story of **specialization**:

> mail first reused surrounding network/file-transfer machinery, then became important enough to demand its own transport semantics, and later became stable enough that extensibility itself had to be standardized.

That is exactly the kind of technical ancestry this repository is meant to preserve.