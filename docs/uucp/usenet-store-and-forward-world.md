# UUCP + Usenet: a network that could go offline between hops

Early network history is distorted if every system is imagined as a continuously connected packet network. UUCP and early Usenet demonstrate a different world: computers dialed one another, exchanged queued files and messages, hung up, and let the next scheduled call move data another hop.

The result was a large social network whose physical substrate could be ordinary telephone service and whose routing could be written into an address as a sequence of machine names.

## UUCP before Usenet

UUCP — Unix-to-Unix Copy — grew inside Bell Labs to solve software-distribution and communication problems among an expanding population of UNIX systems.

D. A. Nowitz and M. E. Lesk described a network whose practical attractions were deliberately modest:

- a site could begin with a dial-up port;
- automatic calling hardware made unattended exchange easier;
- no operating-system redesign was required;
- ordinary telephone lines were sufficient;
- hardwired/private circuits could be substituted where useful;
- file-copy semantics made the system understandable to UNIX users.

The Seventh Edition UNIX documentation included both **A Dial-Up Network of UNIX Systems** and a **UUCP Implementation Description**.

## A physical UUCP link

One representative path was:

```text
UNIX host A
   ↓ tty / serial port
modem or automatic calling unit
   ↓
public switched telephone network
   ↓
modem
   ↓ tty / serial port
UNIX host B
```

The network existed because software repeatedly turned these temporary point-to-point telephone calls into a larger store-and-forward fabric.

## What UUCP actually queued

UUCP was not one monolithic protocol. The suite accumulated programs and spool conventions for tasks such as:

- copying files to another system;
- requesting files where permissions allowed;
- executing work remotely after transfer;
- carrying electronic mail;
- carrying Netnews/Usenet batches;
- status, cleanup and administration.

A future implementation excavation should distinguish versions of `uucp`, `uux`, `uuxqt`, `uucico`, `uusched`, `uustat` and related tools by UNIX release.

## The spool is part of the network

In a packet network, engineers tend to visualize buffers inside switches. In UUCP, the durable queue on disk was central.

A message could wait for:

- the next scheduled call;
- a cheaper nighttime tariff period;
- a modem to become free;
- a failed neighbor to return;
- an administrator to repair configuration.

So delay was not exceptional congestion. Delay was a normal architectural state.

## Routing by bang path

Before universal domain-style addressing, an address might explicitly encode a route:

```text
research!duke!site!user
```

The `!` separators gave rise to the term **bang path**.

The address exposed something modern networks usually hide: the path through intermediate hosts.

As the UUCP network grew, this became difficult to manage. Tools such as **pathalias** later built route tables from connectivity maps so users or mail software did not have to hand-maintain long paths.

## Topology was partly economic

Telephone charges shaped the graph.

A site willing to pay long-distance costs could become an important transit hub. Institutions with favorable budgets, corporate support or existing calls could carry traffic for others. Scheduled calling relationships therefore encoded not only technical reachability but economics and organizational generosity.

This is one reason a historical UUCP map cannot be understood like a modern autonomous-system map. A “link” might mean one side calls the other once per night.

## Usenet emerges on top of UUCP

In late 1979, Tom Truscott and Jim Ellis at Duke and Steve Bellovin at the University of North Carolina were experimenting with a UUCP connection. Bellovin had written a rudimentary local news system; Truscott and Ellis proposed distributing news between sites through UUCP.

By early 1980 the initial group included UNC, Duke and a Duke medical site. The idea was publicized through the UNIX users' community, and software distribution through USENIX helped it spread.

The key architectural fact is:

> **Usenet was an application/distribution system layered on top of a network that already moved queued files.**

## A News

The earliest software lineage is messy and should be preserved as such.

Steve Bellovin's first code was a shell-based news system. It was rewritten/revised in C by Bellovin and others; Steve Daniel and Tom Truscott contributed to what became known as **A News**. A News was distributed through early USENIX channels and worked while the volume of articles and sites remained small.

Do not flatten this into a single-author claim. Surviving participant histories assign overlapping roles to Bellovin, Daniel/Daniels, Truscott and Ellis.

## B News

By 1981, the scale problem was obvious. **Mark Horton** and **Matt Glickman** rewrote the software into **B News**.

B News became the dominant Usenet transport/management software for much of the 1980s and evolved through many revisions.

A full excavation should recover:

- article spool layout;
- history database format;
- `active` file semantics;
- batching and compression;
- neighbor/feed configuration;
- expiration;
- moderation mechanics;
- control messages;
- how UUCP transport was invoked.

## C News

Later, **Geoff Collyer** and **Henry Spencer** developed **C News**, with an emphasis on efficiency, portability and operation at much larger traffic volumes.

Surviving 1989–1990 source distributions and patches expose the operational anatomy directly: incoming and outgoing spool areas, history databases, batching logs, feed tools, locks, expiration and maintenance utilities.

This source code is historical evidence about what operating a worldwide discussion system actually required.

## One article's journey

A simplified 1980s article path might be:

```text
user posts article on site A
        ↓
local news software stores article
        ↓
outgoing batch queued
        ↓
UUCP scheduler/call
        ↓
modem → telephone network → modem
        ↓
site B receives batch into spool
        ↓
news software checks history / installs article
        ↓
article queued for B's other neighbors
        ↓
hours later, another call
        ↓
site C
```

There was no requirement that the global graph be simultaneously online.

## Duplication was expected

Because Usenet propagated through multiple neighbor relationships, the same article could arrive by more than one path. News software therefore needed article identifiers and history tracking to suppress duplicates.

This is a different kind of distributed-systems problem from reliable end-to-end packet delivery. The object being deduplicated is a durable article, not an Ethernet frame or TCP segment.

## Reading and transport were separate

Another distinction that becomes clearer archaeologically:

- **transport software** moved articles between sites;
- **storage/history software** maintained the local news database;
- **reader software** presented articles to humans.

Commands and readers changed over time: `readnews`, `rn`, `trn`, `nn` and others belong to different layers of the Usenet user experience.

## Usenet is not identical to “the Internet”

Usenet traffic eventually crossed TCP/IP links and NNTP replaced UUCP for many feeds, but the early network was not dependent on Internet reachability.

That distinction matters because it demonstrates that 1980s network culture spread across several partially overlapping infrastructures:

- ARPANET/Internet;
- UUCP;
- BITNET;
- commercial packet networks;
- dial-up BBS networks;
- vendor networks.

Gateways and users stitched these worlds together.

## The economics of transit deserves its own history

Participant histories describe institutions such as DEC and Bell Labs carrying long-distance feeds that smaller academic sites could not afford.

A future dataset should record for each known high-degree UUCP/Usenet site:

- who initiated each call;
- approximate call schedule;
- modem speed;
- telephone tariff zone;
- whether the line was dial-up or leased;
- what traffic classes were accepted;
- when the feed began and ended;
- which institution paid.

This would turn famous ASCII UUCP maps into an infrastructure history rather than decorative nostalgia.

## Primary/source trail

1. D. A. Nowitz and M. E. Lesk, **A Dial-Up Network of UNIX Systems**, preserved in BSD system-manager manuals: <https://bitsavers.trailing-edge.com/pdf/usenix/Usenix_BSD_Manuals/4.3_1st_printing_198611/SMM_Unix_System_Managers_Manual_4.3BSD_198604.pdf>
2. Seventh Edition UNIX documentation index at TUHS: <https://www.tuhs.org/cgi-bin/utree.pl?file=V7/usr/doc/index>
3. Michael Lesk publication list, including UUCP papers: <https://www.lesk.com/mlesk/pub.html>
4. Duke University retrospective on Usenet's origin: <https://today.duke.edu/2010/05/usenet.html>
5. USENIX, **Distributing the News**, historical account of UUCP/A News/B News: <https://www.usenix.org/system/files/login/issues/login_aug15_issue.pdf>
6. USENIX history pages and award recognizing Truscott, Bellovin and Ellis: <https://www.usenix.org/about/awards/flame>
7. TUHS Usenet archive, surviving C News source patches: <https://www.tuhs.org/Usenet/comp.sources.bugs/1990-January/002455.html>
8. Peter Honeyman, **PATHALIAS or The Care and Feeding of Relative Addresses**: <https://scholar.archive.org/work/k62latlmgzf3xmxtfpnrqn2kvy>

## Unresolved excavation tasks

- recover exact V6 and V7 UUCP implementation/source chronology;
- document each UUCP wire protocol (`g`, `f`, later variants) separately;
- catalog common modems/automatic calling units used in Bell Labs and universities;
- reconstruct `L.sys`/`Systems`, `Devices`, `Permissions` and related configuration-file evolution;
- preserve historical call schedules and telephone-cost discussions;
- create year-by-year UUCP maps with provenance;
- recover the earliest Usenet announcement pamphlet;
- reconstruct A News source and exact attribution/revision tree;
- reconstruct B News release tree;
- preserve complete C News release/patch history;
- document article format evolution and transition toward RFC 850/1036 conventions;
- document NNTP transition without pretending UUCP disappeared immediately;
- trace major transatlantic and transpacific feeds;
- build a site ledger for famous hubs such as `research`, `decvax`, `ihnp4`, `seismo`, `uunet` and others.

UUCP/Usenet proves that a network can be global even when its links are temporary, its routes are social agreements, and a message can spend the night sitting on a disk waiting for a telephone call.