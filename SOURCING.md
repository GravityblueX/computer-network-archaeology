# Sourcing, Evidence, and Preservation Policy

This project is an archive of **claims about historical computer networking** and, where legally and technically appropriate, an archive of historical artifacts themselves.

The repository should be expansive without becoming careless.

## 1. Source hierarchy

Preferred evidence, roughly from strongest to weakest:

1. **Contemporary primary technical material** — original specifications, RFCs, standards drafts, engineering reports, manuals, schematics, source code, network maps, procurement documents, meeting notes, operator handbooks, advertisements and contemporary papers.
2. **Institutional archives** — RFC Editor, NPL, DARPA/DTIC, Computer History Museum, Smithsonian, IEEE History Center, Inria, University archives, Merit Network, NSF, corporate archives.
3. **First-person oral histories and memoirs** — especially interviews recorded by reputable archives. Treat memory as evidence with normal historical caution.
4. **Peer-reviewed historical scholarship and academic monographs.**
5. **Well-sourced specialist histories.**
6. **General reference works and unsourced web pages** — useful for discovery, weak as terminal evidence.

Wikipedia is a discovery aid, not a preferred final citation when the underlying source can be recovered.

## 2. Every “first” needs a definition

Do not write “the first X” unless the category is defined.

Examples:

- first modem for what purpose?
- first commercial modem, first computer modem, or first modem-like data set?
- first packet network to operate, to demonstrate publicly, or to serve production users?
- first LAN under which definition of LAN?
- first router, or first device retrospectively analogous to a router?

If two reputable sources use incompatible definitions, preserve both claims and explain the difference.

## 3. Separate four layers of fact

Whenever possible, distinguish:

- **specification** — what a document said should happen;
- **implementation** — what hardware/software actually did;
- **deployment** — what was installed in a real network;
- **operation** — how people actually used and maintained it.

A protocol may have existed on paper before interoperable implementations. Hardware may have shipped before a formal standard. A network may have been announced before it was useful.

## 4. Dates

Record the kind of date, not just the year:

- proposed;
- designed;
- first prototype;
- first internal test;
- public demonstration;
- commercial announcement;
- shipment;
- operational deployment;
- standard approval;
- standard publication;
- retirement.

Do not silently substitute one for another.

## 5. Protocol texts and standards

The project wants to preserve the documentary record, but **availability is not the same as permission to redistribute**.

For each protocol/standard document, record:

- title;
- identifier and revision/edition;
- authoring body;
- publication date;
- status;
- canonical URL;
- known mirrors/archives;
- file format;
- checksum when a lawful local copy is held;
- rights/license/public-domain status;
- related predecessor/successor documents.

RFCs and openly distributed historical reports can be linked directly and mirrored only where their terms permit. ITU, ISO, ANSI, vendor manuals, books and scanned commercial documents should not be copied wholesale merely because a scan exists somewhere online.

## 6. Archival redundancy

For fragile sources, prefer recording multiple independent locations:

- canonical institutional URL;
- Internet Archive capture/item when available;
- museum or university mirror;
- bibliographic identifier;
- checksum for known copies.

The goal is that losing one website does not erase the trail.

## 7. Page-level citation

Long PDFs should be cited by page, section or figure when making a precise claim. Historical technical reports often contain multiple generations of a design; a citation to the whole report may conceal important chronology.

## 8. Source conflicts

Use a visible note such as:

> **Source conflict:** Source A dates the event to 1958; Source B dates the product announcement to 1959. These may refer to different milestones. Needs primary-document resolution.

Do not average conflicting dates.

## 9. Terminology drift

Record the contemporary term first and modern analogy second.

Prefer:

> Interface Message Processor (IMP), a packet-switching node often described retrospectively as a router predecessor.

Avoid:

> ARPANET used routers.

unless discussing the concept at a high level.

## 10. Hardware identification

A hardware record should try to capture:

- manufacturer;
- model and revision;
- production/installation dates;
- CPU/chipset where applicable;
- memory;
- interfaces/connectors;
- line rates;
- media;
- rack/cabinet form;
- power/environmental requirements when known;
- firmware/software;
- role in the network;
- photographs;
- manuals;
- surviving specimens;
- predecessor/successor.

Do not merge distinct revisions merely because they share a marketing name.

## 11. Software identification

A software record should capture:

- exact name and version;
- target operating system/hardware;
- language;
- protocol support;
- distribution method;
- source availability;
- known release dates;
- manuals;
- relation to standards;
- surviving source/binary copies.

## 12. Protocol identification

Do not treat a protocol family as one timeless thing. Track revisions.

Examples: NCP, TCP before the TCP/IP split, IPv4, early DNS RFC series, SMTP revisions, BGP-1/2/3/4, X.25 editions, Ethernet experimental/DIX/IEEE versions.

## 13. What not to do

- Do not invent a missing model number.
- Do not infer a connector from a photograph without marking the inference.
- Do not call a later standard by its modern name if the contemporary source used a different one.
- Do not erase failed designs from the story.
- Do not turn uncertain oral history into a precise date.
- Do not copy copyrighted PDFs into the repository by default.
- Do not use an AI-generated sentence as the sole evidence for another AI-generated sentence.

## 14. Useful canonical starting points

- RFC Editor: https://www.rfc-editor.org/
- Computer History Museum: https://www.computerhistory.org/
- NPL history: https://www.npl.co.uk/about-us/history/timeline
- Internet Society histories: https://www.internetsociety.org/internet/history-internet/
- Inria history/CYCLADES material: https://www.inria.fr/
- University of Hawaiʻi ALOHAnet history: https://www.eng.hawaii.edu/about/history/alohanet/
- Merit Network NSFNET history: https://www.merit.edu/research/projects/the-nsfnet-backbone-service/
- NSFNET historical project: https://nsf.net/
- History of Computer Communications: https://historyofcomputercommunications.info/

## 15. Repository rule

**Breadth is encouraged; false precision is not.**

A short record saying “known to exist; primary documentation not yet located” is better than a confident paragraph assembled from folklore.