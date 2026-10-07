# mfc

> Multicast forwarding cache (MFC) status.

-----------

## routing/igmp-proxy/mfc 
**Type:** Directory

Multicast forwarding cache (MFC) status.

RouterOS supports static multicast forwarding rules for IGMP proxy. If a static rule is added, all dynamic rules for that group will be ignored. These rules will take effect only if IGMP-proxy interfaces are configured (upstream and downstream interfaces should be set) otherwise these rules won't be active.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="group" typ="ipAddr" mandatory="1">The multicast group address this rule applies to.</ArgTableRow>
<ArgTableRow arg="source" typ="ipAddr" mandatory="1">The multicast data originator address.</ArgTableRow>
<ArgTableRow arg="upstream-interface" typ="iface_enum" mandatory="1">The interface that is receiving stream data.</ArgTableRow>
<ArgTableRow arg="downstream-interfaces" typ="multi { interface: iface_enum
 }">The received stream will be sent out to the listed interfaces only.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-downstream-interfaces" typ="multi { interface: iface_enum
 }">The packet stream is going out of the router through this interface.</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">The total amount of received multicast traffic.</ArgTableRow>
<ArgTableRow arg="packets" typ="num">The total amount of received multicast packets.</ArgTableRow>
<ArgTableRow arg="wrong-packets" typ="num">The total amount of received multicast packets that arrived on a wrong interface, for example, a multicast stream that is received on a downstream interface instead of an upstream interface.</ArgTableRow>
</ArgTable>
