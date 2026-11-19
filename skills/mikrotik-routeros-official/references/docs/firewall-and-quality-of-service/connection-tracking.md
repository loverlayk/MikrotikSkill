# Connection tracking

> Connection tracking records the connections that pass through or end at the router. It is the basis of the stateful firewall and NAT: view the connection list, use connection states in firewall rules, adjust the...

# Connection tracking

Connection tracking records the logical connections that pass through the router or end at it, and relates each packet to its connection. The stateful firewall and NAT are built on it:

- Firewall rules can match the state of the connection that a packet belongs to, also for protocols that have no connections of their own, such as UDP and ICMP.
- NAT translates all packets of a connection in the same way.

With the default settings, connection tracking starts when the router has a filter, mangle or NAT rule, so a router with the default configuration tracks connections. You do not have to enable it.

## View the connections

The tracked IPv4 connections are in the `/ip/firewall/connection` menu:

```ros
/ip/firewall/connection/print where src-address=192.168.88.10
```

```text
Flags: S - SEEN-REPLY; A - ASSURED; C - CONFIRMED; s - SRCNAT
Columns: PROTOCOL, SRC-ADDRESS, SRC-PORT, DST-ADDRESS, DST-PORT, TCP-STATE, 
         TIMEOUT, ORIG-RATE
#      PROT  SRC-ADDRESS    SRC-P  DST-ADDRESS      DST-  TCP-STATE  TIM  ORIG
0   C  udp   192.168.88.10   5678  255.255.255.255  5678             27s  0bps
1 S Cs icmp  192.168.88.10         10.2.0.2                          9s   0bps
2 S Cs udp   192.168.88.10  51769  10.2.0.2           53             28s  0bps
3 SACs tcp   192.168.88.10  53812  10.2.0.2           80  time-wait  7s   0bps
```

Each entry is one connection. The command lists the connections that the host 192.168.88.10 has opened. A connection that another host opens to it, for example through a port forward, has the address of the host in `reply-src-address`.

- The `S` flag shows that the destination has replied.
- The `A` (assured) flag is set on a TCP connection after the handshake, and on a UDP connection that has become a stream.
- The `C` (confirmed) flag shows that the first packet of the connection has left the router.
- The `s` and `d` flags show that the router applies source or destination NAT to the connection.
- The `E` (expected) flag marks a connection that a connection helper created for a related connection, and the `h` (uses-helper) flag marks a connection that a helper handles. The `D` (dying) flag marks an entry that is being removed. The `F` (fasttrack) flag is described under [FastTrack](#fasttrack).
- `TCP-STATE` is the state of a TCP connection, for example `established`, or `time-wait` for a connection that is closed.
- `TIMEOUT` is the time after which the router removes the entry if it sees no more packets of the connection.

The console shortens the column names to fit the width of the terminal. The first entry in this output is a broadcast packet that the host has sent.

To see all properties of a connection, use `print detail`. It shows the packet and byte counters of both directions, and the addresses of the reply packets. In this output, `reply-dst-address` is the address of the router, because the router applies source NAT to the connection:

```ros
/ip/firewall/connection/print detail where dst-port=53
```

```text
Flags: S - SEEN-REPLY; C - CONFIRMED; s - SRCNAT
2 SCs protocol=udp src-address=192.168.88.10 src-port=51769
      dst-address=10.2.0.2 dst-port=53 reply-src-address=10.2.0.2
      reply-src-port=53 reply-dst-address=10.2.0.1 reply-dst-port=51769
      timeout=28s orig-packets=1 orig-bytes=54 orig-fasttrack-packets=0
      orig-fasttrack-bytes=0 repl-packets=1 repl-bytes=70
      repl-fasttrack-packets=0 repl-fasttrack-bytes=0 orig-rate=0bps
      repl-rate=0bps
```

To count the connections, use `/ip/firewall/connection/print count-only`.

The IPv6 connections are in the `/ipv6/firewall/connection` menu, with the same properties:

```ros
/ipv6/firewall/connection/print
```

All flags and properties are described in the CLI reference of [`/ip/firewall/connection`](../cli-reference/ip/firewall/connection) and [`/ipv6/firewall/connection`](../cli-reference/ipv6/firewall/connection).

## Remove connections

To remove connections from the list, use `remove` with `find`. This command removes the connections that the host 192.168.88.10 has opened:

```ros
/ip/firewall/connection/remove [find src-address=192.168.88.10]
```

`/ip/firewall/connection/remove [find]` removes all connections.

Removing a connection does not stop its traffic. When the next packet of the connection arrives, the router adds a new entry for it at once, with packet and byte counters that start again from zero. To stop a connection, first add a firewall rule that drops its packets, then remove the connection.

## Connection states

When a packet arrives, connection tracking looks for its connection in the connection list and gives the packet one of these states. Firewall rules match the state with the `connection-state` property.

- **new** - the packet starts a connection, or belongs to a connection that has seen packets in one direction only. For TCP, the packet that starts a connection is a packet with the SYN flag. For protocols without connections, such as UDP, a packet is new when the connection list has no entry for it.
- **established** - the packet belongs to a connection in the connection list that has seen packets in both directions.
- **related** - the packet does not belong to a connection in the list, but is related to one. Examples are ICMP error packets, such as "port unreachable", and the data connection of an FTP session.
- **invalid** - the packet does not belong to a connection and cannot start one, for example a TCP reply to a connection that the router has not seen. Drop such packets, unless the router has asymmetric routing.
- **untracked** - the packet was excluded from connection tracking with a [RAW](./firewall/raw) rule that has `action=notrack`.

With these states, the firewall accepts the packets of connections that are already allowed, drops invalid packets, and applies the detailed rules only to the packets that start a connection. This also reduces the load on the CPU:

```ros
/ip/firewall/filter
add chain=input action=accept \
    connection-state=established,related,untracked \
    comment="accept established,related,untracked"
add chain=input action=drop connection-state=invalid \
    comment="drop invalid"
```

A router with the default configuration already has these two rules in the `input` chain and in the `forward` chain: do not add them again. In a firewall that you build yourself, place them before the other rules of the chain, because the order of the rules matters.

To see how many packets the firewall drops as invalid, print the counters of the drop rules:

```ros
/ip/firewall/filter/print stats where connection-state~"invalid"
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN    ACTION  BYTES  PACKETS
;;; defconf: drop invalid
0 input    drop       60        1
;;; defconf: drop invalid
1 forward  drop        0        0
```

:::warning
Do not use these rules on a router with asymmetric routing, where the packets of one connection take different paths in the two directions. The router sees only a part of each connection, considers the packets invalid, and drops them.
:::

### TCP connections that start in the middle

The `loose-tcp-tracking` setting controls what happens to a packet from the middle of a TCP connection that matches no entry of the connection list, for example after the entry was removed:

- With `loose-tcp-tracking=yes`, the default, the router creates an entry from such a packet and the connection continues.
- With `loose-tcp-tracking=no`, such a packet is invalid, and the "drop invalid" rules drop it.

A packet that starts a new TCP connection is still a SYN in both modes: a SYN-ACK that arrives without a SYN is invalid with `loose-tcp-tracking=yes` as well.

```ros
/ip/firewall/connection/tracking/set loose-tcp-tracking=no
```

## How long a connection stays in the list

Each entry has a timeout that depends on the protocol and the state of the connection. When the timeout reaches zero, the router removes the entry. The values are set in the `/ip/firewall/connection/tracking` menu:

- **TCP** - an established connection that is idle stays for `tcp-established-timeout`, one day by default. While sent data is not yet acknowledged, the entry has the shorter `tcp-unacked-timeout`. A connection that is opening or closing has a timeout of a few seconds, set by the timeout of its TCP state, for example `tcp-syn-sent-timeout` and `tcp-time-wait-timeout`.
- **UDP** - an entry stays for `udp-timeout`. A single request and its reply do not change that. When packets keep flowing in both directions, the entry gets the `A` (assured) flag and stays for the longer `udp-stream-timeout`.
- **ICMP** - an entry stays for `icmp-timeout`.
- **Other protocols** - a protocol that connection tracking has no own timeout for, for example IPIP, uses `generic-timeout`.

For example, to keep the entry of a device that sends a UDP request only once in a while, such as a VoIP phone that registers with its server, for one minute:

```ros
/ip/firewall/connection/tracking/set udp-timeout=1m
```

To remove idle TCP connections after two hours:

```ros
/ip/firewall/connection/tracking/set tcp-established-timeout=2h
```

A changed value applies to new connections, and to an existing connection from its next packet.

## Connection tracking settings

The settings and the state of connection tracking are in the `/ip/firewall/connection/tracking` menu:

```ros
/ip/firewall/connection/tracking/print
```

```text
                   enabled: auto  
               active-ipv4: yes   
               active-ipv6: no    
      tcp-syn-sent-timeout: 5s    
  tcp-syn-received-timeout: 5s    
   tcp-established-timeout: 1d    
      tcp-fin-wait-timeout: 10s   
    tcp-close-wait-timeout: 10s   
      tcp-last-ack-timeout: 10s   
     tcp-time-wait-timeout: 10s   
         tcp-close-timeout: 10s   
   tcp-max-retrans-timeout: 5m    
       tcp-unacked-timeout: 5m    
        loose-tcp-tracking: yes   
      liberal-tcp-tracking: no    
               udp-timeout: 30s   
        udp-stream-timeout: 3m    
              icmp-timeout: 10s   
           generic-timeout: 10m   
               max-entries: 100352
             total-entries: 2     
         total-ip4-entries: 2     
         total-ip6-entries: 0     
```

The `enabled` setting has three values:

- `auto`, the default - connection tracking is off until the router has an enabled filter, mangle or NAT rule, separately for IPv4 and IPv6. RAW rules alone do not start it. When the last such rule is removed, connection tracking stops again. `active-ipv4` and `active-ipv6` show whether it works at the moment. In this output, the router has IPv4 firewall rules and no IPv6 firewall rules.
- `yes` - connection tracking works for IPv4 and IPv6, also without firewall rules. Use it to see the connection list on a router that has no firewall rules:

  ```ros
  /ip/firewall/connection/tracking/set enabled=yes
  ```

- `no` - connection tracking is off.

:::warning
With `enabled=no`, the router keeps no connection list, and the firewall features that need connection tracking stop working. Firewall rules that use them get the `I` flag and match no packets. This includes the masquerade rule and the rules of the default configuration that accept established connections and drop new connections from the internet. The router then forwards packets without NAT and without these checks: hosts behind the router lose their NAT, and the firewall no longer protects them.
:::

`max-entries` is the number of connections that the list can hold. It depends on the amount of RAM. The router does not reserve the memory for all entries when it starts: the list grows when needed while free RAM is available, up to 1048576 entries. `total-entries` is the number of connections in the list now.

All settings are described in the CLI reference of [`/ip/firewall/connection/tracking`](../cli-reference/ip/firewall/connection/tracking).

## Features that need connection tracking

These firewall features work only while connection tracking is active:

- NAT.
- The matchers `connection-state`, `connection-nat-state`, `connection-mark`, `connection-type`, `connection-bytes`, `connection-limit`, `connection-rate` and `layer7-protocol`.
- The actions `mark-connection` and `tarpit`.

## FastTrack

IPv4 FastTrack forwards the packets of a connection on a fast path that bypasses most of the packet processing of the router. It works for TCP and UDP connections that a firewall rule with `action=fasttrack-connection` has selected. FastTrack supports source NAT, destination NAT, or both.

The default configuration FastTracks the established and related connections that the router forwards, with a pair of rules like this:

```ros
/ip/firewall/filter
add chain=forward action=fasttrack-connection \
    connection-state=established,related comment="fasttrack"
add chain=forward action=accept \
    connection-state=established,related,untracked \
    comment="accept established,related,untracked"
```

The `fasttrack-connection` action selects the connection for FastTrack and passes the packet on to the next rule. Not all packets of a FastTracked connection take the fast path, so an `accept` rule for established and related packets follows the rule. Without it, the packets that do not take the fast path reach the remaining rules of the chain.

Packets that take the fast path bypass:

- The firewall.
- Connection tracking.
- Simple queues.
- Queue trees with `parent=global`.
- IPsec.
- The HotSpot universal client.
- VRF assignment.

:::warning
The router does not apply queues, except queue trees that are attached to an interface, and firewall filter and mangle rules to FastTracked traffic. Make sure that FastTrack does not interfere with the rest of the configuration: exclude the traffic that needs these features from the `fasttrack-connection` rule. FastTrack works only with the main routing table, so also exclude the connections that use another routing table. The [Packet flow](./packet-flow-in-routeros) page has an example that excludes one host. A connection is FastTracked while a `fasttrack-connection` rule selects it. When you remove or disable that rule, the packets of the connections that are already open take the normal path again.
:::

To check whether the firewall has a FastTrack rule:

```ros
/ip/firewall/filter/print where action=fasttrack-connection
```

To see which connections are FastTracked, print the connections with the `F` flag. Add an address to see the connections of one host, for example `where fasttrack and src-address=192.168.88.10`:

```ros
/ip/firewall/connection/print where fasttrack
```

```text
Flags: S - SEEN-REPLY; A - ASSURED; C - CONFIRMED; F - FASTTRACK; s - SRCNAT
Columns: PROTOCOL, SRC-ADDRESS, SRC-PORT, DST-ADDRESS, DST-PORT, TCP-STATE, 
         TIMEOUT
#       PRO  SRC-ADDRESS    SRC-PORT  DST-ADDRESS  DST-  TCP-STATE    TIMEOUT
5 SACFs tcp  192.168.88.10     51638  10.2.0.2     2000  established  4m59s  
```

When the router has FastTracked connections, the filter, mangle and RAW tables show a dynamic rule with the comment "special dummy rule to show fasttrack counters". It is not a rule that processes packets: its counters show how much traffic takes the fast path. The mangle table has one such rule in each of the `prerouting`, `forward` and `postrouting` chains.

The `ipv4-fasttrack-active`, `ipv4-fasttrack-packets` and `ipv4-fasttrack-bytes` values of `/ip/settings` show the same for the whole router.

### Prerequisites

IPv4 FastTrack is active when all of these conditions are met:

- The packet sniffer, Torch, IP scan and MAC scan are not running. They turn FastTrack off while they run and the router turns it back on when they stop.
- FastPath is allowed in `/ip/settings`.
- Bridge FastPath is enabled, if the connection passes through a bridge interface.

FastPath and FastTrack can both be enabled, but only one of them is active at a time.

The [Packet flow](./packet-flow-in-routeros) page shows where FastTrack sits in the packet flow.
