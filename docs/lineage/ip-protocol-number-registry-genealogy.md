# IP Protocol Number Registry Genealogy: 1, 6, 17, 47, 50, 51, 89 — and the Dead Protocols Beside Them

The IPv4 `Protocol` field is only eight bits wide, but it contains one of the richest machine-readable archaeological layers in the Internet.

The current IANA Protocol Numbers registry states that these values identify the protocol carried in the IPv4 Protocol field and are also used as IPv6 Next Header values.

A packet field therefore became a shared numeric namespace spanning two generations of IP.

## 1. Famous living assignments

The current registry includes values that are instantly recognizable in modern packet captures:

```text
1   ICMP
6   TCP
17  UDP
41  IPv6 encapsulation
47  GRE
50  ESP
51  AH
58  ICMPv6
88  EIGRP
89  OSPF
```

A network stack does not need the string `TCP` on the wire. It sees `6`.

That number is a protocol identity fossil that survives across decades of implementation rewrites.

## 2. The same registry also contains lost worlds

The numerical table preserves old protocols that most modern administrators never encounter:

```text
3   GGP
8   EGP
12  PUP
20  HMP
```

and many other historical entries.

Some assignments are marked deprecated or have references to architectures that vanished from ordinary production networks.

Thus the registry is not a clean list of modern Internet protocols.

It is a mixed layer of:

- living infrastructure;
- niche/specialized systems;
- experimental protocols;
- abandoned architectures;
- formally deprecated branches.

## 3. 1, 6 and 17 are more durable than implementations

Consider three famous values:

```text
1  ICMP
6  TCP
17 UDP
```

The original operating systems, hosts, routers and source trees that first used them are largely gone.

But modern kernels still dispatch incoming IP packets based on the same protocol-number identities.

The numeric assignment therefore outlives:

- machine architecture;
- operating-system generation;
- network-interface hardware;
- compiler/toolchain;
- vendor;
- often the original RFC text itself.

## 4. IPv6 reuses the namespace as Next Header

IPv6 redesigned the network-layer header, but it did not invent an unrelated next-protocol numbering universe.

IANA's registry explicitly notes that the same values are used for the IPv6 Next Header field.

This gives us a cross-generation continuity:

```text
IPv4 Protocol field
        ↓ numeric namespace survives
IPv6 Next Header field
```

This does **not** mean IPv6 is a header-compatible revision of IPv4.

It means one identification namespace was carried into a new network-layer architecture.

## 5. Encapsulation creates protocol-number nesting

Some values identify protocols that themselves carry other packets:

- IPv6 encapsulation;
- GRE;
- ESP;
- IP-in-IP-related mechanisms.

A packet capture may therefore reveal protocol-number ancestry at multiple layers:

```text
outer IPv4
  Protocol = 47 (GRE)
      ↓
GRE
      ↓
inner IP/Ethernet/etc.
```

The number field becomes a dispatch point for protocol composition.

## 6. Security protocols occupy the old 8-bit namespace

IPsec added ESP (`50`) and AH (`51`) without replacing the basic IPv4 protocol-dispatch mechanism.

That is historically significant:

> major security architecture was grafted into the same one-byte protocol-number system created for earlier Internet protocols.

Again, the container survived while new families entered it.

## 7. Old routing protocols sit beside modern ones

The registry places old routing/control protocols such as GGP and EGP in the same namespace as OSPF and EIGRP.

This gives a surprisingly compact routing-history cross-section:

```text
GGP     3
EGP     8
EIGRP  88
OSPF   89
```

The number table does not imply ancestry among them. It merely preserves their common need for an IP payload identifier.

That distinction is essential for the archive.

## 8. Assigned Numbers RFCs froze historical snapshots

Before today's live IANA registries, Internet parameter assignments were periodically published in RFCs titled **Assigned Numbers**.

RFC 1340 and RFC 1700 are valuable because they freeze earlier states of the table. A historian can compare:

```text
1992 snapshot
1994 snapshot
2026 registry
```

and identify:

- assignments that survived;
- protocols that became deprecated;
- new values added later;
- names/references that changed;
- institutional changes in how the registry itself was published.

## 9. RFC 3232 changes the archival medium

RFC 3232 formally obsoleted RFC 1700 in 2002.

Its reason is itself historically important: RFC 1700 was only an October 1994 snapshot, while assigned numbers had moved to an online database maintained by IANA.

So there are two genealogies at once:

```text
protocol-number assignments continue

but

publication mechanism:
periodic RFC snapshot
        ↓
live online registry
```

The standards infrastructure evolved even though many numbers remained the same.

## 10. A registry number is an interoperability promise

Why does `6` remain TCP?

Because reusing a widely deployed number for a different protocol would destroy interpretation across independent implementations.

A successful numeric assignment becomes sticky precisely because so many systems hard-code or register against it.

The apparent triviality of the number is evidence of very deep coordination.

## 11. Root-hunting classification

### Strongly living numbers

- `1` ICMP;
- `6` TCP;
- `17` UDP;
- `47` GRE;
- `50` ESP;
- `51` AH;
- `58` ICMPv6;
- `89` OSPF.

### Historical but still registry-visible

- GGP;
- EGP;
- PUP;
- HMP;
- many experimental/minority protocols.

### Deprecated branches

The live registry also preserves explicitly deprecated protocol identities.

## 12. The field is a timeline in one byte

A modern packet's protocol number may therefore point to a protocol created decades ago, while the same registry row set still contains the names of dead competitors.

The `Protocol` byte is not merely a parser selector.

It is an eight-bit doorway into Internet history.

## Sources

- IANA Protocol Numbers registry: https://www.iana.org/assignments/protocol-numbers/
- RFC 1340 — Assigned Numbers: https://www.rfc-editor.org/info/rfc1340/
- RFC 1700 — Assigned Numbers: https://www.rfc-editor.org/info/rfc1700/
- RFC 3232 — RFC 1700 is Replaced by an On-line Database: https://www.rfc-editor.org/info/rfc3232/

## Next excavation

- export every protocol number with first/last historical reference;
- classify living/deprecated/experimental/unknown entries;
- compare RFC 1340, RFC 1700 and current IANA row-by-row;
- trace Linux/BSD protocol dispatch tables and constants;
- identify protocol-number reuse across IPv4 and IPv6 extension headers;
- build an interactive "one-byte protocol graveyard" view.
