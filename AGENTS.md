# AGENTS.md

Instructions for AI agents and human contributors working in this repository.

## Mission

This repository is a **source-driven archaeology of computer networking**. Do not reduce it to a conventional Internet-history summary.

The default bias is toward **preserving detail**.

If a historical object, document, protocol, interface, product, network, software package, standard, company, line service, operational practice, terminology, or documented technical lineage can be preserved, create a place for it.

## Core rules

1. **Do not stop at famous milestones.** ARPANET, TCP/IP and Ethernet are trunks, not the whole forest.
2. **Preserve losers and dead ends.** X.25, SNA, DECnet, XNS, PUP, Chaosnet, ARCNET, Token Ring, FidoNet, Tymnet, Telenet and obscure vendor systems are first-class historical subjects.
3. **Trace the whole stack.** For a historical network, identify physical media, line service, modem/data set, packet switch, host interface, host software, protocols, addressing, routing, naming, management and user-facing services.
4. **Trace lineage as well as chronology.** Ask what an object inherited, rejected, replaced and left behind in later systems.
5. **Separate specification from implementation and deployment.**
6. **Never hide source disagreements.** Mark them.
7. **Prefer primary sources and institutional archives.**
8. **Do not invent facts to make a narrative smooth.** `unknown` and `needs verification` are valid archival states.
9. **Do not bulk-copy copyrighted standards/manuals.** Preserve metadata and lawful access paths.
10. **Use exact contemporary names.** Add modern analogies only as explanation.
11. **Cross-link aggressively.** Networking history is a graph, not a line.
12. **Do not infer influence from similarity or chronological priority.**

## Four dimensions of a mature excavation

A strong contribution should ideally improve one or more of these views:

### Chronology

When was it conceived, tested, deployed, standardized, revised, replaced and retired?

### Stack

What was physically/logically connected to what?

### Artifact

What exact model, revision, software build, document, site, board, connector or surviving specimen existed?

### Lineage

What formal revision, documented influence, migration, role continuity or interface convention connects it to earlier/later systems?

The lineage model is documented in `lineage/README.md`; machine-readable edges use `schema/lineage-edge.schema.json` and the discovery queue `data/lineage-ledger.csv`.

## Lineage discipline

A lineage edge is a historical claim and needs evidence.

### Strong edges

Prefer relationships such as:

- `revision-of`
- `successor-of`
- `replaced-by`
- `standardizes`
- `derived-from`
- `splits-into`
- `survives-as`
- `role-descends-into`
- `interface-convention-inherited-by`

when the documentation supports them.

### Influence edges

Use `influenced` only when there is direct documentary support such as:

- a design paper citing an earlier system;
- committee minutes/drafts;
- participant testimony;
- source-code derivation;
- a vendor manual explicitly adopting a standard;
- migration documentation.

If the relationship is plausible but not proven, use `possibly-influenced` and say exactly what evidence is missing.

**A predates B** does not imply **A caused B**.

**A resembles B** does not imply **B descends from A**.

### Coexistence is first-class

Do not force every history into replacement.

Systems may:

- coexist;
- interwork;
- gateway to one another;
- encapsulate one another;
- use the same carrier infrastructure;
- compete institutionally while cooperating technically.

The IP-over-X.25 history is an obvious example.

### Property-level lineage

Whenever possible, state what actually survives:

- connector convention;
- electrical signaling;
- frame field;
- addressing rule;
- queueing behavior;
- role in a network;
- software API;
- operator procedure;
- service expectation;
- terminology.

Avoid vague edges such as “influenced modern networking.”

## Desired granularity

A mature entry for a device or protocol may include tiny details that ordinary histories omit:

- connector type;
- framing;
- clock source;
- bit rate;
- line conditioning;
- duplex mode;
- checksum width;
- packet/message size;
- cabinet/revision;
- interface voltage;
- host OS;
- memory limitation;
- operator commands;
- error indicators;
- diagnostic loopback behavior;
- tariff/service assumptions;
- procurement constraints;
- upgrade path;
- known surviving examples;
- formal predecessor/successor;
- inherited interface convention;
- mechanisms that disappeared;
- mechanisms that survived in descendants.

Not every record will have every field. Missing fields become research leads.

## Writing style

Write clearly enough for a technically curious reader who did not live through the period. Avoid presentist mockery of old designs: many apparently strange systems were rational responses to contemporary line costs, hardware prices, memory limits, regulatory structures, reliability assumptions and installed infrastructure.

Whenever possible, explain **why the design made sense then**.

Avoid teleological writing such as:

> X was an inevitable step toward the modern Internet.

Prefer:

> X solved these contemporary constraints; some of its mechanisms later survived in Y, while others disappeared.

## Citation discipline

Each nontrivial section should end with or contain direct source links. Prefer stable institutional URLs, DOI/bibliographic metadata, report numbers, RFC numbers and page references.

Do not cite this repository to itself as evidence.

For a lineage claim, record the source/locator that supports **the relationship itself**, not merely separate sources proving that both endpoints existed.

## New files

Use the templates in `templates/`.

When discovering an artifact that does not yet deserve a full article, add it to a catalog or `data/artifact-ledger.csv` rather than losing the lead.

When discovering a source that has not yet been mined, add it to `data/source-ledger.csv`.

When discovering a plausible technical descent or revision relation, add it to `data/lineage-ledger.csv`. If the relationship is important and well evidenced, promote it to `records/lineages/LIN-*.json`.

## Companion implementation repository

Runnable reimplementations and protocol experiments should normally be placed in:

https://github.com/tmzncty/protocol-zoo

This repository should document enough detail to make such reconstruction possible, but should remain primarily historical/documentary.

## AI disclosure

The project was initially structured and drafted by **GPT-5.6 Sol (OpenAI)**. Do not remove the authorship disclosure in `AUTHORSHIP.md` unless the repository steward explicitly changes the project policy.

## Before finishing a contribution

Ask:

- Did I cite the original evidence?
- Did I distinguish proposal, prototype, deployment and standardization dates?
- Did I accidentally project modern terminology backward?
- Did I preserve competing systems, or narrate only the winner?
- Did I add newly discovered source leads to the ledgers?
- Did I record uncertainty instead of guessing?
- Can another researcher follow my citations and reproduce the claim?
- Did I confuse chronology with causality?
- If I claimed influence or descent, what exact source supports that edge?
- Did I state what survived and what died instead of writing a triumphalist straight line?

If not, the excavation is not finished.