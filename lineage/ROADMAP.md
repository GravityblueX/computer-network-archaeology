# Technology Lineage Roadmap

This roadmap tracks **descent, revision, replacement, coexistence and survival** rather than ordinary chronology.

The unit of completion is an evidence-bearing edge, not a historical slogan.

## Infrastructure

- [x] lineage mission and anti-teleology rules
- [x] lineage edge JSON Schema
- [x] machine-readable lineage discovery ledger
- [x] first structured lineage records
- [x] contributor rules for influence/causality claims
- [ ] automated schema validation
- [ ] duplicate/conflicting-edge detector
- [ ] graph export (JSON-LD/GraphML/CSV)
- [ ] visualization that distinguishes confirmed/probable/disputed edges
- [ ] query layer by scope/property/date
- [ ] edge-level citation/locator linter
- [ ] automatic detection of artifact IDs missing from artifact ledger

## Serial/data-set/interface genealogy

- [x] RS-232 → RS-232-A formal edge
- [x] RS-232-A → Bell 202C/202D implementation edge
- [x] Bell 101/103 chronology conflict preserved
- [x] Bell 103A contemporary existence anchored to 1962 Bell technical literature
- [ ] acquire RS-232 May 1960 complete text
- [ ] acquire RS-232-A complete text
- [ ] acquire RS-232-B complete text
- [ ] acquire RS-232-C complete text
- [ ] field-by-field RS-232 revision diff
- [ ] EIA committee history / drafts / participants
- [ ] earliest V.24 edition and amendment tree
- [ ] V.28 electrical-characteristics revision tree
- [ ] connector/pin allocation history
- [ ] Bell 101A/B/C model tree
- [ ] Bell 103A1/A2/F/etc. model tree
- [ ] automatic calling unit / V.25 lineage
- [ ] Hayes AT command lineage
- [ ] router/terminal-server serial-console afterlife
- [ ] null-modem / DTE-DTE adaptation history

## TCP/IP layering genealogy

- [x] RFC 675 integrated Internet Transmission Control Program identified
- [x] RFC 760 IP IEN ancestry registered
- [x] RFC 761 TCP IEN ancestry registered
- [x] RFC 760 → RFC 791 edge
- [x] RFC 761 → RFC 793 edge
- [x] NCP → TCP/IP operational replacement edge
- [ ] mine IEN 5
- [ ] mine IEN 21
- [ ] mine IEN 27
- [ ] mine IEN 40
- [ ] mine IEN 44
- [ ] mine IEN 55
- [ ] mine IEN 81
- [ ] mine IEN 112
- [ ] mine IEN 124
- [ ] mine IP IEN 26/28/41/54/80/111/123
- [ ] build header/responsibility diff across all versions
- [ ] UDP branch genealogy
- [ ] ICMP branch genealogy
- [ ] TCP congestion-control genealogy (keep separate from early TCP)
- [ ] BSD socket/API genealogy
- [ ] early source-code implementation genealogy

## Ethernet genealogy

- [x] ALOHA → experimental Ethernet documented influence edge
- [x] experimental Ethernet kept separate from 10 Mbit/s Ethernet
- [ ] 1973/1974 PARC memo genealogy
- [ ] experimental Ethernet interface/transceiver revision tree
- [ ] experimental → DIX 10 Mbit/s property-level edges
- [ ] DIX v1 → DIX v2 diff
- [ ] DIX ↔ IEEE 802.3 exact framing/standardization relationships
- [ ] 10BASE5 lineage
- [ ] 10BASE2 lineage
- [ ] 10BASE-T lineage
- [ ] repeater/hub operational lineage
- [ ] bridge lineage
- [ ] spanning-tree lineage
- [ ] Kalpana/multiport-bridge → Ethernet-switch product lineage
- [ ] half-duplex → full-duplex transition
- [ ] autonegotiation genealogy
- [ ] Fast/Gigabit Ethernet physical-layer branch map

## Packet switching / router genealogy

- [ ] IMP routing-algorithm revision tree
- [ ] IMP hardware family tree
- [ ] TIP/Pluribus relationship tree
- [ ] CIGALE routing revisions
- [x] BBN Internet Gateway → later router role edge
- [ ] GGP genealogy
- [ ] EGP genealogy
- [ ] Fuzzball routing software genealogy
- [ ] RIP genealogy
- [ ] HELLO genealogy
- [ ] OSPF design/standardization genealogy
- [ ] IS-IS IP adaptation genealogy
- [ ] BGP-1 → BGP-2 → BGP-3 → BGP-4 formal revision tree
- [ ] route-policy / AS concept genealogy
- [ ] router control-plane vs forwarding-plane separation history

## X.25 / carrier packet-network genealogy

- [x] 1976 X.25 and Triple-X PAD stack first-pass excavation
- [x] IP-over-X.25 coexistence edge preserved
- [ ] X.25 1976 → 1980 → 1984 → 1988 edition diff
- [ ] X.3 parameter revision tree
- [ ] X.28/X.29 revision trees
- [ ] X.75 inter-network genealogy
- [ ] named public packet-network product/service lineages
- [ ] determine documentary relationship to Frame Relay (do not assume successor)
- [ ] determine documentary relationship to ATM (do not assume successor)
- [ ] PAD → terminal-server comparisons with direct vendor/personnel evidence

## Store-and-forward genealogy

- [ ] telegraph store-and-forward ancestry
- [x] UUCP/Usenet mechanism excavation
- [ ] UUCP protocol revision tree (g/f/t/e/etc.)
- [ ] A News → B News → C News release lineage
- [ ] UUCP → NNTP transition
- [ ] email queue/retry genealogy
- [ ] direct influence evidence for later message-queue systems where available

## Naming / directory genealogy

- [ ] ARPANET host naming before HOSTS.TXT centralization
- [ ] HOSTS.TXT format and distribution revision history
- [ ] scaling problem evidence
- [ ] RFC 819/881/882/883 development line
- [ ] RFC 882/883 → RFC 1034/1035 revision relationship
- [ ] resolver API genealogy
- [ ] root server operations genealogy
- [ ] delegation/administrative hierarchy genealogy
- [ ] reverse DNS genealogy

## LAN / enterprise protocol suites

- [ ] PUP → XNS documented design/source genealogy
- [ ] XNS → IPX/SPX relationship
- [ ] DECnet Phase I–V revision tree
- [ ] AppleTalk phase/release genealogy
- [ ] SNA revision/product genealogy
- [ ] NetWare/IPX client/server lineage
- [ ] LAN Manager/SMB genealogy
- [ ] Token Ring standards/product lineage
- [ ] ARCNET revisions

## Access-network genealogy

- [ ] Bell modem speed/modulation tree
- [ ] V.21/V.22/V.22bis/V.32/V.32bis/V.34/V.90/V.92 tree
- [ ] MNP → V.42/V.42bis relationship
- [ ] acoustic coupler → direct-connect modem transition
- [ ] dial-up modem bank → integrated digital modem rack
- [ ] terminal server → remote access server
- [ ] SLIP → PPP transition
- [ ] ISDN dial access genealogy
- [ ] consumer dial-up → broadband access transition (outside core period but useful as descendant endpoint)

## Backbone/institutional genealogy

- [x] Fuzzball → IBM RT NSS replacement edge
- [x] T1 NSFNET → T3 NSFNET replacement edge
- [ ] per-site migration records
- [ ] ANS/ANS CO+RE genealogy
- [ ] FIX-E/FIX-W → NAP transition
- [ ] regional-network → commercial ISP transitions
- [ ] NSF acceptable-use policy → commercialization institutional lineage

## Evidence-quality goals

For every `influenced` edge:

- [ ] direct citation/testimony/design record
- [ ] exact inherited property
- [ ] negative claim limiting overreach

For every `revision-of` edge:

- [ ] both editions identified
- [ ] exact publication dates
- [ ] change summary
- [ ] ideally machine-readable field diff

For every `replaced-by` edge:

- [ ] deployment evidence
- [ ] coexistence window
- [ ] migration method
- [ ] retirement milestone

For every `survives-as` edge:

- [ ] mechanism defined narrowly
- [ ] descendant implementation documented
- [ ] distinguish analogy from direct descent

## Long-term query goals

The lineage graph should eventually answer questions such as:

- Which modern interfaces still preserve DTE/DCE-era control semantics?
- Which Internet mechanisms can be traced to a formal pre-RFC version tree?
- Which technologies were standardized after deployment?
- Which standards were implemented directly by Bell/IBM/DEC/Xerox products?
- Which protocols were replaced operationally but left application roles intact?
- Which historical ideas are commonly claimed as ancestors without direct evidence?
- Which obsolete physical mechanisms left logical conventions that still survive?
- Which technologies coexisted or encapsulated each other despite being described later as competitors?

The graph is successful when it makes those questions answerable without turning history into inevitability.