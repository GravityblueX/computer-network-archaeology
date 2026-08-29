# glibc NSS vs BSD nsdispatch: Same Name-Service Problem, Different Code Lineages

## The tempting but dangerous simplification

Modern Unix-like systems often expose a configuration file named:

```text
/etc/nsswitch.conf
```

and resolve databases such as:

```text
hosts
networks
services
protocols
passwd
group
```

through selectable backends such as:

```text
files
dns
nis
compat
cache
```

That visual similarity makes it tempting to draw one neat family tree:

```text
Solaris NSS → glibc NSS → BSD NSS
```

or:

```text
Solaris NSS → BSD NSS → glibc NSS
```

The historical evidence does **not** support either simple line.

Instead, the same administrative problem produced multiple implementations that borrowed ideas, terminology and configuration style while retaining different internal interfaces and code bases.

---

## 1. The common problem: fixed lookup paths stopped scaling

Classic C library database lookups were strongly associated with local files:

```text
gethostbyname()  → /etc/hosts
getservbyname()  → /etc/services
getprotobyname() → /etc/protocols
```

As NIS and DNS became common, systems accumulated ad-hoc logic such as:

```text
try local file
then try NIS
then try DNS
```

The problem was not only performance. Administrators needed to choose:

- which source was authoritative for each database;
- lookup order;
- fallback behavior;
- what to do on not-found versus temporary failure;
- whether local overrides should beat network data.

This creates the architectural requirement:

```text
stable libc lookup API
        ↓
configurable dispatcher
        ↓
multiple backend modules
```

---

## 2. Solaris supplied the model and the name for glibc NSS

The GNU C Library manual is unusually explicit about provenance.

It says glibc's Name Service Switch was **designed after a method used by Sun Microsystems in the Solaris 2 C library** and deliberately follows Sun's name, NSS.

That establishes a real design influence:

```text
Solaris 2 name-service switch method
        ↓ documented design influence
glibc NSS
```

But the same glibc manual immediately adds a crucial negative claim:

> although the interfaces may look similar, there is no common code; the GNU developers had not seen Sun's implementation source, and the internal interface is incompatible.

That sentence is almost a perfect example of why this repository stores **negative lineage evidence**.

The correct relationship is:

```text
same design idea / terminology
        ↓
independent implementation
```

not:

```text
Sun source → glibc source
```

---

## 3. glibc turns the backend into loadable modules

The GNU model separates database APIs from backend modules.

Conceptually:

```text
gethostbyname / getaddrinfo / getservbyname
              ↓
          glibc NSS
     ┌────────┼─────────┐
     ↓        ↓         ↓
   files     dns       nis
     ↓        ↓         ↓
module implementation / backend-specific data
```

The configuration specifies a database and ordered sources.

A typical host lookup policy can look like:

```text
hosts: files dns
```

The current glibc manual notes that the default for `hosts` and `networks` is commonly `files dns` when no explicit configuration is present.

This means a static local file and DNS are not historical alternatives that necessarily replace one another; they can remain **cooperating runtime backends** decades later.

---

## 4. BSD nsdispatch has its own documented influence chain

The BSD side has a different provenance trail.

NetBSD documentation records that its NSS/nsdispatch design drew ideas from:

```text
ULTRIX svc.conf
Solaris nsswitch.conf
        ↓
NetBSD nsdispatch/NSS
        ↓ import
FreeBSD NSS
```

This was already captured separately in this repository.

The important point is that **both glibc NSS and BSD nsdispatch can cite Solaris ideas without being the same implementation lineage**.

The diagram is therefore closer to:

```text
                    Solaris NSS ideas
                     /            \
                    /              \
          glibc independent       NetBSD nsdispatch
          implementation                ↓
                                     FreeBSD

ULTRIX svc.conf ideas ────────────────┘
```

---

## 5. Similar `/etc/nsswitch.conf` does not imply compatible modules

Two systems may both say:

```text
hosts: files dns
```

while differing in:

- module ABI;
- module file naming;
- return-status representation;
- threading behavior;
- caching;
- internal dispatcher APIs;
- which databases are supported;
- source-specific actions and syntax.

Configuration resemblance is therefore a **surface compatibility/convention**, not proof of binary or source compatibility.

This is a general archaeology lesson:

> human-readable configuration syntax can converge even when implementation internals diverge.

---

## 6. glibc preserves the old API while changing the machinery behind it

A program compiled against classic APIs can continue calling:

```c
getservbyname()
getprotobyname()
gethostbyname()
```

while glibc routes the request through NSS modules instead of opening one fixed file.

The old function name therefore stops meaning:

```text
this function reads this file
```

and instead means:

```text
this function requests a logical database lookup
```

The storage and authority become configurable.

This is one of the strongest examples of **API survivorship under backend replacement**.

---

## 7. `getaddrinfo()` deepens the abstraction

When protocol-independent lookup arrives, an application can ask for:

```text
node name + service name
```

and receive candidate socket addresses.

On glibc systems, that operation can itself interact with NSS host and service databases.

Thus a modern path may look like:

```text
application
   ↓ getaddrinfo()
glibc
   ↓ NSS dispatch
files / DNS / NIS / other
   ↓
address + service resolution
   ↓
sockaddr candidates
```

The function belongs to the socket API lineage; the backend dispatcher belongs to NSS; DNS belongs to a protocol lineage; `/etc/hosts` belongs to static-file practice.

One call crosses all four histories.

---

## 8. The old `+` compatibility mechanism reveals the migration path

Historical Unix systems sometimes used a `+` convention in local files to splice network-directory data into a file-oriented view.

Later NSS makes this backend composition explicit in a dispatcher configuration.

The sequence is conceptually:

```text
pure local file
    ↓
file with magic network-directory inclusion
    ↓
fixed library search order
    ↓
explicit configurable backend switch
```

The awkward transitional forms are historically important because clean modern abstractions hide how migration actually happened.

---

## 9. What survives today

Still visible:

```text
/etc/nsswitch.conf
files
dns
nis
gethostby*
getservby*
getproto*
getaddrinfo()
```

But the hidden implementation differs significantly between libc/OS families.

A root-hunting record for a specific system must therefore capture:

- libc and version;
- NSS implementation family;
- `nsswitch.conf` contents;
- loaded backend modules;
- `/etc/hosts`, `/etc/services`, `/etc/protocols`;
- resolver configuration;
- caching services;
- source code for the dispatcher and modules.

---

## 10. Negative lineage claims to preserve

The archive should explicitly store:

1. **Solaris NSS influenced glibc NSS, but glibc says there is no common source code and the internal interface is incompatible.**
2. NetBSD/FreeBSD nsdispatch has its own documented implementation lineage and should not be treated as glibc NSS source ancestry.
3. Shared `nsswitch.conf` terminology does not establish shared module ABI.
4. A lookup API call does not prove a particular backend was consulted.

These negative claims are as valuable as positive ancestry.

---

## Primary anchors

- GNU C Library manual, *System Databases and Name Service Switch*.
- NetBSD 1.4 `nsswitch.conf(5)` provenance.
- FreeBSD `nsswitch.conf(5)` import/provenance documentation.
- existing repository excavation: `nis-nss-name-service-switch.md`.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
