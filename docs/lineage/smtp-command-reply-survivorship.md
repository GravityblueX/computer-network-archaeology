# SMTP Command and Reply Survivorship — Reading 1982 Inside a Modern Mail Session

SMTP is a particularly satisfying root-hunting target because a modern SMTP dialogue still contains commands and reply-code structures that are immediately recognizable in RFC 821 (1982).

The protocol evolved substantially, but many operator-visible verbs survived.

## 1. The 1982 command vocabulary

RFC 821 describes commands including:

```text
HELO
MAIL
RCPT
DATA
RSET
VRFY
EXPN
HELP
NOOP
QUIT
```

It also contained transaction-start variants such as `SEND`, `SOML`, `SAML`, and a `TURN` command that later became obsolete.

The archaeological value is that the surviving core remains visible in plaintext protocol traces.

## 2. A modern transaction still looks ancient

The durable transactional skeleton is:

```text
HELO/EHLO
MAIL FROM:<...>
RCPT TO:<...>
DATA
...
.
QUIT
```

RFC 5321 still defines `MAIL`, `RCPT`, `DATA`, `RSET`, `VRFY`, `EXPN`, `HELP`, `NOOP` and `QUIT`, while requiring support for `HELO` and preferring `EHLO` for extension negotiation.

Thus the transaction state machine is not merely inspired by 1982 SMTP; much of its operator-visible command language remains directly recognizable.

## 3. HELO → EHLO is a model extension, not a total command-language replacement

Classic SMTP used `HELO`.

Extended SMTP added `EHLO` so a server can advertise supported extensions.

Modern RFC 5321 says clients should start with `EHLO`, while servers must still support `HELO`.

This creates a clear survivorship relation:

```text
HELO
  ├─ survives for baseline compatibility
  └─ role extended by EHLO capability negotiation
```

This is different from an ordinary `revision-of` relationship: the older command remains part of the living protocol.

## 4. MAIL / RCPT / DATA — an extremely durable transaction grammar

The core model is still:

```text
reverse path
     ↓ MAIL
one or more forward paths
     ↓ RCPT
message content
     ↓ DATA
```

This grammar survived even while routing, address syntax, extension negotiation, authentication and transport security evolved around it.

That durability is one reason a contemporary manual SMTP session still feels historically transparent.

## 5. Three-digit replies are another living interface fossil

SMTP replies use three-digit numeric codes.

The first digit describes broad success/failure class, and familiar replies such as:

```text
220 service ready
250 requested action okay
354 start mail input
421 service unavailable
450/451/452 temporary failures
500/501/503 syntax/state failures
550 permanent mailbox/request failure class
221 closing connection
```

form an operator-visible interface that has survived multiple generations of mail software.

A modern MTA log is therefore partly a record of an old protocol language still in use.

## 6. Dot transparency is still recognizable

RFC 821 specifies the `<CRLF>.<CRLF>` end-of-data convention and the associated rule of doubling a leading dot in message text.

This “dot-stuffing” behavior survived into modern SMTP.

It is a good example of a tiny compatibility mechanism that remains because changing it would break the wire grammar of an enormous installed base.

## 7. Some commands died

The old command set also contains fossils that did not survive modern core SMTP.

RFC 5321 explicitly refers to `SEND`, `SOML` and `SAML` as obsolete transaction-start commands.

`TURN` likewise belongs to an earlier operational model.

So the command vocabulary itself can be mapped as:

```text
HELO     → alive, baseline compatibility
EHLO     → later extension-negotiation branch
MAIL     → alive
RCPT     → alive
DATA     → alive
RSET     → alive
VRFY     → alive in specification, often restricted operationally
EXPN     → alive in specification, often restricted operationally
HELP     → alive
NOOP     → alive
QUIT     → alive
SEND     → obsolete
SOML     → obsolete
SAML     → obsolete
TURN     → obsolete
```

## 8. Specification survival and deployment survival differ

A command can remain in the standard while real servers disable or restrict it.

`VRFY` and `EXPN` are good examples: the wire vocabulary survived, but privacy/security/anti-abuse operations changed whether useful information is returned.

Therefore every command needs two status fields:

```text
normative status
operational availability
```

They are not the same thing.

## 9. SMTP extension history should be a capability genealogy

EHLO created an extensible capability-negotiation model.

Later SMTP features can then be traced as advertised service extensions rather than replacements of the whole protocol.

A mature archive should map branches such as:

```text
EHLO capability framework
      ├─ SIZE
      ├─ 8BITMIME
      ├─ PIPELINING
      ├─ STARTTLS
      ├─ AUTH
      ├─ SMTPUTF8
      └─ others
```

The old transaction core persists while capability branches accumulate.

## 10. Root-hunting classification

SMTP today is best described as:

```text
command grammar: strongly continuous
transaction model: strongly continuous
reply-code interface: strongly continuous
extension mechanism: later branch
routing environment: heavily evolved
security/abuse practice: heavily evolved
some early verbs: extinct
```

## Primary source spine

- RFC 821 — 1982 SMTP;
- RFC 1425 and descendants — SMTP extension framework;
- RFC 5321 — modern consolidated SMTP specification.

## Next excavation

- machine-readable command genealogy;
- reply-code genealogy and enhanced status codes;
- exact RFC introduction/obsolescence for every command;
- sendmail/Postfix/Exim command handling across releases;
- AUTH/STARTTLS/8BITMIME/SMTPUTF8 branches;
- real session captures comparing RFC 821-era and modern dialogues;
- security/operational history of VRFY and EXPN.

---

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
