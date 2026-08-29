# `/etc/hosts` → Resolver Library → DNS Stub → `getaddrinfo()`: Name Resolution Moves Behind an API

## Why this is a root-hunting story about interfaces, not just DNS

A modern program can often do something as simple as:

```c
getaddrinfo("example.com", "https", ...)
```

and receive one or more socket addresses suitable for `connect()`.

That apparently small call can hide decades of accumulated machinery:

```text
application name + service
       ↓
protocol-independent lookup API
       ↓
name-service dispatcher
   ┌────┼─────────┐
 files  DNS      other backends
   │     │
/etc/hosts   stub resolver
              ↓
         recursive/authoritative DNS
              ↓
        A / AAAA / other data
       ↓
service name → transport/port mapping
       ↓
struct addrinfo / sockaddr
       ↓
connect()
```

The main historical lesson is that **old naming mechanisms were repeatedly hidden behind new interfaces rather than simply deleted**.

---

## 1. `/etc/hosts`: the local static host database

The classic Unix hosts file maps:

```text
Internet address   official host name   aliases...
```

BSD manual history traces the file format to the early BSD networking era; surviving manuals variously identify 4.1cBSD/4.2BSD lineage depending on edition and documentation ancestry.

Historical descriptions preserve an important institutional fact: the file could be created from the official host database maintained by the Network Information Control Center (NIC), with local changes required for unofficial aliases or hosts unknown to the central database.

This gives the same projection pattern already seen in `/etc/networks`:

```text
central NIC host database
       ↓ distribution
local /etc/hosts
       ↓ local aliases/bootstrapping entries
host lookup API
```

The local file was never identical to the central institution that supplied much of its data.

### 1.1 Why it survived DNS

Modern BSD documentation still treats `/etc/hosts` as useful beside DNS/NIS and as a fallback/bootstrapping source.

So DNS did not erase the file.

Instead:

```text
static host table
      ↓ remains useful locally
DNS distributed hierarchy
      ↓ added as network source
NSS / resolver policy
      ↓ orders or combines sources
```

The ancestor survives as one backend.

---

## 2. DNS introduces a resolver role, not just a name-server protocol

RFC 1034 explicitly separates:

```text
user program
resolver
name server
```

It describes resolvers as programs that interface user programs such as mail, TELNET or FTP to domain name servers.

The user program normally does **not** construct DNS queries directly.

Instead it asks a resolver for information in a local-machine-friendly form.

That separation is crucial:

```text
application naming API
       ≠
DNS wire protocol
```

An application can depend on a name-resolution interface without knowing whether DNS packets are sent, whether a local cache answers, or whether some other database satisfies the request.

---

## 3. Stub resolvers: move the hard work off the host

RFC 1034 describes a particularly durable model: the **stub resolver**.

A resource-constrained host can keep only a small local component plus a list of recursive name-server addresses.

The remote server performs recursion and can share a cache across many clients.

Conceptually:

```text
application
   ↓ local resolver call
stub resolver
   ↓ one recursive query
recursive name server
   ├── cache
   ├── referrals
   └── authoritative queries
```

This is still recognizable in many modern host configurations.

The resolver on the endpoint need not be a full DNS resolver algorithm implementation.

---

## 4. `/etc/resolv.conf`: configuration appears beside the stub

BSD resolver documentation says the `resolv.conf` file format appeared in **4.3BSD**.

The file provides configuration such as:

```text
nameserver
search/domain
resolver options
```

This is another important separation:

```text
/etc/hosts
  = local name/address data

/etc/resolv.conf
  = configuration for where/how DNS resolution should be attempted
```

They can coexist because they do different jobs.

The classic BSD resolver routines include functions such as:

```c
res_init()
res_mkquery()
res_send()
res_query()
res_search()
```

Historical manuals trace resolver routines to the **4.3BSD** period, with some functions appearing in 4.3BSD and `res_query`/`res_search` documented in later 4.3BSD-Tahoe lineage depending on the manual tree.

This is implementation history that should be mapped release-by-release rather than flattened into one date.

---

## 5. `gethostbyname()` hides the DNS packet machinery

Classic Unix applications frequently used:

```c
gethostbyname()
gethostbyaddr()
```

These APIs return `hostent`-style data rather than DNS message sections.

That allows an application to think in terms of:

```text
host name → address
```

while the implementation may use:

```text
/etc/hosts
DNS
NIS
cache
```

or combinations selected by system policy.

A root-hunting record must therefore distinguish:

- lookup API;
- dispatcher policy;
- resolver library;
- DNS wire query;
- recursive server;
- local static database.

---

## 6. IPv6 exposes a limitation in the old API

RFC 2553 states plainly that the sockets interface was the de-facto TCP/IP API, developed for Unix in the early 1980s, but that IPv6 requires changes because address size and other details were visible to applications.

The older host lookup functions also expose an address-family-specific world.

Rather than breaking them, IPv6 socket API work introduced a new protocol-independent path.

This produced one of the most important modern network APIs:

```c
getaddrinfo()
```

RFC 2553 describes `getaddrinfo()` as taking a node name and service name and returning socket-address structures.

RFC 3493 later became the successor specification in that lineage.

---

## 7. `getaddrinfo()` joins two old registries behind one call

This is especially beautiful from a root-hunting perspective.

The call:

```c
getaddrinfo("example.com", "https", ...)
```

contains two different naming problems:

```text
"example.com"
      ↓ node/name resolution
DNS or another host database
      ↓ IP address(es)

"https"
      ↓ service-name resolution
service database / port registry knowledge
      ↓ port + socket type/protocol constraints
```

The result combines them into:

```text
struct addrinfo
   ai_family
   ai_socktype
   ai_protocol
   ai_addr
```

RFC 3493 explicitly describes the function as translating a node and/or service name into a set of socket addresses and associated information suitable for creating/addressing a socket.

So one modern API is the meeting point of:

- DNS/host-table lineage;
- service/port-number lineage;
- BSD socket lineage;
- IPv4/IPv6 dual-stack lineage.

---

## 8. `getnameinfo()` performs the reverse abstraction

The complementary function:

```c
getnameinfo()
```

maps a socket address back toward:

```text
node name
service name
```

RFC 3493 even preserves a subtle reminder that service identity depends on transport semantics: the `NI_DGRAM` flag exists because some numeric ports historically name different services for UDP and TCP.

Thus even a reverse-lookup convenience API retains the old rule:

> port number alone is not always the full service identity.

---

## 9. API compatibility was an explicit design goal

RFC 3493 says the IPv6 socket changes should preserve source and binary compatibility for existing applications where possible.

That is the exact pattern this repository keeps finding:

```text
underlying address model changes radically
         ↓
old applications should keep working
         ↓
new API added beside old API
         ↓
old interface remains for compatibility
```

The history is additive and layered, not a clean replacement.

---

## 10. DNS cache can move between process, host and network

RFC 1034 points out that resolver caches shared by many processes/users/machines are more efficient than isolated caches.

That observation creates several possible implementation placements:

```text
application-local cache
libc/resolver cache
local caching daemon
recursive resolver on LAN
ISP/public recursive resolver
```

The resolver interface can remain similar while cache ownership migrates outward.

So another genealogy axis is:

```text
where does state live?
```

not merely:

```text
which protocol is used?
```

---

## 11. Why `hosts: files dns` is historically profound

An NSS rule such as:

```text
hosts: files dns
```

places two very different historical systems into one ordered policy:

```text
local static host table
      ↓ first
hierarchical distributed DNS
      ↓ second
```

The operating system does not force the historian to choose a winner.

It executes both lineages.

This is a literal example of **historical coexistence encoded as configuration**.

---

## 12. Root-hunting chain

A modern call can therefore be expanded as:

```text
getaddrinfo("host", "service")
      ↓
NSS / name-service dispatcher
      ├── /etc/hosts
      ├── DNS stub resolver
      │      ↓ /etc/resolv.conf
      │   recursive resolver
      └── other configured sources
      ↓
node addresses
      +
service/port mapping
      ↓
sockaddr candidates
      ↓
socket()/connect()
```

Every layer has its own ancestry.

---

## 13. Sources and future archive targets

Primary/current anchors:

- RFC 1034 — resolver and stub-resolver architecture:
  - https://www.rfc-editor.org/info/rfc1034/
- RFC 2553 — protocol-independent name/service translation and early `getaddrinfo()` specification:
  - https://www.rfc-editor.org/info/rfc2553/
- RFC 3493 — successor IPv6 socket API specification:
  - https://www.rfc-editor.org/info/rfc3493/
- historical BSD resolver manual:
  - https://man.freebsd.org/cgi/man.cgi?manpath=4.3BSD+Reno&query=resolver&sektion=3
- BSD `resolv.conf(5)` history:
  - https://man.freebsd.org/cgi/man.cgi?query=resolv.conf&sektion=5
- BSD/descendant `hosts(5)` history:
  - https://man.freebsd.org/cgi/man.cgi?query=hosts&sektion=5

High-value next artifacts:

- exact 4.1c/4.2BSD hosts file and `gethostbyname()` sources;
- first 4.3BSD resolver library source;
- BIND resolver code shared with libc;
- `resolv.conf` revision diffs;
- NetBSD/FreeBSD/glibc NSS host dispatch;
- first `getaddrinfo()` prototype by Eric Allman mentioned in RFC 2553/3493 acknowledgments.

## 14. Root-hunting summary

The simple story:

```text
HOSTS file → DNS
```

is insufficient.

The deeper genealogy is:

```text
static host data ─────────────┐
                             │
DNS resolver architecture ───┼→ host lookup interface
                             │
NIS/NSS backends ────────────┘
                                     ↓
IPv4-specific host APIs
                                     ↓ coexist
protocol-independent getaddrinfo()
                                     ↓
node + service → ready-to-use socket address
```

The most durable artifact is not one file or one DNS message.

It is the **interface contract that lets old applications ask for a name while the machinery behind the question keeps changing**.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
