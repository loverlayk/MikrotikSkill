# instance

> RouterOS directory reference for /routing/bgp/instance.

-----------

## routing/bgp/instance 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1">Name of the routing table, to install routes in.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF BGP connections operate on. By default always uses the "main" routing table.</ArgTableRow>
<ArgTableRow arg="router-id" typ="alt { ip: ipAddr
, name: enum
 }" unset="1">BGP Router ID to be used. Use the ID from the `/routing/router-id` configuration by specifying the reference name, or set the ID directly by specifying IP.Equal router-ids are also used to group peers into one instance.</ArgTableRow>
<ArgTableRow arg="as" typ="super { as: as
, [sub-as] [ /as]
 }" unset="1">32-bit BGP autonomous system number. Enter the value in AS-Plain or AS-Dot formats. Configure BGP confederation using the following format: _`confederation_as/as`_. For example, if your AS is 34 and your confederation AS is 43, set `as=43/34`.</ArgTableRow>
<ArgTableRow arg="cluster-id" typ="ipAddr" unset="1">For route reflector instances, specify the cluster ID of the route reflector cluster. This attribute identifies routing updates from other route reflectors in the cluster to avoid routing information loops. Typically, only one route reflector exists per cluster; in this case, do not configure 'cluster-id' and BGP router ID is used instead.</ArgTableRow>
<ArgTableRow arg="ignore-as-path-len" typ="bool" unset="1">Ignore the **AS_PATH** attribute in the BGP route selection algorithm. Applies to input.</ArgTableRow>
<ArgTableRow arg="multipath" typ="num" unset="1">Install the specified number of ECMP routes received by add-path or selected by [best path selection](../../../user-guides/routing-and-networking-protocols/unicast/bgp/understanding-bgp.md#best-path-selection).</ArgTableRow>
<ArgTableRow arg="always-compare-med" typ="bool" unset="1"></ArgTableRow>
</ArgTable>
