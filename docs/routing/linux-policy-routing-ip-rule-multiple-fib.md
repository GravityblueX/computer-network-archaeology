# Linux policy routing: from one destination lookup to RPDB + multiple FIB tables

## The classic model

The simplest Internet routing model asks:

```text
where is the destination address?
        ↓
longest-prefix match
        ↓
next hop / output interface
```

That model remains the default mental picture, but modern Linux can make route selection depend on more than destination prefix.

## RPDB adds a rule-selection layer before route lookup

`ip-rule(8)` explicitly describes the Routing Policy Database (RPDB) as the mechanism used when routing must depend on fields such as:

- source prefix;
- destination prefix;
- incoming/output interface;
- TOS/DS field;
- fwmark;
- UID range;
- IP protocol;
- source/destination transport ports.

The architecture becomes:

```text
packet/context
      ↓
ordered RPDB rules
      ↓
select action / routing table
      ↓
lookup selected FIB table
      ↓
next hop
```

## Multiple tables are not merely several copies of `route -n`

Linux reserves familiar table IDs/names such as `local`, `main`, and `default`, while administrators and routing software can use additional tables. The default RPDB rules preserve ordinary routing behavior by looking up the standard tables in priority order.

So policy routing is best understood as an **extension around classic destination routing**, not its deletion.

## Policy and topology separate

A route table says which forwarding paths exist under that table's view. A policy rule says which table/action should be consulted for a packet/context.

This allows:

```text
same destination prefix
+
different source / mark / interface
→ different selected table
→ different next hop
```

That capability underlies multi-homing, source-sensitive routing, VRF/l3mdev behavior and many modern network-namespace designs.

## `ip rule` is an operator view of kernel lookup policy

The archaeological chain is:

```text
single/default destination-oriented FIB view
          ↓ role expanded
routing-policy database + multiple FIB tables
          ↓ rtnetlink/iproute2 administration
       ip rule / ip route table ...
```

Do not describe RPDB as a routing protocol. BGP/OSPF/etc. may install information that ends up in tables/rules, but RPDB is a local kernel forwarding-policy mechanism.

Primary anchor:

- `ip-rule(8)`: https://man7.org/linux/man-pages/man8/ip-rule.8.html
