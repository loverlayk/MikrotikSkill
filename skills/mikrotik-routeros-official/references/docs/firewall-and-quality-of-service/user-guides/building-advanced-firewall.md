# Building Advanced Firewall

> This page guides building an advanced firewall on MikroTik RouterOS by configuring interface lists, filtering rules for IPv4 and IPv6, accepting ICMP/DHCPv6 while blocking invalid addresses, and managing traffic...

# Building Advanced Firewall

This example builds a complete firewall for a router that connects a local network to the Internet. It uses as many firewall features as possible to show how they work together: interface lists, address lists, connection states, FastTrack, NAT, user-defined chains and RAW rules, for IPv4 and for IPv6.

Most of the filtering is done in the [RAW](../firewall/raw) table, before connection tracking. The [filter](../firewall/filter) table has only a basic rule set: it accepts established, related and untracked connections and drops everything else that does not come from the LAN.

## Before you start

- The example is a complete rule set for a router that has no firewall rules. The default configuration has its own firewall rules, which do a part of the same work. On such a router, the rules of this example replace the default filter, NAT and IPv6 firewall rules; rules that are added after the default ones are duplicates.
- The LAN network of the example is 192.168.88.0/24 on the interface `bridge`, and the WAN interface is `ether1`. Two RAW rules contain the LAN network. Replace it with your network before you add the rules: the rule "drop local if not from default IP range" drops everything that a LAN device with another address sends, your own session included.
- Add the rules from a device in the LAN network, and use [Safe Mode](../../management-tools/console#safe-mode). The rules do not accept management access from the WAN side.
- Every interface must be in the `WAN` or the `LAN` list. The last RAW rule drops all packets that arrive on an interface that is in neither list, for example a PPPoE client, a VPN or a VLAN interface that is added later.
- Add the blocks in the order of the page, the address lists of a section before its rules. A rule that uses an address list without entries is added without an error.
- The IPv6 blocks are needed only if the router uses IPv6.

## Interface lists

Two interface lists are used: `WAN` and `LAN`. The lists make the rules independent of interface names. The `WAN` list contains the interfaces that are connected to the Internet, in this example `ether1`. The `LAN` list contains the local network interfaces, in this example `bridge`.

```ros
/interface/list
add name=WAN comment=defconf
add name=LAN comment=defconf
/interface/list/member
add list=LAN interface=bridge comment=defconf
add list=WAN interface=ether1 comment=defconf
```

The default configuration already has these lists and members. If your router has them, skip this block.

## Protect the router

The goal is to allow access to the router only from the LAN and to drop everything else.

ICMP is accepted as well. This rule accepts the ICMP packets that have passed the RAW rules.

```ros
/ip/firewall/filter
add chain=input action=accept protocol=icmp \
    comment="defconf: accept ICMP after RAW"
add chain=input action=accept \
    connection-state=established,related,untracked \
    comment="defconf: accept established,related,untracked"
add chain=input action=drop in-interface-list=!LAN \
    comment="defconf: drop all not coming from LAN"
```

The IPv6 part accepts, in addition, UDP traceroute, DHCPv6 client prefix delegation and IPsec (IKE, AH, ESP), as the RFC recommendations say.

```ros
/ipv6/firewall/filter
add chain=input action=accept protocol=icmpv6 \
    comment="defconf: accept ICMPv6 after RAW"
add chain=input action=accept \
    connection-state=established,related,untracked \
    comment="defconf: accept established,related,untracked"
add chain=input action=accept protocol=udp dst-port=33434-33534 \
    comment="defconf: accept UDP traceroute"
add chain=input action=accept protocol=udp dst-port=546 \
    src-address=fe80::/10 \
    comment="defconf: accept DHCPv6-Client prefix delegation"
add chain=input action=accept protocol=udp dst-port=500,4500 \
    comment="defconf: accept IKE"
add chain=input action=accept protocol=ipsec-ah \
    comment="defconf: accept IPSec AH"
add chain=input action=accept protocol=ipsec-esp \
    comment="defconf: accept IPSec ESP"
add chain=input action=drop in-interface-list=!LAN \
    comment="defconf: drop all not coming from LAN"
```

:::warning
In setups where a DHCPv6 relay is used, the source address of the packets may not be from the link-local range. In that case, remove the `src-address` parameter of the DHCPv6 rule or change it to the address of the relay.
:::

## Protect the clients

Before you add the forward rules, create an address list with the IPv4 addresses that must not be forwarded.

The multicast address range is in this list. Multicast is not forwarded in most networks, so this entry blocks it. If your network needs multicast forwarding, disable this address list entry.

```ros
/ip/firewall/address-list
add list=no_forward_ipv4 address=0.0.0.0/8 comment="defconf: RFC6890"
add list=no_forward_ipv4 address=169.254.0.0/16 \
    comment="defconf: RFC6890"
add list=no_forward_ipv4 address=224.0.0.0/4 \
    comment="defconf: multicast"
add list=no_forward_ipv4 address=255.255.255.255/32 \
    comment="defconf: RFC6890"
```

For IPv6, the same applies: if multicast forwarding is needed, disable the multicast entry.

```ros
/ipv6/firewall/address-list
add list=no_forward_ipv6 address=fe80::/10 \
    comment="defconf: RFC6890 Link-Scoped Unicast"
add list=no_forward_ipv6 address=ff00::/8 comment="defconf: multicast"
```

The forward chain does the following:

- FastTracks established and related connections.
- Accepts established, related and untracked connections.
- Drops packets with the invalid connection state.
- Drops new connections from the WAN that are not destination NATed.
- Drops the addresses that must not be forwarded.

The rule that drops new connections from the WAN protects the clients from direct access if somebody on the WAN side knows the LAN network. The RAW rules of this example already drop these packets. The filter rule is one more layer of security in case the RAW rules are changed by mistake.

```ros
/ip/firewall/filter
add chain=forward action=accept ipsec-policy=in,ipsec disabled=yes \
    comment="defconf: accept all that matches IPSec policy"
add chain=forward action=fasttrack-connection \
    connection-state=established,related comment="defconf: fasttrack"
add chain=forward action=accept \
    connection-state=established,related,untracked \
    comment="defconf: accept established,related,untracked"
add chain=forward action=drop connection-state=invalid \
    comment="defconf: drop invalid"
add chain=forward action=drop connection-state=new \
    connection-nat-state=!dstnat in-interface-list=WAN \
    comment="defconf: drop all from WAN not DSTNATed"
add chain=forward action=drop src-address-list=no_forward_ipv4 \
    comment="defconf: drop bad forward IPs"
add chain=forward action=drop dst-address-list=no_forward_ipv4 \
    comment="defconf: drop bad forward IPs"
```

The IPv6 forward chain is similar. It also accepts IPsec and HIP, as the RFC recommendations say, and it drops ICMPv6 packets with a hop limit of 1. IPv6 has no NAT in this example, so the last rule drops everything that does not come from the LAN.

```ros
/ipv6/firewall/filter
add chain=forward action=accept \
    connection-state=established,related,untracked \
    comment="defconf: accept established,related,untracked"
add chain=forward action=drop connection-state=invalid \
    comment="defconf: drop invalid"
add chain=forward action=drop src-address-list=no_forward_ipv6 \
    comment="defconf: drop bad forward IPs"
add chain=forward action=drop dst-address-list=no_forward_ipv6 \
    comment="defconf: drop bad forward IPs"
add chain=forward action=drop protocol=icmpv6 hop-limit=equal:1 \
    comment="defconf: rfc4890 drop hop-limit=1"
add chain=forward action=accept protocol=icmpv6 \
    comment="defconf: accept ICMPv6 after RAW"
add chain=forward action=accept protocol=139 \
    comment="defconf: accept HIP"
add chain=forward action=accept protocol=udp dst-port=500,4500 \
    comment="defconf: accept IKE"
add chain=forward action=accept protocol=ipsec-ah \
    comment="defconf: accept AH"
add chain=forward action=accept protocol=ipsec-esp \
    comment="defconf: accept ESP"
add chain=forward action=accept ipsec-policy=in,ipsec \
    comment="defconf: accept all that matches IPSec policy"
add chain=forward action=drop in-interface-list=!LAN \
    comment="defconf: drop everything else not coming from LAN"
```

Note the IPsec policy matcher rule of the IPv4 forward chain. IPsec traffic must not be FastTracked. For this reason, a disabled rule that accepts the traffic that matches an IPsec policy is placed before the FastTrack rule. Enable this rule when the router uses IPsec tunnels. The IPv6 rules of this example do not use FastTrack, so they do not need this.

Another way to keep IPsec traffic out of FastTrack is a RAW rule, see [IPsec](../../virtual-private-networks/ipsec).

## Masquerade the local network

The devices of the local network need source NAT to reach the Internet. The example uses `masquerade`, which works with a WAN address that changes. See [NAT](../firewall/nat) for the difference between `masquerade` and `src-nat`.

```ros
/ip/firewall/nat
add chain=srcnat action=accept ipsec-policy=out,ipsec disabled=yes \
    comment="defconf: accept all that matches IPSec policy"
add chain=srcnat action=masquerade out-interface-list=WAN \
    comment="defconf: masquerade"
```

The disabled policy matcher rule has the same purpose as in the filter rules. IPsec traffic must be excluded from NAT, except when the IPsec policy is configured to match the NATed address. Enable this rule when the router uses IPsec tunnels.

## RAW filtering

### IPv4 address lists

The RAW rules need several address lists. RFC 6890 is the reference.

The first list has the IPv4 addresses that cannot be used as a source or destination address at all. A packet with such an address is dropped.

```ros
/ip/firewall/address-list
add list=bad_ipv4 address=127.0.0.0/8 comment="defconf: RFC6890"
add list=bad_ipv4 address=192.0.0.0/24 comment="defconf: RFC6890"
add list=bad_ipv4 address=192.0.2.0/24 \
    comment="defconf: RFC6890 documentation"
add list=bad_ipv4 address=198.51.100.0/24 \
    comment="defconf: RFC6890 documentation"
add list=bad_ipv4 address=203.0.113.0/24 \
    comment="defconf: RFC6890 documentation"
add list=bad_ipv4 address=240.0.0.0/4 \
    comment="defconf: RFC6890 reserved"
```

The second list has the IPv4 addresses that are not routed globally.

```ros
/ip/firewall/address-list
add list=not_global_ipv4 address=0.0.0.0/8 comment="defconf: RFC6890"
add list=not_global_ipv4 address=10.0.0.0/8 comment="defconf: RFC6890"
add list=not_global_ipv4 address=100.64.0.0/10 \
    comment="defconf: RFC6890"
add list=not_global_ipv4 address=169.254.0.0/16 \
    comment="defconf: RFC6890"
add list=not_global_ipv4 address=172.16.0.0/12 \
    comment="defconf: RFC6890"
add list=not_global_ipv4 address=192.0.0.0/29 \
    comment="defconf: RFC6890"
add list=not_global_ipv4 address=192.168.0.0/16 \
    comment="defconf: RFC6890"
add list=not_global_ipv4 address=198.18.0.0/15 \
    comment="defconf: RFC6890 benchmark"
add list=not_global_ipv4 address=255.255.255.255/32 \
    comment="defconf: RFC6890"
```

The last two lists have the addresses that cannot be used as a source address (`bad_src_ipv4`) and the addresses that cannot be used as a destination address (`bad_dst_ipv4`).

```ros
/ip/firewall/address-list
add list=bad_src_ipv4 address=224.0.0.0/4 comment="defconf: multicast"
add list=bad_src_ipv4 address=255.255.255.255/32 \
    comment="defconf: RFC6890"
add list=bad_dst_ipv4 address=0.0.0.0/8 comment="defconf: RFC6890"
add list=bad_dst_ipv4 address=224.0.0.0/4 comment="defconf: RFC6890"
```

:::warning
The `bad_dst_ipv4` list contains the multicast range, so the RAW rules drop all packets with a multicast destination, also the ones that are sent to the router itself. If the router runs a service that receives multicast, for example OSPF, VRRP, IGMP proxy, UPnP or mDNS, or if the network needs multicast forwarding, disable this entry or accept the packets of the service before the drop rule.
:::

### IPv4 RAW rules

The IPv4 RAW rules do the following:

- A disabled accept rule at the start, with the comment "enable for transparent firewall". Enable it to switch the RAW filtering off without disabling all RAW rules.
- Accept DHCP discover packets. Most DHCP packets are not seen by the IP firewall, but some of them are, so make sure that they are accepted.
- Drop packets with bogon addresses.
- Drop packets with invalid source and destination addresses.
- Drop packets from the WAN with a source address that is not globally routable.
- Drop packets from the WAN that are sent to the 192.168.88.0/24 network. This protects the clients if somebody on the WAN side knows the internal network.
- Drop packets from the LAN with a source address that is not in 192.168.88.0/24.
- Drop bad ICMP, UDP and TCP.
- Accept everything else that comes from the WAN and the LAN.
- Accept local traffic between the interfaces of the router.
- Drop everything else, so that an interface that is added later (for example, a PPPoE connection to the service provider) and is not in a list is protected.

:::warning
If the WAN network of the router uses private addresses, for example behind another router that does NAT or with an ISP that uses carrier-grade NAT (100.64.0.0/10), the rule "drop non global from WAN" drops all packets that come from the addresses of that network, for example the DNS replies of the upstream router. Disable the rule in such a network, or remove the range of the WAN network from the `not_global_ipv4` list.
:::

```ros
/ip/firewall/raw
add chain=prerouting action=accept disabled=yes \
    comment="defconf: enable for transparent firewall"
add chain=prerouting action=accept protocol=udp \
    src-address=0.0.0.0 src-port=68 \
    dst-address=255.255.255.255 dst-port=67 in-interface-list=LAN \
    comment="defconf: accept DHCP discover"
add chain=prerouting action=drop src-address-list=bad_ipv4 \
    comment="defconf: drop bogon IP's"
add chain=prerouting action=drop dst-address-list=bad_ipv4 \
    comment="defconf: drop bogon IP's"
add chain=prerouting action=drop src-address-list=bad_src_ipv4 \
    comment="defconf: drop bogon IP's"
add chain=prerouting action=drop dst-address-list=bad_dst_ipv4 \
    comment="defconf: drop bogon IP's"
add chain=prerouting action=drop src-address-list=not_global_ipv4 \
    in-interface-list=WAN comment="defconf: drop non global from WAN"
add chain=prerouting action=drop in-interface-list=WAN \
    dst-address=192.168.88.0/24 \
    comment="defconf: drop forward to local lan from WAN"
add chain=prerouting action=drop in-interface-list=LAN \
    src-address=!192.168.88.0/24 \
    comment="defconf: drop local if not from default IP range"
add chain=prerouting action=drop protocol=udp port=0 \
    comment="defconf: drop bad UDP"
add chain=prerouting action=jump jump-target=icmp4 protocol=icmp \
    comment="defconf: jump to ICMP chain"
add chain=prerouting action=jump jump-target=bad_tcp protocol=tcp \
    comment="defconf: jump to TCP chain"
add chain=prerouting action=accept in-interface-list=LAN \
    comment="defconf: accept everything else from LAN"
add chain=prerouting action=accept in-interface-list=WAN \
    comment="defconf: accept everything else from WAN"
add chain=prerouting action=accept src-address-type=local \
    comment="defconf: accept local traffic between router interfaces"
add chain=prerouting action=drop comment="defconf: drop the rest"
```

The rules use two more chains. The `bad_tcp` chain drops TCP packets that are known to be invalid:

```ros
/ip/firewall/raw
add chain=bad_tcp action=drop protocol=tcp \
    tcp-flags=!fin,!syn,!rst,!ack comment="defconf: TCP flag filter"
add chain=bad_tcp action=drop protocol=tcp tcp-flags=fin,syn \
    comment=defconf
add chain=bad_tcp action=drop protocol=tcp tcp-flags=fin,rst \
    comment=defconf
add chain=bad_tcp action=drop protocol=tcp tcp-flags=fin,!ack \
    comment=defconf
add chain=bad_tcp action=drop protocol=tcp tcp-flags=fin,urg \
    comment=defconf
add chain=bad_tcp action=drop protocol=tcp tcp-flags=syn,rst \
    comment=defconf
add chain=bad_tcp action=drop protocol=tcp tcp-flags=rst,urg \
    comment=defconf
add chain=bad_tcp action=drop protocol=tcp port=0 \
    comment="defconf: TCP port 0 drop"
```

The `icmp4` chain accepts only the listed ICMP types and limits the echo requests and echo replies. Such strict ICMP filtering is for a very strict firewall. In most cases it is not necessary, and it adds load to the CPU of the router.

```ros
/ip/firewall/raw
add chain=icmp4 action=accept protocol=icmp icmp-options=0:0 \
    limit=5,10:packet comment="defconf: echo reply"
add chain=icmp4 action=accept protocol=icmp icmp-options=3:0 \
    comment="defconf: net unreachable"
add chain=icmp4 action=accept protocol=icmp icmp-options=3:1 \
    comment="defconf: host unreachable"
add chain=icmp4 action=accept protocol=icmp icmp-options=3:2 \
    comment="defconf: protocol unreachable"
add chain=icmp4 action=accept protocol=icmp icmp-options=3:3 \
    comment="defconf: port unreachable"
add chain=icmp4 action=accept protocol=icmp icmp-options=3:4 \
    comment="defconf: fragmentation needed"
add chain=icmp4 action=accept protocol=icmp icmp-options=8:0 \
    limit=5,10:packet comment="defconf: echo"
add chain=icmp4 action=accept protocol=icmp icmp-options=11:0-255 \
    comment="defconf: time exceeded"
add chain=icmp4 action=drop protocol=icmp \
    comment="defconf: drop other icmp"
```

### IPv6 address lists

The IPv6 addresses that are dropped at once:

```ros
/ipv6/firewall/address-list
add list=bad_ipv6 address=::1/128 comment="defconf: RFC6890 lo"
add list=bad_ipv6 address=::ffff:0:0/96 \
    comment="defconf: RFC6890 IPv4 mapped"
add list=bad_ipv6 address=2001::/23 comment="defconf: RFC6890"
add list=bad_ipv6 address=2001:db8::/32 \
    comment="defconf: RFC6890 documentation"
add list=bad_ipv6 address=2001:10::/28 comment="defconf: RFC6890 orchid"
add list=bad_ipv6 address=::/96 comment="defconf: ipv4 compat"
```

The IPv6 addresses that are not globally routable:

```ros
/ipv6/firewall/address-list
add list=not_global_ipv6 address=100::/64 \
    comment="defconf: RFC6890 Discard-only"
add list=not_global_ipv6 address=2001::/32 \
    comment="defconf: RFC6890 TEREDO"
add list=not_global_ipv6 address=2001:2::/48 \
    comment="defconf: RFC6890 Benchmark"
add list=not_global_ipv6 address=fc00::/7 \
    comment="defconf: RFC6890 Unique-Local"
```

The addresses that are invalid as a destination address and as a source address:

```ros
/ipv6/firewall/address-list
add list=bad_dst_ipv6 address=::/128 comment="defconf: unspecified"
add list=bad_src_ipv6 address=::/128 comment="defconf: unspecified"
add list=bad_src_ipv6 address=ff00::/8 comment="defconf: multicast"
```

### IPv6 RAW rules

The IPv6 RAW rules do the following:

- A disabled accept rule at the start. Enable it to switch the RAW filtering off without disabling all RAW rules.
- Accept the neighbor solicitation that a host sends from the unspecified address to check that its address is not in use.
- Drop packets with bogon addresses.
- Drop packets with invalid source and destination addresses.
- Drop packets from the WAN with a source address that is not globally routable.
- Drop bad ICMPv6.
- Accept the link-local multicast scope and drop other multicast destinations.
- Accept everything else that comes from the WAN and the LAN.
- Drop everything else, so that an interface that is added later (for example, a PPPoE connection to the service provider) and is not in a list is protected.

```ros
/ipv6/firewall/raw
add chain=prerouting action=accept disabled=yes \
    comment="defconf: enable for transparent firewall"
add chain=prerouting action=accept protocol=icmpv6 \
    icmp-options=135 src-address=::/128 \
    dst-address=ff02:0:0:0:0:1:ff00::/104 \
    comment="defconf: RFC4291, section 2.7.1"
add chain=prerouting action=drop src-address-list=bad_ipv6 \
    comment="defconf: drop bogon IP's"
add chain=prerouting action=drop dst-address-list=bad_ipv6 \
    comment="defconf: drop bogon IP's"
add chain=prerouting action=drop src-address-list=bad_src_ipv6 \
    comment="defconf: drop packets with bad SRC ipv6"
add chain=prerouting action=drop dst-address-list=bad_dst_ipv6 \
    comment="defconf: drop packets with bad dst ipv6"
add chain=prerouting action=drop src-address-list=not_global_ipv6 \
    in-interface-list=WAN comment="defconf: drop non global from WAN"
add chain=prerouting action=jump jump-target=icmp6 protocol=icmpv6 \
    comment="defconf: jump to ICMPv6 chain"
add chain=prerouting action=accept dst-address=ff02::/16 \
    comment="defconf: accept local multicast scope"
add chain=prerouting action=drop dst-address=ff00::/8 \
    comment="defconf: drop other multicast destinations"
add chain=prerouting action=accept in-interface-list=WAN \
    comment="defconf: accept everything else from WAN"
add chain=prerouting action=accept in-interface-list=LAN \
    comment="defconf: accept everything else from LAN"
add chain=prerouting action=drop comment="defconf: drop the rest"
```

The `icmp6` chain is as strict as the `icmp4` chain: in most cases it is not necessary, and it adds load to the CPU of the router. The first rule of the chain drops ICMPv6 packets to link-local addresses with a hop limit other than 255. Operating systems send packets with different default hop limits, so this rule also drops a ping to the link-local address of the router when the sender does not use 255. Neighbor solicitations, neighbor advertisements and router advertisements are accepted on every interface, because the router needs them to reach its neighbors on the WAN side too. Router solicitations and inverse neighbor discovery are accepted only from the LAN.

```ros
/ipv6/firewall/raw
add chain=icmp6 action=drop protocol=icmpv6 dst-address=fe80::/10 \
    hop-limit=not-equal:255 \
    comment="defconf: rfc4890 drop ll if hop-limit!=255"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=1:0-255 \
    comment="defconf: dst unreachable"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=2:0-255 \
    comment="defconf: packet too big"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=3:0-1 \
    comment="defconf: limit exceeded"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=4:0-2 \
    comment="defconf: bad header"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=144:0-255 \
    comment="defconf: Mobile home agent address discovery"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=145:0-255 \
    comment="defconf: Mobile home agent address discovery"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=146:0-255 \
    comment="defconf: Mobile prefix solic"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=147:0-255 \
    comment="defconf: Mobile prefix advert"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=128:0-255 \
    limit=5,10:packet comment="defconf: echo request limit 5,10"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=129:0-255 \
    limit=5,10:packet comment="defconf: echo reply limit 5,10"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=133:0-255 \
    hop-limit=equal:255 in-interface-list=LAN limit=5,10:packet \
    comment="defconf: rfc4890 router solic limit 5,10 only LAN"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=134:0-255 \
    hop-limit=equal:255 limit=5,10:packet \
    comment="defconf: rfc4890 router advert limit 5,10"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=135:0-255 \
    hop-limit=equal:255 limit=5,10:packet \
    comment="defconf: rfc4890 neighbor solic limit 5,10"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=136:0-255 \
    hop-limit=equal:255 limit=5,10:packet \
    comment="defconf: rfc4890 neighbor advert limit 5,10"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=141:0-255 \
    hop-limit=equal:255 in-interface-list=LAN limit=5,10:packet \
    comment="defconf: rfc4890 inverse ND solic limit 5,10 only LAN"
add chain=icmp6 action=accept protocol=icmpv6 icmp-options=142:0-255 \
    hop-limit=equal:255 in-interface-list=LAN limit=5,10:packet \
    comment="defconf: rfc4890 inverse ND advert limit 5,10 only LAN"
add chain=icmp6 action=drop protocol=icmpv6 \
    comment="defconf: drop other icmp"
```

## Check the firewall

The counters of the drop rules show what the firewall stops. In this output, a host on the WAN side has sent packets with a private source address to the router, and packets to an address of the LAN network:

```ros
[admin@MikroTik] > /ip/firewall/raw/print stats where action=drop and packets>0
Columns: CHAIN, ACTION, BYTES, PACKETS
# CHAIN       ACTION  BYTES  PACKETS
;;; defconf: drop non global from WAN
0 prerouting  drop      168        3
;;; defconf: drop forward to local lan from WAN
1 prerouting  drop      168        3
```

`/ip/firewall/filter/print stats`, `/ipv6/firewall/raw/print stats` and `/ipv6/firewall/filter/print stats` show the counters of the other tables. Check also that a LAN device reaches the Internet, and that the router does not answer a connection to its management ports from the WAN side.

If the RAW rules stop traffic that you need, enable the first RAW rule. It accepts every packet, so the other RAW rules are not used, and the filter rules still protect the router and the clients. The IPv6 RAW table has its own rule with the same comment.

```ros
/ip/firewall/raw
enable [find comment="defconf: enable for transparent firewall"]
```

What the rules mean for normal traffic:

- The echo rules of the `icmp4` and `icmp6` chains limit all echo requests and all echo replies that the router receives, also the forwarded ones, to 5 packets per second with a burst of 10. A ping with a short interval, or pings from several devices at the same time, lose packets. The limit is shared by all senders, also by the pings that the router sends itself, for example to check a gateway.
- IPv6 hosts in the LAN answer pings from the WAN side, because the forward chain accepts ICMPv6. It also accepts IKE, AH, ESP and HIP to the LAN hosts. Other new connections from the WAN side to the LAN hosts are dropped.
