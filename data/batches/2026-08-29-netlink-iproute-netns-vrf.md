# Batch: Linux Netlink/iproute/namespaces/VRF roots — 2026-08-29

This batch completes the first post-Linux-operations group in the persistent root-hunting worklist.

## Narrative excavations

- `docs/software/linux-ifconfig-ioctl-rtnetlink-transition.md`
- `docs/software/netlink-rtnetlink-origins.md`
- `docs/software/iproute2-early-release-command-evolution.md`
- `docs/operations/rtmon-ip-monitor-rtnetlink-events.md`
- `docs/routing/network-namespaces-vrf-l3mdev-rpdb.md`

## Structured sources

`SRC-0236..0247` cover:

- current Linux network-device ioctl ABI;
- Linux 2.1.15 transitional Netlink source;
- Linux 2.1.68 rtnetlink object model;
- 2.1.68 legacy route-ioctl compatibility translation;
- RFC 3549 participant retrospective;
- ip/iproute history and surviving archive snapshots;
- ip monitor / rtmon;
- network namespaces / CLONE_NEWNET chronology;
- Linux VRF/l3mdev transition documentation.

## Structured artifacts

- `ART-0225` legacy network-device ioctl control family
- `ART-0226` Linux 2.1.15 Netlink character-device/message hybrid
- `ART-0227` Linux 2.1.68 rtnetlink object model
- `ART-0228` early ip/iproute/iproute2 suite
- `ART-0229` rtmon
- `ART-0230` ip monitor
- `ART-0231` Linux network namespace
- `ART-0232` Linux VRF/l3mdev
- `ART-0233` generic l3mdev FIB rule

## Structured lineages

- `LIN-0178` ioctl configuration role → rtnetlink object control
- `LIN-0179` legacy route ioctl → rtnetlink/FIB compatibility conversion
- `LIN-0180` character-device Netlink generation → socket/object-generation Netlink
- `LIN-0181` nlmsghdr/message concepts carried across the transition
- `LIN-0182` rtnetlink object model → ip/iproute userspace vocabulary
- `LIN-0183` rtnetlink multicast notifications → rtmon
- `LIN-0184` rtmon event role → ip monitor live/replay role
- `LIN-0185` RPDB/multiple tables carried into VRF lookup architecture
- `LIN-0186` per-VRF iif/oif rules → generic l3mdev rule
- `LIN-0187` network namespaces ↔ VRF coexist/composition negative-lineage guard

## Important unresolved claim

The exact first public iproute/iproute2 tarball has **not** been proven. Current evidence establishes:

- development/authorship in the 1996-era;
- Linux 2.2 stable-generation association;
- surviving archived iproute2 snapshot families from 1999 onward.

The master worklist therefore marks this item `[~]`, not `[x]`.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
