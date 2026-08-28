# Root-Hunting Method — 寻根活动的方法

This repository does not treat networking history as a sequence of inventions. It treats modern networks as layered surviving systems whose present behavior can often be traced to older standards, implementations and operational practices.

The working question is:

> If I can still capture this field, type this command, read this header, or depend on this behavior today, where did it come from?

## 1. Root-hunting is not priority hunting

Do not ask only who was first. Ask:

- what exact object existed;
- what property or responsibility it carried;
- whether the property survived unchanged, was revised, moved layers, or disappeared;
- whether the old specification is still normative or merely ancestral;
- which implementation made the idea operational;
- whether a modern packet/configuration can still expose the old structure.

## 2. Track five layers separately

For every living technical feature, attempt to reconstruct:

1. **text lineage** — RFC/standard editions and explicit obsolescence/update relations;
2. **wire lineage** — fields, opcodes, message formats, state machines and numeric assignments;
3. **implementation lineage** — kernels, daemons, firmware, drivers, libraries and hardware;
4. **operational lineage** — tools, commands, failure modes, deployment practices and troubleshooting;
5. **institutional lineage** — vendors, standards bodies, network operators and administrative boundaries.

A feature may have a continuous wire lineage but a discontinuous implementation lineage, or vice versa.

## 3. Classify survival

Use at least these survival states:

- **still-current-original-standard** — the old document itself remains part of the current standards corpus;
- **obsoleted-document-living-protocol** — the old text is obsolete but a successor consolidates the same protocol;
- **living-core-with-extension-forest** — the core remains stable while extensions accumulate;
- **role-survives-mechanism-dies** — the job persists but the original mechanism disappears;
- **interface-convention-survives** — a syntax, pinout, command model or API persists beyond its original product;
- **operational-fossil** — a tool, command or diagnostic convention survives even when the underlying architecture changed;
- **extinct-but-explanatory** — no longer deployed, but necessary to explain why a modern mechanism looks the way it does.

## 4. Build a field-level survivorship table

For packet formats and command languages, do not stop at protocol names.

Example questions for IPv4:

- Is the field still present in the base header?
- Is its width unchanged?
- Is its original semantic definition still current?
- Did another RFC redefine its interpretation?
- Is the field now commonly constant, ignored, rewritten or generated differently?
- Is a related feature obsolete even though the bits remain?

This turns a 1981 diagram into a map of present-day active and fossilized semantics.

## 5. Negative lineage is required

Root-hunting must preserve what **did not** descend.

Examples:

- RIP is not an old version of OSPF;
- ping is not ICMP itself;
- traceroute is not an ICMP protocol revision;
- MIME did not replace the Internet Message Format;
- HTTP did not invent media types;
- Proxy ARP is not ARP version 2;
- a modern Ethernet switch is not merely a faster repeater.

Whenever a tempting arrow is unsupported, record `coexisted-with`, `possibly-influenced`, `role-descends-into`, or an explicit negative claim instead of inventing ancestry.

## 6. Prefer things still observable

A powerful root-hunting artifact is one that can be recognized in a contemporary trace:

```text
IPv4 Version/IHL/TTL/Protocol
UDP four-word header
ICMP Echo Request/Reply
ARP request/reply opcode
DNS RR TYPE/CLASS/TTL/RDLENGTH
SMTP MAIL/RCPT/DATA + three-digit replies
MIME Content-Type: type/subtype; parameters
```

The historical claim becomes stronger when the old form can be compared directly with a modern capture or implementation.

## 7. Preserve semantic drift

The same bits may survive while their meaning changes.

Examples already visible in this archive:

- IPv4's 8-bit Type of Service octet survives physically but was redefined into the Differentiated Services field;
- IPv4 Identification survives physically while RFC 6864 narrowed when its value is meaningful;
- Ethernet survives while normal full-duplex switched links no longer use collision arbitration;
- BGP remains BGP-4 while its defining core RFC was replaced;
- TCP remains TCP while RFC 793 was consolidated into RFC 9293.

Do not call these either “unchanged” or “replaced” without qualification.

## 8. A mature root-hunting record

A mature record should eventually answer:

```text
present-day observable
        ↓
current normative definition
        ↓
older specification(s)
        ↓
first/important implementation(s)
        ↓
operational deployment
        ↓
semantic changes
        ↓
extinct branches / surviving branches
        ↓
primary-source locators
```

The purpose is not nostalgia.

The purpose is to show that the modern network is itself an archaeological site that never stopped running.

---

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
