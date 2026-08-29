# `rtmon` and `ip monitor`: asynchronous rtnetlink becomes operational history

## Why monitoring is a separate lineage from configuration

A command such as:

```text
ip route add ...
```

is an active control operation.

A command such as:

```text
ip monitor route
```

is different: it subscribes to kernel state changes and watches the control plane evolve over time.

The root of this capability is already visible in the first rtnetlink object model.

## 1. Linux 2.1.68 already defines notification groups

The Linux 2.1.68 `rtnetlink.h` patch defines multicast groups including:

```text
RTMGRP_LINK
RTMGRP_NOTIFY
RTMGRP_IPV4_IFADDR
RTMGRP_IPV4_NDISC
RTMGRP_IPV4_ROUTE
RTMGRP_IPV4_MROUTE
RTMGRP_IPV6_IFADDR
RTMGRP_IPV6_NDISC
RTMGRP_IPV6_ROUTE
RTMGRP_IPV6_MROUTE
```

This is critical evidence that asynchronous observation is not a late convenience bolted onto `ip`.

It is architectural from the early rtnetlink generation:

```text
kernel object mutation
      ↓
multicast notification group
      ↓
one or many listeners
```

## 2. The same object vocabulary serves both dump and event streams

rtnetlink exposes operations such as `RTM_GETROUTE`, `RTM_NEWROUTE` and `RTM_DELROUTE`.

That allows user space to combine:

```text
initial full dump
      +
subsequent asynchronous events
```

This pattern later becomes fundamental for:

- routing daemons;
- network managers;
- orchestration agents;
- `ip monitor`;
- `rtmon`;
- state-reconciliation systems.

The modern control-plane pattern “snapshot + watch” is therefore visible in Linux networking decades before contemporary controller terminology became common.

## 3. `rtmon`: preserve rtnetlink events as a binary history

`rtmon(8)` is credited to Alexey Kuznetsov.

Its job is not merely printing live updates. It can write rtnetlink messages to a file:

```text
rtmon file /var/log/rtmon.log
```

The manual recommends starting it before network configuration begins if a full history is desired.

Later:

```text
ip monitor file /var/log/rtmon.log
```

can decode the recorded messages.

This creates a striking operational artifact:

```text
kernel control-plane event
      ↓
rtnetlink binary message
      ↓
log file
      ↓
later replay/interpretation
```

The log preserves the kernel/user API itself, not merely a human-formatted textual summary.

## 4. `ip monitor`: the same object model becomes a live observability interface

Current `ip-monitor(8)` says that if no file is specified, the command opens RTNETLINK and listens for state changes.

It can watch object families including:

```text
link
address
route
mroute
maddress
neigh
netconf
rule
stats
nsid
nexthop
```

This list demonstrates how the original link/address/route/rule/neighbour model accumulated new object families without discarding the basic subscription architecture.

## 5. Namespace IDs extend the same event model

Modern `ip monitor` can listen with `all-nsid` and label events with the originating network namespace ID.

That is historically important because namespaces did not require a brand-new monitoring architecture. Instead:

```text
rtnetlink event model
      ↓ extended with namespace identity
same monitor/replay tooling
```

The event language survives while the scope model becomes more complex.

## 6. This is different from polling `/proc`

An older operational style often looks like:

```text
read /proc/net/*
wait
read again
compare snapshots
```

rtnetlink monitoring instead gives:

```text
subscribe
receive typed event
```

These approaches can coexist, but they have different semantics and failure modes.

A missed multicast notification requires resynchronization; a polling loop may miss transient state but reconstruct current state on every read. Modern network software often combines an initial dump with event subscription precisely because neither alone is sufficient.

## 7. Why this matters for routing daemons

Dynamic routing software must learn when:

- an interface appears/disappears;
- an address changes;
- a route changes;
- a neighbour changes;
- policy rules or nexthops change.

The rtnetlink multicast model turns Linux from a kernel that must be periodically scraped into a kernel that can actively notify control-plane processes.

This is one of the roots of the modern Linux networking-controller style.

## 8. Root-hunting lineage

```text
Linux 2.1.68 rtnetlink multicast groups
        ↓
NETLINK_ROUTE asynchronous notifications
        ↓
rtmon binary event logging
        ↓
ip monitor live decode / replay
        ↓
namespace-aware and new-object monitoring
        ↓
modern route/network managers and controllers
```

The thing that survives is the idea that **network state is a stream of typed object events, not only a set of values returned by query commands**.

## Evidence anchors

- Linux 2.1.68 rtnetlink header patch: https://www.nic.funet.fi/pub/Linux/kernel/v2.1/patch-html/patch-2.1.68/linux_include_linux_rtnetlink.h.html
- `ip-monitor(8)`: https://man7.org/linux/man-pages/man8/ip-monitor.8.html
- `rtmon(8)`: https://man7.org/linux/man-pages/man8/rtmon.8.html
- `rtnetlink(7)`: https://man7.org/linux/man-pages/man7/rtnetlink.7.html
- RFC 3549 asynchronous-notification architecture: https://www.rfc-editor.org/info/rfc3549/

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
