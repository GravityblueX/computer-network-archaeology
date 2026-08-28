# IPv4 Header Field Survivorship — What the 1981 Header Still Means

RFC 791's IPv4 base-header diagram is one of the clearest examples of a living technical fossil. A modern IPv4 packet is still recognizably the same object, but not every field carries exactly the same semantics it had in 1981.

## 1. The 1981 layout

RFC 791 defines the familiar fields:

```text
Version | IHL | Type of Service | Total Length
Identification | Flags | Fragment Offset
Time to Live | Protocol | Header Checksum
Source Address
Destination Address
Options | Padding
```

The archaeology problem is not whether those bits still exist. Most do. The problem is **what each field means now**.

## 2. Field-by-field survivorship

| Field | 1981 role | Present survivorship | Archaeological note |
|---|---|---|---|
| Version | identifies IP version | **directly alive** | IPv4 still uses value 4 |
| IHL | base-header length | **directly alive** | still needed because IPv4 options make the header variable-length |
| Type of Service | service/preference semantics | **bits survive; semantics revised** | RFC 2474 redefined this octet as the Differentiated Services field |
| Total Length | complete datagram length | **directly alive** | still a 16-bit IPv4 datagram-length field |
| Identification | fragment reassembly identity | **bits alive; semantics narrowed** | RFC 6864 updates when uniqueness/value is meaningful |
| Flags | fragmentation controls | **alive** | DF/MF remain tied to IPv4 fragmentation behavior |
| Fragment Offset | fragment position | **alive** | still measured in 8-octet units |
| TTL | datagram lifetime bound | **alive, operational meaning shifted** | decremented per forwarding hop; also exploited by traceroute |
| Protocol | next-layer protocol number | **directly alive** | still demultiplexes TCP, UDP, ICMP, etc. |
| Header Checksum | protects IPv4 header | **directly alive in IPv4** | recomputed when mutable header fields change |
| Source Address | source IPv4 address | **alive** | middleboxes/NAT can rewrite it |
| Destination Address | destination IPv4 address | **alive** | routing still fundamentally consumes it |
| Options | optional control/diagnostic functions | **bits/layout alive, many branches fossilized** | some early options became obsolete, rare, filtered or security-sensitive |

## 3. Type of Service became a new semantic layer

The 1981 diagram has an 8-bit **Type of Service** octet.

RFC 2474 did not remove those bits. It explicitly defined a replacement semantic interpretation: the **Differentiated Services (DS) field**, with six bits used as DSCP and the remaining bits subsequently participating in ECN-related evolution.

This is a canonical root-hunting case:

```text
same octet position
      ↓
old TOS interpretation
      ↓ semantic replacement
Differentiated Services field
```

The packet silhouette survived more continuously than the meaning of the bits.

## 4. The Identification field survived high-speed reality by changing meaning

RFC 791's 16-bit Identification field was designed around fragmentation and reassembly.

As network speeds increased, strict uniqueness assumptions became unrealistic. RFC 6864 explicitly updates RFC 791/1122/2003 and narrows the meaningful use of IPv4 ID toward fragmentation/reassembly cases.

This is especially valuable archaeologically because the **field did not disappear**.

Instead:

```text
1981 ID field
    ↓ high-speed implementation reality
same 16 bits
    ↓ revised semantic requirements
meaningful primarily for non-atomic / fragmentation-related datagrams
```

A modern packet capture can therefore show a field whose wire location is ancient but whose operational contract is not frozen in 1981.

## 5. Fragmentation is a living but increasingly uncomfortable fossil

IPv4 fragmentation machinery remains in the base header:

- Identification;
- DF;
- MF;
- Fragment Offset.

RFC 1812 still required IPv4 routers to support the RFC 791 fragmentation model, while later operational practice strongly prefers avoiding in-network fragmentation when possible.

The archaeological lesson is that protocol formats can preserve expensive historical machinery long after deployment style shifts away from relying on it.

## 6. TTL changed from “time” into a hop-count-like operational primitive

RFC 791 says TTL is measured in seconds, but also requires every module processing the datagram to decrement it by at least one.

In practice, forwarding implementations made the field function much more like a hop limit.

That drift produced an unexpected operational afterlife:

```text
TTL forwarding rule
    +
ICMP Time Exceeded
    ↓
traceroute path discovery
```

The field survived not only as a loop-control mechanism but as a diagnostic substrate.

## 7. Protocol number is one of the cleanest living fossils

The 8-bit Protocol field remains a direct demultiplexing mechanism between IPv4 and its payload protocol.

When a contemporary IPv4 packet says:

```text
Protocol = 1   → ICMP
Protocol = 6   → TCP
Protocol = 17  → UDP
```

it is using the same architectural slot visible in the 1981 header.

## 8. Header checksum is an IPv4-specific fossil

IPv4 still checksums its header and routers must account for mutable fields such as TTL.

IPv6 deliberately omitted the analogous base-header checksum.

This makes IPv4's checksum a useful comparison fossil:

```text
IPv4: mutable base header + header checksum
IPv6: redesigned base header without it
```

The difference exposes how later protocol design reacted to earlier costs.

## 9. Options are a cemetery inside a living header

IPv4 options remain structurally possible, but many early options have become obsolete, discouraged, security-sensitive, filtered, or operationally unusual.

RFC 1812 already documents this uneven survival. It calls some options obsolete while preserving rules for parsing and forwarding others.

This makes `Options` perhaps the most literal archaeological zone in IPv4: the extensibility mechanism survives, but many artifacts that once occupied it are dead.

## 10. Root-hunting classification

IPv4 should therefore not be labeled simply “unchanged since 1981.”

A better classification is:

```text
wire skeleton: highly continuous
field widths: mostly continuous
semantic contracts: partly revised
operational use: substantially evolved
extension branches: mixed living/extinct
implementation assumptions: repeatedly corrected
```

## Primary source spine

- RFC 791 — original IPv4 specification;
- RFC 1122 — host requirements and clarifications;
- RFC 1812 — IPv4 router requirements;
- RFC 2474 — DS field replacing old TOS semantics;
- RFC 6864 — updated IPv4 Identification semantics.

## Next excavation

- map every IPv4 option to current status;
- build a versioned TOS → DSCP → ECN bit-semantic diagram;
- collect BSD/Linux kernel header definitions across decades;
- compare `struct ip` / `iphdr` layouts;
- collect real captures demonstrating old fields in modern traffic;
- trace Path MTU Discovery and the changing role of DF;
- trace NAT/checksum rewriting against this header field map.

---

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
