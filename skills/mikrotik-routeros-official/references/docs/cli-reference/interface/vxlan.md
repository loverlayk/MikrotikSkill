# vxlan

> RouterOS directory reference for /interface/vxlan.

-----------

## interface/vxlan 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">hw-offloaded</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="vni" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="group" typ="alt { address: ipAddr
, ipv6-address: ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="enum (disabled | enabled | auto | inherit) { disabled:0, enabled:1, auto:2, inherit:2 }"></ArgTableRow>
<ArgTableRow arg="vtep-vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="vteps-ip-version" typ="enum (ipv4 | ipv6) { ipv4:1, ipv6:2 }"></ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool"></ArgTableRow>
<ArgTableRow arg="max-fdb-size" typ="num"></ArgTableRow>
<ArgTableRow arg="ttl" typ="num"></ArgTableRow>
<ArgTableRow arg="learning" typ="bool"></ArgTableRow>
<ArgTableRow arg="checksum" typ="bool"></ArgTableRow>
<ArgTableRow arg="rem-csum" typ="enum (none | rx | tx | both) { none:0, rx:1, tx:2, both:3 }"></ArgTableRow>
<ArgTableRow arg="hw" typ="bool"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="bridge-pvid" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp) { disabled:0, enabled:1, proxy-arp:2, reply-only:3, local-proxy-arp:4 }"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }"></ArgTableRow>
<ArgTableRow arg="arp-accept" typ="bool"></ArgTableRow>
<ArgTableRow arg="loop-protect" typ="enum (default | off | on) { default:0, off:1, on:2 }"></ArgTableRow>
<ArgTableRow arg="loop-protect-send-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="loop-protect-disable-time" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled) { off:1, on:2, disabled:3 }"></ArgTableRow>
</ArgTable>
