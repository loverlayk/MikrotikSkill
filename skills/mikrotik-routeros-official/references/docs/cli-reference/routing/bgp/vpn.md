# vpn

> L3VPN VPNv4/VPNv6 instance configuration

-----------

## routing/bgp/vpn 
**Conditions:** !smips
**Type:** Directory

L3VPN VPNv4/VPNv6 instance configuration

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" unset="1"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">Name of the instance this VPN is assigned to.</ArgTableRow>
<ArgTableRow arg="route-distinguisher" typ="string" mandatory="1">Specifies the value that gets attached to route so that receiving routers can distinguish advertisements that may otherwise look the same. Used to distinguish between tenants using overlapping IP ranges. Also can be used to simplify convergence and redundancy within Virtual Network. RDs from MLAG pairs should be unique, too.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" mandatory="1">Name of the VRF table that this VPN instance will use.</ArgTableRow>
<ArgTableRow arg="label-allocation-policy" typ="enum (per-vrf | per-prefix)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="import.route-targets" typ="object { route-target: address (flags=R)
 }" unset="1">List of route targets that will be used to import VPNv4 routes. The accepted RT format is similar to the one for Route Distinguishers.</ArgTableRow>
<ArgTableRow arg="export.route-targets" typ="object { route-target: address (flags=R)
 }" unset="1">List of route targets added when exporting VPNv4 routes. The accepted RT format is similar to the one for Route Distinguishers.</ArgTableRow>
<ArgTableRow arg="import.filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="export.filter-select" typ="enum" unset="1">The name of the `routing/filter/select-chain` that is used to select prefixes to be exported.</ArgTableRow>
<ArgTableRow arg="export.filter-chain" typ="enum" unset="1">The name of the `routing/filter/chain` that is used to filter prefixes before exporting.</ArgTableRow>
<ArgTableRow arg="export.redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, slaac)" unset="1">Enable redistribution of specified route types from a VRF to VPNv4.</ArgTableRow>
</ArgTable>
