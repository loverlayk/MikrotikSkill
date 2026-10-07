# advertise-filter

> RouterOS directory reference for /mpls/ldp/advertise-filter.

-----------

## mpls/ldp/advertise-filter 
**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum (any) { any:0xffffffff }" unset="1"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" unset="1">Prefix to match.</ArgTableRow>
<ArgTableRow arg="neighbor" typ="address (flags=46/)" unset="1">Neighbor to which this filter applies.</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool" unset="1">Whether to advertise label bindings to the neighbors for the specified prefix. If parameter is unset then matching prefix is not advertised.</ArgTableRow>
</ArgTable>
