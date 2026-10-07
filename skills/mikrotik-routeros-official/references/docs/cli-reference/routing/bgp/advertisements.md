# advertisements

> RouterOS directory reference for /routing/bgp/advertisements.

-----------

## routing/bgp/advertisements 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="enum"></ArgTableRow>
<ArgTableRow arg="dst" typ="address (flags=46/R)"></ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6 | l2vpn | l2vpn-cisco | vpnv4 | vpnv6)"></ArgTableRow>
<ArgTableRow arg="local-pref" typ="num"></ArgTableRow>
<ArgTableRow arg="med" typ="num"></ArgTableRow>
<ArgTableRow arg="nexthop" typ="multi { prefix: address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="nlri" typ="multi { prefix: address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="withdrawn" typ="multi { prefix: address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="origin" typ="num"></ArgTableRow>
<ArgTableRow arg="as-path" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="as4-path" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="communities" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="ext-communities" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="large-communities" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="as4-aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="originator-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="cluster-list" typ="multi { value: ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="igp-metric" typ="num"></ArgTableRow>
<ArgTableRow arg="otc" typ="num"></ArgTableRow>
</ArgTable>
