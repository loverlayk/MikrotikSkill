# Firewall and routing for IPsec

> Firewall and routing for IPsec in RouterOS: allow IKE and ESP, accept only traffic that came through IPsec, drop unencrypted traffic with a policy, and make a tunnel use a certain WAN link or public address.

# Firewall and routing for IPsec

This page has the firewall rules that IPsec needs, the ways to accept only encrypted traffic, and what to do when a router has several WAN links or several public addresses.

## Allow IKE and ESP

IPsec uses these packets between the two routers:

- UDP port 500 for IKE.
- UDP port 4500 for IKE and the encrypted traffic when there is NAT between the two sides (NAT traversal).
- IP protocol 50 (ESP) for the encrypted traffic without NAT, or protocol 51 (AH).

The default firewall drops them when they come from the internet. Accept them before the default drop rule:

```ros
/ip/firewall/filter
add chain=input action=accept protocol=udp dst-port=500,4500 \
    in-interface-list=WAN comment="accept IKE" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
add chain=input action=accept protocol=ipsec-esp \
    in-interface-list=WAN comment="accept IPsec ESP" \
    place-before=[find comment="defconf: drop all not coming from LAN"]
```

For a tunnel to one known router, add `src-address` with its address to both rules.

## Accept only traffic that came through IPsec

Sometimes a service must be reachable only through IPsec. For example, an L2TP server with IPsec must not accept L2TP connections without encryption. There are three ways:

- The IPsec policy matcher of the firewall.
- An IPsec policy with the action `discard` below the dynamic policies. This suits road warrior setups, where the policies are made dynamically.
- A DSCP value or a priority that is set in mangle before encryption and matched in the firewall after decryption.

### IPsec policy matcher

The matcher `ipsec-policy` has a direction and a policy: `in,ipsec` matches packets that arrived through IPsec and were decrypted, and `in,none` matches packets that did not. The firewall sees the packet after decryption, so the other matchers apply to the inner packet.

These rules accept everything that arrived through IPsec and drop the rest:

```ros
/ip/firewall/filter
add chain=input action=accept in-interface-list=WAN \
    ipsec-policy=in,ipsec comment="accept IPsec traffic"
add chain=input action=drop in-interface-list=WAN log=yes \
    comment="drop all"
```

Put the rules for IKE and ESP before these rules, or the tunnel cannot be made. With the default firewall, add the accept rule with `place-before=[find comment="defconf: drop all not coming from LAN"]`; the drop rule of the default configuration then does the dropping.

To accept only GRE packets from one address through IPsec, and drop the rest:

```ros
/ip/firewall/filter
add chain=input action=accept in-interface-list=WAN \
    ipsec-policy=in,ipsec protocol=gre src-address=192.168.33.1
add chain=input action=drop in-interface-list=WAN log=yes \
    comment="drop all"
```

For an L2TP server, `use-ipsec=required` of the server does this without firewall rules: see [L2TP](../l2tp/). With firewall rules, to accept L2TP only through IPsec:

```ros
/ip/firewall/filter
add chain=input action=accept in-interface-list=WAN \
    ipsec-policy=in,ipsec protocol=udp dst-port=1701 \
    comment="accept L2TP over IPsec"
add chain=input action=drop in-interface-list=WAN protocol=udp \
    dst-port=1701 log=yes comment="drop L2TP without IPsec"
```

The default configuration has the same matcher in the `forward` chain: its rules accept forwarded traffic that comes out of or goes into an IPsec tunnel.

### Discard policy

A policy with `action=discard` drops the packets that match it. Dynamic policies are above it and have priority, so traffic of a connected client is encrypted, and the same kind of traffic without a tunnel is dropped. This example is for an L2TP server with IPsec on the public address 203.0.113.1. The router then drops L2TP traffic that is not encrypted:

```ros
/ip/ipsec/policy/add src-address=203.0.113.1 dst-address=0.0.0.0/0 \
    sa-src-address=203.0.113.1 protocol=udp src-port=1701 \
    tunnel=yes action=discard
```

:::warning
The order of the policies is important. The discard policy must be below the dynamic policies: move it below the policy template if necessary.
:::

When a client is connected, its dynamic policy is above the discard policy. This output is from a server with the address 1.1.1.1:

```ros
[admin@rack2_10g1] /ip/ipsec/policy> print
Flags: T - template, X - disabled, D - dynamic, I - inactive, * - default
0 T * group=default src-address=::/0 dst-address=::/0 protocol=all
proposal=default template=yes

1 D src-address=1.1.1.1/32 src-port=1701 dst-address=10.5.130.71/32
dst-port=any protocol=udp action=encrypt level=require
ipsec-protocols=esp tunnel=no sa-src-address=1.1.1.1
sa-dst-address=10.5.130.71

2 src-address=1.1.1.1/32 src-port=1701 dst-address=0.0.0.0/0
dst-port=any protocol=udp action=discard level=unique
ipsec-protocols=esp tunnel=yes sa-src-address=1.1.1.1
sa-dst-address=0.0.0.0 proposal=default manual-sa=none
```

## Use a certain WAN link or address

`local-address` of a peer sets the source address of the tunnel. It does not select the route: IPsec, as other services of the router, uses the main routing table. On a router with several WAN links or several addresses, more configuration is needed. Without it the log shows `phase1 negotiation failed due to time up`.

### Another routing table

In this example the router has two default routes, one in the main table and one in the table `backup`, and the tunnel must use the backup link:

```ros
[admin@pair_r1] > /ip/route/print detail 
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, U - unreachable, P - prohibit 
0 A S dst-address=0.0.0.0/0 gateway=10.155.107.1 gateway-status=10.155.107.1 reachable via ether1 distance=1 scope=30 target-scope=10 routing-mark=backup 

1 A S dst-address=0.0.0.0/0 gateway=172.22.2.115 gateway-status=172.22.2.115 reachable via ether2 distance=1 scope=30 target-scope=10 

2 ADC dst-address=10.155.107.0/25 pref-src=10.155.107.8 gateway=ether1 gateway-status=ether1 reachable distance=0 scope=10 

3 ADC dst-address=172.22.2.0/24 pref-src=172.22.2.114 gateway=ether2 gateway-status=ether2 reachable distance=0 scope=10 

4 ADC dst-address=192.168.1.0/24 pref-src=192.168.1.1 gateway=bridge-local gateway-status=ether2 reachable distance=0 scope=10 

[admin@pair_r1] > /ip/firewall/nat/print 
Flags: X - disabled, I - invalid, D - dynamic 
0 chain=srcnat action=masquerade out-interface=ether1 log=no log-prefix="" 

1 chain=srcnat action=masquerade out-interface=ether2 log=no log-prefix="" 
```

The peer, the policy and the NAT bypass rule use the address of the backup link:

```ros
/ip/ipsec/peer/add name=site2 address=10.155.130.136/32 \
    local-address=10.155.107.8
/ip/ipsec/identity/add peer=site2 secret=Example-psk-1
/ip/ipsec/policy/add peer=site2 tunnel=yes \
    src-address=192.168.1.0/24 dst-address=172.16.0.0/24
/ip/firewall/nat/add chain=srcnat action=accept place-before=0 \
    src-address=192.168.1.0/24 dst-address=172.16.0.0/24
```

The router still sends the IKE packets through the main table, with a source address that does not fit the link. Mark the IKE and ESP packets to the peer with mangle rules, so that they use the table `backup`:

```ros
/ip/firewall/mangle
add chain=output action=mark-connection connection-mark=no-mark \
    dst-address=10.155.130.136 protocol=udp dst-port=500,4500 \
    new-connection-mark=ipsec passthrough=yes
add chain=output action=mark-connection connection-mark=no-mark \
    dst-address=10.155.130.136 protocol=ipsec-esp \
    new-connection-mark=ipsec passthrough=yes
add chain=output action=mark-routing connection-mark=ipsec \
    new-routing-mark=backup passthrough=no
```

### Several addresses on one interface

In this example the public interface has several addresses of one network, and a masquerade rule for the interface. The tunnel must use one of the addresses:

```ros
[admin@pair_r1] > /ip/address/print 
Flags: X - disabled, I - invalid, D - dynamic 
# ADDRESS NETWORK INTERFACE
0 192.168.1.1/24 192.168.1.0 bridge-local
1 172.22.2.1/24 172.22.2.0 ether1
2 172.22.2.2/24 172.22.2.0 ether1
3 172.22.2.3/24 172.22.2.0 ether1

[admin@pair_r1] > /ip/route/print 
Flags: X - disabled, A - active, D - dynamic, C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, B - blackhole, U - unreachable, P - prohibit 
# DST-ADDRESS PREF-SRC GATEWAY DISTANCE
1 A S 0.0.0.0/0 172.22.2.115 1
3 ADC 172.22.2.0/24 172.22.2.1 ether1 0
4 ADC 192.168.1.0/24 192.168.1.1 bridge-local 0

[admin@pair_r1] /ip/firewall/nat> print 
Flags: X - disabled, I - invalid, D - dynamic 
0 chain=srcnat action=masquerade out-interface=ether1 log=no log-prefix="" 
```

The peer and the policy use that address:

```ros
/ip/ipsec/peer/add name=site2 address=10.155.130.136/32 \
    local-address=172.22.2.3
/ip/ipsec/identity/add peer=site2 secret=Example-psk-1
/ip/ipsec/policy/add peer=site2 tunnel=yes \
    src-address=192.168.1.0/24 dst-address=172.16.0.0/24
/ip/firewall/nat/add chain=srcnat action=accept place-before=0 \
    src-address=192.168.1.0/24 dst-address=172.16.0.0/24
```

The masquerade rule changes the source address of the IKE connection to the preferred source address of the connected route, which is another address than the one in `local-address`. Leave the IKE packets out of masquerade:

```ros
/ip/firewall/nat/add chain=srcnat action=accept protocol=udp \
    src-port=500,4500 place-before=0
```

:::note
The route and address outputs of this section are in an older print format.
:::

## Read more

- [IPsec](./): how IKE works, the menus, the algorithms
- [Site-to-site tunnel](site-to-site): NAT bypass and FastTrack
- [Filter](../../firewall-and-quality-of-service/firewall/filter)
- [Troubleshooting](troubleshooting)
