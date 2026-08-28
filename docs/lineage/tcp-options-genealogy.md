# TCP Options Genealogy: MSS, Window Scale, SACK, and Timestamps Living Beside a 1981 Core Header

TCP's base header is old, but TCP did not remain frozen. One of the most important reasons it could keep evolving is the Options area.

Modern TCP therefore looks like an archaeological layering system:

```text
1981 base header/state machine
        +
option mechanism
        +
MSS
        +
Window Scale
        +
SACK
        +
Timestamps
        +
later option families
```

The root-hunting question is not "Is TCP from 1981?" It is: **which parts of a modern SYN come from which decade?**

## 1. MSS: an early survivor

Maximum Segment Size is part of the classic TCP option lineage and is retained in the current TCP specification.

RFC 9293 still defines MSS as a TCP option usable on connection setup.

That means a modern SYN can carry an option whose conceptual job belongs to the earliest TCP interoperability problems: tell the peer the largest TCP segment the receiver is prepared to accept.

## 2. Window Scale: the 16-bit window became too small without changing the base field

The TCP header's Window field remained 16 bits.

High bandwidth-delay-product paths eventually made that insufficient for efficient use of large receive buffers.

The solution was not to redesign the base TCP header. Window Scale adds a negotiated exponent in a TCP option and changes how the old 16-bit Window field is interpreted after the handshake.

RFC 7323 describes the modernized Window Scale rules and explains that it expands the effective window while retaining the original Window field.

This is an excellent example of compatibility layering:

```text
old field remains 16 bits
        ↓
new option negotiated in SYN
        ↓
old field interpreted through scale factor
```

## 3. Timestamps: another option with two jobs

The TCP Timestamp option carries TSval and TSecr.

RFC 7323 describes two major uses:

- RTT measurement;
- PAWS, protection against wrapped sequence numbers.

Again, the base TCP sequence and ACK machinery remains. The option adds additional temporal state around it.

## 4. SACK: changing loss recovery without replacing ACK

Selective Acknowledgment adds information about non-contiguous blocks received by the peer.

Classic cumulative ACK behavior remains fundamental, but SACK allows a receiver to describe additional received ranges so a sender can recover more intelligently from multiple losses.

The coexistence is historically important:

```text
cumulative ACK core
      +
SACK extension
```

SACK did not replace TCP acknowledgments. It enriched the feedback channel.

## 5. Options turn the SYN into a capability-negotiation fossil bed

A modern TCP handshake often carries a compact history of protocol evolution:

```text
MSS
Window Scale
SACK Permitted
Timestamps
```

The SYN is therefore not merely opening a connection.

It is negotiating which historical extensions both endpoints understand.

This is similar in spirit to SMTP EHLO: an old core protocol survives because later capabilities can be advertised rather than assumed.

## 6. Unknown options and forward compatibility

TCP's option mechanism also depends on implementations not catastrophically failing when they see an unfamiliar option.

RFC 7323 discusses the historical concern that old implementations might mishandle options and notes later evidence that most modern implementations can safely handle unknown options.

This shows that extensibility is partly a social contract:

> future protocols survive only if old implementations are tolerant enough to let new syntax pass.

## 7. The base header stayed recognizable

The remarkable thing is that Window Scale, Timestamps, SACK and other extensions did not require TCPv2.

The familiar fields remain:

- source/destination ports;
- sequence number;
- acknowledgment number;
- flags;
- window;
- checksum;
- urgent pointer;
- options.

The Options field was the escape hatch that allowed the rest of the structure to survive.

## 8. An archaeological classification

### Base header

**Ancient and living.** Descends from RFC 793 and is consolidated in RFC 9293.

### MSS

**Ancient extension still living.** Current TCP continues to specify it.

### Window Scale

**Later performance extension, strongly living.** Negotiated in SYN.

### Timestamps

**Later performance/reliability extension, widely implemented.** Modern policy may vary.

### SACK

**Later loss-recovery extension, strongly living.** Adds information without replacing cumulative ACKs.

### Option namespace

**Living extension container.** The stable base header coexists with evolving option assignments.

## 9. Root-hunting from one SYN packet

A useful future museum exhibit is a single modern SYN decoded as strata:

```text
TCP ports                 old core
sequence number           old core
SYN flag                  old core
window                    old core
MSS                       early option lineage
Window Scale              high-performance extension
SACK Permitted            loss-recovery extension
Timestamps                high-performance/PAWS extension
```

One packet becomes a timeline.

## Sources

- RFC 9293 — Transmission Control Protocol: https://www.rfc-editor.org/info/rfc9293/
- RFC 7323 — TCP Extensions for High Performance: https://www.rfc-editor.org/info/rfc7323/
- RFC 2018 — TCP Selective Acknowledgment Options: https://www.rfc-editor.org/info/rfc2018/
- RFC 879 — The TCP Maximum Segment Size and Related Topics: https://www.rfc-editor.org/info/rfc879/

## Next excavation

- exact TCP option Kind-number registry history;
- RFC 793 option behavior versus RFC 9293;
- RFC 1323 → RFC 7323 field/state diff;
- SACK-permitted/SACK block implementation history;
- SYN packet captures across operating systems and decades;
- TCP Fast Open, MD5, AO, MPTCP and experimental option branches;
- option-space exhaustion and Extended Data Offset proposals.
