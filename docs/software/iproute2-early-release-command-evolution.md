# Early iproute/iproute2: from one-command-per-tool networking to object-oriented `ip`

## Scope

This excavation asks when the modern Linux `ip` command family appears, what problem it was solving, and which parts of its command language were already present in the first surviving distributions.

It does **not** assume that the modern package name `iproute2` existed unchanged from the first prototype.

## 1. The user-space problem before `ip`

Traditional Linux/Unix administration spread networking state across commands such as:

```text
ifconfig
route
arp
netstat
```

and a growing set of specialized programs.

This matched the older ioctl/procfs style reasonably well, but Linux 2.1/2.2 introduced richer kernel objects:

```text
links
addresses
routes
policy rules
neighbours
traffic-control objects
```

rtnetlink exposed these as typed message families. A userspace tool organized around the same object vocabulary was a natural companion.

## 2. Authorship and stable-release boundary

The current `ip(8)` history records that `ip` was written by Alexey N. Kuznetsov and added in Linux 2.2.

The iproute2 credits likewise identify Kuznetsov as the original author and Stephen Hemminger as taking over maintenance beginning in the Linux 2.6 era.

Debian packaging records copyright for Kuznetsov beginning in **1996**, which is a useful lower-bound clue for the tool suite's development period, but copyright metadata alone is not proof of the first public tarball.

## 3. Surviving archive evidence

A surviving mirror of the old INR `ip-routing` archive contains date-stamped source packages such as:

```text
iproute2-2.2.4-now-ss990417.tar.gz
iproute2-2.2.4-now-ss990530.tar.gz
iproute2-2.2.4-now-ss990630.tar.gz
iproute2-2.2.4-now-ss990824.tar.gz
iproute2-2.2.4-now-ss991023.tar.gz
...
iproute2-2.4.7-now-ss010824.tar.gz
```

These prove that by 1999 the package already used the recognizable `iproute2-<kernel>-now-ssYYMMDD` snapshot naming convention.

They do **not**, by themselves, prove that `ss990417` was the first release. The older development history must be reconstructed from additional mirrors, mailing-list references or period distributions.

So the repository records:

```text
first surviving archive currently confirmed: 1999 snapshot family
first development/authorship lower bound: 1996 copyright/history evidence
exact first public release: still open unless a primary archive is found
```

This is preferable to inventing a first version number.

## 4. The command language is object-oriented early

Period iproute2 documentation from the Linux 2.2 era presents `ip` as one command with sub-objects rather than as a collection of unrelated utilities.

The conceptual grammar is already familiar:

```text
ip [ OPTIONS ] OBJECT COMMAND
```

with object families such as:

```text
link
address
neighbour
route
rule
maddress
mroute
tunnel
```

This mirrors rtnetlink's object vocabulary.

The important innovation is not abbreviations or pretty output. It is that user-space language now follows the kernel's network object model.

## 5. A concrete Linux 2.0 → 2.2 command split

Alexey Kuznetsov's 1999 tunnel documentation preserves a useful migration example.

A Linux 2.0.36-era style such as:

```text
ifconfig tunl1 10.0.0.1 pointopoint 193.233.7.65
```

no longer represents the complete operation cleanly under Linux 2.2. The documentation explains that tunnel creation and address configuration are split:

```text
ip tunnel add MY-TUNNEL mode ipip remote 193.233.7.65
ifconfig MY-TUNNEL 10.0.0.1
```

That transitional example is historically valuable because even the new `ip` tool did not immediately replace every old command in every workflow.

The migration could be hybrid:

```text
new rtnetlink/iproute object creation
        +
old ifconfig address assignment
```

Later operational practice converges further toward `ip link` and `ip addr`.

## 6. Policy routing makes the old command model visibly insufficient

Linux 2.2's richer routing system includes multiple tables and policy rules. These are first-class objects in the same rtnetlink vocabulary that appeared in Linux 2.1.68:

```text
RTM_NEWRULE / DELRULE / GETRULE
RT_TABLE_MAIN / DEFAULT / LOCAL
```

The `ip rule` / `ip route table ...` syntax gives users direct access to a routing architecture that classic `route` was not designed to describe elegantly.

This is one reason the newer suite survives: it exposes kernel architecture rather than emulating the old command vocabulary.

## 7. From `iproute` to `iproute2` as a historical naming problem

Historical sources sometimes call the package or documentation “iproute”, while later distributions consistently use “iproute2”. Debian even retained a binary/source package name `iproute` for a period while shipping the `ip` utility.

Therefore the project should not infer a clean product rename date merely from current package naming.

Track separately:

```text
utility name: ip
suite/project naming: iproute / iproute2
kernel generation named in snapshot filenames: 2.2.4, 2.4.7, ...
distribution package names: distro-specific
```

## 8. Command survivorship

The remarkable part is how much of the object grammar remains recognizable:

```text
ip link
ip address
ip neighbour
ip route
ip rule
```

Later generations add many object types and attributes, but the core interaction model survives.

This is another `living-core-with-extension-forest` case, this time at the operations/API layer rather than a wire protocol.

## 9. What remains unresolved

The following should remain marked as open until stronger primary evidence is acquired:

- exact first public `iproute`/`iproute2` tarball;
- precise date when the source tree first adopted the name `iproute2`;
- command-by-command diff between the earliest recoverable 1996/1997 code and 1999 snapshots;
- first distro release that installed `ip` by default;
- exact transition of individual tasks from `ifconfig`/`route`/`arp` to `ip` in distro documentation.

The presence of open questions does not block the documented lineage:

```text
Linux 2.1 rtnetlink object model
        ↓
Kuznetsov ip/iproute user-space vocabulary
        ↓
Linux 2.2 stable generation
        ↓
iproute2 snapshot series
        ↓
modern iproute2
```

## Evidence anchors

- `ip(8)` history: https://manpages.debian.org/experimental/iproute2/ip.8.en.html
- iproute2 credits: https://sources.debian.org/src/iproute2/6.15.0-1~bpo12%2B1/CREDITS
- Debian packaging provenance/copyright: https://sources.debian.org/copyright/license/iproute2/3.16.0-2/
- Archived INR mirror snapshot list: https://ftp.funet.fi/pub/mirrors/Archived/ftp.inr.ac.ru/ip-routing/
- Period iproute2 documentation: https://www.policyrouting.org/iproute2.doc.html
- Linux 2.2 tunnel migration examples: https://android.googlesource.com/platform/external/iproute2/%2B/8776459%5E%21/

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
