# raw-packet-template

> RouterOS directory reference for /tool/traffic-generator/raw-packet-template.

-----------

## tool/traffic-generator/raw-packet-template 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="enum"></ArgTableRow>
<ArgTableRow arg="header" typ="string"></ArgTableRow>
<ArgTableRow arg="data" typ="enum (uninitialized | random | specific-byte | incrementing) { uninitialized:0, random:1, specific-byte:2, incrementing:3 }"></ArgTableRow>
<ArgTableRow arg="data-byte" typ="num"></ArgTableRow>
<ArgTableRow arg="random-byte-offsets-and-masks" typ="multi { array-id, array-id, offset-and-mask: composite { offset: num [ .. 256]
, mask: num [ .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="random-ranges" typ="object { random-range: super { offset: num [ .. 256]
, [width] :enum (8 | 16 | 32) { 8:8, 16:16, 32:32 }
, [range] :range
 }
 }"></ArgTableRow>
<ArgTableRow arg="ip-header-offset" typ="multi { ip-header-offset: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ipv6-header-offset" typ="multi { ipv6-header-offset: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="udp-header-offset" typ="multi { udp-header-offset: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="udp-compute-checksum" typ="multi { udp-compute-checksum: bool
 }"></ArgTableRow>
<ArgTableRow arg="tcp-header-offset" typ="multi { tcp-header-offset: num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="special-footer" typ="bool"></ArgTableRow>
<ArgTableRow arg="compute-checksum-from-offset" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="header-length" typ="num"></ArgTableRow>
</ArgTable>
