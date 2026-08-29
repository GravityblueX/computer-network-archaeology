# Netlink and rtnetlink origins: character device, message header, socket family, routing object model

## Why Netlink has more than one birthday

“Netlink was introduced in year X” is too coarse. Several distinct mechanisms appear at different points:

1. a kernel/user communication **character-device** mechanism;
2. a generic `nlmsghdr` **message framing** convention;
3. an `AF_NETLINK` **socket family**;
4. the `NETLINK_ROUTE` / **rtnetlink object model**;
5. applications such as `ip`, `rtmon`, routing daemons and later many non-routing Netlink families.

Treating these as one event hides the real migration.

## 1. Alan Cox's original Netlink character device

RFC 3549 explicitly credits the original Netlink character device to Alan Cox. Contemporary 2.1-series source still carries the older design in `net/netlink.c`.

The historical implementation describes itself as a loadable kernel-mode driver providing multiple bidirectional kernel/user links. The interface has major/minor-device concepts, open maps, queues and per-unit handlers.

This is not yet the modern mental model:

```text
socket(AF_NETLINK, ...)
```

It is closer to:

```text
/dev/netlink-style character-device endpoints
       ↓
kernel handlers / queues
```

The old source even preserves the earlier name `SKIPLINK` in its revision history before the comment is renamed `NETLINK`.

## 2. Linux 2.1.15: generic Netlink message structure appears in the old world

The December 1996 Linux 2.1.15 patch is an important transitional fossil.

The character-device implementation is still present, but the source now contains a generic `struct nlmsghdr` message model and helpers for batching, sequence values, sender identity, message types and overrun reporting.

Conceptually:

```text
old transport mechanism
      +
new message grammar
```

This demonstrates that **message-format genealogy and transport/API genealogy do not have to change at the same time**.

## 3. Linux 2.1.68: the socket-based generation and rtnetlink object language arrive together

The Linux 2.1.68 patch is a much stronger boundary.

It removes the old internal `include/net/netlink.h` character-device helper interface and integrates Netlink as a protocol family. The same patch introduces a large new `include/linux/rtnetlink.h`.

The latter already contains the object operations that still define modern rtnetlink:

```text
LINK     NEW / DEL / GET
ADDR     NEW / DEL / GET
ROUTE    NEW / DEL / GET
NEIGH    NEW / DEL / GET
RULE     NEW / DEL / GET
```

and object-specific structures including:

```text
ifinfomsg
ifaddrmsg
rtmsg
ndmsg / neighbour-related state
rtattr
rtnexthop
```

The significance is not merely “routing configuration.” It is an extensible **kernel object description language**.

## 4. Multicast groups make state change observable

The first `rtnetlink.h` already defines multicast groups such as:

```text
RTMGRP_LINK
RTMGRP_IPV4_IFADDR
RTMGRP_IPV4_NDISC
RTMGRP_IPV4_ROUTE
RTMGRP_IPV6_IFADDR
RTMGRP_IPV6_NDISC
RTMGRP_IPV6_ROUTE
```

This means the architecture is not only request/response.

It also supports:

```text
kernel object changes
       ↓ asynchronous multicast event
interested user-space listeners
```

That capability later becomes visible operationally through `rtmon`, `ip monitor`, routing suites, network managers and orchestration software.

## 5. Linux 2.2: stable public baseline

The modern `rtnetlink(7)` manual records rtnetlink as a new feature of Linux 2.2.

This is compatible with the source archaeology:

```text
2.1.x development work
       ↓
2.2 stable release interface
```

The period is also when the `ip` utility is remembered as entering the stable Linux networking toolchain.

## 6. RFC 3549 preserves the design interpretation

RFC 3549 was published in 2003 and is informational, not a standard for Linux. It is nevertheless valuable because one of its authors is Alexey Kuznetsov and it explicitly records the architecture as prior art.

It states that:

- the original character-device Netlink was Alan Cox's work;
- Alexey Kuznetsov extended Netlink into the IP-service delivery/control model;
- since the Linux 2.1 kernel, Netlink had been used for IP-service abstractions beyond classic forwarding;
- a Netlink message consists of a generic header, a service-specific template and service-specific TLV-style data;
- Netlink serves parameterization, asynchronous event notification and statistics/query functions.

This source therefore helps distinguish historical implementation stages from the later conceptual architecture.

## 7. Why this is not simply “Linux copied BSD routing sockets”

RFC 3549 explicitly places BSD 4.4 routing sockets earlier in the control-plane/forwarding-plane separation story, then describes Linux Netlink as taking that style of control further beyond classical IPv4 forwarding.

That supports an influence/role comparison, not a source-code ancestry claim.

Correct:

```text
BSD routing-socket control/notification concept
        ↓ historical architectural precedent
Linux Netlink/rtnetlink broader object/service model
```

Incorrect without stronger evidence:

```text
BSD routing socket source code → Netlink source code
```

## 8. Why Netlink survived and expanded

The extensible message model scales much better than a fixed list of socket ioctls when the kernel needs to expose:

- link properties;
- multiple addresses;
- routes and multipath next hops;
- policy rules;
- neighbours;
- traffic control;
- namespaces and namespace IDs;
- bridge/VLAN/tunnel attributes;
- XFRM and many later Netlink families.

This is a general survival pattern:

```text
old API solves one device-era problem
        ↓
networking complexity grows
        ↓
extensible attribute/message interface wins new responsibilities
        ↓
old API remains for compatibility
```

## 9. Root-hunting timeline

```text
pre-1996
Netlink character-device generation
        │ Alan Cox
        ↓
Linux 2.1.15 — Dec 1996
character-device transport + nlmsghdr message machinery
        ↓
Linux 2.1.68 — Nov/Dec 1997
socket-family transition + rtnetlink.h object model
        ↓
Linux 2.2
stable rtnetlink/iproute generation
        ↓
2003 RFC 3549
architecture documented as Linux prior art
        ↓
modern Linux
NETLINK_ROUTE + many other Netlink protocols
```

## Evidence anchors

- Linux 2.1.15 `net/netlink.c`: https://test.nic.funet.fi/pub/linux/PEOPLE/Linus/v2.1/patch-html/patch-2.1.15/linux_net_netlink.c.html
- Linux 2.1.68 `rtnetlink.h`: https://www.nic.funet.fi/pub/Linux/kernel/v2.1/patch-html/patch-2.1.68/linux_include_linux_rtnetlink.h.html
- Linux 2.1.68 old Netlink helper removal: https://ftp.csc.fi/index/Linux/kernel/v2.1/patch-html/patch-2.1.68/linux_include_net_netlink.h.html
- Modern `rtnetlink(7)`: https://man7.org/linux/man-pages/man7/rtnetlink.7.html
- RFC 3549: https://www.rfc-editor.org/info/rfc3549/

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
