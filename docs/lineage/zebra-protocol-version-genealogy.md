# Zebra Protocol / ZAPI version genealogy: v0 → v6

FRRouting's developer documentation preserves an unusually clean internal-protocol archaeology. ZAPI is the streaming protocol used by routing-protocol daemons to communicate with the central `zebra` routing manager.

This is not the BGP/OSPF wire protocol. It is the **inside-the-routing-suite control protocol**.

## Version matrix

| ZAPI version | Historical generation | Header/semantic change |
|---|---|---|
| v0 | all GNU Zebra; Quagga through 0.98 | no explicit version field; header is length + 8-bit command |
| v1 | Quagga 0.99.3–0.99.20 | adds marker + version; command expands to 16 bits |
| v2 | Quagga 0.99.21–0.99.23 | distinct Quagga revision; requires source-level diff to enumerate all message changes |
| v3 | Quagga 0.99.23 until FRR fork | adds 16-bit `vrf_id` |
| v4 | FRR 2.0–3.0.3 | marker changes from Quagga 255 to FRR 254 to prevent daemon mixing |
| v5 | FRR 4.0–5.0.1 | VRF identifier expands from 16 to 32 bits |
| v6 | FRR 6.0+ | removes separate IPv4/IPv6 route-add/delete commands in favor of newer command model |

## v0 is identifiable precisely because it has no version field

FRR documents an elegant compatibility trick. For versioned headers, byte 3 is a marker (255 in Quagga, 254 in FRR); in v0 the same byte position belongs to the command field. Reserved marker values let a parser distinguish an implicit v0 header from later explicitly versioned headers.

That is a small but extremely archaeological design: the descendant protocol had to reserve meaning in a location whose ancestor had used a different field.

## The fork boundary became a byte on the wire

The Quagga→FRR project fork is not only a repository/governance event. ZAPI v4 changes the marker from 255 to 254 specifically to stop people from mixing incompatible Quagga and FRR daemon binaries.

Thus:

```text
project fork
   ↓
compatibility risk
   ↓
wire marker deliberately changed
```

A social/software fork becomes observable in an internal protocol byte.

## VRF growth leaves two separate strata

v3 introduces a 16-bit VRF ID. v5 later makes it 32 bits. That is a concrete example of an internal protocol reacting to routing-system scale/feature growth while retaining the larger ZAPI architecture.

## v6 removes address-family-specific route commands

FRR documents v6 as removing separate IPv4/IPv6 add/delete command names. This is not merely a header revision; it records an internal API cleanup toward a less duplicated route-message model.

## Relationship to the existing project fork lineage

The repository already records:

```text
GNU Zebra → Quagga → FRRouting
```

as a real fork/successor lineage. This document drills underneath that project history and asks what happened to the protocol spoken between their daemons.

## Next source-level diff work

The official version history gives the revision skeleton. A later excavation should diff historical `zclient.h`/message encode-decode code at each transition, especially v1→v2, where the summary history does not enumerate every changed message.

Primary anchor:

- FRRouting Developer Guide, Zebra protocol: https://docs.frrouting.org/projects/dev-guide/en/latest/zebra.html
