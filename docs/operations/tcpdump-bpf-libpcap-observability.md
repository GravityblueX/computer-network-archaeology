# tcpdump, BPF and libpcap: How Operators Learned to See the Packet

## Why observability has a genealogy

Protocol standards define fields and assigned numbers, but operators need a way to observe those fields on a live network.

A packet analyzer is therefore not merely a utility layered on top of networking. It is an **interpretation system** connecting:

```text
wire bytes
  ↓
kernel capture mechanism
  ↓
filter language / capture API
  ↓
protocol dissector
  ↓
human-readable names and fields
```

`tcpdump`, the Berkeley Packet Filter (BPF), and `libpcap` form one of the most influential families in that observability layer.

---

## 1. From raw packets to a useful operator view

A packet on Ethernet may contain only numbers at the relevant boundaries:

```text
EtherType = 0x0800
IP Protocol = 6
Destination Port = 443
```

A useful analyzer presents something closer to:

```text
IPv4
TCP
https / port 443
```

That transformation depends on several knowledge sources:

- packet-format definitions;
- assigned-number registries;
- OS header constants;
- service/protocol databases;
- analyzer-owned tables and dissectors.

The analyzer therefore acts as a historical interpreter.

When an old number remains assigned, a modern dissector may still know its name long after the protocol has disappeared from ordinary deployments.

---

## 2. Packet capture was an operating-system problem first

User-space packet analysis requires the operating system to deliver packets to the analyzer efficiently.

Different systems historically exposed different capture interfaces. The current libpcap project describes itself as a **system-independent interface for user-level packet capture**, created because system vendors exposed different capture mechanisms and multiple tools needed portability.

Its README also preserves a Lawrence Berkeley National Laboratory Network Research Group provenance line and an old libpcap 0.4a7 archive location.

This gives a clean role transformation:

```text
OS-specific capture mechanism
          ↓ portability problem
libpcap abstraction
          ↓
tcpdump and other analyzers
```

The portable API is not the same thing as BPF, and BPF is not the same thing as tcpdump.

---

## 3. BSD Packet Filter

Steven McCanne and Van Jacobson presented **The BSD Packet Filter: A New Architecture for User-level Packet Capture** at the 1993 Winter USENIX conference.

BPF addressed a crucial performance question:

> How can a user process request only the packets it cares about without copying every packet through user space first?

The broad architecture places a small filtering program in or near the kernel capture path so irrelevant packets can be rejected before expensive transfer and processing.

This produces a lineage:

```text
packet capture
    ↓
user expresses filter
    ↓
filter compiled to BPF-style program
    ↓
kernel/capture mechanism evaluates filter
    ↓
selected packets reach user space
```

The modern meaning of “BPF” has expanded enormously on Linux through classic BPF and eBPF ecosystems, but that later history must not be back-projected onto the 1993 packet-capture architecture.

The root-hunting project should preserve:

```text
1993 packet-filter BPF
            ≠
all later eBPF systems
```

while still documenting any actual implementation descent.

---

## 4. libpcap preserves the BPF filter language model across systems

The current libpcap documentation states that it supports filtering based on the BSD Packet Filter architecture.

On systems with compatible in-kernel filtering, a BPF program can be evaluated in the capture path. On other capture backends, libpcap may need to evaluate the filter in user space.

Thus the same user-facing filter expression can survive while the execution site changes:

```text
"tcp port 80"
       ↓
filter compiler
       ↓
BPF-like intermediate/filter program
       ↓
BSD kernel BPF
or Linux packet socket filter
or user-space fallback
```

This is another recurring pattern in the repository:

> interface semantics survive while implementation placement migrates.

---

## 5. A filter expression contains several ancient namespaces

Consider:

```text
tcp port 53
```

The analyzer must understand at least:

```text
"tcp"
  ↓ IP Protocol Number 6

"53"
  ↓ transport endpoint number
```

A filter such as:

```text
ether proto 0x0806
```

reaches the EtherType namespace.

A richer filter can therefore be seen as a query across multiple historical registries.

This suggests a useful root-hunting visualization:

```text
operator token
    ↓
parser symbol
    ↓
registry identity
    ↓
wire offset / field
    ↓
BPF test instruction
```

The path from a word typed by a human to bytes selected in the kernel is a technical genealogy of its own.

---

## 6. tcpdump as a dissector museum

Capture is only half of the tool.

After a packet reaches user space, tcpdump must recognize and print protocol structure.

Over decades the dissector set has accumulated support for:

- Ethernet and other link types;
- ARP and RARP;
- IPv4/IPv6;
- TCP/UDP/ICMP;
- routing protocols;
- older vendor and research protocols;
- tunneling and encapsulation;
- newer data-center/provider protocols.

As a result, the source tree itself can be used as a **survivorship catalog**.

For each decoder:

```text
when added?
which wire number triggers it?
which RFC/vendor document defines it?
still reachable in current builds?
legacy-only?
removed as dead code?
```

The libpcap CHANGES file provides examples of this living maintenance process: old capture backends and protocol/filter aliases are removed, new link-layer types appear, and compatibility behavior continues to change.

Thus observability software has its own birth/death layer independent of protocol standard status.

---

## 7. Capture-file formats create another long-lived interface

Packet analysis also created durable file formats.

Classic pcap files and later pcapng allow traffic to outlive the physical network on which it was captured.

A capture artifact can preserve:

```text
frame bytes
capture timestamp
captured length
wire length
link-layer type
```

and therefore become primary archaeological evidence.

The libpcap source contains explicit warnings not to change saved-file structure interpretation casually because capture files must remain exchangeable across architectures and releases.

That is an interoperability contract between **analysis software across time**.

A packet file recorded decades ago may be parsed by modern software because the capture-format contract survived alongside the protocol formats being captured.

---

## 8. BPF and Assigned Numbers intersect in the compiler

The root-hunting repository should eventually map a filter expression all the way down.

For example:

```text
tcpdump 'arp or tcp port 443'
```

can be decomposed as:

```text
arp
  ↓ EtherType 0x0806

or

tcp
  ↓ IP Protocol 6
port 443
  ↓ TCP destination/source port comparison
```

The compiler then emits tests against packet offsets and values.

This is the moment where:

- IEEE-assigned EtherTypes;
- IANA protocol numbers;
- IANA service/port numbers;
- packet-format standards;
- C source constants;
- analyzer grammar;

meet in one executable predicate.

---

## 9. Why tcpdump matters to historical reconstruction

A protocol standard says what packets should look like.

A packet capture says what a real machine actually sent.

A tcpdump version says what contemporary tools were able to recognize and how operators named what they saw.

These are three different evidence layers:

```text
normative standard
     ↓ comparison
captured deployment traffic
     ↓ interpreted through
contemporary diagnostic tool
```

For difficult archaeology, all three should be kept.

A future record should be able to say:

```text
RFC diagram:       field means X
BSD implementation: emits Y
1988 capture:       bytes show Z
1988 tcpdump:       printed W
modern tcpdump:     prints W2
```

That is far stronger than citing only a retrospective history.

---

## 10. Source/provenance anchors

High-value current/historical anchors include:

- current libpcap source and README:
  - https://github.com/the-tcpdump-group/libpcap
- current tcpdump source:
  - https://github.com/the-tcpdump-group/tcpdump
- Steven McCanne & Van Jacobson, *The BSD Packet Filter: A New Architecture for User-level Packet Capture*, USENIX Winter 1993:
  - https://www.usenix.org/conference/usenix-winter-1993-conference/bsd-packet-filter-new-architecture-user-level-packet

The libpcap project currently identifies itself as formerly from the Lawrence Berkeley National Laboratory Network Research Group and points to an old `libpcap-0.4a7.tar.Z` distribution path.

That old distribution is a high-priority acquisition target.

---

## 11. Root-hunting summary

The observability genealogy can be represented as:

```text
wire protocol standards
      ↓
assigned numeric identities
      ↓
OS packet capture mechanism
      ↓
BPF filtering architecture
      ↓
libpcap portable capture/filter API
      ↓
tcpdump dissectors and presentation
      ↓
operator sees a name instead of raw bytes
```

A command such as:

```text
tcpdump -n 'tcp port 443'
```

therefore sits on top of multiple decades of standardization and implementation work.

The tool is not merely observing network history.

**Its ability to name the packet is itself part of that history.**

## Next excavation

- acquire the oldest surviving tcpdump and libpcap distributions;
- reconstruct pre-BPF capture mechanisms;
- diff BPF VM instruction sets and filter compilers;
- map dissector additions/removals by release;
- trace pcap savefile and pcapng format genealogy;
- preserve period packet captures and their contemporary tcpdump output;
- compare classic BPF packet filtering with later Linux BPF/eBPF without collapsing them into one undifferentiated lineage.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
