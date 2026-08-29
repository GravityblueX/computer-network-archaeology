# ARP, IPv6 ND/NUD, the Linux neighbour subsystem, and `ip neigh`

## Do not call IPv6 Neighbor Discovery “ARPv6”

ARP resolves protocol addresses to link-layer addresses in the IPv4/Ethernet world. IPv6 Neighbor Discovery (RFC 4861) does address resolution too, but it also covers router discovery, prefix/on-link information, redirects and Neighbor Unreachability Detection (NUD).

So this is a required negative-lineage rule:

```text
ARP  ──X──>  “ARPv6”
```

The two families solve an overlapping local-neighbour problem but are not formal revisions of one another.

## Linux creates a common implementation object

Linux nevertheless has good engineering reasons to represent both families through a generic neighbour-cache abstraction.

Conceptually:

```text
IPv4 ARP state ───────┐
                      ├──> Linux neighbour object/cache
IPv6 ND + NUD state ──┘
                                ↓
                           rtnetlink
                                ↓
                           ip neigh
```

The operating system unifies **implementation and administration**, not the wire protocols.

## NUD state-machine roots

RFC 4861 defines Neighbor Cache states including:

- `INCOMPLETE` — address resolution in progress;
- `REACHABLE` — recent positive reachability confirmation;
- `STALE` — cached information exists but reachability has aged;
- `DELAY` — traffic resumed and probing is deferred briefly;
- `PROBE` — unicast Neighbor Solicitations actively test reachability.

Linux additionally exposes states such as failed/noarp/permanent for its generalized neighbour implementation. Therefore an `ip neigh` state name may be partly a direct RFC 4861 conceptual descendant and partly a Linux neighbour-core extension.

## Upper layers participate in NUD

One subtle RFC 4861 detail matters enormously: NUD can use upper-layer evidence of forward progress, such as acknowledgements, before actively probing with Neighbor Solicitation. That is why DELAY exists — a new TCP handshake may quickly provide reachability confirmation without extra ND traffic.

This makes neighbour reachability a cross-layer mechanism even though its messages are ICMPv6.

## `ip neigh` as a convergence point

`ip-neighbour(8)` explicitly notes that for IPv4 the neighbour table is also known as the ARP table. The same operator command can show/manage IPv6 neighbours.

This is a perfect example of root-hunting by implementation object:

> one modern command exposes multiple older protocol families through a common kernel abstraction.

Primary anchors:

- RFC 4861: https://www.rfc-editor.org/info/rfc4861/
- `ip-neighbour(8)`: https://man7.org/linux/man-pages/man8/ip-neighbour.8.html
- Linux neighbour netlink specification: https://docs.kernel.org/next/networking/netlink_spec/rt_neigh.html
