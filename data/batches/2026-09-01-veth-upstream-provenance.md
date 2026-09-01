# Batch: Linux veth initial upstream provenance — 2026-09-01

This batch advances one explicitly open part of the network-namespace worklist: **veth merge provenance**.

It does not claim completion of the network-namespace merge series or `ip netns` first-release archaeology.

## Narrative excavation

- `docs/routing/linux-veth-upstream-provenance.md`

## Structured sources

- `SRC-0269` — Linux commit `e314dbdc1c0dc6a548ecf0afce28ecfd538ff568`, `[NET]: Virtual ethernet device driver.`
- `SRC-0270` — Linux `v2.6.24` `drivers/net/veth.c` source snapshot.

## Structured artifact

- `ART-0249` — Linux veth pair device, initial mainline implementation.

## Recovered facts

1. Exact upstream introduction: `e314dbdc1c0dc6a548ecf0afce28ecfd538ff568`, committed 2007-10-10.
2. The initial commit defines veth as a paired link-layer Ethernet device and explicitly states network-namespace communication as a main use.
3. The initial `newlink` design anticipates creating the peer in a separate namespace when the necessary namespace support is in the kernel.
4. `drivers/net/veth.c` is absent at tag `v2.6.23` and present at tag `v2.6.24`; therefore 2.6.24 is the first stable mainline release containing this driver.
5. The v2.6.24 source header preserves 2007 OpenVZ / SWsoft Inc copyright and Pavel Emelianov authorship provenance.

## Lineage decision

**No `LIN-*` record is created.**

The evidence supports a contemporary intended-use/composition relationship between veth and Linux network namespaces. It does not support `derived-from`, `successor`, or causal influence. `ART-0249` records the functional relationship to `ART-0231` in `related_artifacts` only.

## Explicit negative claims

This batch does **not** prove:

- first real-world deployment of veth;
- completion/maturity date of Linux network namespaces as a subsystem;
- first iproute2 release containing `ip netns`;
- first public veth prototype or out-of-tree patch;
- derivation of mainline veth from a particular earlier OpenVZ implementation merely from copyright/affiliation;
- that network namespaces caused veth simply because the initial veth commit discusses them.

## Remaining work in the parent item

- recover the exact network-namespace merge series and component chronology;
- recover the first iproute2 source release containing `ip netns`;
- optionally recover pre-mainline veth patch-series history to test stronger provenance claims.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), September 2026**.
