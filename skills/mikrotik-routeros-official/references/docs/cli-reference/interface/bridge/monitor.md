# monitor

> RouterOS command reference for /interface/bridge/monitor.

-----------

## interface/bridge/monitor 
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="enum (disabled | disabled | enabled | enabled)"></ArgTableRow>
<ArgTableRow arg="current-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="bridge-id" typ="composite { prio: num
, mac: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="root-bridge" typ="bool"></ArgTableRow>
<ArgTableRow arg="root-bridge-id" typ="composite { prio: num
, mac: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="regional-root-bridge-id" typ="composite { prio: num
, mac: macAddr
 }"></ArgTableRow>
<ArgTableRow arg="root-path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="root-port" typ="iface_enum { none:0 }"></ArgTableRow>
<ArgTableRow arg="port-count" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-port-count" typ="num"></ArgTableRow>
<ArgTableRow arg="mst-config-digest" typ="string"></ArgTableRow>
<ArgTableRow arg="fast-forward" typ="bool"></ArgTableRow>
<ArgTableRow arg="multicast-router" typ="bool"></ArgTableRow>
<ArgTableRow arg="igmp-querier" typ="composite { interface: iface_enum { none:0 }
, ip-address: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="mld-querier" typ="composite { interface: iface_enum { none:0 }
, ipv6-address: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="declared-vlan-ids" typ="multi { vlan-range: range
 }"></ArgTableRow>
<ArgTableRow arg="registered-vlan-ids" typ="multi { vlan-range: range
 }"></ArgTableRow>
<ArgTableRow arg="mlag-state" typ="string">Shows the MLAG connection state: `connected` when ICCP is established, `connecting` while the peers establish or re-establish the connection, or an error such as `peer port not running` when the configured peer port is unavailable.</ArgTableRow>
<ArgTableRow arg="mlag-active-role" typ="enum (primary | secondary)">The peer with the lowest `priority` acts as the primary device. If the priorities are the same, the peer with the lowest bridge MAC address becomes the primary. The `system-id` of the primary device is used for sending the (R/M)STP BPDU bridge identifier and LACP system ID. The role is shown after a successful MLAG connection.</ArgTableRow>
</ArgTable>
