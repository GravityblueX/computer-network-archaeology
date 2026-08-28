# Network Management Lineage: HMP → SGMP → SNMP → SNMPv2/v3

Network management is easy to treat as an administrative afterthought. Historically it is part of the network's architecture.

Routers, gateways, terminal servers and hosts do not become infrastructure merely because they forward packets. Someone must be able to answer:

- Is the node alive?
- Which interfaces are up?
- How many packets are being dropped?
- Which routes/neighbors exist?
- What changed?
- Can a parameter be altered remotely?
- How does an operator learn about a failure without logging into every machine?

The lineage that eventually produced SNMP begins in a world of experimental gateway monitoring and operations centers, not in a finished MIB browser.

## 1. Monitoring existed before SNMP

The early Internet already had operational monitoring requirements.

BBN Internet gateways reported status and traps to the Internet Network Operations Center (INOC), and the gateway software described in RFC 823 contained explicit monitoring/error-reporting machinery.

This is important because the later management protocols did not invent the *need* for remote observability. They standardized and generalized an already essential operator function.

The archive should therefore distinguish:

```text
operations practice
        ↓
monitoring protocol
        ↓
managed-object model
        ↓
standardized network-management framework
```

These layers do not necessarily appear at the same time.

## 2. HMP: Host Monitoring Protocol

RFC 869 (December 1983) describes the Host Monitoring Protocol (HMP).

Its definition of a "host" is broad: an addressable Internet entity that can send and receive messages, including server hosts, workstations, terminal concentrators, packet switches and gateways.

At the time of the RFC, HMP was already being used to collect information from Internet Gateways and TACs, with implementations being designed for other hosts.

This gives HMP a useful archaeological position:

```text
Internet operations / gateway monitoring
           ↓
HMP generalized remote host monitoring
```

HMP should not simply be called "SNMP before SNMP". Its protocol structure, object representation and deployment context need their own reconstruction.

## 3. SGMP: simplify the gateway-management problem

RFC 1028 (November 1987) defines the **Simple Gateway Monitoring Protocol** (SGMP).

The RFC explicitly frames it as an interim response to immediate gateway-monitoring needs.

Its design goals are revealing:

- minimize software complexity inside the gateway;
- expose as much management capability as possible to remote management tools;
- keep the protocol easy for tool developers to understand;
- represent messages independently within transport datagrams;
- use UDP in the specified implementation;
- model gateway management primarily as inspection or alteration of variables;
- rely heavily on polling, with unsolicited messages limited to cases needed to guide monitoring.

The important ancestor here is a **philosophy of simple agents and more capable managers**.

## 4. SGMP → SNMP: syntax breaks, philosophy survives

RFC 1067 (August 1988) is especially valuable lineage evidence because it says this directly.

The new SNMP was **not backward-compatible** with SGMP. The syntax changed and new UDP ports were assigned.

But the RFC also states that the original:

- philosophy;
- design decisions;
- architecture

remained intact.

This produces a very precise lineage edge:

```text
SGMP wire syntax
     ── not carried over compatibly ──X

SGMP management philosophy / architecture
                    ↓ survives
                   SNMP
```

This is exactly why the repository tracks properties rather than writing only "SGMP was replaced by SNMP".

## 5. The manager/agent model becomes explicit

RFC 1067 describes an architecture containing:

- network management stations;
- network elements;
- management applications;
- agents resident in network elements.

The management station performs the more sophisticated monitoring/control logic. The network element exposes an agent that executes a deliberately constrained set of management operations.

This asymmetry survives strongly in later SNMP architecture.

## 6. Managed state becomes named objects

SNMP's management model is based on inspecting and altering variables.

The associated Internet management framework separates:

- the protocol used to access management data;
- the Structure of Management Information (SMI), which defines how managed objects are described/named;
- the Management Information Base (MIB), which defines concrete objects.

This separation is a major conceptual ancestor of modern device-management schemas.

The important lineage is not "SNMP invented counters". Devices already had counters and state.

The new architecture makes those variables part of a standardized, remotely addressable namespace.

## 7. ASN.1 enters Internet operations

SNMP uses a restricted subset of ASN.1 Basic Encoding Rules.

RFC 1067 explicitly notes that earlier SGMP experience influenced this choice and that restrictions were used to preserve simplicity.

This creates another property-level edge:

```text
SGMP ASN.1 experience
        ↓ carried design experience
SNMP SMI / ASN.1-based object and message representation
```

The archive should keep this separate from later BER/ASN.1 use in OSI management systems even when tools or terminology overlap.

## 8. Get / GetNext / Set / Trap

The classic SNMPv1 operational vocabulary stabilizes around a small set of protocol operations.

RFC 1157 documents:

- GetRequest;
- GetNextRequest;
- GetResponse;
- SetRequest;
- Trap.

The Trap PDU includes standard conditions such as:

- coldStart;
- warmStart;
- linkDown;
- linkUp;
- authenticationFailure;
- egpNeighborLoss;
- enterpriseSpecific.

This is a revealing snapshot of what operators cared about in 1990: interfaces, reboots, authentication and EGP neighbors are all visible directly in the base management protocol.

## 9. SNMP's "simplicity" was an architectural policy

The word *Simple* was not decorative branding.

RFC 1067/1157 explicitly minimizes complexity in the managed agent.

Rather than define many imperative remote commands, management functions are represented primarily as reads/writes of variables.

For example, an action can be modeled as setting a parameter that causes behavior rather than inventing a dedicated imperative protocol operation.

This design choice strongly influences later management practice:

```text
complex management logic in manager
              ↕ simple operations
small agent exposing managed state
```

## 10. SNMPv1 specification lineage

The first SNMP specification lineage itself contains several RFC revisions.

A simplified map is:

```text
SGMP RFC 1028 (1987)
      ↓ philosophy survives, syntax incompatible
SNMP working definitions
      ↓
RFC 1067 (1988)
      ↓ later revision
RFC 1098
      ↓ obsoleted by
RFC 1157 (1990)
```

A mature archive needs the missing RFC 1098 diff rather than jumping directly 1067 → 1157.

## 11. SNMPv2: the framework becomes more explicit

RFC 1441 (April 1993) introduces version 2 of the Internet-standard Network Management Framework.

It explicitly states that SNMPv2 is derived from the original SNMPv1 framework and names the SNMPv1 components:

- SMI;
- MIB description mechanism;
- SNMP protocol.

The SNMPv2 framework makes the decomposition clearer through components for:

- information structure;
- textual conventions;
- protocol operations;
- transport mappings;
- instrumentation;
- administration;
- conformance.

So SNMPv2 is not merely a packet-format revision. It is a more explicit management framework.

## 12. SNMPv3: security and modular architecture become first-class

The later SNMPv3 architecture addresses a major weakness of early SNMP generations: security and administrative control.

RFC 3411 (December 2002) describes a modular architecture containing an SNMP engine with:

- message-processing subsystem;
- security subsystem;
- access-control subsystem;
- multiple SNMP applications.

It explicitly says the architecture is modular so the SNMP standards can evolve over time.

This is another lineage transformation:

```text
simple manager/agent protocol
          ↓
management framework
          ↓
modular engine + message/security/access-control subsystems
```

The original "simple management" ancestry remains visible, but the architecture has become much richer.

## 13. What survived from SGMP to modern SNMP

Strong continuities include:

- manager/agent asymmetry;
- remotely accessible managed variables;
- keeping device-side management logic constrained;
- polling as a core mechanism;
- unsolicited event notification as a complementary mechanism;
- structured namespaces for management information;
- network-management stations managing many devices;
- proxying/interworking with devices that use different management mechanisms.

## 14. What did not survive unchanged

- SGMP wire compatibility;
- early variable naming;
- security assumptions;
- administrative/community models;
- exact SMI/MIB structures;
- protocol operations and PDUs;
- transport/security framework details.

The continuity is architectural, not byte-for-byte.

## 15. Hardware makes the protocol real

A mature archaeology of SNMP should include concrete devices.

For example:

```text
NMS workstation
    ↓ UDP/IP
router / bridge / terminal server
    ↓
SNMP agent process
    ↓
MIB variables
    ↓
device driver / interface counters / routing table
```

Questions for each historical device:

- Which firmware release first included SNMP?
- Which MIB groups were implemented?
- Was the agent a separate process or part of the OS image?
- How much memory did the management agent consume?
- What traps were actually generated?
- How were community strings configured?
- What console commands exposed the same counters locally?
- Which NMS products could manage it?

Without implementation evidence, the standards lineage remains incomplete.

## 16. HMP / SGMP / SNMP is not the only management branch

The 1980s also contained OSI/CMIP-oriented network-management work and vendor-specific management systems.

RFC 1157 itself describes SNMP as the short-term Internet approach while the OSI management framework was also being examined.

The history therefore should not be narrated as:

```text
nothing → SNMP → everyone immediately agrees
```

A more accurate topology includes:

```text
vendor management
       ↘
HMP / SGMP → SNMP
       ↗          ↔ OSI/CMIP management work
operations-center practice
```

The eventual dominance of SNMP is a deployment/history question, not proof that alternatives did not exist.

## 17. Lineage summary

```text
ARPANET / Internet operations monitoring
              ↓
HMP (RFC 869, 1983)
              ↓ related monitoring experience
SGMP (RFC 1028, 1987)
              ↓ architecture/philosophy survive
SNMP (RFC 1067, 1988)
              ↓ revision line
SNMPv1 RFC 1157 (1990)
              ↓ framework evolution
SNMPv2 (1993)
              ↓ security/admin evolution
SNMPv3 architecture
              ↓
modern SNMP management framework
```

The exact HMP→SGMP causal edge still needs stronger author/working-group evidence before being encoded as direct formal ancestry. SGMP→SNMP, by contrast, is directly documented by SNMP itself.

## 18. High-priority excavation queue

1. HMP implementations in BBN gateways/TACs.
2. INOC screens, alarm formats and operator manuals.
3. SGMP implementation source and deployed routers.
4. RFC 1028 → 1067 object/PDU/encoding diff.
5. RFC 1067 → 1098 → 1157 revision diff.
6. Original SMI/MIB RFC lineage.
7. First Cisco/Proteon/Wellfleet/etc. SNMP agent releases.
8. Early NMS products and workstation requirements.
9. Community-string operational practice and real incidents.
10. SNMPv2 version branches and coexistence history.
11. SNMPv3 security model development.
12. CMIP/OSI management comparison without winner-centric simplification.
13. MIB module/source archives and vendor enterprise OID genealogies.
14. Trace modern telemetry/gNMI/NETCONF relationships carefully — do not assume direct SNMP descent without documentation.

Network management is therefore another example of the project's main thesis: the modern protocol is not a clean invention. It is the surviving layer of decades of operator practice, experimental monitoring protocols, failed assumptions and increasingly formal information models.
