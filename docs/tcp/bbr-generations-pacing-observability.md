# BBR genealogy: mainline BBR, delivery-rate infrastructure, pacing, and the separate BBRv3 development line

## BBR is not “CUBIC version 2”

BBR changes the primary signal and control model used by TCP congestion control.

Loss-based algorithms such as Reno/CUBIC traditionally interpret loss as a major congestion signal and evolve a congestion window around that feedback.

BBR instead builds an explicit model of:

```text
bottleneck bandwidth
+
round-trip propagation time
```

and primarily controls the **pacing rate**, with cwnd acting as a secondary bound related to estimated BDP.

This is a parallel congestion-control family, not a successor version of CUBIC.

## 1. Delivery-rate measurement lands as infrastructure

The mainline BBR history is inseparable from Linux's ACK-based delivery-rate sampling infrastructure.

The 2016 development series adds per-connection delivery tracking so TCP can estimate:

```text
packets/bytes delivered
      ÷
elapsed delivery interval
      =
delivery-rate sample
```

That measurement is useful beyond BBR and is later exported through `tcp_info`.

So the implementation graph includes:

```text
TCP ACK/delivery accounting
       ↓
delivery-rate sampling
       ↓
BBR bandwidth model
```

rather than one monolithic `tcp_bbr.c` invention.

## 2. Mainline BBR enters Linux in 2016

Commit:

```text
0f8782ea14974ce992618b55f0c041ef43ed0b78
```

adds `tcp_bbr.c` and describes BBR as Bottleneck Bandwidth and RTT congestion control.

The commit explicitly says BBR:

- estimates bottleneck bandwidth from ACK-derived delivery rates;
- keeps a minimum RTT estimate;
- uses pacing rate as the primary control;
- uses cwnd as a secondary multiple-of-BDP bound;
- has four modes:
  - STARTUP
  - DRAIN
  - PROBE_BW
  - PROBE_RTT;
- initially requires the `fq` qdisc with pacing enabled.

This is unusually rich implementation provenance because the commit message itself contains the control model.

## 3. Pacing is not a cosmetic output field

For BBR, pacing is architectural.

The original mainline commit says BBR without pacing does not function properly.

Therefore this lineage must connect:

```text
kernel packet pacing capability
        ↓
TCP pacing rate
        ↓
BBR model/controller
```

and not treat `pacing_rate` merely as something printed by `ss`.

## 4. `tcp_info` becomes a window into the BBR prerequisites

A 2014 Linux commit adds:

```text
tcpi_pacing_rate
tcpi_max_pacing_rate
```

to `struct tcp_info`, explicitly citing monitoring programs such as `ss`.

A 2016 commit adds:

```text
tcpi_delivery_rate
tcpi_delivery_rate_app_limited
```

This creates an operational chain:

```text
internal TCP rate/pacing state
       ↓ exported in TCP_INFO
ss -i / applications / diagnostics
```

The measurements BBR relies on therefore become observable outside the kernel.

## 5. Mainline BBR state machine remains recognizable in 2026

Current mainline `net/ipv4/tcp_bbr.c` still contains the classic mode set:

```text
STARTUP
DRAIN
PROBE_BW
PROBE_RTT
```

and the max-bandwidth/min-RTT model.

This is evidence that “BBR in Linux mainline” has a continuous implementation lineage from the 2016 merge.

That does not mean every internal constant or behavior is unchanged; there have been maintenance and integration changes.

## 6. Google BBRv3 is a separate development line

Google maintains a separate `google/bbr` repository/branch where `tcp_bbr.c` identifies:

```text
BBR_VERSION 3
```

and contains additional model bounds and control logic not present in the same form in the current mainline Linux file.

This creates a crucial negative-lineage rule as of August 2026:

```text
mainline Linux classic BBR lineage
        ≠
Google BBRv3 development branch
```

Do not say “Linux mainline now runs BBRv3” merely because Google has a v3 branch.

A future merge could change that state; the repository should date the claim.

## 7. BBR generations are not simple RFC revisions

Unlike CUBIC's mature RFC lineage, BBR's implementation generation names are primarily development/implementation labels.

Therefore preserve separately:

```text
mainline BBR merge and code revisions
Google BBRv2/v3 research/development branches
papers and deployment reports
future IETF documents, if any
```

Do not manufacture a standards-version ladder from code branch names.

## 8. Operational archaeology with `ss`

A live BBR connection can expose a mixture of:

```text
congestion-control name
pacing rate
cwnd
RTT / RTTVAR
min RTT (through newer fields/tools where surfaced)
delivery rate
app-limited indication
```

These fields come from different layers of Linux history:

- base TCP connection state;
- TCP_INFO expansion;
- pacing infrastructure;
- delivery-rate sampler;
- BBR-specific model/diag information.

This is why `ss -ti` is such a useful modern archaeological window.

## 9. Mainline BBR also exposes controller-specific diagnostic data

The BBR merge adds `INET_DIAG_BBRINFO` and a `tcp_bbr_info` structure containing values such as bandwidth estimate, minimum RTT, pacing gain and cwnd gain.

This is different from generic `TCP_INFO`:

```text
TCP_INFO
  = generic TCP connection telemetry

INET_DIAG_BBRINFO / TCP_CC_INFO style controller data
  = congestion-controller-specific telemetry
```

Again, different interfaces coexist rather than one replacing the other.

## 10. Root-hunting graph

```text
ACK/delivery accounting
       ↓
delivery-rate sampling
       ├── exported via TCP_INFO
       ↓
BBR bandwidth estimate
       + min RTT estimate
       ↓
pacing-primary controller
       ↓
mainline Linux BBR (2016→)

parallel development:
mainline BBR ──────┐
                   ├─ shared ancestry / research evolution
Google BBRv2/v3 ───┘
```

The final branch relation must be documented from source histories, not inferred from the common name alone.

## Primary anchors

- Linux commit `0f8782ea14974ce992618b55f0c041ef43ed0b78` — adds BBR.
- Linux commit `977cb0ecf82eb6d15562573c31edebf90db35163` — exports pacing rate through TCP_INFO.
- Linux commit `eb8329e0a04db0061f714f033b4454326ba147f4` — exports delivery rate/app-limited state.
- Current mainline `net/ipv4/tcp_bbr.c`.
- Google `google/bbr` `v3` branch `net/ipv4/tcp_bbr.c`.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
