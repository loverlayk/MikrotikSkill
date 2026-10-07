# remote-mapping

> The Sub-menu shows label bindings for routes received from other routers. Static mapping can be configured if there is no intention to use LDP dynamically. This table is used to build the Forwarding Table

-----------

## mpls/ldp/remote-mapping 
**Conditions:** !smips
**Type:** Directory

The Sub-menu shows label bindings for routes received from other routers. Static mapping can be configured if there is no intention to use LDP dynamically. This table is used to build the Forwarding Table

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">Whether binding is active and can be selected as a candidate for forwarding.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Whether entry was dynamically added.</ArgTableRow>
<ArgTableRow arg="V" typ="vpls">vpls</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF table this mapping belongs to.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46/)" mandatory="1">Destination prefix the label is assigned to.</ArgTableRow>
<ArgTableRow arg="label" typ="alt { label-enum: enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, label-num: num [16 .. 1048576]
 }" mandatory="1">Label number assigned to destination.</ArgTableRow>
<ArgTableRow arg="nexthop" typ="address (flags=46i)" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="object { peer-id: composite { id: ipAddr
, namespace: num
 }
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="string"></ArgTableRow>
<ArgTableRow arg="pw-fec" typ="string"></ArgTableRow>
</ArgTable>
