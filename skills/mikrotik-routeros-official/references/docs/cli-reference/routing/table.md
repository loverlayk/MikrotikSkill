# table

> RouterOS directory reference for /routing/table.

-----------

## routing/table 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="U" typ="used">used</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the routing table.</ArgTableRow>
<ArgTableRow arg="fib" typ="switch" unset="1">Flag indicating whether routes in this table will be installed in the [FIB](../../user-guides/routing-and-networking-protocols/routing-decision.md#forwarding-information-base).</ArgTableRow>
</ArgTable>
