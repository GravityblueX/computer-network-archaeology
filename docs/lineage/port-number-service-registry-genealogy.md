# Service and Port Number Registry Genealogy: 21, 22, 23, 25, 53, 80, 179, 443 and the Institutional Memory of Internet Services

Transport port numbers are another layer of the Internet where tiny integers outlive entire generations of software.

A modern TCP or UDP header carries 16-bit source and destination ports. The numeric field is simple. The registry behind it is not.

The IANA Service Name and Transport Protocol Port Number Registry is a living institutional memory of Internet services: old assignments, current infrastructure, multiple transport protocols, de-assigned entries, and newer registration policy all coexist in one table.

## 1. Familiar ports are historical artifacts in active use

Many numbers are so familiar that they seem natural rather than assigned:

```text
20/21  FTP data/control
22     SSH
23     Telnet
25     SMTP
53     DNS
80     HTTP
179    BGP
443    HTTPS
```

But there is nothing mathematically inevitable about these pairings.

They are coordination decisions preserved by long deployment.

## 2. A port number is not a protocol itself

A port assignment is a rendezvous convention:

```text
transport protocol + port number
          ↓
expected service / application endpoint
```

The same numeric port can have entries for different transport protocols.

For example, the current IANA registry lists BGP on port 179 for TCP and historical/additional transport entries as well.

Therefore the archaeological object is not simply `179`.

It is a tuple of:

- service name;
- port;
- transport protocol;
- description;
- assignment/reference history.

## 3. The three modern ranges have institutional history

The current registry, following RFC 6335, divides the 16-bit space into:

```text
0–1023       System Ports
1024–49151   User Ports
49152–65535  Dynamic/Private Ports
```

These categories encode a policy about scarcity, privilege and coordination.

The number space is not merely technical. It is administratively governed.

## 4. System Ports preserve early Internet service architecture

The low-number range contains many of the classic service boundaries that shaped host software:

- FTP;
- Telnet;
- SMTP;
- DNS;
- HTTP;
- other early network daemons and control services.

Unix `/etc/services`, socket APIs and daemon configuration turned these shared assignments into local operating-system knowledge.

Thus one registry assignment can survive simultaneously in:

- RFCs;
- IANA data;
- libc service databases;
- `/etc/services`;
- firewall rules;
- packet analyzers;
- application defaults.

## 5. 179: routing policy has a transport rendezvous fossil

BGP's use of TCP port 179 is especially useful because BGP itself has gone through BGP-1/2/3/4 and later RFC revisions while the rendezvous convention remains recognizable.

The modern registry still identifies `bgp` on port 179/tcp.

So a router configuration today may contain two durable historical identifiers at once:

```text
BGP-4 protocol lineage
TCP destination port 179
```

The protocol specification evolved while the service-number convention persisted.

## 6. 443: a number can outlive the transport assumptions around it

`https` is registered on port 443.

Historically this evokes HTTP over TLS over TCP.

Modern HTTP can also use QUIC over UDP, and the IANA registry contains HTTPS-related transport assignments accordingly.

This demonstrates a subtle form of continuity:

> the service identity and familiar port may survive while the transport architecture underneath it changes.

A port number is therefore not proof of one specific protocol stack.

## 7. De-assignment is part of the archaeology

The current IANA registry records entries that have been de-assigned or modified.

That means the registry is not purely additive.

Numbers can move through states such as:

```text
unassigned
   ↓
assigned
   ↓
modified / reference changed
   ↓
de-assigned
```

A historical port table must preserve time, not merely the current owner of a number.

## 8. Assigned Numbers RFCs froze port history too

RFC 1340 and RFC 1700 contain historical tables of well-known and registered ports.

They are snapshots of what the Internet believed its service namespace looked like at a particular moment.

For archaeology, comparing those RFCs with today's live IANA registry can reveal:

- classic services whose numbers never moved;
- renamed services;
- abandoned assignments;
- later additions;
- changes in registration references and authority.

## 9. RFC 3232 changes how assigned numbers are published

RFC 3232 formally obsoleted RFC 1700 because assigned-number information had moved to an online IANA database.

This means the port-number story includes an archival-media transition:

```text
periodic standards-track RFC snapshot
          ↓
live continuously updated registry
```

The numbers themselves may remain stable while the institution maintaining and publishing them becomes more dynamic.

## 10. Service names add another layer

Modern IANA policy treats service names as first-class identifiers alongside port numbers.

This matters because human-readable names can be used in APIs/configuration even when applications use dynamically negotiated ports or multiple transports.

The genealogy therefore is not simply:

```text
number → service
```

but increasingly:

```text
service name
   ↕
transport-specific port registration(s)
   ↕
application protocol / discovery mechanism
```

## 11. Port numbers and discovery protocols can coexist

DNS SRV, SVCB/HTTPS and application-specific discovery do not make the port registry disappear.

Instead modern systems often combine:

- a default/well-known port;
- DNS/service discovery;
- explicit configuration;
- protocol negotiation.

An old numeric rendezvous convention becomes one layer in a richer discovery stack.

## 12. Root-hunting from `/etc/services`

A future exhibit should compare:

```text
RFC 1340 Assigned Numbers
RFC 1700 Assigned Numbers
current IANA registry
BSD /etc/services
modern Linux /etc/services
packet captures / firewall rules
```

That would show how institutional assignments propagate into local operating-system artifacts.

## 13. Why ports feel natural

People often say "HTTPS is 443" as though it were a property of HTTPS itself.

Historically it is better understood as:

> a durable shared convention whose success made the arbitrary number appear inevitable.

That is exactly the kind of thing root-hunting should make visible again.

## Sources

- IANA Service Name and Transport Protocol Port Number Registry: https://www.iana.org/assignments/service-names-port-numbers/
- RFC 6335 — Internet Assigned Numbers Authority Procedures for the Management of the Service Name and Transport Protocol Port Number Registry: https://www.rfc-editor.org/info/rfc6335/
- RFC 1340 — Assigned Numbers: https://www.rfc-editor.org/info/rfc1340/
- RFC 1700 — Assigned Numbers: https://www.rfc-editor.org/info/rfc1700/
- RFC 3232 — RFC 1700 is Replaced by an On-line Database: https://www.rfc-editor.org/info/rfc3232/

## Next excavation

- row-by-row port diff: RFC 1340 → RFC 1700 → current IANA;
- exact earliest documented assignment dates for FTP/Telnet/SMTP/DNS/HTTP/BGP;
- `/etc/services` genealogy in Research Unix/BSD/Linux;
- registered-port boom in commercial Internet software;
- de-assigned and repurposed-port cemetery;
- QUIC/UDP and service-name continuity around port 443;
- service discovery versus default-port interaction.
