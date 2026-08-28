# OUI, EUI-48, and MAC Address Block Genealogy: Vendor Identity in 48 Bits

A MAC address often looks like a meaningless hexadecimal string. Historically it contains several layers of allocation policy, IEEE registration practice, and local/global identity semantics.

The first bytes of a universally administered MAC address can be traced into IEEE-assigned address blocks whose lineage includes the classic OUI and newer MA-L, MA-M, and MA-S products.

## 1. EUI-48 is more than a random 48-bit number

A 48-bit MAC address is commonly represented as six octets.

For globally administered addresses, a prefix is allocated through IEEE Registration Authority mechanisms and the assignee allocates the remaining bits to individual interfaces/devices according to the rules of its assignment block.

This creates a two-level identity structure:

```text
IEEE-assigned block/prefix
       ↓
organization-controlled suffix space
       ↓
individual EUI-48 / MAC addresses
```

## 2. The classic OUI became one member of a family

IEEE's Registration Authority FAQ now describes three address-block sizes:

```text
MA-L   2^24 addresses   formerly called OUI
MA-M   2^20 addresses
MA-S   2^12 addresses   related to the OUI-36/IAB lineage
```

This is a good reminder that "OUI" is often used colloquially for any vendor prefix, while the actual registration products have evolved.

The archive should preserve period-correct terminology.

## 3. MA-L/OUI: 24-bit organization identity plus 24-bit extension

The classic OUI/MA-L model gives the assignee a 24-bit identifier and enough remaining address bits for roughly 16 million EUI-48 addresses.

That model fit large manufacturers, but it is wasteful for smaller organizations.

The later MA-M and MA-S products reflect pressure to use the finite global MAC namespace more efficiently.

So the registration products themselves encode a history of scaling and conservation.

## 4. Universal versus local administration is a separate axis

Not every MAC address needs to come from a globally registered vendor block.

IEEE 802 addressing has a Universal/Local (U/L) distinction. Locally administered addresses can be generated and managed within an administrative domain rather than globally allocated by IEEE.

This produces two different identity models inside the same 48-bit field:

```text
globally administered
   → external allocation/uniqueness process

locally administered
   → local policy/generation process
```

Modern virtualization, privacy features, containers and software-defined networking make the local branch increasingly visible.

## 5. Individual/group semantics occupy another bit

The low-order bit of the first octet distinguishes individual/unicast from group/multicast addressing in the IEEE MAC address architecture.

That means the first octet simultaneously carries allocation semantics and destination-group semantics.

A modern MAC address is therefore not just six bytes of identity. Parts of those bytes are protocol flags with historical meaning.

## 6. IANA itself has an IEEE OUI

RFC 9542 documents that IANA has an OUI allocated by the IEEE Registration Authority and manages subordinate identifiers and MAC blocks under that OUI for IETF standards purposes.

This creates a neat institutional nesting:

```text
IEEE RA
  ↓ allocates OUI
IANA
  ↓ sub-allocates protocol/documentation identifiers under its OUI
IETF protocols / documentation uses
```

The global registry systems are themselves clients of other registry systems.

## 7. Vendor-prefix databases are historical sources, but require care

A MAC/OUI lookup is often treated as a simple question: "Who made this NIC?"

Historically that can be misleading because:

- companies merge or change names;
- blocks can be used across many product lines;
- virtual interfaces may use local addresses;
- addresses can be cloned/spoofed;
- an OUI identifies an assignee, not necessarily the final hardware manufacturer;
- address blocks may appear in embedded modules integrated into another vendor's product.

An OUI registry is therefore evidence of **allocation**, not proof of physical provenance.

## 8. The number can outlive the company

Even if an assignee disappears, devices bearing addresses from its block can remain in service for years.

Packet captures, switch CAM tables and archived configuration files can therefore contain organization identifiers belonging to companies that no longer exist.

This turns OUI data into corporate/industrial archaeology as well as networking archaeology.

## 9. MAC addresses moved across physical generations

The same EUI-48 style identity survives across:

- coax Ethernet;
- twisted-pair Ethernet;
- Wi-Fi;
- virtual Ethernet interfaces;
- bridges and switches;
- tunnels/overlays that carry Ethernet frames;
- software-generated interfaces.

The physical medium changed radically while the link-layer address abstraction remained recognizable.

## 10. Local address generation is a modern branch worth tracing

Virtualization and privacy mechanisms increasingly generate local MAC addresses rather than using factory-assigned global identities.

This creates a modern tension:

```text
old intuition:
MAC address ≈ burned-in vendor/device identity

modern reality:
MAC address may be mutable, randomized, virtual, locally administered, container-created
```

The field survives while the assumption that it identifies physical hardware becomes weaker.

## 11. A switch table is an archaeological dataset

A saved CAM/FDB table can reveal:

- addresses from long-dead vendors;
- virtual/local addresses;
- multicast groups;
- devices spanning different Ethernet generations.

Combined with historical IEEE assignment data, a simple switch dump becomes a source for network archaeology.

## Sources

- IEEE Registration Authority FAQ — MA-L/MA-M/MA-S and OUI/EUI address blocks: https://standards.ieee.org/faqs/regauth/
- IEEE Registration Authority: https://standards.ieee.org/products-programs/regauth/
- RFC 9542 — IANA Considerations and IETF Protocol and Documentation Usage for IEEE 802 Parameters: https://www.rfc-editor.org/info/rfc9542/

## Next excavation

- recover historical OUI lists by decade and diff company names/assignments;
- trace OUI → MA-L terminology and IAB/OUI-36 → MA-S;
- exact U/L and I/G bit history in Ethernet/IEEE standards;
- MAC randomization in Wi-Fi/mobile systems;
- virtualization/container MAC-generation algorithms;
- museum/device MAC-prefix provenance case studies;
- connect vendor OUI history to NIC/chipset catalogs in `catalogs/hardware.md`.
