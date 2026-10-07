# vlan

> Matches VLAN priorities (802.1p PCP/DEI fields) to QoS profiles. By default, all values are matched to the default QoS profile.

-----------

## interface/ethernet/switch/qos/map/vlan 
**Syscap:** rbswitch and crs_prestera
**Type:** Directory

Matches VLAN priorities (802.1p PCP/DEI fields) to QoS profiles. By default, all values are matched to the default QoS profile.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="map" typ="enum">The name of the mapping table.</ArgTableRow>
<ArgTableRow arg="pcp" typ="multi { pcp-range: range [0 .. 7]
 }" mandatory="1">VLAN priority (PCP) value(-s) for the lookup.</ArgTableRow>
<ArgTableRow arg="dei-only" typ="bool">Maps only packets with DEI (formerly CFI) bit set in the VLAN header.</ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1">The name of the QoS profile to assign to the matched packets.</ArgTableRow>
</ArgTable>
