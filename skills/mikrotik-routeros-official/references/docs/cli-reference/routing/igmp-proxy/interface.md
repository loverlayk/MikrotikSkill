# interface

> Configure what interfaces will participate as IGMP proxy interfaces on the router. If an interface is not configured as an IGMP proxy interface, then all IGMP traffic received on it will be ignored.

-----------

## routing/igmp-proxy/interface 
**Type:** Directory

Configure what interfaces will participate as IGMP proxy interfaces on the router. If an interface is not configured as an IGMP proxy interface, then all IGMP traffic received on it will be ignored.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum { all:0 }">Name of the interface.</ArgTableRow>
<ArgTableRow arg="upstream" typ="bool">The interface is called "upstream" if it's in the direction of the root of the multicast tree. An IGMP forwarding router must have exactly one upstream interface configured. The upstream interface is used to send out IGMP membership requests.</ArgTableRow>
<ArgTableRow arg="threshold" typ="num">Minimal TTL. Packets received with a lower TTL value are ignored</ArgTableRow>
<ArgTableRow arg="alternative-subnets" typ="multi { numbers: super { as: ipAddr
, [netmask] /num
 }
 }">By default, only packets from directly attached subnets are accepted. This parameter can be used to specify a list of alternative valid packet source subnets, both for data and IGMP packets. Has an effect only on the upstream interface. Should be used when the source of multicast data often is in a different IP network.</ArgTableRow>
<ArgTableRow arg="robustness" typ="num">The robustness value for this interface. Overrides the global robustness setting in the `/routing/igmp-proxy` menu.</ArgTableRow>
<ArgTableRow arg="query-interval" typ="time">How often to send out IGMP Query messages over this interface. Overrides the global query-interval setting in the `/routing/igmp-proxy` menu.</ArgTableRow>
<ArgTableRow arg="query-response-interval" typ="time">How long to wait for responses to an IGMP Query message on this interface. Overrides the global query-response-interval setting in the `/routing/igmp-proxy` menu.</ArgTableRow>
<ArgTableRow arg="last-member-query-interval" typ="time">The timeout for group-specific queries on this interface. Overrides the global last-member-query-interval setting in the `/routing/igmp-proxy` menu.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state.querier" typ="bool">Whether this interface is currently the elected IGMP querier.</ArgTableRow>
<ArgTableRow arg="state.source-ip-address" typ="ipAddr">The source IP address used by this interface for IGMP messages.</ArgTableRow>
<ArgTableRow arg="state.rx-bytes" typ="num">The total amount of received multicast traffic on the interface, in bytes.</ArgTableRow>
<ArgTableRow arg="state.rx-packets" typ="num">The total amount of received multicast traffic on the interface, in packets.</ArgTableRow>
<ArgTableRow arg="state.tx-bytes" typ="num">The total amount of transmitted multicast traffic on the interface, in bytes.</ArgTableRow>
<ArgTableRow arg="state.tx-packets" typ="num">The total amount of transmitted multicast traffic on the interface, in packets.</ArgTableRow>
<ArgTableRow arg="state.robustness" typ="num">The effective robustness value in use on the interface. When this interface is not the elected querier, it adopts the robustness value announced by the elected querier in its IGMP queries.</ArgTableRow>
<ArgTableRow arg="state.query-interval" typ="time">The effective query interval in use on the interface. When this interface is not the elected querier, it adopts the query interval announced by the elected querier in its IGMP queries.</ArgTableRow>
</ArgTable>
