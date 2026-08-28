# Controlled Vocabulary

This file defines the repository's preferred vocabulary for machine-readable records. It is intentionally narrower than ordinary prose. Historical documents keep their original terminology; the controlled vocabulary exists so that an archive containing thousands of heterogeneous objects can still be queried consistently.

## Core rule

**Never normalize away a historically meaningful distinction.**

Use a controlled category for indexing, then preserve the period term in `canonical_name`, `aliases`, notes and quoted metadata.

Example:

- historical document: **Internet Gateway**
- controlled kind: `gateway` or `router` depending on the record's purpose
- alias/note: “gateway is the contemporary Internet term; later terminology usually calls this an IP router”

If classification itself is historically disputed, use the closest neutral category and record the dispute.

---

## Artifact kinds

### Networks and services

- `network` — an identifiable communications network or experimental network, e.g. ARPANET, NPL Mark I, CYCLADES.
- `network-service` — a customer/user-facing service operating over network infrastructure, e.g. a named public packet data service.
- `carrier-service` — a telecommunications transmission/access product such as a leased-line service, DDS, T1 or a dial data service.
- `site` — a geographically or institutionally identifiable network location, node site, NOC, exchange or laboratory.

### Computing and terminal equipment

- `computer` — general computer when the networking role is not sufficiently specific.
- `host` — a computer acting as a communicating end system in the historical network being described.
- `terminal` — human-facing terminal, hardcopy or display.
- `front-end-processor` — processor offloading communication work from a host.

### Modems and transmission boundary equipment

- `modem-data-set` — modem/data set connecting digital equipment to an analog/digital carrier service. Preserve *data set* when that is the period term.
- `acoustic-coupler` — modem whose telephone interface is acoustically coupled through a handset.
- `csu-dsu` — customer-premises carrier termination for digital leased-line services; split CSU and DSU into separate records when evidence warrants.
- `multiplexer` — device combining multiple channels/ports onto a shared transmission facility.
- `radio-equipment` — radio transmitter/receiver/transceiver when it is a separately identifiable network artifact.
- `network-medium` — cable/radio/fiber/shared medium specification when the medium itself is the archaeological object.

### Packet and LAN forwarding equipment

- `packet-switch` — packet-switching node whose contemporary role is best described as switching packets within a network, e.g. IMP, CIGALE node.
- `gateway` — use when *gateway* is historically significant or the device translates/interconnects unlike environments. Add a modern-role note where necessary.
- `router` — network-layer forwarding device where router is contemporary or useful canonical terminology.
- `bridge` — data-link-layer forwarding device connecting LAN segments.
- `repeater` — physical-layer regeneration/repetition device.
- `hub` — multiport repeater/concentrator where the historically marketed form matters.
- `switch` — multiport forwarding device, normally LAN switching, when the term is appropriate to the period/product.
- `nic` — network interface card/adapter installed in a host or workstation.
- `transceiver` — distinct medium attachment/transceiver such as an Ethernet MAU.
- `interface` — electrical/logical boundary or interface unit whose role deserves its own record.
- `terminal-server` — device providing terminal/serial access to hosts or packet/IP networks.
- `pad` — Packet Assembler/Disassembler, especially X.3/X.28/X.29 environments.

### Diagnostics

- `diagnostic-tool` — breakout box, TDR, line tester, protocol analyzer, loopback plug, monitor or other operator diagnostic artifact.

### Software and protocols

- `software` — identifiable software package, daemon, utility or suite.
- `operating-system` — OS when its networking facilities are being catalogued as an object.
- `protocol` — one protocol/specification with a meaningful version boundary.
- `protocol-family` — lineage or suite containing multiple protocol versions/specifications.
- `standard` — formal standard/recommendation when the standard document/revision itself is the archaeological object.
- `source-code` — source tree, release or surviving code corpus when provenance/version matters independently of the software product.

### Historical and institutional objects

- `document` — a historically identifiable document when represented as an artifact rather than merely as evidence.
- `organization` — institution, company, lab, standards body or operations group.
- `person` — person record. Use carefully; this is a technical archive, not a general biography database.
- `event` — dated transition/test/demo/shutdown/standardization event that needs explicit linkage.
- `other` — only when none of the above is defensible. A future vocabulary revision should eliminate recurring `other` cases.

---

## Research states

Artifact records use:

- `seed` — name saved; little evidence mined.
- `priority` — high-value lead selected for excavation.
- `started` — at least one substantive source has been mined and facts recorded.
- `substantial` — multiple sources and several layers of the object reconstructed.
- `mature` — primary evidence, revision history, physical/software/protocol context and open questions are well developed. **Mature does not mean complete.**
- `blocked` — progress currently depends on unavailable/restricted/lost evidence.

Source records use:

- `discovered` — citation/URL known but contents not yet inspected.
- `acquired` — lawful local or stable archival copy obtained.
- `skimmed` — inspected for relevance.
- `mined` — useful claims/locators extracted.
- `verified` — identity, edition/date and important claims checked against the source itself.
- `needs-rescan` — scan/OCR is too poor for reliable extraction.
- `needs-rights-check` — preservation/redistribution status unresolved.
- `missing` — known source not currently located.
- `conflicted` — source metadata or content conflicts materially with other evidence.

---

## Certainty states

Use certainty on **claims**, not merely documents.

- `confirmed` — directly supported by appropriate evidence with no material conflict currently known.
- `probable` — strong evidence, but a primary record/revision-level confirmation is still missing.
- `disputed` — credible sources conflict or terminology/date boundaries differ materially.
- `unknown` — the repository does not yet have enough evidence.
- `mixed` — record contains claims at multiple certainty levels; individual claims should still be tagged where possible.

Never use “confirmed” merely because many websites repeat the same sentence.

---

## Evidence grades

Source records classify evidentiary position separately from quality:

- `primary-contemporary` — specification, manual, source code, log, memo, report, map, tariff, photograph, advertisement or other record created during the relevant period.
- `primary-retrospective` — later oral history/interview/memoir by a participant.
- `institutional-secondary` — museum/lab/company/university historical synthesis.
- `scholarly-secondary` — peer-reviewed scholarship or serious research monograph.
- `participant-secondary` — later synthesis written by participants but not itself a contemporary record.
- `tertiary-discovery` — encyclopedia, generic timeline, collector page or other lead-generation source.
- `unknown` — evidence position not yet classified.

A contemporary vendor advertisement is primary evidence for what the vendor **claimed**, not automatically for what the product actually achieved in deployed service.

---

## Historical chronology vocabulary

Do not store one ambiguous `date` when several milestones exist.

Preferred milestones:

- `conceived`
- `announced`
- `first_tested`
- `first_operational`
- `standardized`
- `withdrawn`
- `last_known_use`

Date precision:

- `day`
- `month`
- `year`
- `decade`
- `range`
- `circa`
- `unknown`

Example: a network may have been designed in 1967, partially running in 1969 and formally operational in 1970. Those are not contradictory facts unless two sources claim the same milestone.

---

## Stack-position vocabulary

Modern OSI-like labels are useful for search but must not be projected uncritically backward.

- `physical`
- `link`
- `network`
- `transport`
- `session`
- `presentation`
- `application`
- `operations`
- `management`
- `cross-layer`
- `pre-layered`

For early systems, `pre-layered` may be more honest than forcing a 1960s interface into a later seven-layer scheme.

---

## Relationship verbs

Prefer a small reusable set in graph-like records:

- `predecessor-of`
- `successor-of`
- `revision-of`
- `variant-of`
- `implemented-by`
- `implements`
- `runs-on`
- `hosts`
- `attached-to`
- `interfaces-with`
- `transmitted-over`
- `encapsulated-in`
- `carried`
- `gatewayed-to`
- `interconnected-with`
- `operated-by`
- `manufactured-by`
- `funded-by`
- `standardized-by`
- `specified-by`
- `documented-by`
- `replaced-by`
- `coexisted-with`
- `influenced`
- `possibly-influenced`
- `survives-at`

Use `influenced` sparingly. Prefer a concrete documentary relationship such as “paper X cites report Y” when that is what the evidence actually proves.

---

## Rights vocabulary

- `public-domain`
- `open-license`
- `rfc-distribution-terms`
- `copyrighted-link-only`
- `copyrighted-permission-known`
- `government-work-check-jurisdiction`
- `mixed`
- `unknown`

**Finding a PDF online does not grant redistribution permission.**

---

## Survival vocabulary

- `unknown`
- `none-known`
- `documented-only`
- `partial`
- `surviving-specimen`
- `operational-specimen`
- `emulated`
- `source-survives`

A photograph of an unidentified unit is not sufficient to claim that a historically deployed specimen survives. Provenance matters.

---

## Naming rules

1. Use the period-correct official name as `canonical_name` when known.
2. Put later names, abbreviations and spelling variants in `aliases`.
3. Preserve model suffixes: `103A`, `103F`, `Mark I`, `Mark II`, protocol edition year, hardware revision.
4. Split objects when revisions change behavior materially.
5. Do not use marketing-family names as substitutes for exact models when exact models are known.
6. Never silently expand ambiguous acronyms. `NCP`, for example, has unrelated meanings in ARPANET, IBM and Novell contexts.
7. Preserve contemporary capitalization where it aids identification, but search keys may be normalized separately later.

---

## What this vocabulary is for

The archive should eventually support queries such as:

- show every packet switch built on a Honeywell Series 16 computer;
- show terminal → PAD → X.25 paths documented between 1976 and 1985;
- list every artifact with V.24/RS-232 interfaces;
- show protocols whose first deployed implementation predates their formal standard;
- show objects with surviving source code but no known surviving hardware;
- show all disputed “first operational” dates;
- show devices whose historical name was `gateway` but whose role maps to an IP router;
- show every network whose physical service was leased telephone circuits;
- show every claim supported only by retrospective sources.

That is why controlled vocabulary is archival infrastructure, not cosmetic taxonomy.