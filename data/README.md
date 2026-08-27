# Research Ledgers

The CSV files in this directory are **loss-prevention queues**. They are intentionally allowed to contain incomplete records.

The principle is:

> Discover first, record immediately, verify and expand later.

A forgotten product name found in a 1974 manual should not disappear merely because nobody can write a 2,000-word article about it today.

## `artifact-ledger.csv`

Tracks things that existed or were defined:

- physical devices;
- systems;
- interfaces;
- network media;
- protocol families;
- software;
- historically significant implementation objects.

### `artifact_id`

Stable project identifier, currently `ART-NNNN`.

Do not recycle IDs when a row is removed or split.

### `artifact_type`

Free-text now, but expected to converge toward a controlled vocabulary such as:

- system
- host
- terminal
- modem-data-set
- interface
- network-medium
- packet-switch
- router
- bridge
- hub
- switch
- nic
- transceiver
- controller
- multiplexer
- pad
- terminal-server
- access-server
- wan-device
- diagnostic
- protocol-family
- software

### `name`

Use contemporary product/protocol name where known.

### `manufacturer_or_body`

Manufacturer, standards body, project or implementing institution.

### `era_or_first_date`

This field is intentionally not a guaranteed “release date”. Until exact event type is verified it may contain an era/year range.

Precise articles should distinguish:
- proposal;
- prototype;
- announcement;
- shipment;
- deployment;
- standard approval;
- retirement.

### `network_or_family`

Where the artifact belonged or which larger family it is part of.

### `layer_or_role`

Functional historical role. Do not force every object into modern OSI terminology.

### `research_state`

Suggested values:

- `seed` — identified only;
- `priority` — known high-value excavation target;
- `started` — some sourced coverage exists;
- `substantially-documented` — detailed article/record exists;
- `needs-primary-verification`;
- `blocked`.

### `primary_source_target`

The most useful next evidence to seek.

### `notes`

Short warnings/disambiguation, not a substitute for an article.

## `source-ledger.csv`

Tracks evidence rather than artifacts.

### `source_id`

Stable `SRC-NNNN` identifier.

### `source_type`

Examples:
- rfc;
- technical-report;
- manual;
- standard;
- source-code-corpus;
- oral-history;
- advertisement;
- institutional-history;
- academic-book;
- map;
- catalog;
- operator-document.

### `title`

Exact bibliographic title where possible.

### `author_or_body`

Author, company, standards body or archive.

### `date_or_year`

Preserve uncertainty. Do not invent a day/month.

### `identifier`

RFC number, report number, Bell System Practice section, IBM publication number, IEEE/ISO/ITU identifier, catalog number, ISBN/DOI, archive identifier, etc.

### `canonical_url`

Preferred authoritative location.

### `archive_or_mirror`

Independent preservation path when available.

### `rights_status`

Examples:
- public domain;
- RFC distribution terms;
- copyrighted;
- license name;
- verify;
- unknown.

Do not infer redistribution permission merely from the existence of a PDF.

### `topics`

Semicolon-separated discovery tags.

### `research_state`

Suggested values:
- seed;
- priority;
- discovered;
- acquired;
- started;
- partially-mined;
- fully-mined;
- inaccessible;
- rights-blocked.

### `notes`

Include scan/OCR quality, source conflicts and next actions.

## Future machine-readable expansion

Likely future files:

- `network-events.csv` — dated proposal/test/deployment/retirement events;
- `hardware-variants.csv` — model/revision genealogy;
- `protocol-documents.csv` — protocol version ↔ defining document relationships;
- `deployments.csv` — exact site/date/device evidence;
- `links.csv` — physical circuits/media between historical nodes;
- `organizations.csv` — company/lab/standards-body genealogy;
- `people.csv` — contributors linked to projects/documents;
- `archive-holdings.csv` — museums/archives/surviving specimens;
- `terminology.csv` — contemporary term ↔ later terminology mapping.

## Why CSV first

The initial format is deliberately boring:

- Git diffs are readable;
- no database server is required;
- humans and agents can append records;
- scripts can validate it;
- it can later be imported into SQLite/PostgreSQL or converted to JSON/YAML.

If the corpus grows large enough, a relational/graph representation will become useful. The CSVs are an interchange and capture layer, not a claim that networking history is naturally a flat table.

## Rule

**Never delete an inconvenient contradiction merely to make the data cleaner.**

Historical uncertainty should be modeled, not erased.