# Linux `ifconfig` ioctls to rtnetlink: the control-plane interface changes under a familiar job

## Question

When did Linux stop treating interface configuration primarily as a pile of socket `ioctl(2)` calls and start exposing network objects through rtnetlink?

The answer is not a single cutover date. It is a migration with a long compatibility tail.

## 1. The old control surface: `ifreq` plus network-device ioctls

Classic Linux interface configuration uses the socket ioctl interface described today by `netdevice(7)`. The central data structure is `struct ifreq`; the operation is selected by an ioctl number.

Representative families include:

```text
SIOCGIFFLAGS / SIOCSIFFLAGS   interface flags
SIOCGIFADDR  / SIOCSIFADDR    protocol address
SIOCGIFNETMASK / SIOCSIFNETMASK
SIOCGIFBRDADDR / SIOCSIFBRDADDR
SIOCGIFDSTADDR / SIOCSIFDSTADDR
SIOCGIFMTU / SIOCSIFMTU
SIOCGIFHWADDR / SIOCSIFHWADDR
SIOCGIFMAP / SIOCSIFMAP
SIOCGIFTXQLEN / SIOCSIFTXQLEN
SIOCGIFCONF                    enumerate IPv4 interface addresses
```

This API is object-poor: many unrelated interface properties are multiplexed through command numbers and a union-shaped `ifreq` structure.

It also exposes historical constraints. Current `netdevice(7)` still documents that `SIOCGIFCONF` enumerates only AF_INET addresses for compatibility. The modern `ifconfig(8)` documentation also records hardware-address limits imposed by the old `struct sockaddr`/ioctl path and recommends `ip link` when the old representation is insufficient.

So the important lineage is not:

```text
ifconfig → ip
```

but:

```text
socket ioctl command family
        ↓ operational interface
ifconfig
```

## 2. Linux 2.1 already begins escaping the ioctl model

The decisive architectural change appears in the 2.1 development series.

A Linux 2.1.15 patch dated December 1996 still shows the older Netlink character-device world, but it also contains a general `nlmsghdr` message format and batching code. This is a transitional layer: Netlink exists, but it is not yet the socket-based rtnetlink object model that later becomes familiar.

A much larger break lands in Linux 2.1.68, released around the end of November 1997.

That patch creates `include/linux/rtnetlink.h` with message classes that are immediately recognizable today:

```text
RTM_NEWLINK / DELLINK / GETLINK
RTM_NEWADDR / DELADDR / GETADDR
RTM_NEWROUTE / DELROUTE / GETROUTE
RTM_NEWNEIGH / DELNEIGH / GETNEIGH
RTM_NEWRULE / DELRULE / GETRULE
```

It also defines multicast notification groups such as:

```text
RTMGRP_LINK
RTMGRP_IPV4_IFADDR
RTMGRP_IPV4_ROUTE
RTMGRP_IPV6_IFADDR
RTMGRP_IPV6_ROUTE
```

This is a fundamentally different control surface. Instead of “issue ioctl X against `ifreq`”, user space exchanges typed objects and attributes with the kernel.

## 3. Compatibility is implemented explicitly

One of the strongest pieces of evidence against a clean replacement story is Linux 2.1.68 `fib_semantics.c`.

The patch contains `fib_convert_rtentry()` under a compatibility conditional. It translates the old route ioctl representation into an rtnetlink-style message:

```text
old SIOCDELRT / route ioctl
        ↓ conversion
RTM_DELROUTE

old route add ioctl
        ↓ conversion
RTM_NEWROUTE
```

That is a literal compatibility bridge inside the kernel.

So the migration pattern is:

```text
old user API remains callable
        ↓
kernel translates legacy representation
        ↓
new routing object machinery
```

This is a much more precise historical statement than “Linux replaced ioctls with netlink.”

## 4. Linux 2.2 is the first stable generation where rtnetlink becomes a public baseline

Current `rtnetlink(7)` records rtnetlink as a new feature of Linux 2.2. The `ip(8)` history likewise says `ip` was written by Alexey Kuznetsov and added in Linux 2.2.

That makes Linux 2.2 the useful stable-release boundary for userspace archaeology even though the implementation work is visible earlier in 2.1.

A period-correct lineage therefore looks like:

```text
pre-2.2 Linux
socket ioctls + route ioctls
       │
       ├── old ifconfig/route tools continue
       │
Linux 2.1 development
       ↓
Netlink message machinery
       ↓
2.1.68 rtnetlink object families
       ↓
Linux 2.2 stable
       ↓
iproute/iproute2 grows around NETLINK_ROUTE
```

## 5. Why `ip addr` and `ip link` are not just prettier `ifconfig`

The newer tool can address separate kernel object types:

```text
link
address
route
rule
neighbor
qdisc
class
filter
```

Each can carry extensible attributes.

That matters because new features no longer need to be forced into a fixed `ifreq` union or a new ioctl number. The same message/attribute pattern can grow.

This architecture also supports asynchronous notification, dumps, multiple routing tables, policy rules, namespaces and later VRF/l3mdev interactions.

## 6. Survivorship

The ioctl interface did not disappear.

Modern Linux still documents and supports many network-device ioctls. Old programs can continue using them. This is therefore another case of additive layering:

```text
ioctl API survives for compatibility
        +
rtnetlink becomes richer control plane
```

The modern operational recommendation may favor `ip`, but historical survivorship is real.

## 7. Root-hunting conclusion

The exact thing that survives from early Linux is not one command name. It is a stack of compatibility layers:

```text
1980s/early Unix-style interface configuration idea
        ↓
Linux socket ioctl / ifreq API
        ↓ survives
ifconfig

meanwhile

1996–1997 Netlink transition
        ↓
2.1.68 rtnetlink objects
        ↓
Linux 2.2 stable public interface
        ↓
iproute2: ip link / ip addr / ip route / ip rule / ip neigh
```

The key historical event is that **Linux changed the kernel/user-space language from command-number ioctls toward extensible object messages while deliberately preserving the old API**.

## Primary / near-primary anchors

- Linux `netdevice(7)`: https://man7.org/linux/man-pages/man7/netdevice.7.html
- Linux `rtnetlink(7)`: https://man7.org/linux/man-pages/man7/rtnetlink.7.html
- Linux 2.1.15 Netlink patch: https://test.nic.funet.fi/pub/linux/PEOPLE/Linus/v2.1/patch-html/patch-2.1.15/linux_net_netlink.c.html
- Linux 2.1.68 `rtnetlink.h` patch: https://www.nic.funet.fi/pub/Linux/kernel/v2.1/patch-html/patch-2.1.68/linux_include_linux_rtnetlink.h.html
- Linux 2.1.68 FIB compatibility conversion: https://www.nic.funet.fi/pub/linux/kernel/v2.1/patch-html/patch-2.1.68/linux_net_ipv4_fib_semantics.c.html
- RFC 3549, retrospective Netlink architecture/prior-art description: https://www.rfc-editor.org/info/rfc3549/

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
