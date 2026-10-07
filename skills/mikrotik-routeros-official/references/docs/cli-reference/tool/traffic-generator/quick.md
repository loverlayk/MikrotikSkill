# quick

> RouterOS command reference for /tool/traffic-generator/quick.

-----------

## tool/traffic-generator/quick 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="entries-to-show" typ="num"></ArgTableRow>
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

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="seq" typ="enum (TOT) { TOT:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="id" typ="enum (TOT) { TOT:0xffffffff }"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-ooo" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bad-csum" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-packet" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-ratio" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-min" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-avg" typ="string"></ArgTableRow>
<ArgTableRow arg="lat-max" typ="string"></ArgTableRow>
<ArgTableRow arg="jitter" typ="string"></ArgTableRow>
</ArgTable>
