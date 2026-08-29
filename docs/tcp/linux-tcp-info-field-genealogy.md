# Linux `TCP_INFO` field genealogy: a stable socket option that keeps absorbing new implementation state

## Why `TCP_INFO` is a living fossil container

Linux exposes TCP connection state through the `TCP_INFO` socket option and `struct tcp_info`.

The API is long-lived, but the structure is not frozen. Fields have accumulated as the TCP implementation learned new concepts and as operators demanded more visibility.

This creates the same pattern seen in DNS RR types or Netlink attributes:

```text
stable container/interface
       ↓
new fields appended over time
       ↓
modern tooling can observe decades of accumulated TCP state
```

## 1. The interface exists by the Linux 2.4 generation

Current `tcp(7)` documents `TCP_INFO` as available since Linux 2.4.

The exact pre-git introduction commit should still be recovered from historical kernel archives, but by Linux `v2.6.12` the structure is already mature and recognizable.

That snapshot contains:

```text
state
congestion-control state
retransmits / probes / backoff
negotiated option flags + window scales
RTO / ATO
send/receive MSS
unacked / sacked / lost / retrans / fackets
last send/receive/ACK times
PMTU
receive ssthresh
RTT / RTTVAR
send ssthresh
send cwnd
advertised MSS
reordering
receive RTT / receive space
total retransmits
```

So by 2005, `TCP_INFO` is already much more than “connection state”. It is an operational window into timers, loss recovery, path state and congestion control.

## 2. The early structure directly exposes multiple historical lineages

A single old `tcp_info` already combines descendants of:

```text
RFC 793 connection state
Jacobson-era RTO/RTT logic
RFC 5681-style cwnd/ssthresh concepts
SACK accounting
Window Scale/Timestamps/ECN negotiation
PMTU discovery/path state
Linux internal CA-state machine
```

This is why a `struct` field table can itself be treated as an archaeological layer.

## 3. The ABI grows by appending observability

Linux generally extends the structure with new fields rather than replacing the socket option with `TCP_INFO2`.

That allows applications to request a buffer size and learn as much as the running kernel knows/supports.

The survivorship pattern is:

```text
old program asks for old-sized tcp_info
        ↓
still works

new program asks for larger structure
        ↓
receives additional fields
```

The details of getsockopt length handling should be tracked by kernel release, but the long-lived public structure clearly grows incrementally.

## 4. 2014: pacing becomes observable

Commit:

```text
977cb0ecf82eb6d15562573c31edebf90db35163
```

adds:

```text
tcpi_pacing_rate
tcpi_max_pacing_rate
```

The commit message explicitly says these fields are for monitoring applications such as `ss` and even includes an `ss -i` example.

This is strong lineage evidence:

```text
internal socket pacing state
       ↓
TCP_INFO UAPI
       ↓
ss/operator visibility
```

## 5. Mid-2010s: byte/segment/min-RTT/notsent counters accumulate

The structure later gains fields such as:

```text
bytes_acked
bytes_received
segs_in / segs_out
min_rtt
notsent_bytes
data_segs_in / data_segs_out
```

Each field exists because a previously internal quantity becomes useful to applications or diagnostics.

The important point is not merely the growing struct size. It is the movement of knowledge across the kernel/user boundary.

## 6. 2016: delivery-rate sampling becomes public telemetry

Commit:

```text
eb8329e0a04db0061f714f033b4454326ba147f4
```

adds:

```text
tcpi_delivery_rate
tcpi_delivery_rate_app_limited
```

The commit explains that the delivery-rate value represents recently measured goodput and that the app-limited bit indicates whether the measurement was constrained by lack of application data.

The same delivery-rate infrastructure is crucial for BBR.

So a kernel-internal algorithm prerequisite becomes a generic application-visible metric.

## 7. Generic TCP_INFO versus controller-specific information

Linux also grows `TCP_CC_INFO` / inet_diag controller-specific mechanisms.

That means there are now two observability layers:

```text
TCP_INFO
  generic connection/path/timing/congestion telemetry

TCP_CC_INFO / controller-specific diag
  algorithm-specific state such as DCTCP/BBR details
```

These interfaces coexist.

A modern `ss` output can merge information from several kernel sources into one human-readable line.

## 8. Why field genealogy matters for `ss` archaeology

When a modern operator sees:

```text
rtt:...
rto:...
cwnd:...
ssthresh:...
pacing_rate ...
delivery_rate ...
```

those tokens entered the user-visible world at different times.

Therefore `ss -ti` should be read as a composite timeline:

```text
1980s TCP control concepts
   +
1990s options/recovery concepts
   +
2000s Linux TCP_INFO base
   +
2010s pacing/rate/byte counters
   +
controller-specific modern diagnostics
```

## 9. Field-level versioning is better than “TCP_INFO since Linux 2.4”

The statement “TCP_INFO exists since Linux 2.4” is only the root.

A complete genealogy needs a matrix:

| Generation | Example exposed knowledge |
|---|---|
| Linux 2.4 / early 2.6 | state, timers, RTT, cwnd, ssthresh, SACK/loss counters, PMTU |
| 2014 | pacing/max pacing rate |
| 2015-era | bytes and segment counts, other extended accounting |
| 2016 | minimum RTT/notsent/delivery-rate and app-limited visibility |
| later | additional busy/rwnd/sndbuf/delivery/reordering/ACK-compression style metrics |

The exact commit for every current field remains a useful machine-generated future task.

## 10. Negative claims

Do not infer:

- every `TCP_INFO` value appears on the wire;
- all fields come from one RFC;
- `ss` owns the measurements;
- BBR invented delivery-rate observability;
- a current `tcp_info` struct describes Linux 2.4 exactly.

The socket option is the container; the fields have separate roots.

## Primary anchors

- `tcp(7)` for the Linux 2.4 availability statement.
- Linux `v2.6.12` `include/linux/tcp.h` for an early source snapshot.
- Linux commit `977cb0ecf82eb6d15562573c31edebf90db35163` — pacing fields.
- Linux commit `eb8329e0a04db0061f714f033b4454326ba147f4` — delivery-rate fields.
- current `include/uapi/linux/tcp.h` for the modern structure.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
