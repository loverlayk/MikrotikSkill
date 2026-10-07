# pcap

> RouterOS directory reference for /routing/stats/pcap.

-----------

## routing/stats/pcap 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="file" typ="string"></ArgTableRow>
<ArgTableRow arg="timestamp" typ="time"></ArgTableRow>
<ArgTableRow arg="src" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="dst" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="protocol" typ="string"></ArgTableRow>
<ArgTableRow arg="data" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.type" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.notification.code" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.notification.subcode" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.route-refresh.afi" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.route-refresh.safi" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.route-refresh.subtype" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.update.local-pref" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.update.med" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.update.nexthop" typ="multi { prefix: address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.nlri" typ="multi { prefix: address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.withdrawn" typ="multi { prefix: address (flags=46i/SR)
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.origin" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.update.as-path" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.as4-path" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.communities" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.ext-communities" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.large-communities" typ="multi { value: string
 }"></ArgTableRow>
<ArgTableRow arg="bgp.update.atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp.update.aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.update.as4-aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.update.originator-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="bgp.update.cluster-list" typ="multi { value: ipAddr
 }"></ArgTableRow>
</ArgTable>
