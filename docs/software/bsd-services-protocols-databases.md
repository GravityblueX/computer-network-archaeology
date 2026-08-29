# `/etc/services` and `/etc/protocols`: Assigned Numbers Become a Unix Database

## Why this belongs in root-hunting

A port number in an RFC is only a number until software has a way to turn a human-facing name such as `telnet`, `smtp`, `domain`, or `tftp` into the integer a socket API needs.

Likewise, an IP Protocol Number such as `6` or `17` is only a wire-level identifier until programs can map it to names such as `tcp` or `udp`.

Berkeley Unix made those global Internet assignments locally queryable through two plain-text databases:

```text
/etc/services
/etc/protocols
```

The remarkable part is not merely that these files are old. Their **formats are documented as appearing in 4.2BSD**, and descendants of the same interfaces remain visible in modern Unix-like systems.

This is a clean root-hunting chain:

```text
Internet Assigned Numbers / IANA registries
          ↓ periodically published identities
local Unix text databases
          ↓
libc/netdb lookup functions
          ↓
daemons and user programs
          ↓
socket port / IP protocol integer
```

The global numbering institution and the local operating-system representation are different artifacts. The file is not the registry. It is a local operational projection of registry knowledge.

---

## 1. `/etc/services`

The classic file grammar is conceptually:

```text
service-name   port-number/protocol-name   aliases...
```

A historical example looks like:

```text
telnet  23/tcp
smtp    25/tcp
domain  53/udp
domain  53/tcp
```

The important detail is that **port number alone is not the complete key**. A service mapping is qualified by a transport name. TCP port 53 and UDP port 53 are distinct service records even when the conventional service name is identical.

The 4.4BSD documentation describes a `struct servent`:

```c
struct servent {
    char  *s_name;
    char **s_aliases;
    int    s_port;
    char  *s_proto;
};
```

The port is held in network byte order. The protocol is represented as a string such as `tcp` or `udp`.

The associated API family includes:

```c
getservent()
getservbyname()
getservbyport()
```

A period Berkeley networking document even gives the example:

```c
sp = getservbyname("telnet", "tcp");
```

That is the conceptual bridge from a human-visible service name to the numeric endpoint used by the socket layer.

### 1.1 A concrete 4.2BSD program

The surviving 4.2BSD `tftpd.c` source provides particularly useful evidence because it is not an abstract manual example. The daemon actually contains:

```c
sp = getservbyname("tftp", "udp");
```

and then assigns:

```c
sin.sin_port = sp->s_port;
```

So the chain in a real 1983-era daemon was approximately:

```text
"tftp"
  ↓ getservbyname(..., "udp")
/etc/services / netdb database
  ↓ struct servent
UDP port number
  ↓ sockaddr_in.sin_port
socket binding / service operation
```

This is a valuable implementation artifact because it shows how the Internet Assigned Numbers system became executable local configuration.

---

## 2. `/etc/protocols`

The classic grammar is simpler:

```text
official-protocol-name   protocol-number   aliases...
```

Examples conceptually include:

```text
icmp   1
igmp   2
tcp    6
egp    8
udp    17
```

The old manual describes the file as containing the known protocols used in the **DARPA Internet**.

Modern FreeBSD documentation describes the same family more generally as assigned protocol numbers used by IPv4 and IPv6 to identify the next-level protocol.

That sentence contains decades of history in one small documentation change:

```text
4.2BSD-era wording:
known protocols used in the DARPA Internet

modern wording:
assigned protocol numbers used by IPv4 and IPv6
```

The format survives while the institutional and protocol context around it broadens.

The associated API family is:

```c
getprotoent()
getprotobyname()
getprotobynumber()
```

with the conceptual structure:

```c
struct protoent {
    char  *p_name;
    char **p_aliases;
    int    p_proto;
};
```

Thus a program can move between:

```text
"tcp" ↔ 6
"udp" ↔ 17
"icmp" ↔ 1
```

without hard-coding a private mapping table.

---

## 3. Both file formats are explicitly traced to 4.2BSD

Historical BSD manual pages preserve the same HISTORY statement for both databases:

- the `services` file format appeared in **4.2BSD**;
- the `protocols` file format appeared in **4.2BSD**.

This matters because 4.2BSD is also one of the major implementation points at which DARPA TCP/IP and the Berkeley sockets API became broadly distributable Unix networking machinery.

The files therefore belong to the same implementation ecology as:

```text
socket()
bind()
connect()
listen()
accept()
gethostbyname()
getservbyname()
getprotobyname()
```

They are not protocol specifications. They are **operating-system knowledge about protocol specifications**.

---

## 4. A local cache/projection of a global registry

It is tempting to write:

> `/etc/services` is the IANA port registry.

That is wrong.

A better model is:

```text
central/global assigned-number authority
        ↓ publication / distribution / vendor curation
local operating-system database
        ↓ libc lookup API
application
```

The local file may:

- lag the current registry;
- contain aliases;
- contain local additions;
- include historical services;
- differ between operating systems;
- be supplemented or replaced by a directory/database backend.

So the historical artifact is not merely a copy of IANA data. It is the **Unix interface contract for locally resolving Internet names and numbers**.

---

## 5. The static-file model immediately showed its limits

Old `protocols(5)` and `services(5)` pages contain a revealing BUGS remark:

> a name server should be used instead of a static file.

That sentence is an excellent fossil.

The Unix developers already understood that copying centrally coordinated information into static files has freshness and administration problems.

Later systems therefore gained other backends and integration mechanisms. Examples include:

- NIS maps;
- compiled service databases;
- directory services;
- NSS-style source selection;
- resolver/database APIs that hide the physical storage backend.

A FreeBSD services manual, for example, documents both NIS interaction and a compiled `/var/db/services.db` path selected through `nsswitch.conf`.

The interface therefore undergoes a familiar transformation:

```text
plain file
   ↓
plain file + network directory
   ↓
multiple interchangeable name-service backends
   ↓
API stays familiar
```

Again, **storage mechanism changes while interface semantics survive**.

---

## 6. Why `/etc/services` is still different from DNS

Both are name-to-value systems, but they solve different namespaces.

```text
DNS:
name → host/service-related DNS data

/etc/services / service database:
service-name + transport → port number

/etc/protocols / protocol database:
protocol-name → IP protocol number
```

The fact that all three involve names does not make them one lineage.

The service/protocol databases belong to the Assigned Numbers / socket programming ecology, while DNS belongs to distributed naming and delegation.

---

## 7. Archaeological value of the actual file contents

A historical `/etc/services` or `/etc/protocols` file should be archived revision-by-revision because its contents reveal what a Unix release considered normal enough to name locally.

Potential questions include:

- Which early services were present in 4.2BSD?
- When did `ssh` enter vendor files?
- When did `http` and `https` appear?
- Which obsolete ARPANET services remained for years after real use declined?
- Which protocol numbers were represented by name versus omitted?
- Did vendors preserve obsolete aliases for compatibility?
- How closely did a release track the contemporary Assigned Numbers RFC?

A useful future dataset would look like:

```text
release      service/protocol file      assignment snapshot
4.2BSD       /etc/services              contemporary Assigned Numbers
4.3BSD       /etc/services              later RFC snapshot
4.4BSD-Lite  usr/src/etc/services       RFC 1340/1700 era
modern BSD   /etc/services              live IANA era
modern Linux distro /etc/services       distro-curated live era
```

Then every row can be diffed.

---

## 8. Surviving source and archive targets

High-value sources already identified:

- FreeBSD historical `services(5)` manual pages, which preserve the 4.2BSD origin statement;
- FreeBSD historical `protocols(5)` manual pages, also preserving the 4.2BSD origin statement;
- TUHS 4.4BSD-Lite source archive, including `usr/src/etc/services` and `usr/src/etc/protocols`;
- 4.2BSD source such as `tftpd.c`, demonstrating real `getservbyname()` use;
- 4.4BSD IPC documentation describing `servent`, `getservbyname()`, `getservbyport()` and protocol database structures.

### Primary/current links

- https://man.freebsd.org/cgi/man.cgi?apropos=0&manpath=4.4BSD+Lite2&query=services&sektion=5
- https://man.freebsd.org/cgi/man.cgi?apropos=0&manpath=4.4BSD+Lite2&query=protocols&sektion=5
- https://www.tuhs.org/cgi-bin/utree.pl?file=4.2BSD/usr/src/etc/tftpd.c
- https://www.tuhs.org/cgi-bin/utree.pl?file=4.4BSD/usr/share/doc/psd/21.ipc/3.t
- https://minnie.tuhs.org/ftp/BSD/4.4BSD-Lite/usr/src/

---

## 9. Root-hunting summary

The useful genealogy is:

```text
Assigned Numbers
      ↓
/etc/services + /etc/protocols
      ↓
netdb structs and lookup APIs
      ↓
program obtains numeric identifier
      ↓
socket/network stack consumes the number
```

The important survival is not just that two text files remain familiar.

What survived is the idea that an operating system maintains a **local, queryable mapping layer between human protocol/service names and globally coordinated wire numbers**.

That layer has changed storage backends repeatedly, but it still sits between people, programs and the same ancient numeric namespaces.

## Next excavation

- recover exact 4.2BSD `/etc/services` and `/etc/protocols` files;
- diff them against 4.3BSD, 4.4BSD-Lite and modern BSD/Linux files;
- reconstruct `getservent.c` / `getprotoent.c` implementation history;
- trace NIS and NSS backend changes;
- connect service names to `inetd` socket creation;
- connect protocol numbers to kernel `IPPROTO_*` constants.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
