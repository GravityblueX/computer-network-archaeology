# MNP → V.42 / V.42bis: Error Correction and Compression Move into the Modem

> A genealogy of reliable modem links, compatibility negotiation, and data compression above the modulation layer.

The familiar modem-speed ladder — 1200, 2400, 9600, 14.4k, 28.8k, 56k — is only one part of dial-up history.

Another lineage developed alongside modulation speed:

```text
raw modem link
    ↓
vendor error-control protocols
    ↓
Microcom Networking Protocol (MNP)
    ↓
CCITT V.42 standardized error correction
    ↓
CCITT/ITU-T V.42bis data compression
```

This lineage matters because a modem stopped being merely a signal converter. It increasingly became a **link processor** that could negotiate, frame, retransmit, compress, monitor, and adapt data before the host ever saw a byte.

---

## 1. The problem: a faster noisy link is still noisy

Telephone-network modem connections are vulnerable to:

- noise;
- phase/amplitude impairments;
- momentary dropouts;
- retrains;
- corrupted characters/blocks.

Without an error-control layer, reliability must be handled by the application or file-transfer protocol.

That works, but wastes duplicated logic and can perform badly when many applications assume the modem link itself is effectively clean.

The natural next step is therefore:

```text
DTE bytes
   ↓
modem-side framing / sequence / checksum / retry
   ↓
modulation
   ↓
telephone network
```

The modem becomes responsible for transforming an imperfect physical call into a more reliable logical data channel.

---

## 2. MNP as a vendor protocol family

Microcom's MNP — **Microcom Networking Protocol** — became an important pre-standard error-control family.

MNP is not one monolithic protocol version. Commercial documentation distinguishes classes with different capabilities.

Later modem manuals commonly summarize the widely interoperable error-control subset as **MNP Classes 2–4**, with MNP Class 5 adding compression.

A Telebit WorldBlazer/T3000 manual, for example, states that V.42 includes an alternate MNP procedure up to Class 4 for compatibility and separately describes MNP Class 5 compression.

That source is later than MNP's invention, so it is not sufficient for the original Microcom chronology. But it is strong deployed evidence that by the V.42 era MNP interoperability had become important enough to preserve inside products implementing the international standard.

Reference lead:

https://bitsavers.org/communications/telebit/90238-01_Modem_Reference_Manual_for_the_Telebit_T3000_and_WorldBlazer_Family_of_Products.pdf

The archive still needs original Microcom protocol manuals, patents, product announcements, and licensing documents for a primary MNP class genealogy.

---

## 3. V.42 standardizes error correction — but does not simply erase MNP

The first CCITT V.42 edition dates to **November 1988**.

ITU's recommendation database lists the revision history:

- V.42 (11/1988)
- V.42 (03/1993)
- V.42 (10/1996)
- V.42 (03/2002)

Canonical history page:

https://www.itu.int/rec/T-REC-V.42/en

V.42 specifies error-correcting procedures for duplex V-series DCEs accepting start-stop data from a DTE and transmitting synchronously.

Its central standardized protocol is **LAPM — Link Access Procedure for Modems**, an HDLC-derived link procedure.

Modern ITU summary:

https://www.itu.int/ITU-T/recommendations/rec.aspx?lang=en&rec=5692

Thus the cleanest standard lineage is:

```text
vendor error-control environment
        ↓ standardization pressure
V.42 LAPM
```

But deployed compatibility made the real world messier.

---

## 4. MNP survives inside the V.42-era interoperability world

Later modem implementation manuals explicitly describe V.42 products that support both:

- LAPM;
- alternate MNP error control for compatibility with existing MNP modems.

The Telebit manual phrases this directly: V.42 includes LAP-M as the main protocol and an alternate MNP procedure through Class 4.

This is a perfect example of a lineage edge that is **not**:

```text
MNP revision-of V.42
```

and not simply:

```text
V.42 replaced MNP and MNP disappeared
```

The more accurate historical relationship is:

```text
MNP installed base
      ↓ compatibility pressure
V.42-era modems preserve MNP fallback/interworking

while

LAPM becomes the standardized V.42 error-control procedure
```

The standard and the installed vendor protocol therefore coexist.

---

## 5. Error correction changes the host/modem boundary

With modem-side error correction, the DTE may send asynchronous characters while the modem internally:

- buffers data;
- constructs frames;
- performs sequence/error checking;
- retransmits damaged frames;
- negotiates optional procedures;
- converts to a synchronous error-controlled link.

The host therefore sees a stream that may be logically much cleaner than the underlying telephone line.

This creates new operational consequences:

- modem buffers introduce latency;
- host-to-modem serial speed can exceed line modulation rate;
- flow control becomes important;
- data compression can make instantaneous DTE throughput exceed raw line bit rate;
- applications measuring “baud rate” may misunderstand actual throughput.

The modem has become a protocol engine rather than a transparent analog boundary.

---

## 6. V.42bis: compression is a separate standard layer

V.42bis was approved **31 January 1990**.

ITU title:

> *Data compression procedures for data circuit-terminating equipment (DCE) using error correction procedures*

Canonical ITU page:

https://www.itu.int/rec/T-REC-V.42bis-199001-I/en

V.42bis should not be confused with V.42:

```text
V.42     = error-control procedures
V.42bis  = data-compression procedures used with error-control environments
```

The V.42bis specification includes:

- dictionary/string matching;
- changing codeword sizes;
- switching between compressed and transparent modes;
- reset/flush procedures.

ITU's publicly accessible PDF/table of contents provides the algorithmic structure.

This means that one modem connection may contain several conceptually separate layers:

```text
application bytes
      ↓
DTE serial flow control
      ↓
V.42bis compression
      ↓
V.42 LAPM / MNP error control
      ↓
modulation standard (V.32/V.34/etc.)
      ↓
telephone network
```

They are different genealogies even though commercial modem advertising often collapses them into one “speed” number.

---

## 7. MNP Class 5 and V.42bis must not be treated as the same algorithm

MNP Class 5 is associated with MNP-family compression.

V.42bis is an international standardized compression procedure.

A modem may support both families for interoperability.

Therefore the archive must model:

```text
MNP error control (classes 2–4)
MNP compression (class 5)
V.42 LAPM error control
V.42bis compression
```

as distinct artifacts/protocol roles.

The relationship is historical coexistence and competitive/compatibility standardization, not identity.

---

## 8. Compression can make “modem speed” misleading

Suppose the physical modem carrier is 14.4 kbit/s.

If highly compressible data is reduced significantly before transmission, the DTE may observe an effective application throughput greater than 14.4 kbit/s.

This explains why modem manuals often permit host serial rates such as 38.4 or 57.6 kbit/s over a slower line carrier.

The DTE–DCE interface, modem protocol processor, and physical modulation rate are no longer one number.

Historically, this is another reason the word **baud** became increasingly dangerous when used casually.

The archive should record separately:

- symbol rate;
- raw modulation bit rate;
- DTE serial port bit rate;
- compressed effective throughput;
- protocol overhead/retransmission rate.

---

## 9. V.42 revision history continues beyond dial-up's peak

ITU's development history shows that V.42 continued to change after its first 1988 issue.

The 2002 revision, for example, added support related to V.92 modem-on-hold behavior and references negotiation parameters for V.44 compression.

Thus:

```text
V.42 (1988)
  ↓ revision
V.42 (1993)
  ↓
V.42 (1996)
  ↓
V.42 (2002)
```

is a formal standards-revision lineage.

This should be kept separate from:

```text
MNP → V.42 compatibility/standardization history
```

which is not a formal revision chain.

---

## 10. What survives conceptually

The exact modem protocols are now largely historical, but the architecture remains familiar:

```text
unreliable transport medium
      ↓
link framing
      ↓
error detection
      ↓
retransmission
      ↓
negotiated capabilities
      ↓
optional compression
```

Those ideas appear throughout communications technology.

The correct historical claim is not “modern link protocols descend from MNP.”

Instead:

> modem history is a concrete, heavily deployed example of moving reliability, negotiation, and compression into an intermediate communications device.

Any direct influence on later unrelated technologies must be documented separately.

---

## 11. Lineage edges to preserve

High-confidence:

```text
MNP installed/error-control ecosystem
   └─ interworked-with / compatibility-preserved-by → V.42-era modem implementations

V.42 (1988)
   └─ revision-of → V.42 (1993) → V.42 (1996) → V.42 (2002)

V.42 error-controlled modem environment
   └─ complemented-by → V.42bis compression
```

Needs more primary Microcom evidence:

```text
MNP Class 2 → Class 3 → Class 4
MNP Class 4 → V.42 alternate procedure
MNP Class 5 ↔ V.42bis competitive/compatibility relationship
```

Do not call these formal revisions without the original documents.

---

## 12. Next excavation targets

- original Microcom MNP technical specifications;
- patents and licensing terms;
- exact Class 1–10 meanings by MNP revision;
- MNP frame formats and state machines;
- V.42 (1988) Annex A and original alternate-procedure wording;
- LAPM frame/state-machine reconstruction;
- modem negotiation traces showing LAPM↔MNP fallback;
- MNP5 versus V.42bis algorithm comparison;
- V.42bis dictionary/codeword parameters;
- modem buffer/flow-control interactions with RTS/CTS and XON/XOFF;
- product archaeology: Telebit, USRobotics, Hayes, Supra, ZyXEL, Multitech implementations;
- actual dial-up session captures where error control/compression mode can be identified;
- later V.44 branch and V.92 integration.

---

## Archaeological conclusion

The modem did not simply get faster.

It accumulated responsibilities.

A 1960s data set mainly translated between digital equipment and telephone facilities.

By the late 1980s/1990s a modem could also be:

- a negotiator;
- a reliable-link protocol endpoint;
- a retransmission engine;
- a flow-controlled buffer;
- a compression engine;
- a diagnostic device.

That is why the history of MNP, V.42 and V.42bis belongs beside modulation standards rather than beneath them as a footnote.
