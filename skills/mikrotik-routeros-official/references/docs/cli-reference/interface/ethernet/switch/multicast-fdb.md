# multicast-fdb

> CRS125 switch-chip supports up to 1024 entries in the MFDB for multicast forwarding. For each multicast packet, destination MAC or destination IP lookup is performed in the MFDB. MFDB entries are not automatically...

-----------

## interface/ethernet/switch/multicast-fdb 
**Syscap:** musicswitch
**Type:** Directory

CRS125 switch-chip supports up to 1024 entries in the MFDB for multicast forwarding. For each multicast packet, destination MAC or destination IP lookup is performed in the MFDB. MFDB entries are not automatically learned and can only be configured.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="alt { mac-address: macAddr
, ip-address: ipAddr
 }" mandatory="1">Matching IP address or MAC address for multicast packets.</ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id }" mandatory="1">Member ports for multicast traffic.</ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num">Multicast FDB lookup VLAN ID. If the VLAN learning mode is IVL, VLAN id is lookup id, otherwise VLAN id = 0.</ArgTableRow>
<ArgTableRow arg="svl" typ="bool">
Multicast FDB learning mode.
- `svl` - Shared VLAN Learning, learning/lookup is based on MAC addresses - not on VLAN IDs.
- `ivl` - Independent VLAN Learning, learning/lookup is based on both MAC addresses and VLAN IDs.
</ArgTableRow>
<ArgTableRow arg="bypass-vlan-filter" typ="bool">Allows bypassing VLAN filtering for matching multicast packets.</ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none) { none:0xffffffff }">Defined QoS group from QoS group menu.</ArgTableRow>
</ArgTable>
