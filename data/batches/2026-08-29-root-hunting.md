# 2026-08-29 Root-Hunting Batch

Theme: **寻根活动 / root-hunting — identify present-day network behavior that still exposes older standards, fields, command languages and cross-protocol abstractions.**

## Research question

For each modern observable, ask:

> What is the oldest technical form that is still directly recognizable here, and what changed around it?

## Narrative outputs

- `docs/methodology/root-hunting.md`
- `docs/lineage/ipv4-header-field-survivorship.md`
- `docs/lineage/icmp-type-code-survivorship.md`
- `docs/lineage/dns-rr-type-genealogy.md`
- `docs/lineage/smtp-command-reply-survivorship.md`
- `docs/lineage/mime-content-type-to-http-media-types.md`

## Structured artifact outputs

- `ART-0159` — IPv4 TOS → Differentiated Services field semantic lineage
- `ART-0160` — IPv4 Identification field semantic lineage
- `ART-0161` — ICMP Source Quench historical branch
- `ART-0162` — DNS Resource Record typed extension framework
- `ART-0163` — SMTP command/reply transactional core
- `ART-0164` — Internet media-type system descended from MIME
- `ART-0165` — DNS SVCB / HTTPS RR family

## Structured source outputs

- `SRC-0148` — RFC 2474
- `SRC-0149` — RFC 6864
- `SRC-0150` — RFC 2782
- `SRC-0151` — RFC 3596
- `SRC-0152` — RFC 8659
- `SRC-0153` — RFC 9460
- `SRC-0154` — RFC 2046
- `SRC-0155` — RFC 9110

Existing source records also used heavily:

- `SRC-0137` — RFC 791 IPv4
- `SRC-0139` — RFC 792 ICMP
- `SRC-0143` — RFC 1035 DNS core
- `SRC-0119` — RFC 821 SMTP
- `SRC-0144` — RFC 5321 SMTP

## Structured lineage outputs

- `LIN-0112` — RFC 791 TOS octet → RFC 2474 DS field: same wire location, changed semantics
- `LIN-0113` — IPv4 Identification semantics → RFC 6864: same field, narrowed contract
- `LIN-0114` — DNS RR framework → AAAA: new address family inside old typed container
- `LIN-0115` — DNS RR framework → SVCB/HTTPS: 2020s service bootstrap inside 1980s container
- `LIN-0116` — MIME media types → HTTP media types: cross-protocol abstraction reuse
- `LIN-0117` — RFC 821 SMTP command/reply core → modern SMTP: surviving plaintext transaction grammar

## Principal findings

### 1. Wire-format survival and semantic survival are different

IPv4's Type-of-Service octet survived physically while its interpretation changed into the Differentiated Services field.

IPv4 Identification survived physically while RFC 6864 narrowed the conditions in which its value must carry fragment identity semantics.

### 2. A type registry can become an archaeological record

DNS resource records preserve both winners and abandoned branches. The same TYPE/CLASS/TTL/RDATA architecture carries:

- 1980s address/naming data;
- mail routing;
- IPv6 AAAA records;
- service location SRV;
- certificate authorization CAA;
- modern SVCB/HTTPS connection bootstrap.

### 3. Operator-visible command languages can outlive generations of software

Modern SMTP still exposes a transaction skeleton immediately recognizable from RFC 821: HELO/EHLO, MAIL, RCPT, DATA, RSET, NOOP, QUIT and three-digit reply codes.

At the same time, old verbs such as SEND/SOML/SAML/TURN form an extinct branch.

### 4. Abstractions can escape their original protocol

MIME created a generalized `type/subtype; parameters` media-type model for Internet message bodies.

HTTP later explicitly reused RFC 2046 media types for `Content-Type` and `Accept`.

This is not MIME → HTTP ancestry. It is **one abstraction crossing protocol families**.

### 5. One old protocol can contain both living and extinct message types

ICMP contains strongly living branches such as Echo and Time Exceeded, operationally constrained branches such as Redirect, and extinct branches such as Source Quench.

Therefore “protocol alive/dead” is too coarse. Survivorship must often be recorded at field/message/command granularity.

## Next root-hunting targets

High-value continuations:

- IPv4 options cemetery and Path MTU / DF history;
- TOS → DSCP → ECN bit genealogy;
- complete ICMP Type/Code survivorship table;
- DNS TYPE registry timeline including DNSSEC/NAPTR/TLSA/SSHFP;
- SMTP reply-code and EHLO extension genealogy;
- MIME multipart/form-data → HTTP form upload lineage;
- media-type registration history and MIME sniffing;
- BSD/Linux header structs and protocol implementation diffs;
- packet-capture examples pairing old RFC diagrams with current traffic.

## Authorship

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
