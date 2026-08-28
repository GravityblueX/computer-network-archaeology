# Livingston PortMaster → RADIUS → Network AAA

> How dial-up modem-pool administration became a reusable client/server authentication, authorization, and accounting architecture.

RADIUS is now encountered far outside the 1990s dial-up world that gave birth to it.

That makes it easy to forget what problem the protocol originally solved.

RFC 2058 states the problem plainly: managing dispersed serial lines and modem pools for large numbers of users creates a major administrative burden, especially because those modem pools are links from the outside world into private network resources.

The initial solution is equally concrete:

```text
many Network Access Servers / modem pools
              ↓
     send user credentials + request
              ↓
        central RADIUS server
              ↓
 authentication + service configuration
              ↓
 NAS delivers PPP / SLIP / Telnet / etc.
```

Most importantly, RFC 2058 records its own product ancestry:

> RADIUS was originally developed by Livingston Enterprises for the PortMaster series of Network Access Servers.

That gives this archive an unusually strong design/deployment lineage:

```text
Livingston PortMaster access-server problem
              ↓ direct product development
RADIUS authentication/authorization protocol
              ↓ IETF standardization/revision
RFC 2058 → RFC 2138 → RFC 2865
              +
RADIUS Accounting → RFC 2059/2139/2866
```

The later expansion of RADIUS into other access technologies is a separate branch and must not be back-projected into its dial-up origin.

---

## 1. The PortMaster problem is centralized subscriber administration

The PortMaster configuration guide already shows an access server doing much more than serial multiplexing:

- SLIP;
- PPP;
- PAP;
- CHAP;
- dial-in/dial-out operation;
- user authorization;
- flow control;
- IP network attachment.

Once one organization owns many access servers, another problem appears:

> Where should accounts, passwords, service permissions, IP parameters, and policy live?

If every NAS keeps a separate user database, changes must be synchronized across every box.

RFC 2058 describes exactly this scaling problem:

```text
modem pool A ─┐
modem pool B ─┼── scattered account/config state = administration pain
modem pool C ─┘
```

and proposes:

```text
              central user/config database
                        ↑
             RADIUS server/service
                 ↑      ↑      ↑
              NAS A   NAS B   NAS C
```

The protocol is therefore an **operations architecture** as much as an authentication packet format.

Primary source:

https://www.rfc-editor.org/rfc/rfc2058.html

---

## 2. NAS becomes a RADIUS client

RADIUS defines a client/server relationship in which the **Network Access Server (NAS)** is the client.

That naming is important.

The user does not normally speak RADIUS directly.

Instead:

```text
user
 ↓ PAP / CHAP / login / other access method
NAS / PortMaster-like edge
 ↓ RADIUS Access-Request
RADIUS server
 ↓ Access-Accept / Reject / Challenge + attributes
NAS
 ↓
service delivered to user
```

The NAS is responsible for collecting access information, sending it to a RADIUS server, and acting on the response.

The RADIUS server authenticates and returns configuration needed for the requested service.

RFC 2058 explicitly lists services such as:

- SLIP;
- PPP;
- Telnet;
- rlogin.

This is a direct bridge from the terminal/dial-access genealogy into centralized AAA.

---

## 3. Authentication and authorization are already intertwined

The common shorthand "AAA" can make it sound as if RADIUS began with three perfectly separated modules called Authentication, Authorization, and Accounting.

The historical documents are more concrete.

RFC 2058 describes a user database that contains both:

- authentication information;
- configuration information determining which service the user should receive.

A successful Access-Accept can carry attributes describing the service to deliver.

So the original operational flow already combines:

```text
Who are you?
      ↓
May you enter?
      ↓
What service/configuration should this NAS give you?
```

Accounting is standardized through a related protocol/document line rather than simply being one field in the original authentication RFC.

---

## 4. Attribute-Length-Value makes policy extensible

RFC 2058 emphasizes an extensible protocol design using variable-length **Attribute-Length-Value** information.

That matters historically because a centralized access-control protocol cannot freeze every future access technology into one fixed record format.

Attributes include categories such as:

- username/password/CHAP information;
- NAS address/port;
- service type;
- framed protocol;
- framed IP address/netmask;
- routing/filter configuration;
- callback information;
- timeouts;
- vendor-specific data;
- LAT login/service fields;
- AppleTalk fields;
- NAS port type.

The attribute model lets the RADIUS server return more than a yes/no authentication decision.

It can send **network-service configuration** to the NAS.

This is one reason the architecture generalizes well beyond one PortMaster model.

---

## 5. RADIUS remembers the older terminal-access world inside its attributes

One of the most archaeologically delightful details is that RFC 2058 still contains attributes such as:

```text
Login-LAT-Service
Login-LAT-Node
Login-LAT-Group
Login-LAT-Port
```

So the RADIUS RFC itself physically preserves a fossil from DEC/LAT-style terminal service.

It also contains framed-protocol fields for PPP/IP and other access types.

This means the specification is not abstractly "modern AAA."

It is a snapshot of a transitional networking environment in which:

- dial modems;
- PPP;
- Telnet;
- LAT;
- AppleTalk;
- IP routing;
- callback access;

all coexist behind network access servers.

The standard is itself an archaeological layer.

---

## 6. Why UDP?

RADIUS uses UDP rather than building on a persistent transport connection.

That choice belongs to the operational history of access servers.

A NAS sends a request to one or more configured servers, retransmits when necessary, and can fail over to another server.

This allows the access-server authentication path to be relatively simple and not depend on maintaining a long-lived transport session.

The exact retry, failover, duplicate, and timeout rules need version-level reconstruction across RFC 2058/2138/2865 and real implementations.

The important historical point is that reliability is partly an **application-protocol/client operational responsibility**, not simply delegated to TCP.

---

## 7. Shared secrets: the trust boundary is between NAS and server

RFC 2058 authenticates transactions between a RADIUS client/NAS and server using a shared secret that is not sent over the network.

User password handling is also protected within that model.

Thus the trust architecture looks like:

```text
user ↔ access protocol ↔ NAS
                       ↕ shared-secret trust
                   RADIUS server
```

The protocol's later security limitations and extensions belong to a separate lineage.

Do not project today's RADIUS/TLS or later cryptographic recommendations back into the 1997 protocol.

---

## 8. RFC 2058 explicitly documents Livingston ancestry

RFC 2058 is unusually valuable because the standardization document names its own product origin:

> RADIUS was originally developed by Livingston Enterprises for their PortMaster series of Network Access Servers.

This is strong enough for a direct `derived-from`/documented-design lineage edge:

```text
Livingston PortMaster access-server ecosystem
        ↓ direct original development
RADIUS
```

This is fundamentally different from an inferred statement such as:

```text
TIP looked like an access server, therefore TIP caused RADIUS
```

No such causal edge is established.

The archive must preserve that evidentiary asymmetry.

---

## 9. RFC 2058 → RFC 2138 → RFC 2865 is a formal document/protocol line

The RFC history is straightforward:

```text
RFC 2058 — January 1997
    ↓ obsoleted by
RFC 2138 — April 1997
    ↓ obsoleted by
RFC 2865 — June 2000
```

RFC Editor records:

- RFC 2058: https://www.rfc-editor.org/info/rfc2058/
- RFC 2138: https://www.rfc-editor.org/info/rfc2138/
- RFC 2865: https://www.rfc-editor.org/info/rfc2865/

RFC 2865 explicitly says it obsoletes RFC 2138 and provides a change log.

This is therefore a formal `revision-of` lineage, unlike the PortMaster→RADIUS origin edge, which is a product/design ancestry relationship.

---

## 10. The protocol is born around modem pools — RFC 2865 still says so

RFC 2865 retains the historical operational motivation:

> managing dispersed serial line and modem pools for large numbers of users requires substantial administration and careful security, authorization, and accounting.

That continuity matters.

Even by 2000, when RADIUS is already a standardized reusable protocol, its introductory model still describes a world of modem pools and Network Access Servers.

This gives the archive a strong warning:

> do not explain RADIUS's origin using Wi-Fi, 802.1X, enterprise VPN, or modern cloud identity systems.

Those are later deployments/branches.

---

## 11. Accounting becomes a sibling protocol branch

RADIUS Accounting is separately documented.

The 2000 RFC is:

**RFC 2866 — RADIUS Accounting**

https://www.rfc-editor.org/info/rfc2866/

It describes accounting information flowing from a NAS client to a shared accounting server.

The model records session/service events such as start/stop and session duration.

The revision chain includes earlier accounting RFCs:

```text
RFC 2059
   ↓
RFC 2139
   ↓
RFC 2866
```

This is a sibling lineage to authentication/authorization:

```text
RADIUS authentication/authorization
              +
       RADIUS Accounting
```

They share the NAS/server/attribute architecture but have distinct specification histories.

---

## 12. Accounting records expose the operational meaning of a "session"

RFC 2866 defines a session around a service supplied by the NAS to the dial-in user.

Accounting can record:

- start;
- stop;
- interim updates;
- session time;
- input/output octets;
- termination cause;
- link counts for multilink sessions;
- authentication method;
- NAS identity/port.

This is not merely billing metadata.

It is an operational record of edge access.

That makes RADIUS Accounting an important source for reconstructing ISP operations, modem-pool usage, and subscriber sessions.

If historical RADIUS accounting logs survive, they are potential archaeological datasets.

Privacy/legal constraints would of course require extreme care; this repository should preserve schemas and lawful historical metadata rather than ingesting identifiable user records casually.

---

## 13. RADIUS separates the access box from the account database

This may be the most important architectural inheritance.

Without RADIUS-like centralization:

```text
NAS A → local users
NAS B → local users
NAS C → local users
```

With RADIUS:

```text
NAS A ─┐
NAS B ─┼──> shared authentication/policy service
NAS C ─┘
```

Now an access server can be replaced, added, or geographically distributed without making it the only authoritative repository of user identity/policy.

The edge box becomes an **enforcement/attachment point**, while identity/service policy can live elsewhere.

That separation survives as a general architecture in many later systems.

Direct protocol ancestry into any later AAA system must still be documented separately.

---

## 14. RADIUS expands beyond dial-up, but that is later history

Later RADIUS deployments include many access contexts beyond modem pools.

The safe genealogy is:

```text
PortMaster / dial NAS origin
        ↓
RADIUS generic NAS/server protocol
        ↓
additional access technologies adopt RADIUS
```

The archive should build separate branches for:

- broadband access;
- wireless LAN authentication;
- 802.1X/EAP integration;
- VPN/remote access;
- network-device administrative authentication;
- roaming/federation uses;
- Diameter relationship;
- RadSec/RADIUS over TLS descendants.

Do not collapse all of those into the original 1997 use case.

---

## 15. The PortMaster → RADIUS edge is stronger than most product-to-standard stories

Historical technology writing often says a product "inspired" a standard without providing evidence.

Here the RFC itself says who originally developed the protocol and for which product family.

That lets the archive encode:

```text
PortMaster series
   └─ documented-design / derived-from → original RADIUS
```

with high confidence.

But the next edge:

```text
RADIUS → every later AAA system
```

would be unjustified.

Some systems interoperate with RADIUS, replace it, borrow roles, or solve similar problems independently.

Those relations need their own evidence.

---

## 16. New artifacts and sources to preserve

Artifacts:

- original Livingston RADIUS implementation;
- earliest RADIUS server daemon source;
- PortMaster RADIUS client implementation in ComOS;
- RFC 2058 protocol generation;
- RFC 2138 generation;
- RFC 2865 generation;
- RADIUS Accounting RFC 2059/2139/2866 generations;
- early RADIUS dictionary files;
- early vendor-specific attributes;
- UDP port 1645/1812 transition;
- accounting port 1646/1813 transition;
- early shared-secret configuration files;
- Merit and Livingston interoperability implementations.

Sources:

- RFC 2058;
- RFC 2138;
- RFC 2865;
- RFC 2059/2139/2866;
- Livingston PortMaster/ComOS manuals;
- original Livingston RADIUS source/releases;
- IETF RADIUS working-group archives;
- operator documentation from early ISPs/universities.

---

## 17. Next excavation targets

1. Locate the **pre-RFC Livingston RADIUS source tree** and establish first release dates.
2. Identify which PortMaster/ComOS revision first shipped a RADIUS client.
3. Recover early `users`, `clients`, and dictionary file formats.
4. Diff RFC 2058 → 2138 → 2865 packet/attribute/security changes.
5. Reconstruct UDP 1645 → 1812 service-port history.
6. Reconstruct RADIUS Accounting 2059 → 2139 → 2866 and UDP 1646 → 1813.
7. Trace RADIUS proxying and roaming/federation deployments.
8. Trace the NAS concept from dial servers into broadband/wireless access.
9. Trace RADIUS ↔ 802.1X/EAP with exact RFC/IEEE relationships.
10. Trace Diameter as a separate successor/alternative genealogy without claiming simple replacement.
11. Recover early ISP authentication/accounting logs only as schemas/redacted/public historical artifacts with privacy-safe provenance.
12. Preserve old PortMaster/ComOS/RADIUS binaries and source metadata where licensing permits.

---

## Archaeological conclusion

RADIUS did not begin as an abstract enterprise identity protocol.

It began inside a concrete operational world:

```text
telephone lines
    ↓
modem pools
    ↓
network access servers
    ↓
large numbers of accounts
    ↓
central administration problem
```

Livingston's answer separated the access device from the central identity/service database.

That architectural separation survived the decline of the modem pool.

So once again the ancestor is still inside the modern system, even when the original hardware environment has disappeared.
