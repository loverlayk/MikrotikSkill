# meter

> The sub-menu lists the traffic meters installed by the controller. Meters enable rate monitoring before output and applying action instructions.

-----------

## openflow/meter 
**Package:** openflow
**Type:** Directory

The sub-menu lists the traffic meters installed by the controller. Meters enable rate monitoring before output and applying action instructions.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum">Controller name that installed the meter.</ArgTableRow>
<ArgTableRow arg="id" typ="num">Identifier of the meter.</ArgTableRow>
<ArgTableRow arg="band-count" typ="num">Number of meter bands in the meter.</ArgTableRow>
<ArgTableRow arg="bands" typ="string">List of meter bands that define the rate and how packets are processed.</ArgTableRow>
<ArgTableRow arg="bytes" typ="num">Number of bytes processed by the meter.</ArgTableRow>
<ArgTableRow arg="packets" typ="num">Number of packets processed by the meter.</ArgTableRow>
<ArgTableRow arg="duration" typ="time">Time since the meter was installed.</ArgTableRow>
</ArgTable>
