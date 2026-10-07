# vlan

> RouterOS directory reference for /interface/bridge/vlan.

-----------

## interface/bridge/vlan 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="Y" typ="managed">managed</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vlan-ids" typ="multi { vlan-range: range [1 .. 4094]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="tagged" typ="multi { array-id, interface: alt { interface: iface_enum
, interface-list: enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="untagged" typ="multi { array-id, interface: alt { interface: iface_enum
, interface-list: enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="mvrp-forbidden" typ="multi { array-id, interface: alt { interface: iface_enum
, interface-list: enum
 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="current-tagged" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="current-untagged" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
</ArgTable>
