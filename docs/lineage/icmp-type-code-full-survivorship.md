# ICMP Type/Code Survivorship: A Protocol Whose Branches Have Different Life Expectancies

ICMP is often described as if it were one monolithic protocol. That is historically misleading.

The ICMP header contains a Type and Code. Over decades, individual Type/Code combinations have followed radically different paths: some are fundamental to modern operations, some survive only in specialized roles, and some are formally deprecated.

The right archaeological unit is therefore not always "ICMP." It is often one message branch.

## 1. 1981 roots that remain obvious

RFC 792 defined several message classes that are still immediately recognizable:

- Type 0 — Echo Reply;
- Type 3 — Destination Unreachable;
- Type 5 — Redirect;
- Type 8 — Echo;
- Type 11 — Time Exceeded;
- Type 12 — Parameter Problem;
- Type 13/14 — Timestamp / Timestamp Reply;
- Type 15/16 — Information Request / Reply;
- Type 4 — Source Quench.

The modern IANA ICMP registry still assigns the same Type numbers, while marking some historical branches deprecated.

## 2. Echo: extremely alive

Type 8 Echo and Type 0 Echo Reply are the protocol substrate under classic `ping`.

Their survival is unusually direct:

```text
RFC 792 Echo request/reply
       ↓
Unix ping
       ↓
router/server/firewall diagnostics today
```

Implementations may rate-limit or filter Echo, but the Type identities remain instantly recognizable.

## 3. Time Exceeded: old error, modern topology tool

Type 11 Time Exceeded was designed for conditions such as TTL expiration and fragment reassembly timeout.

The TTL-expired branch later became the observation mechanism exploited by traceroute-style tools.

This is a good example of a protocol message acquiring an important operational use that was not identical to its original purpose.

## 4. Destination Unreachable: a family, not one error

Type 3 contains codes that distinguish different failure causes. Over time the family also became central to mechanisms such as IPv4 Path MTU Discovery through the "fragmentation needed and DF set" condition.

A single 1981 Type therefore became a container for multiple generations of operational meaning.

## 5. Redirect: alive in standards, constrained in operations

ICMP Redirect tells a host that a better next hop exists.

It represents an older trust model in which hosts could learn local routing improvements from routers through ICMP control messages.

Modern security practice is often more conservative. Hosts, routers and administrators may restrict redirects because accepting routing changes from the network creates attack surface.

So Redirect belongs in a special category:

```text
not extinct
not universally trusted
still protocol-visible
operationally policy-dependent
```

## 6. Source Quench: a formal fossil

Type 4 Source Quench is the cleanest extinct branch.

It originated as a congestion indication. Later congestion-control experience moved the Internet away from router-generated Source Quench. RFC 6633 formally deprecated it, and the IANA registry marks Type 4 deprecated.

The type number remains in the registry as a historical marker.

This is a powerful archaeological pattern:

> registries remember mechanisms after implementations stop using them.

## 7. Information Request/Reply and Alternate Host Address

Other early branches similarly survive as assigned/deprecated names without being part of ordinary modern operation.

The IANA registry currently marks Information Request/Reply and Alternate Host Address as deprecated.

Thus a registry is not merely a list of valid modern features. It is also a record of abandoned protocol ideas.

## 8. Router discovery adds later branches

ICMP did not stop evolving after RFC 792. Router Advertisement and Router Solicitation were standardized later.

That means the ICMP Type space is both:

- a graveyard of early experiments;
- a living extension registry.

## 9. A survivorship table

| Branch | Current archaeological state | Modern visibility |
|---|---|---|
| Echo / Echo Reply | strongly living | ping, health checks, diagnostics |
| Destination Unreachable | strongly living | errors, PMTUD-related behavior |
| Time Exceeded | strongly living | traceroute, TTL failures |
| Parameter Problem | living/specialized | malformed header reporting |
| Redirect | living but constrained | local-route optimization/security-sensitive |
| Router Advertisement/Solicitation | specialized living | IPv4 router discovery environments |
| Timestamp | rare / legacy | unusual diagnostics |
| Source Quench | deprecated | historical only |
| Information Request/Reply | deprecated | historical only |
| Alternate Host Address | deprecated | historical only |

## 10. Why ICMPv6 matters to the genealogy

ICMPv6 is not simply "ICMP with bigger addresses." IPv6 moves additional network-control responsibilities into ICMPv6, including Neighbor Discovery and Packet Too Big.

That later branch demonstrates how a control-message framework can expand rather than merely preserve old message numbers.

Do not flatten ICMPv4 and ICMPv6 into one direct revision chain.

## 11. The root-hunting lesson

A modern `ping` packet and a deprecated Source Quench packet both belong to ICMP, but their historical states are completely different.

Therefore:

> protocol survivorship should often be recorded at Type/Code granularity.

## Sources

- RFC 792 — Internet Control Message Protocol: https://www.rfc-editor.org/rfc/rfc792.html
- IANA ICMP Parameters registry: https://www.iana.org/assignments/icmp-parameters/
- RFC 6633 — Deprecation of ICMP Source Quench: https://www.rfc-editor.org/info/rfc6633/
- RFC 1256 — ICMP Router Discovery Messages: https://www.rfc-editor.org/info/rfc1256/

## Next excavation

- code-by-code history of Type 3 Destination Unreachable;
- Redirect acceptance behavior in BSD/Linux/Windows;
- Source Quench removal from kernels/router software;
- Timestamp/Information message implementation archaeology;
- ICMP extensions and quoted packet formats;
- ICMPv4 → ICMPv6 responsibility comparison;
- build packet captures for living and synthetic historical messages.
