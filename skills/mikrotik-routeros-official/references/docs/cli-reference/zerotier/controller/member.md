# member

> RouterOS directory reference for /zerotier/controller/member.

-----------

## zerotier/controller/member 
**Package:** zerotier
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">Whether the member is inactive.</ArgTableRow>
<ArgTableRow arg="A" typ="authorized">Whether the member is authorized.</ArgTableRow>
<ArgTableRow arg="B" typ="bridge">Whether the member acts as a bridge.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disabled" typ="bool">Whether an item is disabled.</ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the member.</ArgTableRow>
<ArgTableRow arg="network" typ="enum" mandatory="1">Network the member belongs to.</ArgTableRow>
<ArgTableRow arg="zt-address" typ="string" mandatory="1">ZeroTier address of the member.</ArgTableRow>
<ArgTableRow arg="authorized" typ="bool">Whether the member is authorized to join the network.</ArgTableRow>
<ArgTableRow arg="bridge" typ="bool">Whether the member acts as a bridge.</ArgTableRow>
<ArgTableRow arg="ip-address" typ="multi { array-id, addr: address (flags=46)
 }">IP address assigned to the member.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="lost" typ="bool">Whether the connection to the member is lost.</ArgTableRow>
<ArgTableRow arg="last-seen" typ="time">Time since the member was last seen.</ArgTableRow>
</ArgTable>
