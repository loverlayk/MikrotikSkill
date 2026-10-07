# vlan

> RouterOS directory reference for /interface/ethernet/switch/vlan.

-----------

## interface/ethernet/switch/vlan 
**Syscap:** musicswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vlan-id" typ="num" mandatory="1">VLAN ID of the VLAN member entry.</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1">Member ports of the VLAN.</ArgTableRow>
<ArgTableRow arg="svl" typ="bool">
FDB lookup mode for lookup in UFDB and MFDB.
- `svl` - Shared VLAN Learning, learning/lookup is based on MAC addresses - not on VLAN IDs.
- `ivl` - Independent VLAN Learning, learning/lookup is based on both MAC addresses and VLAN IDs.
</ArgTableRow>
<ArgTableRow arg="learn" typ="bool">Enables or disables source MAC learning for VLAN.</ArgTableRow>
<ArgTableRow arg="flood" typ="bool">Enables or disables forced VLAN flooding per VLAN. If enabled, the result of the destination MAC lookup in the UFDB or MFDB is ignored, and the packet is forced to flood in the VLAN.</ArgTableRow>
<ArgTableRow arg="ingress-mirror" typ="bool">Enables the ingress mirror per VLAN to support the VLAN-based mirror function.</ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }">Defined QoS group from the QoS group menu.</ArgTableRow>
</ArgTable>

## interface/ethernet/switch/vlan 
**Syscap:** rbswitch and oldswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1">Name of the switch for which the respective VLAN entry is intended.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" mandatory="1">VLAN ID of the VLAN member entry.</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, port: enum
 }" mandatory="1">Member ports of the VLAN.</ArgTableRow>
<ArgTableRow arg="independent-learning" typ="bool">Whether to use shared-VLAN-learning (SVL) or independent-VLAN-learning (IVL).</ArgTableRow>
</ArgTable>
