# range

> RouterOS directory reference for /routing/ospf/area/range.

-----------

## routing/ospf/area/range 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="A" typ="advertise">advertise</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="area" typ="enum" mandatory="1">The OSPF area associated with this range.</ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" mandatory="1">The network prefix of this range.</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool">Whether to create a summary LSA and advertise it to the adjacent areas.</ArgTableRow>
<ArgTableRow arg="cost" typ="num" unset="1">The cost of the summary LSA this range will create. Default - use the largest cost of all routes used (i.e. routes that fall within this range).</ArgTableRow>
</ArgTable>
