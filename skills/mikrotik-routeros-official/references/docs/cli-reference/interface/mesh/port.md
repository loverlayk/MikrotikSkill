# port

> RouterOS directory reference for /interface/mesh/port.

-----------

## interface/mesh/port 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mesh" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="port-type" typ="enum (auto | WDS | wireless | ethernet) { auto:0, WDS:1, wireless:2, ethernet:3 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-port-type" typ="enum (wireless | WDS | ethernet-mesh | ethernet-bridge | ethernet-mixed) { wireless:1, WDS:2, ethernet-mesh:3, ethernet-bridge:4, ethernet-mixed:5 }"></ArgTableRow>
<ArgTableRow arg="dr-address" typ="macAddr"></ArgTableRow>
</ArgTable>
