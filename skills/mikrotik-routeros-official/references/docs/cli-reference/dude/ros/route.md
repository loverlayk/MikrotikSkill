# route

> RouterOS directory reference for /dude/ros/route.

-----------

## dude/ros/route 
**Package:** dude
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="A" typ="active"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="C" typ="connect"></ArgTableRow>
<ArgTableRow arg="S" typ="static"></ArgTableRow>
<ArgTableRow arg="r" typ="rip"></ArgTableRow>
<ArgTableRow arg="b" typ="bgp"></ArgTableRow>
<ArgTableRow arg="o" typ="ospf"></ArgTableRow>
<ArgTableRow arg="m" typ="mme"></ArgTableRow>
<ArgTableRow arg="B" typ="blackhole"></ArgTableRow>
<ArgTableRow arg="U" typ="unreachable"></ArgTableRow>
<ArgTableRow arg="P" typ="prohibit"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="ipPrefix"></ArgTableRow>
<ArgTableRow arg="pref-src" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="gateway" typ="object { gw: alt { interface-address: composite { address: ipAddr
, interface: enum
 }
, interface: enum
, address: super { addr: ipAddr
, [table] [ @enum (main) { main:254 }]
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (arp | ping) { arp:1, ping:2 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (unicast | blackhole | unreachable | prohibit) { unicast:1, blackhole:6, unreachable:7, prohibit:8 }"></ArgTableRow>
<ArgTableRow arg="distance" typ="num"></ArgTableRow>
<ArgTableRow arg="scope" typ="num"></ArgTableRow>
<ArgTableRow arg="target-scope" typ="num"></ArgTableRow>
<ArgTableRow arg="routing-mark" typ="string"></ArgTableRow>
<ArgTableRow arg="vrf-interface" typ="enum"></ArgTableRow>
<ArgTableRow arg="bgp-as-path" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp-local-pref" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp-prepend" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp-med" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp-atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp-origin" typ="enum (igp | egp | incomplete) { igp:0, egp:1, incomplete:2 }"></ArgTableRow>
<ArgTableRow arg="bgp-communities" typ="multi { community: alt { special: enum (no-export | no-advertise | local-as) { no-export:0xFFFFFF01, no-advertise:0xFFFFFF02, local-as:0xFFFFFF03 }
, numbers: super { as: num [ .. 0xffff]
, [num] :num [ .. 0xffff]
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="route-tag" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="gateway-status" typ="object { nexthop: super { gw: alt { interface: enum
, address: ipAddr
 }
, [table] [  on string]
, [state] [  enum (unreachable | reachable | recursive | inactive) { unreachable:0, reachable:1, recursive:2, inactive:3 }]
, [via] [  via multi { array-id, ip: ipAddr
 }]
, [device] [  multi { array-id, interface: enum
 }]
 }
 }"></ArgTableRow>
<ArgTableRow arg="bgp-weight" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities" typ="string"></ArgTableRow>
<ArgTableRow arg="received-from" typ="enum"></ArgTableRow>
<ArgTableRow arg="ospf-metric" typ="num"></ArgTableRow>
<ArgTableRow arg="ospf-type" typ="enum (intra-area | inter-area | external-type-1 | external-type-2 | nssa-external-type-1 | nssa-external-type-2) { intra-area:1, inter-area:2, external-type-1:3, external-type-2:4, nssa-external-type-1:8, nssa-external-type-2:9 }"></ArgTableRow>
</ArgTable>
