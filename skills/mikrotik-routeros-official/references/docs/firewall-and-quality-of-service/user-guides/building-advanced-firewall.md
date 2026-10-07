# Building Advanced Firewall

> This page guides building an advanced firewall on MikroTik RouterOS by configuring interface lists, filtering rules for IPv4 and IPv6, accepting ICMP/DHCPv6 while blocking invalid addresses, and managing traffic...

# Building Advanced Firewall

Building on everything we have covered so far, let's now construct an advanced firewall. In this example, we will implement as many firewall features as possible to demonstrate how they work and when they should be used correctly.

Most of the filtering will be handled in the RAW firewall. A standard firewall configuration typically includes only a basic rule set that accepts established, related, and untracked connections while dropping everything else that does not originate from the LAN interface, thereby providing full protection for the router.

### Interface Lists

Two interface lists are defined: **WAN** and **LAN**. These lists simplify future management by grouping interfaces based on their network role. The WAN list contains interfaces connected to the global internet, such as *ether1* in this configuration. The LAN list contains local network interfaces, such as the bridge interface.

```ros
/interface/list
  add comment=defconf name=WAN
  add comment=defconf name=LAN
/interface/list/member
  add comment=defconf interface=bridge list=LAN
  add comment=defconf interface=ether1 list=WAN
```

This configuration assigns the bridge interface to the LAN list and ether1 to the WAN list, enabling consistent firewall rule application across these interface groups.

### Protect the Device

The main goal here is to allow access to the router only from LAN and drop everything else.

Notice that ICMP is accepted here as well; it is used to accept ICMP packets that passed RAW rules.

```ros
/ip/firewall/filter
  add action=accept chain=input comment="defconf: accept ICMP after RAW" protocol=icmp
  add action=accept chain=input comment="defconf: accept established,related,untracked" connection-state=established,related,untracked
  add action=drop chain=input comment="defconf: drop all not coming from LAN" in-interface-list=!LAN
```

The IPv6 part is a bit more complicated, in addition, UDP traceroute, DHCPv6 client PD, and IPSec (IKE, AH, ESP) are accepted as per RFC recommendations.

```ros
/ipv6/firewall/filter
add action=accept chain=input comment="defconf: accept ICMPv6 after RAW" protocol=icmpv6
add action=accept chain=input comment="defconf: accept established,related,untracked" connection-state=established,related,untracked
add action=accept chain=input comment="defconf: accept UDP traceroute" dst-port=33434-33534 protocol=udp 
add action=accept chain=input comment="defconf: accept DHCPv6-Client prefix delegation." dst-port=546 protocol=udp src-address=fe80::/10
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 protocol=udp
add action=accept chain=input comment="defconf: accept IPSec AH" protocol=ipsec-ah
add action=accept chain=input comment="defconf: accept IPSec ESP" protocol=ipsec-esp
add action=drop chain=input comment="defconf: drop all not coming from LAN" in-interface-list=!LAN
```

:::warning
In certain setups where the DHCPv6 relay is used, the src address of the packets may not be from the link-local range. In that case, the src-address parameter of rule #4 must be removed or adjusted to accept the relay address.
:::

### Protect the Clients

Before configuring the firewall rules set, create an address list containing all IPv4 and IPv6 addresses that should not be forwarded. This list prevents routing of invalid or reserved addresses through your network.

Note that a multicast address range is included in this list. Since multicast is not typically used in most networks, this entry blocks multicast traffic by default. If your network requires multicast forwarding, disable this address list entry.

```ros
/ip/firewall/address-list
  add address=0.0.0.0/8 comment="defconf: RFC6890" list=no_forward_ipv4
  add address=169.254.0.0/16 comment="defconf: RFC6890" list=no_forward_ipv4
  add address=224.0.0.0/4 comment="defconf: multicast" list=no_forward_ipv4
  add address=255.255.255.255/32 comment="defconf: RFC6890" list=no_forward_ipv4
```

For IPv6, apply the same principle: if multicast forwarding is required, disable the multicast entry in the address list.

```ros
/ipv6/firewall/address-list
  add address=fe80::/10  comment="defconf: RFC6890 Link-Scoped Unicast" list=no_forward_ipv6
  add address=ff00::/8  comment="defconf: multicast" list=no_forward_ipv6
```

The Forward chain contains more rules than the Input chain and performs the following actions:

- Accept established, related, and untracked connections
- FastTrack established and related connections (IPv4 only)
- Drop invalid connections states
- Drop bad forward IP addresses that should not be routed
- Drop connections attempts initiated from the internet (WAN side) that are not destination NATed
- Drop bogon IP addresses that should not be forwarded

This configuration drops all non-destination-NATed IPv4 packets to protect clients devices from direct attacks if an external attacker knows your internal LAN network range. While this rule is typically unnecessary because RAW filtering already drops these packets, it provides an additional layer of security in case the RAW rules configuration is accidentally modified.

```ros
/ip/firewall/filter
  add action=accept chain=forward comment="defconf: accept all that matches IPSec policy" ipsec-policy=in,ipsec disabled=yes
  add action=fasttrack-connection chain=forward comment="defconf: fasttrack" connection-state=established,related
  add action=accept chain=forward comment="defconf: accept established,related, untracked" connection-state=established,related,untracked
  add action=drop chain=forward comment="defconf: drop invalid" connection-state=invalid
  add action=drop chain=forward comment="defconf:  drop all from WAN not DSTNATed" connection-nat-state=!dstnat connection-state=new in-interface-list=WAN
  add action=drop chain=forward src-address-list=no_forward_ipv4 comment="defconf: drop bad forward IPs"
  add action=drop chain=forward dst-address-list=no_forward_ipv4 comment="defconf: drop bad forward IPs"
```

The IPv6 Forward chain follows a similar structure, with additional rules to accept IPsec and HIP protocols as recommended by RFC standards. ICMPv6 packets with a hop-limit of 1 are dropped.

```ros
/ipv6/firewall/filter
add action=accept chain=forward comment="defconf: accept established,related,untracked" connection-state=established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" connection-state=invalid
add action=drop chain=forward src-address-list=no_forward_ipv6 comment="defconf: drop bad forward IPs"
add action=drop chain=forward dst-address-list=no_forward_ipv6 comment="defconf: drop bad forward IPs"
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6 after RAW" protocol=icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" protocol=udp dst-port=500,4500
add action=accept chain=forward comment="defconf: accept AH" protocol=ipsec-ah
add action=accept chain=forward comment="defconf: accept ESP" protocol=ipsec-esp
add action=accept chain=forward comment="defconf: accept all that matches IPSec policy" ipsec-policy=in,ipsec
add action=drop chain=forward comment="defconf: drop everything else not coming from LAN" in-interface-list=!LAN
```

Note the IPsec policy matcher rule. It is critical that IPsec encapsulated traffic bypasses the FastTrack connection feature. For this reason, a disabled rule is included to accept traffic matching IPsec policies. Enable this rule whenever IPsec tunnels are used on the router. IPv6 does not require this consideration since it does not support FastTrack.

An alternative method to handle IPsec traffic is to add a RAW rule, which will be covered in the RAW section of this documentation.

### Masquerade Local Network

For local devices behind the router to be able to access the internet, local networks must be masqueraded. In most cases, it is advised to use src-nat instead of masquerade, however, in this case when the WAN address is dynamic it is the only option.

```ros
/ip/firewall/nat
  add action=accept chain=srcnat comment="defconf: accept all that matches IPSec policy" ipsec-policy=out,ipsec disabled=yes
  add action=masquerade chain=srcnat comment="defconf: masquerade" out-interface-list=WAN
```

Notice the disabled policy matcher rule, the same as in firewall filters, IPSec traffic must be excluded from being NATed (except in specific scenarios where IPsec policy is configured to match NATed address). So whenever IPsec tunnels are used on the router, this rule must be enabled.

## RAW Filtering

### IPv4 Address Lists

Before setting RAW rules, let's create some address lists necessary for our filtering policy. RFC 6890 will be used as a reference.

First, *address-list* contains all IPv4 addresses that cannot be used as src/dst/forwarded, etc. (will be dropped immediately if such an address is seen)

```ros
/ip/firewall/address-list
  add address=127.0.0.0/8 comment="defconf: RFC6890" list=bad_ipv4
  add address=192.0.0.0/24 comment="defconf: RFC6890" list=bad_ipv4
  add address=192.0.2.0/24 comment="defconf: RFC6890 documentation" list=bad_ipv4
  add address=198.51.100.0/24 comment="defconf: RFC6890 documentation" list=bad_ipv4
  add address=203.0.113.0/24 comment="defconf: RFC6890 documentation" list=bad_ipv4
  add address=240.0.0.0/4 comment="defconf: RFC6890 reserved" list=bad_ipv4
```

Another address list contains all IPv4 addresses that cannot be routed globally.

```ros
/ip/firewall/address-list
  add address=0.0.0.0/8 comment="defconf: RFC6890" list=not_global_ipv4
  add address=10.0.0.0/8 comment="defconf: RFC6890" list=not_global_ipv4
  add address=100.64.0.0/10 comment="defconf: RFC6890" list=not_global_ipv4
  add address=169.254.0.0/16 comment="defconf: RFC6890" list=not_global_ipv4
  add address=172.16.0.0/12 comment="defconf: RFC6890" list=not_global_ipv4
  add address=192.0.0.0/29 comment="defconf: RFC6890" list=not_global_ipv4
  add address=192.168.0.0/16 comment="defconf: RFC6890" list=not_global_ipv4
  add address=198.18.0.0/15 comment="defconf: RFC6890 benchmark" list=not_global_ipv4
  add address=255.255.255.255/32 comment="defconf: RFC6890" list=not_global_ipv4
```

And the last two address lists are for addresses that cannot be used as destination or source addresses.

```ros
/ip/firewall/address-list
  add address=224.0.0.0/4 comment="defconf: multicast" list=bad_src_ipv4
  add address=255.255.255.255/32 comment="defconf: RFC6890" list=bad_src_ipv4
  add address=0.0.0.0/8 comment="defconf: RFC6890" list=bad_dst_ipv4
  add address=224.0.0.0/4 comment="defconf: RFC6890" list=bad_dst_ipv4
```

### IPv4 RAW Rules

Raw IPv4 rules will perform the following actions:

- **add disabled "accept" rule** - can be used to quickly disable RAW filtering without disabling all RAW rules.
- **accept** DHCP discovery - most of the DHCP packets are not seen by an IP firewall, but some of them are, so make sure that they are accepted.
- **drop** packets that use bogon IPs.
- **drop** from invalid SRC and DST IPs.
- **drop** globally unroutable IPs coming from WAN.
- **drop** packets with source-address not equal to 192.168.88.0/24 (default IP range) coming from LAN.
- **drop** packets coming from WAN to be forwarded to 192.168.88.0/24 network; this will protect from attacks if the attacker knows the internal network.
- **drop** bad ICMP, UDP, and TCP.
- **accept** everything else coming from WAN and LAN.
- **accept** local traffic between router interfaces.
- **drop** everything else, to make sure that any newly added interface (like PPPoE connection to service provider) is protected against accidental misconfiguration.

```ros
/ip/firewall/raw
add action=accept chain=prerouting comment="defconf: enable for transparent firewall" disabled=yes
add action=accept chain=prerouting comment="defconf: accept DHCP discover" dst-address=255.255.255.255 dst-port=67 in-interface-list=LAN protocol=udp src-address=0.0.0.0 src-port=68
add action=drop chain=prerouting comment="defconf: drop bogon IP's" src-address-list=bad_ipv4
add action=drop chain=prerouting comment="defconf: drop bogon IP's" dst-address-list=bad_ipv4
add action=drop chain=prerouting comment="defconf: drop bogon IP's" src-address-list=bad_src_ipv4
add action=drop chain=prerouting comment="defconf: drop bogon IP's" dst-address-list=bad_dst_ipv4
add action=drop chain=prerouting comment="defconf: drop non global from WAN" src-address-list=not_global_ipv4 in-interface-list=WAN
add action=drop chain=prerouting comment="defconf: drop forward to local lan from WAN" in-interface-list=WAN dst-address=192.168.88.0/24
add action=drop chain=prerouting comment="defconf: drop local if not from default IP range" in-interface-list=LAN src-address=!192.168.88.0/24
add action=drop chain=prerouting comment="defconf: drop bad UDP" port=0 protocol=udp
add action=jump chain=prerouting comment="defconf: jump to ICMP chain" jump-target=icmp4 protocol=icmp
add action=jump chain=prerouting comment="defconf: jump to TCP chain" jump-target=bad_tcp protocol=tcp
add action=accept chain=prerouting comment="defconf: accept everything else from LAN" in-interface-list=LAN
add action=accept chain=prerouting comment="defconf: accept everything else from WAN" in-interface-list=WAN
add action=accept chain=prerouting comment="defconf: accept local traffic between router interfaces" src-address-type=local
add action=drop chain=prerouting comment="defconf: drop the rest"
```

Notice that we used some optional chains, the first **TCP** chain to drop **TCP** packets known to be *invalid.*

```ros
/ip/firewall/raw
add action=drop chain=bad_tcp comment="defconf: TCP flag filter" protocol=tcp tcp-flags=!fin,!syn,!rst,!ack
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=fin,syn
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=fin,rst
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=fin,!ack
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=fin,urg
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=syn,rst
add action=drop chain=bad_tcp comment=defconf protocol=tcp tcp-flags=rst,urg
add action=drop chain=bad_tcp comment="defconf: TCP port 0 drop" port=0 protocol=tcp
```

And another chain for **ICMP**. Note that if you want a very strict firewall then such strict **ICMP** filtering can be used, but in most cases, it is not necessary and simply adds more load on the router's CPU. ICMP rate limit in most cases is also unnecessary since the Linux kernel is already limiting ICMP packets to 100pps.

```ros
/ip/firewall/raw
add action=accept chain=icmp4 comment="defconf: echo reply" icmp-options=0:0 limit=5,10:packet protocol=icmp
add action=accept chain=icmp4 comment="defconf: net unreachable" icmp-options=3:0 protocol=icmp
add action=accept chain=icmp4 comment="defconf: host unreachable" icmp-options=3:1 protocol=icmp
add action=accept chain=icmp4 comment="defconf: protocol unreachable" icmp-options=3:2 protocol=icmp
add action=accept chain=icmp4 comment="defconf: port unreachable" icmp-options=3:3 protocol=icmp
add action=accept chain=icmp4 comment="defconf: fragmentation needed" icmp-options=3:4 protocol=icmp
add action=accept chain=icmp4 comment="defconf: echo" icmp-options=8:0 limit=5,10:packet protocol=icmp
add action=accept chain=icmp4 comment="defconf: time exceeded " icmp-options=11:0-255 protocol=icmp
add action=drop chain=icmp4 comment="defconf: drop other icmp" protocol=icmp
```

### IPv6 Address Lists

#### List of IPv6 addresses that should be dropped instantly

```ros
/ipv6/firewall/address-list
add address=::1/128 comment="defconf: RFC6890 lo" list=bad_ipv6
add address=::ffff:0:0/96 comment="defconf: RFC6890 IPv4 mapped" list=bad_ipv6
add address=2001::/23 comment="defconf: RFC6890" list=bad_ipv6
add address=2001:db8::/32 comment="defconf: RFC6890 documentation" list=bad_ipv6
add address=2001:10::/28 comment="defconf: RFC6890 orchid" list=bad_ipv6
add address=::/96 comment="defconf: ipv4 compat" list=bad_ipv6
```

#### List of IPv6 addresses that are not globally routable

```ros
/ipv6/firewall/address-list
add address=100::/64 comment="defconf: RFC6890 Discard-only" list=not_global_ipv6
add address=2001::/32 comment="defconf: RFC6890 TEREDO" list=not_global_ipv6
add address=2001:2::/48 comment="defconf: RFC6890 Benchmark" list=not_global_ipv6
add address=fc00::/7 comment="defconf: RFC6890 Unique-Local" list=not_global_ipv6
```

#### List of addresses as an invalid destination address

```ros
/ipv6/firewall/address-list/add address=::/128 comment="defconf: unspecified" list=bad_dst_ipv6
```

#### List of addresses as an invalid source address

```ros
/ipv6/firewall/address-list
  add address=::/128 comment="defconf: unspecified" list=bad_src_ipv6
  add address=ff00::/8  comment="defconf: multicast" list=bad_src_ipv6
```

### IPv6 RAW Rules

Raw IPv6 rules will perform the following actions:

- **Add a disabled accept rule** - can be used to quickly disable RAW filtering without disabling all RAW rules.
- **Drop** packets that use bogon IPs.
- **Drop** from invalid SRC and DST IPs.
- **Drop** globally unroutable IPs coming from WAN.
- **Drop** bad ICMP.
- **Accept** everything else coming from WAN and LAN.
- **Drop** everything else, to make sure that any newly added interface (like PPPoE connection to service provider) is protected against accidental misconfiguration.

```ros
/ipv6/firewall/raw
add action=accept chain=prerouting comment="defconf: enable for transparent firewall" disabled=yes
add action=accept chain=prerouting comment="defconf: RFC4291, section 2.7.1" src-address=::/128 dst-address=ff02:0:0:0:0:1:ff00::/104 icmp-options=135 protocol=icmpv6
add action=drop chain=prerouting comment="defconf: drop bogon IP's" src-address-list=bad_ipv6
add action=drop chain=prerouting comment="defconf: drop bogon IP's" dst-address-list=bad_ipv6
add action=drop chain=prerouting comment="defconf: drop packets with bad SRC ipv6" src-address-list=bad_src_ipv6
add action=drop chain=prerouting comment="defconf: drop packets with bad dst ipv6" dst-address-list=bad_dst_ipv6
add action=drop chain=prerouting comment="defconf: drop non global from WAN" src-address-list=not_global_ipv6 in-interface-list=WAN
add action=jump chain=prerouting comment="defconf: jump to ICMPv6 chain" jump-target=icmp6 protocol=icmpv6
add action=accept chain=prerouting comment="defconf: accept local multicast scope" dst-address=ff02::/16
add action=drop chain=prerouting comment="defconf: drop other multicast destinations" dst-address=ff00::/8
add action=accept chain=prerouting comment="defconf: accept everything else from WAN" in-interface-list=WAN
add action=accept chain=prerouting comment="defconf: accept everything else from LAN" in-interface-list=LAN
add action=drop chain=prerouting comment="defconf: drop the rest"
```

Notice that the optional **ICMP** chain was used. If you want a very strict firewall then such strict **ICMP** filtering can be used, but in most cases, it is not necessary and simply adds more load on the router's CPU. An ICMP rate limit in most cases is also unnecessary since the Linux kernel is already limiting ICMP packets to 100pps.

```ros
/ipv6/firewall/raw
# Be aware that different operating systems originate packets with different default TTL values
add action=drop chain=icmp6 comment="defconf: rfc4890 drop ll if hop-limit!=255" dst-address=fe80::/10 hop-limit=not-equal:255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: dst unreachable" icmp-options=1:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: packet too big" icmp-options=2:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: limit exceeded" icmp-options=3:0-1 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: bad header" icmp-options=4:0-2 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: Mobile home agent address discovery" icmp-options=144:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: Mobile home agent address discovery" icmp-options=145:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: Mobile prefix solic" icmp-options=146:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: Mobile prefix advert" icmp-options=147:0-255 protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: echo request limit 5,10" icmp-options=128:0-255 limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: echo reply limit 5,10" icmp-options=129:0-255 limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 router solic limit 5,10 only LAN" hop-limit=equal:255 icmp-options=133:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 router advert limit 5,10 only LAN" hop-limit=equal:255 icmp-options=134:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 neighbor solic limit 5,10 only LAN" hop-limit=equal:255 icmp-options=135:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 neighbor advert limit 5,10 only LAN" hop-limit=equal:255 icmp-options=136:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 inverse ND solic limit 5,10 only LAN" hop-limit=equal:255 icmp-options=141:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=accept chain=icmp6 comment="defconf: rfc4890 inverse ND advert limit 5,10 only LAN" hop-limit=equal:255 icmp-options=142:0-255 in-interface-list=LAN limit=5,10:packet protocol=icmpv6
add action=drop chain=icmp6 comment="defconf: drop other icmp" protocol=icmpv6

```
