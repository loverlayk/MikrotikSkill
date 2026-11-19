# Filter

> The firewall filter of RouterOS accepts or drops packets in the input, forward and output chains. Add rules to the default firewall, for example to allow a service from the internet, block a device or isolate a guest...

# Filter

The firewall filter decides which packets the router accepts and which it drops: packets that pass through the router to and from your network, packets for the router itself, and packets that the router sends.

Filter rules are in the `/ip/firewall/filter` menu for IPv4 and in the `/ipv6/firewall/filter` menu for IPv6. The default configuration of MikroTik home and office routers already has a firewall that protects the router and the local network from the internet. The first part of this page adds rules to that firewall. The second part builds a firewall from the start.

## Chains and rule order

The filter has three predefined chains that cannot be deleted:

![Packet flow chains with the filter marked: filter input follows mangle input, filter forward follows mangle forward, filter output follows mangle output](./img/filter-01.webp)

- **input** - processes packets that enter the router and have one of the addresses of the router as their destination. Packets that pass through the router are not processed by the rules of the input chain.
- **forward** - processes packets that pass through the router.
- **output** - processes packets that the router itself sends. Packets that pass through the router are not processed by the rules of the output chain.

The router checks a packet against the rules of a chain from the top. The first rule that matches decides what happens to the packet. After an action such as `accept`, `drop` or `reject`, the router does not check the remaining rules. After `action=passthrough`, it continues with the next rule. A packet that no rule matches is accepted. The order of the rules therefore matters: a rule after a matching `accept` or `drop` rule does not see the packet.

You can add chains of your own and send packets to them with `action=jump`. The section about ICMP on this page has an example.

There are two ways to build a filter:

- Accept the traffic that you need and drop everything else. This is more secure, and it limits the damage when a service is misconfigured, but you have to add a rule for each new service.
- Drop only the traffic that you do not want and accept everything else. This is less work in a network where you cannot list all services that the users need, such as a customer network.

The default firewall uses the first way for traffic from the internet.

## Add rules to the default firewall

The examples in this section are for a router whose default configuration has a firewall. Enter the commands in the terminal of WinBox or WebFig, or over SSH. The examples use the `WAN` and `LAN` interface lists of the default configuration: `WAN` holds the interface to the internet and `LAN` the local bridge.

Each example places its rule before a rule of the default firewall with `place-before=[find comment="..."]`, which finds that rule by its comment. If the comment does not exist on your router, the command fails with "no such item": look at your rules with `/ip/firewall/filter/print` and use the comment of the rule that the new rule has to precede. A rule that is added without `place-before` goes to the end of the chain, after the rules that drop the traffic.

The default firewall accepts the packets of established connections with its first rules. For that reason, most rules only have to deal with the first packet of a connection.

The examples are IPv4 rules. If your network also uses IPv6, add the matching rules in `/ipv6/firewall/filter`: an IPv4 rule does not stop IPv6 traffic.

### Allow access to a service of the router from the internet

The default firewall drops what arrives from the internet for the router itself, except ICMP. To manage the router with WinBox from another place that has a fixed public address, accept TCP port 8291 from that address before the rule that drops the rest. Replace 198.51.100.7 with the public address that you connect from:

```ros
/ip/firewall/filter
add chain=input action=accept protocol=tcp dst-port=8291 \
    src-address=198.51.100.7 in-interface-list=WAN \
    comment="WinBox from the office" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

Accept a management service only from addresses that you trust, never from the whole internet. For access from changing addresses, use a VPN.

To check the rule, connect from that address and look at the counters of the rule:

```ros
/ip/firewall/filter/print stats where comment~"WinBox"
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN  ACTION  BYTES  PACKETS
;;; WinBox from the office
0 input  accept     60        1
```

### Block a device from the internet

To stop one device of the local network from reaching the internet, drop its packets in the forward chain. In this example an IP camera has the address 192.168.88.50. Give such a device a static lease in `/ip/dhcp-server/lease`, so that its address does not change.

```ros
/ip/firewall/filter
add chain=forward action=drop src-address=192.168.88.50 \
    out-interface-list=WAN comment="No internet for the camera" \
    place-before=[find comment="defconf: fasttrack"]
```

The rule is placed before the rules that FastTrack and accept established connections, so it also matches the packets of connections that are already open. The section about blocking an open connection on this page describes what to do with FastTracked connections. The camera can still reach the router and the devices of the local network.

The counters of the rule grow when the camera tries to reach the internet:

```ros
/ip/firewall/filter/print stats where comment~"camera"
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN    ACTION  BYTES  PACKETS
;;; No internet for the camera
1 forward  drop      168        3
```

### Reject instead of drop

A dropped packet gets no answer, so the application on the sending host waits until it times out. With `action=reject`, the router answers with an error, and the application fails immediately. This example rejects Telnet connections that hosts of the local network open through the router, with a TCP reset:

```ros
/ip/firewall/filter
add chain=forward action=reject reject-with=tcp-reset \
    protocol=tcp dst-port=23 in-interface-list=LAN \
    comment="No Telnet from the LAN" \
    place-before=[find comment="defconf: fasttrack"]
```

A host in the local network that opens a Telnet connection now gets "connection refused" without waiting. Use `reject` for the hosts of your own network, and `drop` for traffic from the internet, so that the router does not answer port scans.

```ros
/ip/firewall/filter/print stats where comment~"Telnet"
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN    ACTION  BYTES  PACKETS
;;; No Telnet from the LAN
5 forward  reject     60        1
```

### Keep a guest network away from the local network

The default firewall does not separate the networks behind the router from each other: a device in a guest network can reach the devices of the main network. In this example the guest network is on the interface `bridge-guest`. The rules let the guests reach the internet and the DNS server of the router. They do not separate the guest devices from each other.

```ros
/interface/list
add name=GUEST
/interface/list/member
add list=GUEST interface=bridge-guest
/ip/firewall/filter
add chain=forward action=drop connection-state=new \
    in-interface-list=GUEST out-interface-list=!WAN \
    comment="Guests reach only the internet" \
    place-before=[find comment="defconf: fasttrack"]
add chain=input action=accept protocol=udp dst-port=53 \
    in-interface-list=GUEST comment="DNS for guests" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=accept protocol=tcp dst-port=53 \
    in-interface-list=GUEST comment="DNS for guests" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

- The forward rule drops new connections from the guest network to everything that is not the internet. Because it matches only `connection-state=new`, the devices of the local network can still open connections to the guest devices.
- The interface `bridge-guest` must not be in the `LAN` list: check with `/interface/list/member/print`. The default rule "drop all not coming from LAN" then keeps the guests away from the router itself, except for ICMP. The two input rules make an exception for DNS, which the router answers when `allow-remote-requests=yes` is set in `/ip/dns`.
- The interface to the internet must be in the `WAN` list, or the forward rule also drops the guests' internet traffic.
- The DHCP server of the router works for the guest network without a firewall rule.
- Connections from guests to the local network that are already open stay open. The section about blocking an open connection on this page shows how to remove them.

To check the rules, try to reach a device of the local network from a guest device, and look at the counters:

```ros
/ip/firewall/filter/print stats where in-interface-list=GUEST
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN    ACTION  BYTES  PACKETS
;;; DNS for guests
2 input    accept     56        1
;;; DNS for guests
3 input    accept      0        0
;;; Guests reach only the internet
4 forward  drop      168        3
```

### Log what a rule drops

To see which packets a rule drops, turn on logging for the rule. This example logs what the default firewall drops in the input chain:

```ros
/ip/firewall/filter
set [find comment="defconf: drop all not coming from LAN"] \
    log=yes log-prefix="input-drop"
```

The log entries start with the prefix. They show the interface, the addresses, the protocol and the ports of each packet:

```ros
/log/print where message~"input-drop"
```

This rule drops what does not come from the `LAN` list, so the log also shows packets from other local networks, such as a guest network. To log what the firewall drops on the way from the internet to the local network, do the same for the rule of the forward chain:

```ros
/ip/firewall/filter
set [find comment="defconf: drop all from WAN not DSTNATed"] \
    log=yes log-prefix="forward-drop"
```

Logging every dropped packet costs CPU time and fills the log on a router that is under attack. Turn it off when you have what you need. The command for the forward rule is the same, with the comment of that rule:

```ros
/ip/firewall/filter
set [find comment="defconf: drop all not coming from LAN"] log=no
```

## Block a connection that is already open

A drop rule that you add after the rules that accept established connections stops only new connections: connections that are already open keep working until they end.

To stop open connections too, put the drop rule before the rules that accept or FastTrack established connections, and then remove the connections from the connection list. This example blocks the address 203.0.113.10 for all hosts behind the router:

```ros
/ip/firewall/filter
add chain=forward action=drop dst-address=203.0.113.10 \
    comment="Block 203.0.113.10" \
    place-before=[find comment="defconf: fasttrack"]
/ip/firewall/connection
remove [find dst-address=203.0.113.10]
```

The packets of a FastTracked connection that take the fast path bypass the filter rules. When the connection is removed from the list, its next packets go through the rules again and reach the drop rule.

Removing a connection without the drop rule does not stop it: with the default `loose-tcp-tracking=yes` setting, the router adds the connection to the list again when its next packet arrives. See [Connection tracking](../connection-tracking).

To check, look at the counters of the rule, and make sure that the connection list has no entry for the address: `/ip/firewall/connection/print where dst-address=203.0.113.10`.

```ros
/ip/firewall/filter/print stats where comment~"Block"
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN    ACTION   BYTES  PACKETS
;;; Block 203.0.113.10
0 forward  drop    38 532       17
```

## Build an IPv4 firewall

This section builds a firewall on a router that has no filter rules. It uses the interface lists `WAN` for the interfaces towards the internet and `LAN` for the local interfaces. If the router does not have the lists, create them first. In this example `ether1` is the interface to the internet and `bridge` is the local bridge:

```ros
/interface/list
add name=WAN
add name=LAN
/interface/list/member
add list=WAN interface=ether1
add list=LAN interface=bridge
```

The filter does not translate addresses. For internet access of a network with private addresses, the router also needs a source NAT rule, see [NAT](./nat).

Follow these rules of thumb:

- Accept established and related connections first, so that the remaining rules work only with new connections. This decreases the load on the router.
- Accept what you need.
- Drop everything else. You can set `log=yes` on the drop rules to log attackers, but logging adds load to the CPU during heavy attacks.

### Protect the router

The input chain protects the router itself. In this example, any address can send ICMP packets to the router, for example a ping. Only the addresses 192.168.88.2-192.168.88.254 of the local network have access to everything else. Replace the range with the addresses of your network.

:::warning
The last rule of this block drops every connection to the router that the rules before it do not accept. Before you add the rules, make sure that the address from which you manage the router is in the `allowed_to_router` list and that its interface is in the `LAN` list, or use [Safe Mode](../../management-tools/console#safe-mode), so that you do not lock yourself out.
:::

```ros
/ip/firewall/address-list
add list=allowed_to_router address=192.168.88.2-192.168.88.254
/ip/firewall/filter
add chain=input action=accept \
    connection-state=established,related,untracked \
    comment="Accept established, related, untracked"
add chain=input action=drop connection-state=invalid \
    comment="Drop invalid"
add chain=input action=accept src-address-list=allowed_to_router \
    in-interface-list=LAN \
    comment="Accept from the management addresses"
add chain=input action=accept protocol=icmp comment="Accept ICMP"
add chain=input action=drop comment="Drop everything else"
```

The rule that accepts the management addresses also checks the interface. A packet from the internet that only claims to have one of these source addresses does not match it.

### Protect the devices of the local network

The forward chain protects the devices behind the router. In this example the firewall drops unwanted traffic and accepts everything else.

First create an address list with the addresses that cannot be the source or the destination of a packet on the internet:

```ros
/ip/firewall/address-list
add list=not_in_internet address=0.0.0.0/8 comment=RFC6890
add list=not_in_internet address=172.16.0.0/12 comment=RFC6890
add list=not_in_internet address=192.168.0.0/16 comment=RFC6890
add list=not_in_internet address=10.0.0.0/8 comment=RFC6890
add list=not_in_internet address=169.254.0.0/16 comment=RFC6890
add list=not_in_internet address=127.0.0.0/8 comment=RFC6890
add list=not_in_internet address=224.0.0.0/4 comment=Multicast
add list=not_in_internet address=198.18.0.0/15 comment=RFC6890
add list=not_in_internet address=192.0.0.0/24 comment=RFC6890
add list=not_in_internet address=192.0.2.0/24 comment=RFC6890
add list=not_in_internet address=198.51.100.0/24 comment=RFC6890
add list=not_in_internet address=203.0.113.0/24 comment=RFC6890
add list=not_in_internet address=100.64.0.0/10 comment=RFC6890
add list=not_in_internet address=240.0.0.0/4 comment=RFC6890
```

Then add the rules:

```ros
/ip/firewall/filter
add chain=forward action=fasttrack-connection \
    connection-state=established,related comment="FastTrack"
add chain=forward action=accept \
    connection-state=established,related,untracked \
    comment="Accept established, related, untracked"
add chain=forward action=drop connection-state=invalid \
    log=yes log-prefix=invalid comment="Drop invalid"
add chain=forward action=drop dst-address-list=not_in_internet \
    in-interface-list=LAN out-interface-list=!LAN \
    log=yes log-prefix=!public_from_LAN \
    comment="Drop tries to reach not public addresses from LAN"
add chain=forward action=drop connection-state=new \
    connection-nat-state=!dstnat in-interface-list=WAN \
    log=yes log-prefix=!NAT \
    comment="Drop incoming packets that are not NATed"
add chain=forward action=drop src-address-list=not_in_internet \
    in-interface-list=WAN log=yes log-prefix=!public \
    comment="Drop incoming from internet which is not public IP"
add chain=forward action=drop src-address=!192.168.88.0/24 \
    in-interface-list=LAN log=yes log-prefix=LAN_!LAN \
    comment="Drop packets from LAN that do not have LAN IP"
add chain=forward action=jump jump-target=icmp protocol=icmp \
    comment="Jump to ICMP filters"
```

The rules do the following, in this order:

- FastTrack and accept the packets of established and related connections, so that the remaining rules see only new connections and invalid packets.
- Drop invalid packets and log them with the prefix "invalid".
- Drop packets from the local network to addresses that do not exist on the internet, and log them with the prefix "!public_from_LAN". If the router is behind another router with private addresses, for example the modem of the provider, or has local networks on interfaces that are not in the `LAN` list, remove those networks from the list.
- Drop new connections from the internet that are not destination NATed, which means that no port forward matches them, and log them with the prefix "!NAT".
- Drop packets from the internet whose source address is not a public address, and log them with the prefix "!public". The rule before it has already dropped the new connections that no port forward matches, so this rule works on the port-forwarded connections.
- Drop packets from the local network that do not have an address of the local network, 192.168.88.0/24 in this example, and log them with the prefix "LAN_!LAN". If the router has more local networks, change the rule so that it accepts their addresses too.
- Send the remaining ICMP packets to the `icmp` chain. The chain is created by the rules of the next block.

The rules log what they drop. Remove `log=yes` from the rules whose log entries you do not need.

### Accept only the needed ICMP messages

The `icmp` chain accepts the ICMP types and codes that the network needs and drops the rest. The jump rule in the forward chain sends ICMP packets to it. The forward chain accepts established and related packets before the jump, so the chain processes the ICMP packets that start a connection, such as echo requests:

```ros
/ip/firewall/filter
add chain=icmp action=accept protocol=icmp icmp-options=0:0 \
    comment="Echo reply"
add chain=icmp action=accept protocol=icmp icmp-options=3:0 \
    comment="Net unreachable"
add chain=icmp action=accept protocol=icmp icmp-options=3:1 \
    comment="Host unreachable"
add chain=icmp action=accept protocol=icmp icmp-options=3:4 \
    comment="Fragmentation required"
add chain=icmp action=accept protocol=icmp icmp-options=8:0 \
    comment="Echo request"
add chain=icmp action=accept protocol=icmp icmp-options=11:0 \
    comment="Time exceeded"
add chain=icmp action=accept protocol=icmp icmp-options=12:0 \
    comment="Parameter problem"
add chain=icmp action=drop comment="Drop all other types"
```

## Build an IPv6 firewall

The IPv6 firewall follows the same idea as the IPv4 firewall, but IPv6 needs more protocols to work, and the devices of the local network usually have public addresses.

### Protect the router

First create an address list with the addresses of your local network: the link-local addresses, the public prefix that your provider has assigned, and a ULA prefix if you use one. Replace `2001:db8:1::/48` and `fd12:672e:6f65:8899::/64` with your prefixes. The same list is used for the devices of the local network in the next section: a device whose address is not in the list can send only ICMPv6 to the internet.

:::warning
The last rule of this block drops every connection to the router that the rules before it do not accept. Before you add the rules, make sure that the address from which you manage the router is in the `allowed` list and that its interface is in the `LAN` list, or use [Safe Mode](../../management-tools/console#safe-mode).
:::

Then add the input rules:

```ros
/ipv6/firewall/address-list
add list=allowed address=fe80::/10 comment="Link-local"
add list=allowed address=2001:db8:1::/48 comment="Public prefix"
add list=allowed address=fd12:672e:6f65:8899::/64 comment="ULA prefix"
/ipv6/firewall/filter
add chain=input action=accept \
    connection-state=established,related,untracked \
    comment="Accept established, related, untracked"
add chain=input action=drop connection-state=invalid \
    comment="Drop invalid"
add chain=input action=accept protocol=icmpv6 comment="Accept ICMPv6"
add chain=input action=accept protocol=udp dst-port=33434-33534 \
    comment="Accept UDP traceroute"
add chain=input action=accept protocol=udp dst-port=546 \
    src-address=fe80::/10 \
    comment="Accept DHCPv6 client prefix delegation"
add chain=input action=drop src-address=fe80::/10 \
    in-interface-list=WAN log=yes log-prefix=dropLL_from_public \
    comment="Drop link-local from the internet"
add chain=input action=accept src-address-list=allowed \
    in-interface-list=LAN \
    comment="Accept from the allowed addresses"
add chain=input action=drop comment="Drop everything else"
```

The rules do the following:

- Accept the packets of established, related and untracked connections, and drop invalid packets.
- Accept ICMPv6, which IPv6 needs for neighbor discovery.
- Accept UDP traceroute.
- Accept the answers to the DHCPv6 client of the router, which it uses for prefix delegation.
- Drop packets with a link-local source address that arrive from the internet, and log them.
- Accept packets from the addresses of the `allowed` list that arrive from the local network.
- Drop everything else.

:::note
In setups with a DHCPv6 relay, the source address of the DHCPv6 packets can be outside the link-local range. In that case, remove the `src-address` from the rule that accepts the DHCPv6 client prefix delegation, or change it to the address of the relay.
:::

### Protect the devices of the local network

This step is more important for IPv6 than for IPv4. With IPv4, the devices mostly have private addresses behind NAT and cannot be reached directly from the internet. With IPv6, the devices usually have public addresses and can be reached from the internet, so they need filter rules that protect them.

A basic protection of the local network:

- Accepts the packets of established, related and untracked connections.
- Drops invalid packets.
- Accepts ICMPv6 from the local network.
- Accepts new connections only from the local network, from the addresses of the `allowed` list.
- Drops everything else.

```ros
/ipv6/firewall/filter
add chain=forward action=accept \
    connection-state=established,related,untracked \
    comment="Accept established, related, untracked"
add chain=forward action=drop connection-state=invalid \
    log=yes log-prefix=ipv6,invalid comment="Drop invalid"
add chain=forward action=accept protocol=icmpv6 \
    in-interface-list=LAN comment="Accept ICMPv6 from the LAN"
add chain=forward action=accept src-address-list=allowed \
    in-interface-list=LAN comment="Accept new connections from the LAN"
add chain=forward action=drop comment="Drop everything else"
```

## RAW filtering

The firewall RAW table drops or bypasses packets before connection tracking, which reduces the load on the CPU. It is well suited for DoS and DDoS attack mitigation.

The RAW table has its own chains, `prerouting` and `output`, and does not have matchers that depend on connection tracking. Chains, properties and examples are described on the [RAW](./raw) page.

## Read more

- [Common Firewall Matchers and Actions](./common-firewall-matchers-and-actions) - rule counters and the order of the matchers.
- [Connection tracking](../connection-tracking) - connection states and FastTrack.
- [Building advanced firewall](../user-guides/building-advanced-firewall)
- [Connection Rate](../user-guides/connection-rate)
- [SSH brute-force protection](../user-guides/bruteforce-prevention)
- [Syn/DoS protection](../user-guides/ddos-protection)
- CLI reference: [`/ip/firewall/filter`](../../cli-reference/ip/firewall/filter), [`/ipv6/firewall/filter`](../../cli-reference/ipv6/firewall/filter)
