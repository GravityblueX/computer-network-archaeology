# IPv4 Options Cemetery: Source Routing, Timestamps, Security, Router Alert, and Why Options Became Exceptional

IPv4 options are one of the clearest places where the Internet contains both living standards and a graveyard in the same header.

The base IPv4 header reserves a variable-length options area. In 1981 this looked like a general extension point. Decades later, the extension point still exists, but many individual options are deprecated, filtered, slow-pathed, or operationally rare.

## 1. The container survived

RFC 791 defines IHL and an optional options area. That means IPv4 did not freeze at a single fixed 20-byte header. Options could be copied into fragments or omitted depending on the option's copy bit.

The important archaeological distinction is:

- **the options mechanism survives structurally**;
- **the population of useful options changed dramatically**.

## 2. Early option families

Historically important option families include:

- End of Option List / No Operation;
- Record Route;
- Loose Source and Record Route;
- Strict Source and Record Route;
- Internet Timestamp;
- Security-related options;
- Stream Identifier;
- later Router Alert.

These are not one coherent generation. They accumulated from different design needs.

## 3. Source routing: powerful idea, hostile operational afterlife

Source routing allowed the sender to influence or specify the route taken by a datagram. Conceptually this exposes an older Internet in which packet forwarding policy could be expressed directly in an IP header option.

Later security and operational practice became deeply suspicious of source routing. Firewalls and routers frequently filter such options because they complicate policy enforcement and can bypass assumptions about path selection.

The lesson is not simply "source routing was bad." It is that **the trust model around who may influence the path changed**.

## 4. Record Route and Timestamp: observability inside the packet

Record Route and Internet Timestamp attempted to collect path information as the packet moved.

This is a remarkable contrast with modern practice:

```text
old idea:
packet carries a writable path-observation area

modern operational norm:
network measurement is usually performed by external tools,
telemetry protocols, or repeated probe exchanges
```

The IPv4 option space was once expected to host observability directly in the packet. In modern high-speed networks, per-packet option processing is often operationally expensive or restricted.

RFC 7126 recommends filtering behavior for many optioned packets and documents the practical problems around them.

## 5. Stream Identifier: a fossil with formal burial

The Stream Identifier option is particularly useful as a cemetery marker. RFC 7126 notes that it was specified in RFC 791, deprecated by host/router requirements documents, and formally obsoleted by RFC 6814.

This is a case where:

```text
header extension point survives
specific option type survives as historical number/documentation
operational semantics are dead
```

## 6. Router Alert: later life inside the same ancient extension mechanism

IPv4 options were not only an early-Internet feature. RFC 2113 in 1997 defined Router Alert, asking participating routers to examine selected packets more closely.

The option was intended for protocols such as RSVP and IGMP that needed transit-router attention without forcing all ordinary traffic onto slow processing paths.

Router Alert shows that the IPv4 options mechanism continued to receive new uses long after RFC 791.

But it also exposes the operational problem: packets with unusual options may leave fast forwarding paths, consume control-plane CPU, or trigger filtering. RFC 7126 consequently recommends restrictive operational handling outside controlled environments.

## 7. Why the extension point became awkward

Several forces pushed IPv4 options toward exceptional status:

1. variable header length complicates fast-path parsing;
2. some options require transit-router mutation or special processing;
3. security policy is harder when senders can influence route or router behavior;
4. middleboxes often treat unusual options conservatively;
5. widespread deployment of a new option requires many independent implementations to handle it correctly.

This is an important root-hunting pattern:

> an extension mechanism can survive in the standard while becoming socially and operationally disfavored.

## 8. DF and Path MTU Discovery: a base-header bit becomes a discovery mechanism

The Don't Fragment bit was already part of the original fragmentation machinery. RFC 1191 later turned it into part of a Path MTU Discovery algorithm:

```text
sender sets DF
   ↓
router cannot forward without fragmentation
   ↓
router drops packet
   ↓
ICMP Destination Unreachable / fragmentation needed
   ↓
sender lowers estimated PMTU
```

This is a strong example of **new operational machinery growing out of an old bit plus an old ICMP error mechanism**.

The bit did not need to be redesigned. Its surrounding algorithm changed.

## 9. Living / constrained / extinct classification

A useful archaeological classification is:

### Structural survivor

- IPv4 options area itself.

### Living but specialized

- Router Alert in controlled/protocol-specific settings.

### Standardized but operationally constrained

- source-routing and route-recording-related options.

### Historical / effectively extinct

- Stream Identifier and other obsoleted branches.

## 10. Why this matters today

A packet parser still has to understand IHL. A firewall still needs a policy for optioned packets. A router may still encounter Router Alert. PMTUD still descends from DF + ICMP behavior.

So the options field is not simply dead space.

It is a **cemetery with a few living houses inside it**.

## Sources

- RFC 791 — Internet Protocol: https://www.rfc-editor.org/rfc/rfc791.html
- RFC 1191 — Path MTU Discovery: https://www.rfc-editor.org/info/rfc1191/
- RFC 2113 — IP Router Alert Option: https://www.rfc-editor.org/info/rfc2113/
- RFC 7126 — Recommendations on Filtering of IPv4 Packets Containing IPv4 Options: https://www.rfc-editor.org/info/rfc7126/

## Next excavation

- enumerate every assigned IPv4 option number and current status;
- recover historical option implementations in BSD/router source;
- compare fast-path and slow-path behavior in vendor routers;
- trace IPv4 Router Alert into RSVP/IGMP/MPLS-adjacent practice;
- connect classic PMTUD to Packetization Layer PMTUD and IPv6 Packet Too Big;
- capture modern packets with unusual options and record which middleboxes drop them.
