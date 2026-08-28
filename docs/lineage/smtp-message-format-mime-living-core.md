# SMTP, Internet Message Format and MIME: Old Mail Standards Still Visible in Every Message

Internet mail is one of the best examples of a modern system made from several old standards that survived **side by side rather than collapsing into one protocol**.

A contemporary email commonly reflects at least four separate historical lineages:

```text
transport:      SMTP
message syntax: RFC 822 → RFC 2822 → RFC 5322
body extension: MIME
retrieval:      POP / IMAP
routing:        DNS MX
```

The mistake to avoid is saying simply:

> email uses SMTP.

SMTP moves mail. It does not define every property of an email message, mailbox, attachment, or client/server access model.

---

## 1. Transport lineage: SMTP survived by consolidation and extension

Early ARPANET mail had roots in FTP-related mail functions and dedicated Mail Transfer Protocol experiments. By RFC 821 in 1982, SMTP became the core Internet mail-transfer protocol.

Later SMTP documents extended and consolidated the protocol without abandoning the recognizable command/reply architecture.

A simplified standards lineage is:

```text
FTP-era mail functions
       ↓
MTP / early SMTP work
       ↓
RFC 821 SMTP
       ↓
ESMTP extension framework
       ↓
RFC 2821
       ↓
RFC 5321
```

RFC 5321 describes itself as the basic protocol for Internet electronic-mail transport and consolidates/updates earlier documents.

Primary source:

- RFC 5321: https://www.rfc-editor.org/info/rfc5321/

---

## 2. Commands and reply codes are living historical interfaces

The SMTP conversational model remains immediately recognizable:

```text
client command
server numeric reply
client command
server reply
...
```

Core ideas such as envelope sender/recipients, staged transaction processing, and server reply codes survived across generations.

A modern SMTP session still visibly belongs to the same protocol family even though authentication, TLS, internationalization and numerous extensions arrived later.

This is **protocol continuity through extensible command grammar**.

---

## 3. Message format is a separate genealogy

What the recipient eventually reads is governed by a different standards family.

RFC 5322 explicitly says that it revises RFC 2822, which itself superseded RFC 822.

The recognizable message structure remains:

```text
header fields
CRLF
message body
```

Header fields retain the famous textual form:

```text
Field-Name: field value
```

Examples include:

- Date;
- From;
- Sender;
- Reply-To;
- To;
- Cc;
- Message-ID;
- In-Reply-To;
- References;
- Subject.

This syntax is so ordinary today that its historical nature is easy to miss.

Primary source:

- RFC 5322: https://www.rfc-editor.org/info/rfc5322/

---

## 4. RFC 822 did not die when RFC 5322 arrived

The document was superseded.

The message-format lineage continued.

RFC 5322 deliberately preserves a large amount of historical grammar and even contains obsolete-syntax rules so implementations can parse older Internet messages.

That is archival compatibility encoded directly into a modern standard.

A mail parser is therefore partly a historical interpreter.

---

## 5. MIME: extending message bodies without replacing Internet mail

The original Internet message format was heavily oriented toward US-ASCII text.

MIME extended this world so messages could carry:

- non-ASCII text character sets;
- non-text media;
- multipart bodies;
- transfer encodings;
- media/content types;
- richer header information.

RFC 2045 says explicitly that MIME extends the RFC 822 message world rather than replacing the entire mail architecture.

Primary source:

- RFC 2045: https://www.rfc-editor.org/info/rfc2045/

So the lineage is not:

```text
RFC 822 → MIME replaces RFC 822
```

It is:

```text
Internet message format
        +
MIME body/content extensions
```

This is a classic **carried-over + extension** relationship.

---

## 6. Multipart boundaries are living fossils

A current attachment-bearing message may still contain structures like:

```text
Content-Type: multipart/...
Content-Transfer-Encoding: ...
Content-Disposition: ...

--boundary-string
...
--boundary-string--
```

To most users this is invisible behind a mail client.

But raw message source reveals the historical standard directly.

Email clients are still assembling and parsing a decades-old textual protocol/data format under a modern GUI.

---

## 7. DNS MX is another independent layer

SMTP does not by itself answer:

> Which server should receive mail for a domain?

That responsibility migrated into DNS mail-routing data.

The archive already tracks:

- `dns-mail-routing-md-mf-mx.md`

A simplified path is:

```text
recipient domain
      ↓ DNS query
MX records
      ↓ preference/order
mail exchanger host
      ↓
SMTP connection
```

This is a strong example of two old standards co-evolving without merging.

---

## 8. POP and IMAP solve a different problem again

SMTP is about message transport/submission/relay.

Mailbox access is separate.

### POP3

RFC 1939 defines a deliberately simple download-oriented mailbox access model.

### IMAP

The modern IMAP4rev2 specification, RFC 9051, describes remote mailbox manipulation, flags, searching, selective fetch, folders and offline resynchronization.

Primary records:

- POP3 RFC 1939: https://www.rfc-editor.org/info/rfc1939/
- IMAP4rev2 RFC 9051: https://www.rfc-editor.org/info/rfc9051/

RFC 9051 explicitly separates message access from message posting/submission.

So again:

```text
mail transport ≠ mailbox access
```

---

## 9. One email can therefore carry multiple decades of standards

A modern message path can look like:

```text
message authored in a GUI
        ↓
RFC 5322 message structure
        +
MIME body/attachment representation
        ↓
SMTP submission/relay
        ↓
DNS MX routing
        ↓
mail store
        ↓
IMAP/POP access
```

Each layer has a separate historical genealogy.

The modern mail system is not one protocol. It is a federation of old interfaces.

---

## 10. Sendmail made the standards operational

Standards history alone misses the daemon/configuration layer.

The repository tracks Berkeley's real multi-network mail-routing environment and the transition:

```text
ARPANET + UUCP + BerkNet
       ↓
delivermail
       ↓
sendmail
```

Related excavation:

- `delivermail-sendmail-mail-routing.md`

Sendmail turned protocol and routing rules into queueing, rewriting, mailer selection and site-local policy.

This is the implementation genealogy under the standards genealogy.

---

## 11. Why old text formats survived

Text protocols have drawbacks, but they also gave Internet software important survival properties:

- easy manual inspection;
- easy logging;
- human-debuggable command/reply sessions;
- extensible headers;
- unknown-header tolerance;
- incremental deployment;
- compatibility with old stored messages;
- gateways between heterogeneous mail systems.

This helps explain why raw modern mail remains astonishingly readable.

---

## 12. Compatibility creates archaeological obligations

Modern implementations often need to understand obsolete or historical syntax because stored mail can live for decades.

This differs from transient packet protocols.

A mail archive may contain messages generated under old conventions long after those standards were superseded.

Therefore a current parser can be forced to preserve historical knowledge.

The data itself carries the old protocol forward.

---

## 13. Living-standard categories represented by mail

Mail demonstrates several survival modes at once.

### `obsoleted-document-living-format`

```text
RFC 822 → RFC 2822 → RFC 5322
```

The documents revise one another while the format lineage remains.

### `living-core-with-extension-forest`

```text
SMTP core + ESMTP extensions
```

### `extension-layer-over-living-format`

```text
RFC 822/5322 message model + MIME
```

### `parallel-role-protocols`

```text
SMTP transport
POP/IMAP mailbox access
DNS MX routing
```

They cooperate but are not revisions of one another.

---

## 14. What changed radically despite continuity

The surrounding mail ecosystem changed enormously:

- spam and abuse defenses;
- TLS;
- authentication;
- submission separation;
- SPF/DKIM/DMARC;
- internationalization;
- large attachment handling;
- webmail;
- cloud mail storage;
- mobile sync;
- search/indexing;
- anti-malware scanning.

Yet underneath, raw messages still expose `From:`, `To:`, `Date:`, `Message-ID:`, MIME content types and textual SMTP ancestry.

That is exactly the kind of continuity this archive should preserve.

---

## Primary sources

- RFC 821 — Simple Mail Transfer Protocol: https://www.rfc-editor.org/info/rfc821/
- RFC 5321 — Simple Mail Transfer Protocol: https://www.rfc-editor.org/info/rfc5321/
- RFC 822 — Standard for the Format of ARPA Internet Text Messages: https://www.rfc-editor.org/info/rfc822/
- RFC 5322 — Internet Message Format: https://www.rfc-editor.org/info/rfc5322/
- RFC 2045 — MIME Part One: https://www.rfc-editor.org/info/rfc2045/
- RFC 1939 — POP3: https://www.rfc-editor.org/info/rfc1939/
- RFC 9051 — IMAP4rev2: https://www.rfc-editor.org/info/rfc9051/

## Related archive excavations

- `ftp-mail-mtp-smtp-esmtp.md`
- `dns-mail-routing-md-mf-mx.md`
- `mail-access-mime-pop-imap.md`
- `delivermail-sendmail-mail-routing.md`
- `living-standards-still-on-wire.md`

## Next excavation tasks

- RFC 822 → 2822 → 5322 syntax diff;
- RFC 821 → 2821 → 5321 command/reply diff;
- RFC 1425/ESMTP extension genealogy;
- MIME RFC 1341/1521/2045 revision tree;
- media-type registry history;
- POP1/POP2/POP3 genealogy;
- IMAP early Stanford versions → IMAP2 → IMAP4 → rev1 → rev2;
- mail submission RFC lineage;
- STARTTLS/AUTH extension history;
- source-level sendmail parsing/routing genealogy;
- preserve representative raw messages from multiple eras where redistribution is lawful.