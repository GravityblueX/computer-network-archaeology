# FTP: why file transfer ended up with separate control and data connections

## Why FTP archaeology matters

FTP is usually remembered as an old file-transfer command. Historically it is much more revealing: it exposes how early network designers separated **commands**, **representation**, **authentication**, **data transfer**, **file-system differences**, and **connection management**.

Its long revision history also makes it one of the best protocol-genealogy case studies in the RFC corpus.

RFC 959 itself preserves that history, reaching back to RFC 114 in 1971.

---

## 1. RFC 114: file systems were already the problem

Abhay Bhushan's RFC 114 (April 1971) presents a first-cut file transfer protocol intended to let users at one network host use files on cooperating remote hosts.

Primary source:

- RFC 114 — https://www.rfc-editor.org/rfc/rfc114.html

The engineering problem is immediately broader than "copy bytes":

- hosts have different file systems;
- access-control models differ;
- file naming differs;
- representation and byte size differ;
- error recovery matters;
- users may invoke remote storage indirectly through programs.

This becomes a repeating FTP theme: **network file transfer must hide some heterogeneity without pretending all host storage is identical.**

---

## 2. The RFC lineage is long and messy

RFC 959's historical section is unusually useful because it summarizes decades of prior FTP work.

A simplified chain includes:

```text
RFC 114 (1971)
   ↓ comments/revisions
RFC 172 / 265
   ↓
RFC 354 (1972)
   ↓
RFC 454
   ↓
RFC 542 (1973)
   ↓
... later ARPANET revisions ...
   ↓
RFC 765 / IEN 149 (1980)
   ↓
RFC 959 (1985)
```

This is only the spine. Many RFCs comment on, modify or report implementation status without fitting neatly into a single `revision-of` chain.

Primary sources:

- RFC 354 — https://www.rfc-editor.org/rfc/rfc354.html
- RFC 765 — https://www.rfc-editor.org/rfc/rfc765.html
- RFC 959 — https://www.rfc-editor.org/rfc/rfc959.html

The repository should eventually create one record for every historically meaningful FTP RFC rather than using one artifact called `FTP`.

---

## 3. Control connection and data connection are separate roles

The mature FTP architecture uses a **control connection** for commands/replies and a separate **data connection** for transferred data.

Conceptually:

```text
USER-PI  <==== control connection ====> SERVER-PI
   |                                      |
   |                                      |
USER-DTP <===== data connection ======> SERVER-DTP
```

PI = Protocol Interpreter
DTP = Data Transfer Process

This split is one of FTP's most visible architectural fossils.

Why separate them?

Because commands and replies form a persistent conversational control channel while actual data transfers may open/close independently, use different endpoints, and carry files or directory listings.

---

## 4. FTP control is historically tied to Telnet conventions

RFC 959 says the FTP control connection follows the Telnet Protocol and that FTP commands are Telnet strings using Telnet end-of-line conventions.

This creates a concrete cross-protocol lineage:

```text
Telnet NVT/control conventions
       ↓ carried into
FTP control connection syntax/behavior
```

That relationship is stronger than a vague analogy; it is explicitly documented in the specification.

See:

- [`telnet-nvt-option-negotiation.md`](telnet-nvt-option-negotiation.md)

This also demonstrates why protocol histories should not be written as isolated vertical silos.

---

## 5. Active FTP exposes early assumptions about endpoint reachability

Classic FTP can have the server establish a data connection back toward a client-specified data port.

In simplified form:

```text
client -> server: control connection
client tells server data endpoint
server -> client: data connection
```

This model makes more sense in an Internet where hosts are directly addressable than in later NAT/firewall-heavy environments.

The resulting operational pain is historically valuable: **network architecture changed under a protocol whose assumptions remained.**

Later passive operation and firewall/NAT accommodations should be traced as separate operational branches.

Do not back-project NAT-era expectations into 1970s FTP design.

---

## 6. Representation types are evidence of host heterogeneity

FTP supports multiple data representation concepts because hosts did not share one universal file representation.

Historical concerns include:

- ASCII/text representation;
- image/binary data;
- byte size;
- record structures;
- stream/block/compressed transfer modes.

This shows that application protocols once had to confront host storage representation differences more explicitly.

Future work should build a revision matrix showing which types/modes existed in each RFC generation and which disappeared or became rarely used.

---

## 7. File structure and transfer mode are separate axes

Early FTP is especially valuable because it distinguishes things modern users often collapse into "binary vs text".

RFC 354, for example, discusses:

- file structure;
- record boundaries;
- end-of-file/end-of-record semantics;
- stream transfer mode;
- representation types and byte sizes.

These distinctions reflect mainframe/minicomputer diversity and record-oriented storage.

A modern client UI that shows `ASCII` and `binary` exposes only a small surviving surface of that deeper historical model.

---

## 8. Authentication and remote file-system commands become protocol state

FTP embeds user/session control such as USER/PASS and file-system operations into the protocol conversation.

The protocol therefore combines:

```text
session/authentication state
remote pathname/file-system operations
representation negotiation
transfer setup
transfer execution
status/error replies
```

This is why FTP is not just "TCP port 21 plus file bytes".

---

## 9. RFC 765 to RFC 959: same recognizable protocol, revised specification

RFC 959 (October 1985) formally obsoletes RFC 765 / IEN 149 and says the edition is compatible with the previous one while adding optional commands such as CDUP, SMNT, STOU, RMD, MKD, PWD and SYST.

This is a useful lineage category:

> **formal protocol revision with continuity and compatibility, not architectural replacement.**

The exact field/command differences should eventually be machine-readable.

---

## 10. FTP became an operational collision point with NAT and firewalls

The separate data connection later causes major deployment complexity when:

- clients sit behind NAT;
- firewalls permit only explicitly tracked outbound flows;
- servers return embedded network addresses/ports;
- active/passive behavior differs.

This produces a later archaeology branch:

```text
original directly reachable host model
        ↓
firewall/NAT Internet
        ↓
FTP helpers / ALG behavior
passive mode prevalence
firewall-specific configuration
```

Do not confuse this with core FTP's original design history.

---

## 11. FTP and mail once overlapped

Early ARPANET mail was historically intertwined with FTP mechanisms. Later mail transfer responsibilities separate into dedicated mail protocols.

See:

- [`ftp-mail-mtp-smtp-esmtp.md`](ftp-mail-mtp-smtp-esmtp.md)

This is another reminder that application-protocol boundaries were not always the boundaries familiar today.

---

## 12. Implementation archaeology

A mature FTP excavation needs more than RFCs.

Recover:

### Early hosts

- MIT/ARPANET FTP implementations;
- TENEX/TOPS-20 FTP;
- Unix/BSD FTP client/server source;
- command/feature compatibility tables.

### Software architecture

- separate PI/DTP process implementations;
- socket creation/listening behavior;
- active/passive connection code;
- restart/recovery state;
- pathname/representation conversion.

### Operator/user experience

- command-line clients;
- anonymous FTP conventions;
- archive mirrors;
- transfer logs;
- firewall/NAT troubleshooting practice.

### Security branch

- plaintext credentials;
- FTP security extensions;
- FTPS;
- role replacement by SSH/SFTP and HTTP downloads.

SFTP must not be recorded as a revision of FTP; the similar user role hides a different protocol lineage.

---

## 13. Lineage rules

Safe:

```text
ARPANET file-system interoperability problem
     -> early FTP work

RFC 114 ... many RFCs ... RFC 765 -> RFC 959
     = long standards revision genealogy

Telnet conventions
     -> carried into FTP control connection

FTP control/data split
     -> survives through mature FTP
```

Unsafe:

```text
FTP -> SFTP formal revision          WRONG
FTP = port 21 file copy              TOO NARROW
RFC 114 -> RFC 959 one direct edge   ERASES MANY INTERMEDIATE DESIGNS
passive FTP was original default     PRESENTIST
```

---

## 14. Sources

Primary:

- Abhay K. Bhushan, RFC 114, *A File Transfer Protocol*, April 1971 — https://www.rfc-editor.org/rfc/rfc114.html
- Abhay Bhushan, RFC 354, *The File Transfer Protocol*, July 1972 — https://www.rfc-editor.org/rfc/rfc354.html
- Jon Postel, RFC 765 / IEN 149, *File Transfer Protocol*, June 1980 — https://www.rfc-editor.org/rfc/rfc765.html
- Jon Postel and Joyce Reynolds, RFC 959, *File Transfer Protocol*, October 1985 — https://www.rfc-editor.org/rfc/rfc959.html

RFC 959's history section should be mined into a complete document graph.

---

## Open excavation questions

1. Turn every FTP-related RFC named by RFC 959 into a source/artifact record.
2. Build command/representation/mode diffs across major official specifications.
3. Recover working-server status reports and implementation source.
4. Reconstruct a real 1970s FTP transfer including host OS, sockets/NCP connections and user commands.
5. Trace anonymous FTP and software-distribution culture.
6. Trace active/passive mode and NAT/firewall adaptations as later operational branches.
7. Separate FTP security extensions, FTPS and SFTP lineages.

FTP is a protocol fossil from a time when **remote files, terminal conventions, transport connections and host representation differences all had to be negotiated in the open.**
