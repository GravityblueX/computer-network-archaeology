# Ledger synchronization queue

The structured `records/` tree can temporarily advance ahead of the flat discovery CSV ledgers.

This file exists to make that state explicit rather than allowing “ghost” records to appear silently.

## Rule

- `records/artifacts/*.json`, `records/sources/*.json`, and `records/lineages/*.json` are claim-level research records.
- `data/artifact-ledger.csv`, `data/source-ledger.csv`, and `data/lineage-ledger.csv` are flat discovery/index views.
- When a research burst creates many structured records, do **not** risk destructive whole-file replacement merely to update a tail counter.
- Queue the new IDs here, then perform a verified batch merge against the complete current CSV blobs.
- After a successful merge, remove the synchronized entries from this queue.

## Pending artifact-ledger promotion

Structured records created and verified in the 2026-08-29 research bursts:

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
- `ART-0134` — ARP / RFC 826
- `ART-0135` — Proxy ARP / RFC 1027
- `ART-0136` — UDP / RFC 768
- `ART-0137` — ICMP / RFC 792
- `ART-0138` — Telnet / RFC 854 generation
- `ART-0139` — FTP / RFC 959 generation
- `ART-0140` — DNS MX mail-routing model / RFC 974 generation
- `ART-0141` — MIME / RFC 2045 generation

Reserved/identified intermediate artifact IDs that should be created or promoted during the same batch rather than silently reused:

- `ART-0116` — DHCP / RFC 1531 generation
- `ART-0117` — DHCP / RFC 1541 generation
- `ART-0120` — PPP / RFC 1134 generation
- `ART-0121` — PPP / RFC 1171 generation
- `ART-0122` — PPP / RFC 1331 generation
- `ART-0123` — PPP / RFC 1548 generation
- `ART-0126` — OSPF / RFC 1131 generation
- `ART-0127` — OSPFv2 / RFC 1247 generation

Future structured artifacts from the current narrative batch should begin at `ART-0142` unless the flat-ledger merge discovers a concurrent assignment.

## Pending source-ledger promotion

Structured source records already created:

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

Reserved source IDs to fill during batch promotion/revision-diff work:

- `SRC-0100` — RFC 1541 DHCP
- `SRC-0104` — RFC 1171 PPP
- `SRC-0105` — RFC 1331 PPP
- `SRC-0106` — RFC 1548 PPP
- `SRC-0108` — RFC 1549 PPP framing
- `SRC-0109` — RFC 1662 PPP HDLC-like framing
- `SRC-0111` — RFC 1131 OSPF
- `SRC-0112` — RFC 1247 OSPFv2
- `SRC-0114` — RFC 2328 OSPFv2

High-value source records still to promote from the new narratives include RFC 318, RFC 764, RFC 114, RFC 354, RFC 765, RFC 883, RFC 1035, RFC 918, RFC 937, RFC 1081, RFC 1939, RFC 1064, RFC 1176, RFC 1730 and RFC 3501.

Future newly assigned source IDs should begin at `SRC-0129` unless merge-time verification finds a concurrent assignment.

## Pending lineage-ledger promotion

Structured lineage edges already created:

- `LIN-0085` — RARP → BOOTP bootstrap-role generalization
- `LIN-0086` — BOOTP → DHCP direct documented derivation
- `LIN-0087` — SLIP ↔ PPP operational coexistence without invented formal ancestry
- `LIN-0088` — OSI IS-IS → Integrated IS-IS direct derivation
- `LIN-0089` — RIP ↔ OSPF parallel IGP families / negative-lineage guard
- `LIN-0090` — OSPF ↔ Integrated IS-IS parallel link-state families / negative-lineage guard
- `LIN-0091` — FTP-related ARPANET mail practice → dedicated MTP role
- `LIN-0092` — MTP → SMTP formal replacement lineage
- `LIN-0093` — SMTP → ESMTP extension-framework continuity
- `LIN-0094` — ARP → Proxy ARP documented derivation/reuse
- `LIN-0095` — RFC 764 Telnet → RFC 854 formal revision
- `LIN-0096` — Telnet NVT/control conventions carried into FTP control connection
- `LIN-0097` — RFC 765 FTP → RFC 959 formal revision
- `LIN-0098` — DNS MD/MF mail-binding model → MX replacement
- `LIN-0099` — RFC 822 message framework carried into MIME extension architecture

Future newly assigned lineage IDs should begin at `LIN-0100` unless merge-time verification finds a concurrent assignment.

## Narrative files created in the same bursts

Earlier burst:

- `docs/lineage/rarp-bootp-dhcp-host-configuration.md`
- `docs/lineage/slip-to-ppp-point-to-point-links.md`
- `docs/lineage/igp-families-rip-hello-ospf-isis.md`
- `docs/lineage/ftp-mail-mtp-smtp-esmtp.md`

Host/application batch:

- `docs/lineage/arp-address-resolution-proxy-arp.md`
- `docs/lineage/udp-icmp-ip-companion-protocols.md`
- `docs/lineage/telnet-nvt-option-negotiation.md`
- `docs/lineage/ftp-control-data-evolution.md`
- `docs/lineage/dns-mail-routing-md-mf-mx.md`
- `docs/lineage/mail-access-mime-pop-imap.md`
- `docs/lineage/2026-08-29-host-application-batch.md`

`docs/lineage/README.md` should be updated to index the FTP-mail and host/application batch together during the next index synchronization pass.

## Batch-merge checklist

Before clearing entries from this queue:

1. fetch the complete latest CSV blob;
2. verify the current last ID and detect any concurrent additions;
3. validate ID uniqueness;
4. append/promote rows without changing prior data;
5. validate CSV quoting/column counts;
6. confirm every `records/` ID is discoverable from the flat ledger;
7. update `docs/lineage/README.md` and `catalogs/lineages.md` if needed;
8. remove only entries proven synchronized.

This queue is archival hygiene, not a second master database.