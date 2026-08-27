# Network Reconstruction Template

> The target is not a paragraph saying a network “used packet switching”. Reconstruct the actual system that existed at a specific date.

## Identity

- **Network name:**
- **Contemporary expansions / aliases:**
- **Operator(s):**
- **Sponsor/funder:**
- **Geographic scope:**
- **Design period:**
- **First prototype:**
- **First operational service:**
- **Major upgrade dates:**
- **Retirement / transition:**
- **Primary purpose:**

## Historical problem

What need produced the network? Resource sharing, terminals, reservations, military command, research, commercial data service, mail/news, LAN, backbone, etc.

## Snapshot date

A network changes constantly. Every reconstruction should state a date or interval.

**This record describes the network as of:**

## Topology

- number of switching nodes:
- number of host/end sites:
- number of user terminals:
- backbone topology:
- access topology:
- international links:
- gateways to other networks:

Preserve dated maps separately.

```text
site A ---- node ---- node ---- site B
             |         |
             ...
```

## Sites / nodes

| Site | Date joined | Switching hardware | Host/end systems | Link(s) | Evidence |
|---|---|---|---|---|---|
| | | | | | |

## Physical transmission layer

For every important link class:

| Link/service | Provider | Medium | Speed | Modem/termination | Notes |
|---|---|---|---:|---|---|
| | | | | | |

Include:
- leased circuits;
- dial-up;
- coax;
- radio;
- satellite;
- microwave;
- fiber;
- carrier services;
- tariff/service names.

## Switching / forwarding hardware

- node model(s):
- CPU/memory:
- port types:
- software:
- packet buffering:
- routing logic:
- redundancy:
- management interface:

## Host / endpoint interface

Describe how a real computer or terminal connected physically and logically.

- interface standard:
- adapter/controller hardware:
- framing:
- line speed:
- driver/host software:
- bootstrap/configuration:

## Protocol stack

Do not use modern layer names if they distort contemporary architecture, but a mapping table can help.

| Function | Contemporary protocol/system | Document/version |
|---|---|---|
| physical/link | | |
| host-node | | |
| network | | |
| transport/host-host | | |
| naming/addressing | | |
| applications | | |
| management | | |

## Addressing

- node addresses:
- host addresses:
- user/account identifiers:
- network numbers:
- assignment authority:
- changes over time:

## Routing / switching behavior

- routing algorithm:
- update frequency:
- virtual circuit/datagram/message switching:
- failure recovery:
- congestion behavior:
- flow control:

## Naming / directory service

- host lists:
- centralized directory:
- distributed naming:
- user directory:
- update/distribution workflow:

## User-visible services

- remote login;
- file transfer;
- mail;
- news;
- databases;
- reservations/transactions;
- printing;
- chat;
- other.

## Operations

- Network Operations Center / administrator structure:
- monitoring tools:
- alarms:
- statistics:
- scheduled maintenance:
- configuration distribution:
- incident handling:
- time synchronization:

## Economics

- funding model:
- line/circuit costs:
- access charges:
- equipment costs:
- tariffs:
- commercial pricing:

## Governance

- who could connect?
- acceptable-use restrictions:
- address/allocation authority:
- standards process:
- vendor/carrier control:

## Growth table

| Date | Nodes/networks/users | Traffic | Backbone capacity | Source |
|---|---:|---:|---:|---|
| | | | | |

## Major incidents / failures

Preserve outages, congestion episodes, routing failures and operational lessons.

## Interconnection with other networks

For every gateway/interconnect:
- date;
- networks connected;
- gateway hardware/software;
- protocol conversion or common protocol;
- routing/addressing consequences.

## What changed in the next generation

Explain upgrades as a response to measured limits rather than a list of new speeds.

## Surviving artifacts

- maps;
- node hardware;
- host adapters;
- software/source;
- packet traces;
- manuals;
- photographs;
- operator logs;
- oral histories.

## Primary sources

## Secondary sources

## Source conflicts / unresolved questions

## Research status

`seed | started | substantially documented | needs primary verification | blocked`

## Last reviewed

- date:
- reviewer/agent:
