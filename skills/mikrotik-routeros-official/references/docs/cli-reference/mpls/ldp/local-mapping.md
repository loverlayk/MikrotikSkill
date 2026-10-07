# local-mapping

> This sub-menu shows labels bound to the routes locally in the router. In this menu, static mappings can also be configured if there is no intention to use LDP dynamically.

-----------

## mpls/ldp/local-mapping 
**Conditions:** !smips
**Type:** Directory

This sub-menu shows labels bound to the routes locally in the router. In this menu, static mappings can also be configured if there is no intention to use LDP dynamically.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">Whether binding is active and can be selected as a candidate for forwarding.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Whether the entry was dynamically added.</ArgTableRow>
<ArgTableRow arg="E" typ="egress">egress</ArgTableRow>
<ArgTableRow arg="G" typ="gateway">Whether the destination is reachable through the gateway.</ArgTableRow>
<ArgTableRow arg="L" typ="local">Whether the destination is locally reachable on the router.</ArgTableRow>
<ArgTableRow arg="V" typ="vpls">vpls</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF table this mapping belongs to.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46/)" unset="1" mandatory="1">Destination prefix the label is assigned to.</ArgTableRow>
<ArgTableRow arg="label" typ="alt { label-enum: enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, label-num: num [16 .. 1048576]
 }" mandatory="1">Label number assigned to destination.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="adv-path" typ="string"></ArgTableRow>
<ArgTableRow arg="peers" typ="object { peer-id: composite { id: ipAddr
, namespace: num
 }
 }">IP address and label space of the peer to which this entry was advertised.</ArgTableRow>
<ArgTableRow arg="pw-fec" typ="string"></ArgTableRow>
</ArgTable>
