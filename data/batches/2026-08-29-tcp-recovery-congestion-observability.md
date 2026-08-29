# 2026-08-29 TCP recovery, congestion-control and observability roots

This batch follows the persistent root-hunting worklist and separates four historical subgraphs that are often collapsed into one vague “TCP evolution” story:

1. **loss recovery** — Tahoe fast retransmit, Reno fast recovery, NewReno partial-ACK handling, SACK feedback and RFC 6675 SACK-based recovery;
2. **high-BDP congestion control** — Linux BIC → CUBIC implementation genealogy, distinct from CUBIC's later RFC standardization clock;
3. **model-based congestion control** — mainline BBR and the separately identified Google BBRv3 development branch, with pacing/delivery-rate observability;
4. **operations and memory** — live per-socket `TCP_INFO`/`ss` state versus destination-keyed cross-connection `tcp_metrics`/`ip tcp_metrics` memory.

## Narrative documents

- `docs/tcp/tcp-tahoe-reno-newreno-sack-recovery.md`
- `docs/tcp/linux-bic-cubic-implementation-genealogy.md`
- `docs/tcp/cubic-paper-linux-rfc-standardization.md`
- `docs/tcp/bbr-generations-pacing-observability.md`
- `docs/tcp/linux-tcp-info-field-genealogy.md`
- `docs/tcp/tcp-metrics-cache-ip-tcp-metrics.md`

## Structured ranges

- artifacts: `ART-0234..0248`
- sources: `SRC-0248..0268`
- lineages: `LIN-0188..0200`

## High-confidence findings

- RFC 2001 records fast retransmit as first appearing in 4.3BSD Tahoe and fast recovery as first appearing in 4.3BSD Reno.
- NewReno modifies Reno fast recovery; SACK is a parallel feedback/recovery branch, not “the TCP version after NewReno”.
- Linux CUBIC has direct code ancestry from BIC: the CUBIC 2.0 commit explicitly replaces/reworks the BIC 1.1 growth function, and a later 2006 commit changes the Linux default from BIC to CUBIC.
- Linux CUBIC deployment predates RFC 8312 by roughly a decade; RFC 9438 is a later Standards Track specification, not the original source of the Linux implementation.
- BBR entered mainline Linux in 2016 as a bandwidth/RTT model with pacing as its primary control and cwnd as a secondary BDP bound.
- As reviewed on 2026-08-29, current torvalds/linux BBR and the Google `bbr` v3 branch must be kept distinct; the latter explicitly declares `BBR_VERSION 3`.
- `struct tcp_info` is a growing observability ABI: an early v2.6.12 snapshot already exports RTO/RTT/MSS/cwnd/ssthresh/retransmission/path state, with pacing fields added in 2014 and delivery-rate/app-limited fields in 2016.
- In 2012 Linux moved learned dynamic TCP metrics out of route metrics into a dedicated cache; Generic Netlink and `ip tcp_metrics` expose that cross-connection destination memory operationally.
- Live `TCP_INFO`/`ss -ti` state and remembered `tcp_metrics` state are different state planes and are explicitly modeled as such.

## Deliberately unresolved provenance

The batch does **not** manufacture precision where primary evidence is still missing. Follow-up work remains for:

- period 4.3BSD Tahoe/Reno source snapshots and function-level diff;
- exact early NewReno implementation adoption;
- full Linux SACK scoreboard/recovery code genealogy through PRR/RACK;
- exact BBRv1→v2→v3 development chronology;
- exact pre-git `TCP_INFO` introduction patch and exhaustive every-field release matrix;
- pre-2012 TCP route-metrics ancestry and exact first iproute2 release carrying `ip tcp_metrics`;
- reproducible packet capture + synchronous `ss -ti` concordance experiments.

Research and drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
