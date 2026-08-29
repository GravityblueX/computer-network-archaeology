# Linux BIC to CUBIC: a real implementation succession inside one kernel tree

## Why this lineage is unusually strong

Many networking histories can only say that one design influenced another. Linux BIC→CUBIC is stronger: the source tree and commit history contain an explicit replacement/succession story.

The important chain is:

```text
BIC-TCP implementation
      ↓ new window-growth design
CUBIC 2.0 implementation
      ↓
CUBIC becomes Linux default
      ↓
implementation continues to evolve
```

This is implementation genealogy, not merely similarity.

## 1. BIC is present in the pre-CUBIC Linux tree

Linux `v2.6.13` contains `net/ipv4/tcp_bic.c` implementing Binary Increase Congestion Control.

The code identifies BIC as a high-speed TCP congestion-control algorithm and uses the pluggable Linux congestion-control framework.

At that stage the kernel's congestion-control menu contains Reno-compatible fallback behavior and BIC as a prominent high-speed option.

## 2. The decisive commit says “replace existing BIC version 1.1”

Commit:

```text
df3271f3361b61ce02da0026b4a53e63bc2720cb
```

is dated December 2005 / merged January 2006 and says:

```text
[TCP] BIC: CUBIC window growth (2.0)
```

The commit message explicitly says the existing BIC version 1.1 is replaced with version 2.0 and that the main change is replacing the window-growth function with the cubic function described by the CUBIC paper.

This is direct source-history evidence for:

```text
Linux BIC implementation
        ↓ revision/replacement of growth function
Linux CUBIC 2.0 implementation
```

The naming is transitional: the source still carries BIC terminology in structures/macros while the algorithm becomes CUBIC.

## 3. Early CUBIC is still visibly a BIC descendant

Early Linux CUBIC source contains names such as:

```text
struct bictcp
BICTCP_HZ
bictcp_update()
```

This is code-level sediment: the new algorithm lives inside identifiers inherited from the previous implementation generation.

The source comment also says that unless CUBIC is enabled and the congestion window is large, behavior remains compatible with original Reno-style behavior.

So one file can simultaneously contain:

- Reno compatibility assumptions;
- BIC implementation naming;
- CUBIC's new growth function.

## 4. January 2006: implementation refinement begins immediately

The early commit sequence includes:

- precomputation of CUBIC constants;
- replacement of the cube-root calculation with a faster Newton-Raphson implementation;
- later versions tuning friendliness, delayed-ACK estimation and slow-start behavior.

This is important because there is no frozen “CUBIC 2005 implementation.”

The Linux implementation becomes a continuously revised software artifact.

## 5. September 2006: CUBIC becomes the Linux default

Commit:

```text
597811ec167fa01c926a0957a91d9e39baa30e64
```

has the unambiguous message:

```text
[TCP]: make cubic the default
```

The diff changes:

```text
BIC default y → module
CUBIC module  → default y
DEFAULT_BIC   → DEFAULT_CUBIC
"bic"         → "cubic"
```

and the commit message explicitly calls CUBIC the successor to BIC with better properties over long-delay links.

This gives a clean operational transition:

```text
BIC available/default
      ↓
CUBIC code lands
      ↓ coexistence period
      ↓
CUBIC becomes default; BIC remains selectable
```

Again, “default changed” is not the same as “old code vanished.”

## 6. CUBIC itself keeps changing

A later commit:

```text
ae27e98a51526595837ab7498b23d6478a198960
```

updates Linux CUBIC to version 2.3 and integrates HyStart, adding ACK-train and delay-based slow-start exit detection.

The source citation is updated to a later CUBIC paper, and the internal state grows fields for round timing, RTT samples and HyStart detection.

So the implementation genealogy includes sub-generations:

```text
CUBIC 2.0
  ↓
algorithm/constant refinements
  ↓
CUBIC 2.x
  ↓
HyStart-integrated CUBIC 2.3
  ↓
modern Linux CUBIC revisions
```

## 7. Implementation version is not RFC version

Linux used and evolved CUBIC long before CUBIC became an IETF Standards Track RFC.

Therefore do not align:

```text
Linux CUBIC 2.0 == RFC 8312
Linux CUBIC 2.3 == RFC 9438
```

Those are different version spaces.

One is implementation history; the other is standards-document history.

## 8. A useful code-archaeology pattern

This lineage demonstrates several kinds of survival simultaneously:

```text
BIC code naming
    survives inside early CUBIC source

BIC algorithm
    replaced as Linux default

CUBIC implementation
    evolves before/after RFC publication

Reno compatibility behavior
    remains an underlying safety/friendliness reference
```

The kernel source is therefore a layered artifact rather than a clean rewrite.

## 9. Root-hunting conclusion

This is one of the repo's strongest `successor-of` examples because the evidence is direct:

```text
Linux BIC 1.1
     ↓ commit explicitly replaces growth function
CUBIC 2.0
     ↓ default switch
Linux default CUBIC
     ↓ continuing implementation revisions
modern tcp_cubic.c
```

The next separate question is how this long-running implementation lineage intersects with RFC 8312 and RFC 9438. That belongs to standards genealogy, not this code lineage.

## Primary anchors

- Linux `v2.6.13` `net/ipv4/tcp_bic.c`.
- Linux commit `df3271f3361b61ce02da0026b4a53e63bc2720cb` — CUBIC window growth 2.0.
- Linux commit `597811ec167fa01c926a0957a91d9e39baa30e64` — make CUBIC the default.
- Linux commit `ae27e98a51526595837ab7498b23d6478a198960` — CUBIC v2.3 / HyStart.
- Current `net/ipv4/tcp_cubic.c` for surviving implementation lineage.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
