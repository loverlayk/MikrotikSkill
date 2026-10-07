# node

> Configuration for a specific node in a topology.

-----------

## cmr/layout/node 
**Package:** cmr
**Type:** Directory

Configuration for a specific node in a topology.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the node.</ArgTableRow>
<ArgTableRow arg="layout" typ="enum" mandatory="1">Name of the layout where the node will be displayed.</ArgTableRow>
<ArgTableRow arg="device" typ="enum" unset="1">Name of the device that the node will represent in the topology. Mutually exclusive with `target-layout` parameter.</ArgTableRow>
<ArgTableRow arg="target-layout" typ="enum" unset="1">Name of the layout that the node will represent in the topology. Mutually exclusive with `device` parameter.</ArgTableRow>
<ArgTableRow arg="x" typ="num" unset="1">X coordinate of the node in a topology. Default X value is incremented by 200 each time a new node is added, to prevent overlapping when no coordinates are specified. (default value: **0+200*n**)</ArgTableRow>
<ArgTableRow arg="y" typ="num" unset="1">Y coordinate of the node in a topology. (default value: **0**)</ArgTableRow>
</ArgTable>
