# CUBIC standardization: deployed Linux algorithm first, RFC family later

## The chronology runs opposite to a textbook standards-first story

CUBIC is a good example of a protocol/algorithm becoming widely deployed before the IETF standardization lineage catches up.

A naive diagram would be:

```text
RFC defines CUBIC
      ↓
Linux implements it
```

The historical direction is closer to:

```text
BIC research + Linux implementation
      ↓
CUBIC paper / Linux CUBIC
      ↓
large-scale operating-system deployment
      ↓
RFC 8312 Experimental specification
      ↓
implementation experience + research
      ↓
RFC 9438 Standards Track
```

## 1. Linux implementation predates the RFC lineage by years

Linux mainline received the CUBIC growth-function implementation in the 2005/2006 development period and made CUBIC the default in 2006.

That is more than a decade before RFC 8312.

The Linux code also continued changing—constants, friendliness behavior, HyStart integration and many later fixes—during that interval.

Therefore “CUBIC” already referred to a living implementation family long before it referred to an IETF RFC.

## 2. RFC 8312 documents an already-deployed algorithm

RFC 8312, published in 2018 as Experimental, describes CUBIC after extensive real-world deployment.

It is not the birth certificate for the Linux implementation.

Its value in the genealogy is instead:

```text
research/implementation experience
       ↓
IETF specification snapshot
```

This is a `standardizes` / `documents deployed design` relationship, not a source-code revision relationship.

## 3. RFC 9438 makes the deployment-before-standardization story explicit

RFC 9438, published August 2023, obsoletes RFC 8312 and moves CUBIC to the Standards Track.

Its abstract says CUBIC had been adopted as the default congestion-control algorithm by Linux, Windows and Apple stacks.

It also says the new specification incorporates improvements based on implementations and recent academic work and that extensive deployment experience justifies movement to Standards Track.

So the standards history is explicitly informed by the implementation history:

```text
real code + deployment
       ↓ evidence / experience
updated normative specification
```

## 4. RFC 9438 also updates RFC 5681

CUBIC's standardization is not merely a self-contained algorithm document.

RFC 9438 updates RFC 5681 because CUBIC can be more aggressive than the Reno-style congestion-avoidance behavior traditionally used as the baseline.

That creates two interacting standards lineages:

```text
TCP base congestion-control requirements
RFC 5681
       ↑ updated by
RFC 9438 CUBIC
```

and:

```text
RFC 8312 CUBIC
       ↓ obsoleted by
RFC 9438 CUBIC
```

These are different relations.

## 5. Linux implementation versions must not be mapped one-to-one to RFC revisions

The kernel has its own revision history:

```text
BIC 1.1
CUBIC 2.0
CUBIC 2.x
CUBIC 2.3 + HyStart
later mainline revisions
```

The IETF has a different document history:

```text
RFC 8312
    ↓
RFC 9438
```

There is no evidence-bearing reason to identify a Linux internal “2.3” with a particular RFC generation.

The correct model is many-to-many:

```text
research papers ─┐
Linux code ──────┼→ RFC specification work
other stacks ────┤
operational data ┘

RFC clarifications/improvements
       ↓
future implementations
```

## 6. “Standardization” can follow deployment

This matters beyond CUBIC.

Technology genealogy needs at least three clocks:

1. **idea/publication clock** — when a paper/design is published;
2. **implementation/deployment clock** — when code ships and becomes operational;
3. **standards clock** — when an IETF/IEEE/ITU document reaches a particular status.

CUBIC demonstrates that these clocks can be separated by many years.

## 7. Why this matters for reading Linux source

If a kernel version from 2008 says `cubic`, it is not “implementing RFC 9438 early”.

It is implementing the then-current CUBIC design lineage that later standards reconstruct and refine.

Historical language should therefore be time-correct:

```text
2006 Linux: CUBIC implementation based on contemporary CUBIC design/paper
2018: RFC 8312 documents CUBIC as Experimental
2023: RFC 9438 updates specification and moves it to Standards Track
```

## 8. Root-hunting graph

```text
BIC-TCP research / Linux BIC
          ↓ design revision
CUBIC paper + Linux CUBIC
          ↓
large deployment and code evolution
          ↓
RFC 8312 (Experimental)
          ↓ formal RFC revision + implementation feedback
RFC 9438 (Standards Track)
          ↓
modern standard CUBIC lineage
```

Alongside:

```text
Linux CUBIC code history ────────────────┐
Windows/Apple implementations ───────────┼→ deployment evidence / implementation feedback
academic work ───────────────────────────┘
```

## 9. Negative claims

Do not state:

- Linux first got CUBIC from RFC 8312;
- RFC 9438 is identical to the original CUBIC paper;
- Linux CUBIC version numbers are RFC version numbers;
- Standards Track status proves the algorithm was not deployed before 2023.

All four reverse the actual historical relationships.

## Evidence anchors

- Linux CUBIC implementation commits documented in `linux-bic-cubic-implementation-genealogy.md`.
- RFC 8312: https://www.rfc-editor.org/info/rfc8312/
- RFC 9438: https://www.rfc-editor.org/info/rfc9438/
- RFC 5681: https://www.rfc-editor.org/info/rfc5681/

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
