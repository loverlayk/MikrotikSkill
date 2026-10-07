# route

> A read-only table that lists routes from all the address families as well as all filtered routes with all possible route attributes.

-----------

## routing/route 
**Type:** Directory

A read-only table that lists routes from all the address families as well as all filtered routes with all possible route attributes.

Default example output of the table with various route types:

```ros
[admin@MikroTik] /routing/route> print
Flags: A - ACTIVE; c, s, a, l, y - COPY; H - HW-OFFLOADED
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
    DST-ADDRESS                 GATEWAY           AFI    D  SCOPE  TA  IMMEDIATE-GW
 lH 10.0.0.0/8                                    ip     0
;;; defconf
As  10.0.0.0/8                  10.155.130.1      ip     1     30  10  10.155.130.1%ether1
 lH 10.155.130.0/25                               ip     0
Ac  10.155.130.0/25             ether1            ip     0     10      ether1
 aH 10.155.130.12/32                              ip     0
 lH 111.13.0.0/24                                 ip     0
Ac  111.13.0.0/24               ether2            ip     0     10      ether2
 aH 111.13.0.1/32                                 ip     0
Ac  111.111.111.2/32            loopback@vrfTest  ip     0     10      loopback
Ac  2111:4::/64                 ether2            ipv6   0     10      ether2
Ac  fe80::%ether1/64            ether1            ipv6   0     10      ether1
Ac  fe80::%ether2/64            ether2            ipv6   0     10      ether2
Ac  fe80::%ether3/64            ether3            ipv6   0     10      ether3
Ac  fe80::%ether4/64            ether4            ipv6   0     10      ether4
Ac  3333::2/128                 loopback@vrfTest  ipv6   0     10      loopback
Ac  fe80::%loopback/64          loopback@vrfTest  ipv6   0     10      loopback
Ay  111.111.111.2/32&65530:100  loopback@vrfTest  vpnv4  0     10   5  loopback
Ay  3333::2/128&65530:100       loopback@vrfTest  vpnv6  0     10   5  loopback
A H ether1                                        link   0
A H ether2                                        link   0
A H ether3                                        link   0
A H ether4                                        link   0
A H loopback                                      link   0
```

Detailed example output with some BGP, OSPF, and other routes:

```ros
[admin@MikroTik] /routing/route> print detail
Flags: X - disabled, F - filtered, U - unreachable, A - active;
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, a - ldp-address, l - ldp-mapping, y - copy; H - hw-offloaded;
+ - ecmp, B - blackhole
  o   afi=ip4 contribution=best-candidate dst-address=0.0.0.0/0 routing-table=main gateway=10.155.101.1%ether1 immediate-gw=10.155.101.1%ether1
       distance=110 scope=20 target-scope=10 belongs-to="OSPF route"
       ospf.metric=2 .tag=111 .type=ext-type-1
       debug.fwp-ptr=0x203425A0

 Ad + afi=ip4 contribution=active dst-address=0.0.0.0/0 routing-table=main pref-src="" gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1
       distance=1 scope=30 target-scope=10 vrf-interface=ether1 belongs-to="DHCP route"
       debug.fwp-ptr=0x20342060

 As + afi=ip4 contribution=active dst-address=0.0.0.0/0 routing-table=main pref-src="" gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1
       distance=1 scope=30 target-scope=10 belongs-to="Static route"
       debug.fwp-ptr=0x20342060

 Fb   afi=ip4 contribution=filtered dst-address=1.0.0.0/24 routing-table=main gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1 distance=20
       scope=40 target-scope=10 belongs-to="BGP IP routes from 10.155.101.217" rpki=valid
       bgp.peer-cache-id=*B000002 .aggregator="13335:172.68.180.1" .as-path="65530,100,9002,13335" .atomic-aggregate=yes .origin=igp
       debug.fwp-ptr=0x20342960

```

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="F" typ="filtered">A flag indicates whether the route was filtered by routing filters and excluded from being used as the best route.</ArgTableRow>
<ArgTableRow arg="U" typ="unreachable">A flag indicates whether the route next-hop is unreachable.</ArgTableRow>
<ArgTableRow arg="A" typ="active">A flag indicates whether the route is elected as Active and eligible to be added to the FIB.</ArgTableRow>
<ArgTableRow arg="c" typ="connect">connect</ArgTableRow>
<ArgTableRow arg="s" typ="static">static</ArgTableRow>
<ArgTableRow arg="r" typ="rip">rip</ArgTableRow>
<ArgTableRow arg="b" typ="bgp">A flag indicates whether this route was added by the [BGP](../../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) protocol.</ArgTableRow>
<ArgTableRow arg="n" typ="bgp-net">bgp-net</ArgTableRow>
<ArgTableRow arg="o" typ="ospf">ospf</ArgTableRow>
<ArgTableRow arg="i" typ="isis">isis</ArgTableRow>
<ArgTableRow arg="d" typ="dhcp">A flag indicates whether the route was added by the DHCP service.</ArgTableRow>
<ArgTableRow arg="v" typ="vpn">A flag indicates whether the route was added by one of the VPN protocols (PPPoE, L2TP, SSTP, etc.)</ArgTableRow>
<ArgTableRow arg="m" typ="modem">A flag indicates whether the route is added by the LTE or 3g modems.</ArgTableRow>
<ArgTableRow arg="a" typ="ldp-address">A flag indicates whether the route entry is an LDP address.</ArgTableRow>
<ArgTableRow arg="l" typ="ldp-mapping">A flag indicates whether the route entry is the LDP mapping.</ArgTableRow>
<ArgTableRow arg="g" typ="slaac">slaac</ArgTableRow>
<ArgTableRow arg="y" typ="bgp-mpls-vpn">A flag indicates a copy of the route to be redistributed as the L3VPN route. VPNv4/6 related attributes are attached to this route.</ArgTableRow>
<ArgTableRow arg="e" typ="evpn">evpn</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">Indicates whether the route is eligible to be hardware offloaded on supported hardware.</ArgTableRow>
<ArgTableRow arg="+" typ="ecmp">A flag indicates whether the route is added as an [Equal-Cost Multi-Path](../../user-guides/routing-and-networking-protocols/routing-decision.md#multipath-ecmp-routes) route in the FIB</ArgTableRow>
<ArgTableRow arg="B" typ="blackhole">A flag indicates whether it is a blackhole route.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="afi" typ="enum (bad | ip | ipv6 | l2vpn | vpnv4 | vpnv6 | l2vpn-cisco | mip4 | mip6 | link | l2vpn-link | evpn)" unset="1">Address family this route belongs to.</ArgTableRow>
<ArgTableRow arg="contribution" typ="enum (filtered | unreachable | candidate | best-candidate | active)">Shows the route status contributing to the election process, e.g "filtered, active, candidate"</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46i/SR)"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum">Routing table this route belongs to.</ArgTableRow>
<ArgTableRow arg="ve-id" typ="num"></ArgTableRow>
<ArgTableRow arg="ve-block-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="ve-block-size" typ="num"></ArgTableRow>
<ArgTableRow arg="label" typ="num"></ArgTableRow>
<ArgTableRow arg="pref-src" typ="address (flags=46)" unset="1"></ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=46ivL)">Configured gateway, for the actually resolved gateway, see `immediate-gw` parameter.</ArgTableRow>
<ArgTableRow arg="nexthop-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="immediate-gw" typ="multi { gw: address (flags=46i)
 }">Shows actual (resolved) gateway and interface that will be used for packet forwarding. Displayed in format `[ip%interface]`.</ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping | bfd)" unset="1">Currently used check-gateway option.</ArgTableRow>
<ArgTableRow arg="distance" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="scope" typ="num" unset="1">Scope used in the next-hop lookup process. [Read more>>](../../user-guides/routing-and-networking-protocols/routing-decision.md#nexthop-lookup)</ArgTableRow>
<ArgTableRow arg="target-scope" typ="num" unset="1">Target scope used in next-hop lookup process. [Read more>>](../../user-guides/routing-and-networking-protocols/routing-decision.md#nexthop-lookup).</ArgTableRow>
<ArgTableRow arg="vrf-interface" typ="iface_enum" unset="1">Internal use only parameter which allows identifying to which VRF route should be added. Used by services that add routes dynamically, for example, DHCP client. Shown for debugging purposes.</ArgTableRow>
<ArgTableRow arg="belongs-to" typ="string">Descriptive info showing from where the route was received.</ArgTableRow>
<ArgTableRow arg="local-address" typ="address (flags=46iv)">Local IP address of the connected network.</ArgTableRow>
<ArgTableRow arg="route-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="total-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="rpki" typ="enum (unknown | valid | invalid)" unset="1">Current status of the prefix from the [RPKI](../../user-guides/routing-and-networking-protocols/unicast/rpki.md) validation process.</ArgTableRow>
<ArgTableRow arg="bgp.session" typ="enum">[BGP](../../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) session that installed the route. See `/routing/bgp/session` menu.</ArgTableRow>
<ArgTableRow arg="bgp.aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.as-path" typ="string">Value of the **`AS_PATH`** BGP attribute.</ArgTableRow>
<ArgTableRow arg="bgp.cluster-list" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.communities" typ="multi { value: string
 }">Value of the **`COMMUNITIES`** BGP attribute.</ArgTableRow>
<ArgTableRow arg="bgp.ext-communities" typ="multi { value: string
 }">Value of the **`EXTENDED_COMMUNITIES`** BGP attribute.</ArgTableRow>
<ArgTableRow arg="bgp.large-communities" typ="multi { value: string
 }">Value of the **`LARGE_COMMUNITIES`** BGP attribute.</ArgTableRow>
<ArgTableRow arg="bgp.unknown" typ="multi { value: string
 }">Hex blob of unknown [BGP](../../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) attributes.</ArgTableRow>
<ArgTableRow arg="bgp.originator-id" typ="address (flags=4)"></ArgTableRow>
<ArgTableRow arg="bgp.nexthop" typ="multi { gw: address (flags=4)
 }"></ArgTableRow>
<ArgTableRow arg="bgp.out-nexthop" typ="multi { gw: address (flags=4iv)
 }"></ArgTableRow>
<ArgTableRow arg="bgp.weight" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.local-pref" typ="num">Value of the **`LOCAL_PREF`** BGP attribute.</ArgTableRow>
<ArgTableRow arg="bgp.igp-metric" typ="num">Value of the **`IGP_METRIC`** BGP attribute</ArgTableRow>
<ArgTableRow arg="bgp.pmsi" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.med" typ="num">Value of the **`MED`** BGP attribute.</ArgTableRow>
<ArgTableRow arg="bgp.atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp.origin" typ="enum (igp | egp | incomplete) { igp:0, egp:1, incomplete:2 }"></ArgTableRow>
<ArgTableRow arg="bgp.esi" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.otc" typ="num"></ArgTableRow>
<ArgTableRow arg="route-distinguisher" typ="string"></ArgTableRow>
<ArgTableRow arg="rip.tag" typ="num"></ArgTableRow>
<ArgTableRow arg="rip.metric" typ="num"></ArgTableRow>
<ArgTableRow arg="ospf.metric" typ="num"></ArgTableRow>
<ArgTableRow arg="ospf.tag" typ="num"></ArgTableRow>
<ArgTableRow arg="ospf.type" typ="enum (intra | inter | ext-type-1 | ext-type-2 | nssa-type-1 | nssa-type-2) { intra:0, inter:1, ext-type-1:2, ext-type-2:3, nssa-type-1:4, nssa-type-2:5 }"></ArgTableRow>
<ArgTableRow arg="isis.type" typ="enum (l1 | l2 | l1-inter | l1-ext | l2-ext | l1-inter-ext) { l1:0, l2:1, l1-inter:2, l1-ext:3, l2-ext:4, l1-inter-ext:5 }"></ArgTableRow>
<ArgTableRow arg="isis.metric" typ="num"></ArgTableRow>
<ArgTableRow arg="mpls.labels" typ="multi { label: num
 }"></ArgTableRow>
<ArgTableRow arg="mpls.in-label" typ="num">Mapped MPLS ingress label.</ArgTableRow>
<ArgTableRow arg="mpls.out-label" typ="num">Mapped MPLS egress label.</ArgTableRow>
<ArgTableRow arg="ldp.peer-id" typ="num"></ArgTableRow>
<ArgTableRow arg="ldp.label" typ="num">LDP mapped MPLS label.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="hoplimit" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.fwp-ptr" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.route-ptr" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.input.refs" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.input.size" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.input.ptr" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.input.raw" typ="string"></ArgTableRow>
<ArgTableRow arg="debug.merge.refs" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.merge.size" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.merge.ptr" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.merge.raw" typ="string"></ArgTableRow>
</ArgTable>
