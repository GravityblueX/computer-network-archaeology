# From Flat Files to NIS and NSS: The Name-Service Backend Becomes Pluggable

## The interface survives while the database moves

Early Unix network software often appears to imply a direct relationship:

```text
getservbyname()
      ↓
/etc/services
```

or:

```text
gethostbyname()
      ↓
/etc/hosts
```

That picture is historically useful but eventually becomes false.

Unix descendants introduced mechanisms that preserve the **lookup API** while allowing the actual data source to move between:

```text
local files
NIS / YP
DNS
compiled local databases
caches
directory services
other modules
```

This is one of the clearest examples of interface survivorship in the entire networking stack.

---

## 1. The problem: static files do not scale administratively

Classic manuals repeatedly complain that a name server should replace static files.

The reason is straightforward.

Suppose one site has 100 machines, each with local copies of:

```text
/etc/hosts
/etc/networks
/etc/services
/etc/protocols
/etc/ethers
```

A central change now creates a distribution problem:

```text
one authority changes a mapping
        ↓
100 local copies become stale
        ↓
operators distribute replacements
        ↓
local edits conflict with central edits
```

This is the same family of operational pressure that made HOSTS.TXT untenable at Internet scale, although the technical solutions and namespaces differ.

---

## 2. YP/NIS: publish Unix databases as network maps

Sun's Yellow Pages, later renamed **Network Information Service (NIS)**, allowed Unix administrative databases to be served across a network.

For a database such as `/etc/ethers`, historical manuals refer to maps such as:

```text
ethers.byname
ethers.byaddr
```

Services similarly appear in NIS map form.

The conceptual change is:

```text
file parsed locally
       ↓
file transformed into keyed network map
       ↓
client library consults network service
```

Yet an application may still call a familiar lookup function.

So the application-facing contract survives while the administrative location of truth moves.

---

## 3. The `+` convention: network database inserted into a file view

Some historical BSD/Sun-derived file formats used a special `+` line to request NIS data.

This is a particularly striking transition artifact because it literally embeds the network directory into the syntax of the local file:

```text
local entries
+
more local entries
```

Conceptually the `+` means:

```text
splice network-distributed records here
```

This is neither a pure local file nor a fully abstract backend system.

It is a transitional hybrid.

Such mechanisms are worth preserving because clean later APIs often erase the awkward intermediate steps by which systems migrated.

---

## 4. NSS: separate the lookup API from the lookup source

The Name Service Switch makes the source-selection problem explicit.

A modern FreeBSD `nsswitch.conf(5)` describes a configuration that controls how C-library name-service dispatcher routines choose among sources such as:

```text
files
DB
dns
nis
compat
cache
```

An entry can look conceptually like:

```text
hosts: files dns
```

meaning:

```text
query local file first
      ↓ if not found / policy permits
query DNS
```

Other databases can have their own source order.

The important architectural shift is:

```text
old assumption:
API ≈ particular file

new assumption:
API → dispatch policy → one or more backends
```

The file becomes one backend among several.

---

## 5. FreeBSD's NSS lineage is itself imported

FreeBSD documentation preserves useful provenance:

- the `nsswitch.conf` format appeared in FreeBSD 5.0;
- it was imported from NetBSD;
- NetBSD first had it in NetBSD 1.4;
- Luke Mewburn's implementation used ideas from ULTRIX `svc.conf` and Solaris `nsswitch.conf`.

This is exactly the kind of relationship the lineage system should preserve with different certainty levels:

```text
ULTRIX svc.conf ideas ─┐
                      ├─ documented influence → NetBSD NSS
Solaris nsswitch ─────┘
                              ↓ imported
                         FreeBSD NSS
```

That is much more precise than saying “Unix eventually got NSS.”

---

## 6. One API, many possible stores

The classic network database functions therefore evolve from simple file readers into dispatch interfaces.

Examples include families such as:

```text
gethostby* / getaddrinfo
getnetent / getnetby*
getservby*
getproto*
getrpcent / getrpcby*
```

Depending on the system and configured backend, the answer may come from:

- local text file;
- NIS;
- DNS;
- Hesiod;
- compiled database;
- system directory service;
- cache daemon.

This changes how historians should interpret source code.

A call such as:

```c
getservbyname("http", "tcp")
```

does **not necessarily prove** that the process opened `/etc/services`.

It proves dependence on the service-name lookup interface.

The backing data path must be reconstructed separately for the OS/release/configuration.

---

## 7. A local text file can remain as a canonical administrative surface

Even after backend abstraction, plain files often remain important because they are:

- human-readable;
- easy to edit;
- bootstrapping-friendly;
- available before network services come up;
- convenient fallback sources;
- part of POSIX/Unix administrative expectations.

This is another survival pattern:

```text
new distributed backend appears
       ↓
old file does not necessarily die
       ↓
old file becomes one selectable/fallback backend
```

The descendant architecture is additive rather than purely substitutive.

---

## 8. Compiled local databases: same authority, different representation

Modern FreeBSD `services(5)` documents a compiled local database path such as `/var/db/services.db` selected through NSS configuration.

This is a subtler transformation:

```text
text file
   ↓ database compilation
binary/indexed local DB
   ↓
same service lookup semantics
```

Nothing moved to a remote server; the storage representation changed for lookup performance/administration.

Therefore a complete lineage needs at least three independent axes:

```text
lookup API
storage representation
administrative authority/location
```

Two systems can share an API but use different storage; or share a storage format but assign different authority.

---

## 9. Hosts and networks show DNS entering the dispatch graph

NSS configurations often make the host lookup path especially visible:

```text
hosts: files dns
```

This arrangement preserves both major naming regimes:

```text
/etc/hosts
  ← descendant of local/static host tables

DNS
  ← distributed hierarchical naming system
```

Instead of one simply deleting the other, the OS places them in an ordered dispatch policy.

The modern resolver is therefore another place where historical competitors/ancestors coexist operationally.

---

## 10. Why this matters for root-hunting

Suppose an application asks for `www.example.com` or `smtp/tcp`.

A naive historical diagram might show:

```text
program → file
```

A real modern path could be:

```text
program
  ↓ libc API
NSS dispatcher
  ├── files
  ├── cache
  ├── DNS
  ├── NIS
  └── third-party module
```

The public API may look decades old even when the backend stack is entirely different.

That is a particularly important form of compatibility:

> **old source code can keep compiling while the infrastructure behind the call is replaced.**

---

## 11. Provenance anchors

FreeBSD documents that its `nsswitch.conf` format arrived in FreeBSD 5.0 from NetBSD, where it first appeared in NetBSD 1.4, and that the implementation drew ideas from ULTRIX `svc.conf` and Solaris `nsswitch.conf`.

Useful anchors:

- https://man.freebsd.org/cgi/man.cgi?query=nsswitch.conf
- https://man.freebsd.org/cgi/man.cgi?query=services&sektion=5
- https://man.freebsd.org/cgi/man.cgi?query=networks&sektion=5
- historical NIS/YP manuals and Sun source distributions still to acquire.

---

## 12. Root-hunting summary

The deeper genealogy is:

```text
local Unix text databases
          ↓
NIS/YP network maps
          ↓
backend-selection problem
          ↓
NSS / nsdispatch
      ┌────┼────┬─────┐
    files  nis  dns   db/cache/other
      └────┼────┴─────┘
           ↓
old lookup API still answers caller
```

The point is not that files were replaced by directories.

The point is that **the interface was deliberately detached from the storage and authority behind it**.

That is why very old Unix network lookup APIs can still sit inside modern systems without implying that the modern system works like 4.2BSD internally.

## Next excavation

- NIS/YP original source and map-generation tools;
- NetBSD 1.4 NSS introduction;
- ULTRIX `svc.conf` and Solaris `nsswitch.conf` influence records;
- glibc NSS module ABI versus BSD `nsdispatch`;
- service/protocol/network/RPC backend matrices by operating system;
- trace one `getservbyname()` call from source through libc dispatcher to actual backend.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
