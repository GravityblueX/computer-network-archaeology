# Telnet: from ad hoc remote-terminal practice to the Network Virtual Terminal

## Why Telnet deserves archaeology

Telnet is often remembered as "the insecure remote shell before SSH." That description is useful only for modern security comparison; historically it erases the problem Telnet was actually built to solve.

Early network hosts had incompatible terminals, character sets, control conventions, echo behavior, line endings and local operating-system interfaces. The problem was not merely opening a remote command prompt. It was:

> How can a terminal or terminal-oriented process at one host interact with a different host without requiring every pair of systems to understand every terminal type?

The answer grew around the **Network Virtual Terminal (NVT)** and an option-negotiation mechanism.

---

## 1. In 1972 there was still "NO Official Telnet Protocol"

RFC 318 (April 1972) is unusually candid. Jon Postel writes that there was **no official Telnet protocol** and presents his understanding of the ad hoc protocol then in use.

Primary source:

- RFC 318 — https://www.rfc-editor.org/rfc/rfc318.html

This makes RFC 318 an excellent archaeological source because it captures a protocol family while standardization is still unsettled.

It describes three major substructures:

```text
connection establishment / ICP
        +
Network Virtual Terminal
        +
Telnet control signals
```

That composition later changes as the Internet transport layer changes.

---

## 2. The NVT is an interoperability machine

RFC 318 defines the NVT as a bidirectional character device with a printer and keyboard abstraction.

The crucial idea is indirection:

```text
local terminal A
   ↓ local mapping
Network Virtual Terminal representation
   ↓ network exchange
remote mapping
   ↓
remote host/process B
```

Instead of every host supporting every physical terminal, each side supports a common virtual representation.

This pattern survives far beyond Telnet:

> define a canonical network representation at the boundary, then translate locally.

But direct ancestry into later protocols must be documented separately.

---

## 3. Telnet normalized more than characters

Historical Telnet had to confront behaviors that modern terminal emulators hide:

- local vs remote echo;
- carriage return / line feed conventions;
- interrupt/break behavior;
- synchronization;
- terminal control signals;
- character-set mapping;
- connection establishment.

These are not cosmetic. A hardcopy terminal, glass terminal, timesharing host and network process may disagree about who echoes typed characters or what "end of line" means.

The protocol therefore carries assumptions about **human interaction timing and terminal behavior**, not only byte transport.

---

## 4. NCP-era Telnet and TCP-era Telnet are not the same artifact

The early ARPANET Telnet environment depended on the Network Control Program and Initial Connection Protocol conventions.

By RFC 764 (June 1980), a Telnet connection is described as a **TCP connection** containing data interspersed with Telnet control information.

Primary sources:

- RFC 764 — https://www.rfc-editor.org/rfc/rfc764.html
- RFC 854 — https://www.rfc-editor.org/rfc/rfc854.html

This gives a clear responsibility migration:

```text
ARPANET/NCP connection machinery
        ↓ network transition
TCP connection
        +
Telnet NVT/control/option semantics
```

The application role survives while the transport substrate is replaced.

Do not describe the 1983 TCP/IP transition as if Telnet itself vanished and was reinvented.

---

## 5. RFC 854: stable Telnet core

RFC 854 (May 1983) obsoletes RFC 764 and defines Telnet for the ARPA Internet community.

Its goal remains a fairly general bidirectional eight-bit byte-oriented communications facility, primarily for terminal devices and terminal-oriented processes.

The mature structure is roughly:

```text
TCP byte stream
   |
   +-- ordinary NVT data
   |
   +-- IAC command introducer
          |
          +-- Telnet commands
          +-- WILL / WON'T / DO / DON'T option negotiation
```

The option system is crucial because Telnet cannot freeze one universal terminal behavior forever.

---

## 6. Option negotiation is a protocol within the protocol

Telnet options allow peers to negotiate capabilities and behaviors.

Conceptually:

```text
WILL X   = I offer/will perform option X
WON'T X  = I refuse/stop X
DO X     = please perform X
DON'T X  = please do not perform X
```

This creates two historical layers:

1. the **base Telnet protocol**;
2. a large corpus of **Telnet option RFCs**.

Future cataloging must split option documents such as echo, suppress-go-ahead, terminal type, window size and environment negotiation into their own records.

A single `TELNET` row is not enough.

---

## 7. Why negotiation was necessary

Real terminals differ.

A network service might need to know or negotiate:

- who echoes;
- whether character-at-a-time or line-oriented behavior is expected;
- terminal type;
- screen/window dimensions;
- binary vs NVT assumptions;
- environment information.

Telnet's option model is therefore a historical response to heterogeneous endpoints.

This makes it a useful ancestor/analogy source for capability negotiation in later protocols, but direct influence claims require explicit evidence.

---

## 8. Telnet became infrastructure, not only a user command

FTP's control connection historically follows Telnet conventions. RFC 959 explicitly discusses the relationship between FTP and Telnet and says FTP commands are Telnet strings terminated by Telnet end-of-line conventions.

So Telnet survives as a **protocol substrate/convention inside another application protocol**, even where a human is not running a `telnet` program.

See:

- [`ftp-control-data-evolution.md`](ftp-control-data-evolution.md)

This is exactly the sort of hidden lineage this repository exists to preserve.

---

## 9. The user-facing `telnet` client is another artifact

Separate:

```text
Telnet protocol specification
Telnet option specifications
host Telnet server/daemon
user Telnet client program
terminal driver / PTY integration
```

Unix `telnet`, `telnetd`, pseudo-terminals, login programs and terminal databases all belong to implementation archaeology, not to the wire protocol alone.

Future source work should recover:

- early NCP Telnet clients/servers;
- TENEX/TOPS-20 Telnet;
- BSD `telnet` and `telnetd` source trees;
- PTY integration;
- option bugs/interoperability notes;
- terminal-type database interactions.

---

## 10. Security was not the original organizing problem

Telnet later became notorious because credentials and session data are normally exposed without modern cryptographic protection.

That is historically important, but it should be added as a later branch:

```text
remote terminal interoperability
          ↓
widely deployed remote login
          ↓ changing threat model
cleartext authentication/session becomes unacceptable
          ↓
secure remote-login alternatives (e.g. SSH)
```

Do not back-project late-Internet hostile-network assumptions onto the original engineering problem.

Likewise, do not claim SSH is a formal Telnet revision. It occupies overlapping user roles with radically different security and protocol architectures.

---

## 11. Telnet and the physical terminal world

Telnet sits above another deep hardware history:

```text
Teletype / serial terminal
      ↓
RS-232 / modem / terminal server
      ↓
network access
      ↓
Telnet NVT / remote terminal session
```

Connect this excavation to:

- [`bell-data-set-rs232-v24.md`](bell-data-set-rs232-v24.md)
- [`terminal-access-tip-pad-terminal-server-portmaster.md`](terminal-access-tip-pad-terminal-server-portmaster.md)

A remote Telnet session can be conceptually independent of the physical terminal, but historical deployments were not.

---

## 12. Lineage rules

Safe:

```text
heterogeneous terminal problem
    -> NVT abstraction

ad hoc/NCP-era Telnet
    -> formalized Telnet revisions

NCP connection substrate
    replaced by TCP
while Telnet application semantics survive

Telnet conventions
    carried into FTP control protocol
```

Unsafe:

```text
Telnet = remote shell only                  TOO NARROW
Telnet -> SSH formal revision               WRONG
RFC 318 -> RFC 854 one clean revision edge TOO SIMPLE; many intermediate documents/options exist
NVT -> every later virtual-terminal system  UNSUPPORTED
```

---

## 13. Sources

Primary:

- Jon Postel, RFC 318, *Telnet Protocols*, April 1972 — https://www.rfc-editor.org/rfc/rfc318.html
- Jon Postel, RFC 764 / IEN 148, *Telnet Protocol specification*, June 1980 — https://www.rfc-editor.org/rfc/rfc764.html
- Jon Postel and Joyce Reynolds, RFC 854, *Telnet Protocol Specification*, May 1983 — https://www.rfc-editor.org/rfc/rfc854.html

Related early RFCs referenced by RFC 318 should be excavated individually, including RFC 139, RFC 158 and later Telnet issue/option documents.

---

## Open excavation questions

1. Build the full RFC 139/158/318/435/.../764/854 revision graph.
2. Recover NCP-era Telnet source implementations.
3. Inventory every early Telnet option RFC and first implementations.
4. Recover terminal-type negotiation and terminal database interactions.
5. Trace Unix PTY + `telnetd` implementation genealogy.
6. Reconstruct a real 1970s terminal → TIP → Telnet → host login path.
7. Trace the security transition into encrypted remote-login systems without asserting false formal ancestry.

Telnet is best understood not as an obsolete shell command, but as a long-lived answer to a foundational network question: **how do unlike interactive terminals and hosts agree on a common conversation?**
