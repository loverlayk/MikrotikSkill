# RoMON

> RoMON (Router Management Overlay Network) builds an independent MAC-layer overlay between routers for management: peer discovery, MAC ping, RoMON SSH, message authentication with secrets, and per-port participation...

# RoMON

RoMON (Router Management Overlay Network) builds an independent MAC-layer peer discovery and data forwarding network between routers. RoMON packets use EtherType 0x88bf and destination multicast MAC 01:80:c2:00:88:bf and are handled independently of L2 or L3 configuration: a router stays reachable through RoMON even when its IP configuration, routing or firewall is broken. That makes RoMON a recovery path into misconfigured routers, one overlay hop at a time.

Each router on the RoMON network has a RoMON ID, either selected automatically from a port MAC address or configured with `id`.

The RoMON protocol does not encrypt messages. Encryption comes from the application running on top of it, for example SSH or a secure WinBox connection.

:::info
RoMON packets can be forwarded through network switches or bridges, unless there are specific restrictions on multicast traffic. When using a MikroTik bridge with hardware offloading, these packets are treated like regular multicast packets and are flooded across the network.

If the RoMON service is enabled and the switch chip supports ACL rules, dynamic rules are automatically created to redirect these packets to the CPU, where the RoMON service operates. However, if the switch does not support ACL rules and the configuration does not align, such as when the CPU and RoMON untagged packets are not in the same VLAN, the RoMON service might not function as expected.

**RB5009** (switch-chip 88E6393X) does not support this path. The chip's frame-types=admit-only-vlan-tagged filter drops RoMON frames before any ACL rule can be applied, so the packets never reach the CPU.
:::

## Enable RoMON

Enable the service in the [`/tool/romon`](../cli-reference/tool/romon) menu:

```ros
/tool/romon/set enabled=yes
```

When the ID is not configured, it is selected automatically:

```ros
[admin@MikroTik] > /tool/romon/print
     enabled: yes
          id: 00:00:00:00:00:00
  current-id: DC:2C:6E:E7:10:6B
```

## Choose ports

Ports that participate in the RoMON network are configured in the [`/tool/romon/port`](../cli-reference/tool/romon/port) menu. Each entry matches one physical interface name (or the built-in wildcard `all`) and either forbids RoMON on it or allows it with a port cost. Bridge or other master interfaces are not accepted as RoMON ports — name the physical ports that talk to the network. More specific entries override the wildcard entry.

A default entry with the interface list `all` is preconfigured, so every interface participates with cost 100 until you change it:

```ros
[admin@MikroTik] > /tool/romon/port/print
Flags: * - DEFAULT
Columns: INTERFACE, FORBID, COST
#   INTERFACE  FORBID  COST
0 * all        no       100
```

RoMON should not listen on the untrusted side of a router (it accepts management connections by MAC address). Forbid the WAN port and keep the LAN:

```ros
/tool/romon/port/add interface=ether1 forbid=yes
```

Or the other way around: forbid everything with the wildcard entry, then allow the trusted interfaces one by one:

```ros
/tool/romon/port/set [find default=yes] forbid=yes
/tool/romon/port/add interface=ether2 forbid=no
/tool/romon/port/add interface=ether3 forbid=no
```

## Protect the overlay with secrets

RoMON secrets authenticate messages, check their integrity and prevent replays by hashing the message contents with MD5. Every router in the same RoMON network should use the same secrets. On a fresh setup, set the secret on all routers:

```ros
/tool/romon/set secrets="mysecret"
```

The global list lives in `/tool/romon`; an interface-specific list can be set per port in `/tool/romon/port` (if the port list is empty, the global list is used).

When sending, messages are hashed with the first secret in the list, unless the list is empty or starts with the empty secret (in that case messages are sent unhashed). When receiving, unhashed messages are accepted only by an empty list or a list that contains the empty secret; hashed messages are accepted when they carry any secret in the list.

That behaviour makes a rolling change possible without splitting the network — and the rotation works even when you do it while connected through RoMON itself:

```ros
# 1. every router still sends unhashed, but also accepts "mysecret"
/tool/romon/set secrets=("","mysecret")
# 2. every router sends hashed with "mysecret", but still accepts unhashed
/tool/romon/set secrets=("mysecret","")
# 3. every router sends and only accepts "mysecret"
/tool/romon/set secrets="mysecret"
```

To change a secret later, run the same rotation with both the old and the new secret in the list for a while.

:::note
In the CLI, list entries that contain an empty secret need parentheses: `secrets=("","mysecret")`. In WinBox, press the small **+** in the **Secrets** field and leave the first row empty.
:::

A client whose secret does not match gets no answer:

```ros
[admin@MikroTik] > /tool/romon/ping id=DC:2C:6E:E7:10:6B count=3
  SEQ HOST                                    TIME  SIZE STATUS
    0 DC:2C:6E:E7:10:6B                           32 timeout
    1 DC:2C:6E:E7:10:6B                           32 timeout
    2 DC:2C:6E:E7:10:6B                           32 timeout
    sent=3 received=0 packet-loss=100%
```

## Find routers in the overlay

Run [`/tool/romon/discover`](../cli-reference/tool/romon/discover) to list the reachable routers:

```ros
[admin@MikroTik] > /tool/romon/discover
Flags: A - ACTIVE
Columns: ADDRESS, COST, HOPS, PATH, L2MTU, IDENTITY, VERSION
  ADDRESS            COST  HOPS  PATH               L2MTU  IDENTITY  VERSION
A F4:1E:57:46:89:89   200     1  F4:1E:57:46:89:89   1500  Router-B  7.26beta1
```

The discovery table keeps refreshing; with `duration` it stops after the given time. The `address` column holds the RoMON ID of the found router, which is what the other RoMON tools take.

## Test connectivity with RoMON ping

```ros
[admin@MikroTik] > /tool/romon/ping id=F4:1E:57:46:89:89 count=5
  SEQ HOST                                    TIME   SIZE STATUS
    0 F4:1E:57:46:89:89                       1ms      32
    1 F4:1E:57:46:89:89                       0ms      32
    ...
    sent=5 received=5 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=1ms
```

## Open an SSH session over RoMON

[`/tool/romon/ssh`](../cli-reference/tool/romon/ssh) opens an SSH session through the overlay, even when the remote router has no IP address:

```ros
[admin@MikroTik] > /tool/romon/ssh F4:1E:57:46:89:89 user=admin
```

## Connect with WinBox

In WinBox, select **Connect To > RoMON Agent** on the login screen and choose a saved router with RoMON enabled as the agent, then connect to the target by its RoMON ID (see [WinBox](winbox)). Watch the [video tutorial](https://www.youtube.com/watch?v=Peg6UcSJ_eA).

You can also run WinBox from the command line with a RoMON agent and the target router's ID. The agent router must be saved in the WinBox managed router list for the connection to succeed:

```bash
winbox.exe --romon 192.168.88.24 F4:1E:57:46:89:89 admin ""
```

## Technical details

- Discovery, ping and RoMON SSH all run over raw Ethernet frames, so they keep working without any IP configuration.
- RoMON frames are not special for the [packet sniffer](../diagnostics-monitoring-and-troubleshooting/packet-sniffer): capture them with `filter-mac-protocol=romon` (EtherType 0x88BF).
- `hops`, `path` and `cost` in the discovery table describe the RoMON path: routers that run RoMON forward the overlay traffic, so a target several segments away shows the intermediate IDs in `path`.
- A `[find default=yes]` wildcard port entry always exists: it cannot be removed, disabled or enabled — only its `cost`, `forbid` and `secrets` can be changed ("failure: only cost, forbid and secrets can be changed for preset"). Setting it to `forbid=yes` turns the default into "deny all".

For all parameters, see the [`/tool/romon`](../cli-reference/tool/romon), [`/tool/romon/port`](../cli-reference/tool/romon/port), [`/tool/romon/discover`](../cli-reference/tool/romon/discover), [`/tool/romon/ping`](../cli-reference/tool/romon/ping) and [`/tool/romon/ssh`](../cli-reference/tool/romon/ssh) CLI reference pages.
