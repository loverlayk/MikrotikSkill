# stream

> RouterOS directory reference for /tool/traffic-generator/stream.

-----------

## tool/traffic-generator/stream 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="id" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-size" typ="range"></ArgTableRow>
<ArgTableRow arg="pps" typ="num"></ArgTableRow>
<ArgTableRow arg="mbps" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-count" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-core" typ="range"></ArgTableRow>
<ArgTableRow arg="tx-template" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-port" typ="enum"></ArgTableRow>
</ArgTable>
