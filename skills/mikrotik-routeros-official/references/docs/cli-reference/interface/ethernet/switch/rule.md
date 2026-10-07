# rule

> RouterOS directory reference for /interface/ethernet/switch/rule.

-----------

## interface/ethernet/switch/rule 
**Syscap:** rbswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1">Matching the switch group on which the rule will apply.</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, port: enum
 }" syscap="!crs_prestera">Matching switch interfaces where the rule will apply to incoming traffic. Multiple ports and [hardware-offloaded bonding](../../../../../bridging-and-switching/l3-hardware-offloading.md#l3hw-feature-support) interfaces can be selected. Note that the `switch1-cpu` port cannot be selected. If `ports` property is left empty, the rule will apply to all switch interfaces.</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { address: macAddr
, [mask] /macAddr
 }">Matching source MAC address and mask.</ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="super { address: macAddr
, [mask] /macAddr
 }">Matching destination MAC address and mask.</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="alt { protocol-name: enum ()
, protocol-number: num [ .. 65535]
 }">Matching a particular MAC protocol specified by protocol name or number (skips VLAN tags if any).</ArgTableRow>
<ArgTableRow arg="vlan-header" typ="enum (not-present | present)">Matching VLAN header, whether the VLAN header is present or not. Requires `vlan-filtering=yes`.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">Matching VLAN ID. Requires `vlan-filtering=yes`.</ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="num">Matching VLAN priority (priority code point).</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { address: ipAddr
, [mask] /alt { bitmask: ipAddr
, netmask: num [ .. 32]
 }
 }">Matching source IPv4 address and mask. If `mac-protocol=arp` is specified, matches the source IP in ARP packets. Without `mac-protocol`, matches only IPv4 packets.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { address: ipAddr
, [mask] /alt { bitmask: ipAddr
, netmask: num [ .. 32]
 }
 }">Matching destination IPv4 address and mask. If `mac-protocol=arp` is specified, matches the destination IP in ARP packets. Without `mac-protocol`, matches only IPv4 packets.</ArgTableRow>
<ArgTableRow arg="protocol" typ="alt { protocol-name: enum ()
, protocol-number: num [ .. 255]
 }">Matching a particular IP protocol specified by protocol name or number. Only applies to IPv4 packets if `mac-protocol` is not specified. To match certain IPv6 protocols, use the `mac-protocol=ipv6` setting.</ArgTableRow>
<ArgTableRow arg="src-port" typ="range">Matching source protocol port number (applies to IPv4 and IPv6 packets if `mac-protocol` is not specified).</ArgTableRow>
<ArgTableRow arg="dst-port" typ="range">Matching destination protocol port number or range (applies to IPv4 and IPv6 packets if mac-protocol is not specified).</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">Matching the DSCP field of the packet (only applies to IPv4 packets).</ArgTableRow>
<ArgTableRow arg="src-address6" typ="super { address: ip6Addr
, [mask] /alt { bitmask: ip6Addr
, netmask: num
 }
 }">Matching source IPv6 address and mask.</ArgTableRow>
<ArgTableRow arg="dst-address6" typ="super { address: ip6Addr
, [mask] /alt { bitmask: ip6Addr
, netmask: num
 }
 }">Matching destination IPv6 address and mask.</ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num">Matching IPv6 traffic class.</ArgTableRow>
<ArgTableRow arg="flow-label" typ="num">Matching IPv6 flow label.</ArgTableRow>
<ArgTableRow arg="copy-to-cpu" typ="bool">Clones the matching packet and sends it to the CPU.</ArgTableRow>
<ArgTableRow arg="redirect-to-cpu" typ="bool">Changes the destination port of a matching packet to the switch CPU.</ArgTableRow>
<ArgTableRow arg="mirror" typ="bool" syscap="switch-mirror-prestera">Clones the matching packet and sends it to the `mirror-target` port.</ArgTableRow>
<ArgTableRow arg="new-dst-ports" typ="multi { array-id, port: alt { port: enum
, bond: iface_enum
 }
 }">
Changes the destination port as specified, multiple ports allowed, including a switch CPU port.
- If the setting is left empty (e.g. `new-dst-ports=""`), the packet will be dropped;
- If a port or [hardware-offloaded bonding](../../../../../bridging-and-switching/marvell-prestera-switch-chip-features.md#bonding) interface is specified, the packet will be redirected to that port. Only a single port or bond interface is supported;
- if you use the `all` argument, packet will be allowed to pass through to the egress processing without being dropped;
- If this parameter is not used, the packet will be accepted as is.
</ArgTableRow>
<ArgTableRow arg="mirror-ports" typ="multi { array-id, port: enum
 }" syscap="switch-mv88e6xxx">Selects multiple mirroring target ports, only available on the **88E6393X** switch chip. Matched packets in the ACL rule will be copied and sent to selected ports.</ArgTableRow>
<ArgTableRow arg="new-qos-profile" typ="enum" syscap="crs_prestera">The name of the QoS profile to assign to the matched packets.</ArgTableRow>
<ArgTableRow arg="keep-qos-fields" typ="bool" syscap="crs_prestera">Should the original values of QoS fields (PCP, DSCP) be kept (`yes`), or replaced with the ones from the assigned QoS profile (`no`)? Relevant only if `new-qos-profile` is set.</ArgTableRow>
<ArgTableRow arg="new-vlan-id" typ="num">Changes the VLAN ID to the specified value. Requires `vlan-filtering=yes`.</ArgTableRow>
<ArgTableRow arg="new-vlan-priority" typ="num">Changes the VLAN priority (priority code point). Requires `vlan-filtering=yes`.</ArgTableRow>
<ArgTableRow arg="new-vrf" typ="enum" syscap="crs_prestera">Assigns ingress traffic to a specified VRF. Requires [hardware-offloaded VRF](../../../../../bridging-and-switching/l3-hardware-offloading.md#l3hw-feature-support) support on the switch chip. On VRF-unaware switches (98DX3xxx and 98DX2xxx series), setting `new-vrf` to anything other than `main` will be treated as `redirect-to-cpu=yes`.</ArgTableRow>
<ArgTableRow arg="rate" typ="num">Sets ingress traffic limitation (bits per second) for matched traffic.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="packets" typ="num" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="bytes" typ="num" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="internal-priority" typ="num"></ArgTableRow>
</ArgTable>
