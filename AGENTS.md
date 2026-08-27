# AGENTS.md

Instructions for AI agents and human contributors working in this repository.

## Mission

This repository is a **source-driven archaeology of computer networking**. Do not reduce it to a conventional Internet-history summary.

The default bias is toward **preserving detail**.

If a historical object, document, protocol, interface, product, network, software package, standard, company, line service, operational practice or terminology can be documented and is relevant to computer communication, create a place for it.

## Core rules

1. **Do not stop at famous milestones.** ARPANET, TCP/IP and Ethernet are trunks, not the whole forest.
2. **Preserve losers and dead ends.** X.25, SNA, DECnet, XNS, PUP, Chaosnet, ARCNET, Token Ring, FidoNet, Tymnet, Telenet and obscure vendor systems are first-class historical subjects.
3. **Trace the whole stack.** For a historical network, identify physical media, line service, modem/data set, packet switch, host interface, host software, protocols, addressing, routing, naming, management and user-facing services.
4. **Separate specification from implementation and deployment.**
5. **Never hide source disagreements.** Mark them.
6. **Prefer primary sources and institutional archives.**
7. **Do not invent facts to make a narrative smooth.** `unknown` and `needs verification` are valid archival states.
8. **Do not bulk-copy copyrighted standards/manuals.** Preserve metadata and lawful access paths.
9. **Use exact contemporary names.** Add modern analogies only as explanation.
10. **Cross-link aggressively.** Networking history is a graph, not a line.

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
- known surviving examples.

Not every record will have every field. Missing fields become research leads.

## Writing style

Write clearly enough for a technically curious reader who did not live through the period. Avoid presentist mockery of old designs: many apparently strange systems were rational responses to contemporary line costs, hardware prices, memory limits, regulatory structures, reliability assumptions and installed infrastructure.

Whenever possible, explain **why the design made sense then**.

## Citation discipline

Each nontrivial section should end with or contain direct source links. Prefer stable institutional URLs, DOI/bibliographic metadata, report numbers, RFC numbers and page references.

Do not cite this repository to itself as evidence.

## New files

Use the templates in `templates/`.

When discovering an artifact that does not yet deserve a full article, add it to a catalog or `data/artifact-ledger.csv` rather than losing the lead.

When discovering a source that has not yet been mined, add it to `data/source-ledger.csv`.

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

If not, the excavation is not finished.