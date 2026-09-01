# Linux veth initial upstream provenance

## Scope

This note answers one narrow question left open by the network-namespace work: **when and how did the Linux `veth` pair driver enter mainline, and what does the initial source actually say about its relation to network namespaces?**

It does **not** attempt to finish the broader network-namespace merge series or the first-release archaeology of `ip netns`.

## Recovered upstream introduction

The exact mainline introduction is Linux commit:

- `e314dbdc1c0dc6a548ecf0afce28ecfd538ff568`
- subject: `[NET]: Virtual ethernet device driver.`
- committed: 2007-10-10
- signed off by Pavel Emelyanov and David S. Miller; Patrick McHardy acked the change; the message also credits Daniel Lezcano for bug fixes.

The commit adds `CONFIG_VETH`, wires `veth.o` into `drivers/net/Makefile`, and introduces `drivers/net/veth.c` as a new driver.

The commit describes `veth` as a link-layer pair of Ethernet devices: traffic sent into one end appears at the peer. It explicitly says the driver's main intended use is communication between network namespaces, while also saying the pair can be used by itself. The `newlink` path was arranged so that peer creation in a separate namespace would be straightforward once the needed namespace support was present in the kernel.

That wording matters historically. It establishes a **contemporary intended-use/composition relationship** between `veth` and network namespaces. It does not establish that one artifact descended from the other.

## Stable-release boundary

A direct adjacent-tag check gives a clean lower bound:

- `drivers/net/veth.c` is absent from the Linux `v2.6.23` tag;
- `drivers/net/veth.c` is present in the Linux `v2.6.24` tag.

The `v2.6.24` file identifies itself as `drivers/net/veth.c`, carries 2007 OpenVZ / SWsoft Inc copyright, names Pavel Emelianov as author, and reports driver version `1.0`.

Therefore **Linux 2.6.24 is the first stable mainline release containing this `veth` driver**. This is a release-content claim, not a first-deployment claim.

## Evidence table

| Claim | Primary evidence | Locator | Certainty |
|---|---|---|---|
| Exact mainline introduction | Linux commit `e314dbdc1c0dc6a548ecf0afce28ecfd538ff568` | commit message + Kconfig/Makefile/new `drivers/net/veth.c` diff | confirmed |
| Pair semantics are part of the initial implementation | same commit | commit message; `veth_xmit`; Kconfig help | confirmed |
| Network namespaces were a stated main use | same commit | commit message | confirmed |
| Peer creation was shaped for future separate-namespace creation | same commit | commit message + `veth_newlink` diff | confirmed |
| OpenVZ/SWsoft/Pavel authorship provenance appears in released source | Linux `v2.6.24` `drivers/net/veth.c` | file header | confirmed |
| First stable mainline release containing the file is 2.6.24 | adjacent `v2.6.23` / `v2.6.24` tag check | `drivers/net/veth.c` path | confirmed |

## What this evidence does **not** prove

1. It does not prove the date of the first production or user deployment of `veth`.
2. It does not prove when network namespaces as a whole became complete or operationally mature.
3. It does not prove the first iproute2 release containing `ip netns`.
4. The OpenVZ/SWsoft copyright and author affiliation do not, by themselves, prove that Linux mainline `veth` was architecturally derived from one specific earlier OpenVZ virtual-networking implementation.
5. The fact that the veth commit discusses network namespaces does not justify a lineage edge saying “network namespaces caused veth” or “veth descended from network namespaces.” The source supports intended composition/use, not descent.
6. The commit's timing does not establish first public discussion, first prototype, or first out-of-tree patch. Those would require mailing-list / patch-series recovery.

## Lineage decision

**No lineage-ledger edge is added in this batch.**

`ART-0249` is related to `ART-0231` (Linux network namespace) by an explicitly documented functional/composition relationship: the initial veth commit says namespace communication is a main use and anticipates separate-namespace peer creation. That is not enough evidence for `derived-from`, `successor`, `influenced`, or another descent relation.

## Remaining gap

The parent worklist item remains only partially complete. Still needed:

- exact network-namespace subsystem merge series and component chronology;
- first iproute2 release / source snapshot containing `ip netns`;
- if desired, pre-mainline veth patch-series or OpenVZ provenance sufficient to test a stronger implementation-lineage claim.

## Primary source locations

- Linux commit `e314dbdc1c0dc6a548ecf0afce28ecfd538ff568`: `https://github.com/torvalds/linux/commit/e314dbdc1c0dc6a548ecf0afce28ecfd538ff568`
- Linux v2.6.24 source: `https://github.com/torvalds/linux/blob/v2.6.24/drivers/net/veth.c`
- Linux v2.6.23 tree used for the adjacent-tag absence check: `https://github.com/torvalds/linux/tree/v2.6.23/drivers/net`

Research and initial drafting: **GPT-5.6 Sol (OpenAI), September 2026**.
