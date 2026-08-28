# Duke ↔ UNC, 1979–1980: reconstructing the first Usenet path beneath `netnews`

> Status: active excavation. This chapter separates **Usenet's article-distribution software** from the **UUCP transport system**, and separates the **Duke–UNC leased path** from unrelated 300-baud dial-up UUCP calls at Duke. The objective is not merely to repeat that “Usenet began at Duke and UNC,” but to recover the machines, UNIX releases, serial hardware, telephone facilities, auto-dialers, UUCP jobs, news software, call economics and unresolved modem models that made the first network practical.

## 1. Usenet was initially an application over somebody else's transport

The most useful mental model is:

```text
human writes article
        ↓
prototype netnews / A News
        ↓
article formatted for a remote system
        ↓
UUCP remote execution / file transfer
        ↓
UNIX spool and scheduler
        ↓
serial / modem / leased or dial telephone path
        ↓
remote UUCP
        ↓
remote news program
        ↓
remote article store / readers
```

Usenet did not invent the underlying machine-to-machine dialup system. **UUCP supplied the transport machinery.** Netnews/A News supplied a new distributed publication convention on top of it.

This distinction is essential because early news software was deliberately capable of using transports other than UUCP.

## 2. The Duke machine: PDP-11/70 + UNIX Version 7

Tom Truscott's retrospective identifies the Duke Computer Science machine as a **DEC PDP-11/70**. Jim Ellis installed UNIX **Version 7** in 1979.

V7 mattered because it included UUCP and its documentation. Truscott specifically remembered two V7 manual papers:

- D. A. Nowitz and M. E. Lesk, *A Dial-Up Network of UNIX Systems*;
- D. A. Nowitz, *UUCP Implementation Description*.

The upgrade also broke an older local “news”/announcement program obtained from an early UNIX user-group tape, creating one of several motivations to build a replacement.

A future Duke PDP-11/70 artifact record needs:

- exact CPU/option configuration;
- core or semiconductor RAM size;
- disk drives/controllers;
- serial terminal/interface boards;
- telephone-line interfaces;
- V7 build date and local patches;
- UUCP configuration files;
- hostname(s) and phone numbers;
- physical location/rack/console;
- surviving hardware provenance.

## 3. Duke's machine had both auto-dial and auto-answer capability

Truscott says V7 UUCP could send files between telephone-connected UNIX sites when one end had an auto-dialing telephone/modem and the other an auto-answering telephone/modem, and adds that the **Duke Computer Science PDP-11/70 had both**.

He then makes a particularly important hardware remark:

> they **built the auto-dialers themselves**.

That means the path contained custom local communications hardware, not simply a store-bought “Hayes modem” in the later PC sense.

The custom auto-dialer deserves its own artifact record.

Open questions:

- relay/DTMF/pulse dialing method;
- serial or parallel control interface;
- modem model attached to the dialer;
- answer-unit hardware;
- telephone coupler / direct-connect arrangement;
- Bell System customer-provided-equipment rules;
- schematic and builder attribution;
- dialing software hooks in UUCP;
- whether both Duke phone lines had identical hardware.

## 4. Duke already had a small UUCP neighborhood before Usenet

Truscott says the Duke system used UUCP to reach:

- **two other UNIX machines at Duke**;
- **one machine at UNC-Chapel Hill**;
- and, separately, Bell Labs' machine `research`, which called Duke nightly after Truscott arranged the connection.

This means the idea for Usenet arose inside an already functioning **local and long-distance UUCP topology**, not from a blank slate.

The discovery queue should identify all four peer machines by:

- hostname;
- department;
- model;
- UNIX release;
- modem/line type;
- call direction;
- polling schedule;
- telephone cost.

## 5. The UNC machine: PDP-11/45, not the later VAXes

Steve Bellovin's participant history identifies the UNC Computer Science origin machine as a **PDP-11/45**.

His recollection is unusually useful because it gives the pre-Usenet hardware context:

- the machine had originally been intended for molecular-graphics work;
- it initially ran DEC DOS;
- it had extra terminal ports that **did not have modem-control lines**;
- those ports were connected to the university computer center's **Gandalf port selector**;
- with help from Duke, UNC brought up **6th Edition UNIX** as a part-time operating system;
- additional money later bought a better **8-port terminal adapter** and more RAM;
- VAX-11/780 systems came later, but **Usenet began on the smaller PDP-11/45**.

A separate participant recollection published by Duke describes that UNC PDP-11/45 as having roughly **128 KB RAM and 60 MB disk packs**, but these component values should be confirmed against UNC equipment records before being promoted to canonical structured fields.

## 6. The Gandalf port selector is part of the network archaeology

The mention of a **Gandalf port selector** is exactly the kind of detail a milestone history loses.

Before inexpensive ubiquitous Ethernet, institutions often used terminal/port switching systems to let terminals reach different computers. At UNC, a PDP-11/45 terminal-port limitation and the campus port-selector infrastructure influenced how external communication could be arranged.

We need to identify:

- exact Gandalf model;
- port count;
- physical interface standard;
- switching method;
- connection from UNC CS to the university computer center;
- whether the early UUCP/Usenet path traversed the Gandalf system or used the later 8-port adapter directly;
- modem-control workarounds required by the original ports.

Do **not** infer that because Bellovin mentions the Gandalf in the machine's history it necessarily carried every Usenet call. The exact 1979 path remains to be proven.

## 7. Netnews began as a shell-script proof of concept

Truscott recalls meetings involving:

- Jim Ellis;
- Tom Truscott;
- Dennis Rockwell;
- Steven Bellovin.

They discussed:

- article transfer format;
- basic software behavior;
- terminology such as **newsgroups**.

Bellovin implemented the idea in **shell scripts** as a proof of concept. Truscott remembered it as slow but functional.

This source should be reconciled with later summaries that give specific line counts such as “three pages” or “150 lines.” Unless the original script survives or a participant gives a precise copy, those line-count claims should not be treated as established implementation facts.

## 8. A News was a separate production implementation

Stephen Daniel, a Duke graduate student, wrote the first production news software usually called **A News** and introduced the dotted newsgroup structure associated with early Usenet.

The archaeology should keep at least three software objects separate:

```text
Bellovin shell-script proof of concept
        ↓
A News / production netnews
        ↓
B News
        ↓
C News / later transport ecosystem
```

Do not describe the shell script and A News as the same release.

## 9. The first path was not simply “300-baud modems between Duke and UNC”

A widespread modern simplification is:

> Duke and UNC exchanged Usenet over 300-baud modems.

Truscott's interview shows why this needs qualification.

He describes a **different Duke UUCP incident** in fall 1979:

- Jothy Rosenberg had a UNIX PDP-11 at Duke Student Health;
- UUCP moved increasingly large files between it and Duke CS;
- Duke had only **two telephone lines** available for that traffic context;
- one **500 KB** transfer at **300 baud** took about **five hours** and caused complaints.

But Truscott then explicitly distinguishes early news traffic:

- **news to UNC and `phs` used fast leased lines**;
- news to more distant sites happened **in the dead of night**.

Therefore the 500-KB/300-baud story is valuable evidence for the economics/performance of Duke UUCP, but **it is not evidence that the first Duke–UNC news feed itself used a 300-baud dial-up line**.

## 10. Fred Brooks and the Duke–UNC leased line

Truscott says Fred Brooks was not involved in designing Usenet, but **paid for a leased line between UNC and Duke**. That line made UUCP communication between the universities effectively a “free good” to its users because there was no per-call long-distance charge.

This is a remarkable example of how infrastructure economics can change network topology.

Without the leased line:

```text
more articles
 → longer calls
 → larger telephone bill
 → pressure to batch/poll selectively
```

With a prepaid leased circuit:

```text
marginal cost of another transfer ≈ invisible to user
 → easier routine propagation
 → tighter Duke↔UNC relationship
```

The archival target is now concrete: locate UNC/Duke purchase orders, telecom bills, line-service records, circuit numbers and modem equipment associated with Brooks' funded circuit.

## 11. What exactly was “fast”?

Truscott calls the UNC and `phs` lines “fast leased lines” in contrast to the 300-baud telephone transfer.

He does **not**, in the cited interview, give their exact bit rate.

Therefore the archive must not manufacture one.

Candidates that were technologically plausible in the period include 1200/2400/4800/9600-bps private-line equipment or other institutional serial facilities, but these remain hypotheses until a Duke/UNC configuration file, modem manual, bill or participant record identifies the service.

Required fields:

- exact rate;
- synchronous vs asynchronous;
- Bell data-set/modem model;
- two-wire/four-wire;
- full/half duplex;
- clocking;
- leased-line tariff;
- serial adapter at PDP-11/70;
- serial adapter at PDP-11/45;
- call/login procedure;
- UUCP `Systems`/`Devices` configuration.

## 12. UUCP made the telephone network into a store-and-forward computer network

The Bell Labs UUCP design supplied machinery for:

- system naming;
- queued file-transfer requests;
- remote command execution;
- scheduled calls;
- authentication/permissions;
- spool files;
- retry after failure;
- multi-hop mail/routing conventions layered above it.

The key historical transformation is that the telephone network did **not** need to remain connected continuously.

A site could:

```text
queue work on disk
       ↓
wait until scheduled call window
       ↓
dial remote UNIX system
       ↓
exchange queued work
       ↓
hang up
       ↓
remote site later calls another peer
```

This is a network whose topology changes with the clock.

## 13. Long-distance cost shaped time itself

The early UUCP/Usenet world often scheduled distant calls at night because telephone tariffs could be cheaper and machines/users competed for limited lines.

Truscott explicitly remembers early news elsewhere happening “in the dead of night.”

This gives the network a temporal topology:

- at 14:00, two sites may be disconnected;
- at 02:00, a phone call temporarily creates an edge;
- after hangup, the edge disappears but messages persist on disk.

A historical topology map therefore needs more than lines between nodes. It needs **call windows and costs**.

## 14. The Duke phone lines were scarce shared resources

The Student Health incident shows that file transfer competed with other institutional uses. A five-hour 300-baud job could occupy a meaningful fraction of the department's available communications capacity.

At 300 bit/s, even before protocol overhead, the theoretical raw throughput is only about:

```text
300 bits/s
≈ 37.5 bytes/s raw
≈ 135 KB/hour raw maximum
```

A 500-KB file therefore cannot transfer instantaneously even under ideal conditions; framing, UUCP protocol overhead, errors/retransmission and practical line performance further reduce useful throughput. Truscott's “about five hours” recollection is entirely plausible as an operational scale.

The important historical point is not the arithmetic but the resource consequence: **one file could occupy a line for a large part of a working day.**

## 15. Duke ↔ Bell Labs `research`: a nightly UUCP edge

After returning from Bell Labs in 1979, Truscott arranged a UUCP connection between Duke and Bell Labs' machine named **`research`**. He says `research` called Duke nightly.

This gives us another early edge to reconstruct:

```text
Bell Labs `research`
DEC PDP-11/70 (participant recollection)
        ↓ nightly UUCP call
telephone/modem path
        ↓
Duke CS PDP-11/70
```

The exact modem models and call tariff remain open.

This edge is important because it tied Duke's otherwise non-ARPANET UNIX environment into the Bell Labs UNIX development world using ordinary telephone infrastructure.

## 16. Usenet article transport was intentionally pluggable

Truscott quotes early 1980 documentation explaining that each remote system could have:

- a subscription list;
- a **transmission protocol**.

When an article needed delivery, the configured transport program received the formatted article. It might:

- invoke remote execution;
- encapsulate the article in mail;
- use another non-UUCP mechanism.

Truscott says A News had general support for non-UUCP transports very early in 1980.

So Usenet should not be defined as “the UUCP protocol.” More accurately:

> Early Usenet's dominant substrate was UUCP, but its news application architecture could hand an article to different transport mechanisms.

## 17. Early A News storage details belong in network history

Truscott recalls implementation details that show how resource limits shaped the social system:

- newsgroup names documented as 14 characters or fewer by convention;
- users' subscription lists stored in `/usr/spool/news/uindex`;
- an early 200-byte line limit constrained explicitly listed subscriptions;
- `/usr/spool/news/ngfile` later held known newsgroup names;
- A News did not initially store articles in a directory tree per newsgroup;
- PDP-11/70 memory limited the number of articles the program could comfortably process in one batch to roughly 1000.

These are application-software details, but they affect the shape and scalability of the network's information flow and therefore belong in this archive.

## 18. A real first-feed reconstruction still has missing physical boxes

At present, the strongest reconstruction is:

```text
Duke CS
DEC PDP-11/70
UNIX V7
A News / UUCP
custom auto-dial/auto-answer capability
        ↓
[exact Duke serial adapter unresolved]
        ↓
[exact leased-line modem/data set unresolved]
        ↓
Duke ↔ UNC leased telecommunications circuit
funded by Fred Brooks
        ↓
[exact UNC modem/data set unresolved]
        ↓
[exact UNC serial/port-selector path unresolved]
        ↓
UNC CS
DEC PDP-11/45
UNIX V6-era / transition environment
prototype netnews / UUCP
```

This is already much richer than “two computers connected by modem,” but the central physical artifacts remain unidentified.

## 19. Required Duke/UNC archival hunt

### Duke
- PDP-11/70 purchase/configuration records;
- 1979 system logs and UNIX account archives;
- UUCP `L.sys` / `Systems`, `Devices`, `Dialcodes` ancestors/configuration;
- custom auto-dialer schematics/source;
- telephone line numbers and bills;
- leased-line service orders;
- modem/data-set photographs and model plates;
- early A News source/distributions;
- Jim Ellis / Tom Truscott / Stephen Daniel papers.

### UNC
- PDP-11/45 asset record;
- 8-port terminal-adapter model;
- Gandalf port-selector model and port maps;
- UNIX V6/V7 upgrade records;
- UUCP configuration;
- leased-line modem/data set;
- Fred Brooks funding/purchase records;
- Steve Bellovin early script/source material;
- equipment photographs.

### telecommunications
- line rate;
- service type;
- local/long-distance provider;
- circuit identifier;
- monthly cost;
- install date;
- termination equipment;
- testing/maintenance records.

## 20. Provenance question: does first-Usenet hardware survive?

Later informal recollections claim the original Duke PDP-11/70 survived in private hands. Such claims are valuable leads but are **not enough for canonical provenance**.

A surviving-specimen record requires:

- serial number;
- Duke asset tag;
- chain of custody;
- photographs;
- installed boards/disks;
- evidence tying the machine to the 1979 CS installation;
- comparison against archival inventory.

The same hunt should be made for UNC's PDP-11/45, Gandalf equipment and original communications hardware.

## 21. Why this path matters

ARPANET histories emphasize persistent leased packet links and dedicated packet switches.

Usenet/UUCP demonstrates a different route to global networking:

```text
cheap/reused UNIX computers
+ telephone/leased serial links
+ disk spooling
+ scheduled calls
+ local administrative cooperation
+ software that tolerates delay
= a large social network without continuous end-to-end connectivity
```

It is not a failed approximation to the Internet. It is a different infrastructure architecture optimized for different economic constraints.

## 22. Open excavation checklist

1. Identify the exact Duke PDP-11/70 configuration and serial number.
2. Identify the exact UNC PDP-11/45 configuration, 8-port adapter and storage.
3. Identify Duke's custom auto-dialer hardware and recover schematics/source.
4. Identify both ends' modem/data-set models for the Duke–UNC leased line.
5. Establish the leased-line bit rate and service type from contemporary records.
6. Determine whether the UNC Gandalf port selector participated in the first UUCP/Usenet path.
7. Recover 1979 UUCP configuration files from Duke and UNC.
8. Recover Bellovin's shell-script proof of concept.
9. Recover earliest A News source and map transport hooks.
10. Identify the two other Duke UNIX UUCP peers and the `phs` machine precisely.
11. Reconstruct Duke ↔ Bell Labs `research` nightly call hardware/cost.
12. Recover long-distance bills and call schedules for early remote feeds.
13. Build a time-dependent 1979–1981 UUCP/Usenet topology rather than a static map.
14. Trace surviving PDP-11 hardware by serial/asset provenance.
15. Keep 300-baud Student Health traffic separate from the faster leased Duke–UNC news path.

## Sources

Primary/participant and archival leads:

- Ronda Hauben, interview with Tom Truscott, *Amateur Computerist* 8(1), 1998, especially pp. 5–6: https://www.columbia.edu/~hauben/acn/ACN8-1.pdf
- Steven M. Bellovin, *The Early History of Usenet, Part I: The Technological Setting* / participant blog, 2019: https://www.cs.columbia.edu/~smb/blog/2019-11/2019-11-14a.html
- D. A. Nowitz and M. E. Lesk, *A Dial-Up Network of UNIX Systems* — documented in Seventh Edition UNIX manual indexes; archival discovery: https://www.tuhs.org/cgi-bin/utree.pl?file=2.11BSD%2Fdoc%2F2.10%2Fv7index
- Duke Today, *A Piece of Internet History* (2010), institutional/participant recollections: https://today.duke.edu/2010/05/usenet.html
- RFC 2235, *Hobbes' Internet Timeline*, useful only as a broad chronology cross-check: https://www.rfc-editor.org/rfc/rfc2235.html

### Evidence caution

The Truscott and Bellovin recollections are participant sources written years later. They are unusually detailed and internally useful, but machine configuration, line rate, modem model and exact chronology should be promoted to `confirmed` only when contemporary source code, manuals, bills, logs or equipment records corroborate them.
