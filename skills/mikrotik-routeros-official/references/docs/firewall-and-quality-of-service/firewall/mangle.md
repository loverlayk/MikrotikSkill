# Mangle

> The firewall mangle table of RouterOS marks packets, connections and routing decisions for other facilities, such as queues and policy routing, and changes fields of the IP header, such as the TCP MSS and DSCP.

# Mangle

The mangle table marks packets for later processing. Other facilities of RouterOS, such as queues, NAT and routing, find a packet by its mark and process it accordingly. There are three kinds of marks: packet marks, connection marks and routing marks. The marks exist only inside the router: they are not sent to the network.

The mangle table is also used to change some fields of the IP header, such as the DSCP and TTL fields, and the MSS of TCP connections.

Mangle rules are in the `/ip/firewall/mangle` menu for IPv4 and in the `/ipv6/firewall/mangle` menu for IPv6. The table has five predefined chains that cannot be deleted:

![Packet flow chains with the mangle stages marked: mangle prerouting, mangle input, mangle forward, mangle output and mangle postrouting](./img/mangle-01.webp)

- **prerouting** - processes packets when they arrive on an interface, before the routing decision.
- **input** - processes packets for the router itself, before they are given to a local process.
- **forward** - processes packets that are routed through the router.
- **output** - processes packets that the router itself sends.
- **postrouting** - processes packets when they leave through an interface.

The examples on this page use the `WAN` and `LAN` interface lists of the default configuration. Replace the addresses of the examples with the addresses of your hosts.

The default firewall [FastTracks](../connection-tracking#fasttrack) established connections, and FastTracked packets bypass the mangle rules. A mangle rule that has to see all packets of a connection works only when the connection is kept out of FastTrack. The section about marking connections shows how.

## Change MSS

VPN and PPPoE links carry smaller packets than Ethernet, because of the encapsulation overhead. A packet that is too large for the link has to be fragmented, but a packet with the "Don't Fragment" flag cannot be fragmented and is discarded. On links where path MTU discovery (PMTUD) does not work, this breaks TCP connections with large packets: web pages that do not load, and problems with FTP and e-mail.

To solve this, decrease the maximum segment size (MSS) of the TCP connections that go through the link. The MSS is the largest amount of data in one TCP packet, 40 bytes less than the packet size: for a link with an MTU of 1340 bytes, the MSS is 1300. The MSS is set in the SYN packets of a connection, so the rule matches SYN packets with an MSS that is larger than the new value:

```ros
/ip/firewall/mangle
add chain=forward action=change-mss new-mss=1300 protocol=tcp \
    tcp-flags=syn tcp-mss=1301-65535 out-interface-list=WAN \
    comment="Clamp MSS"
```

Use the interface of the link in place of the `WAN` list, for example `out-interface=pppoe-out`.

To check, open a TCP connection through the link and look at the counters of the rule:

```ros
/ip/firewall/mangle/print stats where comment~"MSS"
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN    ACTION      BYTES  PACKETS
;;; Clamp MSS
0 forward  change-mss     60        1
```

## Mark connections and packets

To process all packets of some connections, for example to limit the traffic of one host with a queue, mark the connections and then mark their packets. Matching the address of each packet is more work for the router than matching a connection mark: the first rule looks only at the first packet of a connection, and the second rule matches the mark that connection tracking keeps.

```ros
/ip/firewall/mangle
add chain=forward action=mark-connection \
    new-connection-mark=client_conn connection-state=new \
    src-address=10.0.0.2 in-interface-list=LAN \
    comment="Mark the connections of the client"
add chain=forward action=mark-packet new-packet-mark=client_p \
    connection-mark=client_conn passthrough=no \
    comment="Mark the packets of the client"
```

The first rule has the default `passthrough=yes`, so the packet continues to the next rule. The second rule has `passthrough=no`: the remaining mangle rules of the chain do not process the packet. Put rules that the marked packets also have to pass, such as the MSS rule, before it.

The first rule matches new connections. Connections that are already open when you add the rules stay without a mark.

Use the packet mark in a queue, for example in a [queue tree](../queues/queue-tree). A queue with `parent=global` limits the traffic of both directions together:

```ros
/queue/tree
add name=client parent=global packet-mark=client_p max-limit=5M
```

FastTracked packets bypass the mangle rules and the queues, except queue trees that are attached to an interface. Keep the marked connections out of FastTrack: this change makes the default FastTrack rule match only connections without a connection mark.

```ros
/ip/firewall/filter
set [find comment="defconf: fasttrack"] connection-mark=no-mark
```

Check the result with `/ip/firewall/filter/print where action=fasttrack-connection`: if your FastTrack rule has another comment, the command changes nothing.

To check the marks, send traffic from the host and look at the counters of the mangle rules. The connection list shows the marked connections with `/ip/firewall/connection/print where connection-mark=client_conn`.

```ros
/ip/firewall/mangle/print stats where comment~"client"
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN    ACTION               BYTES  PACKETS
;;; Mark the connections of the client
1 forward  mark-connection         60        1
;;; Mark the packets of the client
2 forward  mark-packet      1 270 796    1 006
```

## Route some traffic through another provider

A routing mark makes the router look up the route for a packet in another routing table. In this example the router has a second provider with the gateway 172.16.17.2 on the interface `ether5`, and the server 10.0.0.3 has to use it for the connections that it opens to the internet.

Add the interface of the second provider to the `WAN` list, so that the masquerade rule and the firewall rules of the default configuration cover it:

```ros
/interface/list/member
add list=WAN interface=ether5
```

Then add the routing table, its default route and the mangle rules:

```ros
/routing/table
add name=to-isp2 fib
/ip/route
add dst-address=0.0.0.0/0 gateway=172.16.17.2 routing-table=to-isp2
/ip/firewall/mangle
add chain=prerouting action=mark-connection \
    new-connection-mark=isp2_conn connection-state=new \
    src-address=10.0.0.3 dst-address-type=!local \
    in-interface-list=LAN comment="Server through the second provider"
add chain=prerouting action=mark-routing new-routing-mark=to-isp2 \
    connection-mark=isp2_conn in-interface-list=LAN passthrough=no \
    comment="Server through the second provider"
```

- The first rule marks the connections that the server opens. `dst-address-type=!local` leaves out the connections to the router itself. Connections that are opened from the internet to the server, for example through a port forward, get no mark and use the main routing table.
- The second rule sets the routing mark on the packets of the marked connections that arrive from the local network. The mark is set in the `prerouting` chain, before the routing decision.
- FastTrack works only with the main routing table. The FastTrack rule of the previous section, with `connection-mark=no-mark`, keeps the marked connections out of FastTrack.

When the interface of the second provider is down, the route of the `to-isp2` table is inactive, and the server uses the main routing table again.

To check, open connections from the server and look at the counters:

```ros
/ip/firewall/mangle/print stats where comment~"second provider"
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN       ACTION               BYTES  PACKETS
;;; Server through the second provider
0 prerouting  mark-connection        116        2
;;; Server through the second provider
1 prerouting  mark-routing     1 235 553      479
```

## Set the DSCP value

To set the DSCP field of packets, for example so that the devices after the router give priority to voice traffic, use `action=change-dscp`. This example sets DSCP 46 on the UDP packets that the PBX 10.0.0.3 sends to the internet. The rule changes only the packets that are not FastTracked.

```ros
/ip/firewall/mangle
add chain=postrouting action=change-dscp new-dscp=46 protocol=udp \
    src-address=10.0.0.3 out-interface-list=WAN passthrough=no \
    comment="Voice from the PBX"
```

```ros
/ip/firewall/mangle/print stats where comment~"Voice"
```

```text
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN        ACTION       BYTES  PACKETS
;;; Voice from the PBX
1 postrouting  change-dscp    255        5
```

All actions and properties are described in the CLI reference of [`/ip/firewall/mangle`](../../cli-reference/ip/firewall/mangle) and [`/ipv6/firewall/mangle`](../../cli-reference/ipv6/firewall/mangle).
