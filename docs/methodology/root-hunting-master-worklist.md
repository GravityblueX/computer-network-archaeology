# Root-Hunting Master Worklist

This file is the persistent execution list for the repository's **寻根活动 / root-hunting** work. It exists so research does not depend on a chat reminder.

Status vocabulary:

- `[x]` completed to narrative + evidence-bearing structured-record level;
- `[~]` started/substantial, but an explicitly named primary-source/provenance gap remains;
- `[ ]` queued.

## 2026-08-29 Linux operations pass — completed

- [x] `ifconfig` / network-device ioctls → rtnetlink → `ip addr` / `ip link`.
- [x] `/proc/net/tcp` and `/proc/net/tcp6` → `tcp_diag` / `inet_diag` / `sock_diag`.
- [x] `ss -ti` as an operational window into RTO, RTT, MSS, cwnd, ssthresh, PMTU and congestion-control state.
- [x] ARP + IPv6 Neighbor Discovery/NUD → Linux neighbour object → `ip neigh`, with explicit negative lineage: ND is not “ARPv6”.
- [x] classic destination-only routing → Linux RPDB / multiple FIB tables → `ip rule`.
- [x] GNU Zebra/Quagga/FRR ZAPI versions 0–6, field-level revision matrix.

## Kernel/user-space interface archaeology

- [x] BSD PF_ROUTE versus Linux rtnetlink as parallel kernel-routing control families.
- [x] net-tools role migration into iproute2.
- [x] BPF → libpcap → tcpdump.
- [x] `/etc/services`, `/etc/protocols`, netdb, inetd.
- [x] `/etc/hosts`, resolver, NSS, `getaddrinfo`.
- [x] exact major Linux network-device ioctl families used by historical `ifconfig`-style administration, plus the 2.1.68 compatibility bridge translating legacy route ioctls into rtnetlink/FIB operations.
- [x] earliest currently recovered Linux Netlink/rtnetlink design provenance: 2.1.15 character-device + `nlmsghdr` transitional source, 2.1.68 socket/object-model patch, and participant retrospective in RFC 3549.
- [~] first iproute/iproute2 releases and command-syntax diffs. **Confirmed:** Kuznetsov authorship/development lower bound in the 1996 era, Linux 2.2 stable-generation association, object grammar, and surviving INR mirror snapshots from 1999 onward. **Still missing:** proof of the exact first public tarball and exact project-name transition to `iproute2`.
- [x] `ip monitor` / `rtmon` / asynchronous rtnetlink notification lineage, including early `RTMGRP_*` multicast groups and binary event-log replay.
- [x] network namespaces and VRF: CLONE_NEWNET broad stack isolation versus VRF/l3mdev L3 domains; pre-4.8 per-VRF iif/oif rules → Linux 4.8 generic l3mdev FIB rule; explicit composition with RPDB/multiple tables.
- [ ] recover pre-2.1.15 SKIPLINK/Netlink source and exact first AF_NETLINK socket-family merge commit.
- [ ] recover the exact first public iproute/iproute2 source distribution and earliest command-reference document.
- [ ] `ip monitor` event-loss/resync semantics and routing-daemon snapshot+watch patterns from primary implementation sources.
- [ ] network namespace merge series, veth merge provenance, and `ip netns` first-release archaeology.
- [ ] VRF device initial merge commit, netdev discussion, l3mdev rule commit and first real deployments.

## TCP implementation/observability archaeology

- [x] RFC 793 → RFC 9293 base-standard continuity.
- [x] Nagle versus Jacobson congestion work kept as different branches.
- [x] Window Scale/Timestamps and SACK option branches.
- [x] `/proc/net/tcp` → diag interfaces → `ss`.
- [x] `ss -i/-t -i` observable metrics map.
- [ ] Tahoe / Reno / NewReno / SACK recovery version-by-version.
- [ ] BIC → CUBIC Linux implementation genealogy.
- [ ] CUBIC RFC standardization versus Linux code history.
- [ ] BBR generations and pacing observability.
- [ ] `tcp_info` struct field/version genealogy by Linux release.
- [ ] TCP metrics cache and `ip tcp_metrics` history.
- [ ] packet captures paired with `ss -ti` output and RFC-variable concordance.

## Neighbour/address-resolution archaeology

- [x] ARP and Proxy ARP.
- [x] IPv6 ND/NUD distinction from ARP.
- [x] Linux unified neighbour object and `ip neigh`.
- [ ] NUD state transitions mapped to Linux neighbour timer/code paths.
- [ ] IPv4 ARP cache state handling versus IPv6 NUD state handling in shared neighbour core.
- [ ] gratuitous ARP / unsolicited NA operational branches.
- [ ] proxy neighbour / proxy ARP / ND proxy comparison.
- [ ] MAC randomization and locally-administered-address interaction with neighbour caches.

## Routing-policy/FIB archaeology

- [x] `route(8)`, `routed`, RIP and PF_ROUTE history.
- [x] GateD multiprotocol routing role.
- [x] GNU Zebra → Quagga → FRRouting real fork chain.
- [x] Linux rtnetlink/iproute2 route control.
- [x] Linux RPDB / `ip rule` / multiple tables.
- [ ] Linux FIB trie/hash implementation generations.
- [ ] policy-routing introduction commits and early HOWTO/deployment evidence.
- [ ] source routing, fwmark routing, VRF/l3mdev and namespaces as RPDB branches.
- [ ] `ip route get` lookup behavior genealogy.
- [ ] route cache removal and modern lookup architecture.

## Zebra / routing-suite internals

- [x] GateD role versus Zebra architecture kept separate from code ancestry.
- [x] GNU Zebra → Quagga fork.
- [x] Quagga → FRRouting fork.
- [x] ZAPI v0→v6 header/command revision matrix.
- [ ] earliest GNU Zebra/Zserv source snapshot and message layouts.
- [ ] exact Quagga 0.98/0.99 transition commits for ZAPI v0→v1.
- [ ] v1→v2 command/layout diff.
- [ ] v2→v3 VRF-ID introduction diff.
- [ ] v3→v4 marker 255→254 fork boundary.
- [ ] v4→v5 16→32-bit VRF ID diff.
- [ ] v5→v6 route-command consolidation diff.
- [ ] current FRR ZAPI beyond v6 and dataplane API separation.

## Number/registry archaeology

- [x] EtherType registry.
- [x] IP Protocol/Next Header registry.
- [x] service/port registry.
- [x] Assigned Numbers RFC snapshots → online IANA.
- [x] ASN 16→32-bit and private/documentation ranges.
- [x] IEEE OUI/MA-L/MA-M/MA-S.
- [x] IPv4 special-purpose/private/documentation/shared address spaces.
- [ ] `/etc/services` snapshot diffs against Assigned Numbers RFCs.
- [ ] `/etc/protocols` snapshot diffs.
- [ ] surviving historical values still compiled into kernels/dissectors.

## Packet-capture concordance

- [ ] create reproducible present-day capture fixtures for IPv4/TCP/UDP/ICMP/ARP/DNS/SMTP.
- [ ] annotate each byte/field with earliest recognizable standard ancestor.
- [ ] run period-appropriate tcpdump where surviving source builds permit it.
- [ ] compare modern dissector output with historical protocol diagrams.

## Rule

When a new excavation is proposed, add it here immediately. A chat message is not the task database. The repository is.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
