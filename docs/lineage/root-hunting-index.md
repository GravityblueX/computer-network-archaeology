# Root-Hunting Index — 寻根活动

This index groups excavations that start from something still observable in modern networking and trace it backward.

## Method

- [`../methodology/root-hunting.md`](../methodology/root-hunting.md) — how to distinguish text lineage, wire lineage, implementation lineage, operational lineage and institutional lineage.

## Living packet fields

- [`ipv4-header-field-survivorship.md`](ipv4-header-field-survivorship.md) — RFC 791 header fields: what stayed, what changed meaning, what became baggage.
- [`icmp-type-code-survivorship.md`](icmp-type-code-survivorship.md) — living and extinct ICMP message branches.
- [`living-standards-still-on-wire.md`](living-standards-still-on-wire.md) — broad survey of old standards still directly recognizable on modern wires.
- [`tcp-rfc793-to-rfc9293-living-standard.md`](tcp-rfc793-to-rfc9293-living-standard.md) — obsolete document, living protocol.

## Living registries and extensibility containers

- [`dns-rfc1034-1035-living-core.md`](dns-rfc1034-1035-living-core.md) — 1987 DNS core surviving under an extension forest.
- [`dns-rr-type-genealogy.md`](dns-rr-type-genealogy.md) — A/NS/MX-era RR container growing AAAA, SRV, CAA, SVCB/HTTPS and experimental branches.

## Living command languages

- [`smtp-command-reply-survivorship.md`](smtp-command-reply-survivorship.md) — RFC 821 verbs/replies still visible in modern SMTP sessions, plus extinct verbs.
- [`smtp-message-format-mime-living-core.md`](smtp-message-format-mime-living-core.md) — mail transport, message format and MIME as distinct living layers.

## Cross-protocol fossils

- [`mime-content-type-to-http-media-types.md`](mime-content-type-to-http-media-types.md) — MIME's media-type abstraction crossing from email into HTTP.

## Operational fossils

- [`../operations/icmp-ping-traceroute.md`](../operations/icmp-ping-traceroute.md) — how ICMP/TTL protocol primitives became operator tools.
- [`tcp-congestion-collapse-to-jacobson.md`](tcp-congestion-collapse-to-jacobson.md) — operational failure feeding back into transport implementation design.

## Implementation fossils

- [`../software/bind-dns-implementation-history.md`](../software/bind-dns-implementation-history.md) — DNS standards becoming a long-lived Unix daemon ecosystem.
- [`../software/delivermail-sendmail-routing-engine.md`](../software/delivermail-sendmail-routing-engine.md) — multi-network mail operations becoming sendmail routing/configuration machinery.

## Machine-readable roots

Representative structured lineage records:

- `LIN-0107` — RFC 793 TCP → RFC 9293;
- `LIN-0111` — RFC 1034/1035 DNS core → modern extension ecosystem;
- `LIN-0112` — IPv4 TOS octet → Differentiated Services field;
- `LIN-0113` — IPv4 Identification semantics → RFC 6864;
- `LIN-0114` — DNS RR framework → AAAA;
- `LIN-0115` — DNS RR framework → SVCB/HTTPS;
- `LIN-0116` — MIME media types → HTTP media types;
- `LIN-0117` — RFC 821 command core → modern SMTP command core.

## The key question

When looking at a current packet, configuration, daemon, command or failure mode, ask:

> **How much of this is new, and how much is old machinery that never stopped running?**

That is the archive's root-hunting activity.
