# From `/etc/hosts` to `getaddrinfo()`: Resolver Interfaces Outlive Their Backends

## Why this is root-hunting

A modern Unix application can contain one apparently simple call:

```c
getaddrinfo("www.example.com", "https", &hints, &res);
```

That call sits on top of several historical layers that were created for different problems and at different times:

```text
static host tables / /etc/hosts
          +
Assigned Numbers / service-name databases
          +
BSD host/service lookup interfaces
          +
DNS resolver libraries
          +
NIS/NSS backend dispatch
          +
IPv4/IPv6 protocol-independent socket API
          ↓
      getaddrinfo()
          ↓
 sockaddr objects ready for socket/connect/sendto
```

The key lesson is that **the lookup interface can survive while the backing database changes completely**.

---

## 1. Static host tables became a Unix-local administrative surface

The host-table world predates DNS. On Unix systems this history survives in `/etc/hosts`, which stores textual mappings between network addresses and host names.

Even after DNS became the dominant global naming system, `/etc/hosts` did not disappear. It remained useful for:

- bootstrap;
- local overrides;
- isolated networks;
- recovery when DNS is broken;
- installation environments;
- testing;
- deliberate name shadowing.

This is therefore not a simple replacement chain:

```text
/etc/hosts  --X-->  DNS
```

A more accurate modern picture is:

```text
                 lookup policy
                /             \
        local hosts file      DNS
                \             /
                 libc resolver API
```

The old file survives as one selectable source.

---

## 2. BSD resolver code made DNS a library service

The DNS architecture deliberately includes a **resolver** between applications and name servers.

RFC 1034 describes resolvers as programs that interface user programs to domain name servers. It also describes the possibility of a small **stub resolver** that forwards work to a recursive server rather than implementing the entire resolution algorithm locally.

BSD made this architecture concrete in a widely deployed Unix API and configuration surface. Historical resolver interfaces include routines such as:

```text
res_init
res_mkquery
res_send
res_query
res_search
```

and configuration in:

```text
/etc/resolv.conf
```

This created an important separation:

```text
application
    ↓
resolver library
    ↓
configured recursive server(s)
    ↓
DNS hierarchy
```

The application therefore need not implement DNS packet formatting, retries, search lists or nameserver selection itself.

---

## 3. `gethostbyname()` exposed an IPv4-shaped API

Classic BSD networking exposed lookup interfaces including:

```c
gethostbyname()
gethostbyaddr()
getservbyname()
getservbyport()
getprotobyname()
getprotobynumber()
```

These were extremely successful because they hid files and protocol-number tables behind C library calls.

But `gethostbyname()` and the associated `hostent` model were strongly shaped by the IPv4 era. As IPv6 arrived, simply making the old interface return a larger address was not a clean solution.

This is a recurring historical pattern:

> an abstraction can be successful enough to become a compatibility constraint.

---

## 4. `getaddrinfo()` combines name lookup with socket construction

RFC 2553 (1999) describes a **protocol-independent nodename and service-name translation** interface taken from the POSIX 1003.1g protocol-independent interface work:

```c
int getaddrinfo(const char *nodename,
                const char *servname,
                const struct addrinfo *hints,
                struct addrinfo **res);
```

The design is broader than DNS.

The caller can supply:

- a node name **or** numeric address;
- a service name **or** numeric port;
- desired address family;
- socket type;
- protocol.

The result contains one or more complete socket-address candidates.

Conceptually:

```text
"example.com" + "https"
        ↓
name/service resolution
        ↓
family + socktype + protocol selection
        ↓
AF_INET / AF_INET6 sockaddr
        ↓
connect() / sendto()
```

This combines several older namespaces behind one call.

---

## 5. The service-name database is part of `getaddrinfo()` history

`getaddrinfo()` does not only replace host-name lookup.

The `servname` argument may be a symbolic service such as:

```text
http
https
smtp
ssh
```

or a decimal port number.

That means the API conceptually joins two old lookup worlds:

```text
host name → address
service name → port/transport
```

The service-name side descends from the same Assigned-Numbers-to-Unix-database history preserved by `/etc/services` and `getservbyname()`.

Therefore a call such as:

```c
getaddrinfo("mail.example", "smtp", ...)
```

is simultaneously invoking descendants of **host naming** and **service-number naming**.

---

## 6. RFC 2553 preserves design provenance

RFC 2553 contains unusually useful historical attribution.

It says that `getaddrinfo()` is taken from the POSIX protocol-independent interface work and notes earlier design work by Keith Sklower. It credits Eric Allman with implementing an early prototype and records the observation that a **name + service pair** can be sufficient to connect independently of protocol details.

This makes `getaddrinfo()` a good lineage object because the design ancestry is documented rather than inferred from similarity.

RFC 3493 (2003) later became the widely cited Basic Socket Interface Extensions for IPv6 specification and obsoleted RFC 2553.

The protocol-independent lookup interface therefore has its own standards genealogy:

```text
BSD host/service lookup APIs
       +
POSIX protocol-independent interface work
       ↓
RFC 2133 / RFC 2553 generation
       ↓
RFC 3493
       ↓
modern getaddrinfo()/getnameinfo()
```

The exact POSIX/IETF revision sequence should be preserved separately from implementation deployment dates.

---

## 7. NSS means the API does not prove the backend

On a system with a Name Service Switch, a call such as:

```c
getaddrinfo("host", "https", ...)
```

can involve a dispatch graph rather than one database:

```text
getaddrinfo
    ↓
libc / NSS
    ├── files
    ├── dns
    ├── nis
    ├── cache
    ├── directory service
    └── other module
```

This gives an important archaeological warning:

> Seeing `getaddrinfo()` or `gethostbyname()` in source code does **not** prove which naming backend was used on a particular machine.

To reconstruct the real path, one must also know:

- operating-system release;
- libc implementation;
- NSS configuration;
- `/etc/hosts` contents;
- resolver configuration;
- NIS/directory availability;
- local caching daemons.

---

## 8. `AI_NUMERICHOST` exposes the abstraction boundary

RFC 2553 defines `AI_NUMERICHOST` specifically to require a numeric node address and prevent a name-resolution service such as DNS from being called.

This is revealing because it makes the hidden backend work explicit:

```text
normal getaddrinfo
    → may invoke naming services

AI_NUMERICHOST
    → parse numeric address only
```

A flag in a late-1990s socket API therefore exposes the cost and side effects of the much older naming-service layer underneath it.

---

## 9. `getnameinfo()` completes the reverse direction

The complementary interface maps a socket address back into textual node and service names:

```text
sockaddr
   ↓
getnameinfo()
   ↓
host name + service name
```

Again, this is not merely reverse DNS. Service-port naming can also be involved, and the system may use local databases or configured name services.

So the API combines multiple registries behind one representation boundary.

---

## 10. What survived and what changed

### Survived

- symbolic host names;
- symbolic service names;
- local host-file override capability;
- C library lookup abstraction;
- resolver as application-facing intermediary;
- `sockaddr` as the socket API address carrier.

### Changed

- static global host-table distribution largely disappeared;
- DNS became hierarchical and delegated;
- backend selection became configurable;
- IPv6 required protocol-independent address handling;
- lookup results became lists of candidate socket addresses rather than one IPv4-oriented host record.

### Still visible today

```text
/etc/hosts
/etc/resolv.conf
/etc/nsswitch.conf
<netdb.h>
getaddrinfo()
getnameinfo()
EAI_*
AI_NUMERICHOST
```

These are ordinary current Unix interfaces and also archaeological layers.

---

## 11. Root-hunting checklist

For one historical Unix host or modern Unix descendant, preserve:

- `/etc/hosts`;
- `/etc/resolv.conf`;
- NSS configuration;
- resolver library version/source;
- `getaddrinfo` implementation source;
- DNS server addresses;
- search/domain rules;
- service database source;
- packet capture of resolver traffic;
- application source showing the lookup API used.

That allows the archive to answer not only:

> “What name-resolution standard existed?”

but:

> **“What exact lookup path did this application traverse on this system?”**

---

## Primary anchors

- RFC 1034, *Domain Names — Concepts and Facilities*.
- RFC 2553, *Basic Socket Interface Extensions for IPv6*.
- RFC 3493, *Basic Socket Interface Extensions for IPv6*.
- historical BSD `resolver(3)`, `hosts(5)` and `resolv.conf(5)` documentation preserved in structured source records.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
