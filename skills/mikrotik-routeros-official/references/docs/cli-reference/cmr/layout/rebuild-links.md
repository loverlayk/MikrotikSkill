# rebuild-links

> If links between nodes in the topology were deleted or not generated initially, this command automatically generates them based on port data.

-----------

## cmr/layout/rebuild-links 
**Package:** cmr
**Type:** Command

If links between nodes in the topology were deleted or not generated initially, this command automatically generates them based on port data.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="labels" typ="object" unset="1">Select devices using labels for which links should be rebuilt. Supports + and - signs as AND and AND NOT operators, respectively; if no sign is provided, the OR operator is used. (default value: **all**)</ArgTableRow>
<ArgTableRow arg="devices" typ="multi { array-id, device: enum
 }" unset="1">Select specific devices for which links should be rebuilt.</ArgTableRow>
</ArgTable>
