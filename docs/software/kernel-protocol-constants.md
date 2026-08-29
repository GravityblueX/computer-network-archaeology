# Registry Numbers Fossilized in Kernel and UAPI Constants

## From standards registry to source-code constant

One of the strongest forms of technical survival is not merely a compatible packet capture. It is a decades-old registry value appearing as a named constant in the source code of a modern operating system.

A root-hunting chain can look like:

```text
IEEE / IANA registry
       ↓
wire number
       ↓
OS header constant
       ↓
kernel/user-space branch or socket selection
       ↓
packet sent or decoded
```

Modern Linux provides unusually visible examples.

---

## 1. EtherType values in Linux `if_ether.h`

The Linux UAPI header `include/uapi/linux/if_ether.h` describes itself as global definitions for the Ethernet IEEE 802.3 interface and contains constants such as:

```c
#define ETH_P_PUP    0x0200
#define ETH_P_IP     0x0800
#define ETH_P_X25    0x0805
#define ETH_P_ARP    0x0806
#define ETH_P_RARP   0x8035
#define ETH_P_IPV6   0x86DD
```

as well as later additions for VLAN, MPLS, PPPoE, 802.1X and many others.

The fascinating part is the temporal mixture.

```text
PUP         ancient Xerox internetworking
IPv4        living 1981 Internet core
X.25        public-data-network era
ARP         living IPv4 LAN mechanism
RARP        largely historical bootstrap mechanism
IPv6        later Internet generation
802.1Q      VLAN era
MPLS        provider/backbone era
PPPoE       broadband access era
802.1X      port-access-control era
```

All live in one source header because the kernel still needs a stable numeric vocabulary to classify frames.

This source file is therefore a small archaeological museum that also compiles.

---

## 2. The constants are not all equal in provenance

The header itself warns that at least some values are not official registered EtherTypes. For example, comments distinguish certain Linux/internal or unofficial values.

That means:

```text
#define exists in Linux
```

is **not sufficient evidence** that:

```text
IEEE Registration Authority assigned this value globally
```

Every constant needs provenance classification:

- formally IEEE-assigned EtherType;
- IETF usage with IEEE allocation;
- vendor/proprietary value;
- historical de-facto value;
- Linux-internal pseudo-protocol discriminator;
- deliberately unregistered compatibility value.

This is why source-code archaeology must be cross-checked against registry archaeology.

---

## 3. IP Protocol Numbers in Linux `in.h`

The Linux UAPI `include/uapi/linux/in.h` contains the next-level protocol constants:

```c
IPPROTO_ICMP = 1
IPPROTO_IGMP = 2
IPPROTO_IPIP = 4
IPPROTO_TCP  = 6
IPPROTO_EGP  = 8
...
IPPROTO_UDP  = 17
```

The file header is itself a fossil. It describes Linux INET as a TCP/IP implementation using the **BSD Socket interface** as the means of communication with user level, and carries early-1990s version/author history.

Thus one file joins several genealogies:

```text
IANA IP Protocol Number namespace
           ↓
BSD-derived socket interface concepts
           ↓
Linux INET implementation
           ↓
UAPI constants visible to applications
```

`IPPROTO_TCP = 6` is not merely documentation. It is an executable identity shared by packet parsers, raw sockets, firewall code, diagnostic software and applications.

---

## 4. The same number can appear at multiple software boundaries

For TCP:

```text
IANA Protocol Number 6
       ↓
IP header Protocol / IPv6 Next Header
       ↓
IPPROTO_TCP constant
       ↓
socket(AF_INET, SOCK_..., IPPROTO_TCP)
       ↓
packet filters / dissectors / kernel dispatch
```

For IPv4 over Ethernet:

```text
IEEE EtherType 0x0800
       ↓
Ethernet type field
       ↓
ETH_P_IP
       ↓
Linux packet-socket / frame dispatch code
```

The registry value becomes a **cross-component ABI-like fact**.

Changing it is not equivalent to changing a private enum inside one program.

---

## 5. Modern headers preserve dead neighbors

This is where kernel headers become historically powerful.

A registry may retain an old assigned value because reuse would be dangerous or misleading. An OS may retain a symbolic constant because:

- packet captures can still contain the protocol;
- compatibility tools refer to it;
- old hardware/drivers may generate it;
- source compatibility matters;
- the code has little cost to retain;
- the number remains formally assigned even if deployments vanished.

So a header can preserve:

```text
living protocol
extinct protocol
legacy compatibility
internal pseudo-protocol
future/new protocol
```

side by side.

That is exactly the kind of mixed stratum the root-hunting project wants to expose.

---

## 6. `struct ethhdr` keeps the field visible

The Linux header also exposes a packed Ethernet header structure conceptually equivalent to:

```c
struct ethhdr {
    unsigned char h_dest[6];
    unsigned char h_source[6];
    __be16        h_proto;
};
```

The last member is where the registry identity lands in the frame representation.

This creates a direct chain:

```text
EtherType registry
   ↓ 16-bit value
Ethernet header type field
   ↓ `h_proto`
Linux `struct ethhdr`
```

The history is literally in a C struct.

---

## 7. BSD ancestry should be reconstructed separately

Linux comments explicitly acknowledge BSD socket-interface ancestry, but the exact source-code genealogy of individual constants must not be guessed.

Future work should compare:

- 4.2BSD / 4.3BSD / 4.4BSD headers;
- Net/2 and 4.4BSD-Lite;
- early Linux INET headers;
- modern FreeBSD/OpenBSD/NetBSD;
- modern Linux UAPI.

For each constant:

```text
symbol name
numeric value
comment
first observed release
registry source
semantic changes
removed aliases
```

should be tracked separately.

A modern symbol spelling may be newer than the wire value it represents.

---

## 8. Kernel constants versus `/etc/protocols`

There are two distinct local representations:

```text
/etc/protocols
    "tcp" → 6
```

and:

```c
IPPROTO_TCP = 6
```

They solve different problems.

`/etc/protocols` is a name database queried at runtime through netdb-style APIs.

`IPPROTO_TCP` is a compile-time symbolic constant embedded in source and binaries.

Therefore:

```text
Assigned Numbers
    ├── local runtime database
    │      └── /etc/protocols
    └── compile-time source constant
           └── IPPROTO_TCP
```

Both project the same global number into the operating system through different mechanisms.

---

## 9. Current Linux is itself a layered archive

The current Linux `if_ether.h` comments still contain an early implementation header with a 1994-era version marker and early INET authorship names.

The `in.h` UAPI comments likewise preserve early Linux INET provenance and explicitly describe the BSD socket interface connection.

So the file contains two histories simultaneously:

1. the protocol-number/EtherType history encoded in constants;
2. the Linux networking implementation history encoded in comments and source structure.

This is precisely why source archives matter. Standards tell us the assigned value; source tells us **where an implementation made the value concrete**.

---

## 10. Source targets

Current Linux reference points:

- https://github.com/torvalds/linux/blob/master/include/uapi/linux/if_ether.h
- https://github.com/torvalds/linux/blob/master/include/uapi/linux/in.h

Historical targets:

- 4.2BSD and 4.3BSD `netinet/in.h`, Ethernet headers and protocol-switch tables;
- Net/2 and 4.4BSD-Lite equivalents;
- early Linux 0.x/1.x INET headers;
- contemporary vendor Unix headers.

The next step should create a field-level diff table rather than only a prose history.

---

## 11. Root-hunting summary

A value such as:

```c
#define ETH_P_IP 0x0800
```

is a complete mini-genealogy:

```text
Ethernet protocol-type allocation
        ↓
0x0800 becomes the IPv4 identity
        ↓
operating systems define a symbol
        ↓
kernel packet dispatch uses it
        ↓
applications and packet tools reuse the symbol
        ↓
modern machine still interprets 0x0800 the same way
```

The device, source tree, compiler and hardware generation can all change while the number remains stable.

That is one of the purest examples of a technical standard outliving almost everything that first implemented it.

## Next excavation

- extract historical BSD/Linux constant tables;
- compare symbol spelling versus wire-value stability;
- identify constants retained after protocol deployment disappeared;
- distinguish official registry values from local pseudo-protocol identifiers;
- connect constants into BPF/tcpdump dissectors and firewall rule parsers.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
