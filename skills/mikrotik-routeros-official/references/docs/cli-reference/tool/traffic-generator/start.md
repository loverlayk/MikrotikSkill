# start

> RouterOS command reference for /tool/traffic-generator/start.

-----------

## tool/traffic-generator/start 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="test-id" typ="num"></ArgTableRow>
<ArgTableRow arg="measure-out-of-order" typ="bool"></ArgTableRow>
<ArgTableRow arg="cpu-core" typ="multi { array-id, array-id, cpu-core: range [0 .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="stream" typ="multi { stream: enum
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="multi { port: enum
 }"></ArgTableRow>
<ArgTableRow arg="interface" typ="multi { port: iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="id" typ="multi { id: num [0 .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="packet-size" typ="multi { array-id, array-id, packet-size: range [1 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="pps" typ="multi { pps: num
 }"></ArgTableRow>
<ArgTableRow arg="mbps" typ="multi { mbps: num
 }"></ArgTableRow>
<ArgTableRow arg="tx-template" typ="multi { tx-template: enum
 }"></ArgTableRow>
<ArgTableRow arg="packet-count" typ="multi { packet-count: num
 }"></ArgTableRow>
</ArgTable>
