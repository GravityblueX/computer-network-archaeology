# X.25 + PAD: what a public packet-switched network looked like from a terminal

X.25 is frequently introduced as “the virtual-circuit alternative to IP.” That description is too abstract to preserve the actual system people used.

A public packet-switched data network had terminals, modems or digital access circuits, PADs, DTE/DCE interfaces, logical channels, call setup, packet switches, tariffs, host ports and operator procedures.

This note reconstructs one representative 1970s/1980s access path.

## Standards context

CCITT's data-network work grew from a joint working party established in 1968. The first X-series Recommendations appeared in the early 1970s, and the first edition of **Recommendation X.25** was approved in 1976.

The original title is precise:

> Interface between data terminal equipment (DTE) and data circuit-terminating equipment (DCE) for terminals operating in the packet mode on public data networks.

That wording matters. X.25 primarily standardizes the **subscriber/network boundary**, not the internal switching implementation of every public data network.

## Packet-mode host path

For a computer that implemented X.25 directly, a simplified stack was:

```text
host computer (DTE)
      ↓
physical interface / line
      ↓
link procedure
      ↓
X.25 packet layer
      ↓
network access DCE
      ↓
public packet-switched data network
      ↓
remote DCE
      ↓
remote X.25 DTE
```

The public network could contain proprietary switching hardware internally while presenting a standardized X.25 interface to customers.

## Three levels in early X.25

The 1976 recommendation describes the DTE/DCE interface in three broad levels:

1. **physical interface**;
2. **link level**;
3. **packet level**.

The terminology and exact procedures evolved by edition, so a historical record must always attach facts to a specific X.25 revision.

### Link level

The 1976 text includes numbered information frames, acknowledgment/retransmission procedures, timers and a configurable maximum number of outstanding unacknowledged frames.

This is one of the crucial differences between classic X.25 engineering and a simplistic “IP vs X.25” diagram: reliability was intentionally provided on the access link because many public-network access circuits were expected to be noisy or imperfect.

### Packet level

At Level 3, packets were multiplexed over **logical channels**.

The 1976 recommendation describes a logical-channel group number and logical-channel number, allowing many virtual calls or permanent virtual circuits to share one physical DTE/DCE access.

A physical line therefore did not correspond to one user conversation.

## Virtual calls

For a switched virtual call, the DTE and network perform call establishment before ordinary data transfer.

Conceptually:

```text
CALL REQUEST
      ↓
network establishes state / route
      ↓
CALL ACCEPTED / connected state
      ↓
DATA packets
      ↓
CLEAR REQUEST / CLEAR CONFIRMATION
```

The exact packet names and state transitions vary by edition and should be copied only from the relevant primary standard.

The important archaeological feature is **state in the network access model**. A conversation is represented by a logical channel for some duration instead of every packet being treated as an independent, fully addressed datagram.

## Permanent virtual circuits

X.25 also allowed **permanent virtual circuits (PVCs)**: logical channels provisioned administratively rather than created and cleared for each session.

This could make a packet network resemble a continuously available private circuit while still being implemented over shared packet-switching infrastructure.

## The terminal problem

Most ordinary asynchronous terminals could not speak X.25 packet protocol.

A Teletype, DEC terminal or ASCII CRT typically produced a stream of characters over a serial interface. Something had to convert between:

```text
character stream
```

and

```text
packet-mode virtual call
```

That device/function was the **Packet Assembler/Disassembler — PAD**.

## Triple-X PAD

The canonical CCITT PAD environment was split across three recommendations:

- **X.3** — PAD parameters/functions;
- **X.28** — asynchronous start-stop terminal ↔ PAD procedures;
- **X.29** — PAD ↔ packet-mode DTE / remote PAD control and data procedures.

Hence the later nickname **Triple-X PAD**.

A typical terminal path looked like:

```text
ASCII terminal
   ↓ serial / modem
X.28 interaction
   ↓
PAD
   ↕ X.3 parameter state
   ↓
X.29 control + user data
   ↓
X.25 virtual call
   ↓
public packet data network
   ↓
remote X.25 host
```

This is why a PAD deserves its own hardware/software catalog. It was not merely a modem and not merely a router.

## X.3 parameters: terminal behavior became network configuration

A PAD needed to know how the attached terminal behaved.

X.3 parameter sets covered issues such as:

- character echo;
- line speed / terminal characteristics;
- editing behavior;
- flow control;
- forwarding conditions;
- escape/control handling;
- idle or packetization behavior.

Different PAD vendors exposed these parameters through different user interfaces and profile systems.

For users, “using the network” could therefore involve manipulating a terminal session profile before the remote host was even contacted.

## X.28: what the human or terminal sees

X.28 defined procedures at the character-mode side of the PAD. A user could issue commands to establish a connection, clear it, inspect or change parameters and interact with the network through a textual command environment.

This user experience is historically important because it sat between dial-up terminal culture and later terminal-server/Telnet culture.

A future exhibit should reproduce several vendor PAD command syntaxes side by side.

## X.29: the control channel inside the data path

X.29 specified how PAD control information and terminal user data were exchanged with a remote packet-mode DTE or another PAD using X.25 data fields.

The 1976 provisional text distinguishes protocol identification/control from ordinary user sequences. This made PAD configuration a network-visible function rather than purely local serial-port setup.

## Public data networks were services, not just protocols

A complete X.25 history must include named public services and their business models:

- Telenet and related commercial offerings;
- Canada's DATAPAC;
- France's TRANSPAC;
- the UK's EPSS/PSS lineage;
- Tymnet interworking contexts;
- Germany's Datex-P;
- international X.75 interconnection;
- academic use through JANET and other national research environments.

For each service, this repository should eventually record:

- access speeds;
- local-call/dial access numbers;
- dedicated-line options;
- packet/byte/time charging;
- X.121 addressing;
- PAD command syntax;
- modem requirements;
- maximum packet/window sizes;
- international gateways;
- known switches and vendor equipment.

## IP over X.25: architectural layers could nest

The historical world was not cleanly divided into “TCP/IP networks” and “X.25 networks.”

RFC 877 (1983) standardized transmission of IP datagrams over X.25-based public data networks for environments including CSNET.

A virtual circuit could be opened when IP traffic appeared, kept active according to policy/cost, and later cleared.

So this completely legitimate stack existed:

```text
application
   ↓
TCP / UDP
   ↓
IP datagram
   ↓
X.25 virtual circuit
   ↓
public packet data network
```

That is an excellent example of why the repository must preserve **deployed stacks**, not ideological family trees.

## X.25 did not simply “lose”

X.25 remained useful for decades in banking, airline, transaction, research, government and industrial networks. Its engineering assumptions fit a world in which:

- carrier networks sold managed service;
- access links could be error-prone;
- terminals were common;
- predictable administrative boundaries mattered;
- traffic volumes were low enough that per-call state was practical;
- public-network billing influenced technical design.

Frame Relay, ISDN packet services, ATM and IP networks later displaced many X.25 roles, but often inherited operational concepts and customer relationships.

## Sources

1. ITU-T recommendation record for **X.25 (10/1976)**: <https://www.itu.int/ITU-T/recommendations/rec.aspx?lang=en&rec=10605>
2. ITU digital archive, **CCITT Orange Book Volume VIII.2 (1976)**: <https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/4.257.43.en.1017.pdf>
3. ITU digital archive, **Provisional Recommendations X.3, X.25, X.28 and X.29 (1976)**: <https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/4.257.43.en.1020.pdf>
4. ITU Study Group history: <https://www.itu.int/en/ITU-T/studygroups/2025-2028/17/Pages/history.aspx>
5. RFC 877, **A Standard for the Transmission of IP Datagrams over Public Data Networks**: <https://www.rfc-editor.org/rfc/rfc877.html>
6. RFC 1356, later multiprotocol X.25 encapsulation: <https://www.rfc-editor.org/rfc/rfc1356.html>

## Unresolved excavation tasks

- create a version-by-version diff for X.25 1976, 1977, 1980, 1984 and 1988;
- extract packet formats and state diagrams into legally safe original diagrams rather than copying standard artwork;
- document LAP/LAPB transition precisely;
- catalog X.3 parameter numbers by edition;
- reconstruct one real terminal session on TRANSPAC, DATAPAC, PSS and Telenet;
- identify representative PAD hardware from Racal-Milgo, Gandalf, Micom, Tymnet/Telenet and other vendors;
- record X.121 address examples and numbering plans;
- document tariff structures and how they affected virtual-circuit timeout policy;
- reconstruct IP-over-X.25 deployments in CSNET and JANET-adjacent environments;
- document X.75 network-to-network interconnection;
- distinguish public X.25 service from private X.25 packet switching;
- collect photographs/manuals for PAD front panels, serial boards and line interfaces.

The archaeological unit here is not merely **X.25**. It is the whole service chain from a human pressing a terminal key to a packet-mode host receiving data through a stateful public network.