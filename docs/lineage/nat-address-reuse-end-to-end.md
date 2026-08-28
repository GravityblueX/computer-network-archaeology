# NAT: address reuse, broken transparency, and the retreat from globally unique host addresses

## Why NAT belongs in an archaeology of standards

Network Address Translation is sometimes introduced as a simple practical trick:

> private addresses inside, public address outside.

Historically, NAT is much more revealing. It appears at the intersection of three pressures:

- IPv4 address depletion;
- routing-table scaling;
- the desire to deploy a short-term solution without modifying every host and router.

RFC 1631 (May 1994) is unusually frank about this. It presents NAT as another short-term solution alongside CIDR while larger-address next-generation Internet protocols are still being developed.

Primary source:

- RFC 1631 — https://www.rfc-editor.org/rfc/rfc1631.html

---

## 1. NAT changes the meaning of an IP address in transit

In the original end-to-end IPv4 model, a host's IP address is intended to be globally meaningful within the Internet routing system.

NAT inserts a translation boundary:

```text
inside host
10.0.0.5
   |
   | packet reaches NAT border
   v
translation state
10.0.0.5 <-> 198.51.100.7
   |
   v
outside Internet sees translated address
```

The packet's addressing information no longer has one immutable meaning from source to destination.

This is not merely a routing-table optimization. It changes the architectural status of endpoint identity.

---

## 2. RFC 1631 explicitly ties NAT to address depletion and routing scale

The RFC opens by identifying two major Internet problems:

- IP address depletion;
- scaling in routing.

It calls CIDR a short-term solution to scaling and discusses larger-address protocols as long-term work. NAT is proposed as address reuse that can complement those efforts.

This is important because NAT should not be narrated as if engineers simply preferred private addressing from the beginning.

It was a response to a specific scarcity/migration moment.

---

## 3. Stub domains and reused address space

The RFC's basic model places NAT at the border of a stub domain.

Inside addresses need not be globally unique. A translation table maps local addresses to globally unique external addresses.

```text
stub domain A: local/reused address space
        |
        v
      NAT
        |
        v
globally routed address space
```

The same local addresses can be reused in other stub domains.

The archival distinction to preserve is:

```text
address reuse concept
      ≠
private-address allocation convention
      ≠
NAT translation mechanism
      ≠
NAPT/PAT port multiplexing
```

These become related but separate branches.

---

## 4. The attraction: deploy without changing hosts or ordinary routers

RFC 1631 emphasizes that NAT can be installed incrementally without changes to hosts or routers.

This is one of the recurring themes of this repository:

> compatibility with a huge installed base often matters more than architectural purity.

Proxy ARP solved a similar kind of migration problem at a different layer: hide subnet boundaries from hosts that do not understand them.

NAT hides address-domain boundaries from ordinary endpoints.

That does **not** mean Proxy ARP is an ancestor of NAT. It means they share a recurring deployment strategy: put adaptation at a boundary rather than update every endpoint.

---

## 5. Translation is not free: checksums and application payloads expose hidden coupling

Changing an IP address affects checksums in upper-layer protocols because TCP/UDP checksum pseudo-headers include IP addresses.

A NAT therefore cannot always rewrite only the IP header.

RFC 1631 describes prototype implementations that adjust:

- IP addresses;
- IP checksums;
- TCP-related fields/checksums;
- and, for FTP, even `PORT` command information and TCP sequence/acknowledgment numbers in a prototype router.

This is one of the most important archaeological facts about NAT:

> applications that embed network-layer addressing inside application payloads break layering assumptions and force translators to become application-aware.

That later grows into Application Level Gateway (ALG) behavior.

---

## 6. FTP is an early NAT stress test

Classic active FTP carries address/port information in the control protocol and opens a separate data connection.

That makes FTP a perfect example of why NAT became operationally complex.

Connect:

- [`ftp-control-data-evolution.md`](ftp-control-data-evolution.md)

A NAT may have to understand enough FTP control syntax to rewrite embedded endpoint information.

So the historical chain is not:

```text
FTP -> NAT
```

but:

```text
FTP's explicit address/data-connection model
          +
NAT address translation
          ↓ interaction failure
FTP-aware translation / ALG behavior
```

---

## 7. RFC 1631 already lists architectural objections

The original NAT memo is not triumphalist. It explicitly lists negative characteristics, including:

- possible performance/state scaling problems;
- mis-addressing risk;
- applications that break or become harder to run;
- hiding host identity;
- complications for SNMP, DNS and other protocols.

This should be preserved because later histories sometimes frame NAT as an obviously successful design with criticisms invented afterward.

The criticisms were present in the proposal itself.

---

## 8. RFC 3022: Traditional NAT becomes a larger family

RFC 3022 (January 2001) obsoletes RFC 1631 and explicitly distinguishes:

- **Basic NAT** — address-to-address translation;
- **NAPT** — address plus TCP/UDP port (or analogous identifier) translation, allowing many internal addresses to share one external address.

Primary source:

- RFC 3022 — https://www.rfc-editor.org/rfc/rfc3022.html

Conceptually:

```text
Basic NAT
local IP A <-> global IP X

NAPT
local IP A:port 1 \
local IP B:port 2  > global IP X:different external ports
local IP C:port 3 /
```

These are historically different mechanisms and should not all be collapsed into a single `NAT` artifact.

---

## 9. NAT creates state at the network edge

Traditional routing can forward using relatively stable destination-prefix information without remembering every individual transport conversation.

NAPT commonly needs per-flow translation state.

That changes failure behavior:

```text
router reboot
  -> routing may reconverge and traffic can resume

stateful NAPT reboot
  -> translation/session state may disappear
  -> active transport sessions fail
```

This is an important step in the long history of increasingly stateful middleboxes.

But "NAT caused stateful networking" is too broad; firewalls and other systems have separate lineages.

---

## 10. NAT and the end-to-end principle

NAT complicates the assumption that arbitrary Internet hosts can initiate direct conversations using globally meaningful endpoint addresses.

Effects include:

- inbound reachability becoming policy/state dependent;
- application payloads needing translation helpers;
- peer-to-peer systems needing traversal techniques;
- host identity becoming less directly visible from observed source addresses.

Later mechanisms such as STUN/TURN/ICE belong to descendant operational branches, not to RFC 1631's original design.

Do not back-project WebRTC-era traversal language into 1994.

---

## 11. NAT is not the same thing as a firewall

The two are commonly combined in products, but their primary roles differ:

```text
NAT
  -> rewrite address/port namespaces

firewall
  -> apply traffic-permission/security policy
```

A NAT deployment may incidentally prevent unsolicited inbound traffic because no mapping exists, but that operational effect should not be mistaken for a complete security architecture.

The product genealogy of home routers later fuses:

- NAT/NAPT;
- stateful firewalling;
- DHCP server;
- DNS forwarding;
- Ethernet switching;
- Wi-Fi access point;
- PPPoE/DHCP WAN client.

That fusion deserves its own hardware/software archaeology.

---

## 12. NAT and CIDR are parallel responses to different parts of the same crisis

CIDR addresses:

- classful allocation waste;
- routing-table aggregation/scaling.

NAT addresses:

- reusable local address spaces / address conservation;
- incremental deployment without globally unique addresses for every internal host.

They intersect, but:

```text
CIDR -> NAT
```

is not a valid revision chain.

The historical relationship is coexistence under shared address/routing pressure.

---

## 13. Implementation archaeology

RFC 1631 names experimental implementations:

- a prototype in public-domain KA9Q TCP/IP software;
- an implementation in a Cray Communications IP router.

These are extraordinarily valuable leads.

Future excavation should recover:

### KA9Q

- exact release containing NAT prototype;
- source modules;
- translation-table structure;
- checksum adjustment code;
- configuration syntax.

### Cray Communications router

- exact model/software release;
- FTP ALG behavior;
- address/checksum rewrite path;
- test setup.

### Commercial routers/firewalls

- Cisco NAT introduction and syntax;
- Linux `ipfwadm`/`ipchains`/`iptables` NAT lineage;
- BSD `ipfilter`/`pf` branches;
- consumer home-router firmware.

---

## 14. Lineage rules

Safe:

```text
IPv4 address depletion + routing pressure
      -> NAT proposal as address-reuse mechanism

RFC 1631 NAT
      -> RFC 3022 Traditional NAT revision/expansion

Basic NAT
      -> expanded operational family including NAPT
```

Unsafe:

```text
Proxy ARP -> NAT formal ancestry             UNSUPPORTED
NAT = firewall                               WRONG RESPONSIBILITY
NAT = private addresses                      TOO BROAD
CIDR -> NAT upgrade chain                    WRONG
NAT solved Internet scaling permanently      CONTRADICTS ORIGINAL MEMO
```

---

## 15. Sources

Primary:

- Kjeld Egevang and Paul Francis, RFC 1631, *The IP Network Address Translator (NAT)*, May 1994 — https://www.rfc-editor.org/rfc/rfc1631.html
- P. Srisuresh and K. Egevang, RFC 3022, *Traditional IP Network Address Translator (Traditional NAT)*, January 2001 — https://www.rfc-editor.org/rfc/rfc3022.html

Related:

- CIDR RFCs 1518/1519;
- private-address-space RFC 1918;
- NAT terminology/behavior documents;
- FTP RFC 959 for an application with embedded endpoint information.

---

## Open excavation questions

1. Recover the KA9Q NAT prototype source named in RFC 1631.
2. Identify the Cray Communications router model/software and test records.
3. Trace Basic NAT → NAPT implementation history by vendor.
4. Reconstruct early FTP ALG behavior and sequence-number adjustment.
5. Trace private-address allocation standards separately from NAT translation.
6. Build Linux/BSD/router NAT implementation and configuration genealogy.
7. Trace consumer broadband routers as compound NAT/firewall/DHCP/DNS/switch/AP appliances.
8. Trace NAT traversal protocols only as later operational descendants.

NAT is one of the clearest cases where the Internet chose **incremental deployability over preservation of a simple global endpoint-address model**, and then spent decades engineering around the consequences.
