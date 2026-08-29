# 2026-08-29 Linux Operations Root-Hunting Completion Pass

This batch was created to eliminate reminder-driven, one-topic-at-a-time work.

## Requested completion set

- [x] `ifconfig` / ioctl → rtnetlink → `ip addr` / `ip link`.
- [x] `/proc/net/tcp` history → tcp/inet/sock diag.
- [x] `ss -ti` TCP state/metric archaeology.
- [x] ARP + IPv6 ND/NUD → Linux neighbour subsystem → `ip neigh`.
- [x] Linux RPDB / multiple FIB tables / `ip rule`.
- [x] GNU Zebra / Quagga / FRR ZAPI v0–v6 diff.

## Narrative outputs

- `docs/methodology/root-hunting-master-worklist.md`
- `docs/software/ifconfig-ioctl-rtnetlink-ip-addr-link.md`
- `docs/operations/proc-net-tcp-to-inet-diag.md`
- `docs/operations/netstat-sockdiag-ss.md`
- `docs/operations/ss-ti-tcp-state-archaeology.md`
- `docs/software/arp-nd-linux-neighbour-ip-neigh.md`
- `docs/routing/linux-policy-routing-ip-rule-multiple-fib.md`
- `docs/lineage/zebra-protocol-version-genealogy.md`

## Structured frontier reserved for this batch

- Sources: `SRC-0222..SRC-0235`
- Artifacts: `ART-0214..ART-0224`
- Lineages: `LIN-0161..LIN-0176`

## Principal methodological findings

1. A command replacement can reflect a kernel-ABI replacement rather than merely a UI preference.
2. A protocol and its observability API have separate histories.
3. One modern kernel object can merge administration of multiple wire-protocol families without making those protocols ancestors of one another.
4. Policy routing adds a rule/table-selection layer around classic destination lookup.
5. Software forks can become visible as protocol bytes: FRR deliberately changed the ZAPI marker at the Quagga fork boundary.
6. A persistent repository worklist is now the task authority; chat reminders are not.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
