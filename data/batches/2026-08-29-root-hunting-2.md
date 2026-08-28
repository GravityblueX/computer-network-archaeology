# 2026-08-29 Root-Hunting Batch 2 — Option and Registry Fossils

Theme: **extension containers as technical tree rings**.

This batch asks what happens when a protocol's outer skeleton survives for decades while options, type registries, command capabilities and body formats keep accumulating descendants.

## Narrative outputs

- `docs/lineage/ipv4-options-cemetery-pmtud.md`
- `docs/lineage/dscp-ecn-shared-octet.md`
- `docs/lineage/icmp-type-code-full-survivorship.md`
- `docs/lineage/tcp-options-genealogy.md`
- `docs/lineage/dns-extension-forest-dnssec-naptr-sshfp-tlsa.md`
- `docs/lineage/smtp-ehlo-capability-genealogy.md`
- `docs/lineage/mime-multipart-to-form-data.md`

## Structured artifacts

- `ART-0166` — IPv4 Options extension mechanism / cemetery
- `ART-0167` — IPv4 Path MTU Discovery / RFC 1191 generation
- `ART-0168` — DSCP/ECN shared-octet semantic lineage
- `ART-0169` — ICMPv4 Type/Code survivorship map
- `ART-0170` — TCP Window Scale/Timestamps option family
- `ART-0171` — TCP Selective Acknowledgment option family
- `ART-0172` — DNSSEC core extension family
- `ART-0173` — SMTP EHLO service-extension framework
- `ART-0174` — multipart/form-data Web form-upload media type

## Structured sources

- `SRC-0156` — RFC 1191 Path MTU Discovery
- `SRC-0157` — RFC 7126 IPv4 option filtering guidance
- `SRC-0158` — RFC 3168 ECN
- `SRC-0159` — RFC 7323 TCP Window Scale/Timestamps
- `SRC-0160` — RFC 2018 TCP SACK
- `SRC-0161` — RFC 4033 DNSSEC introduction/core relationship
- `SRC-0162` — IANA SMTP Service Extensions registry
- `SRC-0163` — RFC 7578 multipart/form-data
- `SRC-0164` — RFC 6838 media-type registration history
- `SRC-0165` — IANA ICMP Parameters registry

## Structured lineages

- `LIN-0118` — IPv4 fragmentation controls → Path MTU Discovery
- `LIN-0119` — Differentiated Services field → DSCP/ECN shared semantics
- `LIN-0120` — TCP living core → Window Scale/Timestamps option family
- `LIN-0121` — TCP cumulative ACK core → SACK option layer
- `LIN-0122` — DNS core → DNSSEC extension family
- `LIN-0123` — SMTP transaction core → EHLO extension framework
- `LIN-0124` — MIME multipart model → multipart/form-data

## Principal findings

### Extension containers become registries of historical time

The same design pattern appears repeatedly:

```text
stable outer mechanism
       ↓
numbered/typed extension slot
       ↓
new branches over decades
       ↓
living + deprecated + obsolete entries coexist
```

Examples:

- IPv4 Options;
- ICMP Types/Codes;
- TCP option Kinds;
- DNS RR TYPEs;
- SMTP EHLO keywords;
- Internet media types.

### A field can survive while semantics move

The IPv4 TOS/DS/ECN octet demonstrates that wire-position continuity is not semantic continuity.

### Later algorithms can grow from old primitive bits

PMTUD is built from the old DF bit plus ICMP feedback rather than from a newly designed packet header.

### A SYN is a protocol-history negotiation packet

MSS, Window Scale, SACK and Timestamps expose different historical layers inside one modern TCP handshake.

### Registries remember dead branches

ICMP Source Quench and old IPv4 options remain visible as named/deprecated history even after ordinary operational use disappears.

### Protocol abstractions can migrate between ecosystems

MIME multipart framing and the media-type system moved from mail into HTTP/Web form uploads without making HTTP a descendant of MIME as a whole.

## Next targets

- complete IPv4 Option-number cemetery;
- RFC 1191 PMTUD → PLPMTUD / IPv6 Packet Too Big lineage;
- DiffServ PHB and ECN/AccECN history;
- TCP option Kind registry and option-space exhaustion;
- DNSSEC predecessor generations and algorithm registry;
- full SMTP EHLO keyword chronology with implementation support dates;
- RFC 1867 → RFC 2388 → RFC 7578 browser-upload chain;
- raw packet examples pairing current captures with original RFC diagrams.

## Authorship

Research and primary drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
