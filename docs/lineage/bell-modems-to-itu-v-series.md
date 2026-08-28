# Modem Lineage: Bell data sets, international V-series standards, and the voiceband speed ladder

A modern summary often reduces modem history to a sequence of speeds:

```text
300 → 1200 → 2400 → 9600 → 14.4k → 28.8k → 33.6k → 56k
```

That is useful as a mnemonic and terrible as history.

The actual lineage is a changing combination of:

- national/vendor data-set families;
- international CCITT/ITU-T recommendations;
- DTE/DCE interface standards;
- modulation methods;
- duplex arrangements;
- call setup and answer procedures;
- error correction and compression;
- characteristics of the public switched telephone network;
- eventual exploitation of the telephone network's internal digital sections.

This file is an initial map. It intentionally avoids claiming that every ITU V-series modem is a direct descendant of a specific Bell product.

## 1. Bell data sets established a practical computer/telephone boundary

Bell System data sets are important not only because of their bit rates, but because they made the boundary between digital terminal/computer equipment and telephone-network transmission into a concrete product interface.

The archival project is already tracking:

- Bell Data Set 101 family;
- Bell Data Set 103 family;
- Bell 202 family;
- Bell 303 wideband family;
- DTE/DCE serial-interface standardization around EIA RS-232;
- automatic calling/answering equipment;
- dial-up versus private-line engineering.

The 101/103 chronology remains partly disputed and must not be flattened into a clean modern timeline until Bell System Practices, technical-journal articles, tariffs and product announcements are reconciled.

## 2. V.21: international 300-bit/s duplex voiceband modem standardization

ITU-T still catalogs Recommendation V.21 as:

> 300 bits per second duplex modem standardized for use in the general switched telephone network.

This makes V.21 an important international-standard artifact in the same speed/use class as early low-speed dial modems.

But this repository should **not** write:

```text
Bell 103 → became V.21
```

unless standards-committee or engineering records establish a direct design/standardization relationship.

The defensible relationship today is:

```text
Bell 103-class national/vendor practice
            ↘
             300-bit/s dial modem ecosystem
            ↗
CCITT V.21 international standard family
```

They are historically comparable and interoperable only under specific modulation/interface compatibility conditions that need exact primary-source verification.

## 3. V.22: 1200-bit/s duplex operation

ITU describes V.22 as a 1200 bit/s duplex modem for the general switched telephone network and point-to-point two-wire leased telephone-type circuits.

This is a major step in modem genealogy because increasing speed on ordinary voiceband circuits was no longer just a matter of changing clock rate.

Higher-rate generations increasingly depended on more sophisticated modulation, equalization, training and line adaptation.

The archive should therefore track, for every modem recommendation:

- nominal data signaling rates;
- symbol rate / baud where applicable;
- modulation constellation or frequency plan;
- duplex method;
- fallback rates;
- equalizer behavior;
- training sequence;
- carrier detection;
- scrambler;
- DTE interface assumptions;
- PSTN/leased-line assumptions.

## 4. V.22bis: 2400 bit/s and an explicit `bis` branch

V.22bis standardized 2400 bit/s duplex operation using frequency-division techniques for switched and leased two-wire circuits.

The suffix matters.

A `bis` recommendation should not be treated as merely an editorial revision. In many telecommunications standards families it can represent a substantive extension or enhanced variant.

For lineage data this should be recorded as an explicit relationship with the exact property delta, not inferred from the name alone.

## 5. V.32: full-duplex 9600 bit/s on two-wire telephone circuits

ITU records the first V.32 edition as October 1984 and describes it as a family of two-wire duplex modems up to 9600 bit/s for the PSTN and leased telephone-type circuits.

This is an especially important transition because high-speed duplex communication over ordinary two-wire telephone infrastructure requires sophisticated signal processing compared with early frequency-separated low-speed modem pairs.

A proper excavation of V.32 should recover:

- echo-cancellation architecture;
- constellation and modulation details;
- training procedures;
- rate negotiation/fallback;
- line probing/equalization;
- implementation chipsets;
- first commercial products;
- relationship to proprietary pre-standard 9600-bit/s systems.

## 6. V.32bis: 14,400 bit/s

Recommendation V.32bis was approved 22 February 1991 and specifies duplex modem operation up to 14,400 bit/s.

By this period, modem standards increasingly describe a negotiated adaptive signal-processing system rather than a simple fixed pair of tones.

That distinction is historically important: a 1990s modem is not merely a faster Bell 103.

The artifact category stayed recognizably "modem", but the amount of algorithmic behavior inside the box increased enormously.

## 7. V.34: 28.8k, then 33.6k

ITU's edition history is itself a useful lineage record:

- V.34 (09/1994): up to 28,800 bit/s;
- V.34 (10/1996): up to 33,600 bit/s;
- later consolidated edition (02/1998): up to 33,600 bit/s.

This demonstrates why the repository must attach behavior to an **edition**, not just to the recommendation name `V.34`.

A sentence such as "V.34 is 33.6k" is wrong for the first V.34 edition.

## 8. V.90: the asymmetry comes from the network itself

V.90, approved in September 1998, is historically different from the earlier symmetrical mental model of "two analog modems talking through an analog phone network".

ITU describes a pair consisting of:

- a **digital modem**;
- an **analogue modem**;

with up to 56,000 bit/s downstream and up to 33,600 bit/s upstream.

This architecture exploits the fact that much of the PSTN had become digital internally. The downstream path could avoid one analog-to-digital conversion under suitable conditions.

So the lineage is not simply:

```text
V.34 + better modulation = V.90
```

It includes a transformation of the carrier network beneath the modem:

```text
mostly analog voice-network assumptions
              ↓
voice network with digital switching/transmission core
              ↓
customer analog loop + provider digital modem
              ↓
56k downstream architecture
```

This is an excellent example of infrastructure changing a protocol/device standard from below.

## 9. Interface lineage runs beside modulation lineage

The modem's telephone-side signaling is only half of the historical object.

The terminal/computer side has its own genealogy:

```text
teleprinter/control circuits
        ↓
DTE/DCE conventions
        ↓
EIA RS-232 revisions
        ↔ CCITT V.24/V.28 family
        ↓
DB-25 serial modem practice
        ↓
smaller PC serial connectors / UART ecosystems
        ↓
internal modems / bus devices / software-visible virtual serial ports
```

The archive should keep these lineages separate because they evolve for different reasons.

A V.32 modem can inherit an RS-232-style DTE boundary without inheriting the modulation of a Bell 103.

## 10. Automatic calling and answering are another branch

Dial modems are not complete if the history records only carrier modulation.

A usable unattended modem service also needs:

- call origination;
- answer detection;
- ringing response;
- dialing mechanisms;
- call-progress detection;
- hangup;
- echo-control interaction;
- terminal/modem command/control.

CCITT/ITU V.25 addresses automatic answering and general procedures for automatic calling equipment.

Later commercial modem command languages — especially the Hayes `AT` command ecosystem — deserve a separate lineage from the line-modulation standards.

The eventual user-visible stack often looked like:

```text
communications software
        ↓
AT-command/control interface
        ↓
modem data pump / error correction / compression
        ↓
V-series line modulation
        ↓
analog subscriber loop
        ↓
PSTN switching/transmission infrastructure
```

Each layer has its own standards and product history.

## 11. Error correction and compression are not identical to line modulation

By the late dial-up era, marketed modem throughput could involve several different mechanisms:

- physical line signaling rate;
- modem-level error correction;
- retransmission;
- compression;
- DTE serial-port rate higher than the actual line rate.

This is why historical advertisements claiming, for example, an effective throughput above the raw carrier rate need to be recorded as marketing/performance claims with exact conditions.

MNP and ITU V.42/V.42bis belong to a parallel error-control/compression genealogy and should be excavated separately.

## 12. Standards genealogy should not erase vendor wars

Between formal recommendation generations, vendors frequently shipped:

- proprietary high-speed modes;
- draft-standard implementations;
- incompatible 9600/14.4/28.8k protocols;
- firmware upgrades after standards stabilized.

The modem market therefore needs both:

```text
formal V-series lineage
```

and

```text
actual product compatibility lineage
```

They will not always match neatly.

## 13. Initial lineage map

```text
Bell / national data-set practice
        ↘
         voiceband modem ecosystem
        ↗
CCITT/ITU V-series standardization

V.21       300 bit/s duplex
  ↓ rate/technology generations (not simple revisions)
V.22      1200 bit/s duplex
  ↓
V.22bis   2400 bit/s duplex
  ↓
V.32      up to 9600 bit/s (1984 first edition)
  ↓
V.32bis   up to 14,400 bit/s (1991)
  ↓
V.34      28,800 (1994) → 33,600 (1996)
  ↓ infrastructure-dependent architectural change
V.90      56k downstream / 33.6k upstream (1998)
```

The downward arrows above mean "successive mainstream voiceband modem generations" unless an exact revision/supersession relation is documented. They must not automatically be encoded as `revision-of`.

## 14. What survived

Even after dial-up Internet disappeared from most daily use, modem-era concepts survive in unexpected places:

- DTE/DCE terminology and interface thinking;
- explicit training/negotiation phases in physical communication systems;
- adaptive equalization;
- fallback rates;
- link-quality estimation;
- layered separation between terminal control and carrier signaling;
- the distinction between raw signaling rate and effective application throughput.

The specific analog PSTN modem may be obsolete; much of its engineering vocabulary is not.

## 15. High-priority excavation queue

1. Bell 101A/B/C and Bell 103A/F exact BSP/announcement genealogy.
2. Bell 103 versus V.21 modulation-frequency and compatibility comparison from primary standards.
3. Bell 202 versus V.23 relationship — documented design influence versus merely similar asymmetric service class.
4. Original CCITT V.21/V.22/V.22bis edition dates, not only later consolidated ITU pages.
5. V.32 (1984) full physical-layer/training/state-machine reconstruction.
6. V.32bis commercial chipset/product adoption.
7. V.34 1994 → 1996 clause-level differences.
8. V.90 architecture and why the 56k path depends on a digital provider-side endpoint.
9. V.92 and later dial-up improvements.
10. MNP → V.42 / V.42bis error correction/compression genealogy.
11. Hayes AT command lineage and de facto standardization.
12. UART/RS-232 PC serial-port bottlenecks and high DTE-rate practice.
13. Real ISP modem-bank archaeology: Total Control, Ascend, PRI/T1, digital modems.

The modem is an ideal archaeological object because its history is the history of **two infrastructures meeting**: computers on one side and the telephone network on the other.
