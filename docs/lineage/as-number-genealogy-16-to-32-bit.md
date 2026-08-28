# Autonomous System Number Genealogy: From 16-Bit Policy IDs to Four-Octet BGP

Autonomous System Numbers are not merely labels attached to organizations. They are protocol-visible routing-policy identities carried inside BGP and allocated through a global registry system.

Their history is a compact example of a namespace that outgrew its original field width without abandoning the protocol architecture built around it.

## 1. ASes are routing-policy identities

RFC 1930 describes Autonomous Systems as units of routing policy for exterior routing.

That formulation matters: an ASN is not simply "an ISP number." The number identifies a routing domain whose policy is visible to interdomain routing protocols.

BGP carries AS numbers in places such as:

- the OPEN message;
- AS_PATH;
- AGGREGATOR-related information;
- communities/management and operational tooling around routing.

## 2. The original BGP world encoded ASNs in two octets

The base BGP-4 specification encoded an AS number as a two-octet value.

That creates a finite namespace:

```text
0 .. 65535
```

As interdomain routing expanded, exhaustion became an architectural concern rather than merely a registry inconvenience.

## 3. RFC 6793 expands the namespace to four octets

RFC 6793 defines support for four-octet AS numbers and explicitly states that the pool expands to:

```text
0 .. 4294967295
```

The remarkable part is how this was done.

BGP was not replaced.

Instead the protocol gained compatibility machinery:

- a capability indicating four-octet ASN support;
- AS4_PATH;
- AS4_AGGREGATOR;
- special handling for peers that only understand two-octet ASNs.

This is classic compatibility-layer archaeology.

## 4. AS_TRANS is a transitional fossil

RFC 6793 defines the special AS number **AS_TRANS** so a four-octet-aware speaker can communicate through old BGP speakers that cannot represent a non-mappable four-octet ASN in the legacy two-octet field.

The transition therefore looks like:

```text
new 32-bit ASN
   ↓
old speaker cannot represent it
   ↓
AS_TRANS in legacy field
AS4_PATH / AS4_AGGREGATOR preserve real information
```

This is not a clean flag-day upgrade. The protocol carries evidence of coexistence between old and new implementations.

## 5. Old ASNs map naturally into the new space

RFC 6793 specifies that existing two-octet ASNs map into four-octet form by setting the upper two octets to zero.

That preserves numeric identity:

```text
AS 64500 (16-bit)
   ↓
AS 64500 (32-bit representation)
```

No mass renumbering of old ASNs was required merely because the field width expanded.

## 6. Text notation became a human interoperability problem

Once ASNs exceeded 65535, humans and configuration systems needed a consistent textual representation.

Different notations appeared, including dotted forms.

RFC 5396 recommends a single decimal integer representation — **asplain** — for documents, systems, interfaces and registries.

This creates another distinction:

```text
wire width
   ≠
human notation
```

A namespace can be technically extended and then require a separate standard just to stop humans from writing the same number in incompatible ways.

## 7. Private-use ASNs preserve the old range and add a new one

RFC 6996 documents two private-use ranges:

```text
64512–65534
4200000000–4294967294
```

The first belongs to the old 16-bit ASN space.

The second exploits the expanded four-octet space.

Private ASNs are intentionally not globally unique and should not leak as ordinary public routing identities.

This is parallel to RFC1918 only in a broad conceptual sense; ASNs and IP addresses have different protocol roles and policies.

## 8. Documentation ASNs solve a different problem

RFC 5398 reserves two 16-number blocks for examples:

```text
64496–64511
65536–65551
```

The second range was deliberately chosen so documentation could demonstrate 32-bit ASN behavior.

This is an excellent example of standards learning from earlier mistakes: using real public identifiers in examples can leak into production configurations.

Documentation identifiers reduce that risk.

## 9. Special-purpose ranges are part of the live registry

IANA maintains both ordinary AS allocation registries and a **Special-Purpose AS Numbers** registry.

The registry therefore contains multiple identity classes:

```text
globally allocatable ASNs
private-use ASNs
documentation ASNs
reserved/special ASNs
```

The bare integer is insufficient without registry context.

## 10. ASNs connect protocol architecture to Internet governance

IANA allocates ASN blocks primarily to the Regional Internet Registries.

The RIRs then allocate/assign according to regional policy.

Thus a BGP AS_PATH is ultimately tied to a layered institutional system:

```text
IANA global pool
      ↓
RIR allocation
      ↓
network/operator assignment
      ↓
BGP configuration
      ↓
AS_PATH on the wire
```

A routing field is connected to governance and registry infrastructure.

## 11. One modern BGP UPDATE can contain decades of ASN history

A current route can expose:

- the AS_PATH architecture descended from early BGP;
- 32-bit ASNs added later;
- compatibility history around AS4_PATH;
- private/special identifiers if configuration is wrong or intentionally internal;
- modern policy communities layered on top.

The AS number is therefore not just an organization label.

It is a long-lived protocol identity whose width, notation and allocation policy all have separate genealogies.

## Sources

- RFC 1930 — Guidelines for creation, selection, and registration of an Autonomous System: https://www.rfc-editor.org/info/rfc1930/
- RFC 6793 — BGP Support for Four-Octet Autonomous System Number Space: https://www.rfc-editor.org/info/rfc6793/
- RFC 5396 — Textual Representation of Autonomous System Numbers: https://www.rfc-editor.org/info/rfc5396/
- RFC 5398 — ASN Reservation for Documentation Use: https://www.rfc-editor.org/info/rfc5398/
- RFC 6996 — ASN Reservation for Private Use: https://www.rfc-editor.org/info/rfc6996/
- IANA Number Resources / AS registries: https://www.iana.org/numbers/registries

## Next excavation

- reconstruct the earliest AS allocation tables and RFC 827/EGP-era AS identifiers;
- trace the first live 32-bit ASN allocations and BGP deployments;
- AS_TRANS incident archaeology;
- ASDOT/asplain configuration history in Cisco/Juniper/BIRD/FRR;
- RIR ASN allocation policy chronology;
- special-purpose ASN leak incidents;
- compare modern BGP dumps against historical 16-bit-only assumptions.
