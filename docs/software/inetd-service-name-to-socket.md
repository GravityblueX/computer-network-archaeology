# `inetd`: Turning Service Names into Listening Sockets and Processes

## The missing layer between `/etc/services` and a running daemon

`/etc/services` answers a naming question:

```text
service + transport → port number
```

But a machine still needs something to create a socket, bind the port, wait for traffic, and hand the resulting connection or datagram stream to a program.

One classic Unix answer was the **Internet super-server**, `inetd`.

The role can be reconstructed as:

```text
/etc/inetd.conf
   │ service name
   │ socket type
   │ protocol
   │ wait/nowait
   │ user
   │ server path / arguments
   ↓
inetd
   ├── service name → /etc/services / netdb → port
   ├── protocol name → protocol database / socket family semantics
   ├── socket()
   ├── bind()
   ├── listen()/recv path
   └── fork/exec or internal service
            ↓
          daemon
```

This turns standards metadata into running operating-system state.

---

## 1. Why a super-server existed

Small network services do not necessarily need one permanently resident daemon per port.

A general dispatcher can instead:

1. open the listening sockets;
2. sleep while the kernel waits for traffic;
3. identify which configured endpoint became ready;
4. launch or invoke the corresponding service program.

This reduces the number of always-running service processes and centralizes common startup mechanics.

The design is particularly understandable in the memory-constrained Unix environment in which early Internet services proliferated.

It also produces a historically important separation:

```text
port ownership / listening endpoint
          ≠
service program lifetime
```

A service can be reachable at a well-known port even while its implementation process does not yet exist.

---

## 2. `inetd.conf` is a binding table between namespaces

A classic entry conceptually includes fields such as:

```text
service-name  socket-type  protocol  wait/nowait  user  server  args...
```

The service field is not merely decorative. Modern FreeBSD documentation still explains that the service name must correspond to an entry in `/etc/services`, which determines the port on which `inetd` listens.

Thus a configuration line can indirectly contain multiple layers of naming:

```text
"telnet"
   ↓ service database
23/tcp
   ↓
AF_INET / SOCK_STREAM / TCP socket
   ↓
listen
   ↓
launch telnet daemon
```

For UDP services the shape differs:

```text
"tftp"
   ↓
69/udp
   ↓
SOCK_DGRAM
   ↓
wait policy / datagram handling
   ↓
tftpd
```

---

## 3. `wait` and `nowait`: a tiny field encoding daemon architecture

One of the most historically informative parts of `inetd.conf` is the `wait`/`nowait` distinction.

A modern FreeBSD description still explains the broad rule:

- datagram services generally use `wait`;
- stream services generally use `nowait`;
- `wait` lets a service handle its socket before another instance is launched;
- `nowait` allows separate child handling of arriving stream connections.

This field preserves an old implementation problem:

> Once a shared super-server owns the socket, who consumes the next unit of work?

For connection-oriented TCP services, accepting/spawning one handler per connection is natural.

For connectionless UDP, there is no TCP-style accepted child socket. The application may need to consume multiple datagrams from the same bound endpoint.

So a one-word configuration choice exposes transport semantics.

---

## 4. `inetd` is not the source of the port number

The genealogy must keep three artifacts separate:

```text
IANA / Assigned Numbers
   ↓ global convention
/etc/services
   ↓ local name-number database
inetd.conf
   ↓ local service activation policy
inetd
   ↓ runtime socket/process state
```

Changing `/etc/services` does not change the Internet standard.

Changing `inetd.conf` does not allocate a port.

Running a service on an arbitrary port does not redefine the well-known service assignment.

These layers can agree, disagree, lag, or be locally overridden.

---

## 5. One line can expose several independent registries

Consider a hypothetical service entry:

```text
service-name   stream   tcp   nowait   user   /path/server   server
```

It reaches several historical namespaces:

```text
service-name
    ↓ /etc/services
TCP port registry

"tcp"
    ↓ protocol database / socket API
IP protocol number 6

socket type "stream"
    ↓ Berkeley sockets abstraction
SOCK_STREAM
```

`inetd` is therefore an excellent archaeological junction point: a configuration file written by an administrator connects **global Internet registries, Berkeley socket semantics, Unix process execution and local security policy**.

---

## 6. Internal services

Many `inetd` implementations also supported trivial internal services such as echo, discard, daytime or chargen rather than always execing an external binary.

This is historically useful because some early service names survive today mainly as registry entries, test protocols or security cautionary tales.

The super-server could embody the service itself:

```text
well-known port
    ↓
inetd internal implementation
```

rather than:

```text
well-known port
    ↓
exec external daemon
```

This distinction should be recorded per implementation/release.

---

## 7. The security/operations role grew

A super-server is also a control point.

Over time implementations and surrounding tools accumulated features such as:

- per-service enable/disable policy;
- user identity selection;
- connection limits;
- logging;
- TCP wrappers / host access control;
- IPv4/IPv6 selection;
- per-source rate limits;
- resource limits.

This means the original optimization/dispatch role gradually became an operational policy role.

That is a common genealogy pattern in networking:

```text
simple resource-sharing mechanism
        ↓
central operational chokepoint
        ↓
policy and security controls accumulate
```

---

## 8. Why the design later became less dominant

As machines gained memory and service architectures changed, many daemons became long-running standalone processes managed by service managers rather than spawned through `inetd`.

Other mechanisms include:

- standalone daemon startup;
- `xinetd`-style extended super-servers;
- launchd/systemd socket activation;
- application containers and orchestrators;
- embedded service supervisors.

This does **not** mean the role disappeared.

Socket activation still rests on a recognizable principle:

> a process other than the ultimate service implementation can own/create the listening socket and start the service on demand.

A future lineage record should distinguish direct code/descent from broader role continuity.

Do not write:

```text
inetd → systemd
```

without documentary evidence for a direct design chain.

Safer:

```text
inetd socket/process activation role
        ↕ role comparison
later socket-activation service managers
```

until influence is sourced.

---

## 9. Concrete sources

Modern NetBSD documentation still explicitly organizes its `inetd` guide around:

- `/etc/inetd.conf`;
- `/etc/services`;
- `/etc/protocols`;
- `/etc/rpc`;
- host access files.

FreeBSD documentation states that the configured service name must correspond to `/etc/services` and explains current socket type/protocol/wait semantics.

Useful links:

- https://www.netbsd.org/docs/guide/en/chap-inetd.html
- https://docs.freebsd.org/en/books/handbook/network-servers/
- historical BSD source/manual archives in TUHS.

---

## 10. Root-hunting summary

A modern administrator looking at:

```text
ssh 22/tcp
```

usually sees one service.

The archaeological view sees several independent layers:

```text
IANA service assignment
       ↓
Unix services database
       ↓
name-service lookup API
       ↓
service activation configuration
       ↓
Berkeley socket object
       ↓
process execution and privilege policy
```

`inetd` is where those layers become runtime behavior.

## Next excavation

- recover earliest surviving `inetd` source and manual;
- identify first BSD release containing `/etc/inetd.conf`;
- diff configuration grammar across 4.2BSD/4.3BSD/4.4BSD descendants;
- recover internal service implementations;
- trace TCP wrappers integration;
- compare inetd activation semantics with launchd/systemd socket activation without asserting ancestry until sourced.

Research and initial drafting: **GPT-5.6 Sol (OpenAI), August 2026**.
