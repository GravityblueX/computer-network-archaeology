# `netstat` to `sock_diag` and `ss`: one command role splits into several modern tools

Classic `netstat` accumulated many jobs: show sockets, routes, interfaces, multicast groups and statistics. Modern Linux documentation now describes it as mostly obsolete and points different jobs to different iproute2 tools.

The important pattern is **role fission**, not a single replacement binary:

```text
netstat socket view   → ss
netstat route view    → ip route
netstat interface view→ ip -s link
netstat multicast view→ ip maddr
```

For sockets the deeper transition is `/proc/net/*` parsing toward `sock_diag`/`inet_diag`. `ss` can ask the kernel for structured socket diagnostic records and expose information that is difficult to represent cleanly in the old all-purpose command.

This history therefore has three layers:

```text
operator role: inspect connections
        ↓ survives
netstat-style presentation
        ↓ role migrates
ss

kernel data path:
/proc/net/*  ↔  sock_diag/inet_diag
```

Neither arrow means TCP itself changed.

The correct archaeological object is the **visibility path from kernel socket state to operator**, not merely the command name.
