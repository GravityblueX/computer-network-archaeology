# Ledger synchronization queue

The structured `records/` tree can temporarily advance ahead of the flat discovery CSV ledgers. This queue makes that state explicit so claim-level research never becomes an invisible “ghost” record.

## Rule

- `records/artifacts/*.json`, `records/sources/*.json`, and `records/lineages/*.json` are claim-level research records.
- `data/artifact-ledger.csv`, `data/source-ledger.csv`, and `data/lineage-ledger.csv` are flat discovery/index views.
- Do **not** destructively replace a large CSV merely to advance a tail ID.
- Before a batch merge: fetch the complete latest blob, detect concurrent additions, validate IDs and CSV columns, append/promote rows, then verify every structured ID is discoverable from the flat view.
- Remove entries from this queue only after successful verification.

---

# Pending artifact-ledger promotion

Structured artifacts already present in `records/artifacts/` but not yet guaranteed present in the flat artifact ledger:

## Bootstrap / point-to-point / routing / mail-transfer burst

- `ART-0114` — RARP / RFC 903
- `ART-0115` — BOOTP / RFC 951
- `ART-0118` — DHCP / RFC 2131 generation
- `ART-0119` — SLIP / RFC 1055
- `ART-0124` — PPP / RFC 1661 generation
- `ART-0125` — RIP / RFC 1058 generation
- `ART-0128` — OSPFv2 / RFC 1583 generation
- `ART-0129` — OSI IS-IS / RFC 1142 representation
- `ART-0130` — Integrated IS-IS / RFC 1195
- `ART-0131` — Mail Transfer Protocol / RFC 772
- `ART-0132` — SMTP / RFC 821 generation
- `ART-0133` — SMTP Service Extensions / ESMTP / RFC 1425 generation

Reserved intermediate IDs still to create/promote during revision-diff work:

- `ART-0116` — DHCP / RFC 1531 generation
- `ART-0117` — DHCP / RFC 1541 generation
- `ART-0120` — PPP / RFC 1134 generation
- `ART-0121` — PPP / RFC 1171 generation
- `ART-0122` — PPP / RFC 1331 generation
- `ART-0123` — PPP / RFC 1548 generation
- `ART-0126` — OSPF / RFC 1131 generation
- `ART-0127` — OSPFv2 / RFC 1247 generation

## Host/application protocol burst

- `ART-0134` — ARP / RFC 826
- `ART-0135` — Proxy ARP / RFC 1027
- `ART-0136` — UDP / RFC 768
- `ART-0137` — ICMP / RFC 792
- `ART-0138` — Telnet / RFC 854 generation
- `ART-0139` — FTP / RFC 959 generation
- `ART-0140` — DNS MX mail-routing model / RFC 974 generation
- `ART-0141` — MIME / RFC 2045 generation

## Standards → implementation → operations burst

- `ART-0142` — NAT / RFC 1631
- `ART-0143` — Traditional NAT / Basic NAT / NAPT / RFC 3022 generation
- `ART-0144` — Nagle TCP small-packet sender rule / RFC 896
- `ART-0145` — Jacobson/Karels congestion-control implementation generation
- `ART-0146` — Mike Muuss Unix `ping`
- `ART-0147` — Van Jacobson 4BSD `traceroute`
- `ART-0148` — Berkeley `delivermail` → `sendmail` implementation lineage
- `ART-0149` — Berkeley Internet Name Domain (BIND) implementation lineage

**Next unreserved artifact ID: `ART-0150`**, subject to merge-time verification against concurrent work.

---

# Pending source-ledger promotion

## Earlier structured RFC/source records

- `SRC-0097` — RFC 903 RARP
- `SRC-0098` — RFC 951 BOOTP
- `SRC-0099` — RFC 1531 DHCP
- `SRC-0101` — RFC 2131 DHCP
- `SRC-0102` — RFC 1055 SLIP
- `SRC-0103` — RFC 1134 early PPP
- `SRC-0107` — RFC 1661 PPP
- `SRC-0110` — RFC 1058 RIP
- `SRC-0113` — RFC 1583 OSPFv2
- `SRC-0115` — RFC 1142 OSI IS-IS
- `SRC-0116` — RFC 1195 Integrated IS-IS
- `SRC-0117` — RFC 772 Mail Transfer Protocol
- `SRC-0118` — RFC 788 SMTP
- `SRC-0119` — RFC 821 SMTP
- `SRC-0120` — RFC 1425 SMTP Service Extensions
- `SRC-0121` — RFC 826 ARP
- `SRC-0122` — RFC 1027 Proxy ARP
- `SRC-0123` — RFC 768 UDP
- `SRC-0124` — RFC 792 ICMP
- `SRC-0125` — RFC 854 Telnet
- `SRC-0126` — RFC 959 FTP
- `SRC-0127` — RFC 974 DNS mail routing / MX
- `SRC-0128` — RFC 2045 MIME

Reserved intermediate source IDs:

- `SRC-0100` — RFC 1541 DHCP
- `SRC-0104` — RFC 1171 PPP
- `SRC-0105` — RFC 1331 PPP
- `SRC-0106` — RFC 1548 PPP
- `SRC-0108` — RFC 1549 PPP framing
- `SRC-0109` — RFC 1662 PPP HDLC-like framing
- `SRC-0111` — RFC 1131 OSPF
- `SRC-0112` — RFC 1247 OSPFv2
- `SRC-0114` — RFC 2328 OSPFv2

## Standards / implementation / operations source records

- `SRC-0129` — RFC 1631 NAT
- `SRC-0130` — RFC 3022 Traditional NAT / NAPT
- `SRC-0131` — RFC 896 TCP congestion / Nagle
- `SRC-0132` — Jacobson & Karels, *Congestion Avoidance and Control* (SIGCOMM 1988)
- `SRC-0133` — Mike Muuss, *The Story of the PING Program*
- `SRC-0134` — reproduced Van Jacobson December 1988 traceroute announcement (primary archive still sought)
- `SRC-0135` — Sendmail project/history paper
- `SRC-0136` — Berkeley report UCB/CSD-84-182, *The Berkeley Internet Name Domain Server*

High-value source records still to promote from existing narratives include RFC 318, RFC 764, RFC 114, RFC 354, RFC 765, RFC 883, RFC 1035, RFC 918, RFC 937, RFC 1081, RFC 1939, RFC 1064, RFC 1176, RFC 1730, RFC 3501, RFC 970, UCB/CSD-84-177, ISC BIND history, original BSD sendmail/delivermail source distributions, original traceroute source/archive message and the earliest surviving ping source.

**Next unreserved source ID: `SRC-0137`**, subject to verification.

---

# Pending lineage-ledger promotion

- `LIN-0085` — RARP → BOOTP bootstrap-role generalization
- `LIN-0086` — BOOTP → DHCP documented derivation
- `LIN-0087` — SLIP ↔ PPP coexistence without invented ancestry
- `LIN-0088` — OSI IS-IS → Integrated IS-IS derivation
- `LIN-0089` — RIP ↔ OSPF negative-lineage guard
- `LIN-0090` — OSPF ↔ Integrated IS-IS negative-lineage guard
- `LIN-0091` — FTP-related ARPANET mail practice → dedicated MTP role
- `LIN-0092` — MTP → SMTP formal replacement
- `LIN-0093` — SMTP → ESMTP extension-framework continuity
- `LIN-0094` — ARP → Proxy ARP documented derivation/reuse
- `LIN-0095` — RFC 764 Telnet → RFC 854 revision
- `LIN-0096` — Telnet NVT/control conventions → FTP control connection
- `LIN-0097` — RFC 765 FTP → RFC 959 revision
- `LIN-0098` — DNS MD/MF → MX replacement
- `LIN-0099` — RFC 822 message framework → MIME extension architecture
- `LIN-0100` — RFC 1631 NAT → RFC 3022 Traditional NAT/NAPT revision
- `LIN-0101` — ICMP Echo → Muuss `ping` operational tool
- `LIN-0102` — IPv4 TTL + ICMP Time Exceeded → `traceroute`
- `LIN-0103` — Berkeley ARPANET/UUCP/BerkNet mail problem → delivermail/sendmail implementation
- `LIN-0104` — early DNS architecture → Berkeley BIND implementation
- `LIN-0105` — Nagle small-packet rule ↔ Jacobson/Karels congestion-control generation (different problems, coexisting mechanisms)
- `LIN-0106` — 1986 Internet congestion-collapse experience → Jacobson/Karels implementation redesign

**Next unreserved lineage ID: `LIN-0107`**, subject to verification.

---

# Narrative files awaiting flat-index / human-index synchronization

## Earlier lineage burst

- `docs/lineage/rarp-bootp-dhcp-host-configuration.md`
- `docs/lineage/slip-to-ppp-point-to-point-links.md`
- `docs/lineage/igp-families-rip-hello-ospf-isis.md`
- `docs/lineage/ftp-mail-mtp-smtp-esmtp.md`

## Host/application burst

- `docs/lineage/arp-address-resolution-proxy-arp.md`
- `docs/lineage/udp-icmp-ip-companion-protocols.md`
- `docs/lineage/telnet-nvt-option-negotiation.md`
- `docs/lineage/ftp-control-data-evolution.md`
- `docs/lineage/dns-mail-routing-md-mf-mx.md`
- `docs/lineage/mail-access-mime-pop-imap.md`
- `docs/lineage/2026-08-29-host-application-batch.md`

## Standards → implementation → operations burst

- `docs/lineage/nat-address-reuse-end-to-end.md`
- `docs/lineage/tcp-congestion-collapse-to-jacobson.md`
- `docs/operations/icmp-ping-traceroute.md`
- `docs/software/delivermail-sendmail-routing-engine.md`
- `docs/software/bind-dns-implementation-history.md`

`docs/lineage/README.md`, `docs/INDEX.md` and `catalogs/lineages.md` should be synchronized in a dedicated index pass after the pending CSV merge rather than edited piecemeal during every excavation burst.

---

# Batch-merge checklist

Before clearing any entry:

1. fetch the complete latest CSV blob;
2. verify current last IDs and concurrent additions;
3. validate ID uniqueness and reserved gaps;
4. append/promote rows without changing prior rows;
5. validate CSV quoting and column counts;
6. confirm every `records/` ID is discoverable from flat ledgers;
7. update `docs/lineage/README.md`, `docs/INDEX.md` and `catalogs/lineages.md`;
8. remove only entries proven synchronized.

This queue is archival hygiene, not a second master database.