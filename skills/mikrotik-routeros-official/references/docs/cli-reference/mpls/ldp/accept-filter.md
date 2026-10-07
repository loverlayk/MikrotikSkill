# accept-filter

> List of label bindings that should be accepted from LDP neighbors.

-----------

## mpls/ldp/accept-filter 
**Conditions:** !smips
**Type:** Directory

List of label bindings that should be accepted from LDP neighbors.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum (any) { any:0xffffffff }" unset="1"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" unset="1">Prefix to match.</ArgTableRow>
<ArgTableRow arg="neighbor" typ="address (flags=46/)" unset="1">Neighbor to which this filter applies.</ArgTableRow>
<ArgTableRow arg="accept" typ="bool" unset="1">Whether to accept label bindings from the neighbors for the specified prefix. If parameter is unset then matching prefix is not accepted.</ArgTableRow>
</ArgTable>
