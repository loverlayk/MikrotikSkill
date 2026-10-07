# instance

> The maximum metric of a RIP route is 15. A metric higher than 15 is considered 'infinity' and routes with such a metric are considered unreachable. Thus RIP cannot be used on networks with more than 15 hops between...

-----------

## routing/rip/instance 
**Type:** Directory

The maximum metric of a RIP route is 15. A metric higher than 15 is considered 'infinity' and routes with such a metric are considered unreachable. Thus RIP cannot be used on networks with more than 15 hops between any two routers, and using redistribute metrics larger than 1 further reduces this maximum hop count.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the instance.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">Name of the VRF to be used for connections.</ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6)"></ArgTableRow>
<ArgTableRow arg="in-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="out-filter-select" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1"></ArgTableRow>
<ArgTableRow arg="originate-default" typ="enum (never | always | if-installed)" unset="1">Whether to originate default route.</ArgTableRow>
<ArgTableRow arg="route-timeout" typ="num">Specifies the time interval after which the route is considered invalid.</ArgTableRow>
<ArgTableRow arg="route-gc-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="update-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1">Routing table name where routes will be installed.</ArgTableRow>
</ArgTable>
