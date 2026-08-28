# Bell Data Sets → DTE/DCE → RS-232 / V.24: Excavating the Serial Interface Boundary

The familiar serial-port story is usually told backward from the DB-25 connector or the name **RS-232**.

That hides the older engineering problem.

Before a computer could “have an RS-232 port,” telephone carriers and equipment makers already needed a clean boundary between:

- a teleprinter, business machine, terminal, or computer;
- a modem/data set;
- the telephone network or leased facility behind it.

This chapter excavates that boundary as a technical lineage.

It also records an unresolved Bell 101/103 chronology problem rather than forcing the surviving Bell System documents into a clean modern product timeline.

---

## 1. Start with the boundary, not the connector

A period installation can be abstracted as:

```text
terminal / business machine / computer
              |
       digital data + control
              |
       customer/data interface
              |
       Bell System data set
              |
 modulation / demodulation / control
              |
      telephone or leased facility
```

The data set was not merely a box that converted ones and zeroes into tones.

It could also participate in:

- call setup;
- automatic answering;
- ready/busy state;
- originate/answer mode;
- timing;
- loopback/testing;
- interface-level control;
- telephone-network compatibility.

Once different manufacturers supplied the terminal/computer and data-set sides, the interchange boundary became a standardization problem.

That is the environment in which the EIA RS-232 family matters.

---

## 2. The Bell 101 family is not yet a clean one-line chronology

Popular histories often reduce the story to:

```text
1958/1959 Bell 101 → 1962/1963 Bell 103
```

The archive should resist publishing that as a fully resolved product genealogy.

### Evidence that does survive

A surviving Bell System Practice for **Data Set 101C** is identified in collector/archive references as:

- *Data Set 101C — Identification and Operation*;
- Issue 2;
- March 1963.

Separate test/trouble sections survive from later dates.

The 101 family is associated with low-speed frequency-shift data transmission and teleprinter/data-service environments. The exact A/B/C revision tree, announcement dates, service deployment and SAGE/commercial relationship still need primary-document reconstruction.

### Why “101 = first modem, 1958” is not enough

A historical statement can refer to several different milestones:

- experimental design;
- military/SAGE use;
- Bell Labs publication;
- AT&T product announcement;
- tariff/service availability;
- first commercial customer deployment;
- later model-family standardization.

These are different claims and should be recorded separately.

See the existing source-conflict excavation:

[`../modems/bell-101-103-source-conflict.md`](../modems/bell-101-103-source-conflict.md)

---

## 3. The 103A document contains a metadata problem worth preserving

A surviving Bell System Practice scan for **Data Set 103A Type — Identification and Operation**, Section 591-014-100, contains a striking internal conflict.

The text visible in the scan says:

- **Issue 5, January 1961**;
- AT&TCo Standard;
- Data Set 103A type;
- designed for simultaneous low-speed serial transmission/reception up to **300 baud** in DATA-PHONE service over the voice message switched network;
- up to **150 baud** in TWX service.

The same first page carries:

- **© American Telephone and Telegraph Company, 1967**.

The archived filename itself is commonly labeled `Jan67`.

Primary access:

https://bitsavers.org/communications/westernElectric/modems/591-014-100_Data_Set_103A_Identification_and_Operation_Jan67.pdf

### What this does and does not establish

It establishes that the surviving scan contains contradictory-looking date metadata.

It does **not** by itself establish that:

- 103A was operational in January 1961;
- “1961” is definitely a typo;
- the entire document was first issued in 1967;
- the issue numbering was reset or carried over from another section.

The correct archaeological response is to preserve the conflict and search for:

1. Issue 1–4 of Section 591-014-100;
2. Bell System Practice master indexes from 1960–1967;
3. tariff/service records;
4. product announcements;
5. manufacturing-change notices;
6. surviving equipment with dated Western Electric components/nameplates.

Do not repair the date silently.

---

## 4. A 1962 Bell System Technical Journal article proves 103A already existed as a technical object

A 1962 *Bell System Technical Journal* article on asynchronous frequency-shift modulators reports measurements on existing Bell System DATA-PHONE **Data Sets 101A, 103A and 202A**.

That is important because it anchors 103A in a contemporary Bell technical publication by 1962.

Source:

https://www.worldradiohistory.com/Archive-Bell-System-Technical-Journal/60s/Bell-System-Technical-Journal-1962-6-Complete.pdf

The article discusses experimental/theoretical jitter measurements and explicitly names these data-set families.

This is stronger evidence than a modern timeline sentence because it is contemporary technical literature.

### Current cautious chronology statement

At this stage the archive can safely say:

> Data Set 103A was an existing Bell System technical object by 1962; a surviving later Bell System Practice identifies the 103A type as a full-duplex low-speed DATA-PHONE/TWX data set capable of up to 300 baud in DATA-PHONE service; the precise issue/product/service chronology remains unresolved because surviving BSP metadata conflict.

That is less tidy than “introduced in 1962,” but more defensible.

---

## 5. 103A1 and 103A2 must be split, not hidden under one model name

The surviving 103A Practice distinguishes at least 103A subtypes.

The document identifies **103A1** for specific TWX/customer-provided business-machine/computer-terminal arrangements.

The model suffix therefore matters historically.

Future records should split:

```text
103A family
  ├── 103A1
  ├── 103A2
  └── other documented variants/revisions
```

and record for each:

- service environment;
- terminal type;
- originate/answer behavior;
- auxiliary sets;
- cord/interface type;
- frequency pair;
- data rate;
- automatic-answer support;
- power;
- physical dimensions;
- BSP sections and issue dates.

Do not use “Bell 103” as the final catalog granularity.

---

## 6. RS-232 formalizes the equipment boundary

A U.S. National Bureau of Standards standards survey records this revision chronology:

- **RS-232 — May 1960**;
- **RS-232-A — October 1963**;
- **RS-232-B — October 1965**;
- **RS-232-C — August 1969**.

Source:

https://www.govinfo.gov/content/pkg/GOVPUB-C13-4d7b52427051ca9e169ba2337917df2f/pdf/GOVPUB-C13-4d7b52427051ca9e169ba2337917df2f.pdf

The historical TIA listing for RS-232-A describes the standard as an interface between **data processing terminal equipment** and **data communication equipment**, exchanging control and binary serialized data signals, particularly where the two sides are supplied by different companies.

Source:

https://store.accuristech.com/standards/tia-rs-232-a?product_id=2593188

This wording exposes the original interoperability problem very clearly:

```text
vendor A terminal/computer
          |
     standard interface
          |
vendor B communication equipment
```

The standard is therefore part of the commercial/institutional history of modular equipment supply.

---

## 7. RS-232-A was actually adopted by Bell data equipment

The strongest genealogy edge in this excavation comes from Bell's own product documentation.

A May 1964 interface specification for Bell **Data Sets 202C and 202D** states that the bipolar voltage interface signals exchanged between business machines and the data sets conform to **Electronic Industries Association Standard RS-232-A of October 1963**.

Archived scan:

https://bitsavers.org/communications/westernElectric/modems/202C_and_202D_Interface_Specification_May64.pdf

This is a direct standard → implementation relationship.

```text
EIA RS-232-A (Oct 1963)
           ↓ explicitly adopted
Bell 202C / 202D interface (May 1964 documentation)
```

This proves that the standardized DTE/DCE boundary was not merely an abstract committee product.

It entered real Bell System data-set engineering.

---

## 8. The revision chain is a history of changing interoperability assumptions

The revision dates alone are useful:

```text
RS-232       May 1960
   ↓
RS-232-A     Oct 1963
   ↓
RS-232-B     Oct 1965
   ↓
RS-232-C     Aug 1969
```

But the archaeological goal is a **field-by-field diff**.

For each edition we eventually need:

- defined interchange circuits;
- circuit names/codes;
- voltage thresholds;
- source/load assumptions;
- cable-length/capacitance limits;
- timing circuits;
- protective/signal ground definitions;
- automatic calling/answering provisions;
- connector requirements;
- pin allocations;
- synchronous vs asynchronous assumptions;
- speed scope;
- compatibility notes.

Do not copy a later RS-232-C pinout backward into 1960.

### Why this matters

Many modern explanations teach RS-232 as if “the standard” always meant:

> DB-25 + TxD/RxD/RTS/CTS/DTR/DSR/DCD + ± voltages.

That can erase revision history.

The archive should instead reconstruct what **each edition actually required**.

---

## 9. V.24 belongs beside RS-232, not underneath it

ITU-T's current V.24 page describes the recommendation as a list of definitions for interchange circuits between **DTE** and **DCE**, covering binary data, control and timing signals.

ITU also exposes an edition history including a 1976 edition and later superseding editions.

Source:

https://www.itu.int/ITU-T/recommendations/rec.aspx?lang=en&rec=4938

A common historical shorthand says “RS-232/V.24.”

For archaeology this shorthand is dangerous.

The standards divide responsibility differently.

A useful map is:

```text
                 terminal / computer
                         |
                 interchange boundary
                 /                   \
        EIA RS-232 family          CCITT family
          integrated US view        V.24: circuit functions
                                     V.28: electrical traits
                                     connector allocation elsewhere
```

The relationship is one of overlapping/parallel standardization and interoperability, not simple identity.

### Research target

Find the earliest CCITT V.24 editions/drafts and committee records and determine:

- first approval date;
- relationship to earlier telegraph/data recommendations;
- documentary interaction with EIA RS-232;
- which side borrowed terminology or interface concepts, if any;
- how national equipment vendors implemented cross-compatible interfaces.

Until that chain is documented, the lineage should remain `coexisted-with`, not `derived-from`.

---

## 10. Data set → modem → serial port is not one straight product line

Several different genealogies are easy to conflate.

### 10.1 Modulation/data-set genealogy

```text
low-speed FSK data set
   ↓
higher-rate voice-band modem families
   ↓
error-correcting/compressing modems
   ↓
V.32/V.34/V.90-era modem systems
```

### 10.2 Terminal-interface genealogy

```text
equipment-specific terminal/data-set wiring
   ↓
DTE/DCE standard boundary
   ↓
RS-232 revisions / CCITT interface families
   ↓
computer serial ports
   ↓
terminal servers / console ports / embedded serial links
```

### 10.3 Telephone-service genealogy

```text
TWX / private-wire / DATA-PHONE service
   ↓
dial data / leased data services
   ↓
consumer dial-up access / modem banks
   ↓
digital access systems
```

One device can participate in all three histories simultaneously.

That is why “the modem evolved into the serial port” would be nonsense, even though modem history and serial-port history are deeply intertwined.

---

## 11. What survived into modern networking equipment?

The original voiceband data set mostly disappeared.

But the interface culture survived surprisingly long.

### Surviving ideas

- explicit terminal side vs communication-equipment side;
- separate transmit and receive data circuits;
- hardware state/control circuits;
- carrier/ready indication;
- defined electrical responsibility at a connector boundary;
- console/terminal access separated from the routed data plane;
- standardized interoperability between separately supplied equipment.

### Things that died or became optional

- many modem-specific control circuits;
- dependence on analog voiceband telephone modulation;
- large external modem boxes for ordinary computer connectivity;
- DB-25 as a universal-looking serial connector;
- strict DTE/DCE cabling assumptions in many later embedded/PC uses.

### A living fossil

A router's serial console port in the late 20th/early 21st century may be technologically far removed from a Bell DATA-PHONE installation.

Yet the cultural expectation remains familiar:

```text
computer/terminal side
      ↕ standardized serial interface
communication/network equipment side
```

That is the kind of survival this repository's lineage model is intended to capture.

---

## 12. Open questions

### Bell 101

- Locate primary Bell 101A and 101B BSPs.
- Acquire and checksum the 101C Issue 2 March 1963 scan.
- Determine exact relationship among SAGE modem hardware, Bell 101 naming and commercial service.
- Separate first design, military use, announcement and commercial availability dates.

### Bell 103

- Locate 103A Section 591-014-100 Issues 1–4.
- Explain `Issue 5, January 1961` vs `© 1967` in the surviving scan.
- Build 103A1/103A2 and later 103-family model tree.
- Recover service tariffs and first customer deployment evidence.
- Verify originate/answer frequency plans by exact model/revision.

### RS-232

- Acquire lawful metadata/copies for 1960 RS-232, A, B and C editions.
- Produce a revision diff.
- Identify committee participants and vendor submissions.
- Establish the exact standard→product adoption chronology beyond Bell 202C/202D.

### V.24/V.28

- Recover earliest editions, not only later ITU database entries.
- Map functional vs electrical vs connector standards.
- Find documentary evidence of EIA/CCITT interaction.

### Physical artifacts

- Locate surviving 101C/103A units with provenance.
- Photograph/document interface cords, connectors, internal cards and labels.
- Record component date codes and Western Electric manufacturing markings.

---

## Evidence ladder used here

### Contemporary / near-contemporary

- Bell System Practice, Data Set 103A Type, Section 591-014-100, surviving scan: https://bitsavers.org/communications/westernElectric/modems/591-014-100_Data_Set_103A_Identification_and_Operation_Jan67.pdf
- *Bell System Technical Journal* 1962 article naming Data Sets 101A, 103A and 202A: https://www.worldradiohistory.com/Archive-Bell-System-Technical-Journal/60s/Bell-System-Technical-Journal-1962-6-Complete.pdf
- Bell 202C/202D Interface Specification, May 1964: https://bitsavers.org/communications/westernElectric/modems/202C_and_202D_Interface_Specification_May64.pdf

### Standards/institutional records

- NBS historical standards survey with RS-232 revision dates: https://www.govinfo.gov/content/pkg/GOVPUB-C13-4d7b52427051ca9e169ba2337917df2f/pdf/GOVPUB-C13-4d7b52427051ca9e169ba2337917df2f.pdf
- Historical TIA RS-232-A listing: https://store.accuristech.com/standards/tia-rs-232-a?product_id=2593188
- ITU-T V.24 recommendation/edition database: https://www.itu.int/ITU-T/recommendations/rec.aspx?lang=en&rec=4938

### Archival leads still needing acquisition/verification

- Data Set 101C BSP set referenced by classic-computing collectors/archives, including Identification and Operation Issue 2 (March 1963): https://www.classiccmp.org/pipermail/cctalk/2017-May/034745.html

---

## Current conclusion

The important historical object is not “the DB-25 connector.”

It is the **standardized boundary between computing/terminal equipment and communication equipment**.

That boundary emerged from real data-service engineering, became formalized through standards such as the EIA RS-232 family and CCITT interchange-circuit recommendations, was implemented in commercial data equipment, and then outlived the specific telephone-modem environment that made it necessary.

This is exactly the sort of standard genealogy that turns a list of old specifications into an explanation of why modern interfaces look the way they do.