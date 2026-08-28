# TCP congestion: from tiny-packet pathology and Source Quench to packet conservation and slow start

## Why this lineage matters

TCP is often presented as though its modern congestion behavior was present in the 1981 protocol specification. It was not.

The modern Internet learned congestion control through operational failure, implementation experiments, gateway behavior, and successive algorithmic additions.

A useful archaeology separates several problems that later summaries often collapse:

```text
small interactive packets / excessive overhead
            ↓
Nagle-style sender behavior

network overload / dropped packets / duplicate retransmissions
            ↓
early Source Quench thinking
            ↓
real Internet congestion collapse
            ↓
Jacobson/Karels transport algorithms
            ↓
slow start + congestion avoidance + improved RTT/RTO behavior
```

These are related, but they are not one protocol revision.

---

## 1. TCP's specification was not enough to guarantee good network behavior

RFC 896, John Nagle's January 1984 memo *Congestion Control in IP/TCP Internetworks*, is explicit that many TCP implementations behaved badly under internetwork congestion even though they implemented the protocol.

Primary source:

- RFC 896 — https://www.rfc-editor.org/rfc/rfc896.html

This distinction is foundational:

```text
TCP wire/state specification
        ≠
transport implementation behavior under load
```

The Internet could have compliant-looking hosts whose local retransmission and packet-generation decisions collectively destabilized the network.

That is why implementation history belongs beside protocol history.

---

## 2. Congestion collapse: adding buffers can make the collapse later, not eliminate it

RFC 896 describes an overload condition in which gateways drop packets, hosts retransmit, duplicate traffic consumes capacity, round-trip time rises, and useful throughput can fall drastically.

Nagle explicitly warns that adding more gateway memory does not solve the fundamental problem. More buffering may increase delay and postpone drops while allowing an even larger fraction of carried traffic to become redundant retransmissions.

The loop is conceptually:

```text
load rises
   ↓
queueing delay rises
   ↓
transport times out
   ↓
retransmits packets still in network
   ↓
more load / more queueing
   ↓
more timeout and loss
   ↓
useful throughput collapses
```

This is one of the clearest early descriptions of why **more buffering is not equivalent to congestion control**.

---

## 3. The small-packet problem is a separate pathology

RFC 896 discusses interactive TCP sending single keyboard characters as packets with roughly one byte of useful data plus around forty bytes of protocol headers in the historical IPv4/TCP case.

That overhead is tolerable on a lightly loaded network but harmful on congested paths.

Nagle notes earlier packet-coalescing traditions in:

- Tymnet;
- NCP Telnet;
- X.25 PADs;
- TCP Telnet.

This is important lineage evidence: the problem of delaying/coalescing interactive characters predates modern TCP's familiar sender rule.

The historical family is not:

```text
Nagle invented packet coalescing from nothing
```

but:

```text
older interactive-network packet-delay practice
              ↓
TCP-specific adaptive problem
              ↓
Nagle sender rule
```

Direct influence between every named system still requires source-by-source evidence.

---

## 4. The Nagle rule solves a local packet-generation problem

RFC 896 proposes a remarkably small implementation rule: if previously transmitted data remains unacknowledged, inhibit sending additional new small segments until an acknowledgment arrives or enough data accumulates.

The essential effect is:

```text
new small application write
      |
      +-- no unacknowledged data -> can send
      |
      +-- data already unacknowledged -> hold/coalesce
```

The rule adapts to the actual network/connection acknowledgment cadence rather than using one fixed character-delay timer.

This mechanism later becomes known as the **Nagle algorithm**, but the archive should preserve the original operational problem and memo context rather than reducing it to a socket checkbox like `TCP_NODELAY`.

### What it does not solve

It is not a complete network congestion-control algorithm.

It addresses excessive tiny-packet generation. The later Jacobson congestion-control work addresses a broader problem: how a TCP sender should discover and respect available network capacity under congestion.

---

## 5. Source Quench was once part of the imagined congestion-control toolbox

RFC 896 then discusses general congestion control through ICMP Source Quench.

The historical idea was roughly:

```text
gateway becomes congested
       ↓
ICMP Source Quench
       ↓
source reduces sending pressure
```

Nagle describes engineering choices about when switching nodes should send Source Quench and argues for reacting before total buffer exhaustion.

This is valuable precisely because Source Quench later became obsolete.

Do not write history backward as though TCP always used only end-host loss inference and never contemplated explicit ICMP congestion signaling.

The death of Source Quench deserves its own protocol/deprecation lineage.

---

## 6. RFC 970: even an infinite-buffer switch can still be congested

Nagle's RFC 970 (December 1985), *On Packet Switches With Infinite Storage*, attacks another common misconception: congestion is not merely “running out of memory.”

Primary source:

- RFC 970 — https://www.rfc-editor.org/rfc/rfc970.html

A hypothetical datagram switch with infinite buffer space can still suffer unacceptable queue growth and pathological throughput behavior under overload.

The memo reframes part of the problem around **packet scheduling and system behavior**, not buffer quantity alone.

This forms an important conceptual branch toward later queueing/fairness/AQM history, though direct ancestry must be documented rather than guessed.

---

## 7. October 1986: operational collapse becomes impossible to ignore

Van Jacobson's later accounts describe a dramatic congestion episode in October 1986. Throughput between Lawrence Berkeley Laboratory and UC Berkeley — geographically very close sites but separated by several network hops — reportedly fell by roughly three orders of magnitude.

The important point is not the anecdote alone. The episode motivated examination of 4.3BSD TCP behavior under severe congestion.

The 1988 SIGCOMM paper by Van Jacobson and Michael Karels states that severe Internet congestion problems were common and that much of the cause lay in **transport protocol implementations rather than the protocol specifications themselves**.

Primary/participant source:

- Van Jacobson, Michael J. Karels, *Congestion Avoidance and Control*, SIGCOMM 1988 — https://ee.lbl.gov/www/papers/congavoid.pdf

---

## 8. Packet conservation becomes the organizing principle

Jacobson's paper frames network stability around a **conservation of packets** idea: once a connection is running in stable equilibrium, a new packet should not be injected until an old packet has left the network.

This leads to several implementation mechanisms intended to make TCP approach that behavior despite uncertain path capacity and round-trip time.

The paper discusses or motivates algorithms including:

- improved round-trip-time variance estimation;
- exponential retransmission timer backoff;
- slow start;
- congestion avoidance / dynamic window adjustment;
- receiver ACK behavior;
- interaction with Karn-style retransmission measurement rules;
- later fast-retransmit work in the same implementation lineage.

The archive must separate which algorithm appears in which paper/source/release rather than retroactively calling all of them “TCP Reno.”

---

## 9. Slow start solves the “starting with no clock” problem

A new TCP connection does not yet have a self-clocking stream of returning acknowledgments that accurately reflects path capacity.

If it immediately emits a full advertised window, it may inject a large burst into a narrow path.

Slow start introduces a congestion window (`cwnd`) that begins small and grows as acknowledgments demonstrate that packets are leaving the network.

Conceptually:

```text
connection begins
    ↓
small cwnd
    ↓ ACKs return
increase allowed outstanding data
    ↓
ACK clock develops
    ↓
transition toward congestion avoidance
```

This is a transport implementation mechanism layered on top of the existing TCP protocol state machine.

That distinction matters historically: **the wire protocol can remain recognizable while sender algorithms change enormously.**

---

## 10. Congestion avoidance turns loss/feedback into capacity inference

After initial ramp-up, a sender needs to avoid repeatedly overflowing bottlenecks.

Jacobson's work formalizes a congestion window separate from the receiver's advertised flow-control window.

This creates two distinct limits:

```text
receiver window
   -> how much the receiver can accept

congestion window
   -> how much the network is estimated to tolerate
```

The effective sending window is constrained by both.

This is one of the most important conceptual splits in TCP history.

Flow control and congestion control are not the same thing.

---

## 11. RTT/RTO estimation is part of congestion history

A sender that estimates round-trip time badly can retransmit too early, creating duplicates and additional congestion.

So Jacobson/Karels work on RTT variance and retransmission timeout is not merely a timer cleanup. It is part of making the sender stable in a network whose delays expand under load.

The historical coupling is:

```text
queueing/congestion changes delay
       ↓
measured RTT distribution changes
       ↓
RTO must adapt
       ↓
bad estimator -> spurious retransmits -> more load
```

Again, an implementation detail becomes network-wide behavior.

---

## 12. BSD source is part of the standard's real history

The algorithms entered the world not only as papers, but as code changes in Berkeley TCP implementations and then spread through widely used Unix-derived stacks.

A mature excavation must therefore connect:

```text
paper / algorithm description
      ↓
4BSD TCP source revision
      ↓
beta deployment / measurement
      ↓
other vendor/OS ports
      ↓
later RFC standardization and refinements
```

This is where protocol archaeology becomes software archaeology.

Future work should recover exact SCCS/source revisions corresponding to Jacobson/Karels changes rather than saying vaguely “BSD added congestion control.”

---

## 13. Do not collapse Nagle and Jacobson into one congestion-control invention

The safe model is:

```text
small interactive-packet pathology
      ↓
Nagle sender coalescing behavior

and separately

network congestion collapse / retransmission instability
      ↓
Jacobson/Karels congestion-control algorithms
```

They interact in real TCP implementations, but they solve different problems.

Likewise:

```text
ICMP Source Quench
```

is a historical congestion-feedback branch, not an ancestor that can be directly renamed `cwnd`.

---

## 14. Later descendants

The Jacobson-era branch leads toward many later algorithms and RFCs:

- Tahoe;
- Reno;
- NewReno;
- SACK-related recovery;
- Vegas;
- CUBIC;
- BBR;
- ECN;
- Active Queue Management and RED/CoDel branches.

These should become separate lineages.

Do not make a single linear ladder. Congestion control becomes a family tree with competing sender and queue algorithms.

---

## 15. Sources

Primary/contemporary:

- John Nagle, RFC 896, *Congestion Control in IP/TCP Internetworks*, January 1984 — https://www.rfc-editor.org/rfc/rfc896.html
- John Nagle, RFC 970, *On Packet Switches With Infinite Storage*, December 1985 — https://www.rfc-editor.org/rfc/rfc970.html
- Van Jacobson and Michael J. Karels, *Congestion Avoidance and Control*, SIGCOMM 1988 — https://ee.lbl.gov/www/papers/congavoid.pdf
- LBL Network Research Group papers archive — https://ee.lbl.gov/www/nrg-papers.html

Related:

- RFC 792 ICMP for historical Source Quench context;
- Phil Karn's retransmission-timer work;
- BSD source trees and SCCS history to be promoted as source artifacts.

---

## 16. Open excavation questions

1. Locate the exact 4BSD source revisions where each Jacobson/Karels algorithm first appears.
2. Separate slow start, congestion avoidance, RTT variance estimation, exponential backoff, fast retransmit and Karn interactions by date/source.
3. Recover LBL/NRG email discussions and test results from 1986–1990.
4. Trace TCP_NODELAY and application interaction with the Nagle algorithm.
5. Reconstruct Source Quench implementation and deprecation history.
6. Build Tahoe/Reno/NewReno branch records from source and RFCs.
7. Connect host congestion control to gateway queue management without inventing a single direct lineage.

The modern TCP sender is not simply the 1981 protocol implemented faithfully. It is **the sediment of multiple Internet failures, measurements, algorithms and source-code revisions layered onto a stable protocol skeleton.**
