# Technology Lineage Index

This is the entrance to the repository's **genealogical view**.

Use the ordinary timeline to ask **when** something happened. Use stack excavations to ask **how the system was wired and operated**. Use this index to ask:

> **What did this technology inherit, revise, replace, coexist with, or leave behind in modern networking?**

Machine-readable edges: [`../data/lineage-ledger.csv`](../data/lineage-ledger.csv)  
Edge schema: [`../schema/lineage-edge.schema.json`](../schema/lineage-edge.schema.json)  
Research rules: [`README.md`](README.md)  
Backlog: [`ROADMAP.md`](ROADMAP.md)  
Catalog: [`../catalogs/lineages.md`](../catalogs/lineages.md)

---

## 1. Terminal / modem / serial-interface ancestry

### [`../docs/lineage/bell-data-set-rs232-v24.md`](../docs/lineage/bell-data-set-rs232-v24.md)

Follow the standardized boundary between terminal/computer equipment and communications equipment:

```text
teleprinter / business machine / computer
        ↓
Bell data set / modem boundary
        ↓
EIA RS-232 → RS-232-A → B → C
        ↕
CCITT V.24 / V.28 family
        ↓
serial terminals / modems / console ports
```

Key archaeological warnings:

- `V.24` is not simply a synonym for the whole RS-232 specification;
- Bell 101/103 product chronology remains partly disputed;
- never copy later RS-232-C pin/electrical facts backward into the 1960 standard.

Structured examples:

- [`../records/lineages/LIN-0001-rs232-to-rs232a.json`](../records/lineages/LIN-0001-rs232-to-rs232a.json)
- [`../records/lineages/LIN-0004-rs232a-to-bell-202.json`](../records/lineages/LIN-0004-rs232a-to-bell-202.json)

---

## 2. Shared-medium ancestry: ALOHA → Ethernet

### [`../docs/lineage/standards-genealogy.md`](../docs/lineage/standards-genealogy.md)

Supporting excavations:

- [`../docs/alohanet/radio-to-ethernet.md`](../docs/alohanet/radio-to-ethernet.md)
- [`../docs/ethernet/xerox-alto-2-94mbps-pup-stack.md`](../docs/ethernet/xerox-alto-2-94mbps-pup-stack.md)
- [`../docs/ethernet/experimental-ethernet-physical-layer.md`](../docs/ethernet/experimental-ethernet-physical-layer.md)

Structured edge:

- [`../records/lineages/LIN-0006-aloha-to-experimental-ethernet.json`](../records/lineages/LIN-0006-aloha-to-experimental-ethernet.json)

The documented inherited object is the shared-medium contention problem/approach, **not** an unchanged packet format or copied radio protocol.

---

## 3. Layering ancestry: integrated TCP → IP + TCP

### [`../docs/lineage/tcp-ip-split-and-standardization.md`](../docs/lineage/tcp-ip-split-and-standardization.md)

```text
RFC 675 Internet Transmission Control Program
              ↓ repeated IEN redesign
        responsibilities separate
          /                \
   Internet Protocol        TCP
      RFC 760             RFC 761
          ↓                  ↓
      RFC 791             RFC 793
```

This lineage preserves a fact modern layered diagrams hide:

> **layering itself has a history.**

Related operational migration:

- [`../records/lineages/LIN-0009-ncp-to-ip-tcp.json`](../records/lineages/LIN-0009-ncp-to-ip-tcp.json)

---

## 4. Naming ancestry: HOSTS.TXT → DNS

### [`../docs/lineage/hosts-txt-to-dns.md`](../docs/lineage/hosts-txt-to-dns.md)

```text
central host-table maintenance/distribution
            ↓ scaling/admin pressure
hierarchical domain naming
            ↓
distributed name servers + resolvers
            ↓
delegation + caching
            ↓
RFC 1034 / 1035 DNS core
```

The transition is not only a file-format change. It redistributes **administrative authority**.

Living fossil: local hosts-file lookup survives beside DNS on modern systems.

---

## 5. Interdomain-routing ancestry: EGP → BGP-1 → BGP-4

### [`../docs/lineage/bgp-1-to-bgp-4.md`](../docs/lineage/bgp-1-to-bgp-4.md)

```text
EGP + NSFNET exterior-routing experience
             ↓ documented design ancestry
BGP-1 / RFC 1105 (1989)
             ↓
BGP-2 / RFC 1163 (1990)
             ↓
BGP-3 / RFC 1267 (1991)
             ↓
BGP-4 / RFC 1771 (1995)
             ↓ revised core specification, same version name
BGP-4 / RFC 4271 (2006)
```

BGP-4's classless-prefix/aggregation change intersects the separate CIDR lineage.

Structured records:

- [`../records/artifacts/ART-0097-bgp-4-rfc1771.json`](../records/artifacts/ART-0097-bgp-4-rfc1771.json)
- [`../records/lineages/LIN-0034-bgp3-to-bgp4.json`](../records/lineages/LIN-0034-bgp3-to-bgp4.json)
- [`../records/sources/SRC-0071-rfc-1771.json`](../records/sources/SRC-0071-rfc-1771.json)
- [`../records/sources/SRC-0072-rfc-1519.json`](../records/sources/SRC-0072-rfc-1519.json)
- [`../records/sources/SRC-0073-rfc-4271.json`](../records/sources/SRC-0073-rfc-4271.json)

---

## 6. Packet-switch / gateway / router role ancestry

### [`../docs/internetworking/bbn-gateway-to-router.md`](../docs/internetworking/bbn-gateway-to-router.md)

Do **not** collapse this into:

```text
IMP → router
```

Instead distinguish:

- packet switching inside one network;
- host-to-packet-network attachment;
- forwarding between heterogeneous networks;
- routing-control computation;
- later router terminology.

A 1982 BBN Internet Gateway is a particularly useful fossil because its functional role feels familiar to a modern router engineer while its contemporary name is still **gateway**.

---

## 7. Virtual circuits and datagrams: interworking, not only competition

### [`../docs/x25/pad-public-data-network-stack.md`](../docs/x25/pad-public-data-network-stack.md)

The archive explicitly preserves operational relationships such as:

```text
IP datagram
    ↓ carried over
X.25 virtual circuit
```

A historical genealogy must allow technologies to compete architecturally while still interworking in deployment.

---

## 8. Store-and-forward afterlife

### [`../docs/uucp/usenet-store-and-forward-world.md`](../docs/uucp/usenet-store-and-forward-world.md)

UUCP's exact protocols and bang paths faded, while engineering patterns such as:

- persistent queues;
- deferred delivery;
- retry after failure;
- intermittent-connectivity tolerance;

remain common.

Do not turn that resemblance into direct descent unless documentary evidence exists.

---

## 9. Backbone-platform role ancestry

Supporting excavations:

- [`../docs/nsfnet/fuzzball-node-internals.md`](../docs/nsfnet/fuzzball-node-internals.md)
- [`../docs/nsfnet/ibm-rt-nss-node-internals.md`](../docs/nsfnet/ibm-rt-nss-node-internals.md)

```text
PDP-11 / LSI-11 Fuzzball backbone
          ↓ operational replacement
IBM RT multi-computer NSS backbone
          ↓
T3 / RS-6000 generation
```

What survives is the backbone-routing role; the chassis, bus, internal architecture, line interfaces and routing software can all change.

---

# Reading rule

Every lineage arrow should eventually answer:

1. **what exact property moved or changed?**
2. **what source proves the relationship?**
3. **where in that source?**
4. **how certain is it?**
5. **what does the arrow not prove?**

If those questions cannot be answered, the relationship belongs in the research queue as a hypothesis, not in the archive as established ancestry.