# ICMP Type/Code Survivorship — A Control Protocol Full of Living and Dead Branches

ICMP is another unusually visible technical fossil. RFC 792 (1981) still defines the core ICMPv4 framework, but the fate of individual message types is uneven: some remain operationally central, some survive mainly for compatibility, and some are obsolete or discouraged.

## 1. ICMP is not “ping protocol”

ICMP is an Internet-layer control/error-reporting protocol carried inside IP.

`ping` uses ICMP Echo Request/Reply, but ICMP also covers destination errors, TTL expiration, redirects and other control conditions.

Root-hunting must preserve:

```text
ICMP protocol
    ≠
ping utility
```

## 2. 1981 core message families

RFC 792 defined, among others:

- Destination Unreachable;
- Source Quench;
- Redirect;
- Echo Request / Echo Reply;
- Time Exceeded;
- Parameter Problem;
- Timestamp Request / Reply;
- Information Request / Reply.

Their afterlives differ dramatically.

## 3. Echo Request / Reply — highly visible living fossil

The basic Echo mechanism remains recognizable:

```text
Echo Request
   ↓
Echo Reply
```

Mike Muuss's Unix `ping` turned that protocol primitive into an operator-facing reachability/latency tool in 1983.

The important lineage is therefore:

```text
ICMP Echo messages
      ↓ operational reuse
ping program
```

not “ICMP became ping.”

## 4. Time Exceeded — a routing safety mechanism that became a diagnostic primitive

ICMP Time Exceeded reports expiry of IPv4 TTL.

Van Jacobson's traceroute exploited a sequence of increasing TTL values so that intermediate routers reveal themselves through Time Exceeded responses.

Thus a packet-lifetime safety rule became an observability interface:

```text
TTL decrement
    +
ICMP Time Exceeded
    ↓
traceroute
```

This is a classic operational fossil: the underlying protocol was not designed merely as a user-facing path-visualization API, yet operators built one from its observable behavior.

## 5. Destination Unreachable — still important, but codes have unequal value

Destination Unreachable includes multiple codes for conditions such as network/host/protocol/port reachability and fragmentation restrictions.

One particularly important descendant role is:

```text
Fragmentation Needed + DF Set
       ↓
Path MTU Discovery mechanisms
```

The exact modern requirements require later RFCs, but the 1981 error family remains visible inside later network behavior.

## 6. Redirect — alive in standards history, often restricted operationally

ICMP Redirect allows a gateway/router to tell a host about a better first-hop route.

The message type survived long enough to become part of host/router requirements, but operational/security practice often disables or filters redirects in environments where accepting route advice from the network edge is undesirable.

Root-hunting classification:

```text
wire mechanism: survives
concept: survives
trust model: heavily constrained by later operations/security practice
```

## 7. Source Quench — a genuine extinct branch

Source Quench attempted to signal congestion by asking a sender to slow down.

Later Internet congestion-control development did not continue along this path. TCP congestion control moved toward end-to-end inference and sender algorithms such as the Jacobson/Karels work.

Source Quench therefore belongs in the archive as **extinct-but-explanatory**:

```text
ICMP Source Quench
     ↓ historical congestion feedback branch
     ✕ not the lineage that produced modern TCP congestion control
```

## 8. Timestamp and Information messages — reminders of a more experimental Internet layer

Early ICMP included mechanisms such as Timestamp and Information Request/Reply.

These reveal that the original Internet control plane experimented with responsibilities that later moved elsewhere or lost relevance.

A protocol type table therefore doubles as a map of abandoned design responsibilities.

## 9. Type/code values are a technical fossil register

ICMP's structure is particularly archaeological because meaning is partly identified by compact numeric assignments:

```text
Type
  └─ Code
```

A mature archive should record, for every historical type/code:

- original RFC and definition;
- updates/obsolescence;
- whether modern host/router requirements still mention it;
- whether common kernels generate it;
- whether common firewalls pass/drop it;
- whether modern tools depend on it;
- surviving packet-capture examples.

## 10. ICMP shows why “old standard still used” is not binary

Inside one 1981 protocol, we can simultaneously have:

```text
Echo               → strongly alive
Time Exceeded       → strongly alive + diagnostic afterlife
Destination Unreach → strongly alive but code-specific evolution
Redirect             → alive but operationally constrained
Source Quench        → extinct branch
Timestamp/Info       → mostly historical/specialized branches
```

So protocol survival should be mapped at message-type granularity.

## Primary source spine

- RFC 792 — ICMP;
- RFC 1122 — host requirements;
- RFC 1812 — router requirements and code clarifications;
- later deprecation/requirements RFCs to be promoted type-by-type.

## Next excavation

- complete Type/Code table with status and successor RFCs;
- trace Source Quench deprecation;
- trace ICMP Redirect security practice;
- trace Fragmentation Needed into Path MTU Discovery;
- compare BSD/Linux ICMP implementations;
- build packet-capture corpus for living types;
- map ICMPv4 concepts to ICMPv6 without pretending ICMPv6 is merely a revision.

---

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
