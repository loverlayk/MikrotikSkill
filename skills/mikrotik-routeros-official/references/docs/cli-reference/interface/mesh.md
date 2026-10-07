# mesh

> RouterOS directory reference for /interface/mesh.

-----------

## interface/mesh 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
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
<ArgTableRow arg="auto-mac" typ="bool"></ArgTableRow>
<ArgTableRow arg="admin-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="mesh-portal" typ="bool"></ArgTableRow>
<ArgTableRow arg="hwmp-default-hoplimit" typ="num"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-waiting-time" typ="time"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-retries" typ="num"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-destination-only" typ="bool"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-reply-and-forward" typ="bool"></ArgTableRow>
<ArgTableRow arg="hwmp-prep-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="hwmp-rann-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="hwmp-rann-propagation-delay" typ="num"></ArgTableRow>
<ArgTableRow arg="hwmp-rann-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="reoptimize-paths" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>
