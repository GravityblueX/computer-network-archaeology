# UDP and ICMP: two small protocols that expose what IP deliberately does not do

## Why study them together

UDP and ICMP sit near IP, but they solve very different missing pieces.

- **UDP** gives applications ports and message delivery with very little transport machinery.
- **ICMP** lets hosts and gateways report control/error conditions about IP datagram processing.

Neither is simply a "smaller TCP" or an "IP error packet". Their histories make visible the deliberate narrowness of IP.

```text
                    applications
                   /            \
              TCP                   UDP
      reliable byte stream     minimal datagrams
                   \            /
                         IP
                          |
                         ICMP
                 control/error reports
```

The diagram is conceptual, not an OSI claim about every implementation.

---

## 1. UDP: minimum transport mechanism

RFC 768 (28 August 1980) says exactly what UDP is for: application programs should be able to send messages to other programs with a **minimum of protocol mechanism**, assuming IP underneath.

Primary source:

- RFC 768 — https://www.rfc-editor.org/rfc/rfc768.html

Its famous small header contains:

- source port;
- destination port;
- length;
- checksum.

The minimum length is eight octets.

Archaeologically, the key property is not merely "UDP is unreliable". It is that UDP deliberately does **not** add the connection state, sequencing, retransmission and flow control found in TCP.

That absence is architecture.

---

## 2. Port numbers move multiplexing above IP

IP identifies internet-layer endpoints. Applications still need a way to distinguish multiple receiving processes on one host.

UDP therefore exposes a process/application multiplexing boundary through ports.

```text
host IP address
      |
      +-- UDP port A -> application A
      +-- UDP port B -> application B
      +-- UDP port C -> application C
```

The RFC explicitly describes creating receive ports and returning source address/source port to the application.

This is one of the lineages to trace into sockets APIs later: **wire-level port semantics and programming-interface socket semantics are related, but not identical historical objects.**

---

## 3. UDP's early uses reveal its intended niche

RFC 768 names the Internet Name Server and TFTP as major uses.

That is historically revealing. Both can benefit from short request/response message exchange without establishing a heavy transport connection for every operation.

Future excavation should connect:

```text
UDP
 ├── early name service / DNS lineage
 ├── TFTP
 ├── boot/configuration protocols
 ├── SNMP
 ├── routing/control protocols
 └── later real-time/application uses
```

Do not imply these later protocols were all original design targets.

---

## 4. UDP checksum history requires precision

RFC 768 defines a checksum over a pseudo-header containing IP-layer addressing/protocol information plus UDP header/data.

This is important because it crosses an apparent layer boundary: transport integrity uses selected IP-header context.

Record separately:

- checksum algorithm;
- pseudo-header fields;
- IPv4 optional/zero-checksum practice;
- later IPv6 requirements;
- hardware checksum offload history.

Do not compress all of these into "UDP has a checksum".

---

# ICMP

## 5. IP needed a companion control channel

RFC 792 (September 1981) states that gateways and hosts need mechanisms to communicate control/error information in the interconnected network.

Primary source:

- RFC 792 — https://www.rfc-editor.org/rfc/rfc792.html

ICMP is carried using the basic IP header. It is therefore tightly coupled to IP but not simply "an application over IP" in the ordinary sense.

The historical architecture is better represented as:

```text
IP tries to forward/process datagram
        |
        +-- success -> ordinary traffic continues
        |
        +-- some control/error condition
                |
                -> ICMP message may be generated
```

---

## 6. Error reporting is constrained to avoid recursion

RFC 792 explicitly says ICMP messages are not sent about ICMP messages, preventing an infinite error-about-error regress.

It also constrains error generation for fragmented datagrams.

This shows that even "report an error" immediately creates second-order network-design questions:

- what if the error report itself fails?
- which fragment carries enough original header/context?
- how much of the triggering datagram should be quoted?
- who is expected to act on the report?

These rules later matter deeply to diagnostics, PMTU discovery, filtering and security.

---

## 7. ICMP contains several different roles

Do not reduce ICMP to `ping`.

The early ICMP family includes mechanisms such as:

- destination unreachable;
- source quench (later deprecated);
- redirect;
- echo / echo reply;
- time exceeded;
- parameter problem;
- timestamp-related functions.

These roles have different descendants and afterlives.

### Example: Echo

Echo request/reply later becomes the basis of the familiar `ping` diagnostic practice.

But the history of the **protocol message** and the history of the **user command/program `ping`** should be recorded separately.

### Example: Redirect

Redirect shows routers/gateways teaching hosts about a better next hop. That is a very different control function from reporting a dead destination.

### Example: Source Quench

Source Quench is an especially useful extinct mechanism: it demonstrates that early Internet congestion signaling ideas differed from later TCP congestion-control architecture.

Do not back-project Jacobson-style TCP congestion control into early ICMP.

---

## 8. ICMP reveals the historical meaning of "gateway"

RFC 792 uses *gateway* for devices connecting networks.

This is another reason the archive must preserve contemporary terminology rather than silently replacing every early *gateway* with *router*.

Link this excavation to:

- [`ggp-egp-bgp-routing-domains.md`](ggp-egp-bgp-routing-domains.md)
- [`../internetworking/bbn-gateway-to-router.md`](../internetworking/bbn-gateway-to-router.md)

---

## 9. UDP and ICMP are different kinds of IP companions

A tempting but misleading diagram is:

```text
TCP / UDP / ICMP = three peer transport protocols
```

That is historically and functionally too coarse.

Better:

```text
TCP, UDP
    -> offer application/process transport interfaces

ICMP
    -> communicates conditions about IP internetwork operation
```

All three may have IP protocol numbers, but protocol-number registration is not identical to architectural role.

---

## 10. What survived into modern systems

### UDP survives recognizably

The fundamental UDP service remains startlingly stable:

- datagram boundaries;
- ports;
- small fixed header;
- no connection establishment;
- no transport retransmission/ordering.

What changed around it:

- application protocols;
- socket APIs;
- checksumming requirements;
- hardware offload;
- NAT behavior;
- firewall/state tracking;
- QUIC and other sophisticated transports built in user space above UDP.

A future QUIC lineage must **not** be written as "UDP evolved into QUIC". UDP is a substrate/interface in that story.

### ICMP survives with heavy operational baggage

ICMP remains fundamental while also becoming filtered, rate-limited and security-sensitive.

Future archaeology should recover:

- router ICMP generation defaults;
- firewall filtering guidance by era;
- traceroute's dependence on TTL/time-exceeded behavior;
- Path MTU Discovery;
- ICMPv6 as a much larger neighbor/control substrate.

---

## 11. Implementation archaeology targets

### UDP

- RFC 768-era reference/host implementations;
- 4.2BSD UDP source and socket interface;
- checksum implementation and optimization;
- first DNS implementations using UDP/TCP fallback;
- TFTP code;
- hardware checksum offload.

### ICMP

- early gateway ICMP source;
- BSD `ping` and `traceroute` source histories;
- redirect processing in hosts;
- Source Quench generation/removal;
- router rate limiting;
- raw sockets and privileged diagnostic interfaces.

---

## 12. Lineage rules

Safe:

```text
IP's deliberately limited service
   -> motivates companion transport/control mechanisms

UDP 1980
   -> survives as minimal datagram transport

ICMP 1981
   -> survives as IP control/error family
```

Unsafe:

```text
UDP = unreliable TCP                     WRONG MODEL
ICMP = ping                              TOO NARROW
ICMP = transport protocol like TCP/UDP   TOO COARSE
UDP -> QUIC                              NOT A SIMPLE REVISION LINE
ICMP Source Quench -> TCP congestion control DIRECT DESCENT UNSUPPORTED
```

---

## 13. Sources

Primary:

- Jon Postel, RFC 768, *User Datagram Protocol*, 28 August 1980 — https://www.rfc-editor.org/rfc/rfc768.html
- Jon Postel, RFC 792, *Internet Control Message Protocol*, September 1981 — https://www.rfc-editor.org/rfc/rfc792.html

Related:

- RFC 760 / RFC 791 IP specifications;
- IEN 116 early Internet Name Server;
- IEN 133 / later TFTP documents;
- later ICMP update/deprecation RFCs to be recorded as separate revision branches.

---

## Open questions

1. Recover UDP and ICMP source implementations corresponding to RFC 760/761/768/792-era stacks.
2. Build a complete early ICMP type/code registry by RFC revision.
3. Trace Source Quench's deployment and deprecation from operational evidence.
4. Trace the first `ping` implementation independently from ICMP Echo specification.
5. Trace `traceroute` as an operational composition of TTL, UDP/ICMP behavior.
6. Build UDP checksum-rule diffs between IPv4 and IPv6.
7. Trace UDP socket API history separately from UDP wire history.

Small protocols are often the best archaeological windows. UDP and ICMP show, with unusual clarity, **what the Internet layer intentionally refused to do itself.**
