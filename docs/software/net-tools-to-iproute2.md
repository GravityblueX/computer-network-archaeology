# From net-tools to iproute2: Linux Networking Outgrows `ifconfig` and `route`

## Why this transition matters

A Linux administrator from the 1990s would recognize:

```text
ifconfig
route
arp
netstat
```

A modern Linux administrator is more likely to use:

```text
ip addr
ip route
ip neigh
ss
```

This looks like a command-line modernization story, but it is deeper than syntax.

The transition reflects a change in the **kernel networking object model and control API**.

---

## 1. net-tools belongs to the Linux NET-3 generation

The Linux Foundation networking documentation describes net-tools as the collection that formed the base set of the Linux NET-3 networking distribution.

It includes:

```text
arp
hostname
ifconfig
ipmaddr
iptunnel
mii-tool
nameif
netstat
plipconfig
rarp
route
slattach
```

These tools inherited a Unix administrative vocabulary that looked familiar to BSD/System V operators.

For ordinary IPv4 host setup, the model was straightforward:

```text
ifconfig → interface address/up/down
route    → kernel routing table
arp      → neighbor mapping
netstat  → protocol/socket/interface statistics
```

That model was enormously successful and became embedded in documentation and scripts.

---

## 2. Compatibility success became a constraint

The Linux Foundation documentation now explicitly warns that most net-tools programs are obsolete and gives direct replacements:

```text
arp       → ip neigh
ifconfig  → ip addr
ipmaddr   → ip maddr
iptunnel  → ip tunnel
route     → ip route
mii-tool  → ethtool
```

This is important because the older tools did not become “wrong” overnight.

Instead, Linux networking grew capabilities that the older command/data model represented poorly.

Examples include:

- multiple addresses per interface without fake alias-device naming;
- multiple routing tables;
- policy routing;
- richer neighbor state;
- multipath routing;
- traffic control;
- tunnels and virtual link types;
- namespaces;
- richer per-route metrics and attributes.

---

## 3. Interface aliasing is a visible fossil

Linux kernel documentation calls IP aliases an **obsolete way** to manage multiple addresses/masks per interface.

Classic practice looked like:

```text
ifconfig eth0:0 192.0.2.2 ...
```

The `eth0:0` object was not truly a separate network device; it was a compatibility naming trick.

Modern iproute2 instead models several addresses directly on one link:

```text
ip addr add 192.0.2.2/24 dev eth0
ip addr add 198.51.100.2/24 dev eth0
```

This illustrates the architectural change perfectly:

```text
old user-visible illusion: one pseudo-interface name per extra address

new model: one link object with a set of address objects
```

The kernel documentation says alias support remains for backward compatibility.

So the fossil is still operational.

---

## 4. iproute2 reflects netlink objects rather than old ioctl-era assumptions

iproute2 is built around the richer Linux networking-control model exposed through netlink/rtnetlink.

The suite includes commands for:

```text
link
address
route
rule
neighbor
tunnel
multicast
traffic control
```

The Linux Foundation describes iproute2 as the utility collection for controlling TCP/IP networking and traffic control and identifies Alexey Kuznetsov as the original author.

The important relationship is:

```text
kernel networking objects
        ↕ rtnetlink/netlink
iproute2
        ↓
operator CLI
```

The tool suite mirrors kernel object classes more directly than the older collection.

---

## 5. `route` and `ip route` share a role, not a command grammar

Both can add or display routes.

But compare the conceptual data exposed:

```text
classic route:
destination / gateway / mask / flags / metric / interface
```

with modern `ip route`:

```text
prefix
route type
routing table
scope
protocol origin
metric
multiple nexthops
per-route MTU/RTT attributes
source preferences
policy-routing context
```

The same operator task expanded into a richer route object.

Therefore:

```text
route(8) → ip route
```

should be recorded as **role migration**, not formal revision or source inheritance.

---

## 6. `ifconfig` and `ip addr` reveal the same transition

Classic `ifconfig` tends to present interface configuration as one aggregate object.

Modern Linux separates:

```text
link object
address object(s)
neighbor object(s)
route object(s)
rule object(s)
```

This matters for containers, VRFs, policy routing, IPv6 and complex virtual networking.

The modern CLI is therefore not only a prettier syntax; it is a user-space reflection of a different kernel control model.

---

## 7. Old commands survive because scripts and operator memory are standards too

Even after official documentation says a utility is obsolete, it can remain installed because:

- shell scripts depend on output format;
- installers assume its presence;
- textbooks keep teaching it;
- operators remember it;
- embedded systems ship older tooling;
- compatibility packages remain easy to install.

This is another type of living standard:

> **not an RFC or wire format, but a command-language convention stabilized by decades of operational use.**

---

## 8. The migration is incomplete by design

The Linux kernel continues carrying compatibility mechanisms such as interface alias conventions.

Distributions still package net-tools in many environments.

So there is no clean death date:

```text
net-tools alive
      ↓
iproute2 introduced and grows
      ↓
both coexist for years/decades
      ↓
iproute2 becomes recommended control surface
      ↓
old tools remain compatibility fossils
```

This is more realistic than writing “iproute2 replaced net-tools in year X.”

---

## 9. A modern command can expose old concepts under new syntax

For example:

```text
ip route show
```

still exposes ideas that long predate Linux:

- destination prefix;
- gateway/nexthop;
- metric/preference;
- interface;
- routing protocol origin.

The underlying transport to the kernel is new, but the routing concepts are older.

So root-hunting must separate:

```text
concept genealogy
operator-language genealogy
kernel-API genealogy
source-code genealogy
```

---

## 10. What to preserve

For each Linux era:

- net-tools source release;
- iproute2 source release;
- matching kernel headers;
- netlink/rtnetlink ABI generation;
- command manuals;
- distro network configuration scripts;
- shell scripts using old commands;
- sample outputs;
- kernel compatibility documentation;
- migration guides.

A particularly useful exhibit would show one task side by side:

```text
1990s-style:
ifconfig eth0 ...
route add ...
arp -n

modern:
ip link ...
ip addr ...
ip route ...
ip neigh ...
```

with the corresponding kernel calls/messages underneath.

---

## Primary anchors

- Linux Foundation net-tools documentation — identifies NET-3 collection and lists obsolete tools/replacements.
- Linux Foundation iproute2 documentation — explains iproute2's role and original authorship.
- Linux kernel IP-aliasing documentation — explicitly calls alias interfaces obsolete and recommends newer iproute2-style multiple-address management.
- maintained iproute2 source repository.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
