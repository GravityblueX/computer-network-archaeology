# TCP loss recovery genealogy: Tahoe, Reno, NewReno and SACK are not a version ladder

## Why the famous names are easy to misread

TCP history is often compressed into a sequence such as:

```text
Tahoe → Reno → NewReno → SACK
```

That picture is convenient and historically misleading.

These names refer to overlapping implementation generations and loss-recovery mechanisms. Some modify congestion-control response, some change fast-recovery behavior, and SACK adds receiver feedback that can be used by multiple congestion-control algorithms.

A better root-hunting question is:

> What information does the sender have after loss, and what does it do with cwnd while repairing the loss?

## 1. The shared Jacobson-era base

The congestion-collapse work of the late 1980s introduced a cluster of mechanisms that later standards describe as four intertwined algorithms:

```text
slow start
congestion avoidance
fast retransmit
fast recovery
```

RFC 5681 says these algorithms were developed in the Jacobson work and standardized through the TCP standards process.

But they did not all appear in BSD at exactly the same moment.

## 2. Tahoe: fast retransmit without Reno fast recovery

RFC 2001 preserves the key implementation provenance:

- **fast retransmit first appeared in 4.3BSD Tahoe**;
- **fast recovery first appeared later in 4.3BSD Reno**.

Tahoe therefore should not be defined as “Reno v1”.

A useful behavioral distinction after a loss detected by duplicate ACKs is:

```text
Tahoe-style generation
        ↓ fast retransmit missing segment
reduce congestion state
        ↓
return through slow-start behavior
```

The precise historical code/release matrix deserves source-level reconstruction, but the standard already proves that fast retransmit and fast recovery have separate implementation origins.

## 3. Reno: preserve the ACK clock during fast recovery

Reno adds the fast-recovery behavior that tries to avoid collapsing all the way back to slow start after a loss detected through duplicate ACKs.

The intuition recorded in later standards is that duplicate ACKs are evidence that later segments are still leaving the network and arriving at the receiver. Therefore the sender can preserve some estimate of packets in flight while repairing the missing segment.

The core Reno-era structure becomes:

```text
3 duplicate ACKs
      ↓
fast retransmit
      ↓
fast recovery
      ↓
new ACK covering recover point
      ↓
exit recovery
```

This works well for one loss in a window, but multiple losses expose a weakness.

## 4. Reno's multiple-loss problem

If several packets from one flight are lost, a cumulative ACK may acknowledge the retransmitted first loss while still leaving later holes.

Classic Reno can interpret that ACK as completion of recovery and leave fast recovery too early.

The result can be:

```text
multiple losses
      ↓
repair first hole
      ↓
exit recovery too early
      ↓
wait for more duplicate ACKs or RTO
```

This is the problem NewReno targets.

## 5. NewReno: partial ACKs become recovery signals

RFC 6582 standardizes the NewReno modification.

The critical semantic change is the treatment of a **partial ACK** during fast recovery.

If an ACK advances the cumulative acknowledgment but does not cover the recovery point, NewReno treats that as evidence that another segment in the same flight remains lost:

```text
partial ACK
    ↓
retransmit next unacknowledged segment
    ↓
stay in fast recovery
```

So NewReno is best represented as:

```text
Reno fast-recovery state machine
        ↓ modified partial-ACK behavior
NewReno recovery
```

not as a new TCP version.

## 6. SACK is a different axis: better information about holes

Selective Acknowledgment gives the sender information about non-contiguous data already received.

Instead of only knowing:

```text
all bytes < cumulative ACK arrived
```

SACK can report blocks such as:

```text
received: [1000,2000)
missing:  [2000,3000)
received: [3000,5000)
```

That changes the sender's information set.

RFC 6675 then specifies a conservative SACK-based loss-recovery algorithm that tracks which data is believed delivered, lost, retransmitted or still in flight.

This means SACK is not simply “NewReno's next version”.

A correct graph is closer to:

```text
                  cumulative-ACK recovery
                  /                  \
              Reno                NewReno
                                   partial-ACK repair

TCP option branch:
RFC 2018 SACK feedback
        ↓
SACK-aware loss-recovery algorithms
        ↓
RFC 6675 conservative SACK recovery
```

The branches interact, but they are not one version line.

## 7. Standards themselves preserve the distinction

RFC 5681 explicitly allows SACK-aware TCPs to use SACK information when interpreting duplicate acknowledgments and says alternate loss-recovery algorithms may be used if they follow congestion-control requirements.

RFC 6582 is specifically the **NewReno Modification to TCP's Fast Recovery Algorithm**.

RFC 6675 is specifically **A Conservative Loss Recovery Algorithm Based on Selective Acknowledgment**.

The titles alone reflect different responsibilities.

## 8. Why Linux/BSD implementation history needs another layer

The protocol genealogy above is not the same thing as a kernel version table.

A real implementation may contain:

- Reno-compatible cwnd behavior;
- NewReno partial-ACK logic;
- SACK scoreboards;
- DSACK;
- FACK/RACK-era later logic;
- pluggable congestion-control modules such as CUBIC or BBR.

Therefore a modern Linux TCP flow using CUBIC may still depend on SACK loss-recovery machinery whose ancestry is distinct from CUBIC's window-growth function.

That is why the archive keeps **congestion-control algorithm** and **loss-recovery mechanism** as separate dimensions.

## 9. Operational observability

Modern `ss -ti` can expose values such as:

```text
cubic / bbr / reno algorithm name
cwnd
ssthresh
retransmitted/lost state
SACK/Timestamp/Window Scale option status
```

Those values are descendants of several different historical branches.

Seeing:

```text
cubic ... sack ... cwnd:123
```

in one line does not mean CUBIC invented SACK or the congestion window.

It means multiple lineages meet in one live TCP control block.

## 10. Negative-lineage rules

Do not write:

```text
Tahoe → Reno → NewReno → SACK
```

Instead preserve:

- Tahoe fast-retransmit implementation provenance;
- Reno fast-recovery addition;
- NewReno partial-ACK modification to Reno recovery;
- SACK as a separate acknowledgment-information and loss-recovery branch;
- later congestion-control algorithms as another orthogonal branch.

## Evidence anchors

- RFC 2001, TCP Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery.
- RFC 5681, TCP Congestion Control: https://www.rfc-editor.org/info/rfc5681/
- RFC 6582, NewReno: https://www.rfc-editor.org/info/rfc6582/
- RFC 2018, TCP Selective Acknowledgment Options: https://www.rfc-editor.org/info/rfc2018/
- RFC 6675, SACK-based loss recovery: https://www.rfc-editor.org/info/rfc6675/

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
