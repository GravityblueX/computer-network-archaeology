# TIP / PAD / Terminal Server / Dial Access Server

> A role genealogy of attaching many low-speed terminals and dial users to packet networks without pretending the boxes form one clean product ancestry.

Modern readers can look at several historical devices and see the same silhouette:

```text
many serial lines
      ↓
one network-facing box
      ↓
shared packet network
```

That resemblance is real, but the genealogy is not a straight line.

The ARPANET **Terminal Interface Processor (TIP)**, the public-data-network **Packet Assembler/Disassembler (PAD)**, an Ethernet **terminal server** such as the DECserver 100, and a 1990s **dial access server** such as Livingston's PortMaster all solve versions of one recurring boundary problem:

> How do many asynchronous terminals, modems, or dial users become usable network endpoints without giving every terminal a full native network stack?

The inherited *role* is durable. The protocols, network architecture, user model, and box internals change radically.

---

## 1. ARPANET TIP: put terminal access at the packet-network edge

BBN's Terminal Interface Message Processor extends the ARPANET IMP idea with terminal-facing serial ports.

The 1974 **BBN TIP Hardware Manual**, preserved in the U.S. National Technical Reports Library as report **ADA002481**, states that the TIP can connect **up to 63 terminal devices** to the ARPA Network.

The same abstract gives unusually concrete interface information:

- terminal interface conforms to **EIA RS-232C**;
- direct connection to most data modems is supported;
- serial data is full duplex;
- each of 64 ports provides four program-settable control lines;
- each port monitors six external status lines.

NTRL record:

https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/ADA002481.xhtml

This is not merely a terminal concentrator in the local-computer sense. It is part of the ARPANET packet-switching edge.

Conceptually:

```text
terminal / modem
      ↓ RS-232C
TIP terminal port
      ↓ TIP software
ARPANET packet network
      ↓
remote host/service
```

The terminal itself need not implement the full host networking machinery.

---

## 2. TIP is a sibling of the IMP, not the ancestor of every terminal server

Historically the TIP grows directly from the BBN IMP/Series-16 packet-switch environment.

That gives us a defensible implementation-family genealogy:

```text
BBN IMP platform/software lineage
          ↓ specialization
Terminal Interface Processor
```

But it would be historically reckless to continue:

```text
TIP → X.25 PAD → DECserver → PortMaster
```

without evidence.

The later devices emerge in different institutional and protocol ecosystems.

The safe question is therefore:

> Which terminal-access responsibilities recur, and how are they redistributed?

---

## 3. X.25 PAD: terminal adaptation becomes a public network service

The X.25 public-data-network world standardizes terminal adaptation through the Triple-X family:

```text
X.3  = PAD parameters/functions
X.28 = start-stop terminal ↔ PAD procedures
X.29 = PAD ↔ packet-mode DTE/PAD control/data
```

ITU still describes X.3 as the **Packet Assembly/Disassembly facility (PAD) in a public data network**.

X.28 is explicitly the DTE/DCE interface for a start-stop terminal accessing a PAD.

X.29 defines exchange of control information and user data between a PAD and a packet-mode DTE or another PAD.

Canonical ITU records:

- https://www.itu.int/rec/T-REC-X.3
- https://www.itu.int/rec/T-REC-X.28
- X-series index: https://www.itu.int/rec/t-rec-x

The architecture is therefore:

```text
asynchronous terminal
      ↓ start/stop characters
X.28 user/PAD interface
      ↓
PAD
  ├── character assembly/disassembly
  ├── echo/editing/forwarding parameters (X.3)
  └── X.29 control toward packet-side host/PAD
      ↓
X.25 virtual circuit
      ↓
packet-mode host
```

The PAD is not merely "a modem bank." It is a protocol/terminal-behavior adapter inside a public packet service.

---

## 4. TIP and PAD: similar edge role, different architecture

They can be compared at the responsibility level:

| Responsibility | ARPANET TIP | X.25 PAD |
| --- | --- | --- |
| attach asynchronous terminals | yes | yes |
| terminate serial/modem-facing interface | yes | yes |
| adapt terminal stream into packet network | yes | yes |
| standardized public terminal parameter model | ARPANET/TIP specific | X.3 |
| public DTE↔PAD command procedure | network-specific | X.28 |
| packet-side PAD/host control standard | network-specific | X.29 |
| network service model | ARPANET research/host access | public X.25 virtual-circuit service |

That supports a **role-convergence/coexistence** claim.

It does *not* prove direct design descent from TIP into Triple-X PAD standards.

If standards committee minutes, citations, or designer testimony later establish influence, add an explicit `influenced` edge. Until then, preserve the distinction.

---

## 5. Ethernet terminal servers move the boundary onto a LAN

By the mid-1980s, another form becomes common:

```text
serial terminals
      ↓
Ethernet terminal server
      ↓ LAN protocol
hosts/services on the LAN
```

A strong concrete artifact is the **DECserver 100**.

DEC's January 1985 documentation identifies it as a Terminal Server. Surviving documentation describes:

- local terminal users;
- multiple sessions;
- connection to network services;
- display of server/terminal/network information;
- local/service command modes.

The DEC LAT Architecture Network Manager's Guide lists the DECserver 100 documentation family and treats it as an Ethernet terminal-server product whose software is loaded from DECnet hosts.

Primary-document archive:

https://www.glaver.org/DECserver/General%20Documents/LAT%20and%20MOP/AA-DJ18B-TK%20LAT%20Architecture%20Network%20Manager%27s%20Guide%20July%201985.pdf

A surviving 1985 user pocket guide identifies **DECserver 100 V1.0** and first printing in January 1985.

The server changes the user/network boundary again:

```text
VT-style terminal
      ↓ serial
DECserver 100
      ↓ Ethernet
LAT service discovery/session protocol
      ↓
VAX/PDP/other LAT service host
```

The packet network is no longer a national/public WAN at this boundary. It is the local Ethernet.

---

## 6. LAT adds service naming, selection, load balancing, and sessions

A 1988 DECUS description of the original LAT terminal-server family lists:

- LAT-11;
- Ethernet Terminal Server;
- DECserver 100.

It describes service names, load balancing, fail-over, auto-configuration, multi-session operation, and an interactive terminal-server user interface.

Archival DECUS source:

https://ftpmirror.your.org/pub/misc/bitsavers/pdf/dec/decus/DECUS_SIG_Newsletters/DECUS_US_Chapters_SIG_Newsletters_V03_N10_Jun1988.pdf

This matters because the terminal server is no longer only converting characters into packets.

It is also mediating **service discovery and session selection**.

The edge role expands:

```text
serial multiplexing
      +
network service naming
      +
session switching
      +
remote/local server management
```

That is a different architectural center from an X.25 PAD, even though both expose serial terminals to a packet network.

---

## 7. Terminal server becomes a general network edge appliance

By the early 1990s, vendors increasingly combine terminal-server and router/remote-access functions.

Cisco's 1992 announcement for the Communication Server product family is explicit: the platform targets **remote router/terminal server** markets.

The entry-level 500-CS provides:

- 8 or 16 asynchronous ports;
- RS-232 and RS-423;
- hardware/software flow control;
- Cisco software;
- replacement for the earlier STS-10x terminal-server model.

The ASM-CS scales up to 112 ports and combines serial interfaces with Ethernet or Token Ring and routing/communications software.

Cisco archival announcement:

https://newsroom.cisco.com/c/r/newsroom/en/us/a/y1992/m05/cisco-systems-moves-aggressivelyiinto-remote-router-terminal-server-markets-with-four-in-one-product-family.html

This is direct evidence of **role convergence inside product families**.

The categories terminal server, communications server, remote router, and access server begin to overlap.

---

## 8. Livingston PortMaster: the terminal edge becomes an IP dial-in edge

The 1995 **Configuration Guide for PortMaster Products** shows how far the role has moved.

A PortMaster serial port can run **SLIP or PPP** for dial-in/dial-out IP access.

The guide explains:

- asynchronous dial connections;
- SLIP;
- PPP;
- LCP negotiation;
- PAP authentication;
- CHAP authentication;
- user authorization;
- hardware RTS/CTS flow control;
- multilink PPP on later ComOS revisions.

Archival manual:

https://bitsavers.computerhistory.org/pdf/livingstonEnterprises/950-1201B_Configuration_Guide_for_Portmaster_Products_Dec95.pdf

Now the path looks like:

```text
PC / workstation
      ↓ modem over telephone network
modem at ISP/site
      ↓ async serial
PortMaster
      ↓ PPP / authentication / IP routing
Ethernet / IP network
      ↓
Internet
```

This is no longer merely "terminal access to a host."

The edge box itself participates in IP-layer access and authentication.

---

## 9. The user endpoint becomes smarter

This is one of the deepest changes across the terminal-access genealogy.

Early model:

```text
dumb terminal
   ↓ characters
network edge box
   ↓ packet service
remote host does computing
```

Later dial-IP model:

```text
personal computer
   ↓ PPP frames over modem/serial link
access server
   ↓ IP packets
Internet
```

Responsibility migrates toward the user endpoint.

A terminal originally sends a character stream and relies on the network/host to provide session semantics.

A PPP dial-in computer has its own IP stack and becomes an Internet host after link negotiation.

Thus the edge device's job changes from:

> **terminal-to-host adaptation**

into:

> **subscriber-link termination + authentication + network-layer attachment**.

This is a responsibility migration, not just faster hardware.

---

## 10. Why PAD and terminal server are not interchangeable terms

A PAD has historically specific semantics tied to packet assembly/disassembly and X.3/X.28/X.29/X.25 service.

A terminal server is usually a device providing serial terminal sessions over a LAN/network protocol.

A dial access server may terminate modem/ISDN/serial subscriber links and create SLIP/PPP/IP sessions.

Some products can implement multiple roles.

Therefore preserve period terms:

```text
TIP
PAD
terminal server
communications server
dial access server
remote-access server
```

Do not normalize them all to "terminal server" or "access concentrator".

---

## 11. One recurring hardware pattern survives

Across these very different systems, a familiar hardware/operations pattern recurs:

```text
many relatively slow edge ports
        ↓
shared processing / buffering
        ↓
one or a few faster network interfaces
```

This produces recurring engineering problems:

- per-port configuration;
- flow control;
- modem signal handling;
- buffering and queueing;
- terminal speed/character settings;
- user/session authentication;
- remote management;
- port diagnostics;
- failure isolation;
- high fan-out cabling.

This role continuity is strong enough to catalogue.

Direct causal ancestry between unrelated vendor/product families must still be proved separately.

---

## 12. Management lineage crosses the terminal-access lineage

All these devices create large numbers of ports that operators must observe and control.

So the terminal-access history intersects management history:

```text
TIP port status/control lines
      ↓
PAD parameters / service signals
      ↓
terminal-server port commands/status
      ↓
access-server user/session/authentication state
      ↓
SNMP/RADIUS/central management ecosystems
```

Again, the diagram is initially a **role/property map**, not a claim of direct protocol descent.

PortMaster/RADIUS is a particularly valuable future excavation because Livingston played an important role in early RADIUS deployment/standardization history; that branch requires its own source-driven treatment.

---

## 13. Lineage edges we can defend now

### Direct implementation-family relationships

```text
BBN IMP hardware/software family
    └─ specialized-into → BBN TIP
```

and within DEC's documented product ecosystem:

```text
LAT terminal-server family
    ├─ LAT-11
    ├─ Ethernet Terminal Server
    └─ DECserver 100
```

### Strong role-descendant relationship

```text
serial terminal-server edge role
    └─ role-descends-into → multi-protocol communications/access server role
```

Cisco's 1992 product announcement directly documents terminal-server and remote-router functions converging in one product family.

### Parallel role, not yet proven ancestry

```text
TIP terminal adaptation
   ↔
X.25 PAD terminal adaptation
   ↔
Ethernet terminal-server terminal adaptation
```

Until documentary design links are found, store these as `coexisted-with` or role comparison, not `derived-from`.

---

## 14. New artifacts/sources to register

High-value artifacts:

- BBN TIP 1974 hardware revision;
- TIP terminal-interface boards/port hardware;
- DECserver 100 V1.0;
- LAT protocol/service model;
- Cisco STS-10x;
- Cisco 500-CS;
- Cisco ASM-CS;
- Livingston PortMaster model families;
- Livingston ComOS releases;
- serial modem banks used with PortMaster;
- early RADIUS server/client implementations.

High-value sources:

- BBN TIP Hardware Manual ADA002481;
- BBN TIP software/manual corpus;
- DECserver 100 hardware/operations/user guides;
- LAT architecture manuals;
- Cisco 1980s/1990s terminal-server manuals/announcements;
- Livingston configuration/manual/source archives;
- RADIUS design/implementation records;
- X.3/X.28/X.29 edition diffs.

---

## 15. Next excavation targets

1. **BBN TIP internals:** exact H316/516-family processor configuration, terminal scanner/interface cards, memory, software tasks, port buffering, modem-control lines, user command interface.
2. **TIP deployment:** named TIP sites, terminal counts, attached modem/terminal models, dial access arrangements.
3. **X.25 PAD product archaeology:** real Tymnet/Telenet/Transpac/DATAPAC PAD hardware and user command sets.
4. **DECserver 100 BOM:** processor, RAM/ROM, Ethernet transceiver/AUI, eight serial-port hardware, firmware/downline-load path.
5. **LAT wire protocol:** service advertisements, session setup, load balancing, failover, multicast/transport assumptions.
6. **Cisco terminal server lineage:** STS → MSM/ASM → 500-CS/ASM-CS and the point at which router/terminal-server roles converge.
7. **PortMaster lineage:** exact models, CPU, UARTs, Ethernet interface, modem integration, ComOS versions, PPP implementation.
8. **RADIUS:** Livingston implementation → RFC standardization and ISP operational use.
9. **One complete 1994 ISP dial-in call:** subscriber modem → telco → modem bank → access server → PPP → authentication → IP address → routed Internet.
10. **Surviving hardware:** locate preserved TIPs, DECservers, early Cisco terminal servers, PortMasters, modem racks and patch/cabling artifacts.

---

## Archaeological conclusion

There is no single object called "the ancestor of the access server."

Instead, the same boundary problem keeps returning:

> many simple or intermittent edge users must enter a packet network through shared infrastructure.

Different eras solve it differently:

```text
TIP       → terminal stream into ARPANET
PAD       → asynchronous terminal into X.25 public service
DECserver → serial terminal into Ethernet/LAT services
PortMaster→ dial subscriber into PPP/IP Internet
```

What survives is the **edge concentration and adaptation role**.

What changes is almost everything else: who owns the intelligence, what the user endpoint knows, what protocol is native, what counts as a session, and whether the edge device is merely adapting characters or actively creating an authenticated routed Internet attachment.
