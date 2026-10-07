# evpn

> See EVPN documentation.

-----------

## routing/bgp/evpn 
**Conditions:** !smips
**Type:** Directory

See EVPN documentation.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">BGP instance this EVPN is assigned to.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF table that this EVPN instance will use.</ArgTableRow>
<ArgTableRow arg="rd" typ="address (flags=R)" unset="1">Specifies the value that gets attached to route so that receiving routers can distinguish advertisements that may otherwise look the same. Used to distinguish between tenants using overlapping IP ranges. Also can be used to simplify convergence and redundancy within Virtual Network. RDs from MLAG pairs should be unique, too.</ArgTableRow>
<ArgTableRow arg="vni" typ="object { range: range
 }" unset="1">Range of Virtual Network Identifiers.</ArgTableRow>
<ArgTableRow arg="import.route-targets" typ="object { route-target: address (flags=R)
 }" unset="1">List of route targets that will be used to import EVPN routes.</ArgTableRow>
<ArgTableRow arg="export.route-targets" typ="object { route-target: address (flags=R)
 }" unset="1">List of route targets that will be added to EVPN routes when exporting.</ArgTableRow>
</ArgTable>
