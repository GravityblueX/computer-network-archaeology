# Documentation Index

This is the human-readable entrance to the excavation. The repository is designed to support two reading modes:

1. **chronological reading** — follow how computer communication changed over decades;
2. **artifact-first research** — start from one device/protocol/network/document and follow cross-links outward.

## Chronological spine

Start here if you want the broad transformation:

1. [`1950s-data-communications.md`](1950s-data-communications.md)  
   SAGE, radar data, modems/data sets, leased telephone infrastructure, remote terminals, SABRE, and why the decade before packet switching matters.

2. [`1960s-time-sharing-packet-switching.md`](1960s-time-sharing-packet-switching.md)  
   Time-sharing, Baran, Davies/NPL, ARPA, BBN, IMPs, the first four ARPANET hosts, and the still-unfinished host protocol problem.

3. [`1970s-many-networks.md`](1970s-many-networks.md)  
   ARPANET/NCP, ALOHAnet, CYCLADES, Ethernet/PUP, X.25, Tymnet/Telenet, packet radio, satellite, vendor architectures and the emergence of internetworking.

4. [`1980s-protocol-wars.md`](1980s-protocol-wars.md)  
   TCP/IP transition, BSD sockets, DNS/routing, BITNET, CSNET, JANET, NSFNET, Ethernet/Token Ring, NetWare, AppleTalk, OSI, X.25, UUCP/Usenet/BBS/FidoNet and the multiprotocol machine room.

5. [`1990s-commercial-internet.md`](1990s-commercial-internet.md)  
   NSFNET T1/T3, BGP/CIDR, commercial providers, dial-up IP, modem banks, PPP, switching Ethernet, Frame Relay, ATM, ISDN, Web-driven growth and the 1995 backbone transition.

The shorter date-oriented reference is [`../timeline/master-timeline.md`](../timeline/master-timeline.md).

## Deep excavations

These files demonstrate the intended final granularity.

### ARPANET

- [`arpanet/1969-host-imp-stack.md`](arpanet/1969-host-imp-stack.md)  
  Reconstructs the early host/IMP boundary from RFC 1 and RFC 7: messages vs packets, logical links, RFNM, error checking, UCLA Sigma 7 host software organization, buffer design and unresolved hardware/carrier questions.

### Modems

- [`modems/bell-101-103-source-conflict.md`](modems/bell-101-103-source-conflict.md)  
  A worked example of source criticism. Modern histories and surviving Bell-document metadata do not yet produce a clean Bell 101/103 model/revision chronology, so the conflict is preserved rather than silently flattened.

## Catalog entrances

The narrative is intentionally not the master database. Use these discovery catalogs when researching one object:

- [`../catalogs/networks.md`](../catalogs/networks.md) — named networks, services and network ecosystems;
- [`../catalogs/hardware.md`](../catalogs/hardware.md) — terminals, modems, switches, interfaces, NICs, routers, carrier gear and diagnostics;
- [`../catalogs/software.md`](../catalogs/software.md) — switching-node software, host stacks, network operating systems, utilities and user-facing programs;
- [`../catalogs/protocols.md`](../catalogs/protocols.md) — protocol/standard families and revisions;
- [`../catalogs/document-corpora.md`](../catalogs/document-corpora.md) — where the original protocol texts and technical record survive.

## Evidence entrances

- [`../sources/primary-sources.md`](../sources/primary-sources.md) — RFC/IEN/BBN/NPL/RAND/CYCLADES/ALOHAnet/PARC/vendor/manual/source-code corpora;
- [`../sources/secondary-sources.md`](../sources/secondary-sources.md) — scholarship and participant histories;
- [`../SOURCING.md`](../SOURCING.md) — evidence hierarchy, dating, copyright/preservation and conflict rules.

## Machine-readable research queues

- [`../data/artifact-ledger.csv`](../data/artifact-ledger.csv) — concrete devices, protocols and software awaiting deeper records;
- [`../data/source-ledger.csv`](../data/source-ledger.csv) — sources discovered/acquired/mined or still sought.

A name can enter a ledger before it gets an article. This prevents obscure discoveries from disappearing simply because there was not enough time to investigate them immediately.

## Record templates

- [`../templates/hardware-record.md`](../templates/hardware-record.md)
- [`../templates/protocol-record.md`](../templates/protocol-record.md)
- [`../templates/network-record.md`](../templates/network-record.md)
- [`../templates/source-record.md`](../templates/source-record.md)

The templates intentionally ask for details that popular histories omit: connector pins, line service, clocking, buffer sizes, software revisions, operator diagnostics, pricing, source conflicts, surviving specimens and rights status.

## Recommended excavation order

The project should now grow both **horizontally** and **vertically**.

### Horizontal: prevent loss

Keep expanding discovery coverage:

- network names;
- device/product families;
- software packages;
- standards/protocols;
- companies;
- national networks;
- archives and document series.

A thin catalog row is enough to save a lead.

### Vertical: prove what a system really was

Choose individual systems and reconstruct them end-to-end:

```text
user / application
      ↓
host software
      ↓
interface hardware
      ↓
switch/router/PAD/modem
      ↓
actual carrier or local medium
      ↓
remote equipment
      ↓
remote software / user
```

The next high-value vertical digs include:

1. September–October 1969 UCLA ARPANET node bill of materials;
2. BBN Report 763 and exact Host–IMP electrical interface;
3. Bell 101A/B/C and 103A/F revision tree from Bell primary documents;
4. complete NPL packet-switch node hardware/software reconstruction;
5. CYCLADES CIGALE Mitra 15 packet switch;
6. 1973 Alto experimental Ethernet hardware + PUP stack;
7. one complete 1970s X.25 terminal → PAD → public data network → host path;
8. 1986 NSFNET PDP-11 Fuzzball node;
9. 1988 NSFNET IBM RT Nodal Switching Subsystem;
10. one 1994 dial-up ISP POP from analog subscriber loop through modem bank/access server to upstream BGP router.

## The completion criterion

This archive should never declare a subject “done” merely because a readable narrative exists.

A mature excavation ideally connects:

**idea → specification → hardware → software → deployment → operation → failure → replacement → surviving artifact → primary source.**

That graph, not article count, is the real measure of completeness.