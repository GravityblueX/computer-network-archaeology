# SMTP EHLO Capability Genealogy: How an Old Command Language Learned New Tricks

SMTP survived partly because it learned to negotiate extensions instead of forcing every server to understand every future feature.

The crucial transition is from a small fixed command set toward the ESMTP capability model introduced through EHLO.

This document treats EHLO keywords as a registry-level genealogy.

## 1. The old transaction skeleton remains

The classic transaction still revolves around:

```text
MAIL FROM
RCPT TO
DATA
```

with session/control verbs such as HELO/EHLO, RSET, NOOP and QUIT.

That core remains recognizable across decades.

## 2. EHLO creates an extension negotiation surface

ESMTP changed the growth model.

A client says EHLO. The server returns a 250 response with one or more extension keywords.

The client can then conditionally use capabilities the server explicitly advertised.

This is a major architectural shift:

```text
old model:
command is either universally understood or risky

extension model:
server advertises capability
client uses extension only when negotiated
```

The old SMTP session becomes a capability-negotiation platform.

## 3. SIZE: operational policy becomes protocol-visible

The SIZE extension lets a server advertise message-size support and lets a client declare a message size before sending the entire body.

This turns an operational constraint — mailbox/server/storage policy — into a negotiated SMTP capability.

It also allows failure to occur before expensive content transfer.

## 4. 8BITMIME: message-body transport grows beyond strict 7-bit assumptions

8BITMIME allows SMTP transport of MIME bodies containing 8-bit octets under defined rules.

Importantly, it does not simply mean "binary SMTP." The historical 7-bit line-oriented transport assumptions remain visible in the restrictions and extension semantics.

The extension therefore bridges:

```text
old SMTP transport constraints
        ↕
MIME content representation
        ↕
8-bit transport capability
```

## 5. PIPELINING: same command grammar, different timing

PIPELINING changes when commands may be sent, not the identity of the classic SMTP verbs.

This is a subtle but important type of evolution:

> protocol performance can change by altering command scheduling while preserving command semantics.

The wire language remains recognizable even when round-trip behavior changes.

## 6. DSN: richer delivery-status semantics

Delivery Status Notification extensions add parameters and reporting controls around message delivery.

Again the core transaction is retained. New information is attached to MAIL/RCPT behavior and later delivery reports.

This makes SMTP a useful example of **extension by parameters rather than replacement of verbs**.

## 7. STARTTLS: security inserted into a plaintext protocol session

STARTTLS upgrades an existing SMTP connection into TLS after capability negotiation.

This is one of the clearest examples of old protocol grammar carrying a much newer security layer:

```text
TCP connection
   ↓
plaintext SMTP EHLO
   ↓ STARTTLS advertised
STARTTLS command
   ↓ TLS handshake
encrypted SMTP continues
```

The old application protocol survives on both sides of a new cryptographic transition.

## 8. AUTH: authentication becomes an advertised service extension

SMTP AUTH adds authentication mechanisms through the extension framework.

The SMTP server's role therefore expands from store-and-forward mail transfer toward authenticated submission/relay environments.

This should not be back-projected into RFC 821-era SMTP.

## 9. The IANA registry is a living fossil record

The IANA SMTP Service Extensions registry records EHLO keywords and their associated parameters/verbs.

That makes the registry itself an archaeological dataset:

- some capabilities became ordinary infrastructure;
- some remain specialized;
- later revisions change references while preserving keywords;
- capability names outlive specific server implementations.

## 10. One modern EHLO response can span decades

A modern server might advertise concepts such as:

```text
SIZE
8BITMIME
PIPELINING
STARTTLS
AUTH
DSN
```

The client is effectively receiving a compact protocol-history manifest.

Each keyword belongs to a different historical problem:

- storage/size policy;
- internationalized message bodies;
- latency/performance;
- transport security;
- user authentication;
- delivery-status reporting.

They coexist because the extension framework gives them a shared negotiation language.

## 11. Root-hunting distinction: verb survival vs extension survival

SMTP genealogy should track at least three things separately:

1. **core command survival** — MAIL/RCPT/DATA etc.;
2. **reply-code survival** — three-digit status grammar;
3. **EHLO capability survival** — extension registry.

A command can remain while its operational environment changes dramatically.

## Sources

- RFC 5321 — Simple Mail Transfer Protocol: https://www.rfc-editor.org/info/rfc5321/
- IANA SMTP Service Extensions registry: https://www.iana.org/assignments/smtp/
- RFC 1870 — SIZE: https://www.rfc-editor.org/info/rfc1870/
- RFC 6152 — 8BITMIME: https://www.rfc-editor.org/info/rfc6152/
- RFC 2920 — PIPELINING: https://www.rfc-editor.org/info/rfc2920/
- RFC 3461 — Delivery Status Notifications: https://www.rfc-editor.org/info/rfc3461/
- RFC 3207 — STARTTLS: https://www.rfc-editor.org/info/rfc3207/
- RFC 4954 — SMTP AUTH: https://www.rfc-editor.org/info/rfc4954/

## Next excavation

- build a chronological EHLO keyword table;
- trace early Sendmail/Postfix/Exim support dates;
- compare message submission on port 587 with relay SMTP;
- AUTH mechanism genealogy;
- STARTTLS deployment history and downgrade problems;
- SMTPUTF8 branch;
- exact reply-code evolution for temporary/permanent/security failures.
