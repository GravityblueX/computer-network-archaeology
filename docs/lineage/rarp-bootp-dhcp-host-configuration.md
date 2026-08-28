# RARP → BOOTP → DHCP: from “what is my IP address?” to reusable host configuration

> **Lineage question:** how did a newly booted machine go from knowing only a hardware address to receiving a reusable IP address, boot parameters, and eventually a leased configuration bundle?

This is one of the clearest examples of a networking responsibility becoming progressively more general.

A modern DHCP exchange can look ordinary enough that it is easy to forget the earlier problem:

> A machine has just powered on. It may have no disk, no local IP configuration, and no idea which server to contact. What can it know before it can speak IP normally?

The answer changed repeatedly.

---

## 1. The bootstrap problem predates DHCP

Early diskless workstations and network-booted machines could know their own hardware-interface address while lacking an Internet Protocol address.

RFC 903 (June 1984), *A Reverse Address Resolution Protocol*, states the problem explicitly: a host such as a diskless workstation may know its hardware address but not its protocol address. RARP reverses the ARP-style question:

```text
ARP:
    IP address  → hardware address

RARP:
    hardware address → IP address
```

RARP therefore introduces a client/server asymmetry absent from ordinary ARP operation: one or more RARP servers maintain a database mapping hardware addresses to protocol addresses.

Primary source:

- RFC 903 — https://www.rfc-editor.org/rfc/rfc903.html

### What RARP solves

- bootstrap discovery of an IP/protocol address;
- use of an already-known hardware address as identity;
- operation on broadcast media such as Ethernet.

### What RARP does **not** solve well

RARP is tightly coupled to the local link/broadcast environment and fundamentally returns an address mapping rather than a rich host configuration.

The historical mistake to avoid is:

> “RARP was basically early DHCP.”

It was not. It solved a much narrower bootstrapping question.

---

## 2. BOOTP generalizes the boot conversation

RFC 951, *Bootstrap Protocol*, was published in September 1985.

Its important historical move is not merely another packet format. BOOTP makes the bootstrap exchange a UDP/IP client/server protocol that can cross router boundaries with the help of relay behavior, and can return more than the client's own IP address.

Primary source:

- RFC 951 — https://www.rfc-editor.org/rfc/rfc951.html

RFC 951 even contains a dedicated comparison with RARP.

Conceptually the responsibility changes from:

```text
hardware address
      ↓
"tell me my protocol address"
```

into:

```text
booting client identity
      ↓
bootstrap request
      ↓
server database
      ↓
client address + boot/server information
```

### Why this matters

The bootstrap service is no longer only an Ethernet-local address reverse-lookup mechanism.

It becomes part of IP infrastructure.

That is a major lineage boundary.

---

## 3. BOOTP relay is an architectural ancestor worth preserving

One of the most important inherited properties in the BOOTP → DHCP line is **relay behavior**.

A large routed network does not want a full bootstrap server on every LAN.

Instead:

```text
client broadcast
      ↓
local relay agent / gateway
      ↓ routed network
central BOOTP/DHCP server
```

This lets administrative centralization coexist with Layer-2-local client discovery.

Later DHCP specifications explicitly preserve BOOTP relay-agent behavior.

This is still recognizable in modern DHCP relay / `ip helper-address`-style deployments.

The direct implementation genealogy of individual router commands belongs in vendor records, but the architectural role is already present in the BOOTP/DHCP standards lineage.

---

## 4. DHCP is explicitly based on BOOTP

RFC 1531, October 1993, says this directly:

- DHCP is based on BOOTP;
- it adds automatic allocation of reusable network addresses;
- it captures BOOTP relay-agent behavior;
- DHCP participants can interoperate with BOOTP participants.

Primary source:

- RFC 1531 — https://www.rfc-editor.org/rfc/rfc1531.html

This is unusually strong lineage evidence.

The correct edge is not a speculative “influenced by”.

It is a documented design derivation.

```text
BOOTP
  ↓ based-on / extended-by
DHCP
```

---

## 5. The major new idea: the address becomes a lease

BOOTP's normal database model fits comparatively stable host identities and assignments.

DHCP adds a different resource-management problem:

> What if addresses are scarce and hosts are temporary?

RFC 1531 explicitly defines three allocation modes:

- **automatic allocation** — permanent assignment;
- **dynamic allocation** — assignment for a limited period;
- **manual allocation** — administrator chooses, DHCP conveys.

Dynamic allocation allows addresses to return to a pool and be reused.

This is one of the most important conceptual changes in the lineage:

```text
address as relatively static host property
              ↓
address as managed reusable resource
              ↓
lease / renewal / expiration lifecycle
```

The familiar modern DHCP lease is therefore not just a convenience feature.

It reflects a change in how IPv4 address space is operationally managed.

---

## 6. DHCP becomes host configuration, not just address allocation

Another responsibility expands simultaneously.

The client does not merely need an address.

It may need:

- subnet mask;
- default-router information;
- DNS servers;
- domain information;
- boot server/file information;
- many later vendor- or protocol-specific options.

Thus the bootstrap lineage becomes:

```text
RARP
"what is my IP address?"

        ↓

BOOTP
"tell me how to boot and where I belong"

        ↓

DHCP
"allocate and maintain my network configuration state"
```

This is responsibility growth, not merely packet-format revision.

---

## 7. DHCP's standards revision chain

The early DHCP RFC line should remain revision-specific.

```text
RFC 1531 (Oct 1993)
    ↓ obsoleted by
RFC 1541 (Oct 1993)
    ↓ obsoleted by
RFC 2131 (Mar 1997)
```

RFC 2131 remains the classic DHCP core specification.

Primary sources:

- RFC 1531 — https://www.rfc-editor.org/rfc/rfc1531.html
- RFC 1541 — https://www.rfc-editor.org/rfc/rfc1541.html
- RFC 2131 — https://www.rfc-editor.org/rfc/rfc2131.html

Do not treat “DHCP” as one timeless wire protocol. The option ecosystem and later extensions have their own genealogy.

---

## 8. RARP → BOOTP → DHCP is not a clean replacement of every layer

A good lineage must preserve what does **not** transfer.

### RARP-specific aspects that do not simply survive into DHCP

- ARP-like link-level framing model;
- dependence on local broadcast-medium behavior;
- narrow hardware-address → protocol-address mapping purpose.

### BOOTP responsibilities that survive strongly

- bootstrapping before normal host configuration exists;
- client/server model;
- central configuration repository;
- relay through routed networks;
- boot/server information fields and options lineage.

### DHCP additions

- reusable dynamic address allocation;
- explicit lease lifecycle;
- expanded configuration-option model;
- richer client state machine.

So the genealogy is best represented as **generalization plus retained BOOTP compatibility**, not simple byte-for-byte revision.

---

## 9. A modern DHCP relay is an old idea wearing newer syntax

The most visible living fossil in this lineage is relay architecture.

A present network may still look like:

```text
client with no usable IP configuration
        ↓ broadcast request
access LAN / VLAN
        ↓
router or L3 switch acting as relay
        ↓ unicast/routed infrastructure
central DHCP service
        ↓
configuration returned through relay
```

That arrangement embodies a decades-old solution to the same organizational tension:

> clients discover locally, administrators manage centrally.

---

## 10. Archaeological objects to split into records

The archive should not keep only one `DHCP` object.

Create or maintain independent records for:

- RARP / RFC 903;
- BOOTP / RFC 951;
- BOOTP relay behavior and later clarification RFCs;
- DHCP RFC 1531;
- DHCP RFC 1541;
- DHCP RFC 2131;
- DHCP option-format specifications;
- individual historical BOOTP/DHCP server implementations;
- router relay implementations;
- diskless workstation boot ROM clients;
- DHCP lease databases and operator tooling.

---

## 11. Sources

Primary sources used in this excavation:

- RFC 903, *A Reverse Address Resolution Protocol* — https://www.rfc-editor.org/rfc/rfc903.html
- RFC 951, *Bootstrap Protocol* — https://www.rfc-editor.org/rfc/rfc951.html
- RFC 1531, *Dynamic Host Configuration Protocol* — https://www.rfc-editor.org/rfc/rfc1531.html
- RFC 1541, *Dynamic Host Configuration Protocol* — https://www.rfc-editor.org/rfc/rfc1541.html
- RFC 2131, *Dynamic Host Configuration Protocol* — https://www.rfc-editor.org/rfc/rfc2131.html

---

## 12. Next excavation layer

High-value next targets:

1. RFC 951 → RFC 1542 BOOTP relay/clarification diff;
2. RFC 1531 → 1541 → 2131 field/state-machine diff;
3. DHCP option genealogy;
4. earliest BOOTP server/client source code;
5. Sun/Unix diskless workstation RARP/BOOTP boot paths;
6. Cisco/Proteon/Fuzzball/Unix relay implementation history;
7. lease-file formats in early DHCP server software;
8. operational history of DHCP at universities/ISPs;
9. later DHCPv6 as a **separate IPv6 configuration lineage**, not a casual “DHCP version 6” continuation.

---

## Conclusion

The modern DHCP lease hides several older networking problems inside it.

```text
hardware identity
      ↓
RARP address discovery
      ↓
BOOTP routed bootstrap/configuration
      ↓
DHCP reusable allocation + host configuration
```

The packet formats changed, but the deeper question survived:

> **How does a machine that does not yet know the network learn enough to become part of it?**

That question is older than DHCP, and its answers form a clear technical lineage.