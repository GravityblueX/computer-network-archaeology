# ping and traceroute: operational tools assembled from existing protocol mechanisms

## Why operational-tool history belongs in the archive

Protocols describe mechanisms. Operators need tools that turn those mechanisms into questions a human can ask:

- is the host reachable?
- how long does the path take?
- where does the path stop?
- which gateway is returning an error?
- did routing change?

`ping` and `traceroute` are canonical examples. Neither required inventing a new routing protocol. Both combine existing IP/ICMP behavior with user-space measurement logic.

This is an important kind of lineage:

```text
existing protocol primitive
        +
operator/debugging need
        +
user-space implementation
        ↓
new operational tool
```

That is different from `revision-of`.

---

## 1. ICMP Echo existed before the `ping` program

RFC 792 (September 1981) defines ICMP Echo and Echo Reply messages.

Primary source:

- RFC 792 — https://www.rfc-editor.org/rfc/rfc792.html

The protocol mechanism therefore predates the famous Unix `ping` utility.

This distinction must be preserved:

```text
ICMP Echo message type
       ≠
Unix ping program
```

The program is an operational composition built on the protocol feature.

---

## 2. Mike Muuss: the direct participant account

Mike Muuss wrote a detailed retrospective titled *The Story of the PING Program*.

Primary/participant source:

- Mike Muuss, *The Story of the PING Program* — original BRL/ARL archival lineage, mirrored copy: https://wpollock.com/Networking/ping.html

Muuss says he wrote the Unix program and named it after the sound of sonar, because the echo-location analogy matched the mechanism.

His implementation sends timed ICMP `ECHO_REQUEST` messages and processes `ECHO_REPLY` responses to measure round-trip behavior.

The name and mechanism are therefore linked by direct author testimony, not later folklore.

---

## 3. The Fuzzball connection is an unusually concrete design lead

Muuss recalls that in July 1983, at a DARPA meeting in Norway, Dave Mills mentioned using ICMP Echo on his Fuzzball LSI-11 systems to measure path latency.

That remark later became relevant when Muuss encountered strange IP-network behavior at Ballistic Research Laboratory in December 1983.

The lineage is therefore:

```text
ICMP Echo protocol
      ↓
Dave Mills/Fuzzball latency-measurement practice
      ↓ participant testimony/inspiration
Muuss Unix ping implementation
```

This is strong participant-testimony evidence for inspiration, but it is not source-code descent unless code sharing is found.

Connect to existing Fuzzball archaeology.

---

## 4. ping was a debugging tool, not a general network monitor

The original practical question was whether the remote host/path was responding and what round-trip timing looked like.

A simplified measurement loop:

```text
record send time
     ↓
ICMP Echo Request
     ↓ network
remote ICMP Echo Reply
     ↓ network
record receive time
     ↓
RTT = receive - send
```

Repeated probes then expose:

- packet loss;
- latency distribution;
- intermittent reachability;
- route/path changes indirectly through RTT and response patterns.

Later implementations add many options. These should be tracked separately rather than projected into the original program.

---

## 5. raw sockets are implementation archaeology

Muuss's retrospective notes that the early Unix implementation used a raw ICMP socket on the 4.2BSD-era system.

This creates another history layer:

```text
ICMP protocol
     ↓
raw socket/kernel API
     ↓
ping user-space implementation
     ↓
privilege/security policy
```

Modern systems may use setuid binaries, capabilities, ping sockets or kernel mediation. Those are **operating-system security/interface lineages**, not changes to ICMP Echo itself.

---

# traceroute

## 6. Time To Live was not invented for traceroute

IP's TTL field existed as part of the datagram forwarding architecture. Routers/gateways decrement TTL; expiration generates ICMP Time Exceeded behavior.

Traceroute turns that ordinary failure/control mechanism into a path-discovery instrument.

Conceptually:

```text
probe with TTL = 1
  -> first gateway expires it
  -> ICMP Time Exceeded reveals hop 1

probe with TTL = 2
  -> second gateway reveals hop 2

probe with TTL = 3
  -> third gateway reveals hop 3

... repeat until destination behavior is reached
```

Again:

```text
IP TTL + ICMP Time Exceeded
      ≠
traceroute program
```

The latter is an operational composition of existing mechanisms.

---

## 7. Van Jacobson and the 1988 traceroute announcement

LBL's institutional history credits Van Jacobson with traceroute development, and an archived/reproduced December 20, 1988 announcement from Jacobson describes a “4BSD routing diagnostic tool” made available by FTP.

Sources:

- Lawrence Berkeley Lab computer-science history — https://cs.lbl.gov/about/history/
- reproduction of Van Jacobson's December 20, 1988 announcement — https://gist.github.com/thiteixeira/50cf5f9c26ca0216e4aa6d42b2440216

The announcement describes a tool sending three probes at each TTL and reporting responding gateways and round-trip times.

This is much better evidence than the vague modern statement “traceroute was invented in the 1980s.”

The original mailing-list archive/source file should still be recovered and registered directly.

---

## 8. Early traceroute needed kernel cooperation

Jacobson's announcement says the available 4BSD version required a small kernel change so a user process could control the IP TTL on raw output.

This is an excellent example of tool/software/API co-evolution:

```text
useful diagnostic algorithm
      ↓ blocked by kernel interface
small kernel/API change
      ↓
portable-ish user tool becomes possible
```

A mature artifact record should therefore include:

- traceroute user program;
- required BSD kernel patch/API;
- raw socket behavior;
- UDP/ICMP probe method by version;
- build/install instructions.

---

## 9. Why traceroute commonly used UDP probes

Classic Unix traceroute sends probes with increasing TTL values and expects ICMP Time Exceeded from intermediate routers, then a distinct terminal response from the destination.

The exact original evolution between possible ICMP-based experiments and the well-known UDP high-port implementation needs primary-source confirmation before being canonicalized.

Do not rely solely on later anecdotes.

The archive should recover:

- earliest source tarball;
- first announcement;
- comments in source explaining probe type choice;
- later ICMP/TCP traceroute variants.

---

## 10. ping and traceroute answer different questions

`ping` asks roughly:

```text
can I exchange Echo messages with this endpoint,
and what do those round trips look like?
```

`traceroute` asks roughly:

```text
which forwarding hops reveal themselves as TTL expires along the route?
```

Therefore:

```text
ping -> traceroute
```

is not a valid formal genealogy.

They are sibling operational tools assembled from overlapping ICMP/IP mechanisms.

---

## 11. The tools expose protocol behavior that networks may suppress

As firewalls, routers and security policy evolved, operators encountered:

- ICMP filtering;
- ICMP rate limiting;
- asymmetric paths;
- load balancing;
- MPLS/tunnels;
- NAT;
- routers that do not answer probes consistently.

Thus a diagnostic tool's observed output is not a literal map of all forwarding infrastructure.

The later history of “ping is blocked” and traceroute stars/timeouts belongs to firewall/operations archaeology.

---

## 12. Operator culture is part of the artifact

These tools became verbs:

- “ping the host”;
- “run traceroute.”

That linguistic survival reflects how deeply they entered operational practice.

Archive not just source and manuals but:

- command-line syntax by OS;
- packet formats generated;
- default probe counts/timeouts;
- privilege requirements;
- output formats;
- scripts/NOC procedures using the tools;
- vendor clones (`tracert`, router ping/traceroute commands, etc.).

---

## 13. Lineage rules

Safe:

```text
ICMP Echo
   -> substrate for Muuss ping

Fuzzball latency-measurement practice
   -> participant-reported inspiration for ping

IP TTL + ICMP Time Exceeded
   -> substrate for traceroute

4BSD kernel/raw-IP capability
   -> implementation dependency for early traceroute
```

Unsafe:

```text
ICMP -> ping as protocol revision             WRONG
ping -> traceroute upgrade                    WRONG
traceroute output = literal physical path     TOO SIMPLE
blocked ping = host down                      OPERATIONALLY FALSE
```

---

## 14. Sources

Primary/participant/institutional:

- RFC 792, *Internet Control Message Protocol* — https://www.rfc-editor.org/rfc/rfc792.html
- Mike Muuss, *The Story of the PING Program* — archival mirror https://wpollock.com/Networking/ping.html
- Mike Muuss/BRL historical materials — https://ftp.arl.army.mil/~mike/
- Lawrence Berkeley Lab history — https://cs.lbl.gov/about/history/
- Van Jacobson December 1988 traceroute announcement reproduction — https://gist.github.com/thiteixeira/50cf5f9c26ca0216e4aa6d42b2440216
- LBL Network Research Group archive — https://ftp.ee.lbl.gov/

---

## 15. Open excavation questions

1. Locate and checksum Muuss's earliest surviving ping source.
2. Identify exact 4.2a/4.2BSD kernel/socket environment used by the first ping build.
3. Recover Dave Mills' Fuzzball ICMP Echo measurement code or logs.
4. Recover Jacobson's original traceroute tarball and mailing-list message from a primary archive.
5. Diff early traceroute releases and kernel patches.
6. Trace Unix `traceroute`, Windows `tracert`, router-CLI implementations and ICMP/TCP variants separately.
7. Build an operational history of ICMP filtering/rate limiting and how it changed tool interpretation.

ping and traceroute are proof that **some of the Internet's most durable inventions were not new protocols at all, but clever ways of interrogating mechanisms that were already there.**
