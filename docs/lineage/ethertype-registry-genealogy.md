# EtherType Registry Genealogy: 0x0800, 0x0806, 0x86DD, and a Link-Layer Fossil Record

EtherType is one of the most compact ways to see decades of networking history in two bytes.

An Ethernet frame can carry a type value telling the receiver what higher-layer payload follows. Many of those values have survived far longer than the original hardware and operating systems that first used them.

## 1. The famous survivors

The current IEEE/IANA historical EtherType table still identifies:

```text
0x0800  IPv4
0x0806  ARP
0x86DD  IPv6
```

These values are not symbolic names inside a user interface. They are bytes that packet parsers, NICs, switches, capture tools and operating systems still encounter directly.

A modern Ethernet capture therefore contains link-layer number assignments whose roots reach back decades.

## 2. EtherType and IEEE 802.3 length semantics

One historical wrinkle is that the same two-octet position is interpreted differently depending on value range.

The IANA IEEE 802 Numbers page records `0000-05DC` (0-1500 decimal) as the IEEE 802.3 Length Field range.

Values from the EtherType range identify protocols instead.

This is another case where **one field position contains multiple historical interpretation rules**.

## 3. Old Xerox values reveal a standards transition

The registry preserves an especially useful fossil:

- old Xerox Experimental PUP values such as `0x0200` are noted as invalid as EtherTypes since 1983;
- the table points to later values such as `0x0A00` for Xerox IEEE 802.3 PUP.

That means the registry does not merely list winners. It preserves traces of a transition from experimental Ethernet numbering into the later standardized type/length regime.

## 4. Nearby numbers tell a forgotten-network story

Around the familiar IPv4 and ARP assignments are historical systems such as:

- X.75 Internet;
- NBS Internet;
- ECMA Internet;
- Chaosnet;
- X.25 Level 3;
- XNS compatibility;
- Frame Relay ARP.

The numerical neighborhood around `0x0800` is therefore an archaeological layer from the era when multiple network architectures coexisted.

## 5. Later Ethernet keeps adding new protocol families

The same registry later includes values for:

- MPLS;
- PPPoE discovery/session;
- 802.1X;
- Service VLAN tags;
- LLDP;
- MACsec;
- Precision Time Protocol;
- other modern link-layer functions.

So EtherType is both a graveyard and an active growth registry.

## 6. A field can outlive every box that first implemented it

The Ethernet controller that first emitted IPv4 with type `0x0800` is obsolete.

The operating system code has been rewritten many times.

The physical medium moved from coax to twisted pair to fiber and beyond.

But the EtherType survives because interoperability depends on retaining the shared numeric identity.

This is a particularly pure form of protocol ancestry:

> hardware generations die; assigned numbers remain machine-readable.

## 7. IPv6 demonstrates continuity through a new network layer

IPv6 did not reuse `0x0800`. It received `0x86DD`.

Thus Ethernet can distinguish two generations of Internet network-layer protocol while keeping the same link-layer framing/typing concept.

The link-layer extension mechanism survives across a major network-layer redesign.

## 8. The registry is not wholly authoritative for modern IEEE assignment

The IANA IEEE 802 Numbers page explicitly warns that EtherTypes are not assigned by IANA and that the displayed list contains historically maintained information; modern allocations are coordinated with the IEEE Registration Authority.

That institutional detail matters for archival work:

```text
registry copy/history
        ≠
assignment authority
```

The provenance of the numbering table is part of the artifact.

## 9. Root-hunting classification

### Strongly living values

- IPv4 `0x0800`;
- ARP `0x0806`;
- IPv6 `0x86DD`;
- many modern control/encapsulation EtherTypes.

### Historical but assigned/documented

- old protocol families that no longer dominate production networks.

### Explicitly invalidated/transition fossils

- early Xerox Experimental values whose old interpretation became invalid in the standardized EtherType regime.

## Sources

- IANA IEEE 802 Numbers / historical EtherType table: https://www.iana.org/assignments/ieee-802-numbers/
- IEEE Registration Authority: https://standards.ieee.org/products-programs/regauth/
- RFC 9542 — IANA Considerations and IETF Protocol and Documentation Usage for IEEE 802 Parameters: https://www.rfc-editor.org/info/rfc9542/

## Next excavation

- build full EtherType assignment chronology by decade;
- isolate obsolete/deprecated protocol families;
- reconstruct DIX Type field → IEEE 802.3 type/length coexistence;
- track VLAN/MPLS/PPPoE/802.1X/MACsec EtherType branches;
- compare current Linux/BSD EtherType headers with historical Assigned Numbers tables;
- pair packet captures with the registry's historical neighbors.
