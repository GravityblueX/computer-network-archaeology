# `ss -ti` as a live window into decades of TCP history

A modern `ss -ti` line can expose a remarkable collection of TCP state:

```text
rto
rtt / rttvar
mss
cwnd
ssthresh
pmtu
window scale
bytes_acked / bytes_received
segments in/out
pacing rate
congestion-control name
```

These values are not one historical generation.

## RTO: old requirement, new estimator generations

Retransmission timeout is foundational TCP state. RFC 6298 standardizes the modern RTO computation rules, while Linux exposes a current connection's RTO through socket diagnostics. The visible value is therefore an implementation state variable whose semantic ancestry reaches into TCP retransmission standards.

## RTT / variation

Round-trip measurement predates modern Linux, but estimator behavior changed over decades. `ss`'s `rtt:<rtt>/<rttvar>` exposes the living implementation's measurements, not a literal RFC field on the wire.

## `cwnd` and `ssthresh`

Congestion window and slow-start threshold belong to congestion-control algorithms, not the original fixed TCP header. RFC 5681 describes slow start/congestion avoidance concepts; Linux maintains corresponding internal per-connection state and `ss` can expose it.

That gives a useful root-hunting distinction:

```text
wire TCP header
   ≠
congestion-control state
   ≠
operator-visible diagnostic record
```

## MSS, PMTU and option history meet at one tool

MSS has a TCP option lineage; PMTU is an IP-path property; window scaling is another TCP option; `ss -i` can display all of them in one place. The command is therefore a **cross-layer archaeological viewport**.

## Linux-specific observability

Linux `TCP_INFO` and inet/sock diagnostic APIs turn internal connection state into a user-visible structure. A value printed by `ss` should not automatically be called an Internet-standard wire field. Some are standardized concepts, some are implementation metrics, and some are Linux-specific extensions.

## Why preserve this

A capture tells us what crossed the wire. `ss -ti` can tell us what the endpoint believed about that connection at the same moment.

Future repository fixtures should therefore pair:

```text
pcap
+
ss -ti snapshot
+
relevant sysctls/congestion-control module
+
route/PMTU state
```

This will make TCP history observable rather than merely textual.

Primary anchors:

- `ss(8)`: https://man7.org/linux/man-pages/man8/ss.8.html
- `tcp(7)`: https://man7.org/linux/man-pages/man7/tcp.7.html
- RFC 5681: https://www.rfc-editor.org/info/rfc5681/
- RFC 6298: https://www.rfc-editor.org/info/rfc6298/
