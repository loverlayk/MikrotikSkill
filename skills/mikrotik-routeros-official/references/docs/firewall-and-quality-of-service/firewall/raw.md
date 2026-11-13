# RAW

> The RAW firewall table in RouterOS processes packets before connection tracking. Use it to drop unwanted packets early, or to exclude traffic from connection tracking with action=notrack.

# RAW

The firewall RAW table processes packets before [connection tracking](../connection-tracking). It has two uses:

- Drop unwanted packets before connection tracking and the mangle, NAT and filter rules process them.
- Exclude traffic from connection tracking with `action=notrack`.

In both cases, the router creates no connection tracking entry for the packet.

RAW rules are in `/ip/firewall/raw` for IPv4 and in `/ipv6/firewall/raw` for IPv6. The table has two built-in chains:

- **prerouting** - every packet that enters the router, both packets for the router itself and packets that pass through it.
- **output** - packets that the router itself sends.

RAW rules are stateless: a rule sees each packet on its own and does not know which connection the packet belongs to.

## Drop unwanted traffic before connection tracking

Drop packets that arrive from the internet with a source address that is never valid there. `WAN` is the interface list of the default configuration that holds the internet port:

```ros
/ip/firewall/address-list
add list=bad_src address=0.0.0.0/8 comment="This network"
add list=bad_src address=127.0.0.0/8 comment="Loopback"
add list=bad_src address=224.0.0.0/4 comment="Multicast"
add list=bad_src address=240.0.0.0/4 comment="Reserved"
/ip/firewall/raw
add chain=prerouting action=drop in-interface-list=WAN \
    src-address-list=bad_src comment="Drop invalid source addresses"
```

The rule drops every packet from these addresses that arrives on the WAN, before the router creates a connection tracking entry for it. Because the rule is stateless, it also drops the replies to connections that your own hosts open to these addresses. Put only addresses in the list that must never reach you. For how to maintain a list, see [Address lists](./address-lists).

To check that the rule works, look at its counters:

```ros
[admin@MikroTik] > /ip/firewall/raw/print stats
Flags: D - DYNAMIC
Columns: CHAIN, ACTION, BYTES, PACKETS
#   CHAIN       ACTION       BYTES  PACKETS
;;; special dummy rule to show fasttrack counters
0 D prerouting  passthrough      0        0
;;; Drop invalid source addresses
1   prerouting  drop           168        3
```

The dynamic rule at the top belongs to [FastTrack](../packet-flow-in-routeros#fasttrack). To set the counters back to zero, use `/ip/firewall/raw/reset-counters-all`.

To detect and drop a flood towards one destination, see [DDoS protection](../user-guides/ddos-protection).

## Exclude traffic from connection tracking

A router that routes between two local networks does not need connection tracking for that traffic, as long as no NAT and no stateful filtering apply to it. In this example, the networks are 192.168.88.0/24 and 192.168.99.0/24.

This example is for a router that does not FastTrack this traffic, for example because you removed the FastTrack rule to use queues on it. The default configuration has a FastTrack rule for established connections, and a FastTrack rule does not match untracked packets, so the following rules take the traffic off FastTrack there.

A connection has packets in both directions, so add one rule for each direction:

```ros
/ip/firewall/raw
add chain=prerouting action=notrack src-address=192.168.88.0/24 \
    dst-address=192.168.99.0/24 comment="Do not track LAN to LAN"
add chain=prerouting action=notrack src-address=192.168.99.0/24 \
    dst-address=192.168.88.0/24 comment="Do not track LAN to LAN"
```

Packets that match `action=notrack` continue through the remaining RAW rules and through the mangle and filter rules, but the router creates no entry for them in `/ip/firewall/connection`. In mangle and filter, they have the connection state `untracked`.

The filter rules must accept untracked packets. The default configuration does: its rules that accept established and related connections in the input and forward chains also list `untracked`. Check your firewall:

```ros
[admin@MikroTik] > /ip/firewall/filter/print where connection-state~"untracked"
0  ;;; defconf: accept established,related,untracked
   chain=input action=accept connection-state=established,related,untracked

1  ;;; defconf: accept established,related, untracked
   chain=forward action=accept connection-state=established,related,untracked
```

If your own rules accept only established and related connections, add `untracked` to them:

```ros
/ip/firewall/filter
set [find action=accept connection-state="established,related"] \
    connection-state=established,related,untracked
```

To check that the traffic is no longer tracked, ping a host in 192.168.88.0/24 from the other network five times. Right after the ping, count the connection entries between the two networks:

```ros
/ip/firewall/connection/print count-only \
    where src-address~"^192.168.99\\." and dst-address~"^192.168.88\\."
```

The command prints `0`. Without the `notrack` rules, the same ping leaves one entry, which expires 10 seconds after the last packet. The counters do not depend on timing, and the `notrack` rules show the five packets of each direction:

```ros
[admin@MikroTik] > /ip/firewall/raw/print stats
Flags: D - DYNAMIC
Columns: CHAIN, ACTION, BYTES, PACKETS
#   CHAIN       ACTION       BYTES  PACKETS
;;; special dummy rule to show fasttrack counters
0 D prerouting  passthrough      0        0
;;; Drop invalid source addresses
1   prerouting  drop           168        3
;;; Do not track LAN to LAN
2   prerouting  notrack        280        5
;;; Do not track LAN to LAN
3   prerouting  notrack        280        5
```

:::warning
Untracked packets have no connection, so everything that depends on one does not apply to them:

- NAT rules do not process them. Do not use `notrack` for traffic that needs source or destination NAT, such as traffic that leaves through a masquerade rule.
- Matchers that read the connection entry, such as `connection-mark`, do not match them, and `action=mark-connection` has no effect on them. `connection-state=untracked` matches them.

:::

Connections that are open when you add the rules continue to work. Their packets are untracked from then on, and the old entries stay in the connection table until they time out. While you add the rules, the firewall can drop a few packets of these connections as invalid.

### Exclude one service

When you exclude one service instead of whole networks, the rule for the replies must match the source address and source port of the server. For example, exclude the DNS traffic of the server 192.168.88.2 that uses UDP:

```ros
/ip/firewall/raw
add chain=prerouting action=notrack protocol=udp dst-port=53 \
    dst-address=192.168.88.2 comment="Do not track DNS queries"
add chain=prerouting action=notrack protocol=udp src-port=53 \
    src-address=192.168.88.2 comment="Do not track DNS replies"
```

To check the rules, resolve a name through the server from the other network and look at the counters. Each rule counts one packet:

```ros
[admin@MikroTik] > /ip/firewall/raw/print stats where comment~"DNS"
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN       ACTION   BYTES  PACKETS
;;; Do not track DNS queries
2 prerouting  notrack     54        1
;;; Do not track DNS replies
3 prerouting  notrack     70        1
```

Without the second rule, the replies are still tracked. Connection tracking has not seen the query, so it handles a UDP reply as a new connection from the server to the client and creates an entry for it. For a TCP service, connection tracking handles the replies as invalid, and the default firewall drops them.

When the service runs on the router itself, the replies do not pass through the prerouting chain. Put the rule for the replies in the output chain. In this example, the router has the address 192.168.88.1:

```ros
/ip/firewall/raw
add chain=prerouting action=notrack protocol=udp dst-port=53 \
    dst-address=192.168.88.1 comment="Do not track DNS to the router"
add chain=output action=notrack protocol=udp src-port=53 \
    src-address=192.168.88.1 comment="Do not track DNS from the router"
```

## Group rules in a chain

Rules can be grouped in your own chains. RouterOS creates a chain when you add the first rule with a new chain name. A packet enters the chain through a rule with `action=jump`. It goes back to the next rule of the calling chain with `action=return`, or when it reaches the end of the chain. Rules in a chain that no jump rule leads to are not processed.

Send the UDP packets that arrive from the internet through a chain that drops the replies of services commonly abused for amplification attacks: Chargen (port 19), SSDP (port 1900) and Memcached (port 11211). Packets from the addresses in the list `trusted` skip the check:

```ros
/ip/firewall/address-list
add list=trusted address=198.51.100.20 comment="Office router"
/ip/firewall/raw
add chain=prerouting action=jump jump-target=udp-check \
    in-interface-list=WAN protocol=udp comment="Check UDP from the WAN"
add chain=udp-check action=return src-address-list=trusted \
    comment="Do not check trusted addresses"
add chain=udp-check action=drop protocol=udp src-port=19,1900,11211 \
    comment="Drop replies of common amplification services"
```

The counters show how many packets entered the chain and what happened to them. Here, two UDP packets entered the chain. One had source port 1900 and was dropped; the other reached the end of the chain and returned:

```ros
[admin@MikroTik] > /ip/firewall/raw/print stats
Flags: D - DYNAMIC
Columns: CHAIN, ACTION, BYTES, PACKETS
#   CHAIN       ACTION       BYTES  PACKETS
;;; special dummy rule to show fasttrack counters
0 D prerouting  passthrough      0        0
;;; Drop invalid source addresses
1   prerouting  drop           168        3
;;; Do not track LAN to LAN
2   prerouting  notrack        280        5
;;; Do not track LAN to LAN
3   prerouting  notrack        280        5
;;; Check UDP from the WAN
4   prerouting  jump           292        2
;;; Do not check trusted addresses
5   udp-check   return           0        0
;;; Drop replies of common amplification services
6   udp-check   drop            57        1
```

## IPv6

The IPv6 RAW table is separate and has the same chains and actions. For example, drop packets that arrive from the internet with the documentation prefix as the source address:

```ros
/ipv6/firewall/raw
add chain=prerouting action=drop in-interface-list=WAN \
    src-address=2001:db8::/32 comment="Drop the documentation prefix"
```

The matchers differ in a few places. IPv6 rules have `headers` and `hop-limit`. They do not have `fragment`, `hotspot`, `ipv4-options`, `psd` and `ttl`.

## How RAW rules behave

### Place in the packet flow

RAW rules are the first rules of the IP firewall that a packet meets. See [Packet Flow in RouterOS](../packet-flow-in-routeros) for the full diagram. This position has the following effects:

- Connection tracking has not seen the packet yet, so RAW rules have no matchers that depend on it.
- NAT has not been applied yet. In the prerouting chain, `dst-address` is the destination address of the packet before destination NAT.
- A packet dropped in the RAW table does not create a connection tracking entry.

### Rule processing

Rules are processed from the top of the chain. `accept`, `drop` and `notrack` differ in what happens next:

- `accept` - the packet skips the remaining RAW rules and goes on to connection tracking.
- `drop` - the packet is discarded.
- `notrack` - the packet is marked to bypass connection tracking and goes on to the next RAW rule.

The other actions, `log`, `passthrough`, `add-src-to-address-list` and `add-dst-to-address-list`, do their work and pass the packet to the next rule. `jump` and `return` move the packet between chains.

A rule without `action` accepts the packet. A packet that matches no rule is accepted as well.

The router refuses a rule with `out-interface` in the prerouting chain and a rule with `in-interface` in the output chain.

### Differences from filter

| | Filter | RAW |
| :-- | :-- | :-- |
| Built-in chains | input, forward, output | prerouting, output |
| Position | After connection tracking | Before connection tracking |
| Matchers that depend on connection tracking | Yes | No |
| Actions that the other table lacks | `fasttrack-connection`, `reject`, `tarpit` | `notrack` |

These filter properties are not available in the RAW table: `connection-bytes`, `connection-limit`, `connection-mark`, `connection-nat-state`, `connection-rate`, `connection-state`, `connection-type`, `hw-offload`, `layer7-protocol`, `p2p`, `realm`, `reject-with` and `routing-mark`.

### Fragmented packets

IPv4 and IPv6 RAW rules see fragmented packets differently:

- **IPv4** - RAW rules see every fragment on its own, before the packet is assembled, also when connection tracking is enabled. `fragment=yes` matches all fragments except the first one, and `packet-size` matches the size of a fragment, not of the whole packet. After the RAW table, connection tracking assembles the packet, and the other firewall tables see one whole packet.
- **IPv6** - RAW rules see the assembled packet.

An IPv4 packet that bypasses connection tracking with `action=notrack` is not assembled. When the router forwards it, it stays fragmented in the mangle and filter rules, where only the first fragment has the port numbers. Packets for the router itself are assembled before the input chain.

## Read more

- [Filter](./filter)
- [Address lists](./address-lists)
- [Connection tracking](../connection-tracking)
- [Building advanced firewall](../user-guides/building-advanced-firewall)

For all rule properties, see the CLI reference for [`/ip/firewall/raw`](../../cli-reference/ip/firewall/raw/) and [`/ipv6/firewall/raw`](../../cli-reference/ipv6/firewall/raw/).
