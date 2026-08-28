# Hayes Smartmodem → AT Command Set → Software-Controlled Modems

> A genealogy of in-band modem control: command mode, dialing, answering, registers, escape sequences, and the long afterlife of `AT`.

One of the most durable modem innovations is not a modulation technique.

It is a **control language**.

For decades a computer could talk to a modem over the same serial interface used for user data and issue commands such as:

```text
AT
ATD...
ATA
ATH
ATS0=1
```

That command style became so widespread that “Hayes-compatible” turned into an industry compatibility category.

The important lineage is:

```text
manual modem control / separate dialing hardware
             ↓
software-controllable Smartmodem
             ↓
Hayes command language
             ↓
Hayes-compatible modem ecosystem
             ↓
AT command supersets in later PSTN/cellular/data modems
```

The exact descendants must be documented separately, but the control-language family is one of the clearest cases where a product interface outlived the original product generation.

---

## 1. Before software-controlled dialing is ordinary

An early modem/data set is primarily a communications boundary.

Dialing may be:

- manual;
- controlled through separate automatic-calling equipment;
- controlled by dedicated leads/interfaces;
- performed by an operator/user before placing a data device online.

The Hayes Smartmodem style changes the user/programmer experience by making call control accessible through ordinary characters sent over the serial DTE interface.

The host does not need a separate complex dialing-control bus for normal use.

Conceptually:

```text
computer serial port
      ↕
modem
  ├── data mode
  └── command interpreter
          ↓
      telephone call control
```

---

## 2. `AT` is an attention prefix

Hayes documentation describes command lines beginning with the characters `AT`, the attention code.

A later Hayes technical reference explicitly calls the family the **Hayes Standard AT Command Set**.

Reference:

https://www.bitsavers.org/pdf/hayes/Hayes_44-012_Technical_Reference_For_Hayes_Modem_Users_1993.pdf

The modem replies to commands and enters different operational states.

The fundamental idea is that the same asynchronous serial stream can carry either:

```text
command text
```

or:

```text
user/application data
```

depending on modem state.

That state distinction is historically crucial.

---

## 3. Command mode makes the modem a programmable peripheral

A Smartmodem-style device exposes control operations as text commands.

Common families include:

- dial;
- answer;
- hang up;
- select pulse/tone dialing;
- configure echo/result codes;
- configure carrier behavior;
- read/write S-registers;
- save/restore profiles;
- select modulation/compatibility behaviors on later models.

This changes software architecture.

A communications program can contain a **modem driver** consisting primarily of command strings and expected responses instead of custom hardware-control logic.

A 1986 PC-SAM networking document provides a concrete example for a Hayes Smartmodem 1200. Its sample modem driver initializes with `AT` commands, dials under software control, waits for `CONNECT`, configures automatic answer, and uses the `+++` escape sequence before an `AT Z` reset/hangup path.

Computer History Museum archival copy:

https://archive.computerhistory.org/resources/access/text/2024/06/102802967-05-001-acc.pdf

This is valuable deployed evidence: command-set semantics were not merely a product-manual curiosity; other network/application software encoded Hayes control behavior directly.

---

## 4. The escape problem: how do you regain command mode?

If the modem is already in data mode, the byte stream belongs to the remote session.

How can the local computer tell the modem:

> stop treating my bytes as remote data; I need to control you again?

The Hayes ecosystem famously uses an escape sequence based on:

```text
+++
```

with guard-time semantics around it.

This is a subtle design problem because `+++` might appear naturally inside user data.

Therefore the escape sequence is not merely three characters. Timing/state context matters.

This design belongs in the archive as a protocol/state-machine object:

```text
COMMAND MODE
   ↓ dial/connect
ONLINE DATA MODE
   ↓ escape sequence + guard time
ONLINE COMMAND MODE
   ↓ return-to-data / hangup
```

Later products often preserve this state model even when they add large command supersets.

---

## 5. S-registers turn modem behavior into persistent configuration

Hayes-style modems expose numbered registers, commonly written as:

```text
S0
S7
...
```

The exact register set changes across models/revisions.

Typical register-controlled behaviors include:

- auto-answer ring count;
- wait time for carrier;
- escape character;
- guard time;
- dialing timing;
- result-code/line behavior.

A deployed modem driver might therefore contain commands such as:

```text
S0=1
S7=120
```

This is an important lineage because device configuration becomes **software-addressable state** exposed through the same textual control language.

Later modems vastly expand configuration, but the pattern survives.

---

## 6. Result codes create a machine-readable call state

The host does not only send commands.

The modem returns state/result information such as:

```text
OK
CONNECT
BUSY
NO CARRIER
NO DIALTONE
```

Later products distinguish speeds and more detailed call progress.

Thus a communications program can implement a state machine:

```text
send initialization
      ↓
wait for OK
      ↓
send dial command
      ↓
parse call-progress response
      ↓
CONNECT → data session
BUSY/NO CARRIER → retry/fail
```

This is the software-visible ancestor of automated dialer logic in BBS software, terminal programs, UUCP dialers, SLIP/PPP scripts, remote-access systems, and many other products.

Direct descent for any particular implementation still needs source-code/config evidence.

---

## 7. Hayes-compatible becomes an ecosystem label

By the mid/late 1980s the command language had become sufficiently dominant that other vendors explicitly marketed products as **Hayes-compatible**.

An IBM PS/2 OEM hardware guide from 1988 lists multiple third-party modems described as Hayes/Smartmodem compatible.

Archive copy:

https://bitsavers.computerhistory.org/pdf/ibm/pc/ps2/PS2_Micro_Channel_OEM_Hardware_Product_Guide_198805.pdf

A 1986 Hayes advertisement itself calls the AT syntax the **Hayes Standard “AT” Command Set** and describes software compatibility around it.

Datamation archive example:

https://bitsavers.computerhistory.org/magazines/Datamation/19861215.pdf

The important archaeological transition is therefore:

```text
one vendor's product interface
        ↓
software assumes interface
        ↓
competitors implement compatibility
        ↓
interface becomes de facto ecosystem convention
```

This is not the same as formal standards-body standardization.

---

## 8. De facto compatibility has edge cases

“Hayes-compatible” does not imply exact identity.

Vendors add:

- proprietary commands;
- `%`, `&`, `\`, `$`, `*`, `+` or other command prefixes;
- new S-registers;
- different default values;
- vendor-specific result codes;
- commands for compression/error control/modulation;
- cellular/radio-specific functions in later eras.

A 1997 remote-access manual states that its modem responds to a **superset of Hayes Smartmodem commands**, with additional prefixes for extended functions.

This is a perfect example of interface genealogy:

```text
core inherited grammar
      +
vendor extensions
```

rather than one frozen protocol.

---

## 9. AT control is independent of modulation lineage

A modem can be Hayes-command compatible while supporting many different line protocols:

- Bell 103;
- Bell 212A;
- V.22bis;
- V.32;
- V.34;
- V.90;
- proprietary modes.

Therefore two genealogies cross:

```text
modulation/error-control genealogy
          ×
command/control-interface genealogy
```

This is one reason the repository needs property-level lineage instead of one product tree.

A Smartmodem 2400 advertisement from 1985, for example, describes compatibility with CCITT V.22bis and Bell 103/212A while the product remains part of the Hayes command ecosystem.

Historical magazine source:

https://www.bitsavers.org/magazines/Datamation/19850101.pdf

---

## 10. AT commands outlive dial-up PSTN modem culture

The `AT` command idiom survives far beyond classic acoustic/telephone modems.

Later communications modules — including cellular data devices — often use `AT`-prefixed command languages for:

- radio/network configuration;
- SIM/account operations;
- SMS;
- packet-data context setup;
- signal/status queries;
- dialing/session setup.

However the archive must not write:

> “modern cellular AT commands are just the original Hayes protocol.”

The safe lineage claim is narrower:

> the textual `AT`-prefixed command/control convention became a durable modem/device-control interface family, repeatedly extended for new communications technologies.

Specific cellular standardization branches (for example 3GPP AT-command specifications) require their own formal-source genealogy.

---

## 11. Why this interface succeeded

From an engineering/ecosystem perspective, the Hayes style has several advantages:

- uses the serial connection already present;
- human-readable enough for terminal debugging;
- easy for software to generate;
- backward-compatible core possible while adding extensions;
- separates call-control state from data transfer;
- allows modem drivers to be configured as strings/scripts;
- encourages software portability across compatible modems.

These advantages also create drawbacks:

- ambiguous vendor compatibility;
- parser quirks;
- escape-sequence hazards;
- mode/state confusion;
- growing command complexity;
- command injection/unsolicited result handling problems in later devices.

The interface's survival is therefore not proof of elegance in every detail; it is evidence of a very strong installed ecosystem and useful abstraction boundary.

---

## 12. Lineage edges to preserve

High confidence:

```text
Hayes Smartmodem command interpreter
   └─ survives-as → Hayes Standard AT Command Set family

Hayes AT command set
   └─ interface-convention-inherited-by → Hayes-compatible third-party modems

Smartmodem command/data mode distinction
   └─ survives-as → later AT-command modem control state models
```

Needs formal descendant sources:

```text
Hayes AT command family
   └─ influenced → cellular/3GPP AT command standards
```

Do not mark that `confirmed` until the relevant standards/history documents explicitly establish the relationship.

---

## 13. Next excavation targets

- original first-generation Smartmodem owner/manual revisions;
- exact product introduction chronology and model naming;
- command grammar in the earliest Smartmodem versus Smartmodem 1200/2400;
- escape-sequence/guard-time original specification;
- complete S-register genealogy;
- `&` command extensions and stored profiles;
- command/result-code compatibility matrices across Hayes, USRobotics, Telebit, Supra, MultiTech, Zoom, ZyXEL;
- UUCP `Devices`/dialer source that drives Hayes-compatible modems;
- SLIP/PPP chat scripts using AT commands;
- BBS/terminal software modem-driver files;
- formal 3GPP/ETSI AT-command branch and exact documented ancestry;
- USB modem/virtual serial-port continuation;
- embedded radio modules that still expose AT commands today.

---

## Archaeological conclusion

The Hayes command set is a reminder that standards do not have to begin in a standards committee.

A successful product interface can become an ecosystem convention because software starts depending on it and competitors implement compatibility.

The durable idea is simple:

> a communications device can expose its control plane as text over the same interface that carries data.

That idea survived multiple generations of physical modem technology, and in many communications devices it survived the telephone modem itself.
