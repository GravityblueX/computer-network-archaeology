# DSCP → ECN: One IPv4 Octet, Two Different Modern Meanings

The first byte after Version/IHL in the IPv4 header is a small archaeological site by itself.

RFC 791 described an 8-bit Type of Service (TOS) field. Later standards reused the same wire location for a Differentiated Services field, then subdivided its low-order bits for Explicit Congestion Notification.

The byte survived. Its semantics changed twice.

## 1. RFC 791: Type of Service

The original TOS field combined precedence with service preferences such as delay, throughput, and reliability.

The important point for root-hunting is that the byte was never merely "reserved." It carried an explicit traffic-treatment model from the beginning.

## 2. RFC 2474: Differentiated Services field

RFC 2474 redefined the IPv4 TOS octet and IPv6 Traffic Class octet as the Differentiated Services field.

The high six bits became the Differentiated Services Codepoint (DSCP), selecting a per-hop behavior.

That gives us a classic semantic-replacement edge:

```text
same wire octet
  ↓
old TOS interpretation
  ↓ redefined
DS field / DSCP interpretation
```

This is not a new header field in a new packet format. It is a new contract over the old location.

## 3. RFC 3168: ECN occupies the remaining two bits

RFC 3168 updates RFC 2474 and defines Explicit Congestion Notification using the low two bits of the same IP header byte.

The byte becomes:

```text
+-------------------+----+
|      DSCP         |ECN |
|      6 bits       |2bit|
+-------------------+----+
```

This is a particularly elegant example of standards archaeology:

- 1981 establishes the byte;
- 1998 redefines its main semantics as DSCP;
- 2001 gives the remaining two bits a congestion-signaling role.

## 4. ECN changes the congestion signal

Classic TCP congestion control inferred congestion primarily from loss.

ECN permits a cooperating network to mark congestion without necessarily dropping the packet. RFC 3168 also updates TCP by introducing ECN-Echo and Congestion Window Reduced signaling in TCP control bits.

Thus one change crosses layers:

```text
IP header bits
   ↕
router queue/congestion behavior
   ↕
TCP endpoint feedback
```

A two-bit allocation in the IP header therefore modifies end-to-end transport behavior.

## 5. Why this is not just QoS history

DSCP and ECN are often taught separately:

- DSCP under QoS;
- ECN under congestion control.

But physically they share one byte because of historical reuse.

A packet capture today therefore exposes at least three historical layers in the same octet:

1. RFC 791 TOS ancestry;
2. RFC 2474 DSCP reinterpretation;
3. RFC 3168 ECN subdivision.

## 6. Tunnels create another archaeological layer

Once the DS/ECN bits became meaningful, tunneling protocols had to decide how to copy, combine, or preserve the outer and inner header states.

That is why later RFCs such as RFC 6040 exist: old header bits became inputs to new encapsulation semantics.

This is a recurring theme in networking history:

> a field that survives long enough eventually becomes someone else's compatibility problem.

## 7. Modern afterlife

ECN did not stop evolving with RFC 3168. Later work relaxed experimentation constraints and introduced more accurate feedback mechanisms.

The root is nevertheless visible:

```text
RFC 791 TOS octet
       ↓
RFC 2474 DS field
       ↓
   DSCP + ECN
       ↓
modern QoS and congestion signaling
```

## 8. Archaeological classification

### Wire location

**Survives.** Same basic IPv4 header octet.

### Original TOS interpretation

**Superseded / transformed.** Do not interpret modern DSCP bits as if the original TOS service-selection model were unchanged.

### DSCP

**Living.** Widely present in operating systems, routers, firewalls, traffic shapers and packet captures.

### ECN

**Living and evolving.** The bit allocation survives while transport feedback mechanisms continue to develop.

## Sources

- RFC 791 — Internet Protocol: https://www.rfc-editor.org/rfc/rfc791.html
- RFC 2474 — Definition of the Differentiated Services Field: https://www.rfc-editor.org/info/rfc2474/
- RFC 3168 — The Addition of Explicit Congestion Notification (ECN) to IP: https://www.rfc-editor.org/info/rfc3168/
- RFC 6040 — Tunnelling of Explicit Congestion Notification: https://www.rfc-editor.org/info/rfc6040/

## Next excavation

- TOS precedence/service-bit deployments before DSCP;
- IP Precedence in Cisco and early router configuration;
- DiffServ PHB genealogy (EF/AF/default);
- Linux `tc`, BSD ALTQ and router QoS implementation history;
- ECN TCP flag and handshake evolution;
- AccECN lineage;
- packet-capture examples showing one octet interpreted across four decades.
