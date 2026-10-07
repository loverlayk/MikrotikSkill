# bridge

> RouterOS directory reference for /interface/bridge.

-----------

## interface/bridge 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="Y" typ="managed">managed</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="protocol-mode" typ="enum (none | stp | rstp | mstp) { none:0, stp:1, rstp:2, mstp:3 }"></ArgTableRow>
<ArgTableRow arg="fast-forward" typ="bool"></ArgTableRow>
<ArgTableRow arg="igmp-snooping" typ="bool"></ArgTableRow>
<ArgTableRow arg="multicast-router" typ="enum (disabled | temporary-query | permanent) { disabled:0, temporary-query:1, permanent:2 }"></ArgTableRow>
<ArgTableRow arg="multicast-querier" typ="bool"></ArgTableRow>
<ArgTableRow arg="querier-uses-bridge-address" typ="bool"></ArgTableRow>
<ArgTableRow arg="startup-query-count" typ="num"></ArgTableRow>
<ArgTableRow arg="last-member-query-count" typ="num"></ArgTableRow>
<ArgTableRow arg="last-member-interval" typ="time" deprecated="1"></ArgTableRow>
<ArgTableRow arg="last-member-query-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="membership-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="querier-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="query-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="query-response-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="startup-query-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="igmp-version" typ="enum (2 | 3) { 2:2, 3:3 }"></ArgTableRow>
<ArgTableRow arg="mld-version" typ="enum (1 | 2) { 1:1, 2:2 }"></ArgTableRow>
<ArgTableRow arg="auto-mac" typ="bool"></ArgTableRow>
<ArgTableRow arg="admin-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ageing-time" typ="time"></ArgTableRow>
<ArgTableRow arg="priority" typ="alt { priority: enum (0x0000 | 0x1000 | 0x2000 | 0x3000 | 0x4000 | 0x5000 | 0x6000 | 0x7000 | 0x8000 | 0x9000 | 0xa000 | 0xb000 | 0xc000 | 0xd000 | 0xe000 | 0xf000) { 0x0000:0x0000, 0x1000:0x1000, 0x2000:0x2000, 0x3000:0x3000, 0x4000:0x4000, 0x5000:0x5000, 0x6000:0x6000, 0x7000:0x7000, 0x8000:0x8000, 0x9000:0x9000, 0xa000:0xa000, 0xb000:0xb000, 0xc000:0xc000, 0xd000:0xd000, 0xe000:0xe000, 0xf000:0xf000 }
, priority: num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="max-message-age" typ="time"></ArgTableRow>
<ArgTableRow arg="forward-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="transmit-hold-count" typ="num"></ArgTableRow>
<ArgTableRow arg="region-name" typ="string"></ArgTableRow>
<ArgTableRow arg="region-revision" typ="num"></ArgTableRow>
<ArgTableRow arg="max-hops" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-filtering" typ="bool"></ArgTableRow>
<ArgTableRow arg="ether-type" typ="enum (0x8100 | 0x88a8 | 0x9100) { 0x8100:0x8100, 0x88a8:0x88a8, 0x9100:0x9100 }"></ArgTableRow>
<ArgTableRow arg="pvid" typ="num"></ArgTableRow>
<ArgTableRow arg="frame-types" typ="enum (admit-all | admit-only-vlan-tagged | admit-only-untagged-and-priority-tagged) { admit-all:0, admit-only-vlan-tagged:1, admit-only-untagged-and-priority-tagged:2 }"></ArgTableRow>
<ArgTableRow arg="ingress-filtering" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-snooping" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-snooping-vlan-ids" typ="multi { vlan-id-range: range [1 .. 4094]
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-agent-circuit-id" typ="string">
Specify the relay agent circuit-id suboption value of the option 82 to be added to the DHCP messages passing through the bridge.
The string length is limited to 255 characters with the default value being: $(INTERFACE):$(VID).
The string value can contain variables, whose names must be enclosed in parentheses and prepended by a dollar sign.
Example: 'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'.
The following variables are supported: HOSTNAME, INTERFACE, VID and BRIDGEMAC.
For the compatibility with previous versions, where the remote-id value was fixed, the semicolon appearing in the default value expression is not
included in the remote-id value, in the case when the vlan filtering is not enabled.
</ArgTableRow>
<ArgTableRow arg="dhcp-agent-remote-id" typ="string">
Specify the relay agent remote-id suboption value of the option 82 to be added to the DHCP messages passing through the bridge.
The string length is limited to 255 characters with the default value being: $(BRIDGEMAC).
The string value can contain variables, whose names must be enclosed in parentheses and prepended by a dollar sign.
Example: 'some_arbitrary_text $(HOSTNAME) another_piece_of_text $(BRIDGEMAC)'.
The following variables are supported: HOSTNAME, INTERFACE, VID and BRIDGEMAC.
</ArgTableRow>
<ArgTableRow arg="arp-inspection" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcpv6-snooping" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcpv6-agent-circuit-id" typ="string">
Specify the DHCPv6 option 18 value to be added to the DHCPv6 messages passing through the bridge.
The string length is limited to 255 characters with the default value being: $(INTERFACE):$(VID).
The string value can contain variables, whose names must be enclosed in parentheses and prepended by a dollar sign.
Example: 'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'.
The following variables are supported: HOSTNAME, INTERFACE, VID and BRIDGEMAC.
</ArgTableRow>
<ArgTableRow arg="dhcpv6-agent-remote-id" typ="string">
Specify the DHCPv6 option 37 value to be added to the DHCPv6 messages passing through the bridge.
The string length is limited to 255 characters with the default value being: $(BRIDGEMAC).
The string value can contain variables, whose names must be enclosed in parentheses and prepended by a dollar sign.
Example: 'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'.
The following variables are supported: HOSTNAME, INTERFACE, VID and BRIDGEMAC.
</ArgTableRow>
<ArgTableRow arg="ip-source-guard" typ="bool"></ArgTableRow>
<ArgTableRow arg="ra-guard" typ="bool"></ArgTableRow>
<ArgTableRow arg="port-cost-mode" typ="enum (short | long)"></ArgTableRow>
<ArgTableRow arg="mvrp" typ="bool"></ArgTableRow>
<ArgTableRow arg="forward-reserved-addresses" typ="bool"></ArgTableRow>
<ArgTableRow arg="max-learned-entries" typ="alt { max-learned-entries: enum (unlimited | auto)
, max-learned-entries: num
 }"></ArgTableRow>
<ArgTableRow arg="mlag-peer-port" typ="alt { interface: iface_enum { none }
, interface-bond: iface_enum
 }">
An interface that will be used as a peer port. Both peer devices are using inter-chassis communication over these peer ports to establish MLAG and update the host table.  
Peer ports can be configured as single Ethernet interfaces or bonding interfaces. However, using a bonding interface is recommended, as it helps prevent a single interface failure from affecting connectivity, especially when both MLAG nodes are still up and running.  
It is recommended to keep the untagged VLAN used by the peer ports separate from the rest of your network, either by assigning a dedicated untagged VLAN (using `pvid`), or by setting the peer port to only allow VLAN tagged frames (using `frame-types=admit-only-vlan-tagged`).  
All VLANs used for bridge slave ports must also be configured as tagged VLANs for peer-port (in the `/interface/bridge/vlan` table), so that peer-port is a member of those VLANs and can forward data.
</ArgTableRow>
<ArgTableRow arg="mlag-priority" typ="num">This setting changes the priority for selecting the primary MLAG node. A lower number means higher priority. If both MLAG nodes have the same priority, the one with the lowest bridge MAC address will become the primary device.</ArgTableRow>
<ArgTableRow arg="mlag-heartbeat" typ="alt { mlag-heartbeat: enum (none) { none:0 }
, mlag-heartbeat: time [1s .. 10s]
 }">This setting controls how often heartbeat messages are sent to check the connection between peers. If no heartbeat message is received for three intervals in a row, the peer logs a warning about potential communication problems. If set to `none`, heartbeat messages are not sent at all.</ArgTableRow>
<ArgTableRow arg="mlag-init-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="mlag-lacp-fallback" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="actual-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>
