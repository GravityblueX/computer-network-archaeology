# ARP, RARP and Proxy ARP: when an IP address is not yet a link-layer destination

## Why this lineage matters

A host can know an Internet address and still be unable to emit a frame.

That sounds trivial today because operating systems hide the translation behind a neighbor/ARP cache. In the early Ethernet Internet, however, the boundary between an internetwork address and a local-medium address had to be designed explicitly.

The archaeology is not simply:

```text
IP -> ARP
```

It is a family of related but different questions:

```text
protocol address -> local hardware address      ARP
hardware address -> protocol address            RARP
answer on behalf of another host                Proxy ARP
avoid/use routing knowledge                     implementation choice
cache the answer                                host operational state
```

These responsibilities must be kept separate.

---

## 1. RFC 826: the protocol boundary is explicit

David Plummer's RFC 826 (November 1982) is titled *An Ethernet Address Resolution Protocol* and frames the problem directly: after a higher-level protocol has chosen a destination protocol address, the sender still needs the corresponding 48-bit Ethernet address before it can transmit on Ethernet hardware.

The crucial archaeological point is that **IP routing and Ethernet transmission are different decisions**.

Conceptually:

```text
application
   ↓
IP chooses next-hop protocol address
   ↓
ARP resolves protocol address to local hardware address
   ↓
Ethernet frame can finally be emitted
```

ARP therefore belongs at a boundary between internetwork naming/routing and a particular local medium.

Primary source:

- RFC 826 — https://www.rfc-editor.org/rfc/rfc826.html

### What RFC 826 did not imply

It did not establish that every network would forever use Ethernet or ARP.

The packet format is intentionally described in a way that carries hardware/protocol type fields. This is evidence that the problem was understood as a more general mapping problem even though Ethernet/IP became the famous deployment pairing.

Do not rewrite the historical claim as "ARP is part of Ethernet" without qualification.

---

## 2. Broadcast request, unicast knowledge

On a shared Ethernet the requester initially lacks the destination Ethernet address, so the request is broadcast. The answer supplies a binding that can be cached.

That gives a very important operational transformation:

```text
unknown mapping
    ↓ broadcast discovery
known mapping
    ↓ cache
ordinary unicast traffic
```

The cache is not merely a performance detail. It turns a network-wide/shared-medium discovery event into temporary local state.

Future artifact work should recover:

- cache lifetime defaults by operating system;
- retry timers;
- incomplete/failed cache entries;
- cache replacement policy;
- operator commands for inspecting and editing ARP tables;
- early BSD source implementations;
- router ARP table limits;
- pathological broadcast/ARP behavior on large LANs.

---

## 3. RARP is the inverse question, not "ARP version 2"

Reverse ARP (RFC 903, June 1984) asks a different bootstrapping question:

> A machine knows its link-layer address. How can it learn the corresponding protocol address?

This was especially important for diskless systems.

So the relationship is:

```text
ARP:   protocol address -> hardware address
RARP:  hardware address -> protocol address
```

not:

```text
ARP -> upgraded ARP -> RARP
```

RARP is a role inversion/companion protocol, not a formal protocol revision.

RARP's limitations also help explain why BOOTP and later DHCP became more useful: a newly started host generally needs more than one address. It may need a boot server, file name, subnet information, routers and other configuration.

See the separate host-configuration excavation:

- [`rarp-bootp-dhcp-host-configuration.md`](rarp-bootp-dhcp-host-configuration.md)

Primary source:

- RFC 903 — https://www.rfc-editor.org/rfc/rfc903.html

---

## 4. Proxy ARP: making routing invisible to a host

RFC 1027 (October 1987) documents a technique already described as widely used: a gateway responds to an ARP request **on behalf of a host on another physical network**.

The gateway returns its own hardware address. The requester therefore emits the frame to the gateway while believing it has resolved the target's address.

```text
Host A
  |
  | ARP: "who has Host B's IP?"
  v
Gateway
  |
  | replies with gateway's own MAC
  v
Host A caches target-IP -> gateway-MAC
  |
  | later sends IP packet inside Ethernet frame to gateway
  v
Gateway routes packet onward to Host B
```

Primary source:

- RFC 1027 — https://www.rfc-editor.org/rfc/rfc1027.html

### Why this existed

The University of Texas deployment described in RFC 1027 had a practical migration problem: subnetting was useful for breaking a large Ethernet into smaller physical units, but multiple host operating systems lacked subnet support.

Proxy ARP allowed the gateway to hide the subnet boundary from those hosts.

This is an excellent example of a broader historical rule:

> Network mechanisms often exist not because the clean architecture demanded them, but because installed software could not be upgraded all at once.

---

## 5. Proxy ARP is not ordinary routing

A normal IP-aware host can decide that a destination is remote and send the packet to a configured router.

Proxy ARP deliberately lets the host behave as though the target were reachable through the local address-resolution mechanism.

So preserve the distinction:

```text
ordinary routing-aware host
  destination IP -> routing table -> gateway IP -> ARP gateway

Proxy-ARP-hosted illusion
  destination IP -> ARP target directly -> gateway answers for target
```

Both may produce frames sent to a gateway MAC address, but the host's knowledge is different.

This difference matters when reconstructing historical configurations.

---

## 6. ARP survived while the LAN architecture changed

ARP outlived the shared coax Ethernet environment in which it is usually taught.

The surrounding LAN changed:

```text
shared coax
  ↓
repeaters/hubs
  ↓
bridged Ethernet
  ↓
switched Ethernet
  ↓
VLANs
```

while IPv4 ARP remained recognizable.

This is a classic `survives-as` lineage: the mapping role survives even though broadcast propagation and physical collision behavior change radically.

The later neighbor-discovery story for IPv6 must be recorded separately; IPv6 Neighbor Discovery is not simply "ARP with bigger addresses".

---

## 7. ARP and VLANs: logical broadcast domains become the relevant boundary

Once Ethernet becomes bridged/switched and later VLAN-aware, the phrase "local network" becomes increasingly logical rather than a literal single cable.

An ARP request is broadcast within a layer-2 broadcast domain, which may now be assembled by switches and VLAN configuration.

That gives another long-lived architectural coupling:

```text
ARP broadcast scope
     ↕
L2 broadcast-domain boundary
     ↕
IP subnet design (usually, but not mathematically identical)
```

The archive must not silently collapse these three into one object.

---

## 8. Operational archaeology targets

For ARP history, protocol format is only the top layer.

Recover:

### Host software

- early BSD `arp` implementation and utility;
- ARP cache structures;
- ioctl/socket APIs used to inspect/update neighbor state;
- gratuitous ARP implementation history;
- duplicate-address behavior before modern IPv4 Address Conflict Detection.

### Routers

- Cisco/Proteon/BBN ARP table implementation;
- proxy-ARP defaults by software release;
- subnet-era configuration examples;
- failure modes caused by excessive proxy ARP.

### LAN hardware

ARP itself may run above switches, but switch flooding behavior determines where broadcasts travel. Track the coupling without falsely claiming switches "implement ARP" merely because they carry it.

### Packet traces

Preserve real captures where possible:

```text
ARP request
ARP reply
cache use
cache timeout/re-resolution
Proxy ARP reply
```

---

## 9. Lineage rules for this family

Safe edges:

```text
Ethernet/IP local-delivery problem
        -> ARP design

ARP mapping role
        <-> RARP inverse bootstrap role

subnet migration + non-subnet-aware hosts
        -> Proxy ARP deployment technique

ARP IPv4 neighbor-resolution role
        -> survives across switched/VLAN Ethernet
```

Unsafe simplifications:

```text
ARP -> RARP -> DHCP                    WRONG
ARP -> Proxy ARP as a formal revision WRONG
Proxy ARP -> NAT                       UNSUPPORTED
ARP -> IPv6 ND as a simple upgrade    TOO SIMPLE
```

---

## 10. Sources

Primary:

- David C. Plummer, RFC 826, *An Ethernet Address Resolution Protocol*, November 1982 — https://www.rfc-editor.org/rfc/rfc826.html
- Ross Finlayson, Timothy Mann, Jeffrey Mogul, Marvin Theimer, RFC 903, *A Reverse Address Resolution Protocol*, June 1984 — https://www.rfc-editor.org/rfc/rfc903.html
- Smoot Carl-Mitchell, John S. Quarterman, RFC 1027, *Using ARP to Implement Transparent Subnet Gateways*, October 1987 — https://www.rfc-editor.org/rfc/rfc1027.html

Related:

- RFC 950 subnetting — https://www.rfc-editor.org/rfc/rfc950.html
- RFC 5227 IPv4 Address Conflict Detection — https://www.rfc-editor.org/rfc/rfc5227.html

---

## Open excavation questions

1. Recover the first deployed ARP implementation and source tree.
2. Identify the earliest BSD release containing the recognizable ARP cache/utility model.
3. Recover historical ARP-cache timer defaults by OS/version.
4. Find the earliest explicit `proxy-arp` operator/configuration commands in router manuals.
5. Recover the University of Texas gateway implementation referenced by RFC 1027.
6. Build an ARP/RARP/BOOTP packet-format comparison.
7. Trace gratuitous ARP, duplicate detection and failover uses as separate branches.
8. Trace IPv6 Neighbor Discovery only with explicit design documents; do not infer a direct one-step replacement.

ARP is a small protocol whose existence exposes a large truth: **an internetwork address and a local transmission address belong to different historical layers.**
