# IPv4 Special-Purpose Address Space Genealogy: Private, Documentation, Shared, Loopback, Link-Local, and the Meaning of "Not Global"

IPv4 addresses look uniform: four octets, 32 bits. But not every address participates in the same global routing and assignment system.

Over decades, standards carved pieces of the IPv4 space into special-purpose blocks with different semantics. Some are private enterprise space, some documentation-only, some provider shared space, some loopback, some link-local, and others exist for protocol mechanisms.

The special-purpose registry is therefore an address-space archaeology map.

## 1. A special-purpose block is not simply "reserved"

The phrase "reserved address" hides important differences.

A block may be reserved for:

- private/internal networks;
- documentation examples;
- loopback;
- link-local communication;
- carrier-grade NAT shared addressing;
- benchmarking;
- protocol translation;
- multicast-related or other infrastructure functions.

Each reservation has different forwarding, source, destination and global-reachability rules.

## 2. RFC 1918: private address space

RFC 1918 reserves three blocks for private internets:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

The motivation explicitly includes address-space pressure and routing-table growth, but the standard does **not** itself define NAT.

Private addressing and NAT became operationally intertwined later, yet they are distinct genealogies.

This distinction belongs permanently in the archive:

```text
RFC1918 private addressing
    ≠
NAT mechanism
```

## 3. Private addresses are intentionally non-global identities

RFC 1918 lets many independent organizations reuse the same addresses internally.

Thus `192.168.1.1` does not have one global owner.

Its meaning is scoped by network context.

This is the opposite of globally unique Internet addressing:

```text
global address
  identity relies on global uniqueness/routing allocation

private address
  identity is meaningful only inside an administrative context
```

## 4. Documentation blocks solve a different problem

RFC 5737 defines:

```text
192.0.2.0/24      TEST-NET-1
198.51.100.0/24   TEST-NET-2
203.0.113.0/24    TEST-NET-3
```

These blocks are not private-enterprise address pools.

They are reserved specifically so examples in RFCs, books and documentation do not accidentally use addresses belonging to real networks.

This is a major standards lesson:

> examples are operational artifacts too; bad example values can escape into production.

Documentation address space is therefore a form of safety engineering.

## 5. RFC 5737 preserves the history of a bad example range

RFC 5737 explicitly notes that `128.66.0.0/16` appeared in historical examples but was **not actually reserved** for documentation.

This is a perfect archaeological warning.

A number can acquire folklore meaning without having formal allocation status.

The archive must distinguish:

```text
historically used in examples
        ≠
formally reserved for documentation
```

## 6. Shared Address Space: 100.64.0.0/10

RFC 6598 allocates:

```text
100.64.0.0/10
```

as **Shared Address Space** for service-provider networks using Carrier-Grade NAT.

The RFC is explicit that this is distinct from RFC 1918 private space.

It is intended for interfaces between CGN infrastructure and customer-premises equipment, subject to specific routing/filtering constraints.

This gives us three different reusable/non-global address concepts:

```text
RFC1918
  enterprise/private scope

RFC5737
  documentation-only examples

RFC6598
  provider shared CGN infrastructure
```

They must never be flattened into "private IP ranges."

## 7. CGN made another shared identity layer necessary

Why not simply use RFC 1918 inside service-provider CGN networks?

RFC 6598 documents operational conflicts when customer networks and provider networks both use overlapping RFC1918 space.

The solution was another specially scoped address block.

This is a beautiful example of layers of reuse colliding:

```text
customer private address reuse
        +
provider private address reuse
        ↓ overlap problem
new Shared Address Space
```

Address-space policy evolves in response to the consequences of earlier address-space policy.

## 8. Loopback: an address that means the local host, not a network location

The `127.0.0.0/8` lineage represents another fundamentally different semantic category.

Loopback addresses refer back to the local system/network stack. They are not merely "unroutable private addresses."

A packet to loopback has a special local processing meaning.

This shows why special-purpose registries need per-block behavioral properties, not just a list of prefixes.

## 9. Link-local: identity bounded by one link

The IPv4 link-local block `169.254.0.0/16` is another distinct branch, associated with automatic local address configuration when conventional configuration is unavailable.

Its scope is link-local, not enterprise-private and not globally routable.

Again:

```text
private
shared
loopback
link-local
documentation
```

are five different things.

## 10. Special-purpose registries formalize properties

IANA maintains an IPv4 Special-Purpose Address Space registry under the Internet Numbers Registry System.

Modern registry entries can record properties such as whether an address block is valid as source/destination, forwardable, globally reachable, or reserved by protocol.

This is much richer than the old intuition of one flat "reserved" list.

## 11. IPv4 scarcity created multiple semantic overlays on one 32-bit space

As the Internet grew, the 32-bit address space had to serve more roles:

- global unicast identity;
- internal private identity;
- local-stack identity;
- local-link identity;
- documentation identity;
- service-provider shared identity;
- protocol-specific infrastructure.

The field did not grow wider.

Instead governance carved the existing space into semantic regions.

## 12. A modern home network is a historical composite

A home user might encounter:

```text
192.168.1.10       RFC1918 private host
192.168.1.1        private default gateway
100.64.x.x         possible ISP/CGN shared address upstream
127.0.0.1          loopback
169.254.x.x        link-local fallback
203.0.113.10       safe documentation example
```

All look like IPv4 addresses.

They belong to completely different standards lineages.

## 13. Special addresses survive into code and policy

Operating systems, routers, firewalls, libraries, address classifiers and cloud platforms contain tables or logic recognizing these blocks.

The standards therefore become code-level behavior:

```text
prefix reservation
   ↓
kernel/router classification
   ↓
forwarding/filtering/application policy
```

A standards reservation becomes an implementation branch.

## Sources

- IANA Number-related Registries: https://www.iana.org/numbers/registries
- RFC 6890 — Special-Purpose IP Address Registries: https://www.rfc-editor.org/info/rfc6890/
- RFC 1918 — Address Allocation for Private Internets: https://www.rfc-editor.org/info/rfc1918/
- RFC 5737 — IPv4 Address Blocks Reserved for Documentation: https://www.rfc-editor.org/info/rfc5737/
- RFC 6598 — IANA-Reserved IPv4 Prefix for Shared Address Space: https://www.rfc-editor.org/info/rfc6598/

## Next excavation

- complete IPv4 special-purpose registry with behavioral flags and dates;
- loopback specification genealogy;
- IPv4 link-local/RFC3927 implementation history;
- benchmarking/documentation/multicast-related special blocks;
- RFC1918 predecessor RFC1597 and Network 10 controversy;
- address-space filtering in routers/Linux/BSD/clouds;
- IPv6 special-purpose registry comparison;
- real CGN traces showing public/private/shared-address layers together.
