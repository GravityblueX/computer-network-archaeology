# From Internet gateway to IP router: the BBN machine behind a changing word

Modern networking uses *router* so naturally that older documents can become confusing. In early Internet engineering, the device that forwarded IP datagrams between networks was normally called a **gateway**.

This note reconstructs the 1982 BBN DARPA Internet Gateway and uses it to show how the word *gateway* gradually shifted meaning.

## The key terminology warning

RFC 1208 (1991) states the historical relationship explicitly: **gateway** was the original Internet term for what would later normally be called a router or IP router.

By the 1990s, *gateway* increasingly meant a translator or application-layer intermediary, while *router* became the preferred name for an IP forwarding device.

Therefore:

> Never modernize an old document silently.

If a 1982 document says *gateway*, preserve the original term and explain that it is functioning as an IP router.

## The 1982 BBN Internet Gateway

RFC 823, written by Robert Hinden and Alan Sheltzer, is a detailed status report on BBN's DARPA Internet Gateway as it existed in 1982.

Its core purpose was straightforward:

```text
network A
   ↓
BBN Internet Gateway
   ↓ inspect/forward IP datagram
network B
```

But its implementation shows how much machinery was required to make heterogeneous networks look like one Internet.

## Hardware platform

The implementation described by RFC 823 ran on **DEC PDP-11 / LSI-11 16-bit processors**.

Earlier gateway code had been written in **BCPL** and used the ELF and later MOS operating environments. In late 1981 BBN began a new implementation optimized for an operational communications facility rather than a research-only testbed.

The new code was written largely in **MACRO-11 assembly language** to conserve memory for packet buffers, monitoring and future mechanisms.

This is a revealing inversion of modern expectations: software abstraction was traded away because packet buffers were more valuable than programmer convenience.

## Software architecture

RFC 823 divides the gateway software conceptually into:

1. **device drivers**;
2. **network-specific software**;
3. **shared gateway software**.

This separation is one of the clearest early examples of the architectural problem every router still has:

```text
specific interface hardware
        ↓
link/network attachment logic
        ↓
common IP forwarding core
        ↓
other attachment logic
        ↓
other hardware
```

The Internet layer exists precisely because the media below it can differ.

## The interface list is an archaeological treasure

RFC 823 lists hardware/network interfaces supported or planned by the gateway. The described implementation included support for devices such as:

- ACC LSI-11 1822;
- DEC IMP11-A 1822;
- ACC LHDH 1822;
- ACC VDH interfaces;
- **Proteon Ring Network**;
- RSRE HDLC;
- **Interlan Ethernet**;
- **BBN Fibernet**;
- planned ACC interfaces for X.25 and HDH.

This single list demonstrates why “the early Internet ran on ARPANET” is inadequate.

A gateway could simultaneously stand with one foot in ARPANET's 1822 world and another in Ethernet, ring networks, HDLC links or experimental fiber.

## Network-specific routine boundary

For every attached network, the gateway maintained a set of routines implementing the local attachment's operations.

Those routines handled tasks such as:

- interface initialization;
- sending and receiving packets;
- local addressing/encapsulation;
- status/error handling;
- network-specific timing.

Above them, shared code could treat packets as Internet datagrams.

That is the actual engineering meaning of **internetworking**.

## Forwarding behavior

The gateway received an IP datagram, examined its destination network, selected an output interface/next hop and attempted to queue the packet for transmission.

If output resources were unavailable, packets could be dropped.

RFC 823 discusses output queue limits and operational traps when queue exhaustion occurred. This matters because it exposes packet loss as an intentional failure mode rather than an implementation accident.

The network layer did not promise to preserve every packet.

## Control and monitoring protocols

The 1982 gateway supported several protocols around ordinary forwarding, including mechanisms for:

- routing exchange;
- gateway-to-gateway coordination;
- error reporting;
- monitoring;
- debugging/operations.

Among these were **GGP (Gateway-to-Gateway Protocol)** and HMP-related monitoring facilities.

A complete router archaeology must therefore distinguish:

```text
forwarding plane
routing/control plane
operations/monitoring plane
```

Those categories existed before the modern names became standard.

## The Internet Operations Center

RFC 823 refers to operational monitoring and traps delivered to the **INOC** (Internet Network Operations Center).

This is historically important. The Internet was already becoming an operated infrastructure with alarms, fault reports and humans responsible for keeping gateways alive.

Future work should recover what INOC consoles looked like, which messages operators saw, escalation procedures and how gateway failures were diagnosed.

## Earlier BBN gateway lineage

RFC 823 says it superseded earlier Internet Experiment Notes including:

- **IEN 30 — Gateway Routing: An Implementation Specification**;
- **IEN 109 — How to Build a Gateway**.

These documents need to be recovered and compared line-by-line with the 1982 implementation.

The gateway architecture itself changed while TCP was being revised and split into TCP + IP. There is no single frozen “first Internet router.”

## Why the PDP-11 eventually became a constraint

RFC 823 explicitly describes pressure from:

- larger configurations;
- more interfaces;
- additional buffering;
- monitoring;
- operational robustness;
- future access controls and mechanisms.

A small general-purpose minicomputer was increasingly tight for the job.

That pressure helped create a market for purpose-built multiprotocol routers and larger gateway platforms during the 1980s.

## Gateway vs bridge

Later Internet documents carefully distinguish an IP gateway/router from a lower-layer bridge.

A bridge forwards based on link-layer/MAC information while keeping attached segments inside the same IP network. An IP router removes the incoming link-layer framing, examines the IP header and constructs appropriate framing for the outgoing network.

That distinction became increasingly important as Ethernet LANs multiplied.

## A concrete heterogeneous path

By the early 1980s, this type of path was entirely plausible:

```text
Ethernet host
  ↓ Ethernet frame
Interlan Ethernet interface
  ↓
BBN gateway (PDP-11/LSI-11)
  ↓ IP forwarding
1822 interface
  ↓
ARPANET IMP
  ↓ packet network
remote gateway
  ↓
other attached network
```

The “Internet” is the continuity of IP across those changes of underlying network.

## From research gateways to commercial routers

During the 1980s, dedicated vendors and commercial products increasingly took over work once performed by experimental gateway machines.

Important families for later excavation include:

- BBN Butterfly gateways;
- Proteon routers;
- Cisco's early router products;
- Fuzzball gateways/routers;
- multiprotocol routers from Wellfleet and others;
- UNIX/BSD hosts configured to forward packets.

The transition should be reconstructed as a hardware/software market history, not just a protocol chronology.

## Sources

1. RFC 823, **The DARPA Internet Gateway** (1982): <https://www.rfc-editor.org/rfc/rfc823.html>
2. RFC 1009, **Requirements for Internet Gateways** (1987): <https://www.rfc-editor.org/rfc/rfc1009.html>
3. RFC 1208, **A Glossary of Networking Terms** (1991), preserving the gateway/router terminology shift: <https://www.rfc-editor.org/rfc/rfc1208.html>
4. RFC 1812, **Requirements for IP Version 4 Routers** (1995): <https://www.rfc-editor.org/rfc/rfc1812.html>
5. RFC Editor index: <https://www.rfc-editor.org/rfc-index/>

## Unresolved excavation tasks

- recover IEN 30 and IEN 109 from stable archives;
- identify exact PDP-11 and LSI-11 models used at each gateway site;
- catalog interface boards listed in RFC 823, including vendor manuals and photographs;
- recover MOS gateway source if surviving;
- document memory maps and packet-buffer allocation;
- reconstruct GGP routing tables and update behavior;
- reconstruct HMP and INOC monitoring path;
- inventory gateway sites and attached network types in 1982;
- document transition from BCPL/ELF to MOS/assembly implementation;
- excavate BBN Butterfly gateway hardware;
- determine when individual documents and operators began preferring the word *router*;
- connect this lineage to commercial Proteon/Cisco/Wellfleet systems.

The device now called a router was born as a boundary machine whose entire reason for existence was that the networks on its two sides were **not the same kind of network**.