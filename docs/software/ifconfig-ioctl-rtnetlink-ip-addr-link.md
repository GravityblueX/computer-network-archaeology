# From `ifconfig` and ioctls to rtnetlink, `ip addr`, and `ip link`

## The command changed because the kernel interface changed

A shallow history says Linux administrators replaced `ifconfig` with `ip`.

The useful history is deeper:

```text
classic Unix interface control
        ↓
network-device ioctl vocabulary
        ↓
Linux net-tools / ifconfig
        ↓                       parallel/newer control plane
                          netlink / rtnetlink objects + messages
                                      ↓
                                  iproute2
                             ┌─────────┴─────────┐
                           ip link            ip addr
```

`ifconfig(8)` still documents that it uses an **ioctl access method** for address information and even notes a concrete limitation: hardware-address retrieval through that path is limited to eight bytes, which is inadequate for a 20-byte InfiniBand address. The manual explicitly directs users to `ip link` for link-layer information.

That is unusually strong evidence that this is not merely command-fashion churn. The user-space tool is exposing constraints of the kernel ABI it depends on.

## Old control surface: device/socket ioctls

Traditional interface administration uses ioctl requests against sockets/network devices. The conceptual model is mostly imperative:

```text
open socket
  ↓
ioctl(SIOCG... / SIOCS...)
  ↓
read or change one device property
```

This is historically convenient but awkward as network objects grow richer: multiple addresses, long link-layer addresses, nested attributes, tunnels, namespaces, policy state and asynchronous notifications do not map elegantly onto a fixed ioctl vocabulary.

## rtnetlink turns network state into messages and attributes

Linux rtnetlink uses netlink messages for links, addresses, routes, neighbours, rules and related objects. Instead of one ioctl number implying one fixed operation/structure, messages contain headers plus typed attributes.

That model scales naturally into:

- `RTM_NEWLINK` / `RTM_DELLINK`;
- `RTM_NEWADDR` / `RTM_DELADDR`;
- route and neighbour messages;
- dump operations;
- multicast notifications to interested user-space processes.

The architectural shift is therefore:

```text
fixed ioctl operation + fixed structure
                  ↓
object/message family + extensible attributes
```

## `ip addr` and `ip link` split an old command's responsibilities

`ifconfig` historically combines several categories under one command. iproute2 makes the object explicit:

```text
ip link     → link-layer/device object
ip address  → protocol address attached to a link
ip route    → route object
ip neighbour→ neighbour-cache object
ip rule     → routing-policy rule
```

This decomposition matters archaeologically. It exposes how the Linux networking control plane itself came to think in separate object classes.

## Negative lineage

Do not write:

```text
ifconfig v1 → ip v2
```

`ip` is not a formal revision of `ifconfig`, and rtnetlink is not an ioctl protocol revision. The justified claim is a **role migration and control-API replacement/expansion** within Linux administration.

Likewise, modern Linux still contains ioctl compatibility paths. A newer interface can become dominant without erasing the older ABI.

## What survives

The operator goal is ancient:

> show or configure a network interface and its addresses.

The mechanism changed dramatically underneath that goal. That is exactly the kind of root-hunting distinction this repository wants to preserve.

Primary anchors:

- `ifconfig(8)`: https://man7.org/linux/man-pages/man8/ifconfig.8.html
- `ip-link(8)`: https://man7.org/linux/man-pages/man8/ip-link.8.html
- `ip-address(8)`: https://man7.org/linux/man-pages/man8/ip-address.8.html
- `rtnetlink(7)`: https://man7.org/linux/man-pages/man7/rtnetlink.7.html
