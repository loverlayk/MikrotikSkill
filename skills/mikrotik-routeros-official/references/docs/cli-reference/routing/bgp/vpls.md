# vpls

> This menu lists all the configured BGP-based VPLS instances. These instances allow the router to advertise VPLS BGP NLRI and indicate that the router belongs to a specific customer VPLS network.

-----------

## routing/bgp/vpls 
**Conditions:** !smips
**Type:** Directory

This menu lists all the configured BGP-based VPLS instances. These instances allow the router to advertise VPLS BGP NLRI and indicate that the router belongs to a specific customer VPLS network.

MP-BGP-based autodiscovery and signaling (RFC 4761).

Cisco VPLS BGP-based auto-discovery (draft-ietf-l2vpn-signaling-08).

Support for multiple import/export route target extended communities for BGP-based VPLS (both, RFC 4761 and draft-ietf-l2vpn-signaling-08).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="rd" typ="address (flags=R)" unset="1">Specifies the value that gets attached to VPLS NLRI so that receiving routers can distinguish advertisements that may otherwise look the same. This implies that a unique route-distinguisher for every VPLS must be used. It is not necessary to use the same route distinguisher for some VPLS on all routers forming that VPLS as distinguisher is not used for determining if some BGP NLRI is related to a particular VPLS (Route Target attribute is used for this), but it is mandatory to have different distinguishers for different VPLSes. Accepts 3 types of formats. [Read more>>](../../../user-guides/routing-and-networking-protocols/route-distinguisher-and-route-target.md)</ArgTableRow>
<ArgTableRow arg="site-id" typ="num" unset="1">Unique site identifier. Each site must have a unique site-id. A parameter must be set for&nbsp;RFC 4761 style VPLS signaling.</ArgTableRow>
<ArgTableRow arg="cisco-id" typ="address" unset="1">Unique identifier. A parameter must be set for cisco-style VPLS signaling. In most cases this should not be used, any modern software supports RFC 4761 style signaling (see site-id parameter). Parameter is a merge of l2-router-id and RD, for example: 10.155.155.1&amp;6550:123</ArgTableRow>
<ArgTableRow arg="import-route-targets" typ="multi { array-id, rt: address (flags=R)
 }" unset="1">The setting is used to determine if BGP NLRI is related to a particular VPLS, by comparing route targets received from BGP NLRI.</ArgTableRow>
<ArgTableRow arg="export-route-targets" typ="multi { array-id, rt: address (flags=R)
 }" unset="1">The setting is used to tag BGP NLRI with one or more route targets which on the remote side is used by `import-route-targets`.</ArgTableRow>
<ArgTableRow arg="local-pref" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="interface-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="pw-type" typ="enum (tagged-ethernet | raw-ethernet | vpls)" unset="1">Pseudowire type (RFC 4447 Section 5.2). By default, `raw-ethernet` is used.</ArgTableRow>
<ArgTableRow arg="pw-l2mtu" typ="num" unset="1">L2MTU value advertised to a remote peer (RFC 4447 Section 5.2).</ArgTableRow>
<ArgTableRow arg="pw-control-word" typ="enum (default | enabled | disabled)" unset="1">Enables or disables Control Word usage (RFC 4623 Section 4). Default values for regular and Cisco-style VPLS tunnels differ. Cisco-style by default has Control Word usage disabled. Read more in the [VPLS Control Word](../../../user-guides/routing-and-networking-protocols/mpls/vpls/control-word.md) article.</ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1">Bridge the VPLS interface belongs to.</ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1">Cost of the bridge port.</ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1">When set to `none`, bridge `horizon` is not used.</ArgTableRow>
<ArgTableRow arg="bridge-pvid" typ="num" unset="1">Port VLAN ID (pvid) assigned to a dynamically bridged interface. Applies only when bridge `vlan-filtering` is set to `yes`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="current-peers" typ="string"></ArgTableRow>
</ArgTable>
