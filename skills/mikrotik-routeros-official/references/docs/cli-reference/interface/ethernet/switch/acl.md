# acl

> Access Control List consists of ingress policy and egress policy engines and allows configuration of up to 128 policy rules (limited by RouterOS). It is an advanced tool for wire-speed packet filtering, forwarding,...

-----------

## interface/ethernet/switch/acl 
**Syscap:** musicswitch
**Type:** Directory

Access Control List consists of ingress policy and egress policy engines and allows configuration of up to 128 policy rules (limited by RouterOS). It is an advanced tool for wire-speed packet filtering, forwarding, shaping, and modifying based on Layer2, Layer3, and Layer4 protocol header field conditions.

:::note
Due to hardware limitations, it is not possible to match broadcast/multicast traffic on specific ports. You should use port isolation, drop traffic on ingress ports, or use VLAN filtering to prevent certain broadcast/multicast traffic from being forwarded.
:::

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="table" typ="enum (ingress | egress) { ingress:0, egress:1 }">Selects the policy table for incoming or outgoing packets.</ArgTableRow>
<ArgTableRow arg="invert-match" typ="bool">Inverts the whole ACL rule matching.</ArgTableRow>
<ArgTableRow arg="src-ports" typ="multi { array-id }">Matching physical source ports or trunks.</ArgTableRow>
<ArgTableRow arg="dst-ports" typ="multi { array-id }">Matching physical destination ports or trunks. It is not possible to match broadcast/multicast traffic on the egress port due to a hardware limitation.</ArgTableRow>
<ArgTableRow arg="service-vid" typ="super { !
, service-vid: range [ .. 4095]
 }">Matching service VLAN ID.</ArgTableRow>
<ArgTableRow arg="service-pcp" typ="num">Matching service PCP.</ArgTableRow>
<ArgTableRow arg="service-dei" typ="num">Matching service DEI.</ArgTableRow>
<ArgTableRow arg="customer-vid" typ="super { !
, customer-vid: range [ .. 4095]
 }">Matching customer VLAN ID.</ArgTableRow>
<ArgTableRow arg="customer-pcp" typ="num">Matching customer PCP.</ArgTableRow>
<ArgTableRow arg="customer-dei" typ="num">Matching customer DEI.</ArgTableRow>
<ArgTableRow arg="src-l3-port" typ="super { !
, src-l3-port: range [ .. 65535]
 }">Matching Layer3 source port.</ArgTableRow>
<ArgTableRow arg="dst-l3-port" typ="super { !
, dst-l3-port: range [ .. 65535]
 }">Matching Layer3 destination port.</ArgTableRow>
<ArgTableRow arg="custom-fields" typ="object { custom-field: super { !
, custom-field: super { base: enum (start-of-frame | end-of-l2-header | end-of-l3-header) { start-of-frame:0, end-of-l2-header:1, end-of-l3-header:2 }
, [offset] :num [ .. 127]
, [range] :range [ .. 65535]
, [mask] [ /num [ .. 65535]]
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="priority" typ="num">Matching internal priority. Valid only in the egress table.</ArgTableRow>
<ArgTableRow arg="drop-precedence" typ="enum (green | yellow | red | drop)">Matching internal drop precedence. Valid only in the egress table.</ArgTableRow>
<ArgTableRow arg="dst-addr-registered" typ="bool">Defines whether to match packets with a registered state - packets whose destination MAC address is in UFDB/MFDB/RFDB. Valid only in the egress table.</ArgTableRow>
<ArgTableRow arg="service-tag" typ="enum (untagged | priority-tagged | tagged | tagged-or-priority-tagged) { untagged:0, priority-tagged:1, tagged:2, tagged-or-priority-tagged:3 }">Format of the service tag.</ArgTableRow>
<ArgTableRow arg="customer-tag" typ="enum (untagged | priority-tagged | tagged | tagged-or-priority-tagged) { untagged:0, priority-tagged:1, tagged:2, tagged-or-priority-tagged:3 }">Format of the customer tag.</ArgTableRow>
<ArgTableRow arg="mac-src-address" typ="super { address: macAddr
, [mask] [ /macAddr]
 }">Source MAC address and mask.</ArgTableRow>
<ArgTableRow arg="mac-dst-address" typ="super { address: macAddr
, [mask] [ /macAddr]
 }">Destination MAC address and mask.</ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="alt { protocol-name: enum (ip-or-ipv6 | non-ip) { ip-or-ipv6:0x10000, non-ip:0x10001 }
, protocol-number: num [ .. 65535]
 }">
Ethernet payload type (MAC-level protocol).
- `802.2` - 802.2 Frames (0x0004)
- `arp` - Address Resolution Protocol (0x0806)
- `capsman` - CAPsMAN to CAP MAC layer connection (0x88BB)
- `dot1x` - EAPoL IEEE 802.1X (0x888E)
- `homeplug-av` - HomePlug AV MME (0x88E1)
- `ip` - Internet Protocol version 4 (0x0800)
- `ip-or-ipv6` - IPv4 or IPv6 (0x0800 or 0x86DD)
- `ipv6` - Internet Protocol Version 6 (0x86DD)
- `ipx` - Internetwork Packet Exchange (0x8137)
- `lacp` - Link Aggregation Control Protocol (0x8809)
- `lldp` - Link Layer Discovery Protocol (0x88CC)
- `loop-protect` - Loop Protect Protocol (0x9003)
- `macsec` - MAC security IEEE 802.1AE (0x88E5)
- `mpls-multicast` - MPLS multicast (0x8848)
- `mpls-unicast` - MPLS unicast (0x8847)
- `mvrp` - Multiple VLAN Registration protocol (0x88F5)
- `non-ip` - Not Internet Protocol version 4 (not 0x0800)
- `packing-compr` - Encapsulated packets with compressed [IP packing](../../../../ip/packing.md) (0x9001)
- `packing-simple` - Encapsulated packets with simple [IP packing](../../../../ip/packing.md) (0x9000)
- `pppoe` - PPPoE Session Stage (0x8864)
- `pppoe-discovery` - PPPoE Discovery Stage (0x8863)
- `rarp` - Reverse Address Resolution Protocol (0x8035)
- `romon` - Router Management Overlay Network [RoMON](../../../../../management-tools/romon.md) (0x88BF)
- `service-vlan` - Provider Bridging IEEE 802.1ad and Shortest Path Bridging IEEE 802.1aq (0x88A8)
- `vlan` - VLAN-tagged frame IEEE 802.1Q and Shortest Path Bridging IEEE 802.1aq with NNI compatibility (0x8100)
</ArgTableRow>
<ArgTableRow arg="lookup-vid" typ="num">VLAN ID used in lookup. It can be changed before reaching the egress table.</ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (tcp | udp | udp-lite | other) { tcp:0, udp:1, udp-lite:2, other:3 }">IP protocol type.</ArgTableRow>
<ArgTableRow arg="fragmented" typ="bool">Whether to match fragmented packets.</ArgTableRow>
<ArgTableRow arg="first-fragment" typ="bool">YES matches not fragmented and the first fragments, NO matches other fragments.</ArgTableRow>
<ArgTableRow arg="ttl" typ="enum (0 | 1 | max | other) { 0:0, 1:1, max:2, other:3 }">Matching TTL field of the packet.</ArgTableRow>
<ArgTableRow arg="ip-dst" typ="composite { address: ipAddr
, netmask: [ num [ .. 32]]
 }">Matching destination IPv4 address.</ArgTableRow>
<ArgTableRow arg="ip-src" typ="composite { address: ipAddr
, netmask: [ num [ .. 32]]
 }">Matching source IPv4 address.</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">Matching DSCP field of the packet.</ArgTableRow>
<ArgTableRow arg="ecn" typ="num">Matching ECN field of the packet.</ArgTableRow>
<ArgTableRow arg="ipv6-dst" typ="ip6Prefix">Matching destination IPv6 address.</ArgTableRow>
<ArgTableRow arg="ipv6-src" typ="ip6Prefix">Matching source IPv6 address.</ArgTableRow>
<ArgTableRow arg="mac-isolation-profile" typ="enum (promiscuous | isolated | community1 | community2) { promiscuous:0, isolated:1, community1:2, community2:3 }">Matches isolation profile based on UFDB. Valid only in the egress policy table.</ArgTableRow>
<ArgTableRow arg="src-mac-addr-state" typ="enum (sa-found | sa-not-found | dynamic-station-move | static-station-move) { sa-found:0, sa-not-found:1, dynamic-station-move:2, static-station-move:3 }">Defines whether to match packets with registered state - packets whose destination MAC address is in UFDB/MFDB/RFDB. Valid only in the egress policy table.</ArgTableRow>
<ArgTableRow arg="flow-id" typ="num"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (forward | redirect-to-cpu | copy-to-cpu | send-to-new-dst-ports | drop) { forward:0, redirect-to-cpu:1, copy-to-cpu:2, send-to-new-dst-ports:3, drop:7 }">
Action for matching ACL packets.
- `copy-to-cpu` - packets are copied to the CPU.
- `drop` - packets are dropped.
- `forward` - packets are forwarded.
- `redirect-to-cpu` - packets are redirected to the CPU.
- `send-to-new-dst-ports` - packets are sent to new destination ports.
</ArgTableRow>
<ArgTableRow arg="new-dst-ports" typ="multi { array-id }">If the action is `send-to-new-dst-ports`, then this property sets which ports/trunks are the new destinations.</ArgTableRow>
<ArgTableRow arg="new-flow-id" typ="num"></ArgTableRow>
<ArgTableRow arg="attack-filter-bypass" typ="bool"></ArgTableRow>
<ArgTableRow arg="ingress-vlan-filter-bypass" typ="bool">Allows bypassing ingress VLAN filtering in the VLAN table for matching packets. This applies only to the ingress policy table.</ArgTableRow>
<ArgTableRow arg="egress-vlan-filter-bypass" typ="bool">Allows bypassing egress VLAN filtering in the VLAN table for matching packets. This applies only to the ingress policy table.</ArgTableRow>
<ArgTableRow arg="isolation-filter-bypass" typ="bool">Allows bypassing the Isolation table for matching packets. This applies only to the ingress policy table.</ArgTableRow>
<ArgTableRow arg="new-registered-state" typ="bool">Whether to modify packet status. YES sets packet status to registered, NO - unregistered. Valid only in the ingress policy table.</ArgTableRow>
<ArgTableRow arg="src-mac-learn" typ="bool">Whether to learn the source MAC of the matched ACL packets. Valid only in the ingress policy table.</ArgTableRow>
<ArgTableRow arg="mirror-to" typ="enum (mirror0 | mirror1) { mirror0:0, mirror1:1 }">Mirroring destination for ACL packets.</ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="num">New service VLAN ID for ACL packets.</ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="num">New customer VLAN ID for ACL packets. If set to 4095, then traffic is dropped.</ArgTableRow>
<ArgTableRow arg="egress-vlan-translate-bypass" typ="bool">Allows bypassing the egress VLAN translation table for matching packets.</ArgTableRow>
<ArgTableRow arg="new-service-pcp" typ="num">New service PCP for ACL packets.</ArgTableRow>
<ArgTableRow arg="new-service-dei" typ="num">New service DEI for ACL packets.</ArgTableRow>
<ArgTableRow arg="new-customer-pcp" typ="num">New customer PCP for ACL packets.</ArgTableRow>
<ArgTableRow arg="new-customer-dei" typ="num">New customer DEI for ACL packets.</ArgTableRow>
<ArgTableRow arg="new-dscp" typ="num">New DSCP for ACL packets.</ArgTableRow>
<ArgTableRow arg="new-priority" typ="num">New internal priority for ACL packets.</ArgTableRow>
<ArgTableRow arg="new-drop-precedence" typ="enum (green | yellow | red | drop)">New internal drop precedence for ACL packets.</ArgTableRow>
<ArgTableRow arg="policer" typ="enum">Applied ACL Policer for ACL packets.</ArgTableRow>
</ArgTable>
