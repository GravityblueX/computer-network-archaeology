# Computer Network Archaeology

> A source-driven archaeology of computer networking, from pre-Internet data communications to the commercial Internet era.

This repository is not intended to be another short history of “ARPANET → TCP/IP → Web”. Its purpose is deliberately broader and more obsessive:

**preserve, identify, date, connect, and explain the hardware, software, protocols, standards, networks, transmission media, organizations, documents, terminology, and dead ends that made computer networking possible.**

The working rule is simple:

> If it existed, mattered to computer communication, and can still be documented, it belongs somewhere in this archive.

That includes technologies that won, technologies that lost, products that disappeared, standards that were superseded, obscure interface boxes, forgotten host software, packet switches, terminal concentrators, modems, leased-line equipment, protocol notes, advertisements, manuals, network maps, source listings, operator procedures, and the institutional machinery behind them.

## Scope

The main chronological window begins in the **1950s**, with radar/data communication, SAGE, modems, remote terminals, real-time reservation systems, teletypes, telephone infrastructure and time-sharing precursors. It then follows the multiplication of computer networks through the 1960s–1990s and continues far enough into the modern Internet to explain how the old world became the present one.

This is a history of **computer networks**, not only the Internet. ARPANET is central, but so are NPL, CYCLADES, ALOHAnet, Tymnet, Telenet, X.25 networks, packet radio, SATNET, Ethernet, Token Ring, ARCNET, DECnet, SNA, XNS, UUCP, Usenet, BITNET, CSNET, JANET, NSFNET, FidoNet, commercial online services, regional research networks and many others.

## What belongs here

- transmission infrastructure: telegraph, telephone, leased circuits, T-carrier, satellite and radio links;
- physical and link hardware: modems, acoustic couplers, multiplexers, transceivers, repeaters, bridges, hubs, switches, NICs, CSU/DSUs, terminal servers, PADs;
- packet-switching hardware: IMPs, TIPs, packet switches, gateways and early routers;
- terminals and host interfaces: teletypes, glass terminals, serial interfaces, Host–IMP interfaces, front ends;
- network operating and host software;
- protocol specifications and protocol families;
- routing, naming, directory and network-management systems;
- standards bodies and standards wars;
- public, commercial, academic, military and experimental networks;
- original reports, RFCs, manuals, advertisements, maps, oral histories and photographs;
- terminology whose meaning changed over time;
- failed, abandoned and superseded designs.

## What does *not* primarily belong here

Executable reimplementations, emulators and protocol toys should normally live in the companion repository **[tmzncty/protocol-zoo](https://github.com/tmzncty/protocol-zoo)**. This repository documents what existed and how it worked; `protocol-zoo` can reconstruct selected mechanisms in runnable form.

## Repository map

- [`docs/`](docs/) — narrative histories and technical archaeology by period/topic
- [`catalogs/`](catalogs/) — long-form inventories of networks, hardware, software and protocols
- [`timeline/`](timeline/) — chronological spine
- [`sources/`](sources/) — primary-source and secondary-source guides
- [`data/`](data/) — machine-readable ledgers for artifacts and sources
- [`templates/`](templates/) — record templates for future additions
- [`SOURCING.md`](SOURCING.md) — evidence, citation, preservation and copyright rules
- [`ROADMAP.md`](ROADMAP.md) — coverage backlog; intentionally very large
- [`AUTHORSHIP.md`](AUTHORSHIP.md) — authorship and AI disclosure
- [`AGENTS.md`](AGENTS.md) — instructions for future AI/human contributors

## Method: reconstruct the stack that actually existed

A recurring goal is to rebuild historical systems conceptually, layer by layer. Instead of saying only “ARPANET used packet switching”, we want to be able to answer questions such as:

```text
host computer
  ↓ host software
host interface
  ↓
IMP / packet switch
  ↓ modem / data set
leased telephone circuit
  ↓ modem / data set
IMP / packet switch
  ↓
remote host interface
  ↓ remote host software
remote host
```

For each layer we should ask:

1. What exact device/software/protocol was used?
2. Who made it?
3. When did it enter service?
4. What electrical or logical interface did it expose?
5. What bit rate and framing did it use?
6. What assumptions did it inherit from telephone/telegraph/computer practice?
7. Which document defined it?
8. What failed in practice?
9. What replaced it?
10. What conceptual descendants survive today?

## A warning about “firsts”

Networking history is full of incompatible claims about the “first modem”, “first packet network”, “first router”, “first LAN”, “birth of the Internet”, and similar labels. This repository treats **firstness as a claim that needs a definition and a citation**, not as a trophy.

When sources disagree, preserve the disagreement. Do not silently collapse it.

## Starting evidence base

The initial archive is anchored in primary and institutional sources including:

- the [RFC Editor index](https://www.rfc-editor.org/rfc-index/), beginning with RFC 1, *Host Software* (1969);
- BBN’s *A History of the ARPANET: The First Decade* (Report 4799, 1981);
- the 1978 *Completion Report: ARPA Network Development*;
- the National Physical Laboratory’s history of Donald Davies and the NPL Data Communications Network;
- Computer History Museum networking/computing timelines;
- Internet Society histories written by participants in early Internet work;
- institutional histories from Inria/CYCLADES, University of Hawaiʻi/ALOHAnet, Merit/NSFNET and others;
- James Pelkey’s *History of Computer Communications*, based on more than 80 interviews.

See [`sources/primary-sources.md`](sources/primary-sources.md) and [`sources/secondary-sources.md`](sources/secondary-sources.md).

## Preservation policy

This repository distinguishes **preserving knowledge about a document** from **redistributing the document itself**. Public-domain and appropriately licensed material may be mirrored where useful. Copyrighted standards, books, vendor manuals and scans should not be copied merely because a PDF can be found online. Record stable metadata, bibliographic details, checksums where legally obtained, and archival locations instead. See [`SOURCING.md`](SOURCING.md).

## Status

This project is intentionally incomplete. “Complete” is probably impossible; the useful target is an expanding, auditable map of surviving evidence.

The first pass establishes the corpus and the excavation method. Subsequent passes should become increasingly granular: individual hardware revisions, protocol versions, network maps, line speeds, interfaces, software releases, standards editions, operating practices and archival copies.

---

## Authorship

**Research, initial architecture, and primary drafting: GPT-5.6 Sol (OpenAI), August 2026.**

This repository is deliberately explicit that a large language model is performing much of the research organization and drafting. AI authorship is not a substitute for evidence: factual claims should be traceable to sources, uncertain claims should be marked, and mistakes should be corrected publicly.

Repository steward: [tmzncty](https://github.com/tmzncty).

See [`AUTHORSHIP.md`](AUTHORSHIP.md) for the full disclosure.