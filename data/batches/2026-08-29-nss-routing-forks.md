# 2026-08-29 Independent NSS and Open-Source Routing Fork Genealogy Batch

Theme: distinguish **design influence**, **parallel implementation**, **operational role migration** and **actual source/project forks**.

## Narrative outputs

- `docs/software/glibc-nss-vs-bsd-nsdispatch.md`
- `docs/software/net-tools-to-iproute2.md`
- `docs/routing/gated-zebra-quagga-frr.md`

## Structured source outputs

- `SRC-0213` — glibc NSS manual: Solaris design influence, explicitly no common code
- `SRC-0214` — Linux Foundation net-tools page
- `SRC-0215` — Linux Foundation iproute2 page
- `SRC-0216` — Linux kernel IP-aliasing compatibility documentation
- `SRC-0217` — GNU Zebra historical project page
- `SRC-0218` — Quagga routing-suite manual
- `SRC-0219` — Quagga governance/fork documentation
- `SRC-0220` — FRRouting current project/user documentation
- `SRC-0221` — FRRouting Zebra protocol version history

## Structured artifact outputs

- `ART-0208` — glibc NSS
- `ART-0209` — Linux net-tools
- `ART-0210` — GNU Zebra
- `ART-0211` — Quagga
- `ART-0212` — FRRouting
- `ART-0213` — Zebra/Quagga/FRR internal Zebra protocol lineage

## Structured lineage outputs

- `LIN-0153` — Solaris NSS method → glibc NSS design influence, explicitly no shared source code
- `LIN-0154` — BSD nsdispatch ↔ glibc NSS parallel implementations under a similar role
- `LIN-0155` — net-tools operator roles → iproute2 operator roles
- `LIN-0156` — GNU Zebra → Quagga direct fork/successor
- `LIN-0157` — Quagga → FRRouting direct fork/successor
- `LIN-0158` — GateD multiprotocol role → GNU Zebra role genealogy, no source ancestry asserted
- `LIN-0159` — GNU Zebra internal protocol v0 → Quagga v0-v3 carry-over/revision family
- `LIN-0160` — Quagga Zebra protocol v3 → FRR v4 revision/compatibility boundary

## Principal findings

1. **Configuration and terminology can be inherited without code.** glibc explicitly says its NSS was designed after Solaris 2 but contains no common Sun source and uses an incompatible internal interface.
2. BSD nsdispatch and glibc NSS should therefore be modeled as parallel name-service-dispatch families, not one source tree.
3. Linux net-tools→iproute2 is primarily an operational/tooling migration reflecting a richer kernel object/control model, not a code fork.
4. **GNU Zebra→Quagga→FRRouting is real project/source fork lineage**, documented by all three project families.
5. GateD and Zebra occupy related multiprotocol Unix routing roles but use different process architectures; direct source ancestry is not established.
6. The internal Zebra daemon protocol preserves project history independently of Git metadata; FRR documents versions spanning GNU Zebra, Quagga and FRR, including an early-FRR marker change preventing binary mixing.

## Next IDs

Subject to verification after commit:

- artifact: `ART-0214`
- source: `SRC-0222`
- lineage: `LIN-0161`

## Next excavation targets

- first glibc NSS release/commit and Solaris NSS contemporary documentation;
- glibc `getaddrinfo` implementation and NSS module call graph;
- exact net-tools → iproute2 distro migration timelines and first iproute release;
- early Linux netlink/rtnetlink source history;
- GNU Zebra first tarball/CVS snapshot and Zserv v0 header;
- exact Quagga fork commit and first public release;
- exact FRR fork commit and Zebra protocol v3→v4 source diff;
- GateD vs Zebra route-selection/RIB architecture comparison from source, without assuming ancestry.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
