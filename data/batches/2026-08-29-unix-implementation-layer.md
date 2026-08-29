# 2026-08-29 Unix Implementation-Layer Root-Hunting Batch

Theme: trace global Internet number registries into concrete Unix data files, C APIs, runtime service activation, kernel/UAPI constants and packet-observability software.

## Narrative outputs

- `docs/software/bsd-services-protocols-databases.md`
- `docs/software/inetd-service-name-to-socket.md`
- `docs/software/kernel-protocol-constants.md`
- `docs/operations/tcpdump-bpf-libpcap-observability.md`

## Structured sources

- `SRC-0185` — BSD `services(5)` historical manual
- `SRC-0186` — BSD `protocols(5)` historical manual
- `SRC-0187` — 4.2BSD `tftpd.c`
- `SRC-0188` — 4.4BSD IPC/netdb documentation
- `SRC-0189` — FreeBSD inetd documentation
- `SRC-0190` — Linux UAPI `if_ether.h`
- `SRC-0191` — Linux UAPI `in.h`
- `SRC-0192` — McCanne/Jacobson 1993 BSD Packet Filter paper
- `SRC-0193` — libpcap source/README
- `SRC-0194` — tcpdump source repository

## Structured artifacts

- `ART-0186` — Unix `/etc/services`
- `ART-0187` — Unix `/etc/protocols`
- `ART-0188` — BSD netdb service/protocol lookup API family
- `ART-0189` — inetd super-server service activation
- `ART-0190` — Linux `ETH_P_*` UAPI constants
- `ART-0191` — Linux `IPPROTO_*` UAPI constants
- `ART-0192` — BSD Packet Filter packet-capture architecture
- `ART-0193` — libpcap portable capture API
- `ART-0194` — tcpdump analyzer/dissector lineage

## Structured lineages

- `LIN-0134` — Assigned Numbers → Unix local service/protocol databases
- `LIN-0135` — `/etc/services` → netdb service lookup API
- `LIN-0136` — `/etc/protocols` → netdb protocol lookup API
- `LIN-0137` — service database → inetd runtime activation
- `LIN-0138` — registry identities → Linux compile-time/UAPI constants
- `LIN-0139` — BPF architecture → libpcap filtering/capture abstraction
- `LIN-0140` — libpcap interface → tcpdump analyzer/dissector tool

## Principal findings

1. A globally assigned number becomes a Unix-local fact through more than one path: runtime databases such as `/etc/protocols` and compile-time constants such as `IPPROTO_TCP` are distinct projections of the same namespace.
2. `/etc/services` and `/etc/protocols` formats are documented as appearing in 4.2BSD.
3. 4.2BSD source demonstrates real `getservbyname()` use, not merely a later documentation convention.
4. inetd is an important junction where registry-derived service identities become listening sockets and process activation policy.
5. Modern Linux UAPI headers are living source-code museums containing protocol identities from PUP/X.25/ARP through IPv6/VLAN/MPLS/PPPoE/802.1X.
6. A source constant is not registry authority; provenance must be checked against IEEE/IANA.
7. BPF, libpcap and tcpdump are separate artifacts: capture filtering architecture, portable capture API and operator-facing analyzer/dissector.
8. A packet analyzer's ability to name a packet is itself a historical product of registries, OS constants and dissector code.

## Next targets

- exact 4.2BSD `/etc/services` and `/etc/protocols` file contents and Assigned Numbers diff;
- historical `getservent.c` / `getprotoent.c` implementations;
- NIS/NSS backend genealogy;
- earliest inetd source/manual and config grammar;
- early Linux/BSD `ETHERTYPE_*`, `ETH_P_*`, `IPPROTO_*` header diffs;
- oldest tcpdump/libpcap distributions and pre-BPF capture mechanisms;
- packet-capture artifacts pairing historical and current dissector output.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
