# Beyond `services` and `protocols`: `/etc/networks`, `/etc/ethers`, and `/etc/rpc`

## `/etc` as a convergence layer for several numbering traditions

Once `/etc/services` and `/etc/protocols` are treated as archaeological artifacts, a larger pattern appears.

Classic Unix-like systems accumulated multiple small databases whose job was to convert between **human-readable names and globally or administratively meaningful numbers**:

```text
/etc/hosts       host name ↔ address
/etc/networks    network name ↔ network number
/etc/services    service name ↔ port / transport
/etc/protocols   protocol name ↔ IP protocol number
/etc/ethers      Ethernet address ↔ host name
/etc/rpc         RPC program name ↔ RPC program number
```

These files look similar, but they do **not** all share one origin.

That is precisely why they are useful for root-hunting: Unix `/etc` became a place where different networking institutions and architectures converged behind similar local file interfaces.

---

## 1. `/etc/networks`: a 4.2BSD projection of the NIC network database

Historical `networks(5)` documentation says the file contains information about known networks comprising the DARPA Internet.

The classical fields are:

```text
official network name
network number
aliases
```

The file format is explicitly documented as appearing in **4.2BSD**.

Even more interesting is the provenance statement in the historical manual: the file was normally created from the **official network database maintained at the Network Information Control Center (NIC)**, but local changes could be required for unofficial aliases or unknown networks.

That sentence is a nearly perfect description of the local-projection problem:

```text
central NIC database
        ↓ distribution / copy
/etc/networks
        ↓ local aliases and additions
getnetent-style lookup
```

The local file is neither purely authoritative nor purely arbitrary.

It is synchronized institutional knowledge with room for site-local reality.

### 1.1 The old classful-network worldview is embedded in the artifact

`/etc/networks` makes most intuitive sense in a world where named IP **network numbers** are stable objects worth looking up as units.

Later CIDR, provider-based allocation, frequent renumbering and prefix-based routing make that worldview less central.

Modern descendants of the manual even discuss provider changes, address renumbering, CIDR and DNS encoding of network names.

So the file survived into a network architecture where its original object — the named classful network — became less foundational.

That is a classic root-hunting pattern:

```text
file/API survives
while the architectural importance of the thing it names declines
```

---

## 2. `/etc/ethers`: same local-file shape, different ancestry

`/etc/ethers` maps an Ethernet MAC address to a host name or other local identifier.

Conceptually:

```text
08:00:20:00:5a:bc   host.example
```

The important historical warning is that this is **not simply another 4.2BSD database invented beside `/etc/services`**.

BSD descendant manual pages explicitly say the format was adopted from **SunOS 4.1.x**; NetBSD/OpenBSD histories describe adoption from SunOS into their own trees.

That gives a different genealogy:

```text
Sun networking / diskless-host administration
        ↓
/etc/ethers format
        ↓ adopted by BSD descendants
        ↓
ethers(3) / ether_aton / ether_line helpers
        ↓
local MAC↔host administration
```

The similar appearance of the file masks a different institutional and product lineage.

### 2.1 Why this file existed

A site operating Ethernet and diskless or centrally managed hosts often needed a durable mapping between:

```text
48-bit link-layer identity
          ↔
human host identity
```

That can be useful for:

- booting/diskless configuration;
- network management;
- static host identification;
- NIS/YP maps;
- administrative scripts.

The file therefore sits one layer below the IP-centric databases.

### 2.2 OUI lookup is not `/etc/ethers`

Do not confuse:

```text
IEEE OUI / MA-L registry
```

with:

```text
/etc/ethers
```

The IEEE registry maps blocks of universal identifier space to assignees.

`/etc/ethers` maps **individual observed/configured addresses** to site-relevant host names.

Thus:

```text
IEEE RA:
prefix → block assignee

/etc/ethers:
full MAC → host identity
```

They can interact, but they solve different naming problems.

---

## 3. `/etc/rpc`: another number registry enters Unix

Sun RPC introduced a separate namespace of **RPC program numbers**.

The classic `/etc/rpc` database maps:

```text
program-name   RPC-program-number   aliases...
```

Examples preserved by historical manuals include:

```text
portmapper   100000
rstatd       100001
rusersd      100002
nfs          100003
mountd       100005
```

The table immediately exposes another historical world:

```text
NFS
NIS/YP
portmapper/rpcbind
remote status/user tools
lock managers
bootparam
keyserv
```

These are not TCP/UDP port-number assignments. The RPC program number identifies an RPC program, while portmapper/rpcbind machinery maps a program/version/protocol combination to an actual transport endpoint.

So there are two levels of number indirection:

```text
RPC program number
       ↓ portmapper/rpcbind
transport protocol + port
       ↓
IP endpoint
```

This is why `/etc/rpc` cannot be collapsed into `/etc/services`.

---

## 4. The same text-file idiom hides different governance structures

The databases can look deceptively uniform:

```text
name number aliases
```

But the authority behind each number differs.

| Local database | Number/identity represented | Historical authority/ecology |
|---|---|---|
| `/etc/networks` | IP network number/name | ARPANET/Internet NIC, later Internet address institutions |
| `/etc/services` | port + transport | Assigned Numbers / IANA service registry |
| `/etc/protocols` | IP protocol number | Assigned Numbers / IANA Protocol Numbers |
| `/etc/ethers` | 48-bit Ethernet host address | site administration; IEEE governs universal address-block assignment, not local hostname binding |
| `/etc/rpc` | RPC program number | Sun RPC / RPC program-number assignment ecology |

The **Unix file format is the common implementation pattern**, not proof of common standards ancestry.

---

## 5. NIS/YP turns local files into distributed maps

Several of these databases acquired YP/NIS integration.

Historical `ethers(5)` documentation, for example, describes `ethers.byname` and `ethers.byaddr` maps.

Older `services(5)` implementations likewise allowed NIS service maps.

This adds a new layer:

```text
flat local file
     ↓ transformed/published as map
NIS/YP distributed database
     ↓
network-wide lookup
```

The lookup semantics can stay similar while data moves off the local disk.

That leads directly to the later Name Service Switch story.

---

## 6. The repeated BUGS line is historically important

Multiple classic database manual pages contain some variation of:

> a name server should be used instead of a static file.

This is not merely a documentation joke.

It exposes a structural problem recognized early:

- central truth changes;
- copied files go stale;
- every host requires distribution;
- local overrides complicate synchronization;
- networked organizations want shared administration.

The same pressure appears repeatedly in networking history:

```text
HOSTS.TXT → DNS
local service files → NIS/NSS/database backends
local user/group files → directory services
```

These are not necessarily direct protocol-descendant relationships, but they share a recurring **central-file replication problem**.

---

## 7. `/etc/networks` as an especially good time capsule

The historical manual's wording that the file records networks which “comprise the DARPA Internet” should be preserved verbatim in metadata even if a modern descendant rewrites the description.

The file's changing documentation can reveal the architecture moving underneath it:

```text
named classful networks
       ↓
subnetting
       ↓
CIDR prefixes
       ↓
provider-based address allocation
       ↓
network name database becomes less central to everyday operation
```

A future version-by-version diff of `networks(5)` may therefore tell a broader story about the decline of the “network number as named object” worldview.

---

## 8. Archive targets

High-value targets include:

- actual 4.2BSD `/etc/networks` contents;
- 4.3BSD and 4.4BSD-Lite network databases;
- SunOS 4.1.x `/etc/ethers` source/manual and YP maps;
- original Sun RPC `/etc/rpc` source distribution;
- NIS maps generated from each local database;
- libc `getnetent`, `getrpcent`, `ether_*` implementations.

Useful current/historical manual anchors:

- `networks(5)` historical BSD manual:
  - https://man.freebsd.org/cgi/man.cgi?query=networks&sektion=5&manpath=4.3BSD+NET%2f2
- modern/historical `ethers(5)`:
  - https://man.freebsd.org/cgi/man.cgi?query=ethers&sektion=5&manpath=FreeBSD+15.1-STABLE
- `rpc(5)`:
  - https://man.freebsd.org/cgi/man.cgi?query=rpc&sektion=5

---

## 9. Root-hunting summary

The Unix `/etc` network databases are not one family tree.

They are a **convergence zone**:

```text
ARPANET/Internet NIC network database ──→ /etc/networks
Assigned Numbers service registry     ──→ /etc/services
Assigned Numbers protocol registry    ──→ /etc/protocols
Sun Ethernet administration           ──→ /etc/ethers
Sun RPC program-number ecology        ──→ /etc/rpc
                                              ↓
                                     Unix lookup APIs
                                              ↓
                                       NIS/NSS backends
```

The shared lesson is that global or organizational numbering systems become operationally useful only after operating systems build local interfaces around them.

## Next excavation

- SunOS origin of `/etc/ethers`;
- original Sun RPC program-number registry and portmapper;
- `/etc/networks` contents across classful→CIDR transition;
- NIS map-generation sources;
- NSS backend genealogy and the point where the lookup API stopped implying a local file.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
