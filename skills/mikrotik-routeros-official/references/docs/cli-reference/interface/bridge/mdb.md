# mdb

> RouterOS directory reference for /interface/bridge/mdb.

-----------

## interface/bridge/mdb 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="group" typ="address (flags=46m)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="multi { array-id, interface: iface_enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vid" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="on-interface" typ="multi { array-id, interface: iface_enum
 }"></ArgTableRow>
</ArgTable>
