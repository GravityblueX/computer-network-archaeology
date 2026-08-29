# `/proc/net/tcp` to `tcp_diag` / `inet_diag` / `sock_diag`

## Text table first, structured diagnostic channel later

Linux has exposed active TCP sockets through text-like procfs tables such as:

```text
/proc/net/tcp
/proc/net/tcp6
```

The current kernel documentation still explains their field layout, including local/remote addresses and ports, connection state, queues, timers and selected TCP internal values. It also states something historically important: these interfaces are **deprecated in favor of tcp_diag**.

That single sentence gives us a direct implementation-lineage boundary.

## Why `/proc/net/tcp` is an archaeological gold mine

The table is an awkward compromise between kernel internals and human-readable text. One row serializes a socket into hexadecimal/numeric columns. User-space programs can parse it, but the representation has disadvantages:

- fields are positional and implementation-specific;
- extensibility is awkward;
- applications must parse text;
- filtering often happens after reading the table;
- exposing more socket families requires more pseudo-files.

Yet this very awkwardness makes it historically useful: old scripts and tools preserve assumptions about exactly how Linux once projected TCP state.

## Diag changes the shape of observability

The diagnostic netlink family (`tcp_diag`, later `inet_diag` and broader `sock_diag`) asks the kernel for structured socket records. A request can select families/states and a reply can carry typed extensions.

Conceptually:

```text
kernel TCP socket
      ↓
/proc text serialization
      ↓
user parser
```

becomes:

```text
kernel socket
      ↓
diag request/response
      ↓
structured netlink attributes
      ↓
user tool
```

The socket has not changed merely because the observation API changed. This is an **observability-interface lineage**, not a TCP wire-protocol revision.

## Coexistence matters

New diagnostic APIs did not instantly remove procfs. Current systems can still expose `/proc/net/tcp`, and current tooling may retain fallback or supplementary procfs code.

Therefore the appropriate relationship is:

```text
/proc socket tables
       ↕ long coexistence
sock_diag / inet_diag
```

with the newer API becoming the preferred structured path.

## Root-hunting consequence

When a historical tool shows a TCP state, ask two different questions:

1. Which TCP state/metric is this?
2. Through which kernel/user-space observation interface did the tool learn it?

Mixing those layers creates false protocol history.

Primary anchor:

- Linux kernel `proc_net_tcp` documentation: https://docs.kernel.org/networking/proc_net_tcp.html
