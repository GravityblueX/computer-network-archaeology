# delivermail to sendmail: a mail-routing engine grows out of a campus with three incompatible networks

## Why sendmail belongs in network archaeology

SMTP is a wire protocol. Sendmail is software that had to make real mail delivery work across changing protocol families, naming systems, network topologies and local administrative rules.

The distinction matters:

```text
SMTP specification
      ≠
sendmail implementation
```

Sendmail's history is valuable precisely because it records the pressure that standards histories often omit: one Berkeley campus simultaneously had ARPANET, UUCP and BerkNet connectivity, and mail had to cross those boundaries.

---

## 1. The immediate problem: three networks, three mail worlds

Sendmail histories by Eric Allman's collaborators describe a Berkeley environment in which:

- one machine associated with the INGRES project was connected to ARPANET;
- the Berkeley Unix machine used UUCP;
- several campus machines were also connected by Eric Schmidt's BerkNet.

Mail software existed **within** these individual environments, but not as one flexible routing layer across all three.

Sources:

- *Changes in Sendmail Version 8 / Sendmail 8.10 history* — https://www.sendmail.org/~gshapiro/Sendmail-8.10.Paper.pdf
- later Sendmail/O'Reilly histories preserving Allman's account.

This gives an unusually clear implementation origin:

```text
ARPANET mail
UUCP mail
BerkNet mail
     \ | /
      routing/interoperability problem
               ↓
          delivermail
```

---

## 2. delivermail solved a local interoperability problem first

The first public `delivermail` version was distributed with 4BSD-era Unix and later 4.1BSD.

Its goal was not yet to become a universal Internet MTA. It solved a concrete Berkeley routing problem across multiple local/network mail transports.

This is a canonical “scratch your own itch” engineering lineage:

```text
specific deployment pain
      ↓
small local solution
      ↓ adoption exposes wider requirements
      ↓
more general architecture
```

The exact 4BSD release date/source tree must be confirmed from original BSD distributions; secondary histories differ slightly in phrasing/year.

---

## 3. Why delivermail was not enough

Historical accounts emphasize that delivermail was not flexible enough as mail-routing requirements changed.

A major weakness was that configuration/routing knowledge was effectively too compiled-in/static for a world whose network and naming topology was changing rapidly.

The coming changes included:

- ARPANET NCP → TCP/IP;
- growth in reachable hosts/networks;
- DNS-style hierarchical names replacing flat host naming;
- SMTP deployment;
- gateways among network/mail systems;
- increasingly site-specific rewrite/routing policy.

Thus sendmail becomes an answer not merely to SMTP, but to **change itself**.

---

## 4. sendmail externalizes policy into configuration

One of sendmail's defining architectural moves is its programmable/configurable address-rewriting and mailer-selection machinery.

Conceptually:

```text
incoming address/message
      ↓
address parsing / rewriting
      ↓
select mailer/transport
      ↓
construct transport-specific envelope/command
      ↓
queue/deliver/retry
```

This allows one daemon/framework to interact with multiple mail transport mechanisms and naming conventions.

That architecture is historically important because it separates:

- **message format**;
- **address rewriting**;
- **routing policy**;
- **mailer/transport selection**;
- **queue management**.

Do not reduce sendmail to “an SMTP server.”

---

## 5. 4.2BSD is the major public sendmail milestone

Historical Sendmail documentation says the program appeared as `sendmail` in the 4.2BSD generation, after the earlier delivermail releases.

The source-code genealogy should therefore be reconstructed from BSD distributions:

```text
4BSD delivermail
    ↓
4.1BSD delivermail
    ↓ redesign/generalization
4.2BSD sendmail
    ↓
4.3BSD sendmail (historical 5.x generation)
    ↓
independent/later Sendmail 8 development
```

This should be proven by exact source-tree tags, SCCS metadata, release notes and binary/manual artifacts.

---

## 6. SMTP adoption did not make sendmail trivial

Even after SMTP becomes the Internet mail transfer standard, an MTA still must decide:

- which destination host to contact;
- how to rewrite addresses;
- whether to use a local mailer, SMTP, UUCP or other route;
- when to queue/retry;
- how to interpret DNS/MX;
- how to handle aliases and local delivery;
- how to bridge old address forms and new domain names.

Thus:

```text
SMTP standardizes one transfer conversation
         ↓
but sendmail still orchestrates the surrounding routing/policy machinery
```

Wire-protocol standardization does not erase implementation complexity.

---

## 7. DNS and MX changed sendmail's environment

The transition from flat host tables to DNS and MX records changes the data source for routing decisions.

Connect this excavation to:

- [`hosts-txt-to-dns.md`](../lineage/hosts-txt-to-dns.md)
- [`dns-mail-routing-md-mf-mx.md`](../lineage/dns-mail-routing-md-mf-mx.md)

The MTA now combines:

```text
address rewriting rules
       +
DNS resolver behavior
       +
MX selection
       +
SMTP connection/delivery
       +
queue policy
```

This is a perfect example of multiple independent standards lineages meeting inside one implementation.

---

## 8. sendmail.cf is an artifact in its own right

Sendmail's configuration language became famous (and infamous) because routing/address-rewrite policy was exposed through rulesets, macros and mailer definitions.

For archaeology, configuration files can preserve realities absent from protocol RFCs:

- gateway names;
- UUCP neighbor paths;
- local domains;
- pseudo-domains;
- relay policy;
- address rewriting conventions;
- mailer executable paths;
- historical DNS assumptions.

A university's 1980s `sendmail.cf` may be as historically valuable as a network map.

The archive should collect metadata/checksums and lawful copies of real historical configurations.

---

## 9. Queueing makes mail tolerant of partial connectivity

Sendmail inherits a central store-and-forward requirement:

```text
attempt delivery
      |
      +-- success -> remove queue item
      |
      +-- temporary failure -> retain queue state
                            -> retry later
```

This connects Internet SMTP operations to older store-and-forward traditions without proving direct code descent from UUCP or message-switching systems.

The implementation history should recover:

- queue file formats by version;
- retry scheduling;
- error/bounce generation;
- operator queue commands;
- disk-space failure behavior;
- queue-run daemon scheduling.

---

## 10. Aliases and local delivery show where network mail meets the operating system

An MTA eventually hands some messages to local delivery mechanisms.

Sendmail therefore sits at a boundary among:

- remote mail transfer;
- system user/account databases;
- aliases;
- local mailbox formats;
- command/program delivery;
- forwarding files.

This is one reason security history becomes inseparable from sendmail history: powerful delivery/configuration mechanisms expose a large attack surface.

But later vulnerabilities must be recorded as implementation/security branches, not back-projected into the original design motivation.

---

## 11. Sendmail 8 becomes an independent long-lived implementation lineage

Later Sendmail 8 development continues outside the original BSD release cadence and accumulates support for changing Internet standards and operational/security requirements.

The Sendmail 8.10 history paper emphasizes that sendmail had existed in forms since around 1980 and describes the project's continuing evolution.

Future genealogy should split:

- BSD sendmail 4.x/5.x history;
- IDA sendmail branch;
- Sendmail 8 releases;
- commercial Sendmail, Inc. relationship;
- later maintenance/security releases.

Do not use one `sendmail` artifact for all of these.

---

## 12. Sendmail demonstrates implementation layering across standards

A running sendmail instance may simultaneously embody lineages from:

```text
RFC 822 / MIME        message representation
SMTP / ESMTP          mail transfer
DNS / MX              mail routing discovery
TCP/IP                transport/network
aliases/mailboxes     local OS conventions
UUCP                  alternate legacy mail path
configuration rules   local institutional policy
```

No single RFC defines that whole system.

This is exactly why the repo must preserve implementations and configurations alongside protocol documents.

---

## 13. Source archaeology targets

### Original Berkeley sources

Recover and checksum:

- 4BSD `delivermail` source;
- 4.1BSD source;
- earliest 4.2BSD sendmail source;
- 4.3BSD sendmail 5.x source;
- SCCS history if surviving.

### Documentation

- original `delivermail` manual;
- sendmail Installation and Operation Guide revisions;
- configuration grammar docs;
- release notes.

### Real deployments

- Berkeley configs;
- CSNET/ARPANET/UUCP gateway configs;
- `.mc`/m4 transition later;
- queue/log files;
- DNS/MX migration configs.

---

## 14. Lineage rules

Safe:

```text
Berkeley ARPANET + UUCP + BerkNet routing problem
      -> delivermail

delivermail
      -> redesigned/generalized into sendmail implementation family

SMTP/DNS/MX changes
      -> implemented/adapted within sendmail
```

Unsafe:

```text
SMTP -> sendmail formal revision            WRONG CATEGORY
sendmail invented email routing             TOO BROAD
UUCP -> sendmail direct code ancestry       UNPROVEN
4BSD/4.2BSD release years from one secondary source = canonical WITHOUT SOURCE CHECK
```

---

## 15. Sources

Implementation/project histories:

- Gregory Neil Shapiro et al., Sendmail 8.10 history/paper — https://www.sendmail.org/~gshapiro/Sendmail-8.10.Paper.pdf
- Sendmail historical documentation and BSD source trees.
- Unix History Repository / original BSD distributions should be used to verify release-level code genealogy.

Related protocol sources:

- SMTP RFC 821/ESMTP lineage;
- DNS MX RFC 974/1035;
- UUCP documentation;
- Berkeley networking source trees.

---

## 16. Open excavation questions

1. Verify exact first public delivermail release/date from original BSD media, not secondary summaries.
2. Diff delivermail architecture against earliest sendmail.
3. Recover earliest sendmail.cf and explain every rule/mailer in historical context.
4. Trace NCP→TCP/IP and HOSTS.TXT→DNS/MX transitions in actual source/config revisions.
5. Build Sendmail release/source genealogy through 4.2BSD, 4.3BSD, IDA and Sendmail 8.
6. Recover real ARPANET/UUCP/BerkNet gateway logs and configuration.
7. Track security history separately from routing architecture.

Sendmail is an implementation fossil of a world where **mail had to cross not just hosts, but incompatible networks, naming systems, transports and institutional policies.**
