# Linux network namespaces, VRF/l3mdev and RPDB: three different ways to split one machine into routing worlds

## Why these mechanisms must not be collapsed

Modern Linux can isolate or partition networking in several ways:

```text
network namespace
VRF device / l3mdev
RPDB + multiple routing tables
```

They overlap operationally, but they are not versions of one feature.

A root-hunting archive must ask what each one isolates and which earlier mechanism it builds on.

## 1. RPDB and multiple FIB tables come first in this lineage

The rtnetlink header introduced in Linux 2.1.68 already contains rule operations:

```text
RTM_NEWRULE
RTM_DELRULE
RTM_GETRULE
```

and reserved routing-table identifiers:

```text
RT_TABLE_DEFAULT
RT_TABLE_MAIN
RT_TABLE_LOCAL
```

This is the early Linux policy-routing world: several route tables can exist, and rules decide which lookup path applies.

The abstraction is still one networking stack:

```text
one network namespace
        ↓
RPDB chooses table/action
        ↓
multiple FIB tables
```

## 2. Network namespaces isolate the networking stack itself

`CLONE_NEWNET` is documented since Linux 2.6.24, with implementation work completed only around 2.6.29.

A network namespace isolates resources including:

- devices;
- IPv4 and IPv6 protocol stacks;
- routing tables;
- firewall rules;
- `/proc/net` view;
- `/sys/class/net` view;
- sockets and port-number space;
- UNIX abstract sockets.

This is a much stronger boundary than choosing another route table.

Conceptually:

```text
machine
 ├── netns A
 │    ├── interfaces
 │    ├── addresses
 │    ├── routes/RPDB
 │    ├── firewall
 │    └── sockets
 └── netns B
      ├── different interfaces
      ├── different routes/RPDB
      └── different sockets
```

Each namespace can then contain its own policy-routing system.

## 3. veth connects namespaces without erasing the isolation boundary

The network-namespace model introduces a useful pair abstraction:

```text
veth-A ===== veth-B
```

with each endpoint placed in a different namespace.

This makes the isolation operationally useful: one can build routers, containers and virtual topologies while keeping separate stacks.

Again, this is not “multiple routing tables with a new command.” It is stack replication/isolation.

## 4. `ip netns` is the userspace administration layer

`ip netns` provides persistent naming and administration of network namespaces.

Typical operations include:

```text
ip netns add NAME
ip netns exec NAME ...
ip link set DEV netns NAME
```

The operational lineage is:

```text
CLONE_NEWNET / namespace kernel mechanism
        ↓
namespace file-descriptor and lifecycle APIs
        ↓
iproute2 namespace administration
```

The underlying namespace is a kernel object; the friendly persistent name is a userspace management convention.

## 5. VRF is not a lightweight network namespace

Linux VRF devices solve a different problem.

Kernel VRF documentation says a VRF device plus `ip rules` provides virtual routing and forwarding domains. A VRF is associated with a routing table.

Example:

```text
ip link add vrf-blue type vrf table 10
```

Interfaces can then be enslaved to the VRF device.

The key boundary is documented explicitly: Linux VRF primarily affects Layer 3 and above. Layer-2 tools do not necessarily need to run separately for each VRF.

So:

```text
network namespace
    = broad network-stack isolation

VRF/l3mdev
    = L3 routing-domain separation inside a namespace
```

They can even be nested operationally:

```text
network namespace
      ↓
VRF devices
      ↓
per-VRF FIB tables
```

## 6. Before l3mdev: per-VRF iif/oif rules

The Linux kernel VRF documentation preserves a useful migration fossil.

Before Linux 4.8, each VRF needed explicit input/output-interface rules such as:

```text
ip rule add iif vrf-blue table 10
ip rule add oif vrf-blue table 10
```

plus IPv6 equivalents.

This shows that early VRF support was layered directly on the existing RPDB rule machinery.

## 7. Linux 4.8: l3mdev condenses the rule layer

As of Linux 4.8, the kernel supports an `l3mdev` FIB rule. One rule can direct lookups to the table associated with the L3-master device.

The first VRF device creates default IPv4 and IPv6 l3mdev rules.

So the architecture changes from:

```text
one iif/oif rule per VRF
```

to:

```text
single l3mdev rule
      ↓
VRF device identity
      ↓
associated FIB table
```

This is a real simplification of policy-routing plumbing, not a new routing protocol.

## 8. iproute2 gains explicit VRF language

Kernel documentation says iproute2 supports the `vrf` keyword as of version 4.7.

This creates another familiar pattern:

```text
kernel mechanism appears
        ↓
generic old syntax can operate it
        ↓
later user-space gains first-class vocabulary
```

The operational interface becomes clearer without changing the fundamental routing-domain concept.

## 9. PBR can override VRF defaults

Linux VRF documentation explicitly says higher-priority policy-routing rules may take precedence over the VRF device rules.

This is crucial for genealogy:

```text
VRF does not replace RPDB
VRF consumes/integrates with RPDB
```

The RPDB remains an underlying selection engine.

## 10. Why modern systems combine all three

A containerized router or multi-tenant host might use:

```text
network namespace
   ↓ isolate device/stack/socket world
VRF
   ↓ split L3 routing domains within that namespace
RPDB rules
   ↓ override/select special traffic paths
multiple FIB tables
```

These are composable mechanisms from different historical layers.

## 11. Root-hunting lineage

```text
Linux 2.1/2.2 policy routing
RPDB + multiple FIB tables
        │
        ├───────────────┐
        ↓               │
network namespaces      │
2.6.24→2.6.29           │
stack isolation         │
        │               │
        └─ can contain ─┤
                        ↓
                     VRF device
                     Linux 4.x
                        ↓
              per-VRF iif/oif rules
                        ↓
                 Linux 4.8 l3mdev
```

Do not rewrite this as a false linear chain:

```text
RPDB → netns → VRF
```

They solve different scopes and coexist.

## Evidence anchors

- `network_namespaces(7)`: https://man7.org/linux/man-pages/man7/network_namespaces.7.html
- `clone(2)` / `CLONE_NEWNET`: https://man7.org/linux/man-pages/man2/clone.2.html
- historical CLONE_NEWNET documentation discussion: https://lkml.iu.edu/0811.2/02085.html
- Linux VRF documentation: https://docs.kernel.org/networking/vrf.html
- older VRF documentation preserving 4.7/4.8 transition: https://kernel.org/doc/html/v5.12/networking/vrf.html
- `ip-netns(8)`: https://man7.org/linux/man-pages/man8/ip-netns.8.html
- Linux 2.1.68 `rtnetlink.h`: https://www.nic.funet.fi/pub/Linux/kernel/v2.1/patch-html/patch-2.1.68/linux_include_linux_rtnetlink.h.html

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
