# BBN 1822: the Host–IMP interface as physical machinery

> Status: active excavation. This chapter focuses on the **electrical and handshake boundary** between an ARPANET host and an IMP. It deliberately avoids reducing 1822 to “an early link-layer protocol.” Report 1822 described wires, signal sequencing, readiness, timing, local/distant variants, host leaders, and failure behavior. Those details mattered because ARPANET hosts had incompatible word lengths and I/O architectures.

## 1. What 1822 actually solved

The ARPANET could not assume a uniform host bus, byte size, operating system, or peripheral interface. In the late 1960s participating machines included 16-, 24-, 32-, and 36-bit families and machines with very different channel architectures.

BBN therefore standardized a boundary at the IMP:

```text
host-native I/O system
        ↓
site-specific interface hardware
        ↓
===============================
       BBN 1822 boundary
  bit-serial + handshake + ready
===============================
        ↓
IMP host interface hardware
        ↓
IMP buffers/software
```

RFC 3109, written when 1822 was finally moved to Historic status, summarizes the essential design: the Host/IMP hardware interface was **bit-serial and asynchronous**, specifically so that it did not depend on a universal 8-bit byte or host word length.

## 2. 1822 was not RS-232

A recurring modern mistake is to see “serial interface” and mentally substitute RS-232.

That is wrong.

The classic 1822 Host–IMP interface used a custom set of data and handshake signals. It moved one bit at a time, with explicit signaling that a bit was available and that the receiver was ready for the next bit.

The interface therefore belongs conceptually closer to a **hardware handshake protocol** than to a simple asynchronous character serial port.

## 3. Core handshake: one bit is a transaction

The surviving 1822 text describes paired signals with wonderfully literal names. In the Host→IMP direction the sequence includes concepts such as:

- `Host-to-IMP Data Line`
- `There's-Your-Host-Bit`
- `Ready-For-Next-Host-Bit`
- `Last-Host-Bit`

The opposite direction mirrors the same idea with IMP→Host equivalents.

Conceptually:

```text
sender places DATA bit
        ↓
sender asserts THERE'S-YOUR-BIT
        ↓
receiver accepts bit
        ↓
receiver drops READY-FOR-NEXT-BIT
        ↓
sender withdraws THERE'S-YOUR-BIT / advances
        ↓
receiver reasserts READY-FOR-NEXT-BIT
        ↓
next bit
```

The important property is not a globally fixed bit clock. The ordering of events is primary.

This made the boundary tolerant of hosts with very different internal speeds and word sizes.

## 4. Asynchronous here means handshake sequencing, not start/stop characters

Report 1822's use of *asynchronous* must not be confused with modern colloquial “async serial” meaning start bit + character + stop bit.

The 1822 interface was asynchronous because the two sides coordinated each bit through request/accept-style signal transitions rather than sharing a continuous character clock.

A recovered 1973 revision says the interface emphasized **ordering rather than precise timing**. It nevertheless imposed minimum visible pulse times and internal delays so that the receiving side could reliably observe transitions.

The document gives examples of much shorter minimum transitions for a Local Host than a Distant Host, reflecting the analog realities of cable length and interface circuitry.

## 5. Local Host and Distant Host were physically different variants

Historical discussions identify at least three attachment concepts:

### Local Host (LH)

For a nearby host and IMP. Later technical summaries describe the local form as using comparatively direct logic-level signaling over paired conductors.

### Distant Host (DH)

For a host farther away from the IMP. The logical handshake remained similar, but the electrical layer used differential/isolated signaling suitable for a longer cable and ground-potential differences.

### Very Distant Host (VDH)

VDH should **not** be treated as merely a longer 1822 cable. It was a different solution using synchronous line/modem techniques to attach a remote host over telecommunications facilities.

These must become separate artifact records because their cabling, interface electronics, timing, and operational failure modes differ substantially.

## 6. Ready lines were part of machine health, not merely flow control

The interface included **Host Ready** and **IMP Ready** concepts. These were not simply packet-window signals.

The 1973 Report 1822 text describes relay contacts and readiness interrogation. If a machine lost power, crashed, or otherwise could no longer maintain its ready state, the other side could detect that condition.

On the IMP side, readiness was tied to a **watchdog timer**. Software periodically serviced the watchdog; if it failed to do so, the ready relay could open and recovery behavior could begin.

Thus the Host–IMP cable carried evidence about machine liveness.

This is an early example of how networking hardware entangled:

- data transport;
- flow sequencing;
- crash detection;
- recovery state;
- operator diagnostics.

## 7. RFC 642 shows how implementation ambiguity became an operational problem

By 1974, the ARPA community had implemented enough different Host–IMP interfaces that BBN engineer Jerry Burchfiel described the situation as one of widespread confusion over ready-line behavior.

RFC 642, *Ready Line Philosophy and Implementation*, was written as a practical “cookbook” for interface implementors. Its goals included:

1. reliable resynchronization after either side lost state;
2. simpler host-interface software;
3. predictable response to ready-line transitions.

This is historically revealing. A protocol specification does not automatically produce interoperability. **Electrical and state-machine conventions still had to be learned, clarified, and standardized through operational experience.**

## 8. Arbitrary host word length was a design requirement

RFC 3109 explicitly emphasizes that when the interface was designed, ARPANET could not rely on an industry-wide 8-bit-byte machine model. Host machines had diverse word lengths.

1822 therefore moved a bit stream across the boundary and let site-specific hardware translate to/from the host's natural word or channel format.

This is why an ARPANET “host interface” was a significant engineering project at each early site.

Examples to excavate separately:

- UCLA Sigma 7 interface (Mike Wingfield);
- SRI SDS 940 interface;
- UCSB IBM 360/75 interface;
- Utah PDP-10 interface;
- later DEC PDP-11 local-host interfaces;
- ACC commercial 1822 interface boards;
- Xerox Alto 1822 interface designed by Larry Stewart.

## 9. The interface and the message protocol are different layers

The physical handshake moved bits. Above that, Report 1822 also defined the IMP/Host message access format: leaders, destination/source information, message types, and control indications.

The archaeology must preserve this distinction:

```text
1822 electrical handshake
        ↓
1822 bit stream / message boundary
        ↓
IMP-Host leader and control messages
        ↓
ARPANET host-to-host protocol (NCP era)
        ↓
applications
```

Conflating all of these as “the 1822 protocol” obscures both hardware and software evolution.

## 10. Leaders changed over time

The IMP–Host leader format was revised repeatedly as ARPANET expanded and new functions were added.

RFC 660 (1974) documents changes to the IMP and Host interface including:

- decoupling message-number sequences;
- access-control changes;
- expanding the message-number window;
- messages outside the normal numbering mechanism.

Later 1822L extended addressing as the network outgrew earlier assumptions.

Therefore there is no single timeless “1822 header.” Any packet diagram in this repository should be labeled by revision/date.

## 11. Very Distant Host changes prove the interface was a living system

RFC 547 (1973) exists specifically to replace portions of the Very Distant Host specification in Report 1822. This is a useful warning against treating technical manuals as static monuments.

A complete document genealogy should track:

- initial 1969 Host–IMP design reports;
- early Report 1822 editions;
- 1973 revisions;
- March 1974 revision;
- October 1974 interface changes;
- December 1975 revision referenced by RFC 745;
- January 1976 revision;
- later 1822L additions;
- eventual Historic status in RFC 3109 (2001).

## 12. JANUS: 1822's asymmetry became visible when people tried to reuse it

RFC 745 (1978) designed the **JANUS** interface for packet-radio work as a symmetrical “1822-like” interface.

Its motivation is especially valuable as historical evidence: engineers wanted to reuse the 1822 style between arbitrary devices, but the original Host–IMP standard was not actually fully symmetric. Parts of it were Host-specific and IMP-specific.

JANUS therefore reworked those assumptions and based its distant electrical characteristics on **EIA RS-422**, compatible with MIL-188-114.

This gives us a clear lineage:

```text
1822 Host ↔ IMP interface
        ↓ lessons / reuse pressure
1822-like device interfaces
        ↓
JANUS symmetrical interface
```

## 13. Physical signal inventory: excavation target

The full pin-by-pin signal list must be captured from a clean Report 1822 scan. The 1973 text already exposes categories such as:

### readiness / liveness
- IMP Master Ready
- IMP Ready Test
- Host Master Ready
- Host Ready Test

### Host → IMP data transfer
- Host-to-IMP Data
- There's-Your-Host-Bit
- Ready-For-Next-Host-Bit
- Last-Host-Bit

### IMP → Host data transfer
- corresponding IMP data, bit-available, ready-for-next-bit, and last-bit signals

### additional conductors
- grounds / return paths;
- local vs distant electrical conditioning;
- test/control lines depending on revision.

A final hardware record must include the exact connector type, conductor count, signal names, active polarity, voltage ranges, source/sink limits, cable length limits, and local/distant schematics.

## 14. Timing details matter

The recovered 1973 text includes concrete timing constraints, including:

- minimum on/off visibility requirements;
- different minima for Local vs Distant Host circuitry;
- an IMP delay after `There's-Your-Host-Bit` before sampling data/Last-Bit;
- a corresponding setup interval before the IMP asserts its bit-available signal.

These values should be transcribed into a revision-specific table only after the scan is page-verified. The important point at this stage is that 1822 was **not timing-free**; it was an asynchronous handshake with bounded analog/electrical behavior.

## 15. Why commercial interface boards appeared

At first, each host organization could face a custom engineering project. As ARPANET grew, vendors such as ACC and DEC produced standard interface hardware for popular minicomputers.

That transition should be cataloged as its own history:

```text
1969: one-off site interfaces
        ↓
1970s: repeated designs / community conventions
        ↓
commercial 1822 interface boards
        ↓
router/network-interface products with standardized buses
```

It is a small but important piece of the larger transition from research prototype to networking industry.

## 16. Failure archaeology

A mature reconstruction should document what happened for each fault:

| Fault | Expected evidence / reaction |
|---|---|
| host loses power | Host Ready drops/open contact |
| IMP software wedges | watchdog affects IMP Ready / recovery |
| cable removed | ready state should fail safely |
| message transmission interrupted | both sides must discard/resynchronize partial state |
| receiver buffer unavailable | bit-level readiness can stall transfer |
| interface signal stuck | diagnostics / ready-line cookbook becomes relevant |

The exact state transitions vary by Report 1822 revision and host implementation; do not universalize a later cookbook backward without evidence.

## 17. What this means for modern readers

A modern Ethernet NIC + PCIe bus hides most of this boundary engineering. In 1969, the network's edge was visibly a hardware protocol negotiated one bit at a time.

This makes 1822 historically important for a reason deeper than “it came before Ethernet”:

> It standardized **the machine/network boundary** in a world where computers themselves were not standardized.

## 18. Open excavation checklist

1. Obtain the earliest surviving 1969 Report 1822 or predecessor specification, not merely 1975/76.
2. Produce a revision table for every known Report 1822 edition.
3. Transcribe local-host pinout and electrical values from scan images.
4. Transcribe distant-host pinout and differential/isolation circuit details.
5. Separate VDH completely and reconstruct its modem/framing path.
6. Recover photographs of original 1822 connectors/cables.
7. Record physical cable type, maximum lengths, and grounding recommendations.
8. Catalog site-built interfaces by host model.
9. Catalog commercial ACC/DEC/etc. 1822 interface boards.
10. Recover host driver source code to show how electrical events became buffers and interrupts.
11. Compare Report 1822 state machine to JANUS and later packet-radio interfaces.
12. Record surviving 1822 hardware specimens and provenance.

## Sources

- BBN Report 1822 scan index (January 1976 revision available): https://www.bitsavers.org/pdf/bbn/imp/
- RFC 3109, *Request to Move STD 39 to Historic Status* (2001): https://www.rfc-editor.org/rfc/rfc3109.html
- RFC 642, *Ready Line Philosophy and Implementation* (1974): https://www.rfc-editor.org/rfc/rfc642.html
- RFC 660, *Some Changes to the IMP and the IMP/Host Interface* (1974): https://www.rfc-editor.org/rfc/rfc660.html
- RFC 547, *Change to the Very Distant Host Specification* (1973): https://www.rfc-editor.org/rfc/rfc547.html
- RFC 745, *JANUS Interface Specifications* (1978): https://www.rfc-editor.org/rfc/rfc745.html
- Computer History Wiki, `1822 interface`, useful as a discovery map for local/distant signal families: https://gunkies.org/wiki/1822_interface

The RFCs are stronger evidence for operational clarifications than later summaries; the Report 1822 scans remain the authoritative target for the physical specification itself.
